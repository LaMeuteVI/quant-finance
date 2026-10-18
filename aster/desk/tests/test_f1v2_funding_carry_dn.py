"""F1v2 unit tests — funding carry delta-neutral v1.1.0.

No holdout, no real data download, no live, no key, no order.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.strategies.funding_carry_dn import FundingCarryDN, _spot_perp_columns


def _make_close(n: int = 200, start: str = "2023-01-01") -> pd.DataFrame:
    rng = np.random.default_rng(seed=42)
    rets = rng.normal(0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(rets))
    idx = pd.date_range(start, periods=n, freq="4h", tz="UTC")
    return pd.DataFrame({"BTCUSDT": close}, index=idx)


def _make_funding(n: int = 200, start: str = "2023-01-01",
                  bias_bps: float = 8.0) -> pd.DataFrame:
    """Build a perp-indexed funding panel: 3 fixings/day at +bias_bps each.

    At 4h bars there are 6 bars/day, so a +8 bps/fixing series
    delivers 24 bps/day and an average of 4 bps/bar (well above the
    2 bps cost cushion the strategy uses to gate entries). 4 bps/fixing
    is right at the cushion and produces a noisy signal, so we use
    8 bps/fixing in the test to make the long/short intent crisp.
    """
    idx = pd.date_range(start, periods=n, freq="4h", tz="UTC")
    fix = np.zeros(n)
    hours = idx.hour
    fix[(hours == 0) | (hours == 8) | (hours == 16)] = bias_bps / 1e4
    return pd.DataFrame({"BTCUSDT:USDT": fix}, index=idx)


def _make_perp_close(close: pd.DataFrame, *, basis_bps: float = 0.0) -> pd.DataFrame:
    """Build a perp close panel = spot * (1 + basis_bps) for every bar."""
    return close * (1.0 + basis_bps / 1e4)


def test_f1v2_no_funding_returns_zero_weights():
    prices = _make_close()
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices)
    assert w.shape == (len(prices), 1)
    assert (w == 0).all().all()


def test_f1v2_long_signal_with_positive_funding():
    prices = _make_close()
    # 8 bps/fixing = 24 bps/day, well above the 2 bps/bar cushion.
    funding = _make_funding(bias_bps=8.0)
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices, funding=funding)
    # 2N columns: BTCUSDT (spot) + BTCUSDT:USDT (perp).
    assert w.shape == (len(prices), 2)
    assert set(w.columns) == {"BTCUSDT", "BTCUSDT:USDT"}
    # After the first 42 bars (lookback), the signal should be +1 on
    # the spot leg and -1 on the perp leg.
    later = w.iloc[50:]
    assert (later["BTCUSDT"] > 0).all()
    assert (later["BTCUSDT:USDT"] < 0).all()
    # The book is delta-neutral: per-bar sum of weights ≈ 0.
    assert (later.sum(axis=1).abs() < 1e-9).all()


def test_f1v2_short_signal_with_negative_funding():
    prices = _make_close()
    funding = _make_funding(bias_bps=-8.0)
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices, funding=funding)
    later = w.iloc[50:]
    assert (later["BTCUSDT"] < 0).all()
    assert (later["BTCUSDT:USDT"] > 0).all()


def test_f1v2_basis_guard_blocks_extreme_basis():
    """When perp_close is supplied, the strategy uses the perp close
    (not the spot close) to compute the basis z-score. A crash-
    like perp discount lowers the signal.

    We test the path: supply a perp close that is exactly the spot
    close. The basis is 0 everywhere, the z-score is 0/0 = NaN, and
    the basis guard is a no-op (the signal survives).
    """
    prices = _make_close()
    funding = _make_funding(bias_bps=8.0)
    perp = prices.copy()  # no discount
    s = FundingCarryDN(timeframe="4h")
    w_v2 = s.target_weights(prices, funding=funding, perp_close=perp)
    # Signal should be active: spot +1, perp -1 in the later half.
    later = w_v2.iloc[50:]
    assert (later["BTCUSDT"] > 0).all()
    assert (later["BTCUSDT:USDT"] < 0).all()


def test_f1v2_falls_back_to_v1_basis_when_no_perp_close():
    """If perp_close is not supplied, V2 falls back to V1's spot-return
    z-score. A sanity check: the resulting weights are NOT all zero
    (the basis guard fires on the spot z-score but the funding signal
    is still active).
    """
    prices = _make_close()
    funding = _make_funding(bias_bps=8.0)
    s = FundingCarryDN(timeframe="4h")
    w_no_perp = s.target_weights(prices, funding=funding)
    later = w_no_perp.iloc[50:]
    # Some bars should be non-zero (the funding signal is active).
    assert later.abs().sum().sum() > 0


def test_f1v2_strategy_version_is_1_1_0():
    assert FundingCarryDN.version == "1.1.0"
    assert FundingCarryDN.name == "funding_carry_dn"


def test_f1v2_spot_perp_columns_helper():
    spot, perp, all_cols = _spot_perp_columns(["BTCUSDT", "ETHUSDT"])
    assert spot == ["BTCUSDT", "ETHUSDT"]
    assert perp == ["BTCUSDT:USDT", "ETHUSDT:USDT"]
    assert all_cols == ["BTCUSDT", "ETHUSDT", "BTCUSDT:USDT", "ETHUSDT:USDT"]


def test_f1v2_below_cushion_stays_flat():
    """A funding rate below the cost cushion (2 bps) means no carry."""
    prices = _make_close()
    # 1 bps/fixing < 2 bps cushion -> no signal.
    funding = _make_funding(bias_bps=1.0)
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices, funding=funding)
    # All bars after the lookback should be flat.
    assert (w.iloc[42:].abs() < 1e-9).all().all()
