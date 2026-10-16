import numpy as np
import pandas as pd
import pytest

from aster.backtest.engine import CostModel, run_backtest
from aster.backtest.metrics import max_drawdown, summary


def test_buy_and_hold_matches_asset_returns(prices):
    px = prices[["BTC/USDT"]]
    w = pd.DataFrame(1.0, index=px.index, columns=px.columns)
    res = run_backtest(px, w, CostModel(0, 0), lag=1)
    expected = px["BTC/USDT"].pct_change().iloc[2:]
    np.testing.assert_allclose(res.returns.iloc[2:], expected, rtol=1e-12)


def test_lag_zero_is_refused(prices):
    with pytest.raises(ValueError):
        run_backtest(prices, prices * 0, lag=0)


def test_costs_charged_on_turnover(prices):
    px = prices[["BTC/USDT"]]
    w = pd.DataFrame(1.0, index=px.index, columns=px.columns)
    free = run_backtest(px, w, CostModel(0, 0))
    paid = run_backtest(px, w, CostModel(10, 5))
    # buy-and-hold trades once: 100% turnover at entry, ~0 afterwards
    assert paid.turnover.iloc[1] == pytest.approx(1.0)
    assert paid.turnover.iloc[5:].abs().max() < 1e-9
    assert (free.returns - paid.returns).sum() == pytest.approx(15e-4)


def test_future_signal_is_invisible_to_engine_but_caught_by_detector(prices):
    """The engine cannot know a weight was built from the future: the truncation
    detector is what catches it, which is why the pipeline always runs it."""
    from aster.validation.lookahead import check_truncation_invariance

    px = prices[["BTC/USDT"]]

    def cheat(p):
        return np.sign(p.pct_change(fill_method=None).shift(-1)).fillna(0)

    res = run_backtest(px, cheat(px), CostModel(0, 0), lag=1)
    assert summary(res.returns)["sharpe_ann"] > 10          # absurd: the tell-tale sign
    assert not check_truncation_invariance(cheat, px)["passed"]


def test_unlisted_asset_contributes_nothing(prices):
    w = pd.DataFrame(0.2, index=prices.index, columns=prices.columns)
    res = run_backtest(prices, w, CostModel(0, 0))
    assert (res.held["SOL/USDT"].iloc[:301] == 0).all()


def test_funding_paid_by_longs(prices):
    px = prices[["BTC/USDT"]]
    w = pd.DataFrame(1.0, index=px.index, columns=px.columns)
    f = pd.DataFrame(0.0001, index=px.index, columns=px.columns)
    a = run_backtest(px, w, CostModel(0, 0))
    b = run_backtest(px, w, CostModel(0, 0), funding=f, perp_legs="all")
    assert (a.returns - b.returns).iloc[2:].mean() == pytest.approx(0.0001)


def test_max_drawdown():
    r = pd.Series([0.1, -0.5, 0.2])
    assert max_drawdown(r) == pytest.approx(-0.5)


# --------------------------------------------------------------------------- #
# P2b tests: funding charged on perp legs only (delta-neutral contract)       #
# --------------------------------------------------------------------------- #


def test_funding_zero_when_no_perp_leg_marked(prices):
    """A spot-only book never pays funding, even if a funding panel is passed."""
    px = prices[["BTC/USDT"]]
    w = pd.DataFrame(1.0, index=px.index, columns=px.columns)
    f = pd.DataFrame(0.0001, index=px.index, columns=px.columns)
    a = run_backtest(px, w, CostModel(0, 0))                  # no funding
    b = run_backtest(px, w, CostModel(0, 0), funding=f)      # funding but no perp
    # b must equal a: the funding panel is ignored because no leg is marked perp
    np.testing.assert_allclose(b.returns, a.returns, atol=1e-12)
    assert b.meta["perp_legs"] == []


