from __future__ import annotations

import hashlib
import io
import json
import zipfile
from pathlib import Path

import pandas as pd
import pytest

from aster.data import funding_rate


def _ms(ts: pd.Timestamp) -> int:
    return int(ts.value // 1_000_000)


def _build_funding_zip(path: Path, calc_times: list[int]) -> None:
    buf = io.StringIO()
    buf.write("calc_time,funding_interval_hours,last_funding_rate\n")
    for t in calc_times:
        buf.write(f"{t},8,0.00010000\n")
    payload = buf.getvalue().encode("utf-8")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(path.with_suffix(".csv").name, payload)


def test_import_archive_rejects_when_only_post_cutoff_rows_remain(tmp_path: Path) -> None:
    cutoff = pd.Timestamp("2024-07-01", tz="UTC")
    archive = tmp_path / "BTCUSDT-fundingRate-2024-06.zip"
    # Only post-cutoff timestamps remain after filtering; the importer must
    # refuse rather than emit an empty partition.
    crossing_ms = _ms(cutoff)
    later_ms = _ms(cutoff) + 8 * 3600 * 1000
    _build_funding_zip(archive, [crossing_ms, later_ms])

    with pytest.raises(ValueError, match="no rows strictly before"):
        funding_rate.import_archive(archive, cutoff=cutoff)


def test_import_archive_writes_metadata_only_manifest(tmp_path: Path, isolated_desk: Path) -> None:
    archive = tmp_path / "BTCUSDT-fundingRate-2020-01.zip"
    times = [1577836800000, 1577865600000, 1577894400000]
    _build_funding_zip(archive, times)

    info = funding_rate.import_archive(archive)
    destination = isolated_desk / info["destination"]
    manifest_path = destination.with_suffix(".parquet.manifest.json")

    assert destination.exists()
    assert manifest_path.exists()
    manifest = json.loads(manifest_path.read_text())
    assert set(manifest) == {
        "source", "key", "size_bytes", "sha256", "rows",
        "start", "end", "timestamp_unit", "cutoff_exclusive",
    }
    assert manifest["source"] == "data.binance.vision"
    assert manifest["sha256"] == hashlib.sha256(destination.read_bytes()).hexdigest()
    assert manifest["size_bytes"] == destination.stat().st_size
    assert manifest["rows"] == 3
    assert manifest["timestamp_unit"] == "ms"

    parquet = pd.read_parquet(destination)
    assert list(parquet.columns) == ["funding_interval_hours", "last_funding_rate"]
    assert len(parquet) == 3
    assert (parquet.index < pd.Timestamp("2024-07-01", tz="UTC")).all()


def test_audit_local_round_trips_sha256(tmp_path: Path, isolated_desk: Path) -> None:
    archive = tmp_path / "ETHUSDT-fundingRate-2021-03.zip"
    times = [1614556800000, 1614585600000]
    _build_funding_zip(archive, times)
    funding_rate.import_archive(archive)

    report = funding_rate.audit_local(("ETHUSDT",), verify_sha256=True)
    assert report["ok"] is True
    assert report["symbols"] == ["ETHUSDT"]
    assert report["partitions"] == 1
    assert report["rows"] == 2
    assert report["sha256_recomputed"] is True


def test_audit_local_rejects_partition_crossing_cutoff(tmp_path: Path, isolated_desk: Path, monkeypatch) -> None:
    archive = tmp_path / "BTCUSDT-fundingRate-2020-02.zip"
    times = [1580515200000]  # 2020-02-01
    _build_funding_zip(archive, times)
    info = funding_rate.import_archive(archive)

    # Tamper: append a post-cutoff timestamp to the parquet and rewrite the
    # manifest to match row count and time bounds so only the content check
    # can catch it.
    destination = isolated_desk / info["destination"]
    df = pd.read_parquet(destination)
    extra = pd.DataFrame(
        {"funding_interval_hours": [8], "last_funding_rate": [0.0001]},
        index=pd.DatetimeIndex([pd.Timestamp("2024-07-15 00:00", tz="UTC")], name="ts"),
    )
    tampered = pd.concat([df, extra])
    tampered.to_parquet(destination)
    manifest_path = destination.with_suffix(".parquet.manifest.json")
    manifest = json.loads(manifest_path.read_text())
    manifest["rows"] = int(len(tampered))
    manifest["end"] = tampered.index[-1].isoformat()
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    with pytest.raises(ValueError, match="crosses the cutoff"):
        funding_rate.audit_local(("BTCUSDT",))