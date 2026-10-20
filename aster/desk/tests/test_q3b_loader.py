"""Q3b loader tests — perp data, Hive -> wide panel.

No holdout, no real data download, no live, no key, no order.
Tests use a synthetic Hive layout in a tmp_path and a small
synthetic bar index.
"""
from __future__ import annotations

import json
import math
import shutil
import zipfile
from pathlib import Path

import pandas as pd
import pytest

from aster import paths
from aster.data.funding_materialise import _reindex_to_bar
from aster.data.funding_rate import DEFAULT_CUTOFF
from aster.data.perp_data import (
    KLINE_COLUMNS,
    METRICS_COLUMNS,
    import_kline_archive,
    import_metrics_archive,
)
from aster.data.perp_loader import (
    KLINE_STREAMS,
    load_perp_close,
    load_perp_metrics,
)


def _build_kline_zip(path: Path, *, month: str, with_header: bool = True) -> Path:
    """Build a synthetic 1h kline ZIP covering one month starting
    on the 1st of ``month`` (e.g. "2023-01"). 720 rows.
    """
    year, m = month.split("-")
    start = pd.Timestamp(f"{year}-{m}-01 00:00:00", tz="UTC")
    rows = []
    for i in range(720):
        ts = int((start + pd.Timedelta(hours=i)).timestamp() * 1000)
        rows.append([ts, 100.0, 101.0, 99.5, 100.5, 10.0,
                     ts + 3_599_999, 1005.0, 5, 5.0, 502.5, 0])
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        with zf.open(f"BTCUSDT-1h-{month}.csv", "w") as fh:
            text = ""
            if with_header:
                text += ",".join(KLINE_COLUMNS) + "\n"
            for r in rows:
                text += ",".join(str(x) for x in r) + "\n"
            fh.write(text.encode("utf-8"))
    return path


def _build_metrics_zip(path: Path, *, day: str) -> Path:
    """Build a synthetic daily metrics ZIP for one day."""
    ts = pd.Timestamp(day, tz="UTC")
    rows = [[
        ts.isoformat(), "BTCUSDT", 75000.0, 3.5e9,
        1.1, 1.1, 1.2, 1.2,
    ]]
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        with zf.open(f"BTCUSDT-metrics-{day}.csv", "w") as fh:
            for r in rows:
                text = ",".join(METRICS_COLUMNS) + "\n"
                text += ",".join(str(x) for x in r) + "\n"
                fh.write(text.encode("utf-8"))
    return path


def test_q3b_loader_kline_to_wide(tmp_path):
    """Importer writes Hive, loader reads Hive and returns a wide panel
    aligned to a 1h bar index, with the standard store manifest.
    """
    # Import two months (2023-01, 2023-02) of BTCUSDT klines.
    for month in ("2023-01", "2023-02"):
        zpath = tmp_path / f"BTCUSDT-1h-{month}.zip"
        _build_kline_zip(zpath, month=month, with_header=True)
        import_kline_archive("klines_1h", zpath)
    # Build a 1h bar index that spans 2023-01..2023-02.
    bar_index = pd.date_range("2023-01-01", "2023-02-28 23:00:00", freq="1h", tz="UTC")
    panel = load_perp_close(["BTCUSDT"], bar_index=bar_index)
    assert panel.shape == (len(bar_index), 1)
    assert panel.columns.tolist() == ["BTCUSDT"]
    # Every bar after the first 1h must have a close (ffill is causal).
    assert panel["BTCUSDT"].notna().iloc[1:].all()
    # The standard store path was written.
    dst = paths.path("data", "perpetuals", "binance", "BTCUSDT", "klines_1h.parquet")
    assert dst.exists()
    assert dst.with_suffix(".manifest.json").exists()
    manifest = json.loads(dst.with_suffix(".manifest.json").read_text())
    assert manifest["source"].startswith("derived:pre-cutoff-r2-perp-klines_1h")
    # Cleanup the produced persistent parquet so the test is idempotent.
    dst.unlink(missing_ok=True)
    dst.with_suffix(".manifest.json").unlink(missing_ok=True)
    # Cleanup the Hive partitions too.
    shutil.rmtree(
        paths.path("data", "r2", "market", "futures", "um", "klines_1h", "symbol=BTCUSDT"),
        ignore_errors=True,
    )


def test_q3b_loader_metrics_long_form(tmp_path):
    """Importer writes Hive, loader returns a long-form metrics frame
    with columns = the 8 Binance columns, and writes per-symbol parquet.
    """
    for day in ("2023-01-01", "2023-01-02"):
        zpath = tmp_path / f"BTCUSDT-metrics-{day}.zip"
        _build_metrics_zip(zpath, day=day)
        import_metrics_archive(zpath)
    out = load_perp_metrics(["BTCUSDT"])
    assert not out.empty
    assert "symbol" in out.columns
    assert out["symbol"].iloc[0] == "BTCUSDT"
    dst = paths.path("data", "perpetuals", "binance", "BTCUSDT", "metrics.parquet")
    assert dst.exists()
    # Cleanup.
    dst.unlink(missing_ok=True)
    dst.with_suffix(".manifest.json").unlink(missing_ok=True)
    shutil.rmtree(
        paths.path("data", "r2", "market", "futures", "um", "metrics", "symbol=BTCUSDT"),
        ignore_errors=True,
    )


def test_q3b_loader_rejects_unknown_stream():
    with pytest.raises(ValueError, match="not a kline stream"):
        load_perp_close(["BTCUSDT"], bar_index=pd.DatetimeIndex([]), stream="metrics")


def test_q3b_loader_rejects_missing_store(tmp_path):
    """If the Hive root for a (stream, symbol) is missing, the loader
    raises with a useful message pointing at the download script.
    """
    # Use a symbol that we know we haven't imported.
    bar_index = pd.date_range("2023-01-01", periods=2, freq="1h", tz="UTC")
    with pytest.raises(FileNotFoundError, match="q3b_download_perp"):
        load_perp_close(["XXNOMEMXX"], bar_index=bar_index)