def test_funding_applied_only_to_marked_perp_leg(prices):
    """A spot + perp book charges funding on the perp leg only."""
    perp_sym = "BTC/USDT:USDT"
    px = prices[["BTC/USDT"]].copy()
    px[perp_sym] = px["BTC/USDT"]  # perp tracks spot
    w = pd.DataFrame(0.0, index=px.index, columns=px.columns)
    w["BTC/USDT"] = 0.5
    w[perp_sym] = -0.5
    f = pd.DataFrame(0.0001, index=px.index, columns=px.columns)
    no_perp = run_backtest(px, w, CostModel(0, 0), funding=f)
    with_perp = run_backtest(px, w, CostModel(0, 0), funding=f, perp_legs=[perp_sym])
    # Funding is only on the perp short: held[perp] = -0.5, rate = +0.0001,
    # fund = -5e-5 per bar, so with_perp.returns = no_perp.returns - (-5e-5)
    # = no_perp.returns + 5e-5. The mean delta (no_perp - with_perp) is -5e-5.
    delta = (no_perp.returns - with_perp.returns).iloc[2:]
    assert delta.mean() == pytest.approx(-0.0001 * 0.5, abs=1e-7)


def test_delta_neutral_pair_pays_funding_on_short_leg_only(prices):
    """Long spot + short perp on the same asset: funding hits the short only."""
    perp_sym = "BTC/USDT:USDT"
    px = prices[["BTC/USDT"]].copy()
    px[perp_sym] = px["BTC/USDT"]
    w = pd.DataFrame(0.0, index=px.index, columns=px.columns)
    w["BTC/USDT"] = 1.0
    w[perp_sym] = -1.0
    f = pd.DataFrame(0.0002, index=px.index, columns=px.columns)
    res = run_backtest(px, w, CostModel(0, 0), funding=f, perp_legs=[perp_sym])
    # funding applied to the short perp leg: net return loses ~2e-4 per bar
    assert res.funding.iloc[2:].mean() == pytest.approx(-0.0002, abs=1e-7)


def test_perp_legs_rejects_symbol_not_in_weights(prices):
    perp_sym = "BTC/USDT:USDT"
    px = prices[["BTC/USDT"]]
    w = pd.DataFrame(1.0, index=px.index, columns=px.columns)
    f = pd.DataFrame(0.0001, index=px.index, columns=px.columns)
    with pytest.raises(ValueError, match="perp_legs contains symbols not in the weight frame"):
        run_backtest(px, w, CostModel(0, 0), funding=f, perp_legs=[perp_sym])


def test_perp_legs_rejects_bogus_string(prices):
    px = prices[["BTC/USDT"]]
    w = pd.DataFrame(1.0, index=px.index, columns=px.columns)
    with pytest.raises(ValueError, match="perp_legs must be None"):
        run_backtest(px, w, CostModel(0, 0), perp_legs="bogus")


def test_funding_panel_with_unmarked_column_does_not_pollute(prices):
    """If the funding panel has a column the strategy does not hold, the
    engine must not invent a return out of it. Funding only enters via the
    held*perp_panel product.
    """
    perp_sym = "ETH/USDT:USDT"
    spot_sym = "BTC/USDT"
    px = prices[[spot_sym]].copy()
    px[perp_sym] = prices["ETH/USDT"]
    w = pd.DataFrame(0.0, index=px.index, columns=px.columns)
    w[spot_sym] = 1.0
    f = pd.DataFrame(0.0001, index=px.index, columns=px.columns)
    f[perp_sym] = 0.0005  # spurious funding on a leg the strategy does not hold
    res = run_backtest(px, w, CostModel(0, 0), funding=f, perp_legs=[perp_sym])
    # perp_legs marks the ETH perp, but the strategy holds 0 there; the
    # funding column is zeroed out for the unmarked BTC spot, so funding
    # stays at 0.
    assert res.funding.abs().max() < 1e-12


def test_backtest_result_meta_records_perp_legs(prices):
    perp_sym = "BTC/USDT:USDT"
    px = prices[["BTC/USDT"]].copy()
    px[perp_sym] = px["BTC/USDT"]
    w = pd.DataFrame(0.0, index=px.index, columns=px.columns)
    w["BTC/USDT"] = 0.5
    w[perp_sym] = -0.5
    res = run_backtest(px, w, CostModel(0, 0), perp_legs=[perp_sym])
    assert res.meta["perp_legs"] == [perp_sym]
