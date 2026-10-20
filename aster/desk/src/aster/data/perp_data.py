"""Import USD-M perp archives from data.binance.vision (Q3b).

Four sibling layouts are imported by this module:

- perp **klines** (1h OHLCV) — the perp close series F1v2 needs.
  Layout: ``data/futures/um/monthly/klines/<SYM>/1h/<SYM>-1h-YYYY-MM.zip``.
  Schema: 12 columns, same as spot klines.
- **premiumIndexKlines** (1h) — the mark premium index; F2 reads this.
  Same layout, same schema (12 cols), slightly different magnitudes.
- **markPriceKlines** (1h) — the perp mark price.
  Same layout, same schema.
- **metrics** (daily) — open interest + long/short ratio, daily file.
  Layout: ``data/futures/um/daily/metrics/<SYM>/<SYM>-metrics-YYYY-MM-DD.zip``.
  Schema: 8 columns, see ``METRICS_COLUMNS``.

Cutoff (2024-07-01 UTC) is enforced at import time, same as the
funding importer. Manifests are written with a SHA-256 of the
local Parquet and a row count + time bounds round-trip.

Local layout (per stream):

    data/r2/market/futures/um/{stream}/symbol=<SYM>/year=<YYYY>/month=<MM>/part-0.parquet
    data/r2/market/futures/um/{stream}/symbol=<SYM>/year=<YYYY>/month=<MM>/part-0.parquet.manifest.json

Where ``stream`` is one of ``klines_1h``, ``premium_index_klines_1h``,
``mark_price_klines_1h``, ``metrics``.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from pathlib import Path
from typing import Iterable
from zipfile import ZipFile

import pandas as pd

from aster import paths

KLINE_COLUMNS = (
    "open_time", "open", "high", "low", "close", "volume", "close_time",
    "quote_volume", "number_of_trades", "taker_buy_base_volume",
    "taker_buy_quote_volume", "ignore",
)
METRICS_COLUMNS = (
    "create_time", "symbol", "sum_open_interest", "sum_open_interest_value",
    "count_toptrader_long_short_ratio", "sum_toptrader_long_short_ratio",
    "count_long_short_ratio", "sum_taker_long_short_vol_ratio",
)
DEFAULT_CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")

_KLINE_FN = re.compile(
    r"(?P<symbol>[A-Z0-9]+)-1h-(?P<year>\d{4})-(?P<month>\d{2})\.zip$"
)
_METRICS_FN = re.compile(
    r"(?P<symbol>[A-Z0-9]+)-metrics-(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\.zip$"
)
_STREAMS_KLINE = {
    "klines_1h": "klines",
    "premium_index_klines_1h": "premiumIndexKlines",
    "mark_price_klines_1h": "markPriceKlines",
}


def _source_sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _read_kline_zip(source: Path) -> pd.DataFrame:
    if source.suffix != ".zip":
        raise ValueError(f"{source}: perp kline archives must be ZIP")
    with ZipFile(source) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"{source}: expected exactly one CSV member, found {len(names)}")
        with archive.open(names[0]) as fh:
            text = io.TextIOWrapper(fh, encoding="utf-8")
            raw = pd.read_csv(text, header=None)
    if raw.empty:
        raise ValueError(f"{source}: empty archive")
    # Vision perp kline archives publish a header row (the column
    # names). Detect it by content ("open_time" / "open time")
    # and drop it, same as the spot binance_vision importer.
    if str(raw.iloc[0, 0]).lower() in {"open time", "open_time"}:
        raw = raw.iloc[1:].reset_index(drop=True)
    if raw.shape[1] != len(KLINE_COLUMNS):
        raise ValueError(
            f"{source}: expected {len(KLINE_COLUMNS)} columns, found {raw.shape[1]}"
        )
    raw.columns = KLINE_COLUMNS
    return raw


def _read_metrics_zip(source: Path) -> pd.DataFrame:
    if source.suffix != ".zip":
        raise ValueError(f"{source}: perp metrics archives must be ZIP")
    with ZipFile(source) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"{source}: expected exactly one CSV member, found {len(names)}")
        with archive.open(names[0]) as fh:
            text = io.TextIOWrapper(fh, encoding="utf-8")
            raw = pd.read_csv(text)
    if list(raw.columns) != list(METRICS_COLUMNS):
        raise ValueError(
            f"{source}: expected columns {METRICS_COLUMNS}, found {list(raw.columns)}"
        )
    return raw


def _normalise_open_time(series: pd.Series) -> tuple[pd.Series, str]:
    numeric = pd.to_numeric(series, errors="raise")
    maximum = numeric.abs().max()
    unit = "us" if maximum >= 100_000_000_000_000 else "ms"
    return pd.to_datetime(numeric, unit=unit, utc=True), unit


def _kline_destination(stream: str, symbol: str, year: int, month: int) -> Path:
    return paths.path(
        "data", "r2", "market", "futures", "um", stream,
        f"symbol={symbol}", f"year={year:04d}", f"month={month:02d}", "part-0.parquet",
    )


def _metrics_destination(symbol: str, year: int, month: int, day: int) -> Path:
    return paths.path(
        "data", "r2", "market", "futures", "um", "metrics",
        f"symbol={symbol}", f"year={year:04d}", f"month={month:02d}", f"day={day:02d}",
        "part-0.parquet",
    )


def import_kline_archive(stream: str, source: Path,
                          cutoff: pd.Timestamp = DEFAULT_CUTOFF) -> dict:
    """Import one monthly perp kline archive (klines, premiumIndexKlines,
    markPriceKlines) into the R2 store. Cutoff is enforced strictly.
    """
    if stream not in _STREAMS_KLINE:
        raise ValueError(f"unknown stream {stream!r}; expected one of {list(_STREAMS_KLINE)}")
    match = _KLINE_FN.fullmatch(source.name)
    if not match:
        raise ValueError(f"unrecognised perp kline filename: {source.name}")
    raw = _read_kline_zip(source)
    timestamps, ts_unit = _normalise_open_time(raw["open_time"])
    raw["ts"] = timestamps
    raw = raw[raw["ts"] < cutoff].copy()
    if raw.empty:
        raise ValueError(f"{source}: no rows strictly before the cutoff {cutoff.isoformat()}")
    if (raw["ts"] >= cutoff).any():
        raise ValueError(f"{source}: archive crosses the cutoff {cutoff.isoformat()}")
    numeric_cols = [c for c in KLINE_COLUMNS if c not in {"open_time", "ignore", "close_time"}]
    raw[numeric_cols] = raw[numeric_cols].apply(pd.to_numeric, errors="raise")
    raw = raw.drop(columns=["open_time", "close_time", "ignore"]).set_index("ts").sort_index()
    raw.index.name = "ts"
    raw = raw[~raw.index.duplicated(keep="last")]

    symbol = match["symbol"]
    year, month = int(match["year"]), int(match["month"])
    destination = _kline_destination(stream, symbol, year, month)
    manifest_path = destination.with_suffix(destination.suffix + ".manifest.json")
    if destination.exists() or manifest_path.exists():
        raise FileExistsError(f"refusing to overwrite perp {stream} partition: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    raw.to_parquet(destination)
    parquet_sha = hashlib.sha256(destination.read_bytes()).hexdigest()
    archive_sha = _source_sha256(source.read_bytes())
    manifest = {
        "source": "data.binance.vision",
        "stream": stream,
        "archive_kind": _STREAMS_KLINE[stream],
        "key": f"data/futures/um/monthly/{_STREAMS_KLINE[stream]}/{symbol}/1h/{source.name}",
        "size_bytes": destination.stat().st_size,
        "sha256": parquet_sha,
        "archive_sha256": archive_sha,
        "rows": int(len(raw)),
        "start": raw.index[0].isoformat(),
        "end": raw.index[-1].isoformat(),
        "timestamp_unit": ts_unit,
        "cutoff_exclusive": cutoff.isoformat(),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    return {
        "stream": stream, "source": str(source), "symbol": symbol,
        "year": year, "month": month, "rows_imported": int(len(raw)),
        "destination": str(destination.relative_to(paths.desk_root())),
    }


def import_metrics_archive(source: Path,
                            cutoff: pd.Timestamp = DEFAULT_CUTOFF) -> dict:
    """Import one daily perp metrics archive (OI + long/short ratio) into
    the R2 store. Cutoff is enforced strictly.
    """
    match = _METRICS_FN.fullmatch(source.name)
    if not match:
        raise ValueError(f"unrecognised perp metrics filename: {source.name}")
    raw = _read_metrics_zip(source)
    raw["create_time"] = pd.to_datetime(raw["create_time"], utc=True)
    raw = raw[raw["create_time"] < cutoff].copy()
    if raw.empty:
        raise ValueError(f"{source}: no rows strictly before the cutoff {cutoff.isoformat()}")
    if (raw["create_time"] >= cutoff).any():
        raise ValueError(f"{source}: archive crosses the cutoff {cutoff.isoformat()}")
    numeric_cols = [c for c in METRICS_COLUMNS if c not in {"create_time", "symbol"}]
    raw[numeric_cols] = raw[numeric_cols].apply(pd.to_numeric, errors="raise")
    raw = raw.drop(columns=["symbol"]).set_index("create_time").sort_index()
    raw.index.name = "ts"
    raw = raw[~raw.index.duplicated(keep="last")]

    symbol = match["symbol"]
    year, month, day = int(match["year"]), int(match["month"]), int(match["day"])
    destination = _metrics_destination(symbol, year, month, day)
    manifest_path = destination.with_suffix(destination.suffix + ".manifest.json")
    if destination.exists() or manifest_path.exists():
        raise FileExistsError(f"refusing to overwrite metrics partition: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    raw.to_parquet(destination)
    parquet_sha = hashlib.sha256(destination.read_bytes()).hexdigest()
    archive_sha = _source_sha256(source.read_bytes())
    manifest = {
        "source": "data.binance.vision",
        "stream": "metrics",
        "key": f"data/futures/um/daily/metrics/{symbol}/{source.name}",
        "size_bytes": destination.stat().st_size,
        "sha256": parquet_sha,
        "archive_sha256": archive_sha,
        "rows": int(len(raw)),
        "start": raw.index[0].isoformat(),
        "end": raw.index[-1].isoformat(),
        "cutoff_exclusive": cutoff.isoformat(),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    return {
        "stream": "metrics", "source": str(source), "symbol": symbol,
        "year": year, "month": month, "day": day, "rows_imported": int(len(raw)),
        "destination": str(destination.relative_to(paths.desk_root())),
    }


def audit_local(symbols: Iterable[str], cutoff: pd.Timestamp = DEFAULT_CUTOFF,
                verify_sha256: bool = False,
                streams: Iterable[str] = ("klines_1h", "premium_index_klines_1h",
                                          "mark_price_klines_1h", "metrics")) -> dict:
    """Audit perp partitions: manifest present + SHA-256 round-trip +
    row count / time bounds agree with Parquet + no row at or after
    the cutoff.
    """
    selected = tuple(dict.fromkeys(symbols))
    if not selected:
        raise ValueError("at least one symbol is required")
    rows = bytes_total = partitions_count = 0
    found_streams: dict[str, list[str]] = {}
    for stream in streams:
        base = paths.path("data", "r2", "market", "futures", "um", stream)
        if not base.is_dir():
            continue
        for symbol in selected:
            sym_dir = base / f"symbol={symbol}"
            if not sym_dir.is_dir():
                continue
            for part in sorted(sym_dir.rglob("part-0.parquet")):
                manifest_path = part.with_suffix(part.suffix + ".manifest.json")
                if not manifest_path.is_file():
                    raise ValueError(f"{part}: missing manifest {manifest_path.name}")
                manifest = json.loads(manifest_path.read_text())
                required = {"source", "key", "size_bytes", "sha256", "rows",
                            "start", "end", "cutoff_exclusive"}
                if not required.issubset(set(manifest)):
                    raise ValueError(f"{manifest_path}: manifest missing required fields")
                df = pd.read_parquet(part)
                if df.index.has_duplicates:
                    raise ValueError(f"{part}: duplicate timestamps in partition")
                if (df.index >= cutoff).any():
                    raise ValueError(
                        f"{part}: partition crosses the cutoff {cutoff.isoformat()}"
                    )
                if len(df) != manifest["rows"]:
                    raise ValueError(f"{part}: row count disagrees with manifest")
                if df.index[0].isoformat() != manifest["start"]:
                    raise ValueError(f"{part}: start bound disagrees with manifest")
                if df.index[-1].isoformat() != manifest["end"]:
                    raise ValueError(f"{part}: end bound disagrees with manifest")
                if part.stat().st_size != manifest["size_bytes"]:
                    raise ValueError(f"{part}: local size disagrees with manifest")
                if verify_sha256:
                    digest = hashlib.sha256()
                    with part.open("rb") as fh:
                        for block in iter(lambda: fh.read(1 << 20), b""):
                            digest.update(block)
                    if digest.hexdigest() != manifest["sha256"]:
                        raise ValueError(f"{part}: SHA-256 disagrees with manifest")
                rows += int(len(df))
                bytes_total += part.stat().st_size
                partitions_count += 1
                found_streams.setdefault(stream, []).append(symbol)
    return {
        "ok": True,
        "cutoff_exclusive": cutoff.isoformat(),
        "partitions": partitions_count,
        "streams": {k: sorted(set(v)) for k, v in found_streams.items()},
        "rows": rows,
        "bytes": bytes_total,
        "sha256_recomputed": verify_sha256,
    }
