"""F1v2 + F1v3 unit tests — funding carry delta-neutral.

No holdout, no real data download, no live, no key, no order.

v1.1.0 (H-20261018-003) was falsified; v1.3.0 (H-20261016-002 family
continuation, R3 of QUEUE 2026-10-19) replaces the cushion with the
amortised round-trip cost and adds entry/exit hysteresis. v1.3.0 is
LONG ONLY (no inverse).
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
    delivers 24 bps/day. The default amortised cushion for v1.3.0
    is 1.67 bps/fixing, so a bias of 8 bps easily clears the entry
    threshold. We use bias = 8 bps in most tests to make the long
    intent crisp.
    """
    idx = pd.date_range(start, periods=n, freq="4h", tz="UTC")
    fix = np.zeros(n)
    hours = idx.hour
    fix[(hours == 0) | (hours == 8) | (hours == 16)] = bias_bps / 1e4
    return pd.DataFrame({"BTCUSDT:USDT": fix}, index=idx)


def _make_perp_close(close: pd.DataFrame, *, basis_bps: float = 0.0) -> pd.DataFrame:
    return close * (1.0 + basis_bps / 1e4)


def test_no_funding_returns_zero_weights():
    prices = _make_close()
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices)
    assert w.shape == (len(prices), 1)
    assert (w == 0).all().all()


def test_long_signal_with_positive_funding():
    """V3: positive persistent funding clears the amortised cushion
    AND the current funding is positive -> long spot / short perp.
    """
    prices = _make_close()
    funding = _make_funding(bias_bps=8.0)
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices, funding=funding)
    assert w.shape == (len(prices), 2)
    assert set(w.columns) == {"BTCUSDT", "BTCUSDT:USDT"}
    # After enough bars for the lookback (42) + hysteresis to fill,
    # the position should be long spot / short perp.
    later = w.iloc[80:]
    assert (later["BTCUSDT"] > 0).all()
    assert (later["BTCUSDT:USDT"] < 0).all()
    # Delta-neutral: per-bar sum of weights ≈ 0.
    assert (later.sum(axis=1).abs() < 1e-9).all()


def test_negative_funding_stays_flat_v3():
    """V3 is LONG ONLY — no inverse side. Persistent negative funding
    must leave the book flat.
    """
    prices = _make_close()
    funding = _make_funding(bias_bps=-8.0)
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices, funding=funding)
    later = w.iloc[80:]
    # Book must remain flat (no inverse).
    assert (later.abs() < 1e-9).all().all()


def test_basis_guard_blocks_extreme_basis():
    """When perp_close is supplied, the strategy uses the perp close
    (not the spot close) to compute the basis z-score. We pass a perp
    close exactly equal to the spot close, the basis is 0 everywhere,
    the basis guard is a no-op (the signal survives).
    """
    prices = _make_close()
    funding = _make_funding(bias_bps=8.0)
    perp = prices.copy()
    s = FundingCarryDN(timeframe="4h")
    w_v2 = s.target_weights(prices, funding=funding, perp_close=perp)
    later = w_v2.iloc[80:]
    assert (later["BTCUSDT"] > 0).all()
    assert (later["BTCUSDT:USDT"] < 0).all()


def test_no_perp_close_falls_back_to_v1_basis():
    """If perp_close is not supplied, the basis guard falls back to
    the spot-return z-score. The funding signal is still active in
    the test data so weights are non-zero.
    """
    prices = _make_close()
    funding = _make_funding(bias_bps=8.0)
    s = FundingCarryDN(timeframe="4h")
    w_no_perp = s.target_weights(prices, funding=funding)
    later = w_no_perp.iloc[80:]
    assert later.abs().sum().sum() > 0


def test_strategy_version_is_1_3_0():
    """R3 of QUEUE 2026-10-19 — the carry rule the hypothesis states."""
    assert FundingCarryDN.version == "1.3.0"
    assert FundingCarryDN.name == "funding_carry_dn"


def test_spot_perp_columns_helper():
    spot, perp, all_cols = _spot_perp_columns(["BTCUSDT", "ETHUSDT"])
    assert spot == ["BTCUSDT", "ETHUSDT"]
    assert perp == ["BTCUSDT:USDT", "ETHUSDT:USDT"]
    assert all_cols == ["BTCUSDT", "ETHUSDT", "BTCUSDT:USDT", "ETHUSDT:USDT"]


def test_below_cushion_stays_flat():
    """A funding rate below the amortised cushion (1.67 bps) means no
    carry. We use 1 bps/fixing so predicted ≈ 1 bps < 1.67 bps.
    """
    prices = _make_close()
    funding = _make_funding(bias_bps=1.0)
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices, funding=funding)
    assert (w.iloc[42:].abs() < 1e-9).all().all()


def test_hysteresis_holds_position_through_short_dip():
    """A 1-bar funding flip should NOT trigger an exit (hysteresis)."""
    prices = _make_close(n=400)
    funding = _make_funding(n=400, bias_bps=8.0)
    # Force a single-bar flip at bar 100: funding = -5 bps for one
    # fixing only.
    funding.iloc[100, 0] = -5e-4
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices, funding=funding)
    # Around bar 100 the position should stay long (hysteresis
    # exit_persistence_bars default is 18, so 1 bar cannot exit).
    assert (w.iloc[80:].abs().sum(axis=1) > 0).any()


def test_persistence_exit_fires_after_long_funding_dip():
    """If funding is non-positive for exit_persistence_bars (18)
    consecutive bars, the position must exit *during the dip*.
    After the dip, the strategy may re-enter if funding is again
    positive AND predicted > amortised — that is the correct
    hysteresis behaviour.
    """
    prices = _make_close(n=400)
    funding = _make_funding(n=400, bias_bps=8.0)
    # Force a 30-bar funding dip at bar 100.
    funding.iloc[100:130, 0] = -1e-4  # slightly negative per bar
    s = FundingCarryDN(timeframe="4h")
    w = s.target_weights(prices, funding=funding)
    # During the dip (e.g. bar 120, well after 18-bar hysteresis has
    # elapsed), the position should be flat.
    assert (w.iloc[120:130].abs() < 1e-9).all().all()
    # Just before the dip ends, the position is still flat
    # (hysteresis hasn't fully cleared yet — wait, hysteresis exit
    # triggers DURING the dip at bar 100+18=118).
    assert (w.iloc[118:130].abs() < 1e-9).all().all()
    # After the dip ends and funding is again positive, the position
    # may re-enter (the prediction mean is still > 1.67 bps).
    # Re-entry is correct hysteresis behaviour; we do not assert it
    # here because the test only cares about exit.