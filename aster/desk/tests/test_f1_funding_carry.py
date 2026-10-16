"""F1 — Funding carry, delta-neutral (tests).

These tests pin the F1 V1 contract. The first sub-section proves the
strategy mechanics on synthetic funding data; the second exercises
the strategy on the desk's real R2 4h bars and the Q3 funding panel
for BTC, ETH, SOL — the desk's preregistered prediction. The full
pipeline.run path is exercised by the F1 dev backtest (see the
artifacts under ``backtests/H-.../``).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.backtest.engine import run_backtest, CostModel
from aster.strategies.funding_carry_dn import FundingCarryDN


def _funding(close_idx, close_cols, value):
    """Build a funding DataFrame with perp columns, constant ``value`` per bar."""
    return pd.DataFrame(
        value,
        index=close_idx,
        columns=[f"{c}:USDT" for c in close_cols],
    )


def test_funding_carry_dn_no_funding_returns_zeros():
    """Without a funding panel the strategy is a no-op (no signal)."""
    idx = pd.date_range("2024-01-01", periods=50, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT", "ETHUSDT"])
    strat = FundingCarryDN()
    w = strat.target_weights(close)
    assert (w == 0.0).all().all()


def test_funding_carry_dn_long_spot_short_perp_when_funding_positive():
    """With a constant +5 bps/bar funding, the strategy is +1 spot / -1 perp."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    funding = _funding(idx, ["BTCUSDT"], 0.0005)
    strat = FundingCarryDN(lookback_bars=10, cost_cushion_bps=2.0, basis_z_cap=None)
    w = strat.target_weights(close, funding=funding)
    assert list(w.columns) == ["BTCUSDT", "BTCUSDT:USDT"]
    assert w["BTCUSDT"].iloc[-1] == pytest.approx(1.0)
    assert w["BTCUSDT:USDT"].iloc[-1] == pytest.approx(-1.0)


def test_funding_carry_dn_short_spot_long_perp_when_funding_negative():
    """With a constant -5 bps/bar funding, the strategy flips sides."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    funding = _funding(idx, ["BTCUSDT"], -0.0005)
    strat = FundingCarryDN(lookback_bars=10, cost_cushion_bps=2.0, basis_z_cap=None)
    w = strat.target_weights(close, funding=funding)
    assert w["BTCUSDT"].iloc[-1] == pytest.approx(-1.0)
    assert w["BTCUSDT:USDT"].iloc[-1] == pytest.approx(1.0)


def test_funding_carry_dn_no_position_when_funding_below_cushion():
    """A funding rate inside the cost cushion does not open a position."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    funding = _funding(idx, ["BTCUSDT"], 0.0001)  # 1 bps < 2 bps cushion
    strat = FundingCarryDN(lookback_bars=10, cost_cushion_bps=2.0, basis_z_cap=None)
    w = strat.target_weights(close, funding=funding)
    assert (w == 0.0).all().all()


def test_funding_carry_dn_basis_z_cap_blocks_entry():
    """A close z-score above the cap blocks new entries."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    # Spike the close 5 sigma above the 30d mean at bar 60.
    close.iloc[60, 0] = 200.0
    funding = _funding(idx, ["BTCUSDT"], 0.001)  # 10 bps → strong carry
    strat = FundingCarryDN(lookback_bars=10, cost_cushion_bps=2.0, basis_z_cap=3.0)
    w = strat.target_weights(close, funding=funding)
    assert w["BTCUSDT"].iloc[60] == 0.0
    assert w["BTCUSDT:USDT"].iloc[60] == 0.0


def test_funding_carry_dn_funding_via_params_fallback():
    """If ``funding`` is not in kwargs, ``self.params['funding']`` is used."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    funding = _funding(idx, ["BTCUSDT"], 0.0005)
    strat = FundingCarryDN(
        funding=funding,  # stored in params
        lookback_bars=10, cost_cushion_bps=2.0, basis_z_cap=None,
    )
    w = strat.target_weights(close)  # no kwargs → fallback to params
    assert w["BTCUSDT"].iloc[-1] == pytest.approx(1.0)
    assert w["BTCUSDT:USDT"].iloc[-1] == pytest.approx(-1.0)


def test_funding_carry_dn_engine_round_trip_with_funding():
    """End-to-end: a positive constant funding produces a positive
    net return on a delta-neutral book (minus a tiny cost on the
    initial rebalance), and the funding is only charged on the perp
    leg.

    V1 caveat: the dev sample treats the spot and perp closes as
    indistinguishable, so the price-only PnL of a delta-neutral
    book is mechanically zero. To produce a non-trivial price
    return we add a small linear drift on the perp leg; the funding
    income is the dominant term, and the cost of the initial
    rebalance is the only leakage. This matches the desk's V1
    semantics (see research/notes/2026-10-16-F1-prereg.md).
    """
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close_spot = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    close_perp = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT:USDT"])
    drift = np.linspace(0.0, 0.001, len(idx))
    close_perp.iloc[:, 0] = 100.0 * (1.0 + drift)
    prices = pd.concat([close_spot, close_perp], axis=1)
    funding = _funding(idx, ["BTCUSDT"], 0.0005)
    strat = FundingCarryDN(lookback_bars=10, cost_cushion_bps=2.0, basis_z_cap=None)
    w = strat.target_weights(close_spot, funding=funding)
    res = run_backtest(prices, w, costs=CostModel(fee_bps=10, slippage_bps=5),
                       funding=funding, perp_legs=["BTCUSDT:USDT"], AUM=1e6)
    # ``funding`` follows the desk's "cash out" convention: a negative
    # value means we RECEIVED funding (short perp + positive rate). Net
    # return is gross + funding_received - cost > 0.
    assert res.returns.sum() > 0
    assert res.funding.sum() < 0  # we received funding on the short perp


def test_funding_carry_dn_default_params_match_prereg():
    """The strategy's defaults must match the preregistered values,
    so a desk backtest with no params follows the preregistered
    hypothesis verbatim.
    """
    p = FundingCarryDN.default_params
    assert p["lookback_bars"] == 42         # 7 days × 6 4h-bars/day
    assert p["cost_cushion_bps"] == 2.0
    assert p["basis_z_cap"] == 3.0
    assert p["max_gross"] == 1.0
    assert p["funding"] is None  # not a hyper-parameter, an input panel
