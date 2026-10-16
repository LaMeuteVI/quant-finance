"""Read-only pre-cutoff R2 data and an isolated post-cutoff sealed holdout.

Exploration readers accept only ``data/r2`` and enforce the strict exclusive
2024-07-01 UTC cutoff. Sealed imports are stored only under ``data/sealed``;
their manifests contain provenance metadata but never market values. Sealed
reads require an explicit ledger gate that is persisted per hypothesis/symbol.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urlparse

import pandas as pd
import pyarrow.fs as pafs
import pyarrow.parquet as pq

from aster import paths

if TYPE_CHECKING:
    from aster.ledger.db import Ledger

BUCKET = "cryptos"
PREFIX = "market/spot/klines_1m"
CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SEALED_STORE = "sealed"
SEALED_PREFIX = f"{SEALED_STORE}/{PREFIX}"
SYMBOLS = (
    "BTCUSDT", "ETHUSDT", "SOLUSDT", "AAVEUSDT", "DOGEUSDT", "SUIUSDT",
    "XRPUSDT", "BNBUSDT", "LINKUSDT", "NEARUSDT", "XMRUSDT", "FETUSDT",
)
RAW_COLUMNS = (
    "open_time_ms", "open_time_utc", "close_time_ms", "open", "high", "low",
    "close", "volume", "quote_volume", "trades", "taker_buy_base", "taker_buy_quote",
)
CANONICAL_COLUMNS = tuple(column for column in RAW_COLUMNS if column != "open_time_utc")
_TIMESTAMP_COLUMNS = ("open_time_utc", "open_time", "open_time_ms", "ts", "timestamp")
_PARTITION_KEY = re.compile(
    rf"^{re.escape(PREFIX)}/symbol=(?P<symbol>[A-Z0-9]+)/year=(?P<year>\d{{4}})/"
    r"month=(?P<month>\d{2})/(?P<filename>[^/]+\.parquet)$"
)


@dataclass(frozen=True)
class RemoteObject:
    key: str
    size: int
    etag: str | None = None


def _months_before(cutoff: pd.Timestamp) -> list[tuple[int, int]]:
    if cutoff.tz is None:
        raise ValueError("cutoff must be timezone-aware")
    cutoff = cutoff.tz_convert("UTC")
    if cutoff != CUTOFF:
        raise ValueError(f"only the fixed exploration cutoff {CUTOFF.isoformat()} is allowed")
    months: list[tuple[int, int]] = []
    year, month = 2017, 1
    while (year, month) < (cutoff.year, cutoff.month):
        months.append((year, month))
        month += 1
        if month == 13:
            year, month = year + 1, 1
    return months


def _prefix(symbol: str, year: int, month: int) -> str:
    return f"{PREFIX}/symbol={symbol}/year={year:04d}/month={month:02d}/"


def _validate_key(key: str, allowed_prefix: str) -> None:
    if not key.startswith(allowed_prefix) or not key.endswith(".parquet"):
        raise ValueError(f"object outside allowed monthly Parquet prefix: {key}")


def _validate_sealed_key(key: str) -> tuple[str, int, int]:
    match = _PARTITION_KEY.fullmatch(key)
    if not match:
        raise ValueError(f"unexpected sealed object layout: {key}")
    symbol = match["symbol"]
    year, month = int(match["year"]), int(match["month"])
    if symbol not in SYMBOLS or not 1 <= month <= 12:
        raise ValueError(f"partition outside approved sealed inventory: {key}")
    if (year, month) < (CUTOFF.year, CUTOFF.month):
        raise ValueError(f"partition precedes the sealed holdout boundary: {key}")
    return symbol, year, month


def _key_parts(key: str) -> tuple[str, int, int]:
    match = _PARTITION_KEY.fullmatch(key)
    if not match:
        raise ValueError(f"unexpected R2 object layout: {key}")
    symbol = match["symbol"]
    year, month = int(match["year"]), int(match["month"])
    if symbol not in SYMBOLS or not 1 <= month <= 12:
        raise ValueError(f"partition outside approved R2 inventory: {key}")
    if (year, month) not in set(_months_before(CUTOFF)):
        raise ValueError(f"partition outside allowed monthly Parquet prefix: {key}")
    return symbol, year, month


def r2_filesystem() -> pafs.S3FileSystem:
    """Construct an R2 client from the environment without exposing credentials."""
    endpoint = os.environ.get("CLOUDFLARE_R2_ENDPOINT")
    access_key = os.environ.get("CLOUDFLARE_R2_ACCESS_KEY_ID")
    secret_key = os.environ.get("CLOUDFLARE_R2_SECRET_ACCESS_KEY")
    if not all((endpoint, access_key, secret_key)):
        raise RuntimeError("R2 endpoint and read credentials must be present in the environment")
    parsed = urlparse(endpoint)
    if not parsed.scheme or not parsed.netloc:
        raise RuntimeError("CLOUDFLARE_R2_ENDPOINT must be an absolute HTTP(S) URL")
    return pafs.S3FileSystem(
        access_key=access_key,
        secret_key=secret_key,
        endpoint_override=parsed.netloc,
        scheme=parsed.scheme,
        region="auto",
        background_writes=False,
    )


def _approved_symbols(symbols: tuple[str, ...]) -> tuple[str, ...]:
    requested = tuple(dict.fromkeys(symbols))
    unknown = sorted(set(requested).difference(SYMBOLS))
    if unknown:
        raise ValueError(f"symbols outside the approved pre-cutoff inventory: {unknown}")
    if not requested:
        raise ValueError("at least one approved symbol is required")
    return requested


def inventory(filesystem: pafs.FileSystem, symbols: tuple[str, ...] = SYMBOLS,
              cutoff: pd.Timestamp = CUTOFF) -> list[RemoteObject]:
    """List only pre-cutoff monthly prefixes; never enumerate a broader root."""
    objects: list[RemoteObject] = []
    for symbol in _approved_symbols(symbols):
        for year, month in _months_before(cutoff):
            prefix = _prefix(symbol, year, month)
            selector = pafs.FileSelector(f"{BUCKET}/{prefix}", recursive=False, allow_not_found=True)
            for info in filesystem.get_file_info(selector):
                if info.type != pafs.FileType.File:
                    continue
                key = info.path.removeprefix(f"{BUCKET}/")
                _validate_key(key, prefix)
                objects.append(RemoteObject(key=key, size=info.size))
    return sorted(objects, key=lambda item: item.key)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _timestamp_series(path: Path) -> pd.Series:
    parquet = pq.ParquetFile(path)
    columns = set(parquet.schema_arrow.names)
    for name in _TIMESTAMP_COLUMNS:
        if name in columns:
            return parquet.read(columns=[name]).to_pandas()[name]
    raise ValueError(f"{path}: no supported timestamp column; schema has {sorted(columns)}")


def _normalise_timestamps(values: pd.Series, path: Path) -> tuple[pd.Series, str]:
    if values.empty:
        raise ValueError(f"{path}: empty Parquet partition")
    if pd.api.types.is_datetime64_any_dtype(values):
        return pd.to_datetime(values, utc=True), "datetime"
    maximum = pd.to_numeric(values, errors="raise").abs().max()
    unit = "us" if maximum >= 100_000_000_000_000 else "ms"
    return pd.to_datetime(pd.to_numeric(values, errors="raise"), unit=unit, utc=True), unit


def _validate_sealed_partition(path: Path) -> dict[str, str | int]:
    timestamps, unit = _normalise_timestamps(_timestamp_series(path), path)
    if (timestamps < CUTOFF).any():
        raise ValueError(f"{path}: sealed holdout contains a pre-cutoff timestamp")
    return {"timestamp_unit": unit, "rows": int(len(timestamps)),
            "start": timestamps.min().isoformat(), "end": timestamps.max().isoformat()}


def _validate_cutoff(path: Path, cutoff: pd.Timestamp) -> dict[str, str | int]:
    timestamps, unit = _normalise_timestamps(_timestamp_series(path), path)
    if (timestamps >= cutoff).any():
        raise ValueError(f"{path}: contains a timestamp at or after the exploration cutoff")
    return {"timestamp_unit": unit, "rows": int(len(timestamps)),
            "start": timestamps.min().isoformat(), "end": timestamps.max().isoformat()}


def _sealed_destination(key: str) -> Path:
    return paths.path("data", SEALED_STORE, key)


def _sealed_root() -> Path:
    return paths.path("data", SEALED_PREFIX)


def reject_sealed_path(path: Path) -> None:
    """Fail closed when an exploration reader is pointed at the sealed store."""
    resolved = path.resolve(strict=False)
    sealed = paths.path("data", SEALED_STORE).resolve(strict=False)
    if resolved == sealed or sealed in resolved.parents:
        raise ValueError("sealed holdout paths are inaccessible to exploration readers")


def _destination(key: str) -> Path:
    return paths.path("data", "r2", key)


def _local_root() -> Path:
    return paths.path("data", "r2", PREFIX)


def _sealed_partitions(symbols: tuple[str, ...]) -> list[tuple[Path, str]]:
    root = _sealed_root()
    if not root.is_dir():
        raise FileNotFoundError(f"no local sealed holdout store at {root}")
    partitions: list[tuple[Path, str]] = []
    for path in sorted(root.rglob("*.parquet")):
        key = path.relative_to(paths.path("data", SEALED_STORE)).as_posix()
        symbol, _, _ = _validate_sealed_key(key)
        if symbol in symbols:
            partitions.append((path, key))
    return partitions


def _local_partitions(symbols: tuple[str, ...]) -> list[tuple[Path, str]]:
    root = _local_root()
    reject_sealed_path(root)
    if not root.is_dir():
        raise FileNotFoundError(f"no local R2 store at {root}")
    partitions: list[tuple[Path, str]] = []
    for path in sorted(root.rglob("*.parquet")):
        key = path.relative_to(paths.path("data", "r2")).as_posix()
        symbol, _, _ = _key_parts(key)
        if symbol in symbols:
            partitions.append((path, key))
    return partitions


def _manifest_path(path: Path) -> Path:
    return path.with_suffix(path.suffix + ".manifest.json")


def _read_sealed_manifest(path: Path, key: str) -> dict:
    manifest_path = _manifest_path(path)
    if not manifest_path.is_file():
        raise FileNotFoundError(f"{path}: missing sealed provenance manifest {manifest_path.name}")
    manifest = json.loads(manifest_path.read_text())
    required = {"source", "key", "size_bytes", "sha256", "rows", "start", "end", "timestamp_unit"}
    if set(manifest) != required:
        raise ValueError(f"{manifest_path}: sealed manifest must contain metadata fields only")
    if manifest["key"] != key:
        raise ValueError(f"{manifest_path}: provenance does not match sealed partition")
    return manifest


def _read_manifest(path: Path, key: str) -> dict:
    manifest_path = _manifest_path(path)
    if not manifest_path.is_file():
        raise FileNotFoundError(f"{path}: missing provenance manifest {manifest_path.name}")
    manifest = json.loads(manifest_path.read_text())
    required = {"source", "bucket", "key", "size_bytes", "sha256", "cutoff_exclusive", "rows", "start", "end", "timestamp_unit"}
    missing = sorted(required.difference(manifest))
    if missing:
        raise ValueError(f"{manifest_path}: missing required fields {missing}")
    if manifest["source"] != "cloudflare-r2" or manifest["bucket"] != BUCKET or manifest["key"] != key:
        raise ValueError(f"{manifest_path}: provenance does not match local partition")
    if manifest["cutoff_exclusive"] != CUTOFF.isoformat():
        raise ValueError(f"{manifest_path}: cutoff is not the fixed exploration cutoff")
    return manifest


def _check_schema(path: Path) -> None:
    actual = tuple(pq.ParquetFile(path).schema_arrow.names)
    if actual != RAW_COLUMNS:
        raise ValueError(f"{path}: unexpected schema {actual}; expected {RAW_COLUMNS}")


def audit_sealed(symbols: tuple[str, ...] = SYMBOLS, verify_sha256: bool = False) -> dict:
    """Validate sealed metadata and boundaries without exposing record values."""
    approved = _approved_symbols(symbols)
    partitions = _sealed_partitions(approved)
    if not partitions:
        raise FileNotFoundError(f"no sealed holdout partitions for {', '.join(approved)}")
    rows = bytes_total = 0
    found_symbols: set[str] = set()
    for partition, key in partitions:
        symbol, _, _ = _validate_sealed_key(key)
        manifest = _read_sealed_manifest(partition, key)
        _check_schema(partition)
        verified = _validate_sealed_partition(partition)
        if {field: manifest[field] for field in verified} != verified:
            raise ValueError(f"{partition}: sealed manifest time bounds or row count disagree with Parquet")
        if partition.stat().st_size != manifest["size_bytes"]:
            raise ValueError(f"{partition}: local size disagrees with sealed provenance manifest")
        if verify_sha256 and _sha256(partition) != manifest["sha256"]:
            raise ValueError(f"{partition}: SHA-256 disagrees with sealed provenance manifest")
        rows += verified["rows"]
        bytes_total += partition.stat().st_size
        found_symbols.add(symbol)
    return {
        "ok": True, "store": SEALED_PREFIX, "cutoff_exclusive": CUTOFF.isoformat(),
        "partitions": len(partitions), "symbols": sorted(found_symbols),
        "rows": rows, "bytes": bytes_total, "sha256_recomputed": verify_sha256,
    }


def audit_local(symbols: tuple[str, ...] = SYMBOLS, verify_sha256: bool = False) -> dict:
    """Audit only local imported R2 partitions, including each partition's time bounds."""
    approved = _approved_symbols(symbols)
    partitions = _local_partitions(approved)
    if not partitions:
        raise FileNotFoundError(f"no local R2 partitions for {', '.join(approved)}")
    rows = 0
    bytes_total = 0
    found_symbols: set[str] = set()
    for path, key in partitions:
        symbol, _, _ = _key_parts(key)
        manifest = _read_manifest(path, key)
        _check_schema(path)
        verified = _validate_cutoff(path, CUTOFF)
        if {field: manifest[field] for field in verified} != verified:
            raise ValueError(f"{path}: manifest time bounds or row count disagree with Parquet")
        if path.stat().st_size != manifest["size_bytes"]:
            raise ValueError(f"{path}: local size disagrees with provenance manifest")
        if verify_sha256 and _sha256(path) != manifest["sha256"]:
            raise ValueError(f"{path}: SHA-256 disagrees with provenance manifest")
        rows += verified["rows"]
        bytes_total += path.stat().st_size
        found_symbols.add(symbol)
    return {
        "ok": True,
        "store": str(_local_root().relative_to(paths.desk_root())),
        "cutoff_exclusive": CUTOFF.isoformat(),
        "partitions": len(partitions),
        "symbols": sorted(found_symbols),
        "rows": rows,
        "bytes": bytes_total,
        "schema": list(RAW_COLUMNS),
        "sha256_recomputed": verify_sha256,
    }


