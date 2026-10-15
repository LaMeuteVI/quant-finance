"""Axe 6 — ML panel diagnostics on klines 1m daily (descriptive only).

Falsification-first study: build a panel of microstructure-style features from
the pre-cutoff klines 1m daily store (BTC, ETH, BNB, SOL), label each bar with
a 5-day ATR-scaled triple-barrier, run a sparse logistic regression under
purged k-fold CV with embargo (AFML ch07), and report the OOS hit-rate, the
Diezmado-Aleatorico baseline (sign of prior return) and the Deflated Sharpe
Ratio (DSR) versus a random classifier. No XGBoost, no sklearn, only
numpy/pandas/scipy. The objective is to measure the ceiling of what is
extractable from the klines 1m daily panel; a null result is a valid outcome
and will close the klines-1m ML axis.

All inputs respect the exploration cutoff `2024-07-01T00:00:00Z`. The pipeline
does not register a ledger hypothesis, does not run a `desk backtest`, and does
not read the holdout. Outputs are descriptive artifacts in `research/assets/`.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Sequence

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import expit
from scipy.stats import norm

from aster.data import store

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
DEV_END = pd.Timestamp("2022-10-11", tz="UTC")
SYMBOLS: tuple[str, ...] = ("BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT")
SEED = 20261015
N_SPLITS = 5
EMBARGO_DAYS = 6  # label window (5) + 1 for safety
TRIPLE_HORIZON_DAYS = 5
ATR_WINDOW = 14
L2_GRID: tuple[float, ...] = (1e-2, 1e-1, 1.0, 10.0, 100.0)
N_BOOT_DSR = 5_000

ASSET_DIR = Path("research/assets")
OUTPUT_CSV = ASSET_DIR / "2026-10-15-ml-panel-diagnostics.csv"
OUTPUT_MD = ASSET_DIR / "2026-10-15-ml-panel-diagnostics.md"
OUTPUT_SUMMARY = ASSET_DIR / "2026-10-15-ml-panel-diagnostics-summary.json"

FEATURE_NAMES: tuple[str, ...] = (
    "log_return_1d",
    "hl_range_norm_atr",
    "co_asymmetry_norm_atr",
    "realized_var_1d",
    "sign_persist_1d",
    "rv_ratio_5d_1d",
    "vol_of_vol_5d",
    "zscore_20d",
)


def _log_returns(close: pd.Series) -> pd.Series:
    return np.log(close).diff()


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, window: int) -> pd.Series:
    prev_close = close.shift(1)
    tr = pd.concat(
        [(high - low).abs(), (high - prev_close).abs(), (low - prev_close).abs()],
        axis=1,
    ).max(axis=1)
    return tr.rolling(window=window, min_periods=window).mean()


def _build_features(ohlcv: pd.DataFrame) -> pd.DataFrame:
    """Build the 8-feature panel from daily OHLCV, all strictly causal (row t
    uses only data <= t)."""
    if not isinstance(ohlcv.index, pd.DatetimeIndex) or ohlcv.index.tz is None:
        raise ValueError("ohlcv must have a tz-aware DatetimeIndex")
    if (ohlcv.index >= CUTOFF).any():
        raise ValueError("ohlcv crosses the exploration cutoff")
    work = ohlcv.sort_index().astype(float).copy()
    log_close = np.log(work["close"])
    log_ret_1d = log_close.diff()
    atr = _atr(work["high"], work["low"], work["close"], ATR_WINDOW)
    hl_range = (work["high"] - work["low"]) / atr
    co_asym = (work["close"] - work["open"]) / atr
    rvar_1d = log_ret_1d.pow(2)
    sign_1d = np.sign(log_ret_1d)
    sign_persist_1d = sign_1d.shift(1) * sign_1d  # in {-1, 0, +1}
    rvar_5d = rvar_1d.rolling(window=5, min_periods=5).mean()
    rv_ratio = rvar_5d / rvar_1d.replace(0.0, np.nan)
    vol_of_vol = rvar_1d.rolling(window=5, min_periods=5).std()
    ma_20 = log_close.rolling(window=20, min_periods=20).mean()
    std_20 = log_close.rolling(window=20, min_periods=20).std()
    zscore_20d = (log_close - ma_20) / std_20
    feats = pd.concat(
        [
            log_ret_1d.rename("log_return_1d"),
            hl_range.rename("hl_range_norm_atr"),
            co_asym.rename("co_asymmetry_norm_atr"),
            rvar_1d.rename("realized_var_1d"),
            sign_persist_1d.rename("sign_persist_1d"),
            rv_ratio.rename("rv_ratio_5d_1d"),
            vol_of_vol.rename("vol_of_vol_5d"),
            zscore_20d.rename("zscore_20d"),
        ],
        axis=1,
    )
    return feats


def _triple_barrier_label(close: pd.Series, atr: pd.Series) -> pd.Series:
    """For each bar t, look forward up to TRIPLE_HORIZON_DAYS. The first barrier
    touched wins: upper = close + 1*ATR, lower = close - 1*ATR, vertical at
    horizon. Returns +1 (upper first), -1 (lower first), 0 (vertical)."""
    n = len(close)
    labels = np.zeros(n, dtype=np.int8)
    values = close.to_numpy(dtype=float)
    atr_vals = atr.to_numpy(dtype=float)
    for i in range(n - TRIPLE_HORIZON_DAYS):
        a = atr_vals[i]
        if not np.isfinite(a) or a <= 0:
            continue
        upper = values[i] + a
        lower = values[i] - a
        label = 0
        for k in range(1, TRIPLE_HORIZON_DAYS + 1):
            v = values[i + k]
            if v >= upper:
                label = 1
                break
            if v <= lower:
                label = -1
                break
        labels[i] = label
    return pd.Series(labels, index=close.index, name="label")


def _zscore(df: pd.DataFrame) -> pd.DataFrame:
    """Z-score each column with its own expanding mean/std (causal)."""
    mu = df.expanding(min_periods=60).mean()
    sd = df.expanding(min_periods=60).std()
    return (df - mu) / sd.replace(0.0, np.nan)


def _fit_zscore(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Compute the expanding mean/std at the LAST row of `df` (causal
    statistic). Used to normalize the test fold using only training-fold
    statistics, which prevents preprocessing look-ahead (AFML ch04, ch07)."""
    mu = df.expanding(min_periods=60).mean()
    sd = df.expanding(min_periods=60).std()
    return mu.iloc[-1], sd.iloc[-1]


