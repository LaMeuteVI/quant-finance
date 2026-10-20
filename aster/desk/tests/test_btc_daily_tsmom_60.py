"""Unit tests for the registered BTC 60-day momentum baseline."""
from __future__ import annotations

import pandas as pd
import pytest

from aster.strategies.btc_daily_tsmom_60 import BTCDailyTSMom60
from aster.validation.lookahead import check_truncation_invariance


def _prices() -> pd.DataFrame:
    index = pd.date_range("2023-01-01", periods=180, freq="D", tz="UTC")
    # First trend upward, then downward: both rule branches must be observable.
    values = list(range(100, 190)) + list(range(190, 100, -1))
    return pd.DataFrame({"BTC/USDT": values}, index=index, dtype=float)


def test_btc_daily_tsmom_is_cash_during_warmup_and_long_after_positive_trend() -> None:
    prices = _prices()
    weights = BTCDailyTSMom60().target_weights(prices)
    assert (weights.iloc[:60, 0] == 0.0).all()
    assert weights.iloc[80, 0] > 0.0


def test_btc_daily_tsmom_goes_to_cash_after_negative_60_day_return() -> None:
    prices = _prices()
    weights = BTCDailyTSMom60().target_weights(prices)
    assert weights.iloc[-1, 0] == pytest.approx(0.0)


def test_btc_daily_tsmom_is_causal() -> None:
    prices = _prices()
    assert check_truncation_invariance(BTCDailyTSMom60().target_weights, prices)["passed"]


def test_btc_daily_tsmom_refuses_a_universe_without_btc() -> None:
    prices = _prices().rename(columns={"BTC/USDT": "ETH/USDT"})
    with pytest.raises(ValueError, match="BTC/USDT"):
        BTCDailyTSMom60().target_weights(prices)