def read_local(symbol: str) -> pd.DataFrame:
    """Read one approved local R2 symbol as a UTC-indexed canonical minute frame.

    The audit is intentionally performed first so a reader cannot consume an
    unproven partition.  The returned index is ``open_time_utc`` and all other
    source columns retain their original names and dtypes.

    Exploration guard: the function refuses to return any row whose index is
    >= ``HOLDOUT_START`` (the reserved convention holdout window).  Only
    :func:`read_holdout` may return those rows, and only once per
    (hypothesis_id, symbol) pair.
    """
    approved = _approved_symbols((symbol,))
    audit_local(approved)
    frames = [pq.ParquetFile(path).read().to_pandas() for path, _ in _local_partitions(approved)]
    frame = pd.concat(frames, ignore_index=True)
    index = pd.to_datetime(frame.pop("open_time_utc"), utc=True)
    frame.index = pd.DatetimeIndex(index, name="open_time_utc")
    frame = frame.loc[:, CANONICAL_COLUMNS].sort_index()
    if frame.index.has_duplicates:
        raise ValueError(f"{symbol}: duplicate open_time_utc values across local partitions")
    if (frame.index >= CUTOFF).any():
        raise ValueError(f"{symbol}: canonical frame crosses the exploration cutoff")
    return frame


