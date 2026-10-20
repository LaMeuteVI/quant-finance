"""Q3b unit tests — perp data importer + audit.

No holdout, no real data download, no live, no key, no order.
Tests use a synthetic ZIP built in memory and a tmp_path
destination.
"""
from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

import pandas as pd
import pytest

from aster import paths
from aster.data.perp_data import (
    DEFAULT_CUTOFF,
    KLINE_COLUMNS,
    METRICS_COLUMNS,
    _kline_destination,
    _metrics_destination,
    audit_local,
    import_kline_archive,
    import_metrics_archive,
)


def _write_kline_zip(path: Path, *, n: int = 24, with_header: bool = False) -> Path:
    """Build a synthetic perp kline ZIP with n hourly rows starting
    2023-01-01 UTC. Timestamps in milliseconds. The real Vision
    archives have no header row (the column convention is the
    Binance standard), so we default to no header.
    """
    start = pd.Timestamp("2023-01-01", tz="UTC")
    rows = []
    for i in range(n):
        ts = int((start + pd.Timedelta(hours=i)).timestamp() * 1000)
        rows.append([ts, 100.0, 101.0, 99.5, 100.5, 10.0,
                     ts + 3_599_999, 1005.0, 5, 5.0, 502.5, 0])
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        with zf.open("BTCUSDT-1h-2023-01.csv", "w") as fh:
            text = ""
            if with_header:
                text += ",".join(KLINE_COLUMNS) + "\n"
            for r in rows:
                text += ",".join(str(x) for x in r) + "\n"
            fh.write(text.encode("utf-8"))
    return path


def _write_metrics_zip(path: Path, *, n: int = 5, with_header: bool = False) -> Path:
    rows = []
    base = pd.Timestamp("2023-01-01", tz="UTC")
    for i in range(n):
        ts = base + pd.Timedelta(hours=i)
        rows.append([
            ts.isoformat(), "BTCUSDT", 75000.0, 3.5e9,
            1.1, 1.1, 1.2, 1.2,
        ])
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        with zf.open("BTCUSDT-metrics-2023-01-01.csv", "w") as fh:
            text = ""
            if with_header:
                text += ",".join(METRICS_COLUMNS) + "\n"
            for r in rows:
                text += ",".join(str(x) for x in r) + "\n"
            fh.write(text.encode("utf-8"))
    return path


def test_q3b_kline_importer_round_trip(tmp_path):
    """Importer reads synthetic ZIP (with and without header),
    writes R2 parquet + manifest, no row crosses the cutoff.
    """
    for header, ym in [(False, "2023-01"), (True, "2023-02")]:
        zpath = tmp_path / f"BTCUSDT-1h-{ym}.zip"
        _write_kline_zip(zpath, n=24, with_header=header)
        out = import_kline_archive("klines_1h", zpath)
        assert out["symbol"] == "BTCUSDT"
        assert out["rows_imported"] == 24
        dst = Path(paths.desk_root()) / out["destination"]
        assert dst.exists()
        assert dst.with_suffix(dst.suffix + ".manifest.json").exists()
        df = pd.read_parquet(dst)
        assert len(df) == 24
        assert (df.index < DEFAULT_CUTOFF).all()
    # Audit (no SHA-256 recompute to keep it fast).
    report = audit_local(["BTCUSDT"], verify_sha256=False)
    assert report["ok"] is True
    assert "BTCUSDT" in report["streams"].get("klines_1h", [])


def test_q3b_kline_importer_refuses_cutoff_breach(tmp_path):
    """A row at or after the cutoff raises. The importer drops
    anything at or after the cutoff; if the file has no pre-cutoff
    rows left, the import is refused with a clear message.
    """
    # Build a 1-row archive at 2025-01-01 (post-cutoff).
    zpath = tmp_path / "BTCUSDT-1h-2025-01.zip"
    start = pd.Timestamp("2025-01-01", tz="UTC")
    rows = [[int(start.timestamp() * 1000), 100.0, 101.0, 99.5, 100.5, 10.0,
             0, 1005.0, 5, 5.0, 502.5, 0]]
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        with zf.open("BTCUSDT-1h-2025-01.csv", "w") as fh:
            text = ""
            for r in rows:
                text += ",".join(str(x) for x in r) + "\n"
            fh.write(text.encode("utf-8"))
    with pytest.raises(ValueError, match="no rows strictly before"):
        import_kline_archive("klines_1h", zpath)


def test_q3b_metrics_wrong_schema_raises(tmp_path):
    """A metrics CSV whose header is not the 8-column Binance schema
    raises with a clear message. (Defends against silent column
    mismatches.)
    """
    zpath = tmp_path / "BTCUSDT-metrics-2023-01-01.zip"
    # Build a 1-row CSV with a wrong header.
    base = pd.Timestamp("2023-01-01", tz="UTC")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        with zf.open("BTCUSDT-metrics-2023-01-01.csv", "w") as fh:
            text = "ts,sym,foo,bar,baz,qux,quux,corge\n"
            text += f"{base.isoformat()},BTCUSDT,1,2,3,4,5,6\n"
            fh.write(text.encode("utf-8"))
    with pytest.raises(ValueError, match="expected columns"):
        import_metrics_archive(zpath)


def test_q3b_metrics_importer_round_trip(tmp_path):
    zpath = tmp_path / "BTCUSDT-metrics-2023-01-01.zip"
    _write_metrics_zip(zpath, n=5, with_header=True)
    out = import_metrics_archive(zpath)
    assert out["symbol"] == "BTCUSDT"
    assert out["rows_imported"] == 5
    dst = Path(paths.desk_root()) / out["destination"]
    assert dst.exists()
    df = pd.read_parquet(dst)
    assert (df.index < DEFAULT_CUTOFF).all()
