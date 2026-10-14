"""BTC/ETH N1 descriptive study: common technical-analysis signals with placebo
and inverse.  Pre-cutoff only.  See
``research/2026-10-14-btc-eth-n1-ta-prereg.md`` for the protocol.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp

from aster.data import r2_klines

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
HORIZONS = (1, 3, 7, 14)
BOOTSTRAPS = 5_000
RNG_SEED = 20261014
FIB_LEVELS = (0.382, 0.5, 0.618)
FIB_PLACEBO_LEVELS = (0.55, 0.6, 0.65, 0.7)
REPORT = "research/assets/2026-10-14-{sym}-n1-ta.md"
CSV_PATH = "research/assets/2026-10-14-{sym}-n1-ta.csv"
REGIME_CSV = "research/assets/2026-10-14-{sym}-n1-ta-regime.csv"
SYMBOLS = ("BTCUSDT", "ETHUSDT")


# ----------------------------- signal primitives -----------------------------


def rsi(close: pd.Series, length: int = 14) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0.0)
    down = (-delta).clip(lower=0.0)
    avg_up = up.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()
    avg_dn = down.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()
    # Convention: if avg_dn == 0 (no down moves) return 100; if avg_up == 0 return 0.
    rs = avg_up / avg_dn.replace(0.0, np.nan)
    out = 100.0 - 100.0 / (1.0 + rs)
    no_down = (avg_dn.abs() < 1e-18) & (avg_up.abs() >= 1e-18)
    no_up = (avg_up.abs() < 1e-18) & (avg_dn.abs() >= 1e-18)
    out = out.where(~no_down, 100.0)
    out = out.where(~no_up, 0.0)
    return out.fillna(50.0)


def bollinger(close: pd.Series, length: int = 20, k: float = 2.0) -> tuple[pd.Series, pd.Series]:
    mid = close.rolling(length, min_periods=length).mean()
    sd = close.rolling(length, min_periods=length).std()
    return mid - k * sd, mid + k * sd


def donchian(high: pd.Series, low: pd.Series, length: int = 20) -> tuple[pd.Series, pd.Series]:
    return high.rolling(length, min_periods=length).max().shift(1), low.rolling(length, min_periods=length).min().shift(1)


def sma_cross(close: pd.Series, fast: int, slow: int) -> pd.Series:
    fast_ma = close.rolling(fast, min_periods=fast).mean()
    slow_ma = close.rolling(slow, min_periods=slow).mean()
    diff = fast_ma - slow_ma
    return ((diff > 0).astype(int) - (diff < 0).astype(int)).fillna(0).astype(int)


def fvg_events(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.DataFrame:
    """Daily FVG events.  Up FVG: low[t] > high[t-2] (gap up, three-bar).
    Down FVG: high[t] < low[t-2].  Event at t+1 (next-day entry)."""
    prev_high = high.shift(2)
    prev_low = low.shift(2)
    up = (low > prev_high).shift(1).fillna(False)
    down = (high < prev_low).shift(1).fillna(False)
    return pd.DataFrame({"fvg_up": up, "fvg_down": down}, index=close.index)


def weekly_pivots(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.DataFrame:
    """Classic weekly pivots: PP = (H+L+C)/3 of previous week, mapped onto the
    following daily bars.  S1/R1 = 2*PP-prev_low / 2*PP-prev_high."""
    week = high.index.tz_localize(None).to_period("W")
    pp_raw = pd.DataFrame({"H": high, "L": low, "C": close}).groupby(week).agg({"H": "max", "L": "min", "C": "last"})
    pp_raw["PP"] = (pp_raw["H"] + pp_raw["L"] + pp_raw["C"]) / 3.0
    pp_raw["S1"] = 2.0 * pp_raw["PP"] - pp_raw["H"]
    pp_raw["R1"] = 2.0 * pp_raw["PP"] - pp_raw["L"]
    pp_raw = pp_raw.shift(1)
    pp_raw.index = pp_raw.index.to_timestamp(how="end").tz_localize("UTC")
    pp = pp_raw["PP"].reindex(high.index, method="ffill")
    s1 = pp_raw["S1"].reindex(high.index, method="ffill")
    r1 = pp_raw["R1"].reindex(high.index, method="ffill")
    return pd.DataFrame({"PP": pp, "S1": s1, "R1": r1})


def fib_levels(swing_high: pd.Series, swing_low: pd.Series, level: float) -> pd.Series:
    return swing_low + (swing_high - swing_low) * level


# ----------------------------- study plumbing --------------------------------


def _bootstrap_mean(values: np.ndarray, block: int, rng: np.random.Generator) -> tuple[float, float]:
    n = len(values)
    if n < 30:
        return float("nan"), float("nan")
    starts = rng.integers(0, n, size=int(np.ceil(n / block)))
    offsets = np.arange(block)
    idx = ((starts[:, None] + offsets[None, :]) % n).ravel()[:n]
    samples = np.empty(BOOTSTRAPS, dtype=float)
    for i in range(BOOTSTRAPS):
        s = idx if i == 0 else ((starts[:, None] + offsets[None, :] + i) % n).ravel()[:n]
        samples[i] = values[s].mean()
    return float(np.nanpercentile(samples, 2.5)), float(np.nanpercentile(samples, 97.5))


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


def _event_returns(events: pd.Series, fwd: pd.DataFrame, horizon: int) -> pd.Series:
    target = fwd[f"fwd_{horizon}d"]
    return target[events.fillna(False)]


@dataclass(frozen=True)
class StudyOutput:
    grid: pd.DataFrame
    regime: pd.DataFrame


def build_daily(symbol: str) -> pd.DataFrame:
    minutes = r2_klines.read_local(symbol)
    active = minutes[(minutes["trades"] > 0) & (minutes["close"] > 0)].copy()
    daily = pd.DataFrame(
        {
            "open": active["open"].resample("1D", label="left", closed="right").first(),
            "high": active["high"].resample("1D", label="left", closed="right").max(),
            "low": active["low"].resample("1D", label="left", closed="right").min(),
            "close": active["close"].resample("1D", label="left", closed="right").last(),
        }
    ).dropna()
    daily = daily[daily.index < CUTOFF]
    return daily


def build_features(daily: pd.DataFrame) -> pd.DataFrame:
    out = pd.DataFrame(index=daily.index)
    out["close"] = daily["close"]
    out["high"] = daily["high"]
    out["low"] = daily["low"]
    out["open"] = daily["open"]
    out["rsi14"] = rsi(daily["close"], 14)
    out["bb_low"], out["bb_up"] = bollinger(daily["close"], 20, 2.0)
    out["don_hi"], out["don_lo"] = donchian(daily["high"], daily["low"], 20)
    out["sma_cross_long"] = sma_cross(daily["close"], 20, 100)
    out["sma_cross_short"] = sma_cross(daily["close"], 5, 20)
    fvg = fvg_events(daily["open"], daily["high"], daily["low"], daily["close"])
    out["fvg_up"] = fvg["fvg_up"]
    out["fvg_down"] = fvg["fvg_down"]
    pivots = weekly_pivots(daily["high"], daily["low"], daily["close"])
    out["pivot_pp"] = pivots["PP"]
    out["pivot_s1"] = pivots["S1"]
    out["pivot_r1"] = pivots["R1"]
    swing_hi = daily["high"].rolling(252, min_periods=60).max()
    swing_lo = daily["low"].rolling(252, min_periods=60).min()
    fib_grid = {}
    for level in FIB_LEVELS + FIB_PLACEBO_LEVELS:
        fib_grid[f"fib_{level}"] = fib_levels(swing_hi, swing_lo, level)
    fib_frame = pd.DataFrame(fib_grid, index=daily.index)
    out = pd.concat([out, fib_frame], axis=1)
    for h in HORIZONS:
        out[f"fwd_{h}d"] = np.log(daily["close"]).shift(-h) - np.log(daily["close"])
    return out


def _ttest(values: np.ndarray) -> tuple[float, float]:
    n = len(values)
    if n < 30:
        return float("nan"), float("nan")
    t, p = ttest_1samp(values, popmean=0.0)
    return float(t), float(p)


def event_grid(features: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(RNG_SEED)
    fwd = features[[f"fwd_{h}d" for h in HORIZONS]]
    rows: list[dict] = []
    pvalues: list[float] = []
    for h in HORIZONS:
        target = features[f"fwd_{h}d"]
        # Use the next-longer horizon as placebo: it has minimal overlap with the original target.
        placebo_h = next((k for k in HORIZONS if k > h), h)
        placebo_target = features[f"fwd_{placebo_h}d"]

        def _eval(mask, label, inv_mask=None):
            mask = mask.fillna(False) if mask.dtype == bool else mask.fillna(False).astype(bool)
            vals = target[mask].dropna().to_numpy()
            t, p = _ttest(vals)
            lo, hi = _bootstrap_mean(vals, max(5, h), rng)
            placebo_vals = placebo_target[mask].dropna().to_numpy()
            t_p, p_p = _ttest(placebo_vals)
            if inv_mask is not None:
                inv = target[inv_mask.fillna(False)].dropna().to_numpy()
                t_inv, p_inv = _ttest(inv)
                inv_mean = float(inv.mean()) if inv.size else float("nan")
            else:
                t_inv, p_inv, inv, inv_mean = float("nan"), float("nan"), np.array([]), float("nan")
            rows.append({
                "signal": label,
                "horizon_days": h,
                "observations": int(mask.sum()),
                "mean_fwd": float(vals.mean()) if vals.size else float("nan"),
                "t_stat": t,
                "p_value": p,
                "bootstrap_lo": lo,
                "bootstrap_hi": hi,
                "inverse_mean_fwd": inv_mean,
                "inverse_t_stat": t_inv,
                "inverse_p_value": p_inv,
                "placebo_mean": float(placebo_vals.mean()) if placebo_vals.size else float("nan"),
                "placebo_t_stat": float(t_p),
                "placebo_p_value": float(p_p),
            })
            pvalues.append(p)

        # MA crossovers
        _eval(features["sma_cross_long"] == 1, f"sma_cross_long_state_1_h{h}", features["sma_cross_long"] == -1)
        _eval(features["sma_cross_long"] == -1, f"sma_cross_long_state_minus1_h{h}", features["sma_cross_long"] == 1)
        _eval(features["sma_cross_short"] == 1, f"sma_cross_short_state_1_h{h}", features["sma_cross_short"] == -1)
        _eval(features["sma_cross_short"] == -1, f"sma_cross_short_state_minus1_h{h}", features["sma_cross_short"] == 1)

        # RSI zones
        _eval(features["rsi14"] < 30, f"rsi_oversold_h{h}", features["rsi14"] > 70)
        _eval(features["rsi14"] > 70, f"rsi_overbought_h{h}", features["rsi14"] < 30)

        # Bollinger
        _eval(features["close"] < features["bb_low"], f"bb_lower_break_h{h}", features["close"] > features["bb_up"])
        _eval(features["close"] > features["bb_up"], f"bb_upper_break_h{h}", features["close"] < features["bb_low"])

        # Donchian
        _eval(features["close"] > features["don_hi"], f"donchian_break_up_h{h}", features["close"] < features["don_lo"])
        _eval(features["close"] < features["don_lo"], f"donchian_break_down_h{h}", features["close"] > features["don_hi"])

        # Fibonacci (real + placebo)
        for level in FIB_LEVELS + FIB_PLACEBO_LEVELS:
            _eval(features["close"] < features[f"fib_{level}"], f"fib_{level}_below_h{h}", features["close"] > features[f"fib_{level}"])
            _eval(features["close"] > features[f"fib_{level}"], f"fib_{level}_above_h{h}", features["close"] < features[f"fib_{level}"])

        # Pivots
        _eval(features["close"] < features["pivot_s1"], f"pivot_s1_break_h{h}", features["close"] > features["pivot_r1"])
        _eval(features["close"] > features["pivot_r1"], f"pivot_r1_break_h{h}", features["close"] < features["pivot_s1"])

        # FVG
        _eval(features["fvg_up"].fillna(False), f"fvg_up_entry_h{h}", features["fvg_down"].fillna(False))
        _eval(features["fvg_down"].fillna(False), f"fvg_down_entry_h{h}", features["fvg_up"].fillna(False))

    grid = pd.DataFrame(rows)
    if grid.empty:
        return grid
    grid["bh_q_value"] = _bh_adjust(np.array(pvalues))
    grid["bh_survives_q05"] = grid["bh_q_value"] < 0.05
    grid["bootstrap_excludes_zero"] = (grid["bootstrap_lo"] > 0) | (grid["bootstrap_hi"] < 0)
    # Placebo non-significant: the placebo target's t-test is non-significant (p >= 0.05).
    grid["placebo_non_significant"] = grid["placebo_p_value"].isna() | (grid["placebo_p_value"] >= 0.05)
    # Inverse does not dominate: |inverse_mean_fwd| <= |mean_fwd|.
    grid["inverse_does_not_dominate"] = grid["inverse_mean_fwd"].isna() | (grid["inverse_mean_fwd"].abs() <= grid["mean_fwd"].abs())
    grid["retention"] = grid["bh_survives_q05"] & grid["bootstrap_excludes_zero"] & grid["placebo_non_significant"] & grid["inverse_does_not_dominate"]
    return grid


def regime_breakdown(features: pd.DataFrame, grid: pd.DataFrame) -> pd.DataFrame:
    roll5 = np.log(features["close"]).rolling(5, min_periods=5).mean()
    roll22 = np.log(features["close"]).rolling(22, min_periods=22).mean()
    trend = np.sign(roll5 - roll22).fillna(0.0).astype(int)
    log_ret = np.log(features["close"]).diff()
    realised = (log_ret.rolling(22, min_periods=22).std() * np.sqrt(365))
    median_vol = realised.rolling(252, min_periods=60).median()
    vol_regime = (realised > median_vol).astype(int)
    rows: list[dict] = []
    survivors = grid[grid["retention"]]
    for _, cell in survivors.iterrows():
        signal = cell["signal"]
        h = int(cell["horizon_days"])
        if signal.startswith("sma_cross_long_state_1"):
            mask = features["sma_cross_long"] == 1
        elif signal.startswith("sma_cross_long_state_minus1"):
            mask = features["sma_cross_long"] == -1
        elif signal == "rsi_oversold":
            mask = features["rsi14"] < 30
        elif signal == "rsi_overbought":
            mask = features["rsi14"] > 70
        elif signal == "bb_lower_break":
            mask = features["close"] < features["bb_low"]
        elif signal == "bb_upper_break":
            mask = features["close"] > features["bb_up"]
        elif signal == "donchian_break_up":
            mask = features["close"] > features["don_hi"]
        elif signal == "donchian_break_down":
            mask = features["close"] < features["don_lo"]
        elif signal.startswith("fib_") and signal.endswith("below"):
            level = signal.split("_")[1]
            mask = features["close"] < features[f"fib_{level}"]
        elif signal.startswith("fib_") and signal.endswith("above"):
            level = signal.split("_")[1]
            mask = features["close"] > features[f"fib_{level}"]
        elif signal == "pivot_s1_break":
            mask = features["close"] < features["pivot_s1"]
        elif signal == "pivot_r1_break":
            mask = features["close"] > features["pivot_r1"]
        elif signal == "fvg_up_entry":
            mask = features["fvg_up"].fillna(False)
        elif signal == "fvg_down_entry":
            mask = features["fvg_down"].fillna(False)
        else:
            continue
        target = features[f"fwd_{h}d"]
        mask = mask.fillna(False).rename("mask")
        target = target.rename("target")
        panel = pd.concat([mask, target, trend.rename("trend"), vol_regime.rename("vol")], axis=1)
        for (t, v), group in panel.groupby(["trend", "vol"]):
            valid = group["mask"] & group["target"].notna()
            if valid.sum() < 30:
                continue
            vals = group.loc[valid, "target"].to_numpy()
            t_stat, p = ttest_1samp(vals, popmean=0.0)
            rows.append({"signal": signal, "horizon_days": h, "trend": int(t), "vol": int(v), "n": int(valid.sum()), "mean_fwd": float(vals.mean()), "t_stat": float(t_stat), "p_value": float(p)})
    return pd.DataFrame(rows)


def write_reports(symbol: str, features: pd.DataFrame, grid: pd.DataFrame, regime: pd.DataFrame) -> dict:
    csv = Path(CSV_PATH.format(sym=symbol.lower().replace("usdt", "")))
    rep = Path(REPORT.format(sym=symbol.lower().replace("usdt", "")))
    rcsv = Path(REGIME_CSV.format(sym=symbol.lower().replace("usdt", "")))
    csv.parent.mkdir(parents=True, exist_ok=True)
    grid.to_csv(csv, index=False)
    regime.to_csv(rcsv, index=False)
    survivors = grid[grid["retention"]]
    lines = [
        f"# {symbol} N1 — common technical-analysis signals (descriptive only)",
        "",
        "**Status: descriptive only; no ledger hypothesis, no backtest, no holdout.**",
        "",
        f"- Cutoff exclusive: `{CUTOFF.isoformat()}`.",
        f"- Bootstrap: `{BOOTSTRAPS}` circular moving-block resamples; seed `{RNG_SEED}`; block length `max(5, h)`.",
        "- Frozen minutes excluded from close-derived features; weekly pivots and Fibonacci levels are level-of-the-market features, not signed returns.",
        f"- Forward log-returns at horizons {HORIZONS}; placebo = forward target shifted by one day; inverse = swapped event polarity; retention = BH q<0.05 ∧ bootstrap excludes zero ∧ placebo non-significant ∧ inverse does not dominate.",
        "",
        f"## Grid ({len(grid)} cells)",
        "",
        grid.to_string(index=False) if not grid.empty else "no cells",
        "",
        f"Retained cells: `{len(survivors)}` of `{len(grid)}`.",
        "",
        f"Artifacts: `{csv}`, regime breakdown `{rcsv}`.",
    ]
    rep.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"grid_rows": int(len(grid)), "retained": int(len(survivors)), "regime_rows": int(len(regime)), "days": int(len(features))}


def main() -> int:
    summary = {}
    for symbol in SYMBOLS:
        daily = build_daily(symbol)
        features = build_features(daily)
        grid = event_grid(features)
        regime = regime_breakdown(features, grid)
        summary[symbol] = write_reports(symbol, features, grid, regime)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
