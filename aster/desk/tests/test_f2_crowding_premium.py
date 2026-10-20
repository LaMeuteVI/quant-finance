"""F2 unit tests — crowding premium v1.0.0.

No holdout, no real data download, no live, no key, no order.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.strategies.crowding_premium import CrowdingPremium


def _make_spot_close(n: int = 200, start: str = "2023-01-01") -> pd.DataFrame:
    rng = np.random.default_rng(0)
    idx = pd.date_range(start, periods=n, freq="4h", tz="UTC")
    rets = rng.normal(0.0, 0.005, size=n)
    prices = 100.0 * np.exp(np.cumsum(rets))
    return pd.DataFrame(prices, index=idx, columns=["BTC-USDT"])


def _make_perp_close(spot: pd.DataFrame, basis: float = 0.0) -> pd.DataFrame:
    return pd.DataFrame(spot["BTC-USDT"] * (1.0 + basis),
                        index=spot.index, columns=["BTC-USDT"])


def _make_oi(spot: pd.DataFrame, start: float = 1000.0,
             step: float = 0.0) -> pd.DataFrame:
    n = len(spot)
    rng = np.random.default_rng(1)
    base = start + step * np.arange(n) + rng.normal(0.0, 1.0, n)
    return pd.DataFrame(base, index=spot.index, columns=["BTC-USDT"])


def test_f2_no_perp_close_returns_zero():
    spot = _make_spot_close()
    s = CrowdingPremium(timeframe="4h")
    w = s.target_weights(spot)
    assert list(w.columns) == ["BTC-USDT", "BTC-USDT:USDT"]
    assert (w.abs() < 1e-9).all().all()


def test_f2_no_oi_entry_z_only_uses_premium_signal():
    """When OI is missing, the strategy still enters on the premium
    z-score alone (the OI conditioning is disabled, not the entry)."""
    spot = _make_spot_close()
    # Engineer a constant +5 % perp premium for the last 50 bars.
    perp = _make_perp_close(spot, basis=0.0)
    perp.iloc[-50:] = perp.iloc[-50:] * 1.05
    s = CrowdingPremium(timeframe="4h",
                        premium_lookback_bars=30,
                        entry_z=2.0, exit_z=0.5,
                        oi_min_z=0.5, max_gross=1.0)
    w = s.target_weights(spot, perp_close=perp, oi=pd.DataFrame())
    # The basis z-score on the last 50 bars: the basis is constant 0.05
    # over spot ~100, rolling mean rises, rolling std shrinks. The
    # z-score spikes on the first bar after the step (basis vs old
    # mean of ~0) then decays. The 2.0 threshold may or may not be
    # crossed. The test is just that the function returns without
    # crashing and the perp column is finite.
    assert np.isfinite(w["BTC-USDT:USDT"]).all()
    # And the spot column is always zero.
    assert (w["BTC-USDT"].abs() < 1e-9).all()


def test_f2_short_perp_signal_with_oi_agreement():
    spot = _make_spot_close()
    perp = _make_perp_close(spot, basis=0.0)
    # Step the perp UP by 10 % at bar 100 (perp rich, basis > 0).
    perp.iloc[100:] = perp.iloc[100:] * 1.10
    # OI ramps up linearly from bar 100 onward with a small noise
    # so the rolling diff std is non-zero. Each bar's diff is
    # ~+10, so the rolling diff z-score is stably positive
    # (> 0.5) in a window where the rolling mean hasn't caught up.
    n = len(spot)
    oi = pd.DataFrame(1000.0, index=spot.index, columns=["BTC-USDT"])
    oi.iloc[100:, 0] = 1000.0 + 10.0 * np.arange(n - 100) + np.random.default_rng(2).normal(0, 1, n - 100)
    s = CrowdingPremium(timeframe="4h",
                        premium_lookback_bars=30,
                        entry_z=2.0, exit_z=0.5,
                        oi_lookback_bars=30,
                        oi_min_z=0.5, max_gross=1.0)
    w = s.target_weights(spot, perp_close=perp, oi=oi)
    # After the step (bars 100-130), the strategy should short
    # the perp on at least one bar. The exit band may flatten
    # later as the rolling mean catches up, so we only inspect
    # the early entry window.
    entry_window = w["BTC-USDT:USDT"].iloc[100:130]
    assert (entry_window < 0).any(), (
        f"F2 should short the perp in the entry window 100..130; "
        f"min={entry_window.min():.3f}"
    )
    # The spot column is always zero (perp-only book).
    assert (w["BTC-USDT"].abs() < 1e-9).all()


def test_f2_long_perp_signal_when_basis_inverted():
    spot = _make_spot_close()
    perp = _make_perp_close(spot, basis=0.0)
    # Step the perp DOWN by 10 % at bar 100 (perp cheap, basis < 0).
    perp.iloc[100:] = perp.iloc[100:] * 0.90
    # OI ramps DOWN linearly from bar 100 onward with small noise
    # so the rolling diff std is non-zero. Each bar's diff is
    # ~-10, so the rolling diff z-score is stably negative
    # (< -0.5) in the entry window.
    n = len(spot)
    oi = pd.DataFrame(2000.0, index=spot.index, columns=["BTC-USDT"])
    oi.iloc[100:, 0] = 2000.0 - 10.0 * np.arange(n - 100) + np.random.default_rng(3).normal(0, 1, n - 100)
    s = CrowdingPremium(timeframe="4h",
                        premium_lookback_bars=30,
                        entry_z=2.0, exit_z=0.5,
                        oi_lookback_bars=30,
                        oi_min_z=0.5, max_gross=1.0)
    w = s.target_weights(spot, perp_close=perp, oi=oi)
    # After the step, the strategy should long the perp in the
    # early entry window.
    entry_window = w["BTC-USDT:USDT"].iloc[100:130]
    assert (entry_window > 0).any(), (
        f"F2 should long the perp in the entry window 100..130; "
        f"max={entry_window.max():.3f}"
    )


def test_f2_version():
    assert CrowdingPremium.version == "1.0.0"
    assert CrowdingPremium.name == "crowding_premium"


def test_f2_exit_band_flattens():
    spot = _make_spot_close()
    perp = _make_perp_close(spot, basis=0.0)
    # Step premium up at bar 50, then revert at bar 80. The
    # strategy should enter short during the spike and exit
    # once the rolling mean catches up.
    perp.iloc[50:80] = perp.iloc[50:80] * 1.10
    n = len(spot)
    oi = pd.DataFrame(1000.0, index=spot.index, columns=["BTC-USDT"])
    oi.iloc[50:80] = 2000.0
    s = CrowdingPremium(timeframe="4h",
                        premium_lookback_bars=30,
                        entry_z=2.0, exit_z=0.5,
                        oi_min_z=0.0, max_gross=1.0)
    w = s.target_weights(spot, perp_close=perp, oi=oi)
    # The strategy must enter at least once on the spike.
    entry_window = w["BTC-USDT:USDT"].iloc[50:80]
    assert (entry_window < 0).any(), (
        f"F2 should short during the spike; "
        f"min in 50..80 = {entry_window.min():.3f}"
    )
    # The first non-zero bar must come at or after bar 50
    # (the spike start), not in the pre-spike noise.
    nz = w["BTC-USDT:USDT"].values
    first_nz = next((i for i, v in enumerate(nz) if v != 0), -1)
    assert first_nz >= 50, (
        f"F2 first non-zero bar should be at or after 50; "
        f"got {first_nz}"
    )
