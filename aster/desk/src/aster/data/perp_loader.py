"""Load perp data (Q3b) into the standard pipeline layout.

The Q3b importer writes Hive-partitioned Parquet under
``data/r2/market/futures/um/<stream>/symbol=<SYM>/year=<YYYY>/month=<MM>/part-0.parquet``,
one partition per monthly archive, for four streams:

- ``klines_1h`` — perp 1h OHLCV (the perp close series F1v2 needs).
- ``premium_index_klines_1h`` — premium index (mark ÷ index) 1h klines.
- ``mark_price_klines_1h`` — mark price 1h klines.
- ``metrics`` — daily OI / taker volume / top trader long/short ratio.

This module reads those partitions and:

- returns a **wide close** panel (tz-aware UTC index x symbols) for the
  kline streams, aligned to the same bar index the pipeline uses;
- returns a **long-form** metrics frame (ts, symbol, columns) for the
  daily stream;
- writes a Parquet + manifest under the standard
  ``data/perpetuals/<exchange>/<symbol>/<timeframe>.parquet`` path so the
  pipeline (and the engine's ``perp_close`` kwarg) can read it via the
  standard store API.

The pre-cutoff invariant is enforced by the importer; we re-assert it
here as defence in depth.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from aster import paths
from aster.data import store
from aster.data.funding_materialise import _reindex_to_bar  # noqa: F401
from aster.data.funding_rate import DEFAULT_CUTOFF


KLINE_STREAMS: frozenset[str] = frozenset(
    {"klines_1h", "premium_index_klines_1h", "mark_price_klines_1h"}
)


def _stream_root(stream: str) -> Path:
    if stream in KLINE_STREAMS:
        return paths.path(
            "data", "r2", "market", "futures", "um", stream,
        )
    if stream == "metrics":
        return paths.path(
            "data", "r2", "market", "futures", "um", "metrics",
        )
    raise ValueError(f"unknown perp stream {stream!r}")


def _symbol_root(stream: str, symbol: str) -> Path:
    return _stream_root(stream) / f"symbol={symbol}"


def _read_kline_symbol(symbol: str, stream: str,
                        cutoff: pd.Timestamp) -> pd.DataFrame:
    """Read every pre-cutoff kline partition for one symbol/stream."""
    base = _symbol_root(stream, symbol)
    if not base.is_dir():
        raise FileNotFoundError(
            f"no {stream} for {symbol} at {base}; run `python -m aster.scripts.q3b_download_perp`"
        )
    parts: list[pd.DataFrame] = []
    for part in sorted(base.rglob("part-0.parquet")):
        df = pd.read_parquet(part)
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ValueError(f"{part}: kline partition must have DatetimeIndex")
        if df.index.tz is None:
            df.index = df.index.tz_localize("UTC")
        else:
            df.index = df.index.tz_convert("UTC")
        df = df[df.index < cutoff]
        if df.empty:
            continue
        # The schema (perp_data.KLINE_COLUMNS) is the same for klines,
        # premiumIndexKlines, and markPriceKlines. We keep all
        # columns the importer stored.
        parts.append(df)
    if not parts:
        raise ValueError(
            f"no pre-cutoff {stream} partitions for {symbol} at {base}"
        )
    out = pd.concat(parts).sort_index()
    out = out[~out.index.duplicated(keep="last")]
    if (out.index >= cutoff).any():
        raise ValueError(f"{symbol}/{stream}: materialised data crosses the cutoff {cutoff.isoformat()}")
    return out


def load_perp_close(symbols: Iterable[str],
                    *,
                    bar_index: pd.DatetimeIndex,
                    exchange: str = "binance",
                    stream: str = "klines_1h",
                    cutoff: pd.Timestamp = DEFAULT_CUTOFF) -> pd.DataFrame:
    """Wide close-price perp panel (UTC index x symbols), aligned to
    ``bar_index`` via causal forward-fill. For the perp kline stream
    (or premium / mark), a bar at time ``t`` sees the last observed
    perp close at or before ``t``. Side effect: persists the wide panel
    under ``data/perpetuals/<exchange>/<symbol>/<stream>.parquet``.
    """
    if stream not in KLINE_STREAMS:
        raise ValueError(
            f"stream {stream!r} not a kline stream; use load_perp_metrics()"
        )
    panels: dict[str, pd.Series] = {}
    for sym in dict.fromkeys(symbols):
        df = _read_kline_symbol(sym, stream, cutoff=cutoff)
        close = df["close"]
        # Reindex to bar_index, causal ffill (no bfill).
        aligned = _reindex_to_bar(close.to_frame(name="close"), bar_index)
        panels[sym] = aligned["close"]
        # Persist the wide-bar panel under the standard store path so
        # the engine and pipeline can load it via the regular store API.
        out = aligned.copy()
        out.columns = ["close"]
        source = (
            f"derived:pre-cutoff-r2-perp-{stream}; "
            f"source_symbol={sym}; cutoff_exclusive={cutoff.isoformat()}; "
            f"bar_index={bar_index[0].isoformat()}..{bar_index[-1].isoformat()}"
        )
        store.write(out, "perpetuals", exchange, sym, stream, source=source)
    return pd.DataFrame(panels).sort_index()


def load_perp_metrics(symbols: Iterable[str],
                       *,
                       exchange: str = "binance",
                       cutoff: pd.Timestamp = DEFAULT_CUTOFF) -> pd.DataFrame:
    """Return a long-form metrics frame (ts, symbol, columns) for all
    symbols. Persists a per-symbol metrics parquet under
    ``data/perpetuals/<exchange>/<symbol>/metrics.parquet``.
    """
    rows: list[pd.DataFrame] = []
    for sym in dict.fromkeys(symbols):
        df = _read_kline_symbol(sym, "metrics", cutoff=cutoff)
        df = df.copy()
        df["symbol"] = sym
        rows.append(df)
    if not rows:
        return pd.DataFrame()
    out = pd.concat(rows).sort_index()
    out.index.name = "ts"
    # Persist per symbol so the standard store API works.
    for sym, g in out.groupby("symbol"):
        per_sym = g.drop(columns=["symbol"])
        source = (
            f"derived:pre-cutoff-r2-perp-metrics; "
            f"source_symbol={sym}; cutoff_exclusive={cutoff.isoformat()}"
        )
        store.write(per_sym, "perpetuals", exchange, sym, "metrics", source=source)
    return out


def audit_perp_streams(symbols: Iterable[str],
                        *,
                        cutoff: pd.Timestamp = DEFAULT_CUTOFF,
                        verify_sha256: bool = False) -> dict:
    """Audit every (stream, symbol) Q3b wrote. Returns a dict with
    per-stream stats, the same shape as the funding audit. Mirrors
    :func:`aster.data.funding_rate.audit_local` so callers can
    compare funding vs perp data with the same operator contract.
    """
    streams: dict[str, dict] = {}
    for stream in (*KLINE_STREAMS, "metrics"):
        parts_total = 0
        rows_total = 0
        bytes_total = 0
        symbols_present: list[str] = []
        any_post_cutoff = False
        for sym in dict.fromkeys(symbols):
            base = _symbol_root(stream, sym)
            if not base.is_dir():
                continue
            parts = sorted(base.rglob("part-0.parquet"))
            for p in parts:
                try:
                    df = pd.read_parquet(p)
                except Exception as exc:
                    streams[stream] = {"ok": False, "error": f"{p}: {exc}"}
                    return streams
                if not isinstance(df.index, pd.DatetimeIndex):
                    streams[stream] = {
                        "ok": False,
                        "error": f"{p}: index not a DatetimeIndex",
                    }
                    return streams
                if (df.index >= cutoff).any():
                    any_post_cutoff = True
                rows_total += len(df)
                bytes_total += p.stat().st_size
                parts_total += 1
                if verify_sha256:
                    import hashlib
                    sha = hashlib.sha256(p.read_bytes()).hexdigest()
                    manifest_path = p.with_name("manifest.json")
                    if manifest_path.exists():
                        import json
                        manifest = json.loads(manifest_path.read_text())
                        if manifest.get("sha256") and manifest["sha256"] != sha:
                            streams[stream] = {
                                "ok": False,
                                "error": f"{p}: sha256 mismatch",
                            }
                            return streams
            symbols_present.append(sym)
        if not symbols_present:
            streams[stream] = {"ok": True, "partitions": 0, "rows": 0,
                                "symbols": [], "ok_no_data": True,
                                "note": "no symbols imported"}
            continue
        streams[stream] = {
            "ok": not any_post_cutoff,
            "partitions": parts_total,
            "rows": rows_total,
            "bytes": bytes_total,
            "symbols": symbols_present,
            "cutoff_exclusive": cutoff.isoformat(),
            "any_post_cutoff": any_post_cutoff,
        }
    return {
        "ok": all(v.get("ok", False) for v in streams.values()),
        "store": "r2/market/futures/um",
        "cutoff_exclusive": cutoff.isoformat(),
        "streams": streams,
    }


__all__ = [
    "KLINE_STREAMS",
    "load_perp_close",
    "load_perp_metrics",
    "audit_perp_streams",
]
