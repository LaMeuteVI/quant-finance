"""Integration tests for the exact signed-flow desk channel."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.data.signed_flow_materialise import (
    _aggregate_partition,
    load_signed_flow_panel,
    panel_report,
)


def _write_partition(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_parquet(path, index=False)


def test_partition_aggregation_uses_all_rows_and_close_labels(tmp_path):
    path = tmp_path / "symbol=BTCUSDT" / "year=2022" / "month=01" / "part-0.parquet"
    base = pd.Timestamp("2022-01-01T00:00:00Z")
    rows = [
        {"price": 100.0, "quantity": 2.0, "transact_time": int(base.timestamp() * 1000), "is_buyer_maker": False},
        {"price": 101.0, "quantity": 1.0, "transact_time": int((base + pd.Timedelta(minutes=1)).timestamp() * 1000), "is_buyer_maker": True},
        {"price": 102.0, "quantity": 3.0, "transact_time": int((base + pd.Timedelta(minutes=15)).timestamp() * 1000), "is_buyer_maker": False},
    ]
    _write_partition(path, rows)
    out = _aggregate_partition(path, "15min")
    # [00:00,00:15) is labelled at 00:15; signed = +2 - 1, total = 3.
    assert out.loc[base + pd.Timedelta(minutes=15), "signed"] == 1.0
    assert out.loc[base + pd.Timedelta(minutes=15), "total"] == 3.0
    # The trade at 00:15 belongs to the next close-labelled bar.
    assert out.loc[base + pd.Timedelta(minutes=30), "signed"] == 3.0


def test_panel_loader_enforces_cutoff_and_namespace(tmp_path):
    root = tmp_path / "aggtrades"
    path = root / "symbol=BTCUSDT" / "year=2022" / "month=01" / "part-0.parquet"
    base = pd.Timestamp("2022-01-01T00:00:00Z")
    rows = [
        {"price": 100.0, "quantity": 2.0, "transact_time": int(base.timestamp() * 1000), "is_buyer_maker": False},
    ]
    _write_partition(path, rows)
    idx = pd.date_range(base + pd.Timedelta(minutes=15), periods=2, freq="15min", tz="UTC")
    panel = load_signed_flow_panel(["BTC/USDT"], idx, timeframe="15min", root=root)
    assert list(panel.columns) == ["BTC/USDT"]
    assert panel.iloc[0, 0] == 1.0
    assert np.isnan(panel.iloc[1, 0])
    rep = panel_report(panel)
    assert rep["cutoff_exclusive"] == "2024-07-01T00:00:00+00:00"
    assert rep["all_values_in_range"] is True


def test_panel_loader_rejects_post_cutoff_partition(tmp_path):
    root = tmp_path / "aggtrades"
    path = root / "symbol=BTCUSDT" / "year=2024" / "month=07" / "part-0.parquet"
    ts = pd.Timestamp("2024-07-01T00:00:00Z")
    _write_partition(path, [{
        "price": 100.0, "quantity": 1.0,
        "transact_time": int(ts.timestamp() * 1000),
        "is_buyer_maker": False,
    }])
    try:
        load_signed_flow_panel(["BTC/USDT"], pd.date_range(ts, periods=1, freq="15min"), root=root)
    except ValueError as exc:
        assert "cutoff" in str(exc).lower()
    else:
        raise AssertionError("post-cutoff partition was accepted")
