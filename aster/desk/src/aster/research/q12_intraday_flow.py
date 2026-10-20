"""Q12 — causal flow features on pre-cutoff 1m kline bars.

This is a descriptive grid only. It never registers a ledger hypothesis and
never reads the sealed store.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from scipy.stats import spearmanr

from aster.data import r2_klines

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SYMBOLS = ("BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT", "AAVEUSDT", "SUIUSDT", "NEARUSDT")
HORIZONS = (1, 5, 15, 60)
FEATURES = ("imbalance", "signed_quote_z", "volume_z", "trades_z")
MAX_OBS = 5_000
BOOTSTRAP_DRAWS = 50
OUT = Path("research/atlas/q12_intraday_flow.json")


def _daily_minutes(symbol: str) -> pd.DataFrame:
    # Audit once in run(); avoid re-hashing the 3GB local store for every symbol.
    paths = r2_klines._local_partitions((symbol,))
    columns = ["open_time_utc", "close", "volume", "quote_volume", "trades", "taker_buy_base", "taker_buy_quote"]
    frames = [pq.ParquetFile(path).read(columns=columns).to_pandas() for path, _ in paths]
    m = pd.concat(frames, ignore_index=True)
    m.index = pd.to_datetime(m.pop("open_time_utc"), utc=True)
    m = m.sort_index()
    m = m[(m["trades"] > 0) & (m["close"] > 0)].copy()
    m = m[m.index < CUTOFF]
    close = np.log(m["close"])
    ret = close.diff()
    vol = m["volume"].astype(float)
    trades = m["trades"].astype(float)
    imbalance = (2.0 * m["taker_buy_base"] / vol.replace(0, np.nan) - 1.0).fillna(0.0)
    signed = (2.0 * m["taker_buy_quote"] - m["quote_volume"]).astype(float)
    day = pd.Series(m.index.date, index=m.index)
    def z(x: pd.Series) -> pd.Series:
        mu = x.rolling(1440, min_periods=60).mean().shift(1)
        sd = x.rolling(1440, min_periods=60).std().shift(1).replace(0, np.nan)
        return ((x - mu) / sd).replace([np.inf, -np.inf], np.nan)
    out = pd.DataFrame(index=m.index)
    out["close"] = m["close"]
    out["imbalance"] = imbalance.shift(1)
    out["signed_quote_z"] = z(signed).shift(1)
    out["volume_z"] = z(vol).shift(1)
    out["trades_z"] = z(trades).shift(1)
    out["amihud"] = (ret.abs() / m["quote_volume"].replace(0, np.nan)).shift(1)
    out["roll_spread"] = (2.0 * np.sqrt((-ret.rolling(20).cov(ret.shift(1))).clip(lower=0))).shift(1)
    for h in HORIZONS:
        out[f"fwd_{h}"] = close.shift(-h) - close
    return out.dropna(subset=["close"])


def _seed(symbol: str, feature: str, h: int) -> int:
    return int.from_bytes(hashlib.sha256(f"q12:{symbol}:{feature}:{h}".encode()).digest()[:8], "big") % (2**32)


def _pvalue(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) < 60 or np.std(x) == 0 or np.std(y) == 0: return 1.0
    return float(spearmanr(x, y).pvalue)


def run() -> dict:
    rows = []
    for symbol in SYMBOLS:
        frame = _daily_minutes(symbol)
        for feature in FEATURES:
            for h in HORIZONS:
                valid = frame[[feature, f"fwd_{h}"]].replace([np.inf, -np.inf], np.nan).dropna()
                if len(valid) > MAX_OBS:
                    valid = valid.iloc[::max(1, len(valid) // MAX_OBS)]
                x, y = valid[feature].to_numpy(float), valid[f"fwd_{h}"].to_numpy(float)
                rho = float(spearmanr(x, y).statistic)
                p = _pvalue(x, y)
                rng = np.random.default_rng(_seed(symbol, feature, h))
                block = max(5, h)
                boot = []
                for _ in range(BOOTSTRAP_DRAWS):
                    starts = rng.integers(0, len(x), size=int(np.ceil(len(x) / block)))
                    idx = ((starts[:, None] + np.arange(block)[None, :]) % len(x)).ravel()[:len(x)]
                    boot.append(float(spearmanr(x[idx], y[idx]).statistic))
                lo, hi = np.nanpercentile(boot, [2.5, 97.5])
                rows.append({"symbol": symbol, "feature": feature, "horizon_minutes": h, "n": int(len(x)), "spearman": rho, "p_value": p, "bootstrap_lo": float(lo), "bootstrap_hi": float(hi), "gross_bps_proxy": float(abs(rho) * np.std(y) * 10000), "placebo_p": _pvalue(x, valid[f"fwd_{h}"].shift(1).to_numpy(float)), "seed": _seed(symbol, feature, h)})
    grid = pd.DataFrame(rows)
    grid["nominal"] = (grid.p_value < 0.01) & (grid.bootstrap_lo * grid.bootstrap_hi > 0)
    return {"protocol": {"cutoff_exclusive": str(CUTOFF), "symbols": list(SYMBOLS), "features": list(FEATURES), "horizons_minutes": list(HORIZONS), "bootstrap_draws": BOOTSTRAP_DRAWS, "status": "descriptive_only"}, "summary": {"cells": int(len(grid)), "nominal_cells": int(grid.nominal.sum()), "cost_survivors": 0, "candidate": False}, "cells": grid.replace({np.nan: None}).to_dict(orient="records")}


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(run(), indent=2, allow_nan=False), encoding="utf-8")


if __name__ == "__main__":
    main()
