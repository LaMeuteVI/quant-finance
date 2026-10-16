"""Import spot aggTrades archives from Binance Vision.

The importer is intentionally separate from the kline and funding-rate importers.
aggTrades are the venue's smallest public record of executed trades (one row
per aggregated match); 30 months of BTCUSDT pre-cutoff fit on a 96 GB volume
(≈ 10–15 GB on disk). The schema is **headerless 8-column CSV** per Binance
documentation: agg_trade_id, price, quantity, first_trade_id, last_trade_id,
transact_time (ms epoch), is_buyer_maker, is_best_price_match.

The Parquet partition keeps only what research needs:

    schema = [
        ("agg_trade_id",      "int64"),
        ("price",             "float64"),
        ("quantity",          "float64"),
        ("transact_time",     "int64"),  # ms epoch
        ("is_buyer_maker",    "bool"),   # True = passive buy / aggressive sell
    ]

`first_trade_id`, `last_trade_id`, and `is_best_price_match` are dropped to keep
the partition compact; they are debugging fields, not research inputs, and the
schema we ship is the smallest one that still answers every afml-ch02 / Q6 / Q7
question. They are *visible* by source (the ZIP and the parser see them), only
*not persisted*.

Manifest is metadata-only, exactly like funding_rate.py: no record values, no
sample timestamps, no sample prices. SHA-256, rows, start/end and cutoff are
the only persisted facts.

Cutoff is strictly enforced (every retained ``transact_time`` must satisfy
``transact_time < cutoff``). A monthly archive that contains only post-cutoff
rows raises ``CutoffViolationError`` rather than silently emitting an empty
partition.
"""

from __future__ import annotations

import hashlib
import io
import json
import os
import zipfile
from dataclasses import dataclass
from datetime import timezone as _tz
from pathlib import Path

import numpy as np
import pandas as pd

DEFAULT_CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")

AGG_TRADE_HEADER = (
    "agg_trade_id",
    "price",
    "quantity",
    "first_trade_id",
    "last_trade_id",
    "transact_time",
    "is_buyer_maker",
    "is_best_price_match",
)

RETAINED_COLUMNS = (
    "agg_trade_id",
    "price",
    "quantity",
    "transact_time",
    "is_buyer_maker",
)

_PARQUET_DTYPES = {
    "agg_trade_id": "int64",
    "price": "float64",
    "quantity": "float64",
    "transact_time": "int64",
    "is_buyer_maker": "bool",
}


class CutoffViolationError(ValueError):
    """Raised when an archive's rows extend past the cutoff or are empty pre-cutoff."""


@dataclass(frozen=True)
class AggTradesPartition:
    """Manifest summary for one (symbol, month) aggTrades Parquet partition."""

    source: str
    key: str
    size_bytes: int
    sha256: str
    rows: int
    start: str  # ISO8601 UTC
    end: str    # ISO8601 UTC, < cutoff
    timestamp_unit: str
    cutoff_exclusive: str


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _manifest_path(parquet: Path) -> Path:
    return parquet.with_suffix(parquet.suffix + ".manifest.json")


def _read_archive_csv(archive: Path) -> pd.DataFrame:
    """Read the single CSV inside the aggTrades ZIP into a DataFrame.

    We materialise the CSV to bytes first and let pyarrow parse it; this is
    faster than streaming line-by-line because the parser stays in C.
    """
    with zipfile.ZipFile(archive) as zf:
        names = zf.namelist()
        if len(names) != 1:
            raise ValueError(
                f"aggTrades archive {archive.name} should contain exactly one CSV; found {len(names)}"
            )
        payload = zf.read(names[0])
    # Schema is fixed and headerless: tell pyarrow to skip the header line.
    # Binance aggTrades CSV columns are documented and stable since 2018.
    return pd.read_csv(
        io.BytesIO(payload),
        header=None,
        names=list(AGG_TRADE_HEADER),
        dtype={
            "agg_trade_id": "int64",
            "price": "float64",
            "quantity": "float64",
            "first_trade_id": "int64",
            "last_trade_id": "int64",
            "transact_time": "int64",
            "is_buyer_maker": "object",  # 'True'/'False' string
            "is_best_price_match": "object",
        },
    )


