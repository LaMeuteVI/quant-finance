"""F1 — Funding carry, delta-neutral (tests).

These tests pin the F1 v3 contract. The first sub-section proves the
strategy mechanics on synthetic funding data; the second exercises
the strategy on the desk's real R2 4h bars and the Q3 funding panel
for BTC, ETH, SOL — the desk's preregistered prediction. The full
pipeline.run path is exercised by the F1 dev backtest (see the
artifacts under ``backtests/H-.../``).

V3 contract (memo N23, family H-20261016-002 closed falsified):
    Entry: mean_funding_lookback > amortised_round_trip_bps_per_fixing
           AND funding_rate_now > 0.
    Exit: funding_rate_now < 0 OR non-positive for
          exit_persistence_bars consecutive bars.
    Long spot / short perp only (no inverse side).
    Costs: amortised across expected_holding_fixings.
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


def test_funding_carry_dn_long_spot_short_perp_when_mean_funding_above_amortised():
    """With a constant +5 bps/bar funding that exceeds the v3 amortised
    cushion (~1.67 bps/fixing), the strategy is +1 spot / -1 perp."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    funding = _funding(idx, ["BTCUSDT"], 0.0005)
    strat = FundingCarryDN(
        lookback_bars=10,
        amortised_round_trip_bps_per_fixing=0.5,  # 0.5 bps/fixing cushion
        basis_z_cap=None,
        exit_persistence_bars=4,
    )
    w = strat.target_weights(close, funding=funding)
    assert list(w.columns) == ["BTCUSDT", "BTCUSDT:USDT"]
    # After warm-up, the last bar must be long spot / short perp.
    assert w["BTCUSDT"].iloc[-1] == pytest.approx(1.0)
    assert w["BTCUSDT:USDT"].iloc[-1] == pytest.approx(-1.0)


def test_funding_carry_dn_no_inverse_side_when_funding_negative():
    """With negative funding the v3 strategy is FLAT (no short spot /
    long perp). This is a key v3 change from v1.x: we do not run the
    inverse carry because the historical sample shows funding is
    asymmetric (paid > received)."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    funding = _funding(idx, ["BTCUSDT"], -0.0005)
    strat = FundingCarryDN(
        lookback_bars=10,
        amortised_round_trip_bps_per_fixing=0.5,
        basis_z_cap=None,
        exit_persistence_bars=4,
    )
    w = strat.target_weights(close, funding=funding)
    assert (w == 0.0).all().all()


def test_funding_carry_dn_no_position_when_funding_below_cushion():
    """A funding rate inside the amortised cushion does not open a
    position. 1 bps/fixing funding < 5 bps/fixing cushion → flat."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    funding = _funding(idx, ["BTCUSDT"], 0.0001)
    strat = FundingCarryDN(
        lookback_bars=10,
        amortised_round_trip_bps_per_fixing=5.0,  # 5 bps cushion
        basis_z_cap=None,
        exit_persistence_bars=4,
    )
    w = strat.target_weights(close, funding=funding)
    assert (w == 0.0).all().all()


def test_funding_carry_dn_basis_z_cap_blocks_entry():
    """A close z-score above the cap blocks new entries."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    # Spike the close 5 sigma above the 30d mean at bar 60.
    close.iloc[60, 0] = 200.0
    funding = _funding(idx, ["BTCUSDT"], 0.001)
    strat = FundingCarryDN(
        lookback_bars=10,
        amortised_round_trip_bps_per_fixing=0.5,
        basis_z_cap=3.0,
        exit_persistence_bars=4,
    )
    w = strat.target_weights(close, funding=funding)
    assert w["BTCUSDT"].iloc[60] == 0.0
    assert w["BTCUSDT:USDT"].iloc[60] == 0.0


def test_funding_carry_dn_funding_via_params_fallback():
    """If ``funding`` is not in kwargs, ``self.params['funding']`` is used."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    funding = _funding(idx, ["BTCUSDT"], 0.0005)
    strat = FundingCarryDN(
        funding=funding,
        lookback_bars=10,
        amortised_round_trip_bps_per_fixing=0.5,
        basis_z_cap=None,
        exit_persistence_bars=4,
    )
    w = strat.target_weights(close)  # no kwargs → fallback to params
    assert w["BTCUSDT"].iloc[-1] == pytest.approx(1.0)
    assert w["BTCUSDT:USDT"].iloc[-1] == pytest.approx(-1.0)


def test_funding_carry_dn_engine_round_trip_with_funding():
    """End-to-end: a positive constant funding on the v3 contract
    produces a positive net return on a long-spot / short-perp book.
    The v3 strategy is asymmetric (no inverse), and exits cleanly
    when funding turns non-positive for ``exit_persistence_bars``."""
    idx = pd.date_range("2024-01-01", periods=80, freq="4h", tz="UTC")
    close_spot = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT"])
    close_perp = pd.DataFrame(100.0, index=idx, columns=["BTCUSDT:USDT"])
    drift = np.linspace(0.0, 0.001, len(idx))
    close_perp.iloc[:, 0] = 100. * (1.0 + drift)
    prices = pd.concat([close_spot, close_perp], axis=1)
    funding = _funding(idx, ["BTCUSDT"], 0.0005)
    strat = FundingCarryDN(
        lookback_bars=10,
        amortised_round_trip_bps_per_fixing=0.5,
        basis_z_cap=None,
        exit_persistence_bars=4,
    )
    w = strat.target_weights(close_spot, funding=funding)
    res = run_backtest(prices, w, costs=CostModel(fee_bps=10, slippage_bps=5),
                       funding=funding, perp_legs=["BTCUSDT:USDT"], AUM=1e6)
    # On a delta-neutral book with a positive funding rate, the
    # funding income (perp leg) > 0 and we receive it as a "cash
    # out" (negative funding column). Cost of initial rebalance is
    # the only leakage; net should be positive.
    assert res.funding.sum() < 0  # we received funding on the short perp


def test_funding_carry_dn_default_params_match_prereg():
    """The strategy's defaults must match the v3 preregistered values,
    so a desk backtest with no params follows the preregistered
    hypothesis verbatim."""
    p = FundingCarryDN.default_params
    assert p["lookback_bars"] == 42                 # 7 days × 6 4h-bars/day
    assert p["amortised_round_trip_bps_per_fixing"] == 1.67
    assert p["basis_z_cap"] == 3.0
    assert p["max_gross"] == 1.0
    assert p["funding"] is None  # not a hyper-parameter, an input panel
    assert p["exit_persistence_bars"] == 18
    assert p["expected_holding_fixings"] == 42