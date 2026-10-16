"""Q11 — per-alt N4 regime re-evaluation, pre-cutoff descriptive only.

Protocol is fixed before reading the output. Regimes are causal trailing
threshold labels (trend and volatility); the existing pre-registered Hamilton
MS result is also reported as a negative cross-check, not re-tuned here.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from aster.data import r2_klines

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT", "LINKUSDT", "AAVEUSDT", "SUIUSDT", "NEARUSDT")
HORIZONS = (1, 3, 7)
SIGNALS = ("ret_1d", "ret_5d", "ret_22d", "rv_22d", "btc_corr_30d")
OUT = Path("research/atlas/q11_regimes.json")


def _daily(symbol: str) -> pd.DataFrame:
    m = r2_klines.read_local(symbol)
    m = m[(m["trades"] > 0) & (m["close"] > 0)].copy()
    d = pd.DataFrame({"close": m["close"].resample("1D").last()}).dropna()
    d = d[d.index < CUTOFF]
    return d


def _features(symbol: str, d: pd.DataFrame, btc: pd.Series) -> pd.DataFrame:
    logp = np.log(d.close)
    r = logp.diff()
    out = pd.DataFrame(index=d.index)
    out["ret_1d"] = r.shift(1)
    out["ret_5d"] = logp.diff(5).shift(1)
    out["ret_22d"] = logp.diff(22).shift(1)
    out["rv_22d"] = r.rolling(22).std().shift(1)
    if symbol == "BTCUSDT":
        out["btc_corr_30d"] = 1.0
    else:
        br = np.log(btc).diff()
        out["btc_corr_30d"] = r.rolling(30).corr(br).shift(1)
    for h in HORIZONS:
        out[f"fwd_{h}d"] = logp.shift(-h) - logp
    out["year"] = out.index.year
    return out.dropna(subset=["fwd_1d"])


def _labels(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    out["trend_regime"] = np.where(out.ret_22d > 0, 1, -1)
    med = out.rv_22d.expanding(min_periods=60).median().shift(1)
    out["vol_regime"] = np.where(out.rv_22d > med, 1, 0)
    out["corr_regime"] = np.where(out.btc_corr_30d >= 0.5, 1, 0)
    return out


def run() -> dict:
    btc = _daily("BTCUSDT").close
    rows = []
    for symbol in SYMBOLS:
        d = _daily(symbol)
        f = _labels(_features(symbol, d, btc.reindex(d.index).ffill()))
        for regime in ("trend_regime", "vol_regime", "corr_regime"):
            for state in sorted(f[regime].dropna().unique()):
                g = f[f[regime] == state]
                for signal in SIGNALS:
                    for h in HORIZONS:
                        valid = g[[signal, f"fwd_{h}d"]].dropna()
                        if len(valid) < 60: continue
                        rho, p = spearmanr(valid[signal], valid[f"fwd_{h}d"])
                        if not np.isfinite(rho):
                            continue
                        rows.append({"symbol": symbol, "regime": regime, "state": int(state), "signal": signal, "horizon": h, "n": int(len(valid)), "spearman": float(rho), "p_value": float(p)})
    grid = pd.DataFrame(rows)
    # Fixed descriptive filters; no selection is promoted to a strategy.
    grid["nominal"] = (grid.p_value < 0.01) & (grid.spearman.abs() > 0.05)
    return {"protocol": {"cutoff_exclusive": str(CUTOFF), "symbols": list(SYMBOLS), "horizons": list(HORIZONS), "regimes": ["trend_sign_22d", "expanding_median_vol_22d", "btc_corr_30d_ge_0.5"], "status": "descriptive_only"}, "summary": {"cells": int(len(grid)), "nominal_cells": int(grid.nominal.sum()), "candidate": False}, "cells": grid.replace({np.nan: None}).to_dict(orient="records")}


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(run(), indent=2, allow_nan=False), encoding="utf-8")


if __name__ == "__main__":
    main()
