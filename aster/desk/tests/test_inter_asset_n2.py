"""Tests for BTC/ETH inter-asset descriptive diagnostics."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.inter_asset_n2 import _bh_adjust, analyse


def test_bh_adjust_is_monotone_in_sorted_p_values() -> None:
    out = _bh_adjust(np.array([0.01, 0.02, 0.9]))
    assert np.all(out <= 1.0)
    assert out[0] <= out[1] <= out[2]


def test_inter_asset_analysis_has_fixed_grid_and_annual_output() -> None:
    index = pd.date_range("2019-01-01", periods=1500, freq="D", tz="UTC")
    btc = np.exp(np.cumsum(np.sin(np.arange(len(index)) / 17.0) * 0.001))
    eth = np.exp(np.cumsum(np.sin(np.arange(len(index)) / 17.0) * 0.001 + 0.0002))
    panel = pd.DataFrame({"BTC/USDT": btc, "ETH/USDT": eth}, index=index)
    grid, annual, residuals = analyse(panel)
    assert len(grid) == 6 * (1 + 4 * 2)
    assert set(grid["direction"]) == {"BTC_to_ETH", "ETH_to_BTC"}
    assert len(annual) == 4
    assert len(residuals) == 48
    assert bool((grid["bh_q_value"] >= 0).all())


def test_inter_asset_analysis_rejects_post_cutoff() -> None:
    index = pd.date_range("2024-06-30", periods=2, freq="D", tz="UTC")
    panel = pd.DataFrame({"BTC/USDT": [1.0, 1.1], "ETH/USDT": [1.0, 1.1]}, index=index)
    try:
        analyse(panel)
    except ValueError as exc:
        assert "cutoff" in str(exc)
    else:
        raise AssertionError("post-cutoff input must be rejected")
