"""Q5-V2 — intraday seasonality (hour UTC, weekday, funding fixings).

Descriptive only. No ledger hypothesis, no F-hypothesis, no DSR charge.

Outputs ``research/atlas/q5_v2_seasonality.json`` and the corresponding memo.
The preregistration is in ``research/notes/2026-10-19-Q5-V2-prereg.md``.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

from aster.data import r2_klines
from aster.data.r2_backtest_store import bars_from_minutes

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SPOT_SYMBOLS = ("BTCUSDT", "ETHUSDT")
FUNDING_SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT")
TIMEFRAMES = ("5m", "15m", "1h", "4h")
FIXING_HOURS = (0, 8, 16)
ASIA_HOURS = (0, 1, 2, 3, 4, 5, 6, 7)
EUROPE_HOURS = (7, 8, 9, 10, 11, 12, 13, 14, 15)
US_HOURS = (13, 14, 15, 16, 17, 18, 19, 20, 21)
BOOTSTRAP_DRAWS = 1000
BOOTSTRAP_BLOCK = 60  # minutes per block
SEED = 20261019
TAKER_BPS_PER_SIDE = 10
ROUND_TRIP_BPS = 3 * 2 * TAKER_BPS_PER_SIDE  # 60 bps round-trip, conservative
FDR_Q = 0.05
OUT = Path("research/atlas/q5_v2_seasonality.json")


# ---------- helpers ----------

def _bh_adjust(p: np.ndarray) -> np.ndarray:
    """Benjamini-Hochberg adjusted p-values (same shape, same order)."""
    p = np.asarray(p, dtype=float)
    n = len(p)
    order = np.argsort(p)
    ranked = p[order]
    adj = ranked * n / (np.arange(n) + 1)
    # enforce monotone non-decreasing from the right
    adj = np.minimum.accumulate(adj[::-1])[::-1]
    adj = np.clip(adj, 0.0, 1.0)
    out = np.empty(n, dtype=float)
    out[order] = adj
    return out


def _bar_returns(bars: pd.DataFrame) -> pd.Series:
    """Log-return per bar from the close column."""
    c = np.log(bars["close"].astype(float))
    return c.diff()


def _bucket_mean_se(ret: np.ndarray) -> tuple[float, float, float, int]:
    """Mean, standard-error-of-the-mean, t-stat, n of a 1-D return array (NaN-safe)."""
    r = ret[np.isfinite(ret)]
    n = int(len(r))
    if n < 30:
        return float("nan"), float("nan"), float("nan"), n
    mean = float(np.mean(r))
    se = float(np.std(r, ddof=1) / math.sqrt(n))
    t = float(mean / se) if se > 0 else float("nan")
    return mean, se, t, n


def _bootstrap_mean_ci(ret: np.ndarray, *, block: int, n_draws: int, seed: int) -> tuple[float, float]:
    """Block-bootstrap CI on the mean of a 1-D return series."""
    r = ret[np.isfinite(ret)]
    if len(r) < block * 4:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    n_blocks = len(r) // block
    blocks = r[: n_blocks * block].reshape(n_blocks, block)
    n_b = blocks.shape[0]
    means = np.empty(n_draws, dtype=float)
    for i in range(n_draws):
        idx = rng.integers(0, n_b, size=n_b)
        means[i] = float(blocks[idx].mean())
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def _two_sample_t(a: np.ndarray, b: np.ndarray) -> float:
    """Welch two-sample t-statistic (NaN-safe)."""
    a = a[np.isfinite(a)]
    b = b[np.isfinite(b)]
    if len(a) < 30 or len(b) < 30:
        return float("nan")
    m_a, s_a = float(np.mean(a)), float(np.std(a, ddof=1))
    m_b, s_b = float(np.mean(b)), float(np.std(b, ddof=1))
    se = math.sqrt(s_a ** 2 / len(a) + s_b ** 2 / len(b))
    if se <= 0:
        return float("nan")
    return float((m_a - m_b) / se)


# ---------- spot grid ----------

def _spot_grid() -> dict:
    """Per (symbol, timeframe, hour-utc) bucket + weekday bucket."""
    out: dict[str, dict] = {}
    flat_rows: list[dict] = []
    for sym in SPOT_SYMBOLS:
        sym_block: dict[str, dict] = {}
        try:
            minutes = r2_klines.read_local(sym)
        except FileNotFoundError:
            sym_block = {"_error": "read_local raised FileNotFoundError"}
            out[sym] = sym_block
            continue
        for tf in TIMEFRAMES:
            try:
                bars = bars_from_minutes(minutes, tf)
            except ValueError as exc:
                sym_block[tf] = {"_error": str(exc)}
                continue
            r = _bar_returns(bars).to_numpy()
            idx = bars.index
            by_hour = {}
            for h in range(24):
                mask = (idx.hour == h)
                rs = r[mask]
                mean, se, t, n = _bucket_mean_se(rs)
                lo, hi = _bootstrap_mean_ci(rs, block=BOOTSTRAP_BLOCK, n_draws=BOOTSTRAP_DRAWS, seed=SEED + h)
                by_hour[h] = {
                    "n": n, "mean_log_ret": mean, "se": se, "t": t,
                    "ci_lo": lo, "ci_hi": hi,
                    "bps_per_bar": mean * 1e4 if math.isfinite(mean) else float("nan"),
                    "bps_per_day": (mean * 1e4 * (24 * 60 / _tf_minutes(tf))) if math.isfinite(mean) else float("nan"),
                }
                flat_rows.append({
                    "kind": "spot_hour",
                    "symbol": sym, "timeframe": tf, "bucket": str(h),
                    "n": n, "t": t, "mean_log_ret": mean,
                })
            by_weekday = {}
            for w in range(7):
                mask = (idx.weekday == w)
                rs = r[mask]
                mean, se, t, n = _bucket_mean_se(rs)
                by_weekday[w] = {
                    "n": n, "mean_log_ret": mean, "se": se, "t": t,
                    "bps_per_bar": mean * 1e4 if math.isfinite(mean) else float("nan"),
                }
                flat_rows.append({
                    "kind": "spot_weekday",
                    "symbol": sym, "timeframe": tf, "bucket": str(w),
                    "n": n, "t": t, "mean_log_ret": mean,
                })
            # fixing-vs-not
            fixing_mask = np.isin(idx.hour, FIXING_HOURS)
            nonfix_mask = ~fixing_mask
            mean_fix, se_fix, t_fix, n_fix = _bucket_mean_se(r[fixing_mask])
            mean_non, se_non, t_non, n_non = _bucket_mean_se(r[nonfix_mask])
            t_diff = _two_sample_t(r[fixing_mask], r[nonfix_mask])
            # session labels
            def _session_mean(hours: Iterable[int]) -> float:
                mask = np.isin(idx.hour, list(hours))
                rs = r[mask]
                m, _, _, _ = _bucket_mean_se(rs)
                return m
            asia = _session_mean(ASIA_HOURS)
            europe = _session_mean(EUROPE_HOURS)
            us = _session_mean(US_HOURS)
            # weekend vs weekday
            weekend_mask = (idx.weekday >= 5)
            weekday_mask = ~weekend_mask
            mean_we, _, t_we, n_we = _bucket_mean_se(r[weekend_mask])
            mean_wd, _, t_wd, n_wd = _bucket_mean_se(r[weekday_mask])
            sym_block[tf] = {
                "n_obs": int(np.isfinite(r).sum()),
                "by_hour_utc": by_hour,
                "by_weekday": by_weekday,
                "fixing": {
                    "fixing_mean": mean_fix, "nonfix_mean": mean_non,
                    "fixing_t": t_fix, "nonfix_t": t_non,
                    "diff_t": t_diff, "n_fixing": n_fix, "n_nonfix": n_non,
                },
                "session": {
                    "asia": asia, "europe": europe, "us": us,
                },
                "weekend": {
                    "weekend_mean": mean_we, "weekday_mean": mean_wd,
                    "weekend_t": t_we, "weekday_t": t_wd,
                    "n_weekend": n_we, "n_weekday": n_wd,
                },
            }
        out[sym] = sym_block
    return {"cells": out, "flat": flat_rows}


def _tf_minutes(tf: str) -> int:
    return {"5m": 5, "15m": 15, "1h": 60, "4h": 240}[tf]


# ---------- funding grid ----------

def _funding_grid() -> dict:
    """Read funding rate pre-cutoff and bucket per (symbol, fixing-hour-utc).

    Reads only ``funding_time`` column; raises on post-cutoff.
    """
    out: dict[str, dict] = {}
    for sym in FUNDING_SYMBOLS:
        try:
            df = _read_funding(sym)
        except FileNotFoundError:
            out[sym] = {"_error": "no funding file"}
            continue
        df = df[df.index < CUTOFF]
        if df.empty:
            out[sym] = {"_error": "no pre-cutoff funding"}
            continue
        rates = df["funding_rate"].astype(float).to_numpy()
        hours = df.index.hour
        by_hour = {}
        for h in range(24):
            mask = (hours == h)
            rs = rates[mask]
            n = int(len(rs))
            if n < 5:
                continue
            mean = float(np.mean(rs))
            se = float(np.std(rs, ddof=1) / math.sqrt(n))
            t = mean / se if se > 0 else float("nan")
            by_hour[h] = {"n": n, "mean": mean, "se": se, "t": t}
        # lag-1 autocorr
        a = rates[:-1]
        b = rates[1:]
        mask = np.isfinite(a) & np.isfinite(b)
        if mask.sum() > 30:
            autocorr1 = float(np.corrcoef(a[mask], b[mask])[0, 1])
        else:
            autocorr1 = float("nan")
        # fixing vs non-fixing hour means
        fixing_mask = np.isin(hours, FIXING_HOURS)
        mean_fix = float(np.mean(rates[fixing_mask])) if fixing_mask.any() else float("nan")
        mean_non = float(np.mean(rates[~fixing_mask])) if (~fixing_mask).any() else float("nan")
        out[sym] = {
            "n_fixing": int(len(rates)),
            "by_hour_utc": by_hour,
            "fixing_hour_mean": mean_fix,
            "nonfix_hour_mean": mean_non,
            "autocorr_lag1": autocorr1,
        }
    return out


def _read_funding(symbol: str) -> pd.DataFrame:
    """Read the funding-rate Parquet(s) for one symbol strictly pre-cutoff.

    Tries ``data/r2/market/futures/um/funding_rate/symbol=<SYM>/*.parquet``.
    """
    import pyarrow.parquet as pq
    base = Path("data/r2/market/futures/um/funding_rate") / f"symbol={symbol}"
    if not base.exists():
        raise FileNotFoundError(f"no funding store at {base}")
    parts = sorted(base.rglob("*.parquet"))
    if not parts:
        raise FileNotFoundError(f"no parquet under {base}")
    # Concatenate preserving the per-file tz-aware DatetimeIndex (ts).
    pieces = []
    for p in parts:
        t = pq.read_table(p)
        df = t.to_pandas()
        # The store uses 'ts' as the index column; restore the DatetimeIndex.
        if "ts" in df.columns:
            df.index = pd.to_datetime(df["ts"], utc=True)
            df = df.drop(columns=["ts"])
        pieces.append(df)
    df = pd.concat(pieces)
    # Column rename: last_funding_rate -> funding_rate (the rest of the module
    # expects this column name).
    if "last_funding_rate" in df.columns and "funding_rate" not in df.columns:
        df = df.rename(columns={"last_funding_rate": "funding_rate"})
    if "funding_rate" not in df.columns:
        raise FileNotFoundError(f"no funding_rate column in store for {symbol}")
    if not isinstance(df.index, pd.DatetimeIndex):
        raise FileNotFoundError(f"no datetime column in funding store for {symbol}")
    df = df.sort_index()
    # Hard-cutoff any row >= 2024-07-01 UTC
    mask = df.index < CUTOFF
    df = df.loc[mask].copy()
    return df


# ---------- verdict ----------

def _verdict(spot: dict, funding: dict) -> dict:
    """Apply the preregistered falsification bar."""
    flat = spot["flat"]
    ts = np.array([r["t"] for r in flat], dtype=float)
    finite = ts[np.isfinite(ts)]
    if len(finite) == 0:
        sig_frac = 0.0
        bh_sig = 0
        total = 0
    else:
        # two-sided t; approximate p with the t distribution (n large enough)
        from scipy import stats as sst
        n_per_row = np.array([r["n"] for r in flat], dtype=float)
        df = np.where(np.isfinite(ts), np.maximum(n_per_row - 2, 1), 1.0)
        p_two = 2.0 * (1.0 - sst.t.cdf(np.abs(np.where(np.isfinite(ts), ts, 0.0)), df))
        adj = _bh_adjust(p_two)
        sig = (adj < FDR_Q) & np.isfinite(ts)
        total = len(finite)
        bh_sig = int(sig.sum())
        sig_frac = bh_sig / max(total, 1)
    # cost hurdle: which buckets beat 30 bps round-trip in bps/day?
    bps_per_day_max = float("-inf")
    best = None
    for sym, sym_block in spot["cells"].items():
        if "_error" in sym_block:
            continue
        for tf, cell in sym_block.items():
            for h, b in cell["by_hour_utc"].items():
                v = b["bps_per_day"]
                if math.isfinite(v) and v > bps_per_day_max:
                    bps_per_day_max = v
                    best = {"symbol": sym, "timeframe": tf, "hour_utc": h, "bps_per_day": v}
    cost_hurdle_pass = bps_per_day_max > ROUND_TRIP_BPS
    # funding autocorr
    auts = []
    for sym, cell in funding.items():
        if "_error" in cell:
            continue
        if math.isfinite(cell.get("autocorr_lag1", float("nan"))):
            auts.append(cell["autocorr_lag1"])
    autocorrs = np.array(auts, dtype=float) if auts else np.array([float("nan")])
    funding_strong = float(np.nanmean(autocorrs)) >= 0.7 if len(auts) >= 4 else False
    # falsifications
    h1 = sig_frac >= 0.05 and cost_hurdle_pass
    h2 = funding_strong
    h3 = len(auts) >= 4 and (np.sum(np.array(auts) >= 0.7) >= 4)
    return {
        "n_spot_rows": total,
        "n_bh_significant": bh_sig,
        "frac_bh_significant": sig_frac,
        "max_bps_per_day": bps_per_day_max if bps_per_day_max != float("-inf") else float("nan"),
        "best_bucket": best,
        "cost_hurdle_bps_round_trip": ROUND_TRIP_BPS,
        "cost_hurdle_pass": cost_hurdle_pass,
        "funding_autocorrs": [float(x) for x in auts],
        "funding_autocorr_mean": float(np.nanmean(autocorrs)),
        "h1_pass": bool(h1),
        "h2_pass": bool(h2),
        "h3_pass": bool(h3),
        "verdict": "RETAIN" if (h1 or h2 or h3) else "FALSIFIED_ON_COVERAGE",
    }


# ---------- entry ----------

def run() -> dict:
    spot = _spot_grid()
    funding = _funding_grid()
    v = _verdict(spot, funding)
    return {
        "cutoff_exclusive": CUTOFF.isoformat(),
        "spot_symbols": list(SPOT_SYMBOLS),
        "funding_symbols": list(FUNDING_SYMBOLS),
        "timeframes": list(TIMEFRAMES),
        "fixing_hours_utc": list(FIXING_HOURS),
        "spot_grid": spot["cells"],
        "funding_grid": funding,
        "verdict": v,
        "seed": SEED,
        "bootstrap_draws": BOOTSTRAP_DRAWS,
    }


def main() -> None:
    out = run()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True))
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    print(f"verdict={out['verdict']['verdict']}")
    print(f"H1={out['verdict']['h1_pass']} H2={out['verdict']['h2_pass']} H3={out['verdict']['h3_pass']}")


if __name__ == "__main__":
    main()
