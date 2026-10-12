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
    b = run_backtest(px, w, CostModel(0, 0), funding=f)
    assert (a.returns - b.returns).iloc[2:].mean() == pytest.approx(0.0001)


def test_max_drawdown():
    r = pd.Series([0.1, -0.5, 0.2])
    assert max_drawdown(r) == pytest.approx(-0.5)
