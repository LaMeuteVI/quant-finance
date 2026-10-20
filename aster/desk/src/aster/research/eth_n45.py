"""BTC N4/N5 descriptive study: regimes and kline flow proxies, pre-cutoff only.

The protocol is fixed in ``research/2026-10-14-btc-n4-n5-prereg.md``.  This
module never calls the backtest pipeline, never reads the sealed holdout, and
never registers a hypothesis.  Its sole output is a causal mapping of kline
flow features across volatility/trend regimes.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from aster.data import bars as bar_tools
from aster.data import r2_klines

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SYMBOL = "ETHUSDT"
DAILY_HORIZONS = (1, 2, 5)
FEATURE_FRAMES = ("1m", "15m", "1h")
BOOTSTRAPS = 5_000
RNG_SEED = 20261014
REGIME_LABEL = Path("research/assets/2026-10-14-eth-n4-regimes.md")
FLOW_REPORT = Path("research/assets/2026-10-14-eth-n5-flow.md")
FLOW_CSV = Path("research/assets/2026-10-14-eth-n5-flow.csv")
REGIME_CSV = Path("research/assets/2026-10-14-eth-n4-regimes.csv")


@dataclass(frozen=True)
class DayFrame:
    day: pd.Timestamp
    log_return: float
    fwd_returns: dict[int, float]
    regime_trend: int
    regime_vol: int
    imbalance: float
    signed_dollar: float
    volume_z: float
    trades_z: float
    roll_spread: float
    amihud: float
    n_active_minutes: int


def _active_minute_returns(minutes: pd.DataFrame) -> pd.DataFrame:
    active = minutes[(minutes["trades"] > 0) & (minutes["close"] > 0)].sort_index().copy()
    delta = active.index.to_series().diff()
    valid = delta == pd.Timedelta(minutes=1)
    log_price = np.log(active["close"])
    ret = log_price.diff().where(valid)
    out = pd.DataFrame(
        {
            "log_return": ret,
            "volume": active["volume"],
            "quote_volume": active["quote_volume"],
            "taker_buy_base": active["taker_buy_base"],
            "taker_buy_quote": active["taker_buy_quote"],
            "trades": active["trades"],
        },
        index=active.index,
    )
    return out.dropna(subset=["log_return"])


def _daily_directional_features(minutes: pd.DataFrame) -> pd.DataFrame:
    returns = _active_minute_returns(minutes)
    if returns.empty:
        raise ValueError("no active minute returns to build features")
    day = returns.index.normalize()
    imbalance = (2.0 * returns["taker_buy_base"] / returns["volume"] - 1.0).rename("imbalance")
    signed = (2.0 * returns["taker_buy_quote"] - returns["quote_volume"]).rename("signed_dollar")
    group = pd.concat(
        [
            imbalance,
            signed,
            returns["log_return"].abs().rename("abs_log_return"),
            returns["quote_volume"].rename("quote_volume"),
            returns["trades"].rename("trades"),
        ],
        axis=1,
    ).groupby(day)
    imbalance_mean = group["imbalance"].mean()
    signed_dollar = group["signed_dollar"].sum(min_count=1)
    amihud = (group["abs_log_return"].sum() / group["quote_volume"].sum() * 1e6).rename("amihud")
    active = group.size().rename("active_minutes")
    return pd.concat([imbalance_mean, signed_dollar, amihud, active], axis=1).rename_axis("day")


def _daily_roll_spread(minutes: pd.DataFrame) -> pd.Series:
    returns = _active_minute_returns(minutes)
    if returns.empty:
        return pd.Series(dtype=float)
    delta = returns["log_return"]
    cov = delta.groupby(delta.index.normalize()).apply(
        lambda x: x.cov(x.shift(1))
    )
    roll = (2.0 * np.sqrt((-cov).clip(lower=0.0))).rename("roll_spread")
    return roll


def _build_daily_features(minutes: pd.DataFrame, daily: pd.DataFrame) -> pd.DataFrame:
    flow = _daily_directional_features(minutes)
    roll = _daily_roll_spread(minutes)
    out = daily.join(flow, how="left").join(roll, how="left")
    if out.empty:
        raise ValueError("empty daily feature frame")
    out["imbalance"] = out["imbalance"].fillna(0.0)
    out["signed_dollar"] = out["signed_dollar"].fillna(0.0)
    out["amihud"] = out["amihud"].fillna(out["amihud"].median() if out["amihud"].notna().any() else 0.0)
    out["roll_spread"] = out["roll_spread"].fillna(out["roll_spread"].median() if out["roll_spread"].notna().any() else 0.0)
    out["log_return"] = np.log(out["close"]).diff()
    for h in DAILY_HORIZONS:
        out[f"fwd_{h}d"] = np.log(out["close"]).shift(-h) - np.log(out["close"])
    out = out.dropna(subset=["log_return"])
    return out


def _regime_labels(features: pd.DataFrame) -> pd.DataFrame:
    roll5 = np.log(features["close"]).rolling(5, min_periods=5).mean()
    roll22 = np.log(features["close"]).rolling(22, min_periods=22).mean()
    trend = (roll5 - roll22).rename("trend_signal")
    log_returns = np.log(features["close"]).diff()
    realised = (log_returns.rolling(22, min_periods=22).std() * np.sqrt(365)).rename("annualised_vol")
    median_vol = realised.rolling(252, min_periods=60).median()
    out = features.copy()
    out["regime_trend"] = np.sign(trend).fillna(0.0).astype(int)
    out["regime_vol"] = (realised > median_vol).astype(int)
    out["annualised_vol"] = realised
    out["trend_signal"] = trend
    return out


def _bh_adjust(pvalues: np.ndarray) -> np.ndarray:
    p = np.asarray(pvalues, dtype=float)
    n = len(p)
    order = np.argsort(p)
    adjusted = np.empty(n, dtype=float)
    running = 1.0
    for rank in range(n, 0, -1):
        idx = order[rank - 1]
        running = min(running, p[idx] * n / rank)
        adjusted[idx] = running
    return adjusted


def _block_indices(n: int, block: int, rng: np.random.Generator) -> np.ndarray:
    starts = rng.integers(0, n, size=int(np.ceil(n / block)))
    offsets = np.arange(block)
    return ((starts[:, None] + offsets[None, :]) % n).ravel()[:n]


def _bootstrap_spearman(x: np.ndarray, y: np.ndarray, block: int, rng: np.random.Generator) -> tuple[float, float]:
    n = len(x)
    if n < 30:
        return float("nan"), float("nan")
    samples = np.empty(BOOTSTRAPS, dtype=float)
    for i in range(BOOTSTRAPS):
        idx = _block_indices(n, block, rng)
        corr, _ = spearmanr(x[idx], y[idx])
        samples[i] = corr
    samples = samples[np.isfinite(samples)]
    if samples.size == 0:
        return float("nan"), float("nan")
    return float(np.nanpercentile(samples, 2.5)), float(np.nanpercentile(samples, 97.5))


def _flow_grid(features: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(RNG_SEED)
    features = features.copy()
    feature_cols = ("imbalance", "signed_dollar", "amihud", "roll_spread", "annualised_vol")
    rows: list[dict] = []
    pvalues: list[float] = []
    for feature in feature_cols:
        for horizon in DAILY_HORIZONS:
            target = features[f"fwd_{horizon}d"]
            valid = features[feature].notna() & target.notna()
            if valid.sum() < 60:
                continue
            x = features.loc[valid, feature].to_numpy(float)
            y = target.loc[valid].to_numpy(float)
            corr, p = spearmanr(x, y)
            placebo_y = target.shift(1).loc[valid].to_numpy(float)
            p_corr, p_p = spearmanr(x, placebo_y)
            inverse_corr, _ = spearmanr(-x, y)
            lo, hi = _bootstrap_spearman(x, y, max(5, horizon), rng)
            rows.append(
                {
                    "feature": feature,
                    "horizon_days": horizon,
                    "observations": int(valid.sum()),
                    "spearman": float(corr),
                    "p_value": float(p),
                    "spearman_placebo_shift_1d": float(p_corr),
                    "spearman_placebo_p": float(p_p),
                    "spearman_inverse": float(inverse_corr),
                    "bootstrap_lo": lo,
                    "bootstrap_hi": hi,
                    "bootstrap_excludes_zero": bool((lo > 0) | (hi < 0)) if np.isfinite(lo) and np.isfinite(hi) else False,
                }
            )
            pvalues.append(float(p))
    grid = pd.DataFrame(rows)
    if grid.empty:
        return grid, pd.DataFrame()
    grid["bh_q_value"] = _bh_adjust(np.array(pvalues))
    grid["bh_survives_q05"] = grid["bh_q_value"] < 0.05
    grid["placebo_non_significant"] = grid["spearman_placebo_p"] > 0.05
    grid["inverse_does_not_dominate"] = grid["spearman_inverse"].abs() <= grid["spearman"].abs()
    grid["retention"] = grid["bh_survives_q05"] & grid["bootstrap_excludes_zero"] & grid["placebo_non_significant"] & grid["inverse_does_not_dominate"]
    stable_rows: list[dict] = []
    for _, row in grid.iterrows():
        feature, horizon = row["feature"], row["horizon_days"]
        target = features[f"fwd_{horizon}d"]
        stable = []
        for year in (2018, 2019, 2020, 2021, 2022, 2023):
            mask = (features.index.year == year) & features[feature].notna() & target.notna()
            if mask.sum() < 30:
                continue
            corr, _ = spearmanr(features.loc[mask, feature], target.loc[mask])
            stable.append({"feature": feature, "horizon_days": horizon, "year": year, "spearman": float(corr)})
    stability = pd.DataFrame(stable_rows) if stable_rows else pd.DataFrame()
    return grid, stability


def _regime_stability(features: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for label, group in features.groupby(["regime_trend", "regime_vol"]):
        if len(group) < 60:
            continue
        for feature in ("imbalance", "signed_dollar"):
            for horizon in DAILY_HORIZONS:
                target = group[f"fwd_{horizon}d"]
                valid = group[feature].notna() & target.notna()
                if valid.sum() < 30:
                    continue
                corr, p = spearmanr(group.loc[valid, feature], target.loc[valid])
                rows.append(
                    {
                        "regime_trend": int(label[0]),
                        "regime_vol": int(label[1]),
                        "feature": feature,
                        "horizon_days": horizon,
                        "observations": int(valid.sum()),
                        "spearman": float(corr),
                        "p_value": float(p),
                    }
                )
    return pd.DataFrame(rows)


def _regime_summary(features: pd.DataFrame) -> dict:
    counts = features.groupby(["regime_trend", "regime_vol"]).size().to_dict()
    persistence = []
    for label, group in features.groupby(["regime_trend", "regime_vol"]):
        if len(group) < 2:
            continue
        idx = features.index.get_indexer(group.index)
        runs = []
        current = 1
        for i in range(1, len(idx)):
            if idx[i] == idx[i - 1] + 1:
                current += 1
            else:
                runs.append(current)
                current = 1
        runs.append(current)
        persistence.append({"regime": f"trend={int(label[0])}, vol={int(label[1])}", "mean_run": float(np.mean(runs)), "n_days": int(len(group))})
    return {"counts": {f"trend={k[0]}, vol={k[1]}": v for k, v in counts.items()}, "persistence": persistence}


def write_reports(features: pd.DataFrame, grid: pd.DataFrame, regime: pd.DataFrame, stability: pd.DataFrame, regime_stats: dict) -> None:
    FLOW_REPORT.parent.mkdir(parents=True, exist_ok=True)
    grid.to_csv(FLOW_CSV, index=False)
    features[["regime_trend", "regime_vol", "annualised_vol", "trend_signal", "imbalance", "signed_dollar", "amihud", "roll_spread"]].to_csv(REGIME_CSV, index_label="day")
    regime.to_csv(FLOW_CSV.with_name("2026-10-14-eth-n5-flow-regime.csv"), index=False)
    if not stability.empty:
        stability.to_csv(FLOW_CSV.with_name("2026-10-14-eth-n5-flow-stability.csv"), index=False)
    survivors = grid[grid["retention"]]
    flow_lines = [
        "# ETH N5 — causal kline flow mapping (descriptive only)",
        "",
        "**Status: descriptive only; no ledger hypothesis, no backtest, no holdout.**",
        "",
        f"- Cutoff exclusive: `{CUTOFF.isoformat()}`.",
        f"- Bootstrap: `{BOOTSTRAPS}` circular moving-block resamples; seed `{RNG_SEED}`; block length `max(5, h)`.",
        "- Features: daily aggregates of 1-minute active observations.  Frozen minutes excluded.",
        "- Targets: forward log returns at 1/2/5 days.  Placebo: forward target shifted by one day.",
        "",
        "## Causal grid",
        "",
        grid.to_string(index=False),
        "",
        f"Retained cells (BH q < 0.05, bootstrap excludes zero, placebo non-significant, inverse does not dominate): `{len(survivors)}` of `{len(grid)}`.",
        "",
        "If a descriptive cell survives the joint filter, it is **not** an edge.  Any future strategy must come from a fresh pre-registration and a counted `desk backtest`.",
        "",
        f"Artifacts: `{FLOW_CSV}`, regime table `{REGIME_CSV}`.",
    ]
    FLOW_REPORT.write_text("\n".join(flow_lines) + "\n", encoding="utf-8")
    regime_lines = [
        "# ETH N4 — regime cartography (descriptive only)",
        "",
        "**Status: descriptive only.**",
        "",
        f"- Cutoff exclusive: `{CUTOFF.isoformat()}`.",
        "- Trend regime: sign of the 5d vs 22d log-price mean difference at day t-1.",
        "- Vol regime: 1 if rolling 22d annualised volatility is above the trailing 252d median, else 0.",
        "",
        "## Class counts and mean run length",
        "",
        json.dumps(regime_stats, indent=2),
        "",
        "## Per-regime feature/horizon correlations",
        "",
        regime.to_string(index=False) if not regime.empty else "No regime had enough observations to evaluate.",
        "",
        "No regime filter is selected after viewing results.  Any future strategy must come from a fresh pre-registration.",
        "",
        f"Artifact: `{REGIME_CSV}`.",
    ]
    REGIME_LABEL.write_text("\n".join(regime_lines) + "\n", encoding="utf-8")


def main() -> int:
    minutes = r2_klines.read_local(SYMBOL)
    repaired, _ = bar_tools.normalise_clock(minutes)
    daily = bar_tools.build_bars(repaired, "1d", label="close", drop_frozen=False)
    daily = daily[daily.index < CUTOFF]
    if daily.empty:
        raise ValueError("no complete pre-cutoff daily bars")
    features = _build_daily_features(repaired, daily)
    features = _regime_labels(features)
    grid, stability = _flow_grid(features)
    regime = _regime_stability(features)
    regime_stats = _regime_summary(features)
    write_reports(features, grid, regime, stability, regime_stats)
    print(json.dumps({"grid_rows": len(grid), "retained": int(grid["retention"].sum()) if not grid.empty else 0, "regime_rows": len(regime), "days": int(len(features))}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
