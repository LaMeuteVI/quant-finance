"""Materialise spot bars at any timeframe from the sealed pre-cutoff R2 minute store.

The generic backtest pipeline reads ``data/ohlcv``.  It must never solve a
missing dataset by fetching current exchange history: that would cross the desk
exploration cutoff.  This bridge creates its daily (1d) and intraday
(5m/15m/1h/4h) inputs solely from :func:`aster.data.r2_klines.read_local`,
which rejects post-cutoff rows, and records that provenance in the normal
store manifest.

This module is data plumbing, not a signal calculation and not a backtest.
Per-hypothesis timeframe and instrument selection (P2) live in the prereg
ledger, not here: the bridge is a deterministic resampler with a hard
2024-07-01 UTC cutoff, called once per (symbol, timeframe) pair.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass

import pandas as pd

from aster.data import store
from aster.data.bars import TIMEFRAMES, build_bars, normalise_clock
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

# The 1d default timeframes that P1 used, kept here so callers without a
# prereg can still reproduce the legacy materialise_daily() behaviour.
DEFAULT_TIMEFRAMES: tuple[str, ...] = ("1d",)

# What the QA pre-flight and the materialise step are willing to build.
SUPPORTED_TIMEFRAMES: frozenset[str] = frozenset(TIMEFRAMES.keys())


@dataclass(frozen=True)
class BarsManifest:
    """Provenance for a single (symbol, timeframe) materialisation.

    ``cutoff_exclusive`` is the literal cutoff the bar builder honoured:
    every row in the produced frame is strictly before it.
    """

    symbol: str
    timeframe: str
    path: str
    rows: int
    start: str
    end: str
    cutoff_exclusive: str

    def as_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "path": self.path,
            "rows": self.rows,
            "start": self.start,
            "end": self.end,
            "cutoff_exclusive": self.cutoff_exclusive,
        }


def bars_from_minutes(minutes: pd.DataFrame, timeframe: str,
                      *, label: str = "close", drop_frozen: bool = False) -> pd.DataFrame:
    """Build close-labelled bars at ``timeframe`` and prove they remain pre-cutoff."""
    if timeframe not in SUPPORTED_TIMEFRAMES:
        raise ValueError(
            f"unsupported timeframe {timeframe!r}; expected one of {sorted(SUPPORTED_TIMEFRAMES)}"
        )
    if label != "close":
        raise ValueError("label must be 'close' (research default); plotting-only labels are not exported")
    repaired, _ = normalise_clock(minutes)
    bars = build_bars(repaired, timeframe, label="close", drop_frozen=drop_frozen)
    if not isinstance(bars.index, pd.DatetimeIndex) or bars.index.tz is None:
        raise ValueError("derived bars must have a tz-aware index")
    # A close-labelled bar at cutoff would include source minutes up to the
    # cutoff boundary; it is not part of the exploration sample.
    bars = bars[bars.index < CUTOFF].copy()
    if bars.empty:
        raise ValueError(f"no complete pre-cutoff bars at {timeframe}")
    required = ["open", "high", "low", "close", "volume", "quote_volume", "trades"]
    return bars[required]


# Backwards-compatible alias used by tests and the legacy daily CLI.
def daily_from_minutes(minutes: pd.DataFrame) -> pd.DataFrame:
    """Build close-labelled 1d bars and prove they remain entirely pre-cutoff."""
    return bars_from_minutes(minutes, "1d")


def materialise_daily(symbols: Iterable[str], exchange: str = "binance") -> dict[str, dict]:
    """Write 1d pipeline datasets with immutable pre-cutoff provenance.

    Kept as a thin wrapper around :func:`materialise_bars` for callers that
    hard-code the daily horizon (legacy daily strategies, regression tests).
    """
    return materialise_bars(symbols, DEFAULT_TIMEFRAMES, exchange=exchange)


def materialise_bars(symbols: Iterable[str], timeframes: Iterable[str],
                     exchange: str = "binance") -> dict[tuple[str, str], BarsManifest]:
    """Materialise every (symbol, timeframe) the preregistration asks for.

    Each call writes a parquet + manifest under
    ``data/ohlcv/<exchange>/<symbol>/<timeframe>.parquet`` and returns a
    mapping ``(pipeline_symbol, timeframe) -> BarsManifest``.  Symbols not
    present in :data:`R2_TO_PIPELINE_SYMBOL` raise ``ValueError`` before
    any file is written; timeframes not in :data:`SUPPORTED_TIMEFRAMES`
    raise ``ValueError`` for the same reason.  The pre-cutoff invariant
    is enforced by :func:`bars_from_minutes`.
    """
    tfs = tuple(timeframes)
    if not tfs:
        raise ValueError("materialise_bars requires at least one timeframe")
    for tf in tfs:
        if tf not in SUPPORTED_TIMEFRAMES:
            raise ValueError(
                f"unsupported timeframe {tf!r}; expected one of {sorted(SUPPORTED_TIMEFRAMES)}"
            )
    results: dict[tuple[str, str], BarsManifest] = {}
    # First pass: validate every (symbol, timeframe) without writing, so a
    # misconfiguration in the prereg fails fast and atomically.
    plan: list[tuple[str, str, str]] = []
    for r2_symbol in symbols:
        if r2_symbol not in R2_TO_PIPELINE_SYMBOL:
            raise ValueError(f"no pipeline symbol mapping for {r2_symbol}")
        for tf in tfs:
            plan.append((r2_symbol, R2_TO_PIPELINE_SYMBOL[r2_symbol], tf))
    for r2_symbol, pipeline_symbol, tf in plan:
        minutes = read_local(r2_symbol)
        bars = bars_from_minutes(minutes, tf)
        path = store.write(
            bars,
            "ohlcv",
            exchange,
            pipeline_symbol,
            tf,
            source=("derived:pre-cutoff-r2-spot-klines-1m; "
                    f"source_symbol={r2_symbol}; cutoff_exclusive={CUTOFF.isoformat()}; "
                    f"timeframe={tf}"),
        )
        results[(pipeline_symbol, tf)] = BarsManifest(
            symbol=pipeline_symbol,
            timeframe=tf,
            path=str(path),
            rows=int(len(bars)),
            start=bars.index[0].isoformat(),
            end=bars.index[-1].isoformat(),
            cutoff_exclusive=CUTOFF.isoformat(),
        )
    return results


def summarise(results: Mapping[tuple[str, str], BarsManifest]) -> list[dict]:
    """JSON-ready list of BarsManifest, sorted for stable CLI output."""
    return [results[k].as_dict() for k in sorted(results.keys())]


def main() -> int:
    # The configured daily universe is deliberately explicit: it avoids silently
    # expanding a strategy universe and preserves the pipeline's current scope.
    from aster import paths
    cfg = paths.load_config("desk")
    pipeline_symbols = list(cfg["universe"])
    inverse = {v: k for k, v in R2_TO_PIPELINE_SYMBOL.items()}
    r2_symbols = [inverse[s] for s in pipeline_symbols]
    tfs = tuple(cfg.get("timeframes", DEFAULT_TIMEFRAMES))
    result = materialise_bars(r2_symbols, tfs, exchange=cfg["exchange"])
    for key, item in result.items():
        print(key, item.as_dict())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
