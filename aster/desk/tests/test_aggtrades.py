from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

import pandas as pd
import pytest

from aster.data import aggtrades


def _build_aggtrades_zip(path: Path, rows: list[tuple]) -> None:
    """Build a Binance-style headerless 8-column aggTrades CSV ZIP."""
    buf = io.StringIO()
    for r in rows:
        buf.write(",".join(str(x) for x in r) + "\n")
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("trades.csv", buf.getvalue())


def _make_row(
    ts_ms: int, price: str = "100.00", qty: str = "0.10",
    is_buyer_maker: str = "False", agg_trade_id: int | None = None,
) -> tuple:
    if agg_trade_id is None:
        agg_trade_id = ts_ms
    return (agg_trade_id, price, qty, agg_trade_id, agg_trade_id, ts_ms, is_buyer_maker, "True")


def test_import_archive_writes_parquet_with_5_columns(tmp_path: Path, isolated_desk: Path) -> None:
    rows = [_make_row(1700000000000 + 1000 * i) for i in range(5)]
    archive = tmp_path / "BTCUSDT-aggTrades-2024-01.zip"
    _build_aggtrades_zip(archive, rows)

    result = aggtrades.import_archive(archive, isolated_desk / "data" / "r2" / "market" / "spot" / "aggtrades")

    assert result["rows"] == 5
    table = pd.read_parquet(result["path"])
    assert list(table.columns) == ["agg_trade_id", "price", "quantity", "transact_time", "is_buyer_maker"]
    assert int(table["transact_time"].iloc[0]) == 1700000000000


def test_import_archive_metadata_only_manifest(tmp_path: Path, isolated_desk: Path) -> None:
    rows = [_make_row(1700000000000)]
    archive = tmp_path / "BTCUSDT-aggTrades-2024-01.zip"
    _build_aggtrades_zip(archive, rows)

    result = aggtrades.import_archive(archive, isolated_desk / "data" / "r2" / "market" / "spot" / "aggtrades")
    manifest_path = Path(result["path"] + ".manifest.json")
    manifest = json.loads(manifest_path.read_text())

    # Metadata-only keys: source, key, size_bytes, sha256, rows, start, end,
    # timestamp_unit, cutoff_exclusive. No price/quantity/trade_id leaks.
    expected = {
        "source", "key", "size_bytes", "sha256", "rows",
        "start", "end", "timestamp_unit", "cutoff_exclusive",
    }
    assert set(manifest) == expected

    # The trade we ingested had price=100.00; if the manifest ever serialised a
    # price it would show up here. We assert the exact string is absent.
    flat = json.dumps(manifest)
    assert "100.00" not in flat
    assert "100.0" not in flat
    assert "0.10" not in flat
    assert "1700000000000" not in flat


def test_import_archive_rejects_post_cutoff_row(tmp_path: Path, isolated_desk: Path) -> None:
    cutoff = pd.Timestamp("2024-07-01", tz="UTC")
    crossing_ms = int(cutoff.value // 10**6)
    safe_ms = crossing_ms - 60_000
    rows = [_make_row(safe_ms), _make_row(crossing_ms)]
    archive = tmp_path / "BTCUSDT-aggTrades-2024-06.zip"
    _build_aggtrades_zip(archive, rows)

    with pytest.raises(aggtrades.CutoffViolationError, match="at or after the cutoff"):
        aggtrades.import_archive(
            archive,
            isolated_desk / "data" / "r2" / "market" / "spot" / "aggtrades",
        )


def test_import_archive_rejects_when_only_post_cutoff_rows_remain(tmp_path: Path, isolated_desk: Path) -> None:
    cutoff = pd.Timestamp("2024-07-01", tz="UTC")
    crossing_ms = int(cutoff.value // 10**6) + 1000
    rows = [_make_row(crossing_ms + i) for i in range(3)]
    archive = tmp_path / "BTCUSDT-aggTrades-2024-07.zip"
    _build_aggtrades_zip(archive, rows)

    with pytest.raises(aggtrades.CutoffViolationError, match="at or after the cutoff"):
        aggtrades.import_archive(
            archive,
            isolated_desk / "data" / "r2" / "market" / "spot" / "aggtrades",
        )


def test_import_archive_rejects_empty_zip(tmp_path: Path, isolated_desk: Path) -> None:
    archive = tmp_path / "BTCUSDT-aggTrades-2024-01.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("trades.csv", "")

    with pytest.raises(aggtrades.CutoffViolationError, match="no rows strictly before the cutoff"):
        aggtrades.import_archive(
            archive,
            isolated_desk / "data" / "r2" / "market" / "spot" / "aggtrades",
        )


def test_audit_local_round_trips_sha256(tmp_path: Path, isolated_desk: Path) -> None:
    rows = [_make_row(1700000000000 + i * 1000) for i in range(3)]
    archive = tmp_path / "BTCUSDT-aggTrades-2024-01.zip"
    _build_aggtrades_zip(archive, rows)

    aggtrades.import_archive(archive, isolated_desk / "data" / "r2" / "market" / "spot" / "aggtrades")

    summary = aggtrades.audit_local(("BTCUSDT",), verify_sha256=True)
    assert summary["ok"] is True
    assert summary["partitions"] == 1
    assert summary["rows"] == 3
    assert summary["sha256_recomputed"] is True


def test_audit_local_returns_empty_when_store_missing(isolated_desk: Path) -> None:
    summary = aggtrades.audit_local(("BTCUSDT",))
    assert summary["ok"] is False
    assert summary["partitions"] == 0
    assert summary["rows"] == 0