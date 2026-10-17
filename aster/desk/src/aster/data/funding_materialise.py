"""Materialise the R2 funding store into the standard pipeline layout.

The research funding store is a Hive-partitioned Parquet tree at
``data/r2/market/futures/um/funding_rate/symbol=<SYM>/year=<YYYY>/month=<MM>/part-0.parquet``,
imported by :mod:`aster.data.funding_rate`. The pipeline (and every
strategy that wants to read funding through the standard
:func:`aster.data.store.read` path) expects
``data/funding/binance/<SYM>/<timeframe>.parquet``.

This module bridges the two:

* it concatenates every pre-cutoff funding partition for a symbol,
* forward-fills to the requested bar frequency **causally** (the
  fixing at time *t* is the *announcement*; bars between *t* and
  *t + 8h* see the same rate; bars *before* the first fixing are
  NaN — never zero, never back-filled from a future observation),
* writes a Parquet + manifest under the standard store path.

The forward-fill is causal because the engine charges funding on the
*held* perp position at the fixing bar; the rate that applies to a
bar at time ``t`` is the last rate announced at or before ``t``.
No ``bfill`` is used.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import pandas as pd

from aster import paths
from aster.data import store
from aster.data.funding_rate import audit_local as _funding_audit_local
from aster.data.funding_rate import DEFAULT_CUTOFF


FIXING_HOURS_UTC: tuple[int, ...] = (0, 8, 16)


def _read_symbol_funding(symbol: str, cutoff: pd.Timestamp) -> pd.DataFrame:
    """Concatenate every pre-cutoff funding partition for ``symbol``.

    Returns a DataFrame indexed by tz-aware ``DatetimeIndex`` (UTC),
    with a single column ``rate`` = ``last_funding_rate`` (per 8h,
    the convention of the original Binance archive). Rows strictly
    before the cutoff are kept; rows at or after the cutoff are
    dropped (defence in depth — the importer already enforces this).
    """
    base = paths.path("data", "r2", "market", "futures", "um", "funding_rate",
                       f"symbol={symbol}")
    if not base.is_dir():
        raise FileNotFoundError(
            f"no funding rate store for {symbol} at {base}; run the Q3 import"
        )
    parts: list[pd.DataFrame] = []
    for part in sorted(base.rglob("part-0.parquet")):
        df = pd.read_parquet(part)
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ValueError(f"{part}: funding partition must have DatetimeIndex")
        if df.index.tz is None:
            df.index = df.index.tz_localize("UTC")
        else:
            df.index = df.index.tz_convert("UTC")
        df = df[df.index < cutoff]
        if df.empty:
            continue
        # The original archive stores ``last_funding_rate`` (per 8h) plus
        # ``funding_interval_hours``. We keep only the rate.
        if "last_funding_rate" not in df.columns:
            raise ValueError(f"{part}: missing 'last_funding_rate'")
        parts.append(df[["last_funding_rate"]].rename(columns={"last_funding_rate": "rate"}))
    if not parts:
        raise ValueError(
            f"no pre-cutoff funding partitions for {symbol}; audit says: "
            f"{_funding_audit_local([symbol], cutoff=cutoff)}"
        )
    out = pd.concat(parts).sort_index()
    out = out[~out.index.duplicated(keep="last")]
    if (out.index >= cutoff).any():
        raise ValueError(f"{symbol}: materialised funding crosses the cutoff {cutoff.isoformat()}")
    out.index.name = "ts"
    return out


def _reindex_to_bar(funding: pd.DataFrame, bar_index: pd.DatetimeIndex) -> pd.DataFrame:
    """Forward-fill funding to the bar index *causally*.

    The fixing at time ``t`` is the announcement that applies to all
    bars in ``[t, t + 8h)``. The forward-fill respects this:

    * bars at or after the first fixing see the last announced rate,
    * bars before the first fixing stay NaN (a missing observation,
      never zero — a zero would mean a free short perp leg).

    No ``bfill`` is used. A bar after the last announced rate also
    stays NaN, which is correct: a bar after the last data point
    must not borrow a stale rate forever.
    """
    if not isinstance(bar_index, pd.DatetimeIndex) or bar_index.tz is None:
        raise ValueError("bar_index must be a tz-aware UTC DatetimeIndex")
    bar_index = bar_index.tz_convert("UTC")
    # ``reindex(...).ffill()`` is causal: a bar at t sees the last
    # funding value at or before t, never the next one.
    out = funding.reindex(funding.index.union(bar_index)).sort_index().ffill()
    out = out.reindex(bar_index)
    return out


def materialise_funding_panel(
    symbols: Iterable[str],
    *,
    bar_index: pd.DatetimeIndex,
    exchange: str = "binance",
    timeframe: str = "8h",
    cutoff: pd.Timestamp = DEFAULT_CUTOFF,
) -> dict[str, pd.DataFrame]:
    """Build a per-symbol wide funding panel aligned to ``bar_index``.

    Returns a dict ``symbol -> DataFrame`` (one column ``rate``,
    ``bar_index`` rows). Each value is the last announced funding
    rate at or before that bar (causal forward-fill).

    Side effect: writes a Parquet + manifest under
    ``data/funding/<exchange>/<symbol>/<timeframe>.parquet`` for each
    symbol, so the standard :func:`aster.data.store.load_funding`
    path works end to end.
    """
    panels: dict[str, pd.DataFrame] = {}
    for sym in dict.fromkeys(symbols):
        raw = _read_symbol_funding(sym, cutoff=cutoff)
        aligned = _reindex_to_bar(raw, bar_index)
        panels[sym] = aligned
        # Persist the wide-bar panel so the standard store path works.
        out = aligned.copy()
        out.columns = ["rate"]
        source = (
            "derived:pre-cutoff-r2-funding-rate; "
            f"source_symbol={sym}; cutoff_exclusive={cutoff.isoformat()}; "
            f"bar_index={bar_index[0].isoformat()}..{bar_index[-1].isoformat()}; "
            f"fixing_hours_utc={FIXING_HOURS_UTC}"
        )
        store.write(out, "funding", exchange, sym, timeframe, source=source)
        manifest = store.manifest("funding", exchange, sym, timeframe)
        # Embed a small note about the forward-fill for the audit.
        manifest["forward_fill"] = "causal ffill on bar_index, no bfill"
        Path(manifest_path := store.dataset_path("funding", exchange, sym, timeframe)
             .with_suffix(".manifest.json")).write_text(json.dumps(manifest, indent=2))
    return panels


def perp_fixing_rate_per_bar(bar_index: pd.DatetimeIndex) -> pd.Series:
    """Return a 1.0/0.0 series: 1 on a bar that IS a 00/08/16 UTC fixing.

    Used by the engine to charge funding only on the fixing bar (the
    real Binance funding event), not on every bar in between. A bar
    is a fixing bar when its UTC hour is in {0, 8, 16} and the bar
    resolution is fine enough to align to the hour.
    """
    if not isinstance(bar_index, pd.DatetimeIndex) or bar_index.tz is None:
        raise ValueError("bar_index must be tz-aware UTC")
    hours = bar_index.tz_convert("UTC").hour
    minutes = bar_index.tz_convert("UTC").minute
    return pd.Series(
        ((hours.isin(FIXING_HOURS_UTC)) & (minutes == 0)).astype(float),
        index=bar_index,
    )


__all__ = [
    "FIXING_HOURS_UTC",
    "materialise_funding_panel",
    "perp_fixing_rate_per_bar",
]
