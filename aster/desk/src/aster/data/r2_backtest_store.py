"""Materialise daily spot OHLCV only from the sealed pre-cutoff R2 minute store.

The generic backtest pipeline reads ``data/ohlcv``.  It must never solve a
missing dataset by fetching current exchange history: that would cross the desk
exploration cutoff.  This bridge creates its daily inputs solely from
:func:`aster.data.r2_klines.read_local`, which rejects post-cutoff rows, and
records that provenance in the normal store manifest.

This module is data plumbing, not a signal calculation and not a backtest.
"""
from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

from aster.data import store
from aster.data.bars import build_bars, normalise_clock
from aster.data.r2_klines import CUTOFF, read_local

R2_TO_PIPELINE_SYMBOL = {
    "BTCUSDT": "BTC/USDT",
    "ETHUSDT": "ETH/USDT",
    "SOLUSDT": "SOL/USDT",
    "BNBUSDT": "BNB/USDT",
    "XRPUSDT": "XRP/USDT",
    "DOGEUSDT": "DOGE/USDT",
    "LINKUSDT": "LINK/USDT",
    "XMRUSDT": "XMR/USDT",
    "AAVEUSDT": "AAVE/USDT",
    "SUIUSDT": "SUI/USDT",
    "NEARUSDT": "NEAR/USDT",
    "FETUSDT": "FET/USDT",
}


def daily_from_minutes(minutes: pd.DataFrame) -> pd.DataFrame:
    """Build close-labelled 1d bars and prove they remain entirely pre-cutoff."""
    repaired, _ = normalise_clock(minutes)
    bars = build_bars(repaired, "1d", label="close", drop_frozen=False)
    if not isinstance(bars.index, pd.DatetimeIndex) or bars.index.tz is None:
        raise ValueError("derived daily bars must have a tz-aware index")
    # A close-labelled bar at cutoff would include source minutes up to the
    # cutoff boundary; it is not part of the exploration sample.
    bars = bars[bars.index < CUTOFF].copy()
    if bars.empty:
        raise ValueError("no complete pre-cutoff daily bars were built")
    required = ["open", "high", "low", "close", "volume", "quote_volume", "trades"]
    return bars[required]


def materialise_daily(symbols: Iterable[str], exchange: str = "binance") -> dict[str, dict]:
    """Write daily pipeline datasets with immutable pre-cutoff provenance."""
    results: dict[str, dict] = {}
    for r2_symbol in symbols:
        if r2_symbol not in R2_TO_PIPELINE_SYMBOL:
            raise ValueError(f"no pipeline symbol mapping for {r2_symbol}")
        minutes = read_local(r2_symbol)
        bars = daily_from_minutes(minutes)
        pipeline_symbol = R2_TO_PIPELINE_SYMBOL[r2_symbol]
        path = store.write(
            bars,
            "ohlcv",
            exchange,
            pipeline_symbol,
            "1d",
            source=("derived:pre-cutoff-r2-spot-klines-1m; "
                    f"source_symbol={r2_symbol}; cutoff_exclusive={CUTOFF.isoformat()}"),
        )
        results[pipeline_symbol] = {
            "path": str(path), "rows": int(len(bars)),
            "start": bars.index[0].isoformat(), "end": bars.index[-1].isoformat(),
            "cutoff_exclusive": CUTOFF.isoformat(),
        }
    return results


def main() -> int:
    # The configured daily universe is deliberately explicit: it avoids silently
    # expanding a strategy universe and preserves the pipeline's current scope.
    from aster import paths
    cfg = paths.load_config("desk")
    pipeline_symbols = list(cfg["universe"])
    inverse = {v: k for k, v in R2_TO_PIPELINE_SYMBOL.items()}
    r2_symbols = [inverse[s] for s in pipeline_symbols]
    result = materialise_daily(r2_symbols, exchange=cfg["exchange"])
    for symbol, item in result.items():
        print(symbol, item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
