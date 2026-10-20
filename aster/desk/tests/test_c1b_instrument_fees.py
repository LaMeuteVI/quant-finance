"""C1b invariant tests: instrument-specific fees in the grid and the engine.

The C1 DoD required per-instrument fees — spot taker 10 bps/side, USDⓈ-M
perp taker 5 bps/side (VIP 0, no discount). The first rebuilt grid kept
``fee_bps_per_side = 10`` on every row, so C2 charged F3 v1.1 (perp legs
only) the spot fee: ~10 bps of phantom cost per round trip.

These tests pin the two schedules in the grid, pin the venue inference
that decides which one a leg pays, and pin the end-to-end arithmetic:
a perp-only round trip costs 2x5 bps + spread + impact; a spot-only one
2x10 bps + spread + impact.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from aster.backtest.cost_model import (
    FEE_BPS_PER_SIDE,
    GridCostModel,
    infer_venue,
)

ROOT = Path(__file__).resolve().parents[1]
GRID = ROOT / "research/atlas/cost-grid.csv"
COSTS_MD = ROOT / "research/atlas/costs.md"

LIQUID_MAJORS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]


@pytest.fixture(scope="module")
def grid() -> pd.DataFrame:
    return pd.read_csv(GRID)


# ---- grid structure ---------------------------------------------------

def test_grid_has_both_venue_schedules(grid: pd.DataFrame) -> None:
    for col in ("fee_bps_per_side_spot", "fee_bps_per_side_perp",
                "round_trip_bps_spot", "round_trip_bps_perp"):
        assert col in grid.columns, f"C1b DoD: grid must carry {col}"
    assert (grid["fee_bps_per_side_spot"] == 10.0).all()
    assert (grid["fee_bps_per_side_perp"] == 5.0).all()


def test_venue_round_trip_decomposition(grid: pd.DataFrame) -> None:
    """round_trip = 2*fee + spread + impact, per venue.

    The spread is paid once per round trip (it is symmetric), which is
    the desk's v1 convention — C1b changes the fee term only.
    """
    for venue, fee in (("spot", 10.0), ("perp", 5.0)):
        expected = 2 * fee + grid["spread_bps"] + grid["impact_bps"]
        np.testing.assert_allclose(
            grid[f"round_trip_bps_{venue}"], expected, rtol=1e-12,
            err_msg=f"{venue} round-trip must be 2*fee + spread + impact",
        )


def test_perp_schedule_is_exactly_ten_bps_cheaper(grid: pd.DataFrame) -> None:
    """Halving the per-side fee removes exactly 2*5 = 10 bps per RT."""
    delta = grid["round_trip_bps_spot"] - grid["round_trip_bps_perp"]
    np.testing.assert_allclose(delta, 10.0, rtol=1e-12)


def test_spot_schedule_matches_the_pre_c1b_flat_column(grid: pd.DataFrame) -> None:
    """The spot schedule must reproduce the v1 flat column exactly, so
    C1b is a pure fee correction and nothing else moved."""
    np.testing.assert_allclose(
        grid["round_trip_bps_spot"], grid["round_trip_bps"], rtol=1e-12)


def test_no_high_low_source_on_liquid_majors(grid: pd.DataFrame) -> None:
    """C1 invariant must survive the C1b regeneration."""
    sub = grid[grid["symbol"].isin(LIQUID_MAJORS)]
    assert not sub.empty
    assert (sub["spread_source"] == "aggtrades_effective").all()


# ---- venue inference --------------------------------------------------

@pytest.mark.parametrize(
    "column,perp_legs,expected",
    [
        ("BTC-USDT:USDT", None, "perp"),
        ("BTC-USDT", None, "spot"),
        ("BTCUSDT", None, "perp"),
        ("BTC/USDT", None, "spot"),
        ("BTC/USDT:USDT", None, "perp"),
        # An explicit ``perp_legs`` list is authoritative and
        # exhaustive: a column it lists is a perp leg, a column it
        # omits is spot.  ``perp_legs=[]`` means "spot-only book".
        ("ETH-USDT", ["ETH-USDT"], "perp"),
        ("SOL-USDT", ["SOL-USDT"], "perp"),
        ("BTC-USDT", [], "spot"),
        ("BTC-USDT:USDT", [], "spot"),
        ("BTC-USDT:USDT", None, "perp"),
    ],
)
def test_infer_venue(column: str, perp_legs, expected: str) -> None:
    assert infer_venue(column, perp_legs) == expected


def test_unknown_column_defaults_to_spot() -> None:
    """Conservative: spot fee is 2x perp, so a miss can only over-charge."""
    assert infer_venue("SOMETHING_ODD") == "spot"


# ---- model arithmetic -------------------------------------------------

def test_perp_only_round_trip_is_ten_bps_below_spot_only(grid: pd.DataFrame) -> None:
    """The C1b DoD test, end to end through the model."""
    model = GridCostModel(grid)
    perp = model.round_trip_bps("BTC-USDT:USDT", 0, 100_000.0)
    spot = model.round_trip_bps("BTC-USDT", 0, 100_000.0)
    assert spot - perp == pytest.approx(10.0, abs=1e-9)

    row = grid[(grid["symbol"] == "BTCUSDT")
               & (grid["utc_hour"] == 0)
               & (grid["notional"] == 100_000.0)].iloc[0]
    # perp: 2*5 + spread + impact; spot: 2*10 + spread + impact
    assert perp == pytest.approx(2 * 5.0 + row.spread_bps + row.impact_bps)
    assert spot == pytest.approx(2 * 10.0 + row.spread_bps + row.impact_bps)


def test_per_trade_cost_bps_panel_uses_perp_schedule(grid: pd.DataFrame) -> None:
    model = GridCostModel(grid)
    idx = pd.date_range("2024-01-01", periods=3, freq="D", tz="UTC")
    cols = ["BTC-USDT", "BTC-USDT:USDT"]
    prices = pd.DataFrame(100.0, index=idx, columns=cols)
    weights = pd.DataFrame(0.5, index=idx, columns=cols)
    panel = model.per_trade_cost_bps(weights, prices, 100_000.0)
    diff = (panel["BTC-USDT"] - panel["BTC-USDT:USDT"]).to_numpy()
    np.testing.assert_allclose(diff, 10.0, rtol=1e-12)


def test_perp_legs_argument_declares_a_bare_named_column_as_perp(grid: pd.DataFrame) -> None:
    """A column the prereg lists in ``perp_legs`` is a perp leg, whatever
    its name.  Without the list the same column falls back to spot, so
    the two panels must differ by the 10 bps fee step."""
    model = GridCostModel(grid)
    idx = pd.date_range("2024-01-01", periods=2, freq="D", tz="UTC")
    prices = pd.DataFrame(100.0, index=idx, columns=["ETH-USDT:USDT"])
    weights = pd.DataFrame(1.0, index=idx, columns=["ETH-USDT:USDT"])
    declared_perp = model.per_trade_cost_bps(weights, prices, 100_000.0,
                                             perp_legs=["ETH-USDT:USDT"])
    assumed_spot = model.per_trade_cost_bps(weights, prices, 100_000.0,
                                             perp_legs=[])
    assert assumed_spot.iloc[0, 0] - declared_perp.iloc[0, 0] == pytest.approx(
        10.0, abs=1e-9)


def test_fee_schedule_constants_match_do_d() -> None:
    assert FEE_BPS_PER_SIDE == {"spot": 10.0, "perp": 5.0}


def test_stress_scales_both_venues(grid: pd.DataFrame) -> None:
    base = GridCostModel(grid)
    stressed = base.scaled(2.0)
    a = base.round_trip_bps("BTC-USDT:USDT", 0, 100_000.0)
    b = stressed.round_trip_bps("BTC-USDT:USDT", 0, 100_000.0)
    assert b == pytest.approx(2 * a)


# ---- hash freeze ------------------------------------------------------

def test_costs_md_records_the_current_grid_sha() -> None:
    digest = hashlib.sha256(GRID.read_bytes()).hexdigest()
    assert digest in COSTS_MD.read_text(), (
        "C1b DoD: re-freeze the grid SHA-256 in research/atlas/costs.md")
