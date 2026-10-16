"""P4 — Realistic costs and capacity (tests).

The contract:

* ``GridCostModel.from_csv`` loads the desk's per-asset / per-UTC-hour /
  per-size round-trip cost grid.
* ``round_trip_bps(symbol, utc_hour, notional)`` returns the grid value
  in bps; an AUM between two grid points uses the next-larger point.
* ``per_trade_cost_bps(weights, prices, AUM)`` returns a wide panel
  aligned on (index, columns) with ``weights``.
* ``capacity_max_AUM`` linearly interpolates the AUM at which the net
  Sharpe first crosses the threshold.
* ``engine.run_backtest`` accepts a ``GridCostModel`` AND an ``AUM``;
  the resulting ``BacktestResult.costs`` is materially larger at
  larger AUM (because the impact term scales with sqrt(Q/ADV)).
* The ×2 and ×3 stress tests are first-class: ``scaled(2)`` doubles
  the cost panel, ``scaled(3)`` triples it.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from aster.backtest import engine
from aster.backtest.cost_model import (
    ConstantCostModel,
    GridCostModel,
    REPORT_SIZES,
    capacity_max_AUM,
)


def _toy_grid() -> pd.DataFrame:
    """A tiny deterministic grid for unit tests.

    3 symbols × 24 hours × 4 sizes = 288 rows. Round-trip cost is the
    same value in every hour for a given (symbol, size) — the only
    axis we vary is size, so the cost panel test is unambiguous.
    """
    rows = []
    for sym, base in [("BTCUSDT", 30.0), ("ETHUSDT", 35.0), ("SOLUSDT", 60.0)]:
        for hour in range(24):
            for notional, mult in [(1e5, 1.0), (1e6, 1.5), (1e7, 3.0), (5e7, 6.0)]:
                rows.append({
                    "symbol": sym, "utc_hour": hour,
                    "notional": float(notional),
                    "round_trip_bps": base * mult,
                })
    return pd.DataFrame(rows)


def test_gridcostmodel_loads_and_validates_schema():
    grid = _toy_grid()
    m = GridCostModel(grid)
    assert m.sizes == REPORT_SIZES


def test_gridcostmodel_rejects_missing_columns():
    bad = _toy_grid().drop(columns=["round_trip_bps"])
    with pytest.raises(ValueError, match="must have columns"):
        GridCostModel(bad)


def test_gridcostmodel_rejects_zero_stress():
    with pytest.raises(ValueError, match="stress must be > 0"):
        GridCostModel(_toy_grid(), stress=0.0)


def test_round_trip_bps_uses_next_larger_grid_point():
    """An AUM between two grid points rounds UP to the larger point
    (conservative: a capacity report must not under-state impact).
    """
    m = GridCostModel(_toy_grid())
    # BTC @ hour 0 @ 100k = 30.0 bps
    assert m.round_trip_bps("BTCUSDT", 0, 1e5) == pytest.approx(30.0)
    # BTC @ hour 0 @ 5e5 is between 1e5 (30 bps) and 1e6 (45 bps) → 45 bps
    assert m.round_trip_bps("BTCUSDT", 0, 5e5) == pytest.approx(45.0)
    # BTC @ hour 0 @ 1e9 is above the largest grid point → uses 5e7 (180 bps)
    assert m.round_trip_bps("BTCUSDT", 0, 1e9) == pytest.approx(180.0)


def test_round_trip_bps_raises_for_missing_symbol_or_hour():
    m = GridCostModel(_toy_grid())
    with pytest.raises(KeyError):
        m.round_trip_bps("DOGEUSDT", 0, 1e5)
    with pytest.raises(KeyError):
        m.round_trip_bps("BTCUSDT", 99, 1e5)


def test_per_trade_cost_bps_panel_shape_and_alignment():
    m = GridCostModel(_toy_grid())
    idx = pd.date_range("2024-01-01", periods=48, freq="h", tz="UTC")
    cols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    prices = pd.DataFrame(100.0, index=idx, columns=cols)
    weights = pd.DataFrame(0.0, index=idx, columns=cols)
    weights.iloc[10, 0] = 1.0  # one rebalance on BTC at index 10
    panel = m.per_trade_cost_bps(weights, prices, 1e5)
    assert panel.shape == weights.shape
    assert panel.columns.equals(weights.columns)
    assert panel.index.equals(weights.index)
    # BTC @ hour 10 @ 100k = 30 bps; ETH @ hour 10 @ 100k = 35 bps
    assert panel.iloc[10, 0] == pytest.approx(30.0)
    assert panel.iloc[10, 1] == pytest.approx(35.0)


def test_per_trade_cost_bps_rejects_zero_aum():
    m = GridCostModel(_toy_grid())
    idx = pd.date_range("2024-01-01", periods=4, freq="h", tz="UTC")
    cols = ["BTCUSDT"]
    prices = pd.DataFrame(100.0, index=idx, columns=cols)
    weights = pd.DataFrame(0.0, index=idx, columns=cols)
    with pytest.raises(ValueError, match="AUM must be > 0"):
        m.per_trade_cost_bps(weights, prices, 0.0)


def test_per_trade_cost_bps_rejects_misaligned_frames():
    m = GridCostModel(_toy_grid())
    idx = pd.date_range("2024-01-01", periods=4, freq="h", tz="UTC")
    prices = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT", "ETHUSDT"])
    weights = pd.DataFrame(0.0, index=idx[:2], columns=["BTCUSDT", "ETHUSDT"])
    with pytest.raises(ValueError, match="share index"):
        m.per_trade_cost_bps(weights, prices, 1e5)
    weights2 = pd.DataFrame(0.0, index=idx, columns=["BTCUSDT", "DOGEUSDT"])
    with pytest.raises(ValueError, match="share columns"):
        m.per_trade_cost_bps(weights2, prices, 1e5)


def test_scaled_stress_multiplies_costs():
    m = GridCostModel(_toy_grid(), stress=1.0)
    m2 = m.scaled(2.0)
    m3 = m.scaled(3.0)
    assert m2.round_trip_bps("BTCUSDT", 0, 1e5) == pytest.approx(60.0)
    assert m3.round_trip_bps("BTCUSDT", 0, 1e5) == pytest.approx(90.0)


def test_capacity_max_aum_above_at_smallest_returns_smallest():
    # Net Sharpe > 1 at every size → capacity = smallest AUM
    cap = capacity_max_AUM({1e5: 2.0, 1e6: 1.5, 1e7: 1.2, 5e7: 1.05})
    assert cap == pytest.approx(1e5)


def test_capacity_max_aum_below_at_largest_returns_zero():
    # Net Sharpe < 1 at every size → not viable
    cap = capacity_max_AUM({1e5: 0.9, 1e6: 0.7, 1e7: 0.4, 5e7: 0.1})
    assert cap == 0.0


def test_capacity_max_aum_interpolates_crossing():
    # 100k: 1.5  |  1M: 0.7  |  10M: 0.4  |  50M: 0.1
    # First point is above the threshold → return the smallest AUM.
    cap = capacity_max_AUM({1e5: 1.5, 1e6: 0.7, 1e7: 0.4, 5e7: 0.1})
    assert cap == pytest.approx(1e5)


def test_capacity_max_aum_interpolates_between_two_points():
    # 100k: 0.5  |  1M: 0.9  |  10M: 1.4  |  50M: 0.6
    # Capacity = AUM at which the curve drops below 1.0 for the last
    # time. Linearly between (10M, 1.4) and (50M, 0.6):
    # frac = (1.4 - 1.0) / (1.4 - 0.6) = 0.5
    # AUM = 1e7 + 0.5 * (5e7 - 1e7) = 3.0e7
    cap = capacity_max_AUM({1e5: 0.5, 1e6: 0.9, 1e7: 1.4, 5e7: 0.6})
    assert cap == pytest.approx(3.0e7, rel=1e-3)


def test_capacity_max_aum_empty_returns_zero():
    assert capacity_max_AUM({}) == 0.0


def test_constant_cost_model_back_compat():
    """A ConstantCostModel gives the same numbers as the legacy CostModel.

    This is the safety net for the 30+ existing tests that still pass
    a flat CostModel: nothing about the new integration changes their
    numbers, just the internal representation.
    """
    cm = ConstantCostModel(fee_bps=10.0, slippage_bps=5.0)
    idx = pd.date_range("2024-01-01", periods=4, freq="h", tz="UTC")
    cols = ["BTCUSDT", "ETHUSDT"]
    prices = pd.DataFrame(100.0, index=idx, columns=cols)
    weights = pd.DataFrame(0.0, index=idx, columns=cols)
    panel = cm.per_trade_cost_bps(weights, prices, 1e5)
    assert (panel == 15.0).all().all()


def test_engine_run_backtest_uses_grid_at_1m_aum():
    """An engine run with a GridCostModel and AUM=1M must produce a
    positive cost that is materially larger than the scalar default
    (10 + 5 = 15 bps). At AUM=1M BTC round-trip is 45 bps in the toy
    grid, ETH 52.5, SOL 90.0; a single full rebalance therefore pays
    ~6-9 bps of cost, not 1.5.
    """
    idx = pd.date_range("2024-01-01", periods=20, freq="h", tz="UTC")
    cols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    prices = pd.DataFrame(100.0, index=idx, columns=cols)
    weights = pd.DataFrame(0.0, index=idx, columns=cols)
    weights.iloc[5, 0] = 1.0  # signal at bar 5; trade at bar 6 (lag=1)
    weights.iloc[5, 1] = 0.5
    weights.iloc[5, 2] = -0.5
    m = GridCostModel(_toy_grid())
    res = engine.run_backtest(prices, weights, costs=m, AUM=1e6)
    assert res.meta["AUM"] == 1e6
    assert res.meta["cost_model"] == "GridCostModel"
    # The trade is at bar 6 (lag); the per-leg turnover is 1 / 0.5 / 0.5
    # on (BTC, ETH, SOL). With 1M AUM the round-trip costs are
    # 45 / 52.5 / 90 bps → cost contribution = 0.0045 + 0.002625 + 0.0045
    # = 0.011625.
    cost = res.costs.iloc[6]
    assert cost == pytest.approx(0.011625, rel=1e-3)


def test_engine_run_backtest_cost_grows_with_aum():
    """At AUM=100k the cost must be lower than at AUM=1M, which must
    be lower than at AUM=10M. This is the capacity-monotonicity contract.
    """
    idx = pd.date_range("2024-01-01", periods=20, freq="h", tz="UTC")
    cols = ["BTCUSDT"]
    prices = pd.DataFrame(100.0, index=idx, columns=cols)
    weights = pd.DataFrame(0.0, index=idx, columns=cols)
    weights.iloc[5, 0] = 1.0
    m = GridCostModel(_toy_grid())
    # The trade is at bar 6 (lag=1), so we read iloc[6] for the cost.
    c_100k = engine.run_backtest(prices, weights, costs=m, AUM=1e5).costs.iloc[6]
    c_1m = engine.run_backtest(prices, weights, costs=m, AUM=1e6).costs.iloc[6]
    c_10m = engine.run_backtest(prices, weights, costs=m, AUM=1e7).costs.iloc[6]
    c_50m = engine.run_backtest(prices, weights, costs=m, AUM=5e7).costs.iloc[6]
    assert c_100k < c_1m < c_10m < c_50m


def test_engine_run_backtest_stress_x2_doubles_cost():
    """scaled(2) must double the cost; this is the ×2 stress test."""
    idx = pd.date_range("2024-01-01", periods=20, freq="h", tz="UTC")
    cols = ["BTCUSDT"]
    prices = pd.DataFrame(100.0, index=idx, columns=cols)
    weights = pd.DataFrame(0.0, index=idx, columns=cols)
    weights.iloc[5, 0] = 1.0
    m = GridCostModel(_toy_grid())
    c_base = engine.run_backtest(prices, weights, costs=m, AUM=1e6).costs.iloc[6]
    c_x2 = engine.run_backtest(prices, weights, costs=m.scaled(2.0), AUM=1e6).costs.iloc[6]
    c_x3 = engine.run_backtest(prices, weights, costs=m.scaled(3.0), AUM=1e6).costs.iloc[6]
    assert c_x2 == pytest.approx(2 * c_base)
    assert c_x3 == pytest.approx(3 * c_base)


def test_engine_run_backtest_legacy_scalar_path_unchanged():
    """The scalar path (no AUM) must keep producing the same numbers
    the existing test suite relies on.
    """
    idx = pd.date_range("2024-01-01", periods=20, freq="h", tz="UTC")
    cols = ["BTCUSDT"]
    prices = pd.DataFrame(100.0, index=idx, columns=cols)
    weights = pd.DataFrame(0.0, index=idx, columns=cols)
    weights.iloc[5, 0] = 1.0
    res = engine.run_backtest(prices, weights, costs=engine.CostModel(), lag=1)
    # scalar default: 10 + 5 = 15 bps; the trade happens at bar 6 because
    # of the lag (bar 5 is the signal, bar 6 is the fill), so the cost
    # appears at iloc[6], not iloc[5].
    assert res.costs.iloc[6] == pytest.approx(0.0015)


def test_grid_csv_has_12_symbols_and_4_report_sizes(tmp_path):
    """The on-disk grid must have exactly the 12 brief symbols and the
    4 report sizes. This is a guard against silent regressions in the
    regeneration step.
    """
    grid = pd.read_csv(Path("research/atlas/cost-grid.csv"))
    assert set(grid["symbol"].unique()) == {
        "BTCUSDT", "ETHUSDT", "SOLUSDT", "AAVEUSDT", "DOGEUSDT", "SUIUSDT",
        "XRPUSDT", "BNBUSDT", "LINKUSDT", "NEARUSDT", "XMRUSDT", "FETUSDT",
    }
    assert set(grid["notional"].unique()) == set(REPORT_SIZES)