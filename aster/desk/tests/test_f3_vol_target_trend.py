"""F3 unit tests — vol_target_trend_ensemble v1.0.0.

No holdout, no real data download, no live, no key, no order.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.strategies.vol_target_trend_ensemble import VolTargetTrendEnsemble


def _make_close(n: int = 500, start: str = "2022-01-01",
                drift: float = 0.001, vol: float = 0.02,
                seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, periods=n, freq="1d", tz="UTC")
    rets = rng.normal(drift, vol, size=n)
    prices = 100.0 * np.exp(np.cumsum(rets))
    return pd.DataFrame(prices, index=idx, columns=["BTC-USDT"])


def _make_panel(n: int = 500, start: str = "2022-01-01", seed: int = 0) -> pd.DataFrame:
    """Two assets, one trending up, one choppy."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, periods=n, freq="1d", tz="UTC")
    # Up trending
    up = 100.0 * np.exp(np.cumsum(rng.normal(0.002, 0.02, n)))
    # Choppy / mean-reverting
    chop = 100.0 * np.exp(np.cumsum(rng.normal(0.0, 0.03, n)))
    return pd.DataFrame({"UP": up, "CHOP": chop}, index=idx)


def test_f3_version():
    s = VolTargetTrendEnsemble(timeframe="1d")
    assert s.name == "vol_target_trend_ensemble"
    assert s.version == "1.1.0"


def test_f3_no_perp_leg_returns_zeros():
    """Without a perp_legs list, the engine treats the result as
    all-spot. The strategy should still emit a frame, but the
    spot leg is always 0 in this implementation."""
    close = _make_close()
    s = VolTargetTrendEnsemble(timeframe="1d")
    w = s.target_weights(close)
    assert (w["BTC-USDT"].abs() < 1e-9).all()


def test_f3_trend_long_signal():
    """A consistent up-trend should produce a long perp position."""
    close = _make_close(drift=0.005, vol=0.01, seed=1)  # strong up
    s = VolTargetTrendEnsemble(
        timeframe="1d",
        lookbacks=[20, 60, 120],
        re_entry_lookback=5,
        vol_target_ann=0.10,
        vol_lookback_days=60,
        gross_cap=1.5,
    )
    w = s.target_weights(close)
    perp = w["BTC-USDT:USDT"]
    # The signal should be positive on most of the late sample.
    tail = perp.iloc[200:]
    assert (tail > 0).sum() / len(tail) > 0.5, (
        f"F3 should be long on a consistent up-trend; "
        f"positive frac = {(tail > 0).sum() / len(tail):.2f}"
    )


def test_f3_trend_short_signal():
    """A consistent down-trend should produce a short perp position."""
    close = _make_close(drift=-0.005, vol=0.01, seed=2)  # strong down
    s = VolTargetTrendEnsemble(
        timeframe="1d",
        lookbacks=[20, 60, 120],
        re_entry_lookback=5,
        vol_target_ann=0.10,
        vol_lookback_days=60,
        gross_cap=1.5,
    )
    w = s.target_weights(close)
    perp = w["BTC-USDT:USDT"]
    tail = perp.iloc[200:]
    assert (tail < 0).sum() / len(tail) > 0.5, (
        f"F3 should be short on a consistent down-trend; "
        f"negative frac = {(tail < 0).sum() / len(tail):.2f}"
    )


def test_f3_vol_target_scales_position():
    """High-vol asset should get a smaller position than a low-vol
    asset (same signal)."""
    # Two panels: one with low vol, one with high vol, both
    # trending up at the same drift.
    low_vol = _make_close(drift=0.003, vol=0.005, seed=10, n=400)
    high_vol = _make_close(drift=0.003, vol=0.040, seed=11, n=400)
    s = VolTargetTrendEnsemble(
        timeframe="1d",
        lookbacks=[20, 60, 120],
        re_entry_lookback=5,
        vol_target_ann=0.10,
        vol_lookback_days=60,
        gross_cap=1.5,
    )
    w_low = s.target_weights(low_vol)["BTC-USDT:USDT"]
    w_high = s.target_weights(high_vol)["BTC-USDT:USDT"]
    # Average |weight| in the steady-state window.
    avg_low = w_low.iloc[250:].abs().mean()
    avg_high = w_high.iloc[250:].abs().mean()
    assert avg_low > avg_high, (
        f"low-vol asset should have larger |w|; got "
        f"low={avg_low:.3f} vs high={avg_high:.3f}"
    )


def test_f3_cold_start_is_flat():
    """Before the rolling windows are populated, the strategy
    should emit zero weights."""
    close = _make_close(n=50)  # less than min_history=120
    s = VolTargetTrendEnsemble(timeframe="1d")
    w = s.target_weights(close)
    assert w.abs().sum().sum() < 1e-9, (
        f"F3 should be flat in the cold-start window; got "
        f"max |w| = {w.abs().max().max():.6f}"
    )


def test_f3_gross_cap_respected():
    """The sum of |weights| on the perp leg should never exceed
    gross_cap on any bar."""
    panel = _make_panel(seed=42, n=500)
    s = VolTargetTrendEnsemble(
        timeframe="1d",
        lookbacks=[20, 60, 120],
        re_entry_lookback=5,
        vol_target_ann=0.10,
        vol_lookback_days=60,
        gross_cap=1.5,
    )
    w = s.target_weights(panel)
    # Only the perp leg has any weight; sum |w| on each bar.
    perp = w[["UP:USDT", "CHOP:USDT"]]
    gross = perp.abs().sum(axis=1)
    assert gross.max() <= 1.5 + 1e-6, (
        f"F3 gross cap violated; max = {gross.max():.4f}"
    )
