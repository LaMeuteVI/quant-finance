"""Q5-V4 — Month-end and turn-of-month effect on crypto spot panel.

Preregistration: research/notes/2026-10-19-Q5-V4-prereg.md
Output: research/atlas/q5_v4_monthend.json

Pure descriptive. No strategy, no cost, no ledger hypothesis.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

CUTOFF = pd.Timestamp("2024-07-01T00:00:00Z")
SPOT_SLUGS = ["BTC-USDT", "ETH-USDT", "BNB-USDT", "SOL-USDT", "XRP-USDT"]
TIMEFRAMES = ["1d", "4h"]
N_VALUES = [2, 3, 5]


def _bh_fdr(pvals: list[float], q: float = 0.05) -> list[bool]:
    """Benjamini-Hochberg FDR at level q. Returns a boolean list of rejections."""
    n = len(pvals)
    if n == 0:
        return []
    order = np.argsort(pvals)
    sorted_p = np.array(pvals)[order]
    crit = (np.arange(1, n + 1) / n) * q
    rejected_sorted = sorted_p <= crit
    if not rejected_sorted.any():
        return [False] * n
    last = np.max(np.flatnonzero(rejected_sorted))
    rejected_sorted[: last + 1] = True
    rejected_sorted[last + 1 :] = False
    rejected = [False] * n
    for i, idx in enumerate(order):
        rejected[idx] = bool(rejected_sorted[i])
    return rejected


def _load_spot(slug: str, timeframe: str) -> pd.DataFrame:
    fp = Path(f"data/ohlcv/binance/{slug}/{timeframe}.parquet")
    df = pd.read_parquet(fp)
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    return df[df.index < CUTOFF].copy()


def _last_n_of_month(idx: pd.DatetimeIndex, n: int) -> np.ndarray:
    """Boolean mask, True where idx is in the last n bars of its calendar month."""
    last_per_month = idx.to_series().groupby([idx.year, idx.month]).transform("size").values
    pos_within_month = idx.to_series().groupby(
        [idx.year, idx.month]
    ).cumcount().values + 1
    return pos_within_month > (last_per_month - n)


def _first_n_of_month(idx: pd.DatetimeIndex, n: int) -> np.ndarray:
    """Boolean mask, True where idx is in the first n bars of its calendar month."""
    pos = idx.to_series().groupby([idx.year, idx.month]).cumcount().values + 1
    return pos <= n


def _fwd1(close: pd.Series, mask: np.ndarray) -> dict:
    fwd = (close.shift(-1) / close - 1.0)[mask].dropna()
    if fwd.size < 2 or fwd.std(ddof=1) == 0:
        return {
            "n": int(fwd.size),
            "mean": float(fwd.mean()) if fwd.size else float("nan"),
            "std": float("nan"),
            "p_vs_zero": float("nan"),
        }
    from scipy import stats
    t = float(fwd.mean()) / (fwd.std(ddof=1) / np.sqrt(fwd.size))
    p = float(2 * (1 - stats.t.cdf(abs(t), df=fwd.size - 1)))
    return {
        "n": int(fwd.size),
        "mean": float(fwd.mean()),
        "std": float(fwd.std(ddof=1)),
        "p_vs_zero": p,
    }


def _run_axis(slug: str, timeframe: str) -> dict:
    df = _load_spot(slug, timeframe)
    idx = df.index
    close = df["close"].astype(float)
    out = {"symbol": slug, "timeframe": timeframe, "n_obs": len(idx), "axes": {}}
    for n in N_VALUES:
        lom = _last_n_of_month(idx, n)
        fon = _first_n_of_month(idx, n)
        out["axes"][f"lom_n{n}"] = _fwd1(close, lom)
        out["axes"][f"fon_n{n}"] = _fwd1(close, fon)
    return out


def _verdict(per_axis: dict) -> dict:
    """Apply H1/H2/H3 from the prereg."""
    # ---- H1 (LOM positive at 1d, N=3): mean > 0 across >=4/5 symbols
    means_lom = []
    pvals_lom = []
    for sym in SPOT_SLUGS:
        ax = per_axis.get(f"{sym}|1d")
        if ax is None or "lom_n3" not in ax["axes"]:
            continue
        cell = ax["axes"]["lom_n3"]
        means_lom.append(cell["mean"])
        pvals_lom.append(cell["p_vs_zero"])
    pos_signs = sum(1 for m in means_lom if m > 0)
    if pvals_lom:
        # p-values are two-sided; for BH retention we keep the structure
        # but require positive mean >=4/5 symbols
        h1 = pos_signs >= 4 and all(m > 0 for m in means_lom if m > 0)
        # tighten with BH: any p <= q/2 (one-sided equivalent)
        bh_one_sided = [p / 2 for p in pvals_lom if not np.isnan(p)]
        rej = _bh_fdr(bh_one_sided, q=0.05)
        bh_keep = any(rej)
        h1 = h1 and bh_keep
    else:
        h1 = False

    # ---- H2 (FON positive at 1d, N=3)
    means_fon = []
    pvals_fon = []
    for sym in SPOT_SLUGS:
        ax = per_axis.get(f"{sym}|1d")
        if ax is None or "fon_n3" not in ax["axes"]:
            continue
        cell = ax["axes"]["fon_n3"]
        means_fon.append(cell["mean"])
        pvals_fon.append(cell["p_vs_zero"])
    pos_signs_fon = sum(1 for m in means_fon if m > 0)
    if pvals_fon:
        bh_one_sided = [p / 2 for p in pvals_fon if not np.isnan(p)]
        rej = _bh_fdr(bh_one_sided, q=0.05)
        bh_keep = any(rej)
        h2 = pos_signs_fon >= 4 and bh_keep
    else:
        h2 = False

    # ---- H3 (turn-of-month positive at 1d): sum of LOM+N + FON 1-bar returns
    tum_count = 0
    for sym in SPOT_SLUGS:
        ax = per_axis.get(f"{sym}|1d")
        if ax is None:
            continue
        lom_cell = ax["axes"].get("lom_n3", {})
        fon_cell = ax["axes"].get("fon_n3", {})
        lom_mean = lom_cell.get("mean", float("nan"))
        fon_mean = fon_cell.get("mean", float("nan"))
        if not (np.isnan(lom_mean) or np.isnan(fon_mean)):
            if lom_mean + fon_mean > 0:
                tum_count += 1
    h3 = tum_count >= 4

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
        "lom_means_1d": means_lom,
        "fon_means_1d": means_fon,
        "tum_count": tum_count,
    }


def run() -> dict:
    per_axis = {}
    for slug in SPOT_SLUGS:
        for tf in TIMEFRAMES:
            try:
                per_axis[f"{slug}|{tf}"] = _run_axis(slug, tf)
            except Exception as exc:  # pragma: no cover
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
    out_path = Path("research/atlas/q5_v4_monthend.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, default=str))
    v = out["verdict"]
    print(
        f"wrote {out_path} ({out_path.stat().st_size} bytes); "
        f"verdict={v['verdict']} H1={v['h1_pass']} H2={v['h2_pass']} H3={v['h3_pass']}"
    )


if __name__ == "__main__":
    main()