def read_holdout(symbol: str, *, hypothesis_id: str, ledger: "Ledger") -> pd.DataFrame:
    """Read one sealed post-cutoff symbol after atomically consuming its ledger gate.

    The caller must provide a ledger. Consumption is persisted before materialising
    rows, so a fresh process cannot repeat a successful read. This API is not an
    exploration reader and must only be reached by the holdout pipeline.
    """
    if not isinstance(hypothesis_id, str) or not hypothesis_id:
        raise ValueError("hypothesis_id must be a non-empty string")
    if not symbol or not isinstance(symbol, str):
        raise ValueError("symbol must be a non-empty string")
    if ledger is None or not hasattr(ledger, "consume_sealed_holdout"):
        raise TypeError("ledger must provide the sealed holdout gate")
    approved = _approved_symbols((symbol,))
    audit_sealed(approved)
    ledger.consume_sealed_holdout(hypothesis_id, symbol)
    frames = [pq.ParquetFile(path).read().to_pandas() for path, _ in _sealed_partitions(approved)]
    frame = pd.concat(frames, ignore_index=True)
    index = pd.to_datetime(frame.pop("open_time_utc"), utc=True)
    frame.index = pd.DatetimeIndex(index, name="open_time_utc")
    frame = frame.loc[:, CANONICAL_COLUMNS].sort_index()
    if frame.index.has_duplicates:
        raise ValueError(f"{symbol}: duplicate open_time_utc values across sealed partitions")
    if (frame.index < CUTOFF).any():
        raise ValueError(f"{symbol}: sealed frame crosses the exploration cutoff")
    return frame


