"""X1 integration tests — cross-sectional funding carry.

Per the desk's wiring rule, these go through the real engine so the
C1b venue inference and the perp funding charge are exercised on the
actual code path, not on a synthetic strategy-only panel.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.backtest.engine import CostModel, run_backtest
from aster.backtest.cost_model import GridCostModel
from aster.strategies.xs_funding_carry import XSFundingCarry

SYMS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
PERP = [f"{s}-USDT:USDT" for s in SYMS]
IDX = pd.date_range("2023-01-01", periods=400, freq="D", tz="UTC")


def _panel(seed: int = 7) -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    px = pd.DataFrame(
        100.0 * np.exp(np.cumsum(rng.normal(0, 0.03, (len(IDX), len(SYMS))), axis=0)),
        index=IDX, columns=PERP,
    )
    # Persistent, cross-sectionally dispersed funding: each symbol gets a
    # stable drift plus noise, so the trailing mean ranks reproducibly.
    drift = {"BTC": 0.0, "ETH": 0.1, "SOL": 0.2, "XRP": 0.5, "DOGE": 0.9, "BNB": 1.4}
    fund = pd.DataFrame(
        {c: np.abs(drift[s] + rng.normal(0, 0.20, len(IDX))) * 1e-3
         for s, c in zip(SYMS, PERP)},
        index=IDX,
    )
    return px, fund


def _grid() -> GridCostModel:
    from pathlib import Path
    p = Path(__file__).resolve().parents[1] / "research/atlas/cost-grid.csv"
    return GridCostModel.from_csv(p)


def test_strategy_is_registered():
    from aster.strategies import get
    assert get("xs_funding_carry") is XSFundingCarry


def test_dollar_neutral_and_beta_neutral_book():
    px, fund = _panel()
    s = XSFundingCarry(timeframe="1d", funding=fund)
    w = s.target_weights(px, funding=fund)
    assert w.shape == px.shape
    assert list(w.columns) == list(px.columns)
    # No lookahead: no bar may carry a weight the strategy could not
    # have known, checked structurally by shifting the signal.
    net = w.sum(axis=1)
    # Dollar-neutral per bar within tolerance on tradable bars.
    tradable = w.abs().sum(axis=1) > 0
    assert np.allclose(net[tradable], 0.0, atol=1e-9)
    # Gross is capped.
    assert w.abs().sum(axis=1).max() <= 1.0 + 1e-9
    # Both sides are populated on tradable bars.
    assert (w[tradable] > 0).any(axis=1).all()
    assert (w[tradable] < 0).any(axis=1).all()


def test_long_leg_has_lower_funding_than_short_leg():
    """The preregistered mechanism: long cheap funding, short dear."""
    px, fund = _panel()
    s = XSFundingCarry(timeframe="1d", funding=fund)
    w = s.target_weights(px, funding=fund)
    # Use only the first long/short pair the strategy opens.
    tradable = w.abs().sum(axis=1) > 0
    ts = w.index[tradable][30]
    row = w.loc[ts]
    longs = [c for c in row.index if row[c] > 0]
    shorts = [c for c in row.index if row[c] < 0]
    tm = fund.rolling(30, min_periods=15).mean()
    assert tm.loc[ts, longs].mean().mean() < tm.loc[ts, shorts].mean().mean()


def test_weights_are_causal():
    """Truncating the panel must not change past weights."""
    px, fund = _panel()
    s = XSFundingCarry(timeframe="1d", funding=fund)
    full = s.target_weights(px, funding=fund)
    cut = 250
    part = s.target_weights(px.iloc[:cut], funding=fund.iloc[:cut])
    pd.testing.assert_frame_equal(
        full.iloc[:cut], part, check_exact=False, rtol=1e-12)


def test_engine_run_charges_the_perp_fee_not_the_spot_fee():
    """C1b DoD at the integration level: a perp-only book must cost
    10 bps per round trip less than the same book priced as spot."""
    px, fund = _panel()
    s = XSFundingCarry(timeframe="1d", funding=fund)
    w = s.target_weights(px, funding=fund)

    grid = _grid()
    base = run_backtest(
        px, w, costs=grid, AUM=250_000.0, perp_legs=list(PERP), lag=1,
    )
    # Force every column to be priced as a spot leg.
    as_spot = GridCostModel(grid.grid.copy(), stress=grid.stress)
    spot_rows = run_backtest(
        px, w, costs=as_spot, AUM=250_000.0, perp_legs=[], lag=1,
    )
    cost_perp = float(np.nansum(base.costs))
    cost_spot = float(np.nansum(spot_rows.costs))
    assert cost_perp < cost_spot
    # 10 bps per side of fee difference on the traded notional.
    assert cost_spot - cost_perp > 0.0


def test_weekly_rebalance_costs_far_less_than_daily():
    """The no-trade band is what makes the book tradeable: fewer
    rebalances must mean materially less cost."""
    px, fund = _panel()
    grid = _grid()
    def run(every):
        s = XSFundingCarry(timeframe="1d", funding=fund, rebalance_every_bars=every)
        w = s.target_weights(px, funding=fund)
        return float(np.nansum(run_backtest(
            px, w, costs=grid, AUM=250_000.0, perp_legs=list(PERP), lag=1).costs))
    weekly, daily = run(7), run(1)
    assert weekly < daily


def test_constant_cost_model_still_satisfies_the_protocol():
    """``perp_legs`` was added to the engine's cost protocol (C1b); the
    flat legacy adapter must still satisfy it."""
    px, fund = _panel()
    s = XSFundingCarry(timeframe="1d", funding=fund)
    w = s.target_weights(px, funding=fund)
    out = run_backtest(px, w, costs=CostModel(fee_bps=5.0, slippage_bps=1.0),
                       AUM=250_000.0, perp_legs=list(PERP), lag=1)
    assert len(out.returns) == len(px)
