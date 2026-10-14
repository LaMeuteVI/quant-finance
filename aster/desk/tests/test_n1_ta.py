"""Reference tests for the BTC/ETH N1 TA study."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research.n1_ta import (
    bollinger,
    donchian,
    fib_levels,
    rsi,
    sma_cross,
)


def test_rsi_constant_is_50():
    close = pd.Series(np.full(50, 100.0))
    out = rsi(close, 14)
    assert out.iloc[-1] == pytest.approx(50.0)


def test_rsi_uptrend_eventually_high():
    close = pd.Series(np.linspace(100.0, 130.0, 200))
    out = rsi(close, 14)
    # Wilder convention: pure uptrend -> RSI = 100.
    assert out.iloc[-1] == pytest.approx(100.0)


def test_bollinger_known_value():
    close = pd.Series(np.arange(20, dtype=float))
    low, up = bollinger(close, 20, 2.0)
    assert low.iloc[-1] == pytest.approx(close.mean() - 2.0 * close.std())
    assert up.iloc[-1] == pytest.approx(close.mean() + 2.0 * close.std())


def test_donchian_uses_previous_window():
    idx = pd.date_range("2024-01-01", periods=25, freq="D")
    high = pd.Series(np.arange(25, dtype=float) + 100.0, index=idx)
    low = pd.Series(np.arange(25, dtype=float) + 80.0, index=idx)
    hi, lo = donchian(high, low, length=20)
    # rolling(20).max().shift(1): at t=24 the window is bars 4..23.
    assert hi.iloc[-1] == pytest.approx(123.0)
    assert lo.iloc[-1] == pytest.approx(84.0)


def test_sma_cross_sign():
    close = pd.Series(np.linspace(100.0, 110.0, 200))
    cross = sma_cross(close, 5, 20)
    assert cross.iloc[-1] == 1


def test_fib_levels_midpoint():
    swing_hi = pd.Series([120.0])
    swing_lo = pd.Series([80.0])
    mid = fib_levels(swing_hi, swing_lo, 0.5)
    assert mid.iloc[0] == pytest.approx(100.0)
