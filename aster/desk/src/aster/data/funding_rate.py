"""Import USD-M funding rate archives from Binance Vision.

The importer is intentionally separate from the spot kline importer:
funding rates are a sparse 8-hour series with three columns
(calc_time, funding_interval_hours, last_funding_rate) instead of the
12-column kline schema. The cutoff is enforced at import time by
default; loading later data requires an explicit, separately
authorised workflow (no post-cutoff partition may live in the
research store).

Local layout:

    data/r2/market/futures/um/funding_rate/
        symbol=<SYM>/year=<YYYY>/month=<MM>/part-0.parquet
        symbol=<SYM>/year=<YYYY>/month=<MM>/part-0.parquet.manifest.json
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

FUNDING_COLUMNS = ("calc_time", "funding_interval_hours", "last_funding_rate")
DEFAULT_CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
_FUNDING_FILENAME = re.compile(
    r"(?P<symbol>[A-Z0-9]+)-fundingRate-(?P<year>\d{4})-(?P<month>\d{2})\.zip$"
)
_DOWNLOAD_FILENAME = re.compile(
    r"(?P<symbol>[A-Z0-9]+)-fundingRate-(?P<year>\d{4})-(?P<month>\d{2})\.csv$"
)


def _source_sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _normalise_calc_time(series: pd.Series) -> tuple[pd.Series, str]:
    if pd.api.types.is_datetime64_any_dtype(series):
        return pd.to_datetime(series, utc=True), "datetime"
    numeric = pd.to_numeric(series, errors="raise")
    maximum = numeric.abs().max()
    unit = "us" if maximum >= 100_000_000_000_000 else "ms"
    return pd.to_datetime(numeric, unit=unit, utc=True), unit


def _read_funding_zip(source: Path) -> pd.DataFrame:
    if source.suffix != ".zip":
        raise ValueError(f"{source}: funding archives must be ZIP")
    with ZipFile(source) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"{source}: expected exactly one CSV member, found {len(names)}")
        with archive.open(names[0]) as fh:
            text = io.TextIOWrapper(fh, encoding="utf-8")
            df = pd.read_csv(text)
    if list(df.columns) != list(FUNDING_COLUMNS):
        raise ValueError(
            f"{source}: expected columns {FUNDING_COLUMNS}, found {list(df.columns)}"
        )
    if df.empty:
        raise ValueError(f"{source}: empty funding archive")
    return df


def _destination(symbol: str, year: int, month: int) -> Path:
    return paths.path(
        "data", "r2", "market", "futures", "um", "funding_rate",
        f"symbol={symbol}", f"year={year:04d}", f"month={month:02d}", "part-0.parquet",
    )


def import_archive(source: Path, cutoff: pd.Timestamp = DEFAULT_CUTOFF) -> dict:
    """Import one monthly funding rate archive. Cutoff is enforced strictly.

    Raises if the archive contains any row at or after the cutoff.
    """
    match = _FUNDING_FILENAME.fullmatch(source.name)
    if not match:
        raise ValueError(f"unrecognised Binance Vision funding rate filename: {source.name}")
    raw = _read_funding_zip(source)
    timestamps, ts_unit = _normalise_calc_time(raw["calc_time"])
    raw["ts"] = timestamps
    raw = raw[raw["ts"] < cutoff].copy()
    if raw.empty:
        raise ValueError(f"{source}: no rows strictly before the cutoff {cutoff.isoformat()}")
    if (raw["ts"] >= cutoff).any():
        raise ValueError(f"{source}: archive crosses the cutoff {cutoff.isoformat()}")
    raw["funding_interval_hours"] = pd.to_numeric(raw["funding_interval_hours"], errors="raise")
    raw["last_funding_rate"] = pd.to_numeric(raw["last_funding_rate"], errors="raise")
    raw = raw.drop(columns=["calc_time"]).set_index("ts").sort_index()
    raw.index.name = "ts"
    raw = raw[~raw.index.duplicated(keep="last")]

    year, month = int(match["year"]), int(match["month"])
    destination = _destination(match["symbol"], year, month)
    manifest_path = destination.with_suffix(destination.suffix + ".manifest.json")
    if destination.exists() or manifest_path.exists():
        raise FileExistsError(f"refusing to overwrite funding partition: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    raw.to_parquet(destination)
    parquet_sha = hashlib.sha256(destination.read_bytes()).hexdigest()
    manifest = {
        "source": "data.binance.vision",
        "key": f"data/futures/um/monthly/fundingRate/{match['symbol']}/{source.name}",
        "size_bytes": destination.stat().st_size,
        "sha256": parquet_sha,
        "rows": int(len(raw)),
        "start": raw.index[0].isoformat(),
        "end": raw.index[-1].isoformat(),
        "timestamp_unit": ts_unit,
        "cutoff_exclusive": cutoff.isoformat(),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    return {
        "source": str(source), "symbol": match["symbol"],
        "year": year, "month": month, "rows_imported": int(len(raw)),
        "destination": str(destination.relative_to(paths.desk_root())),
    }


def audit_local(symbols: Iterable[str], cutoff: pd.Timestamp = DEFAULT_CUTOFF,
                verify_sha256: bool = False) -> dict:
    """Audit funding rate partitions: each manifest must round-trip SHA-256,
    row count and time bounds must agree with the Parquet content, and no
    partition may cross the cutoff.
    """
    selected = tuple(dict.fromkeys(symbols))
    if not selected:
        raise ValueError("at least one symbol is required")
    base = paths.path("data", "r2", "market", "futures", "um", "funding_rate")
    if not base.is_dir():
        raise FileNotFoundError(f"no funding rate store at {base}")
    rows = bytes_total = partitions_count = 0
    found_symbols: set[str] = set()
    for symbol in selected:
        sym_dir = base / f"symbol={symbol}"
        if not sym_dir.is_dir():
            continue
        for part in sorted(sym_dir.rglob("part-0.parquet")):
            manifest_path = part.with_suffix(part.suffix + ".manifest.json")
            if not manifest_path.is_file():
                raise ValueError(f"{part}: missing manifest {manifest_path.name}")
            manifest = json.loads(manifest_path.read_text())
            required = {
                "source", "key", "size_bytes", "sha256", "rows",
                "start", "end", "timestamp_unit", "cutoff_exclusive",
            }
            if set(manifest) != required:
                raise ValueError(
                    f"{manifest_path}: manifest must contain metadata only, found {set(manifest)}"
                )
            df = pd.read_parquet(part)
            if df.index.has_duplicates:
                raise ValueError(f"{part}: duplicate timestamps in funding rate partition")
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
            found_symbols.add(symbol)
    return {
        "ok": True,
        "store": "r2/market/futures/um/funding_rate",
        "cutoff_exclusive": cutoff.isoformat(),
        "partitions": partitions_count,
        "symbols": sorted(found_symbols),
        "rows": rows,
        "bytes": bytes_total,
        "sha256_recomputed": verify_sha256,
    }


def list_downloaded_csvs(zip_dir: Path) -> list[Path]:
    """List monthly CSV files already downloaded under zip_dir (helper for imports)."""
    if not zip_dir.is_dir():
        return []
    return sorted(p for p in zip_dir.rglob("*.csv") if _DOWNLOAD_FILENAME.match(p.name))