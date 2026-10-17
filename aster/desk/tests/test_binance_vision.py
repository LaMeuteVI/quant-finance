from __future__ import annotations

from zipfile import ZipFile

import pandas as pd

from aster.data.binance_vision import import_root


def _row(timestamp: int, close: float = 101.0) -> str:
    return f"{timestamp},100,102,99,{close},3,{timestamp + 59_999},300,7,2,200,0\n"


def _archive(root, name: str, rows: list[str]) -> None:
    csv_name = f"{name.removesuffix('.zip')}.csv"
    with ZipFile(root / name, "w") as archive:
        archive.writestr(csv_name, "".join(rows))


def test_import_detects_ms_and_writes_provenance(tmp_path):
    source = tmp_path / "vision"
    source.mkdir()
    _archive(source, "BTCUSDT-1m-2024-06.zip", [
        _row(1_719_791_880_000),  # 2024-06-30 23:58 UTC
        _row(1_719_791_940_000, 102.0),
    ])

    result = import_root(source)

    assert result[0]["timestamp_unit"] == "ms"
    assert result[0]["rows_imported"] == 2
    output = tmp_path / result[0]["partitions"][0]
    frame = pd.read_parquet(output)
    manifest = pd.read_json(output.with_suffix(".manifest.json"), typ="series")
    assert frame.index.tz is not None
    assert frame.index.max() < pd.Timestamp("2024-07-01", tz="UTC")
    assert manifest["timestamp_unit"] == "ms"
    assert manifest["source_sha256"]


def test_import_detects_microseconds_and_excludes_cutoff_and_later_rows(tmp_path):
    source = tmp_path / "vision"
    source.mkdir()
    _archive(source, "ETHUSDT-1m-2024-07.zip", [
        _row(1_719_791_980_000_000),  # 2024-06-30 23:59:40 UTC
        _row(1_719_792_000_000_000, 102.0),  # exact cutoff: excluded
    ])

    result = import_root(source)

    assert result[0]["timestamp_unit"] == "us"
    assert result[0]["rows_imported"] == 1
    output = tmp_path / result[0]["partitions"][0]
    frame = pd.read_parquet(output)
    assert list(frame["close"]) == [101.0]
    assert frame.index[0] == pd.Timestamp("2024-06-30 23:59:40", tz="UTC")
