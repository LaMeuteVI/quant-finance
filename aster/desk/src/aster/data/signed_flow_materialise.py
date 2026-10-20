"""Exact, pre-cutoff signed-flow panels from spot aggTrades.

This is a research data bridge, not a strategy. It aggregates every local
Parquet partition file-by-file so each time bar receives the numerator and
denominator from all trades in that bar. It deliberately does not use the
legacy strided ``max_rows`` shortcut: that shortcut creates a random-subset
VWAP/flow panel and is invalid for a backtest.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

from aster.data.r2_klines import CUTOFF

DEFAULT_ROOT = Path("data/r2/market/spot/aggtrades")


def _r2_symbol(symbol: str) -> str:
    """Translate a pipeline symbol to the Binance R2 symbol namespace."""
    return symbol.replace("/", "").replace("-", "").replace(":USDT", "")


def _pipeline_symbol(symbol: str) -> str:
    """Translate an R2/desk symbol to the pipeline spot namespace."""
    s = symbol.replace(":USDT", "")
    s = s.replace("-", "/") if "-" in s else s
    if "/" not in s and s.endswith("USDT"):
        s = s[:-4] + "/USDT"
    return s


def _partition_files(root: Path, r2_symbol: str) -> list[Path]:
    symbol_root = root / f"symbol={r2_symbol}"
    return sorted(symbol_root.glob("year=*/month=*/part-*.parquet"))


def _aggregate_partition(path: Path, timeframe: str) -> pd.DataFrame:
    """Return signed and total quantity by close-labelled bar for one file."""
    raw = pd.read_parquet(
        path,
        columns=["price", "quantity", "transact_time", "is_buyer_maker"],
    )
    if raw.empty:
        return pd.DataFrame(columns=["signed", "total"])
    ts = pd.to_datetime(raw["transact_time"], unit="ms", utc=True)
    if ts.max() >= CUTOFF:
        raise ValueError(f"aggTrades partition crosses cutoff: {path}")
    qty = pd.to_numeric(raw["quantity"], errors="coerce").fillna(0.0)
    maker = raw["is_buyer_maker"].astype(bool).to_numpy()
    frame = pd.DataFrame(
        {"signed": np.where(maker, -qty.to_numpy(), qty.to_numpy()),
         "total": qty.abs().to_numpy()},
        index=pd.DatetimeIndex(ts),
    )
    # Close labels match data.bars.build_bars: [start, end), labelled at end.
    return frame.resample(timeframe, label="right", closed="left").sum()


def load_signed_flow(
    symbol: str,
    bar_index: pd.DatetimeIndex,
    *,
    timeframe: str = "15min",
    root: Path | str = DEFAULT_ROOT,
) -> pd.Series:
    """Load one exact signed-flow series aligned to an existing price index."""
    root = Path(root)
    r2 = _r2_symbol(symbol)
    files = _partition_files(root, r2)
    if not files:
        raise FileNotFoundError(f"no aggTrades partitions for {r2} below {root}")
    partials = [_aggregate_partition(path, timeframe) for path in files]
    grouped = pd.concat(partials).groupby(level=0).sum().sort_index()
    denom = grouped["total"].replace(0.0, np.nan)
    flow = (grouped["signed"] / denom).replace([np.inf, -np.inf], np.nan)
    flow.index = pd.DatetimeIndex(flow.index)
    flow = flow[flow.index < CUTOFF]
    return flow.reindex(pd.DatetimeIndex(bar_index))


def load_signed_flow_panel(
    symbols: Iterable[str],
    bar_index: pd.DatetimeIndex,
    *,
    timeframe: str = "15min",
    root: Path | str = DEFAULT_ROOT,
) -> pd.DataFrame:
    """Load a finite-column panel in the same namespace as ``symbols``."""
    out = {}
    for symbol in symbols:
        out[symbol] = load_signed_flow(symbol, bar_index, timeframe=timeframe, root=root)
    return pd.DataFrame(out, index=bar_index)


def panel_report(panel: pd.DataFrame, *, cutoff: pd.Timestamp = CUTOFF) -> dict:
    """Shape and cutoff evidence stored in the desk report."""
    finite = panel.replace([np.inf, -np.inf], np.nan).count()
    return {
        "rows": int(len(panel)),
        "columns": [str(c) for c in panel.columns],
        "finite_by_column": {str(k): int(v) for k, v in finite.items()},
        "cutoff_exclusive": cutoff.isoformat(),
        "max_index": panel.index.max().isoformat() if len(panel) else None,
        "all_values_in_range": bool(panel.index.max() < cutoff) if len(panel) else True,
    }
