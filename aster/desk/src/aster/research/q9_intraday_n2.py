"""Q9 — N2 per-alt descriptive grid.

The implementation reuses Q5's tested statistics but reads the local R2 spot
store through ``aster.data.store``. It enforces the development cutoff before
any observations enter a statistic and never touches the sealed store.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from aster.data.r2_backtest_store import bars_from_minutes
from aster.data.r2_klines import read_local
from aster.research.q5_intraday_n2 import (
    _autocorr,
    _hurst_rs,
    _variance_ratio,
)

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SYMBOLS = [
    "BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT",
    "XMRUSDT", "AAVEUSDT", "FETUSDT", "NEARUSDT", "SUIUSDT",
]
TIMEFRAMES = ["5m", "15m", "1h", "4h", "1d"]


def describe(close: pd.Series) -> dict:
    """Compute the preregistered Q9 N2 block for one close series."""
    if close.empty:
        raise ValueError("close series is empty")
    idx = pd.to_datetime(close.index, utc=True)
    if idx.max() >= CUTOFF:
        raise ValueError("Q9 development input crosses the cutoff")
    clean = close.copy()
    clean.index = idx
    clean = clean.sort_index()
    ret = clean.pct_change(fill_method=None).to_numpy()
    abs_ret = np.abs(ret)
    return {
        "n_obs": int(np.isfinite(ret).sum()),
        "start": str(clean.index[0]),
        "end": str(clean.index[-1]),
        "ret_autocorr": {f"lag{k}": _autocorr(ret, k) for k in (1, 2, 3, 5, 10)},
        "abs_ret_autocorr": {f"lag{k}": _autocorr(abs_ret, k) for k in (1, 2, 3, 5, 10)},
        "variance_ratio": {"q2": _variance_ratio(ret, 2), "q4": _variance_ratio(ret, 4)},
        "hurst_rs": _hurst_rs(ret),
    }


def run(symbols: list[str] | None = None, timeframes: list[str] | None = None,
        exchange: str = "binance") -> dict:
    """Run the fixed asset × timeframe grid on local pre-cutoff data."""
    symbols = symbols or SYMBOLS
    timeframes = timeframes or TIMEFRAMES
    cells: dict[str, dict] = {}
    for symbol in symbols:
        sym_cells = {}
        for timeframe in timeframes:
            minutes = read_local(symbol)
            bars = bars_from_minutes(minutes, timeframe)
            sym_cells[timeframe] = describe(pd.Series(bars["close"], index=bars.index, name="close"))
        cells[symbol] = sym_cells

    blocks = [cells[s][tf] for s in symbols for tf in timeframes]
    ret_lag1 = np.array([b["ret_autocorr"]["lag1"] for b in blocks], dtype=float)
    abs_lag1 = np.array([b["abs_ret_autocorr"]["lag1"] for b in blocks], dtype=float)
    return {
        "cutoff_exclusive": CUTOFF.isoformat(),
        "symbols": symbols,
        "timeframes": timeframes,
        "cell_count": len(blocks),
        "by_symbol": cells,
        "summary": {
            "ret_lag1_negative_cells": int(np.sum(ret_lag1 < 0)),
            "ret_lag1_positive_cells": int(np.sum(ret_lag1 > 0)),
            "abs_ret_lag1_positive_cells": int(np.sum(abs_lag1 > 0)),
            "ret_lag1_mean": float(np.nanmean(ret_lag1)),
            "abs_ret_lag1_mean": float(np.nanmean(abs_lag1)),
            "hurst_min": float(np.nanmin([b["hurst_rs"] for b in blocks])),
            "hurst_max": float(np.nanmax([b["hurst_rs"] for b in blocks])),
        },
    }


def main() -> None:
    from aster.cli import paths

    cfg = paths.load_config("desk")
    out = run(exchange=cfg.get("exchange", "binance"))
    path = Path("research/atlas/q9_intraday_n2.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True))
    print(f"wrote {path} ({path.stat().st_size} bytes)")
    print(f"cells={out['cell_count']} summary={out['summary']}")


if __name__ == "__main__":
    main()