def reset_holdout_consumption() -> None:
    """Deprecated compatibility helper; persisted sealed consumption is immutable."""
    return None


def load_r2_closes(symbols: tuple[str, ...]) -> pd.DataFrame:
    if not symbols:
        raise ValueError("at least one approved symbol is required")

    _approved_symbols(symbols)

    panel = pd.DataFrame(index=pd.DatetimeIndex([], tz="UTC"))  # Initialize with a UTC-aware DatetimeIndex
    for symbol in symbols:
        frame = read_local(symbol)
        series = frame["close"]
        series.name = symbol  # Assign the symbol directly to the series name
        panel = panel.join(series, how="outer")

    if panel.empty and symbols:
        raise FileNotFoundError(f"no local R2 data found for symbols: {symbols}")

    # Ensure the columns (symbols) are in the requested order
    # Reindex columns to explicitly set the order and handle any symbols that might not have data
    panel = panel.reindex(columns=list(symbols))

    return panel


def transfer_sealed(filesystem: pafs.FileSystem, objects: list[RemoteObject]) -> list[dict]:
    """Copy post-cutoff objects into the sealed store with metadata-only manifests.

    The transfer does not emit or retain row values outside the Parquet file.
    It rejects any partition whose declared month precedes the strict cutoff.
    """
    results: list[dict] = []
    for obj in objects:
        _validate_sealed_key(obj.key)
        destination = _sealed_destination(obj.key)
        manifest_path = _manifest_path(destination)
        if destination.exists() or manifest_path.exists():
            raise FileExistsError(f"refusing to overwrite sealed partition: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        partial = destination.with_suffix(destination.suffix + ".partial")
        if partial.exists():
            raise FileExistsError(f"stale sealed partial requires manual inspection: {partial}")
        try:
            with filesystem.open_input_file(f"{BUCKET}/{obj.key}") as source, partial.open("xb") as sink:
                while block := source.read(1 << 20):
                    sink.write(block)
            if partial.stat().st_size != obj.size:
                raise ValueError(f"{obj.key}: downloaded size differs from inventory")
            _check_schema(partial)
            verified = _validate_sealed_partition(partial)
            manifest = {
                "source": "cloudflare-r2", "key": obj.key, "size_bytes": obj.size,
                "sha256": _sha256(partial), **verified,
            }
            partial.replace(destination)
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
            results.append({"key": obj.key, "destination": str(destination.relative_to(paths.desk_root()))})
        except Exception:
            # Preserve every downloaded market-data byte for manual inspection.
            raise
    return results


def transfer(filesystem: pafs.FileSystem, objects: list[RemoteObject],
             cutoff: pd.Timestamp = CUTOFF) -> list[dict]:
    """Copy inventoried objects atomically; reject duplicate local partitions."""
    allowed_months = set(_months_before(cutoff))
    results: list[dict] = []
    for obj in objects:
        symbol, year, month = _key_parts(obj.key)
        if (year, month) not in allowed_months:
            raise ValueError(f"object outside allowed monthly Parquet prefix: {obj.key}")
        _validate_key(obj.key, _prefix(symbol, year, month))
        destination = _destination(obj.key)
        manifest_path = _manifest_path(destination)
        if destination.exists() or manifest_path.exists():
            raise FileExistsError(f"refusing to overwrite existing partition: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        partial = destination.with_suffix(destination.suffix + ".partial")
        if partial.exists():
            raise FileExistsError(f"stale partial requires manual inspection: {partial}")
        remote_path = f"{BUCKET}/{obj.key}"
        try:
            with filesystem.open_input_file(remote_path) as source, partial.open("xb") as sink:
                while block := source.read(1 << 20):
                    sink.write(block)
            if partial.stat().st_size != obj.size:
                raise ValueError(f"{obj.key}: downloaded size differs from inventory")
            _check_schema(partial)
            verified = _validate_cutoff(partial, cutoff)
            sha256 = _sha256(partial)
            partial.replace(destination)
            manifest = {
                "source": "cloudflare-r2", "bucket": BUCKET, "key": obj.key,
                "size_bytes": obj.size, "etag": obj.etag, "sha256": sha256,
                "cutoff_exclusive": cutoff.isoformat(), "imported_at": datetime.now(timezone.utc).isoformat(),
                **verified,
            }
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
            results.append({"key": obj.key, "destination": str(destination.relative_to(paths.desk_root())),
                            "size_bytes": obj.size, **verified})
        except Exception:
            partial.unlink(missing_ok=True)
            raise
    return results


def import_r2(symbols: tuple[str, ...] = SYMBOLS, cutoff: pd.Timestamp = CUTOFF) -> dict:
    filesystem = r2_filesystem()
    objects = inventory(filesystem, symbols, cutoff)
    return {"inventory": {"objects": len(objects), "bytes": sum(item.size for item in objects)},
            "transferred": transfer(filesystem, objects, cutoff)}
