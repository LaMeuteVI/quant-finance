"""Test du parser / dispatch de `desk data audit-r2` sans aucune I/O réseau ni Parquet réel."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from aster.cli import build_parser
from aster.data.r2_klines import CUTOFF, PREFIX, RAW_COLUMNS, SYMBOLS

DESK = Path(__file__).resolve().parents[1]


def _seed_fake_partition(root: Path, *,
                         symbol: str = "BTCUSDT",
                         month: str = "06",
                         n_rows: int = 10,
                         sha256_ok: bool = True) -> Path:
    """Écrire un partition fake pré-cutoff (manifest + parquet conforme) dans un desk isolé."""
    path = root / "data" / "r2" / PREFIX / f"symbol={symbol}" / "year=2024" / f"month={month}" / "part.parquet"
    path.parent.mkdir(parents=True, exist_ok=True)
    ts = pd.date_range("2024-06-01 00:00:00", periods=n_rows, freq="1min", tz="UTC")
    table = pa.table({
        "open_time_ms": pa.array((ts.asi8 // 1_000_000).astype("int64")),
        "open_time_utc": pa.array(ts),
        "close_time_ms": pa.array((ts.asi8 // 1_000_000 + 59_999).astype("int64")),
        "open": pa.array([100.0] * n_rows), "high": pa.array([101.0] * n_rows),
        "low": pa.array([99.0] * n_rows), "close": pa.array([100.5] * n_rows),
        "volume": pa.array([3.0] * n_rows), "quote_volume": pa.array([300.0] * n_rows),
        "trades": pa.array([7] * n_rows), "taker_buy_base": pa.array([2.0] * n_rows),
        "taker_buy_quote": pa.array([200.0] * n_rows),
    })
    assert tuple(table.schema.names) == RAW_COLUMNS
    pq.write_table(table, path)
    if sha256_ok:
        sha = __import__("hashlib").sha256(path.read_bytes()).hexdigest()
    else:
        sha = "0" * 64
    key = path.relative_to(root / "data" / "r2").as_posix()
    manifest = {
        "source": "cloudflare-r2", "bucket": "cryptos", "key": key,
        "size_bytes": path.stat().st_size, "etag": None,
        "sha256": sha, "cutoff_exclusive": CUTOFF.isoformat(),
        "imported_at": "2026-10-13T00:00:00+00:00",
        "timestamp_unit": "datetime", "rows": n_rows,
        "start": ts.min().isoformat(), "end": ts.max().isoformat(),
    }
    path.with_suffix(".parquet.manifest.json").write_text(json.dumps(manifest) + "\n")
    return path


def test_cli_parse_audit_r2_invokes_cmd_data_check_r2(monkeypatch):
    """Parser : `data audit-r2 --symbols BTC,ETH --sha256` dispatche vers cmd_data_check_r2."""
    called = []

    fake_audit = lambda symbols, verify_sha256: (called.append((symbols, verify_sha256)), None)[1]
    monkeypatch.setattr("aster.data.r2_klines.audit_local", fake_audit)
    monkeypatch.setattr("aster.data.r2_klines.SYMBOLS", ("BTCUSDT", "ETHUSDT"))

    out = build_parser().parse_args(["data", "audit-r2", "--symbols", "BTC,ETH", "--sha256"])
    out.fn(out)

    assert called == [(("BTC", "ETH"), True)]


def test_cli_parse_audit_r2_defaults_and_alias(monkeypatch):
    """Par défaut : tous les SYMBOLS, verify_sha256=False ; `check-r2` conserve l'alias."""
    called = []
    fake_audit = lambda symbols, verify_sha256: called.append((symbols, verify_sha256))
    monkeypatch.setattr("aster.data.r2_klines.audit_local", fake_audit)
    monkeypatch.setattr("aster.data.r2_klines.SYMBOLS", SYMBOLS)

    a1 = build_parser().parse_args(["data", "audit-r2"])
    a1.fn(a1)
    assert called[-1] == (SYMBOLS, False)

    called.clear()
    a2 = build_parser().parse_args(["data", "check-r2"])  # alias conservé
    a2.fn(a2)
    assert called[-1] == (SYMBOLS, False)


def test_parser_alias_present():
    """`check-r2` apparaît bien comme alias de `audit-r2` (usage existant préservé)."""
    parser = build_parser()
    # on teste le comportement observable plutôt qu'un attribut interne
    a1 = parser.parse_args(["data", "audit-r2"])
    a2 = parser.parse_args(["data", "check-r2"])
    assert a1.fn is a2.fn and a1.fn.__name__ == "cmd_data_check_r2"


def test_cli_audit_r2_no_local_store(monkeypatch, isolated_desk):
    """Pas de données locales -> FileNotFoundError, aucun appel réseau."""
    monkeypatch.setenv("ASTER_DESK", str(isolated_desk))
    imported_r2 = {}

    def fake_read(*args, **kwargs):
        imported_r2["hit"] = True
        raise RuntimeError("network call in test")

    monkeypatch.setattr("aster.data.r2_klines.pq.ParquetFile", fake_read)

    with pytest.raises(FileNotFoundError, match="no local R2 store"):
        build_parser().parse_args(["data", "audit-r2"]).fn(
            build_parser().parse_args(["data", "audit-r2"]))

    assert not imported_r2.get("hit")


def test_cli_audit_r2_valid_partition_produces_report(isolated_desk, monkeypatch):
    """Desk avec un partition fake valide -> rapport JSON complet, sans réseau."""
    _seed_fake_partition(isolated_desk, n_rows=10)
    captured = []
    monkeypatch.setattr("aster.cli._print", captured.append)

    # les symboles doivent être approuvés (le parser ne fait que splitter, cf.
    # cmd_data_import_r2 : pas de normalisation) ; le test utilise donc un
    # partition réel dans le desk isolé.
    args = build_parser().parse_args(["data", "audit-r2", "--symbols", "BTCUSDT", "--sha256"])
    args.fn(args)

    report = captured[0]
    assert report["ok"] is True
    assert report["cutoff_exclusive"] == CUTOFF.isoformat()
    assert report["partitions"] == 1
    assert report["symbols"] == ["BTCUSDT"]
    assert report["rows"] == 10
    assert report["sha256_recomputed"] is True
    assert "bytes" in report and "schema" in report
    assert set(report["schema"]) == set(RAW_COLUMNS)
