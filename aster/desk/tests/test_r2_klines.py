from __future__ import annotations

import json

import pandas as pd
import pyarrow as pa
import pyarrow.fs as pafs
import pyarrow.parquet as pq
import pytest

from aster.data.r2_klines import (
    CANONICAL_COLUMNS,
    CUTOFF,
    HOLDOUT_START,
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
# Convention holdout tests (cf. research/notes/2026-10-15-holdout-audit.md)
# ---------------------------------------------------------------------------


def test_holdout_constants_are_well_defined():
    # The holdout is a strict prefix of the cutoff window.  Both are
    # timezone-aware UTC.  The holdout is a 3-month convention window:
    # 2024-04-01 -> 2024-06-30.
    assert HOLDOUT_START.tz is not None
    assert HOLDOUT_START < CUTOFF
    assert (CUTOFF - HOLDOUT_START) == pd.Timedelta(days=91)
    assert HOLDOUT_START == pd.Timestamp("2024-04-01", tz="UTC")
    assert CUTOFF == pd.Timestamp("2024-07-01", tz="UTC")


def test_read_local_rejects_holdout_window(isolated_desk):
    # Exploration code that tries to read a row inside the convention
    # holdout window must fail.  The new guard is independent of the
    # post-cutoff guard and uses a different error message.
    _local_partition(isolated_desk, timestamps=[pd.Timestamp("2024-05-15 12:00:00", tz="UTC")])

    with pytest.raises(ValueError, match="convention holdout start"):
        read_local("BTCUSDT")


def test_read_local_allows_pre_holdout_data(isolated_desk):
    # The default helper timestamp is 2024-03-31, which is before HOLDOUT_START.
    # Exploration reads must continue to work for any data that lies strictly
    # before HOLDOUT_START.
    _local_partition(isolated_desk)

    frame = read_local("BTCUSDT")

    assert frame.index.max() < HOLDOUT_START


def test_read_holdout_returns_only_holdout_window(isolated_desk):
    # The convention holdout is exactly [HOLDOUT_START, CUTOFF).
    # We populate the partition with one row in the holdout window and
    # one row outside, and assert that only the in-window row comes back.
    reset_holdout_consumption()
    _local_partition(
        isolated_desk,
        timestamps=[
            pd.Timestamp("2024-03-31 23:59:00", tz="UTC"),
            pd.Timestamp("2024-05-15 12:00:00", tz="UTC"),
            pd.Timestamp("2024-06-30 23:59:00", tz="UTC"),
        ],
    )

    frame = read_holdout("BTCUSDT", hypothesis_id="H-20261015-TEST-001")

    assert frame.index.min() >= HOLDOUT_START
    assert frame.index.max() < CUTOFF
    assert len(frame) == 2  # 2024-05-15 and 2024-06-30 only


def test_read_holdout_is_single_shot(isolated_desk):
    # "Un holdout ne se consulte qu'une fois": a second read for the same
    # (hypothesis_id, symbol) pair must raise.  This is the in-process
    # enforcement.  A different hypothesis_id for the same symbol must work.
    reset_holdout_consumption()
    _local_partition(isolated_desk, timestamps=[pd.Timestamp("2024-05-15 12:00:00", tz="UTC")])

    first = read_holdout("BTCUSDT", hypothesis_id="H-20261015-TEST-002")
    assert len(first) == 1

    with pytest.raises(RuntimeError, match="Holdout already consumed"):
        read_holdout("BTCUSDT", hypothesis_id="H-20261015-TEST-002")

    # A different hypothesis_id is allowed: the contamination is on the
    # (hypothesis, symbol) pair, not on the symbol alone.
    second = read_holdout("BTCUSDT", hypothesis_id="H-20261015-TEST-003")
    assert len(second) == 1


def test_read_holdout_requires_hypothesis_id(isolated_desk):
    # No anonymous reads.  Empty or None hypothesis_id is refused.
    _local_partition(isolated_desk, timestamps=[pd.Timestamp("2024-05-15 12:00:00", tz="UTC")])

    with pytest.raises(ValueError, match="hypothesis_id must be a non-empty string"):
        read_holdout("BTCUSDT", hypothesis_id="")

    with pytest.raises(ValueError, match="hypothesis_id must be a non-empty string"):
        read_holdout("BTCUSDT", hypothesis_id=None)  # type: ignore[arg-type]


def test_read_holdout_raises_when_window_empty(isolated_desk):
    # If a partition exists but has no rows in [HOLDOUT_START, CUTOFF),
    # read_holdout must raise.  This protects against silent empty
    # confirmations that would let a hypothesis "pass" on zero trades.
    reset_holdout_consumption()
    _local_partition(isolated_desk, timestamps=[pd.Timestamp("2024-03-31 23:59:00", tz="UTC")])

    with pytest.raises(FileNotFoundError, match="no rows in the holdout window"):
        read_holdout("BTCUSDT", hypothesis_id="H-20261015-TEST-004")


def test_read_holdout_rejects_unapproved_symbol(isolated_desk):
    # Same approval gate as read_local: an unknown symbol cannot read the
    # holdout either.  This prevents the holdout API from being a backdoor
    # to bypass the symbol allowlist.
    reset_holdout_consumption()
    _local_partition(isolated_desk, symbol="BTCUSDT", timestamps=[pd.Timestamp("2024-05-15 12:00:00", tz="UTC")])

    with pytest.raises(ValueError, match="symbols outside the approved pre-cutoff inventory"):
        read_holdout("FAKEUSDT", hypothesis_id="H-20261015-TEST-005")