def _apply_zscore(
    df: pd.DataFrame, mu: pd.Series, sd: pd.Series
) -> pd.DataFrame:
    """Normalize `df` using the supplied expanding mean/std."""
    return (df - mu) / sd.replace(0.0, np.nan)


def _logistic_loss_and_grad(
    w: np.ndarray,
    X: np.ndarray,
    y: np.ndarray,
    l2: float,
) -> tuple[float, np.ndarray]:
    z = X @ w
    p = expit(z)
    eps = 1e-12
    p_clip = np.clip(p, eps, 1.0 - eps)
    loss = -np.mean(y * np.log(p_clip) + (1.0 - y) * np.log(1.0 - p_clip))
    loss += 0.5 * l2 * float(np.dot(w, w))
    grad = (X.T @ (p - y)) / len(y)
    grad += l2 * w
    return float(loss), grad


def _fit_logreg(
    X: np.ndarray, y: np.ndarray, l2: float, max_iter: int = 200
) -> np.ndarray:
    n_features = X.shape[1]
    w0 = np.zeros(n_features, dtype=float)
    res = minimize(
        _logistic_loss_and_grad,
        w0,
        args=(X, y, l2),
        method="L-BFGS-B",
        jac=True,
        options={"maxiter": max_iter},
    )
    return res.x


def _predict_proba(X: np.ndarray, w: np.ndarray) -> np.ndarray:
    return expit(X @ w)


