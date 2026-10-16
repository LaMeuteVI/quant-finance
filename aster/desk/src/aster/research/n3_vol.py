"""BTC/ETH N3 realized-volatility forecasts, strictly pre-cutoff.

This is a descriptive pseudo-OOS forecast study.  It does not create a trading
signal, register a hypothesis, read the holdout, or call the backtest pipeline.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import norm

from aster.data import bars as bar_tools
from aster.data import r2_klines

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
TRAIN_END = pd.Timestamp("2022-12-31 23:59:59", tz="UTC")
SYMBOLS = {"BTCUSDT": "BTC/USDT", "ETHUSDT": "ETH/USDT"}
MIN_ACTIVE = 720
MIN_PAIRS = 1000
MIN_TRAIN = 756
NAIVE_WINDOW = 30
OUTPUT_CSV = Path("research/assets/2026-10-14-btc-eth-n3-vol.csv")
OUTPUT_MD = Path("research/assets/2026-10-14-btc-eth-n3-vol.md")


def realized_daily(minutes: pd.DataFrame) -> pd.DataFrame:
    """Build daily RV/BV from consecutive traded 1-minute closes.

    Frozen minutes are excluded, and only one-minute-spaced active observations
    form returns.  Returns are assigned to their endpoint UTC calendar day.
    """
    if not isinstance(minutes.index, pd.DatetimeIndex) or minutes.index.tz is None:
        raise ValueError("minutes must have a tz-aware DatetimeIndex")
    if (minutes.index >= CUTOFF).any():
        raise ValueError("N3 input crosses the exploration cutoff")
    frame = minutes.sort_index()
    active = frame[(frame["trades"] > 0) & (frame["close"] > 0)].copy()
    if active.empty:
        raise ValueError("no active minute observations")
    delta = active.index.to_series().diff()
    ret = np.log(active["close"]).diff()
    valid = (delta == pd.Timedelta(minutes=1)) & ret.notna()
    endpoints = active.index[valid]
    returns = pd.Series(ret.loc[valid].to_numpy(float), index=endpoints, name="r")
    day = returns.index.normalize()
    active_day = active.groupby(active.index.normalize()).size().rename("active_minutes")
    pair_day = returns.groupby(day).size().rename("valid_pairs")
    rv = (returns.pow(2).groupby(day).sum() * 1e8).rename("rv")
    previous = returns.shift(1)
    same_day = day.to_series(index=returns.index).eq(day.to_series(index=returns.index).shift(1)).to_numpy()
    products = (returns.abs() * previous.abs()).where(same_day)
    bv = (products.groupby(day).sum(min_count=1) * (np.pi / 2 * 1e8)).rename("bv")
    out = pd.concat([rv, bv, active_day, pair_day], axis=1)
    out["jump"] = (out["rv"] - out["bv"]).clip(lower=0.0)
    out["valid"] = (out["active_minutes"] >= MIN_ACTIVE) & (out["valid_pairs"] >= MIN_PAIRS)
    out.index = pd.DatetimeIndex(out.index, tz="UTC", name="day")
    return out.sort_index()


def _daily_close_returns(minutes: pd.DataFrame) -> pd.Series:
    repaired, _ = bar_tools.normalise_clock(minutes)
    daily = bar_tools.build_bars(repaired, "1d", label="close", drop_frozen=False)
    daily = daily[daily.index < CUTOFF]
    return np.log(daily["close"]).diff().rename("daily_return")


def build_dataset(minutes: pd.DataFrame) -> pd.DataFrame:
    out = realized_daily(minutes)
    out = out.join(_daily_close_returns(minutes), how="left")
    return out


def _har_features(log_rv: pd.Series) -> pd.DataFrame:
    return pd.DataFrame({
        "const": 1.0,
        "lag1": log_rv,
        "mean5": log_rv.rolling(5, min_periods=5).mean(),
        "mean22": log_rv.rolling(22, min_periods=22).mean(),
    })


def fit_har_predict(log_rv: pd.Series, origin: int) -> float:
    features = _har_features(log_rv)
    target = log_rv.shift(-1)
    train = pd.concat([features, target.rename("target")], axis=1).iloc[:origin].dropna()
    if len(train) < MIN_TRAIN:
        return float("nan")
    beta = np.linalg.lstsq(train[["const", "lag1", "mean5", "mean22"]].to_numpy(), train["target"].to_numpy(), rcond=None)[0]
    row = features.iloc[origin][["const", "lag1", "mean5", "mean22"]].to_numpy(float)
    return float(row @ beta) if np.isfinite(row).all() else float("nan")


def _garch_variance(params: np.ndarray, returns: np.ndarray) -> tuple[float, np.ndarray]:
    omega, alpha, beta = params
    var0 = max(float(np.var(returns)), 1e-12)
    variances = np.empty(len(returns), dtype=float)
    variances[0] = var0
    for i in range(1, len(returns)):
        variances[i] = omega + alpha * returns[i - 1] ** 2 + beta * variances[i - 1]
    return variances[-1], variances


def _garch_params(sample: np.ndarray) -> np.ndarray:
    """Estimate GARCH parameters once for a fixed expanding-window sample."""
    variance = max(float(np.var(sample)), 1e-12)
    initial = np.array([variance * 0.05, 0.05, 0.90])

    def objective(params: np.ndarray) -> float:
        omega, alpha, beta = params
        if omega <= 0 or alpha < 0 or beta < 0 or alpha + beta >= 0.9999:
            return 1e12 + 1e12 * max(alpha + beta - 0.9999, 0.0)
        _, variances = _garch_variance(params, sample)
        return float(np.sum(np.log(variances) + sample * sample / variances))

    result = minimize(
        objective,
        initial,
        method="L-BFGS-B",
        bounds=[(1e-12, variance * 10.0), (1e-8, 0.999), (1e-8, 0.999)],
        options={"maxiter": 50, "ftol": 1e-8},
    )
    return result.x if result.success and np.isfinite(result.fun) else initial


def fit_garch_predict(returns: pd.Series, origin: int) -> float:
    """Fit one GARCH forecast at an origin (legacy reference path)."""
    sample = returns.iloc[:origin].dropna().to_numpy(float)
    if len(sample) < MIN_TRAIN:
        return float("nan")
    sample = sample[-min(len(sample), 1260):]
    params = _garch_params(sample)
    omega, alpha, beta = params
    last_var, _ = _garch_variance(params, sample)
    forecast = omega + alpha * sample[-1] ** 2 + beta * last_var
    return float(np.log(max(forecast * 1e8, 1e-12)))


def dm_hln(loss_diff: np.ndarray, horizon: int = 1) -> tuple[float, float]:
    """DM-HLN statistic and two-sided normal p-value with HAC loss variance."""
    d = np.asarray(loss_diff, dtype=float)
    d = d[np.isfinite(d)]
    n = len(d)
    if n < 10:
        return float("nan"), float("nan")
    centered = d - d.mean()
    bandwidth = max(0, int(np.floor(n ** (1 / 3))))
    variance = float(np.dot(centered, centered) / n)
    for lag in range(1, bandwidth + 1):
        gamma = float(np.dot(centered[lag:], centered[:-lag]) / n)
        variance += 2.0 * (1.0 - lag / (bandwidth + 1.0)) * gamma
    variance = max(variance, 1e-18)
    dm = float(d.mean() / np.sqrt(variance / n))
    hln = np.sqrt((n + 1 - 2 * horizon + horizon * (horizon - 1) / n) / n)
    dm *= hln
    return dm, float(2.0 * norm.sf(abs(dm)))


def forecast_one(symbol: str, dataset: pd.DataFrame) -> pd.DataFrame:
    data = dataset.loc[dataset["valid"] & dataset["rv"].gt(0)].copy()
    data["log_rv"] = np.log(data["rv"])
    data["log_bv"] = np.log(data["bv"].clip(lower=1e-12))
    data["log_rv_lag"] = data["log_rv"].shift(1)
    rows: list[dict] = []
    for i in range(len(data) - 1):
        origin_date = data.index[i]
        target_date = data.index[i + 1]
        if origin_date <= TRAIN_END or target_date >= CUTOFF:
            continue
        naive = float(data["log_rv"].iloc[max(0, i - NAIVE_WINDOW + 1):i + 1].mean())
        har = fit_har_predict(data["log_rv"], i)
        garch = fit_garch_predict(data["daily_return"], i)
        target = float(data["log_rv"].iloc[i + 1])
        rows.append({
            "symbol": symbol, "origin": origin_date, "target": target_date,
            "target_log_rv": target, "naive_log_rv": naive,
            "har_log_rv": har, "garch_log_rv": garch,
        })
    return pd.DataFrame(rows)


def summarize(forecasts: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    pairs = (("har", "naive"), ("garch", "naive"), ("har", "garch"))
    for symbol, group in forecasts.groupby("symbol"):
        for loss_name, loss_fn in (("squared", lambda e: e * e), ("absolute", np.abs)):
            for first, second in pairs:
                e1 = loss_fn(group["target_log_rv"] - group[f"{first}_log_rv"])
                e2 = loss_fn(group["target_log_rv"] - group[f"{second}_log_rv"])
                diff = (e1 - e2).to_numpy(float)
                dm, p = dm_hln(diff, horizon=1)
                rows.append({
                    "symbol": symbol, "loss": loss_name, "model_1": first,
                    "model_2": second, "observations": int(np.isfinite(diff).sum()),
                    "mean_loss_diff_model1_minus_model2": float(np.nanmean(diff)),
                    "dm_hln": dm, "p_value": p,
                    "year_2023_mean_diff": float(np.nanmean(diff[group["target"].dt.year.to_numpy() == 2023])),
                    "year_2024_mean_diff": float(np.nanmean(diff[group["target"].dt.year.to_numpy() == 2024])) if (group["target"].dt.year == 2024).any() else float("nan"),
                })
    out = pd.DataFrame(rows)
    if not out.empty:
        p = out["p_value"].to_numpy(float)
        order = np.argsort(p)
        q = np.empty(len(p), dtype=float)
        running = 1.0
        for rank in range(len(p), 0, -1):
            idx = order[rank - 1]
            running = min(running, p[idx] * len(p) / rank)
            q[idx] = running
        out["bh_q_value"] = q
        out["bh_q05"] = out["bh_q_value"] < 0.05
    return out


def main() -> int:
    forecast_frames = []
    dataset_stats = []
    for r2_symbol, symbol in SYMBOLS.items():
        minutes = r2_klines.read_local(r2_symbol)
        dataset = build_dataset(minutes)
        dataset_stats.append({"symbol": symbol, "minute_rows": len(minutes), "daily_rows": len(dataset), "valid_days": int(dataset["valid"].sum())})
        forecast_frames.append(forecast_one(symbol, dataset))
    forecasts = pd.concat(forecast_frames, ignore_index=True)
    summary = summarize(forecasts)
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    forecasts.to_csv(OUTPUT_CSV, index=False)
    summary_path = OUTPUT_CSV.with_name("2026-10-14-btc-eth-n3-vol-summary.csv")
    summary.to_csv(summary_path, index=False)
    lines = [
        "# BTC/ETH N3 — realized volatility forecasts",
        "",
        "**Status: descriptive pseudo-OOS forecast study only; no strategy, no holdout, no allocation.**",
        "",
        f"- Cutoff exclusive: `{CUTOFF.isoformat()}`; training boundary: `{TRAIN_END.isoformat()}`.",
        f"- Validity gate: active minutes >= `{MIN_ACTIVE}`, one-minute active pairs >= `{MIN_PAIRS}`; minimum model history `{MIN_TRAIN}` observations.",
        "- RV/BV are calculated from consecutive active 1-minute closes; frozen minutes and missing minutes are not imputed.",
        "- Models: 30-observation naive, recursive HAR-RV, recursive GARCH(1,1) volatility benchmark.",
        "- Evaluation: log-RV squared and absolute loss; DM-HLN with HAC bandwidth floor(N^(1/3)); BH-FDR across the fixed 12 model/loss/asset comparisons.",
        "",
        "## Dataset audit",
        "",
        pd.DataFrame(dataset_stats).to_string(index=False),
        "",
        "## Forecast comparison",
        "",
        summary.to_string(index=False),
        "",
        "A lower loss for a volatility forecast is not alpha. No strategy hypothesis is registered from this report; any future volatility-targeting idea requires its own mechanism, costs, capacity, counted desk backtest, sealed holdout and paper-trading evidence.",
        "",
        f"Forecast artifact: `{OUTPUT_CSV}`; summary: `{summary_path}`.",
    ]
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"forecasts": len(forecasts), "comparisons": len(summary), "csv": str(OUTPUT_CSV), "summary": str(summary_path), "report": str(OUTPUT_MD)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
