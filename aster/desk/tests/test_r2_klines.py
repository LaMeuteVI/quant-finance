from __future__ import annotations

import json
import os
import subprocess
import sys

import pandas as pd
import pyarrow as pa
import aster.data.r2_klines as r2_klines
import pyarrow.fs as pafs
import pyarrow.parquet as pq
import pytest

from aster.data.r2_klines import (
    CANONICAL_COLUMNS,
    CUTOFF,
    PREFIX,
    RAW_COLUMNS,
    RemoteObject,
    _months_before,
    _validate_cutoff,
    audit_local,
    inventory,
    read_holdout,
    read_local,
    reset_holdout_consumption,
    transfer,
)


SEALED_PREFIX = "market/spot/klines_1m"


class FakeFileSystem:
    def __init__(self, entries):
        self.entries = entries
        self.selectors = []

    def get_file_info(self, selector):
        self.selectors.append(selector.base_dir)
        return self.entries.get(selector.base_dir, [])


def test_inventory_lists_only_monthly_prefixes_before_cutoff():
    class Info:
        type = pafs.FileType.File
        size = 17
        path = "cryptos/market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=06/part-0.parquet"

    filesystem = FakeFileSystem({
        "cryptos/market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=06/": [Info()],
    })

    objects = inventory(filesystem, symbols=("BTCUSDT",))

    assert objects == [RemoteObject(
        key="market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=06/part-0.parquet", size=17,
    )]
    assert filesystem.selectors
    assert all("/year=2024/month=07/" not in prefix for prefix in filesystem.selectors)
    assert all(prefix.startswith(f"cryptos/{PREFIX}/symbol=BTCUSDT/") for prefix in filesystem.selectors)


def test_inventory_rejects_symbols_outside_the_approved_universe():
    with pytest.raises(ValueError, match="outside the approved"):
        inventory(FakeFileSystem({}), symbols=("HYPEUSDT",))


def test_fixed_cutoff_rejects_any_other_cutoff():
    with pytest.raises(ValueError, match="fixed exploration cutoff"):
        _months_before(pd.Timestamp("2024-08-01", tz="UTC"))


def test_transfer_refuses_an_existing_partition_before_remote_read(isolated_desk):
    key = "market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=06/part-0.parquet"
    destination = isolated_desk / "data" / "r2" / key
    destination.parent.mkdir(parents=True)
    destination.write_bytes(b"existing")

    with pytest.raises(FileExistsError, match="refusing to overwrite"):
        transfer(object(), [RemoteObject(key, 8)])


def test_transfer_rejects_post_cutoff_key_without_remote_read():
    key = "market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=07/part-0.parquet"

    with pytest.raises(ValueError, match="outside allowed monthly"):
        transfer(object(), [RemoteObject(key, 0)])


def test_validate_cutoff_supports_existing_open_time_utc_schema(tmp_path):
    path = tmp_path / "part.parquet"
    pq.write_table(pa.table({"open_time_utc": pa.array([pd.Timestamp("2024-06-30 23:59:00", tz="UTC")])}), path)

    result = _validate_cutoff(path, CUTOFF)

    assert result == {
        "timestamp_unit": "datetime", "rows": 1,
        "start": "2024-06-30T23:59:00+00:00", "end": "2024-06-30T23:59:00+00:00",
    }


def test_manifest_schema_is_json_serializable():
    # Guard the provenance contract without using network or writing market data.
    payload = {
        "source": "cloudflare-r2", "cutoff_exclusive": CUTOFF.isoformat(),
        "rows": 1, "timestamp_unit": "ms",
    }
    assert json.loads(json.dumps(payload))["cutoff_exclusive"] == "2024-07-01T00:00:00+00:00"


