"""Import Binance Vision kline archives without silently mixing timestamp units.

The importer is intentionally separate from the ccxt OHLCV store: Vision archives
contain microstructure proxy columns and are partitioned by symbol/month so their
provenance remains auditable.  The research cutoff is enforced at import time by
default; loading later data requires an explicit, separately authorised workflow.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from zipfile import ZipFile

import pandas as pd

from aster import paths

BINANCE_COLUMNS = (
    "open_time", "open", "high", "low", "close", "volume", "close_time",
    "quote_volume", "number_of_trades", "taker_buy_base_volume",
    "taker_buy_quote_volume", "ignore",
)
DEFAULT_CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
_FILENAME = re.compile(r"(?P<symbol>[A-Z0-9]+)-(?P<timeframe>\d+[mhdw])-\d{4}-\d{2}(?:\.zip|\.csv)$")


def _timestamp_unit(values: pd.Series) -> str:
    """Return ms or us using magnitude, not an archive-date assumption."""
    maximum = pd.to_numeric(values, errors="raise").abs().max()
    if pd.isna(maximum):
        raise ValueError("archive has no timestamps")
    return "us" if maximum >= 100_000_000_000_000 else "ms"


def _read_csv(source: Path) -> pd.DataFrame:
    if source.suffix == ".zip":
        with ZipFile(source) as archive:
            names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
            if len(names) != 1:
                raise ValueError(f"{source}: expected exactly one CSV member, found {len(names)}")
            with archive.open(names[0]) as fh:
                raw = pd.read_csv(fh, header=None)
    else:
        raw = pd.read_csv(source, header=None)
    if raw.empty:
        raise ValueError(f"{source}: empty archive")
    # Vision switched some archives to a header row. Detect it without assuming a date.
    if str(raw.iloc[0, 0]).lower() in {"open time", "open_time"}:
        raw = raw.iloc[1:].reset_index(drop=True)
    if raw.shape[1] != len(BINANCE_COLUMNS):
        raise ValueError(f"{source}: expected {len(BINANCE_COLUMNS)} columns, found {raw.shape[1]}")
    raw.columns = BINANCE_COLUMNS
    return raw


def _source_sha256(source: Path) -> str:
    digest = hashlib.sha256()
    with source.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _destination(symbol: str, timeframe: str, month: pd.Period) -> Path:
    return paths.path(
        "data", "binance_vision", "spot", f"symbol={symbol}", f"timeframe={timeframe}",
        f"year={month.year}", f"month={month.month:02d}.parquet",
    )


def import_archive(source: Path, cutoff: pd.Timestamp = DEFAULT_CUTOFF) -> dict:
    """Import one monthly kline archive, retaining only rows strictly before cutoff."""
    match = _FILENAME.fullmatch(source.name)
    if not match:
        raise ValueError(f"unrecognised Binance Vision monthly kline filename: {source.name}")
    raw = _read_csv(source)
    unit = _timestamp_unit(raw["open_time"])
    raw["ts"] = pd.to_datetime(pd.to_numeric(raw.pop("open_time"), errors="raise"), unit=unit, utc=True)
    raw = raw[raw["ts"] < cutoff].copy()
    numeric = [column for column in BINANCE_COLUMNS if column not in {"open_time", "ignore", "close_time"}]
    raw[numeric] = raw[numeric].apply(pd.to_numeric, errors="raise")
    raw = raw.drop(columns=["close_time", "ignore"]).set_index("ts").sort_index()
    raw.index.name = "ts"
    raw = raw[~raw.index.duplicated(keep="last")]

    source_sha256 = _source_sha256(source)
    written: list[str] = []
    rows_by_month: dict[str, int] = {}
    months = raw.index.tz_localize(None).to_period("M")
    for month, frame in raw.groupby(months):
        destination = _destination(match["symbol"], match["timeframe"], month)
        destination.parent.mkdir(parents=True, exist_ok=True)
        frame.to_parquet(destination)
        manifest = {
            "source_file": str(source.resolve()),
            "source_sha256": source_sha256,
            "symbol": match["symbol"],
            "timeframe": match["timeframe"],
            "timestamp_unit": unit,
            "cutoff_exclusive": cutoff.isoformat(),
            "rows": int(len(frame)),
            "start": frame.index[0].isoformat(),
            "end": frame.index[-1].isoformat(),
        }
        destination.with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=2))
        written.append(str(destination.relative_to(paths.desk_root())))
        rows_by_month[str(month)] = int(len(frame))
    return {
        "source": str(source), "symbol": match["symbol"], "timeframe": match["timeframe"],
        "timestamp_unit": unit, "rows_imported": int(len(raw)), "rows_by_month": rows_by_month,
        "partitions": written,
    }


def import_root(root: Path, cutoff: pd.Timestamp = DEFAULT_CUTOFF) -> list[dict]:
    """Import all recognised monthly CSV/ZIP files below root in deterministic order."""
    files = sorted(path for path in root.rglob("*") if path.is_file() and _FILENAME.fullmatch(path.name))
    if not files:
        raise ValueError(f"no Binance Vision monthly kline CSV/ZIP files found below {root}")
    return [import_archive(source, cutoff) for source in files]
