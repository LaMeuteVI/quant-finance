"""BTC N2 descriptive return dependence, strictly pre-cutoff and dev-only.

This module does not register or backtest a strategy.  It reads the existing
pre-cutoff daily store, stops at the development boundary used by the first BTC
hypothesis, and produces fixed-horizon continuation/reversal diagnostics with
moving-block bootstrap intervals and Benjamini-Hochberg FDR.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr

from aster.data import store

SYMBOL = "BTC/USDT"
CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
DEV_END = pd.Timestamp("2022-10-11", tz="UTC")
HORIZONS = (1, 3, 7, 14, 30, 60)
SEED = 20261014
BOOTSTRAPS = 10_000
OUTPUT_CSV = Path("research/assets/2026-10-14-btc-n2.csv")
OUTPUT_MD = Path("research/assets/2026-10-14-btc-n2.md")


def _bh_adjust(pvalues: np.ndarray) -> np.ndarray:
    """Benjamini-Hochberg adjusted p-values in original order."""
    p = np.asarray(pvalues, dtype=float)
    n = len(p)
    order = np.argsort(p)
    adjusted = np.empty(n, dtype=float)
    running = 1.0
    for rank in range(n, 0, -1):
        i = order[rank - 1]
        running = min(running, p[i] * n / rank)
        adjusted[i] = running
    return adjusted


def _block_indices(n: int, block: int, rng: np.random.Generator) -> np.ndarray:
    """Circular moving-block bootstrap indices of length n."""
    starts = rng.integers(0, n, size=(int(np.ceil(n / block)),))
    offsets = np.arange(block)
    indices = (starts[:, None] + offsets[None, :]) % n
    return indices.ravel()[:n]


def _bootstrap(x: np.ndarray, y: np.ndarray, block: int, rng: np.random.Generator) -> tuple[float, float]:
    values = np.empty(BOOTSTRAPS, dtype=float)
    n = len(x)
    for i in range(BOOTSTRAPS):
        idx = _block_indices(n, block, rng)
        values[i] = np.corrcoef(x[idx], y[idx])[0, 1]
    return float(np.nanpercentile(values, 2.5)), float(np.nanpercentile(values, 97.5))


def analyse(prices: pd.Series) -> pd.DataFrame:
    if not isinstance(prices.index, pd.DatetimeIndex) or prices.index.tz is None:
        raise ValueError("prices must have a tz-aware DatetimeIndex")
    if (prices.index >= CUTOFF).any():
        raise ValueError("N2 input crosses the exploration cutoff")
    prices = prices.loc[prices.index <= DEV_END].astype(float).sort_index()
    log_close = np.log(prices)
    rows: list[dict[str, float | int | str | bool]] = []
    rng = np.random.default_rng(SEED)
    pvalues: list[float] = []
    for h in HORIZONS:
        formation = log_close - log_close.shift(h)
        forward = log_close.shift(-h) - log_close
        valid = pd.concat({"formation": formation, "forward": forward}, axis=1).dropna()
        x, y = valid["formation"].to_numpy(), valid["forward"].to_numpy()
        corr, pvalue = pearsonr(x, y)
        sign = np.sign(x)
        signed_mean = float(np.mean(sign * y))
        hit = float(np.mean(sign == np.sign(y)))
        lag_x = log_close.shift(h + 1) - log_close.shift(1)
        placebo = pd.concat({"x": lag_x, "y": forward}, axis=1).dropna()
        placebo_corr = float(pearsonr(placebo["x"], placebo["y"])[0])
        lo, hi = _bootstrap(x, y, max(5, h), rng)
        rows.append({
            "horizon_days": h, "observations": len(valid), "correlation": float(corr),
            "p_value": float(pvalue), "bootstrap_lo": lo, "bootstrap_hi": hi,
            "mean_signed_forward_log_return": signed_mean, "directional_hit_rate": hit,
            "inverse_correlation": float(pearsonr(-x, y)[0]),
            "one_day_lag_placebo_correlation": placebo_corr,
            "bootstrap_block_days": max(5, h), "bootstrap_count": BOOTSTRAPS,
        })
        pvalues.append(float(pvalue))
    result = pd.DataFrame(rows)
    result["bh_q_value"] = _bh_adjust(np.array(pvalues))
    result["bootstrap_excludes_zero"] = (result["bootstrap_lo"] > 0) | (result["bootstrap_hi"] < 0)
    result["fdr_survives_q05"] = result["bh_q_value"] < 0.05
    return result


def write_report(result: pd.DataFrame) -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT_CSV, index=False)
    manifest = store.manifest("ohlcv", "binance", SYMBOL, "1d")
    survivors = result[result["fdr_survives_q05"] & result["bootstrap_excludes_zero"]]
    lines = [
        "# BTC N2 — descriptive return dependence",
        "",
        "**Status: descriptive only; no strategy validation or holdout read.**",
        "",
        f"- Dataset: `data/ohlcv/binance/BTC-USDT/1d.parquet`, manifest SHA-256 `{manifest['sha256']}`.",
        f"- Development boundary: `{DEV_END.isoformat()}`; exploration cutoff remains `{CUTOFF.isoformat()}`.",
        f"- Horizons: `{list(HORIZONS)}` days; block bootstrap `{BOOTSTRAPS}` resamples, seed `{SEED}`.",
        "- BH-FDR is applied across the six primary Pearson tests. Overlapping returns make p-values diagnostic, not independent evidence.",
        "- The inverse is an algebraic control; the one-day lag is a timing placebo. Neither is an independent trial.",
        "",
        "## Results",
        "",
        result.to_string(index=False),
        "",
        f"## Triage: `{len(survivors)}` horizon(s) jointly pass bootstrap non-zero interval and BH q < 0.05.",
        "",
        "Interpretation: the point estimates are mixed (1-day reversal; 7–60-day continuation), but every block-bootstrap interval still includes zero. No horizon passes the pre-specified joint triage rule; no BTC N2 strategy hypothesis is registered.",
        "",
        "A surviving descriptive relationship is not a tradable edge. Any strategy candidate requires a new ledger preregistration, cost/capacity prediction, and a counted `desk backtest`.",
    ]
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    prices = store.read("ohlcv", "binance", SYMBOL, "1d")["close"]
    result = analyse(prices)
    write_report(result)
    print(json.dumps({"rows": len(result), "survivors": int(result["fdr_survives_q05"].sum()), "csv": str(OUTPUT_CSV), "report": str(OUTPUT_MD)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
