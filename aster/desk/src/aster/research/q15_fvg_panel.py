"""Q15 — ETH fair-value-gap-down entry-h1 panel re-test.

Preregistration: research/notes/2026-10-19-Q15-prereg.md
Output: research/atlas/q15_fvg_panel.json

Pure descriptive. No strategy. No cost. No ledger hypothesis.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

CUTOFF = pd.Timestamp("2024-07-01T00:00:00Z")
SPOT_SLUGS = ["BTC-USDT", "ETH-USDT", "BNB-USDT", "SOL-USDT", "XRP-USDT"]
TIMEFRAMES = ["1d", "4h", "1h"]
HORIZONS = [1, 2, 5, 10]
GAP_SIZES = [0.0, 0.001, 0.003, 0.01]
GAP_DIRECTIONS = ["down", "up"]


def _load_spot(slug: str, timeframe: str) -> pd.DataFrame:
    """Load spot parquet for a (symbol, timeframe) pair, slice pre-cutoff."""
    fp = Path(f"data/ohlcv/binance/{slug}/{timeframe}.parquet")
    df = pd.read_parquet(fp)
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    return df[df.index < CUTOFF].copy()


def _detect_gaps(
    close: pd.Series,
    low: pd.Series,
    high: pd.Series,
    direction: str,
    gap_size: float,
) -> pd.Series:
    """Boolean mask, True on bar t where a (direction, gap_size) gap occurred.

    direction == "down":
        close[t] < low[t-2] * (1 - gap_size)   (price dropped, leaving a gap)
    direction == "up":
        close[t] > high[t-2] * (1 + gap_size)
    gap_size == 0: any gap at all (contiguous bars).

    Bar `t` is the third bar of the 3-bar pattern; entry is at t+1 open.
    """
    if direction == "down":
        triggered = close < low.shift(2) * (1.0 - gap_size)
    else:
        assert direction == "up"
        triggered = close > high.shift(2) * (1.0 + gap_size)
    return triggered.fillna(False)


def _forward_returns(close: pd.Series, triggered: pd.Series, horizons: Iterable[int]) -> dict:
    """Compute mean fwd_h returns conditional on triggered[t] being True,
    using close[t+1] as the entry price (the first bar after gap detection).
    """
    entry = close.shift(-1)  # close at t+1, the entry point
    out = {}
    for h in horizons:
        # fwd_h: return from entry (t+1) to entry (t+1+h) = close[t+1+h] / close[t+1] - 1
        fwd = close.shift(-(1 + h)) / entry - 1.0
        vals = fwd[triggered].dropna()
        out[h] = {
            "count": int(vals.size),
            "mean": float(vals.mean()) if vals.size else float("nan"),
            "std": float(vals.std(ddof=1)) if vals.size > 1 else float("nan"),
        }
    return out


def _bh_fdr(pvals: list[float], q: float = 0.05) -> list[bool]:
    """Benjamini-Hochberg FDR at level q. Returns a boolean list of rejections."""
    n = len(pvals)
    if n == 0:
        return []
    order = np.argsort(pvals)
    sorted_p = np.array(pvals)[order]
    # critical values: p_(k) <= k/n * q
    crit = (np.arange(1, n + 1) / n) * q
    rejected_sorted = sorted_p <= crit
    # enforce monotonicity: largest k that is rejected, all below also rejected
    if not rejected_sorted.any():
        return [False] * n
    last = np.max(np.flatnonzero(rejected_sorted))
    rejected_sorted[: last + 1] = True
    rejected_sorted[last + 1 :] = False
    # un-sort
    rejected = [False] * n
    for i, idx in enumerate(order):
        rejected[idx] = bool(rejected_sorted[i])
    return rejected


def _bootstrap_ci(vals: np.ndarray, n_boot: int = 1000, seed: int = 0) -> tuple[float, float]:
    """Circular moving-block bootstrap of the mean; returns (q05, q95)."""
    if vals.size < 2:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    n = vals.size
    block = max(1, int(np.sqrt(n)))
    means = np.empty(n_boot)
    centered = vals - vals.mean()
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        # circular shift so blocks near the end wrap
        idx_circ = np.mod(idx + np.arange(n) // block, n)
        means[i] = centered[idx_circ].mean() + vals.mean()
    q05, q95 = np.quantile(means, [0.05, 0.95])
    return (float(q05), float(q95))


def _one_cell_stats(
    df: pd.DataFrame,
    direction: str,
    gap_size: float,
    horizons: Iterable[int],
) -> dict:
    close = df["close"].astype(float)
    low = df["low"].astype(float)
    high = df["high"].astype(float)
    triggered = _detect_gaps(close, low, high, direction, gap_size)
    fwd = _forward_returns(close, triggered, horizons)
    # bootstrap CI on fwd_1 mean
    entry = close.shift(-1)
    fwd1 = (close.shift(-2) / entry - 1.0)[triggered].dropna()
    ci = _bootstrap_ci(fwd1.to_numpy())
    # analytic one-sample t-test p-value (mean != 0), for BH-FDR
    from scipy import stats
    if fwd1.size > 1 and fwd1.std(ddof=1) > 0:
        t = float(fwd1.mean()) / (fwd1.std(ddof=1) / np.sqrt(fwd1.size))
        p = float(2 * (1 - stats.t.cdf(abs(t), df=fwd1.size - 1)))
    else:
        p = float("nan")
    return {
        "n_events": int(triggered.sum()),
        "fwd": fwd,
        "fwd1_mean": float(fwd1.mean()) if fwd1.size else float("nan"),
        "fwd1_ci": ci,
        "p_value_fwd1_vs_zero": p,
    }


def _run_one_axis(slug: str, timeframe: str) -> dict:
    df = _load_spot(slug, timeframe)
    out = {"symbol": slug, "timeframe": timeframe, "n_obs": len(df), "axes": {}}
    for direction in GAP_DIRECTIONS:
        for gap_size in GAP_SIZES:
            cell = _one_cell_stats(df, direction, gap_size, HORIZONS)
            key = f"{direction}_gap{int(gap_size * 10000):04d}bps"
            out["axes"][key] = cell
    return out


def _verdict(per_axis: dict) -> dict:
    """Apply the preregistered H1/H2/H3 over the panel of base cells:
    direction=down, gap_size=0.001 (10 bps), all 5 symbols × 3 TF × 4 horizons.

    H1: ETH fvg_down_entry_h1 (gap=10bps) survives BH at q=0.05 within each TF.
    H2: sign of fwd_1 consistent across >=4/5 symbols at 1d.
    H3: fwd_1 monotone in gap_size (0.001 vs 0.003) at 1d.
    """
    # ---- H1
    h1_pass = []
    for tf in TIMEFRAMES:
        pvals_tf = []
        for sym in SPOT_SLUGS:
            axis = per_axis.get(f"{sym}|{tf}")
            if axis is None:
                continue
            cell = axis["axes"].get("down_gap0010bps")
            if cell:
                pvals_tf.append(cell["p_value_fwd1_vs_zero"])
        if pvals_tf:
            rej = _bh_fdr(pvals_tf, q=0.05)
            # ETH must survive the BH test
            eth = SPOT_SLUGS.index("ETH-USDT")
            h1_pass.append(bool(rej[eth]))
    h1 = bool(h1_pass) and all(h1_pass)

    # ---- H2
    fwd1_signs = []
    for sym in SPOT_SLUGS:
        axis = per_axis.get(f"{sym}|1d")
        if axis is None:
            continue
        cell = axis["axes"].get("down_gap0010bps")
        if cell and cell["n_events"] > 0:
            fwd1_signs.append(int(np.sign(cell["fwd1_mean"])))
    h2 = (len(fwd1_signs) >= 4 and len(set(fwd1_signs)) == 1)

    # ---- H3
    fwd_by_size = {}
    for gap in [0.001, 0.003]:
        vals = []
        for sym in SPOT_SLUGS:
            axis = per_axis.get(f"{sym}|1d")
            if axis is None:
                continue
            cell = axis["axes"].get(f"down_gap{int(gap * 10000):04d}bps")
            if cell and cell["n_events"] > 0:
                vals.append((sym, cell["fwd1_mean"], cell["n_events"]))
        fwd_by_size[gap] = vals
    monotone_count = 0
    syms_001 = {v[0] for v in fwd_by_size[0.001]}
    syms_003 = {v[0] for v in fwd_by_size[0.003]}
    common = syms_001 & syms_003
    for sym in common:
        m1 = next(v for v in fwd_by_size[0.001] if v[0] == sym)[1]
        m3 = next(v for v in fwd_by_size[0.003] if v[0] == sym)[1]
        # monotone: |m3| >= |m1| with same sign
        if np.sign(m3) == np.sign(m1) and abs(m3) >= abs(m1):
            monotone_count += 1
    h3 = monotone_count >= 4

    n_pass = int(h1) + int(h2) + int(h3)
    if n_pass == 3:
        verdict = "RETAIN"
    elif n_pass == 0:
        verdict = "FALSIFIED"
    else:
        verdict = "NEUTRAL"
    return {
        "verdict": verdict,
        "h1_pass": h1,
        "h2_pass": h2,
        "h3_pass": h3,
        "fwd1_signs_1d": fwd1_signs,
        "monotone_count": monotone_count,
    }


def run() -> dict:
    per_axis = {}
    for slug in SPOT_SLUGS:
        for tf in TIMEFRAMES:
            try:
                per_axis[f"{slug}|{tf}"] = _run_one_axis(slug, tf)
            except Exception as exc:  # pragma: no cover -- defensive
                per_axis[f"{slug}|{tf}"] = {
                    "symbol": slug,
                    "timeframe": tf,
                    "error": repr(exc),
                }
    verdict = _verdict(per_axis)
    return {
        "cutoff_exclusive": "2024-07-01T00:00:00Z",
        "n_axes": len(per_axis),
        "per_axis": per_axis,
        "verdict": verdict,
    }


def main() -> None:
    out = run()
    out_path = Path("research/atlas/q15_fvg_panel.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, default=str))
    v = out["verdict"]
    print(
        f"wrote {out_path} ({out_path.stat().st_size} bytes); "
        f"verdict={v['verdict']} H1={v['h1_pass']} H2={v['h2_pass']} H3={v['h3_pass']}"
    )


if __name__ == "__main__":
    main()
