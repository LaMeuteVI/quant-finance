"""Fixed BTC/ETH inter-asset descriptive diagnostics, pre-cutoff only.

The lead-lag design is causal: a leader's trailing return ending at t-k is
compared with the target's forward return from t to t+h.  This module makes no
strategy claim and never reads the sealed holdout.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr

from aster.data import store

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
DEV_END = pd.Timestamp("2022-10-11", tz="UTC")
HORIZONS = (1, 3, 7, 14, 30, 60)
LAGS = (0, 1, 3, 7)
SEED = 20261014
BOOTSTRAPS = 10_000
OUTPUT_CSV = Path("research/assets/2026-10-14-inter-asset-btc-eth.csv")
OUTPUT_MD = Path("research/assets/2026-10-14-inter-asset-btc-eth.md")


def _bh_adjust(values: np.ndarray) -> np.ndarray:
    p = np.asarray(values, dtype=float)
    n = len(p)
    order = np.argsort(p)
    out = np.empty(n, dtype=float)
    running = 1.0
    for rank in range(n, 0, -1):
        i = order[rank - 1]
        running = min(running, p[i] * n / rank)
        out[i] = running
    return out


def _block_indices(n: int, block: int, rng: np.random.Generator) -> np.ndarray:
    starts = rng.integers(0, n, size=int(np.ceil(n / block)))
    return ((starts[:, None] + np.arange(block)[None, :]) % n).ravel()[:n]


def _corr_ci(x: np.ndarray, y: np.ndarray, block: int, rng: np.random.Generator) -> tuple[float, float]:
    values = np.empty(BOOTSTRAPS)
    for i in range(BOOTSTRAPS):
        idx = _block_indices(len(x), block, rng)
        values[i] = np.corrcoef(x[idx], y[idx])[0, 1]
    return float(np.percentile(values, 2.5)), float(np.percentile(values, 97.5))


def _formation(close: pd.Series, h: int) -> pd.Series:
    """Trailing h-day log return known at timestamp t."""
    return np.log(close) - np.log(close).shift(h)


def _forward(close: pd.Series, h: int) -> pd.Series:
    """Forward h-day log return from timestamp t; label only, never a feature."""
    return np.log(close).shift(-h) - np.log(close)


def analyse(panel: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if panel.index.tz is None or (panel.index >= CUTOFF).any():
        raise ValueError("inter-asset input must be UTC and strictly pre-cutoff")
    panel = panel.loc[panel.index <= DEV_END, ["BTC/USDT", "ETH/USDT"]].dropna().sort_index()
    rng = np.random.default_rng(SEED)
    rows: list[dict] = []
    pvalues: list[float] = []

    for h in HORIZONS:
        btc_form = _formation(panel["BTC/USDT"], h)
        eth_form = _formation(panel["ETH/USDT"], h)
        btc_fwd = _forward(panel["BTC/USDT"], h)
        eth_fwd = _forward(panel["ETH/USDT"], h)

        same = pd.concat({"btc": btc_form, "eth": eth_form}, axis=1).dropna()
        corr, pvalue = pearsonr(same["btc"], same["eth"])
        rank_corr, _ = spearmanr(same["btc"], same["eth"])
        lo, hi = _corr_ci(same["btc"].to_numpy(), same["eth"].to_numpy(), max(5, h), rng)
        rows.append({"kind": "contemporaneous", "horizon_days": h, "lag_days": 0,
                     "direction": "BTC_to_ETH", "observations": len(same),
                     "correlation": float(corr), "spearman": float(rank_corr),
                     "p_value": float(pvalue), "bootstrap_lo": lo, "bootstrap_hi": hi,
                     "bootstrap_excludes_zero": bool(lo > 0 or hi < 0)})
        pvalues.append(float(pvalue))

        for lag in LAGS:
            for direction, leader_form, target_fwd in (
                ("BTC_to_ETH", btc_form.shift(lag), eth_fwd),
                ("ETH_to_BTC", eth_form.shift(lag), btc_fwd),
            ):
                valid = pd.concat({"leader": leader_form, "target": target_fwd}, axis=1).dropna()
                corr, pvalue = pearsonr(valid["leader"], valid["target"])
                rows.append({"kind": "lead_lag", "horizon_days": h, "lag_days": lag,
                             "direction": direction, "observations": len(valid),
                             "correlation": float(corr), "spearman": np.nan,
                             "p_value": float(pvalue), "bootstrap_lo": np.nan,
                             "bootstrap_hi": np.nan, "bootstrap_excludes_zero": False})
                pvalues.append(float(pvalue))

    leadlag = pd.DataFrame(rows)
    leadlag["bh_q_value"] = _bh_adjust(np.array(pvalues))

    annual_rows: list[dict] = []
    for year, group in panel.groupby(panel.index.year):
        btc = np.log(group["BTC/USDT"]).diff()
        eth = np.log(group["ETH/USDT"]).diff()
        valid = pd.concat({"btc": btc, "eth": eth}, axis=1).dropna()
        corr, pvalue = pearsonr(valid["btc"], valid["eth"])
        annual_rows.append({"year": int(year), "observations": len(valid),
                            "correlation": float(corr), "p_value": float(pvalue)})

    # Residual test: remove contemporaneous same-horizon co-movement, then test
    # whether a lagged leader explains the target residual. At lag 0 this is a
    # deliberate zero-information control, not a claimed lead-lag edge.
    residual_rows: list[dict] = []
    for h in HORIZONS:
        btc_form = _formation(panel["BTC/USDT"], h)
        eth_form = _formation(panel["ETH/USDT"], h)
        btc_fwd = _forward(panel["BTC/USDT"], h)
        eth_fwd = _forward(panel["ETH/USDT"], h)
        for direction, leader_form, leader_fwd, target_fwd in (
            ("BTC_to_ETH", btc_form, btc_fwd, eth_fwd),
            ("ETH_to_BTC", eth_form, eth_fwd, btc_fwd),
        ):
            base = pd.concat({"leader_fwd": leader_fwd, "target_fwd": target_fwd}, axis=1).dropna()
            slope, intercept = np.polyfit(base["leader_fwd"], base["target_fwd"], 1)
            residual = target_fwd - (slope * leader_fwd + intercept)
            for lag in LAGS:
                valid = pd.concat({"leader": leader_form.shift(lag), "residual": residual}, axis=1).dropna()
                corr, pvalue = pearsonr(valid["leader"], valid["residual"])
                residual_rows.append({"horizon_days": h, "direction": direction,
                                      "lag_days": lag, "observations": len(valid),
                                      "residual_leader_correlation": float(corr),
                                      "p_value": float(pvalue), "slope": float(slope)})

    return leadlag, pd.DataFrame(annual_rows), pd.DataFrame(residual_rows)


def main() -> int:
    closes = store.load_closes("binance", ["BTC/USDT", "ETH/USDT"], "1d")
    leadlag, annual, residuals = analyse(closes)
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    leadlag.to_csv(OUTPUT_CSV, index=False)
    annual_path = OUTPUT_CSV.with_name("2026-10-14-inter-asset-btc-eth-annual.csv")
    residual_path = OUTPUT_CSV.with_name("2026-10-14-inter-asset-btc-eth-residuals.csv")
    annual.to_csv(annual_path, index=False)
    residuals.to_csv(residual_path, index=False)
    survivors = leadlag[(leadlag["bh_q_value"] < 0.05) & (leadlag["bootstrap_excludes_zero"])]
    lines = [
        "# BTC–ETH inter-asset descriptive study", "",
        "**Status: descriptive only; no strategy validation or holdout read.**", "",
        f"- Development boundary: `{DEV_END.isoformat()}`; cutoff: `{CUTOFF.isoformat()}`.",
        f"- Horizons: `{list(HORIZONS)}`; lags: `{list(LAGS)}`; bootstrap: `{BOOTSTRAPS}`, seed `{SEED}`.",
        "- A lead-lag row compares a trailing leader return ending at t-k with the target forward return from t to t+h.",
        "- BH-FDR is applied over the fixed 54-test grid. Overlapping returns mean the p-values are diagnostic, not independent evidence.",
        "", "## Contemporaneous and lead–lag results", "", leadlag.to_string(index=False),
        "", "## Annual one-day stability", "", annual.to_string(index=False),
        "", "## Residual diagnostics", "", residuals.to_string(index=False), "",
        f"Joint bootstrap/FDR survivors: `{len(survivors)}`. Only contemporaneous rows have bootstrap intervals by design.",
        "", "No strategy is registered from these diagnostics. A candidate would require economic mechanism, residual stability, cost/capacity analysis and a new ledger preregistration.",
    ]
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(leadlag), "annual_rows": len(annual), "residual_rows": len(residuals),
                      "survivors": len(survivors), "csv": str(OUTPUT_CSV),
                      "annual_csv": str(annual_path), "residual_csv": str(residual_path),
                      "report": str(OUTPUT_MD)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