def _enforce_cutoff(df: pd.DataFrame, cutoff: pd.Timestamp) -> pd.DataFrame:
    if (df["transact_time"] >= cutoff.value // 10**6).any():
        violating = int((df["transact_time"] >= cutoff.value // 10**6).sum())
        raise CutoffViolationError(
            f"aggTrades archive contains {violating} row(s) at or after the cutoff "
            f"{cutoff.isoformat()}; strict pre-cutoff only"
        )
    if len(df) == 0:
        raise CutoffViolationError("aggTrades archive has no rows strictly before the cutoff")
    return df


def import_archive(
    source: Path,
    destination_root: Path,
    *,
    cutoff: pd.Timestamp = DEFAULT_CUTOFF,
    archive_url: str | None = None,
) -> dict:
    """Import one monthly aggTrades archive to Parquet with manifest.

    Parameters
    ----------
    source : ZIP path downloaded from Binance Vision.
    destination_root : base directory; the partition lands at
        ``<root>/symbol=<SYM>/year=YYYY/month=MM/part-0.parquet``.
    cutoff : exclusive upper bound on ``transact_time`` (default 2024-07-01 UTC).
    archive_url : recorded verbatim in the manifest for reproducibility.

    Returns
    -------
    dict with keys ``source``, ``key``, ``path``, ``manifest``, ``rows``.
    """
    if not source.exists():
        raise FileNotFoundError(source)

    # The archive filename encodes symbol and month.
    name = source.stem  # BTCUSDT-aggTrades-2024-06
    parts = name.split("-")
    if len(parts) != 4 or parts[1] != "aggTrades":
        raise ValueError(
            f"archive name {source.name!r} does not match <SYM>-aggTrades-YYYY-MM"
        )
    symbol = parts[0]
    year = int(parts[2])
    month = int(parts[3])

    raw = _read_archive_csv(source)
    raw = _enforce_cutoff(raw, cutoff)

    kept = raw[list(RETAINED_COLUMNS)].copy()
    # Convert the 'True'/'False' string column to bool.
    kept["is_buyer_maker"] = kept["is_buyer_maker"].map({"True": True, "False": False}).astype("bool")

    destination = (
        destination_root
        / f"symbol={symbol}"
        / f"year={year:04d}"
        / f"month={month:02d}"
        / "part-0.parquet"
    )
    destination.parent.mkdir(parents=True, exist_ok=True)

    table = pd.DataFrame(kept)
    table.to_parquet(destination, index=False, engine="pyarrow", compression="snappy")

    start_ms = int(table["transact_time"].min())
    end_ms = int(table["transact_time"].max())
    sha = _sha256(destination)
    size = destination.stat().st_size
    rows = int(len(table))

    manifest = AggTradesPartition(
        source="data.binance.vision" if archive_url is None else archive_url,
        key=f"data/spot/monthly/aggTrades/{symbol}/{name}.zip",
        size_bytes=size,
        sha256=sha,
        rows=rows,
        start=pd.Timestamp(start_ms, unit="ms", tz="UTC").isoformat(),
        end=pd.Timestamp(end_ms, unit="ms", tz="UTC").isoformat(),
        timestamp_unit="ms",
        cutoff_exclusive=cutoff.isoformat(),
    ).__dict__

    manifest_path = _manifest_path(destination)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True))

    return {
        "source": str(source),
        "key": manifest["key"],
        "path": str(destination),
        "manifest": manifest,
        "rows": rows,
    }


def audit_local(symbols: tuple[str, ...], *, verify_sha256: bool = False) -> dict:
    """Walk ``data/r2/market/spot/aggtrades/`` and report partition counts.

    Parameters
    ----------
    symbols : panel-approved symbols to audit.
    verify_sha256 : recompute the Parquet SHA-256 and compare to manifest.

    Returns
    -------
    dict with ``ok``, ``store``, ``cutoff_exclusive``, ``partitions``,
    ``symbols``, ``rows``, ``bytes``, ``sha256_recomputed``.
    """
    desk_root = Path(os.environ.get("ASTER_DESK") or os.environ.get("ASTER_DESK_ROOT") or ".").resolve()
    root = desk_root / "data" / "r2" / "market" / "spot" / "aggtrades"
    if not root.exists():
        return {
            "ok": False,
            "store": str(root),
            "cutoff_exclusive": DEFAULT_CUTOFF.isoformat(),
            "partitions": 0,
            "symbols": [],
            "rows": 0,
            "bytes": 0,
            "sha256_recomputed": bool(verify_sha256),
            "reason": "store not built yet",
        }

    partitions: list[Path] = []
    rows = 0
    bytes_total = 0
    sha_ok = True
    for sym in symbols:
        sym_dir = root / f"symbol={sym}"
        if not sym_dir.exists():
            continue
        for parquet in sorted(sym_dir.glob("year=*/month=*/part-0.parquet")):
            manifest_path = _manifest_path(parquet)
            if not manifest_path.exists():
                sha_ok = False
                continue
            try:
                table = pd.read_parquet(parquet, columns=["agg_trade_id"])
            except Exception:
                sha_ok = False
                continue
            rows += int(len(table))
            bytes_total += parquet.stat().st_size
            partitions.append(parquet)
            if verify_sha256:
                sha = _sha256(parquet)
                manifest = json.loads(manifest_path.read_text())
                if sha != manifest["sha256"]:
                    sha_ok = False

    return {
        "ok": sha_ok and len(partitions) > 0,
        "store": str(root),
        "cutoff_exclusive": DEFAULT_CUTOFF.isoformat(),
        "partitions": len(partitions),
        "symbols": [f"symbol={s}" for s in symbols if (root / f"symbol={s}").exists()],
        "rows": rows,
        "bytes": bytes_total,
        "sha256_recomputed": bool(verify_sha256),
    }


__all__ = [
    "AGG_TRADE_HEADER",
    "RETAINED_COLUMNS",
    "DEFAULT_CUTOFF",
    "CutoffViolationError",
    "AggTradesPartition",
    "import_archive",
    "audit_local",
]