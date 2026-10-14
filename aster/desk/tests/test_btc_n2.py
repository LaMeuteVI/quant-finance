"""Tests for the fixed BTC N2 descriptive study."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.btc_n2 import _bh_adjust, analyse


def test_bh_adjust_preserves_order_and_monotonicity() -> None:
    adjusted = _bh_adjust(np.array([0.01, 0.04, 0.20, 0.03]))
    assert adjusted[0] == 0.04
    assert adjusted[1] == 0.05333333333333334
    assert adjusted[2] == 0.20
    assert adjusted[3] == 0.05333333333333334


def test_n2_is_causal_in_its_formation_and_forward_definitions() -> None:
    index = pd.date_range("2020-01-01", periods=150, freq="D", tz="UTC")
    # Smooth deterministic path gives a well-defined continuation relation.
    prices = pd.Series(np.exp(np.linspace(0.0, 1.0, len(index))), index=index)
    result = analyse(prices)
    assert list(result["horizon_days"]) == [1, 3, 7, 14, 30, 60]
    assert bool((result["observations"] == 150 - 2 * result["horizon_days"]).all())
    assert bool((result["bootstrap_count"] == 10_000).all())
    assert bool(result["one_day_lag_placebo_correlation"].notna().all())


def test_n2_rejects_post_cutoff_input() -> None:
    index = pd.date_range("2024-06-30", periods=2, freq="D", tz="UTC")
    prices = pd.Series([1.0, 1.1], index=index)
    try:
        analyse(prices)
    except ValueError as exc:
        assert "cutoff" in str(exc)
    else:
        raise AssertionError("post-cutoff input must be rejected")