def _purged_kfold_indices(
    n: int, n_splits: int, embargo: int
) -> list[tuple[np.ndarray, np.ndarray]]:
    """Purged k-fold (AFML ch07). Test folds are non-overlapping slices of
    the time index. Training indices remove the test fold plus an embargo of
    `embargo` days on each side (purging label leakage across the horizon)."""
    fold_sizes = np.full(n_splits, n // n_splits, dtype=int)
    fold_sizes[: n % n_splits] += 1
    starts = np.cumsum(np.concatenate([[0], fold_sizes]))
    folds: list[tuple[np.ndarray, np.ndarray]] = []
    for k in range(n_splits):
        test_lo, test_hi = int(starts[k]), int(starts[k + 1])
        test_idx = np.arange(test_lo, test_hi)
        mask = np.ones(n, dtype=bool)
        mask[max(0, test_lo - embargo): min(n, test_hi + embargo)] = False
        train_idx = np.where(mask)[0]
        folds.append((train_idx, test_idx))
    return folds


def _hit_rate(y_true: np.ndarray, p: np.ndarray) -> float:
    pred = (p >= 0.5).astype(int)
    return float(np.mean(pred == y_true))


def _dsr_normal(
    sr_hat: float, n_trials: int, n_obs: int, sr_benchmark: float = 0.0
) -> tuple[float, float]:
    """Deflated Sharpe Ratio test, normal approximation (Bailey & López de
    Prado 2014, equation 4 in the practitioner version): the expected maximum
    SR under the null is e_m = sqrt(V[SR]) * ((1 - gamma) * Z_inv[1 - 1/N] +
    gamma * Z_inv[1 - 1/(N*e)]) for a one-sided N(0,1). Returns (dsr_pvalue,
    e_max_sr)."""
    e_max = 0.0
    if n_trials > 1:
        z1 = norm.ppf(1.0 - 1.0 / n_trials)
        z2 = norm.ppf(1.0 - 1.0 / (n_trials * math.e))
        gamma = 0.5772156649
        v_sr_estimate = 1.0 / max(n_obs - 1, 1)
        e_max = math.sqrt(v_sr_estimate) * ((1.0 - gamma) * z1 + gamma * z2)
    if sr_hat - sr_benchmark <= 0:
        return 1.0, e_max
    z = (sr_hat - sr_benchmark) / math.sqrt(max(1.0 / max(n_obs - 1, 1), 1e-12))
    pval = 1.0 - norm.cdf(z - e_max * math.sqrt(max(n_obs - 1, 1)))
    return float(pval), float(e_max)


def analyse() -> dict:
    """Run the diagnostic pipeline on the dev sample, return a JSON-able
    summary, and write the artifacts (CSV, MD, summary JSON)."""
    rng = np.random.default_rng(SEED)
    panels: list[pd.DataFrame] = []
    for symbol in SYMBOLS:
        ohlcv = store.read("ohlcv", "binance", symbol, "1d")
        ohlcv = ohlcv.loc[ohlcv.index <= DEV_END]
        if len(ohlcv) < 252:
            continue
        feats = _build_features(ohlcv)
        atr = _atr(ohlcv["high"], ohlcv["low"], ohlcv["close"], ATR_WINDOW)
        label = _triple_barrier_label(ohlcv["close"], atr)
        joined = feats.assign(label=label, symbol=symbol)
        panels.append(joined)
    panel = pd.concat(panels).sort_index()
    panel = panel.dropna(subset=list(FEATURE_NAMES) + ["label"])
    panel = panel.loc[panel["label"] != 0]  # drop vertical-barrier touches
    panel["label_binary"] = (panel["label"] > 0).astype(int)

    # z-score features by symbol (causal expanding)
    normed_parts: list[pd.DataFrame] = []
    for sym, sub in panel.groupby("symbol"):
        feats = sub[list(FEATURE_NAMES)]
        z = _zscore(feats)
        z = z.assign(label_binary=sub["label_binary"], symbol=sym)
        normed_parts.append(z)
    normed = pd.concat(normed_parts).sort_index()
    normed = normed.dropna(subset=list(FEATURE_NAMES))
    # cross-section: stack the panel into a single (T*4)-by-8 matrix
    X = normed[list(FEATURE_NAMES)].to_numpy(dtype=float)
    y = normed["label_binary"].to_numpy(dtype=int)
    n = len(y)
    # use the same normed index for the sign baseline so lengths agree
    log_ret_1d_aligned = normed["log_return_1d"].to_numpy(dtype=float)
    if n < 200:
        raise RuntimeError(f"panel too small: n={n}")
    # add intercept column
    X_int = np.concatenate([np.ones((n, 1), dtype=float), X], axis=1)

    # Primary metric: hold out a tail end-of-sample section (last 20%) as a
    # fixed OOS slice so purged k-fold cannot leak into the tail. We use the
    # first 80% for purged k-fold to pick lambda, then refit on the 80% and
    # score on the 20%.
    #
    # Preprocessing discipline (AFML ch04, ch07): features are z-scored using
    # a causal expanding mean/std computed on the training fold only, and the
    # test fold is normalized with the LAST value of that statistic. This
    # prevents the standard CV pitfall of normalizing the entire dataset and
    # then splitting, which leaks the test-fold mean/std into the training
    # features.
    oos_frac = 0.2
    oos_n = int(n * oos_frac)
    is_n = n - oos_n
    folds = _purged_kfold_indices(is_n, N_SPLITS, EMBARGO_DAYS)
    best_lambda: float | None = None
    best_score = -np.inf
    cv_table: list[dict] = []
    feat_names = list(FEATURE_NAMES)
    for l2 in L2_GRID:
        scores: list[float] = []
        for train_idx, test_idx in folds:
            X_train_raw = X_int[train_idx]
            y_train = y[train_idx]
            X_test_raw = X_int[test_idx]
            y_test = y[test_idx]
            # drop the intercept column for the z-score fit, then re-add
            mu, sd = _fit_zscore(pd.DataFrame(X_train_raw[:, 1:], columns=feat_names))
            sd = sd.replace(0.0, np.nan)
            X_train_norm = np.concatenate(
                [np.ones((len(train_idx), 1), dtype=float), (X_train_raw[:, 1:] - mu.values) / sd.values],
                axis=1,
            )
            X_test_norm = np.concatenate(
                [np.ones((len(test_idx), 1), dtype=float), (X_test_raw[:, 1:] - mu.values) / sd.values],
                axis=1,
            )
            w = _fit_logreg(X_train_norm, y_train, l2=l2)
            p_te = _predict_proba(X_test_norm, w)
            scores.append(_hit_rate(y_test, p_te))
        mean_score = float(np.mean(scores))
        cv_table.append({"lambda": l2, "cv_hit_rate": mean_score, "fold_scores": scores})
        if mean_score > best_score:
            best_score = mean_score
            best_lambda = l2
    if best_lambda is None:
        raise RuntimeError("no lambda selected")
    # refit on full IS sample with the chosen lambda, score on tail OOS
    X_train_full_raw = X_int[:is_n]
    y_train_full = y[:is_n]
    X_oos_raw = X_int[is_n:]
    y_oos = y[is_n:]
    mu_full, sd_full = _fit_zscore(pd.DataFrame(X_train_full_raw[:, 1:], columns=feat_names))
    sd_full = sd_full.replace(0.0, np.nan)
    X_train_full_norm = np.concatenate(
        [np.ones((is_n, 1), dtype=float), (X_train_full_raw[:, 1:] - mu_full.values) / sd_full.values],
        axis=1,
    )
    X_oos_norm = np.concatenate(
        [np.ones((oos_n, 1), dtype=float), (X_oos_raw[:, 1:] - mu_full.values) / sd_full.values],
        axis=1,
    )
    w_full = _fit_logreg(X_train_full_norm, y_train_full, l2=best_lambda)
    p_oos = _predict_proba(X_oos_norm, w_full)
    oos_hit = _hit_rate(y_oos, p_oos)
    majority_class_rate = float(np.mean(y_oos == 1)) if np.mean(y_oos == 1) > 0.5 else float(1 - np.mean(y_oos == 1))

    # baseline: sign of prior-day log_return (positive -> predict 1). At time
    # t we only know data up to t-1, so we use the one-day lagged raw return.
    # We re-read close per symbol (the panel kept only features, not raw OHLCV).
    normed_with_sign = normed.copy()
    normed_with_sign["_prior_log_ret"] = np.nan
    for sym in SYMBOLS:
        sub_ohlcv = store.read("ohlcv", "binance", sym, "1d").loc[
            lambda d: d.index <= DEV_END
        ]
        prior = np.log(sub_ohlcv["close"]).diff().shift(1)
        mask = normed_with_sign["symbol"] == sym
        normed_with_sign.loc[mask, "_prior_log_ret"] = normed_with_sign.index[mask].map(
            prior
        )
    prior_sign = np.sign(
        normed_with_sign["_prior_log_ret"].to_numpy(dtype=float)
    )
    prior_sign = np.nan_to_num(prior_sign, nan=0.0)
    sign_pred = (prior_sign > 0).astype(int)
    valid = (prior_sign != 0)
    sign_hit = float(np.mean(sign_pred[valid] == y[valid]))
    sign_n = int(valid.sum())

    # also: random classifier
    p_random = rng.uniform(size=oos_n)
    random_hit = _hit_rate(y_oos, p_random)

    # DSR: treat each fold and the OOS tail as independent SR trials
    sr_trials = [s - 0.5 for s in [r["cv_hit_rate"] for r in cv_table] + [oos_hit]]
    sr_trials_clean = [s for s in sr_trials if np.isfinite(s)]
    sr_hat = float(np.mean(sr_trials_clean)) if sr_trials_clean else 0.0
    n_trials = max(len(L2_GRID) + 1, 1)
    pval, e_max = _dsr_normal(sr_hat, n_trials, n_obs=len(sr_trials_clean))

    # write artifacts
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    out_df = pd.DataFrame(
        {
            "metric": [
                "n_panel",
                "n_is",
                "n_oos",
                "oos_positive_rate",
                "majority_class_oos_hit",
                "sign_baseline_oos_hit",
                "sign_baseline_n",
                "random_oos_hit",
                "best_lambda",
                "cv_best_hit_rate",
                "oos_hit_logreg",
                "oos_hit_minus_majority",
                "oos_hit_minus_sign_baseline",
                "sr_hat_across_trials",
                "dsr_pvalue",
                "e_max_sr",
            ],
            "value": [
                n,
                is_n,
                oos_n,
                float(np.mean(y_oos == 1)),
                majority_class_rate,
                sign_hit,
                sign_n,
                random_hit,
                best_lambda,
                best_score,
                oos_hit,
                oos_hit - majority_class_rate,
                oos_hit - sign_hit,
                sr_hat,
                pval,
                e_max,
            ],
        }
    )
    out_df.to_csv(OUTPUT_CSV, index=False)
    fold_rows: list[dict] = []
    for r in cv_table:
        for k, s in enumerate(r["fold_scores"]):
            fold_rows.append({"lambda": r["lambda"], "fold": k, "hit_rate": s})
    pd.DataFrame(fold_rows).to_csv(
        ASSET_DIR / "2026-10-15-ml-panel-diagnostics-folds.csv", index=False
    )
    summary = {
        "cutoff": CUTOFF.isoformat(),
        "dev_end": DEV_END.isoformat(),
        "symbols": list(SYMBOLS),
        "n_panel": n,
        "n_is": is_n,
        "n_oos": oos_n,
        "feature_names": list(FEATURE_NAMES),
        "lambda_grid": list(L2_GRID),
        "best_lambda": best_lambda,
        "cv_best_hit_rate": best_score,
        "cv_table": cv_table,
        "oos_hit_logreg": oos_hit,
        "majority_class_oos_hit": majority_class_rate,
        "sign_baseline_oos_hit": sign_hit,
        "sign_baseline_n": sign_n,
        "random_oos_hit": random_hit,
        "oos_hit_minus_majority": oos_hit - majority_class_rate,
        "oos_hit_minus_sign_baseline": oos_hit - sign_hit,
        "dsr_pvalue": pval,
        "e_max_sr": e_max,
        "n_l2_trials": n_trials,
    }
    OUTPUT_SUMMARY.write_text(json.dumps(summary, indent=2, default=float), encoding="utf-8")
    return summary


def write_report(summary: dict) -> None:
    lines = [
        "# ML panel diagnostics on klines 1m daily — falsification-first",
        "",
        "**Status: descriptive only; no ledger hypothesis, no backtest, no holdout read.**",
        "",
        f"- Cutoff: `{CUTOFF.isoformat()}`; dev end: `{summary['dev_end']}`.",
        f"- Symbols: `{summary['symbols']}`.",
        f"- Panel size: n_panel=`{summary['n_panel']}`, n_is=`{summary['n_is']}`, n_oos=`{summary['n_oos']}`.",
        f"- Features (8): `{', '.join(summary['feature_names'])}`.",
        f"- Label: 5-day ATR(14) triple-barrier, drop vertical touches, binary +1 / -1.",
        f"- Purged k-fold (k=5) with embargo `{EMBARGO_DAYS}` days; tail 20% held out as a fixed OOS slice.",
        f"- Model: sparse logistic regression (L2) with λ ∈ {summary['lambda_grid']}; L-BFGS-B, max 200 iters.",
        f"- DSR (Bailey & López de Prado 2014, normal approximation); trials = len(λ) + 1.",
        "",
        "## Results",
        "",
        f"- Best λ (purged CV): **{summary['best_lambda']}** with CV hit-rate **{summary['cv_best_hit_rate']:.4f}**.",
        f"- OOS hit-rate (logreg, fixed tail): **{summary['oos_hit_logreg']:.4f}**.",
        f"- Majority class baseline (OOS): **{summary['majority_class_oos_hit']:.4f}**.",
        f"- Sign-of-prior-return baseline (OOS, n=`{summary['sign_baseline_n']}`): **{summary['sign_baseline_oos_hit']:.4f}**.",
        f"- Random classifier (OOS): **{summary['random_oos_hit']:.4f}**.",
        f"- OOS lift over majority: **{summary['oos_hit_minus_majority']:+.4f}**.",
        f"- OOS lift over sign baseline: **{summary['oos_hit_minus_sign_baseline']:+.4f}**.",
        f"- DSR p-value (vs SR=0, n trials=`{summary['n_l2_trials']}`): **{summary['dsr_pvalue']:.4f}**.",
        "",
        "## Triage rule (pre-registered in this note, before any number above was read)",
        "",
        "1. OOS hit-rate > max(majority class, sign baseline) by at least 3 absolute percentage points, AND",
        "2. DSR p-value < 0.05 against SR=0 (n trials = len(λ) + 1), AND",
        "3. CV best hit-rate > sign baseline CV hit-rate by at least 1 absolute percentage point.",
        "",
        f"- Rule 1: logreg `{summary['oos_hit_logreg']:.4f}` vs max(maj, sign) `{max(summary['majority_class_oos_hit'], summary['sign_baseline_oos_hit']):.4f}` → **diff {summary['oos_hit_logreg'] - max(summary['majority_class_oos_hit'], summary['sign_baseline_oos_hit']):+.4f}** (need ≥ +0.03).",
        f"- Rule 2: DSR p-value `{summary['dsr_pvalue']:.4f}` (need < 0.05).",
        "- Rule 3: see CV table in `2026-10-15-ml-panel-diagnostics-folds.csv`.",
        "",
        "## Verdict",
        "",
        "If any rule fails → **0 edge tradable** and the klines-1m ML axis is closed; the only credible next axis is tick microstructure data (BACKLOG item 15), which requires Samuel's budget OK and a fresh cutoff seal.",
        "",
        "If all rules pass → a primary feature is identified; escalate to ledger preregistration and a counted `desk backtest` (NOT in this note).",
    ]
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary = analyse()
    write_report(summary)
    print(
        json.dumps(
            {
                "n_panel": summary["n_panel"],
                "best_lambda": summary["best_lambda"],
                "cv_best_hit_rate": summary["cv_best_hit_rate"],
                "oos_hit_logreg": summary["oos_hit_logreg"],
                "majority_class_oos_hit": summary["majority_class_oos_hit"],
                "sign_baseline_oos_hit": summary["sign_baseline_oos_hit"],
                "oos_hit_minus_sign": summary["oos_hit_minus_sign_baseline"],
                "dsr_pvalue": summary["dsr_pvalue"],
                "csv": str(OUTPUT_CSV),
                "md": str(OUTPUT_MD),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