def _local_partition(root, *, symbol="BTCUSDT", month="03", timestamps=None):
    # Default timestamp is 2024-03-31 23:59:00 UTC, before the convention
    # holdout window (HOLDOUT_START=2024-04-01). Tests that want to exercise
    # the holdout path must pass an explicit ``timestamps`` argument that
    # overlaps with [HOLDOUT_START, CUTOFF).
    timestamps = timestamps or [pd.Timestamp("2024-03-31 23:59:00", tz="UTC")]
    path = root / "data" / "r2" / PREFIX / f"symbol={symbol}" / "year=2024" / f"month={month}" / "part.parquet"
    path.parent.mkdir(parents=True)
    values = pd.DatetimeIndex(timestamps)
    table = pa.table({
        "open_time_ms": pa.array((values.asi8 // 1_000_000).astype("int64")),
        "open_time_utc": pa.array(values),
        "close_time_ms": pa.array((values.asi8 // 1_000_000 + 59_999).astype("int64")),
        "open": pa.array([100.0] * len(values)), "high": pa.array([101.0] * len(values)),
        "low": pa.array([99.0] * len(values)), "close": pa.array([100.5] * len(values)),
        "volume": pa.array([3.0] * len(values)), "quote_volume": pa.array([300.0] * len(values)),
        "trades": pa.array([7] * len(values)), "taker_buy_base": pa.array([2.0] * len(values)),
        "taker_buy_quote": pa.array([200.0] * len(values)),
    })
    assert tuple(table.schema.names) == RAW_COLUMNS
    pq.write_table(table, path)
    key = path.relative_to(root / "data" / "r2").as_posix()
    manifest = {
        "source": "cloudflare-r2", "bucket": "cryptos", "key": key,
        "size_bytes": path.stat().st_size, "etag": None,
        "sha256": __import__("hashlib").sha256(path.read_bytes()).hexdigest(),
        "cutoff_exclusive": CUTOFF.isoformat(), "imported_at": "2026-10-13T00:00:00+00:00",
        "timestamp_unit": "datetime", "rows": len(values),
        "start": values.min().isoformat(), "end": values.max().isoformat(),
    }
    path.with_suffix(".parquet.manifest.json").write_text(json.dumps(manifest))
    return path


def test_read_local_returns_utc_index_and_preserves_canonical_columns(isolated_desk):
    _local_partition(isolated_desk)

    frame = read_local("BTCUSDT")

    assert frame.index.name == "open_time_utc"
    assert frame.index.tz is not None
    assert tuple(frame.columns) == CANONICAL_COLUMNS
    assert frame.index.max() < CUTOFF


def test_audit_local_rejects_a_partition_at_the_cutoff(isolated_desk):
    _local_partition(isolated_desk, timestamps=[pd.Timestamp("2024-07-01", tz="UTC")])

    with pytest.raises(ValueError, match="at or after the exploration cutoff"):
        audit_local(("BTCUSDT",))


def test_audit_local_requires_provenance_manifest(isolated_desk):
    path = _local_partition(isolated_desk)
    path.with_suffix(".parquet.manifest.json").unlink()

    with pytest.raises(FileNotFoundError, match="missing provenance manifest"):
        audit_local(("BTCUSDT",))


def test_audit_local_rejects_absent_local_data(isolated_desk):
    with pytest.raises(FileNotFoundError, match="no local R2 store"):
        audit_local(("BTCUSDT",))


def test_audit_local_rejects_schema_divergence(isolated_desk):
    path = _local_partition(isolated_desk)
    pq.write_table(pa.table({"open_time_utc": pa.array([pd.Timestamp("2024-06-30", tz="UTC")])}), path)

    with pytest.raises(ValueError, match="unexpected schema"):
        audit_local(("BTCUSDT",))


# ---------------------------------------------------------------------------
# Convention window: no longer a holdout. True holdout data is post-cutoff.
# ---------------------------------------------------------------------------


def test_cutoff_is_timezone_aware_and_fixed():
    assert CUTOFF.tz is not None
    assert CUTOFF == pd.Timestamp("2024-07-01", tz="UTC")


def test_read_local_allows_contaminated_pre_cutoff_validation_window(isolated_desk):
    _local_partition(isolated_desk, timestamps=[pd.Timestamp("2024-05-15 12:00:00", tz="UTC")])

    frame = read_local("BTCUSDT")

    assert frame.index.max() < CUTOFF


# ---------------------------------------------------------------------------
# True sealed post-cutoff holdout tests.  These use only synthetic Parquet.
# ---------------------------------------------------------------------------


def test_exploration_readers_reject_paths_under_the_sealed_store(isolated_desk):
    sealed_path = isolated_desk / "data" / "sealed" / SEALED_PREFIX / "symbol=BTCUSDT" / "year=2024" / "month=07" / "part.parquet"

    with pytest.raises(ValueError, match="sealed"):
        r2_klines.reject_sealed_path(sealed_path)


def test_local_partition_discovery_rejects_r2_symlink_into_sealed_store(isolated_desk):
    data_root = isolated_desk / "data"
    sealed_root = data_root / "sealed"
    (sealed_root / SEALED_PREFIX).mkdir(parents=True)
    (data_root / "r2").symlink_to(sealed_root, target_is_directory=True)

    with pytest.raises(ValueError, match="sealed"):
        r2_klines._local_partitions(("BTCUSDT",))


def test_sealed_transfer_rejects_a_pre_cutoff_partition_without_remote_read(isolated_desk):
    key = "market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=06/part-0.parquet"

    with pytest.raises(ValueError, match="sealed holdout"):
        r2_klines.transfer_sealed(object(), [RemoteObject(key, 0)])


def test_sealed_transfer_preserves_partial_market_data_when_validation_fails(isolated_desk):
    source_bytes = b"synthetic-invalid-parquet-fixture"
    key = "market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=07/part-0.parquet"

    class SourceFileSystem:
        def open_input_file(self, remote_path):
            assert remote_path == f"cryptos/{key}"
            import io
            return io.BytesIO(source_bytes)

    with pytest.raises(Exception):
        r2_klines.transfer_sealed(SourceFileSystem(), [RemoteObject(key, len(source_bytes))])

    destination = isolated_desk / "data" / "sealed" / key
    partial = destination.with_suffix(destination.suffix + ".partial")
    assert partial.read_bytes() == source_bytes


def test_sealed_manifest_contains_only_metadata_and_validates_synthetic_partition(isolated_desk):
    source = isolated_desk / "source.parquet"
    timestamp = pd.Timestamp("2024-07-01", tz="UTC")
    table = pa.table({
        "open_time_ms": pa.array([timestamp.value // 1_000_000]),
        "open_time_utc": pa.array([timestamp]),
        "close_time_ms": pa.array([timestamp.value // 1_000_000 + 59_999]),
        "open": pa.array([1.0]), "high": pa.array([1.0]), "low": pa.array([1.0]),
        "close": pa.array([1.0]), "volume": pa.array([1.0]), "quote_volume": pa.array([1.0]),
        "trades": pa.array([1]), "taker_buy_base": pa.array([1.0]), "taker_buy_quote": pa.array([1.0]),
    })
    pq.write_table(table, source)
    key = "market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=07/part-0.parquet"

    class SourceFileSystem:
        def open_input_file(self, remote_path):
            assert remote_path == f"cryptos/{key}"
            return source.open("rb")

    results = r2_klines.transfer_sealed(SourceFileSystem(), [RemoteObject(key, source.stat().st_size)])
    destination = isolated_desk / "data" / "sealed" / key
    manifest = json.loads(destination.with_suffix(".parquet.manifest.json").read_text())

    assert results == [{"key": key, "destination": str(destination.relative_to(isolated_desk))}]
    assert set(manifest) == {"source", "key", "size_bytes", "sha256", "rows", "start", "end", "timestamp_unit"}
    assert manifest["key"] == key
    assert all("open" not in field and "close" not in field for field in manifest)
    r2_klines.audit_sealed(("BTCUSDT",))


def test_read_holdout_requires_a_ledger_gate(isolated_desk):
    with pytest.raises(TypeError, match="ledger"):
        read_holdout("BTCUSDT", hypothesis_id="H-20261016-TEST-001")  # type: ignore[call-arg]


def test_read_holdout_reads_only_sealed_data_once_across_processes(isolated_desk):
    from aster.ledger.db import Ledger

    source = isolated_desk / "source.parquet"
    timestamp = pd.Timestamp("2024-07-01", tz="UTC")
    table = pa.table({
        "open_time_ms": pa.array([timestamp.value // 1_000_000]),
        "open_time_utc": pa.array([timestamp]),
        "close_time_ms": pa.array([timestamp.value // 1_000_000 + 59_999]),
        "open": pa.array([1.0]), "high": pa.array([1.0]), "low": pa.array([1.0]),
        "close": pa.array([1.0]), "volume": pa.array([1.0]), "quote_volume": pa.array([1.0]),
        "trades": pa.array([1]), "taker_buy_base": pa.array([1.0]), "taker_buy_quote": pa.array([1.0]),
    })
    pq.write_table(table, source)
    key = "market/spot/klines_1m/symbol=BTCUSDT/year=2024/month=07/part-0.parquet"

    class SourceFileSystem:
        def open_input_file(self, remote_path):
            assert remote_path == f"cryptos/{key}"
            return source.open("rb")

    r2_klines.transfer_sealed(SourceFileSystem(), [RemoteObject(key, source.stat().st_size)])
    ledger = Ledger()
    hypothesis_id = ledger.register(
        "Synthetic sealed test", "A synthetic test verifies durable single-shot gating.",
        "A test-only fixture verifies ledger persistence.",
        "Rejected if the persisted gate permits a second read.",
        {"sharpe_ann_min": 0.8}, "test", "crypto-spot", "test",
    )
    with ledger._conn() as conn:
        conn.execute("UPDATE hypotheses SET status = 'backtest_passed' WHERE id = ?", (hypothesis_id,))

    frame = read_holdout("BTCUSDT", hypothesis_id=hypothesis_id, ledger=ledger)
    assert (frame.index >= CUTOFF).all()
    code = (
        "from aster.data.r2_klines import read_holdout; "
        "from aster.ledger.db import Ledger, LedgerError; "
        "import sys; "
        f"\ntry:\n read_holdout('BTCUSDT', hypothesis_id={hypothesis_id!r}, ledger=Ledger())\n"
        "except LedgerError:\n sys.exit(0)\n"
        "sys.exit(1)"
    )
    env = {**os.environ, "ASTER_DESK": str(isolated_desk)}
    completed = subprocess.run([sys.executable, "-c", code], env=env, capture_output=True, text=True)

    assert completed.returncode == 0
    assert completed.stdout == ""
    assert completed.stderr == ""
