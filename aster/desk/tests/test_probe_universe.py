import csv
import io
from pathlib import Path

import pytest

from aster.scripts.probe_universe import PROBE_SYMBOLS, probe


def _write_dummy_partition(desk_root: Path, symbol: str) -> Path:
    base = desk_root / "data" / "r2" / "market" / "spot" / "klines_1m" / f"symbol={symbol}"
    year, month = 2024, 6
    part_dir = base / f"year={year:04d}" / f"month={month:02d}"
    part_dir.mkdir(parents=True, exist_ok=True)
    part = part_dir / "part-0.parquet"
    part.write_bytes(b"")
    return part


def test_probe_lists_all_brief_symbols(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ASTER_OFFLINE", "1")

    rows = probe(tmp_path, offline=True)

    seen = {(r["symbol"], r["channel"]) for r in rows}
    for sym in PROBE_SYMBOLS:
        assert (sym, "local-r2-spot") in seen
        assert (sym, "data.binance.vision-spot") in seen
        assert (sym, "data.binance.vision-um") in seen


def test_probe_detects_local_partition_when_present(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ASTER_OFFLINE", "1")
    part = _write_dummy_partition(tmp_path, "RENDERUSDT")

    rows = probe(tmp_path, offline=True)
    local_rows = [r for r in rows if r["symbol"] == "RENDERUSDT" and r["channel"] == "local-r2-spot"]

    assert local_rows and local_rows[0]["exists"] == "yes"
    assert local_rows[0]["sample_key"].endswith("part-0.parquet")


def test_probe_emits_no_record_values(tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ASTER_OFFLINE", "1")
    _write_dummy_partition(tmp_path, "RENDERUSDT")

    rows = probe(tmp_path, offline=True)
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=["symbol", "channel", "exists", "sample_key", "error"])
    writer.writeheader()
    writer.writerows(rows)
    captured = capsys.readouterr()
    output = (captured.out or "") + (buf.getvalue() or "")

    assert "1.0" not in output, "probe output must not leak any record field values"
    assert "close" not in output.lower().split("channels")[0]


def test_probe_is_deterministic_for_listed_symbols(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ASTER_OFFLINE", "1")
    first = probe(tmp_path, offline=True)
    second = probe(tmp_path, offline=True)
    assert first == second