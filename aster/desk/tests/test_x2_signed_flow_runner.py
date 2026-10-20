"""Tests for the X2 runner — the arithmetic that decides each axis.

These are unit tests on the decision helpers, not on the 100 M-row
aggTrades load: the runner's job is to turn a bar panel into a verdict,
and that logic is what has to be right.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research.x2_signed_flow import (
    BARS_PER_DAY,
    HOLD_BARS,
    _round_trip,
    _slug,
    gross_quintile_spread,
    spearman,
    verdict,
)
from aster.backtest.cost_model import GridCostModel


GATES = {
    "min_obs": 500,
    "sharpe_ann_min": 0.8,
    "max_drawdown_floor": -0.35,
    "dsr_min": 0.95,
    "stress_sharpe_ann_min": 0.3,
}


def test_slug_convention():
    assert _slug("BTCUSDT") == "BTC-USDT"
    assert _slug("ETHUSDT") == "ETH-USDT"


def test_bars_per_day_are_right():
    assert BARS_PER_DAY["15min"] == 96
    assert BARS_PER_DAY["1h"] == 24


def test_round_trip_is_the_spot_schedule_and_venue_aware():
    """X2 trades spot aggTrades, so it must be charged the spot leg of
    the C1b grid, and the perp leg must be exactly 10 bps cheaper."""
    grid = GridCostModel.from_csv("research/atlas/cost-grid.csv")
    spot = _round_trip(grid, "BTCUSDT", 250_000.0)
    g = grid.grid
    sub = g[g["symbol"].astype(str).str.replace("-", "").str.upper() == "BTCUSDT"]
    n = sub[np.isclose(sub["notional"], 250_000.0)]
    if n.empty:
        n = sub[sub["notional"] == sub["notional"].min()]
    perp = float(n["round_trip_bps_perp"].mean())
    assert spot == pytest.approx(float(n["round_trip_bps_spot"].mean()))
    assert spot - perp == pytest.approx(10.0, abs=0.01)
    # The C1b cost at this size is the number the prereg quoted as
    # decisive: a 15m quintile spread below ~23 bps cannot clear it.
    assert spot > 20.0


def test_quintile_spread_recovers_a_planted_signal():
    """A planted monotone relationship must be recovered with the right
    sign and roughly the right size, so the descriptive number X2
    carries over from Q22 is not silently broken."""
    n = 4000
    idx = pd.date_range("2022-01-01", periods=n, freq="15min", tz="UTC")
    rng = np.random.default_rng(17)
    flow = rng.normal(0, 0.4, n)
    # The slope must be large enough to be visible against the noise:
    # at 6e-4 the planted correlation is ~0.51 and the Q4-Q0 spread is
    # ~6.5 bps. A slope small enough to look realistic (6e-7) produces a
    # correlation of -0.01 and the test would assert nothing.
    ret = 0.0006 * flow + rng.normal(0, 0.0004, n)
    assert np.corrcoef(flow, ret)[0, 1] > 0.4
    bar = pd.DataFrame(
        {"signed_flow_imbalance": flow, "ret_1bar": ret}, index=idx)
    out = gross_quintile_spread(bar)
    assert out["q4_minus_q0_bps"] is not None
    assert out["q4_minus_q0_bps"] > 0.0
    assert 3.0 < out["q4_minus_q0_bps"] < 12.0


def test_quintile_spread_is_zero_on_noise():
    n = 3000
    idx = pd.date_range("2022-01-01", periods=n, freq="15min", tz="UTC")
    rng = np.random.default_rng(23)
    flow = rng.normal(0, 0.4, n)
    noise = rng.normal(0, 0.001, n)
    bar = pd.DataFrame(
        {"signed_flow_imbalance": flow, "ret_1bar": noise}, index=idx)
    out = gross_quintile_spread(bar)
    assert abs(out["q4_minus_q0_bps"]) < 2.0


def test_spearman_needs_enough_data():
    idx = pd.date_range("2022-01-01", periods=10, freq="15min", tz="UTC")
    assert spearman(pd.Series(range(10), index=idx, dtype=float),
                    pd.Series(range(10), index=idx, dtype=float)) is None


def test_verdict_fails_on_each_gate_independently():
    base = {
        "status": "ok", "n_bars": 5000, "sharpe_ann": 1.2,
        "max_drawdown": -0.10, "net_pnl_ann": 0.05,
    }
    assert verdict(base, GATES)["passes"]

    for key, bad in (
        ("n_bars", 100), ("sharpe_ann", 0.5),
        ("max_drawdown", -0.50), ("net_pnl_ann", -0.01),
    ):
        axis = dict(base)
        axis[key] = bad
        v = verdict(axis, GATES)
        assert not v["passes"], key
        expected = {"n_bars": "min_obs", "sharpe_ann": "sharpe_ann",
                    "max_drawdown": "max_drawdown",
                    "net_pnl_ann": "net_positive"}[key]
        assert expected in v["failed"]


def test_verdict_treats_a_non_ok_axis_as_a_failure_not_a_crash():
    for status in ("no_data", "no_bars", "too_short"):
        v = verdict({"status": status}, GATES)
        assert not v["passes"]
        assert v["reason"] == status


def test_breakeven_arithmetic_holds_for_the_preregistered_hold():
    """The prereg's decisive number: a bar-level spread must clear the
    round trip divided by the holding period."""
    grid = GridCostModel.from_csv("research/atlas/cost-grid.csv")
    rt = _round_trip(grid, "BTCUSDT", 250_000.0)
    be = rt / HOLD_BARS
    # Q22 measured BTC 15m Q4-Q0 at 7.16 bps gross; the prereg says that
    # is below break-even. Keep the assertion anchored to the artefact.
    assert be > 7.16
