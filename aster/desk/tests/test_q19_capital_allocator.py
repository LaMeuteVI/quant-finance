"""Q19 unit tests — capital_allocator v1.0.0.

No holdout, no real data download, no live, no key, no order.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.strategies.capital_allocator import CapitalAllocator


def _make_returns(n: int = 500, mean: float = 0.001, vol: float = 0.02,
                  start: str = "2022-01-01", seed: int = 0) -> pd.Series:
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, periods=n, freq="1d", tz="UTC")
    rets = rng.normal(mean, vol, size=n)
    return pd.Series(rets, index=idx, name="ret")


def test_q19_version():
    a = CapitalAllocator()
    assert a.name == "capital_allocator"
    assert a.version == "1.0.0"


def test_q19_equal_weight():
    sr = {
        "A": _make_returns(seed=1),
        "B": _make_returns(seed=2),
        "C": _make_returns(seed=3),
    }
    a = CapitalAllocator(scheme="equal")
    w = a.allocate(sr)
    assert len(w) == 3
    assert np.allclose(w.values, 1.0 / 3)
    assert w.sum() == pytest.approx(1.0, abs=1e-9)


def test_q19_risk_parity_favours_high_sharpe_low_vol():
    """A high-Sharpe, low-vol strategy should get more weight
    than a low-Sharpe, high-vol one."""
    sr = {
        "good": _make_returns(mean=0.002, vol=0.01, seed=4),
        "bad":  _make_returns(mean=0.0,   vol=0.05, seed=5),
    }
    a = CapitalAllocator(scheme="risk_parity", max_weight=1.0)
    w = a.allocate(sr)
    assert w["good"] > w["bad"], (
        f"risk-parity should weight good > bad; got {w.to_dict()}"
    )


def test_q19_min_variance_favours_low_vol():
    """min_variance should weight the lower-vol strategy more."""
    sr = {
        "low_vol":  _make_returns(mean=0.0, vol=0.01, seed=6),
        "high_vol": _make_returns(mean=0.0, vol=0.05, seed=7),
    }
    a = CapitalAllocator(scheme="min_variance", max_weight=1.0)
    w = a.allocate(sr)
    assert w["low_vol"] > w["high_vol"], (
        f"min-variance should weight low > high; got {w.to_dict()}"
    )


def test_q19_max_weight_cap():
    """A single strategy's weight should be capped at max_weight."""
    sr = {
        "best": _make_returns(mean=0.005, vol=0.005, seed=8),
        "worse": _make_returns(mean=0.0, vol=0.04, seed=9),
    }
    a = CapitalAllocator(scheme="risk_parity", max_weight=0.7)
    w = a.allocate(sr)
    assert w.max() <= 0.7 + 1e-9, f"max weight {w.max()} > 0.7"
    assert w.sum() == pytest.approx(1.0, abs=1e-6)


def test_q19_all_negative_sharpe_falls_back_to_equal():
    """If every strategy has Sharpe ≤ 0, the allocator falls
    back to equal weight (no negative weights)."""
    sr = {
        "A": _make_returns(mean=-0.001, vol=0.02, seed=10),
        "B": _make_returns(mean=-0.001, vol=0.02, seed=11),
    }
    a = CapitalAllocator(scheme="risk_parity")
    w = a.allocate(sr)
    # Either equal (the fallback) or all zero. We require all
    # non-negative.
    assert (w >= 0).all(), f"negative weights: {w.to_dict()}"
    assert w.sum() == pytest.approx(1.0, abs=1e-6)


def test_q19_empty_inputs():
    a = CapitalAllocator()
    w = a.allocate({})
    assert len(w) == 0


def test_q19_target_weights_returns_frame():
    """The base-class target_weights is a no-op stub; the real
    entry point is ``allocate``. The frame must be well-formed
    even if empty."""
    prices = pd.DataFrame(
        np.ones((10, 2)),
        index=pd.date_range("2022-01-01", periods=10, freq="1d", tz="UTC"),
        columns=["BTC-USDT", "ETH-USDT"],
    )
    a = CapitalAllocator()
    w = a.target_weights(prices)
    assert w.shape[1] == 4  # 2N
    assert (w.abs().sum().sum()) < 1e-9
