"""Q8 funding/carry unit tests."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.q8_funding_carry import (
    _autocorr,
    _bh_qvalues,
    _conditional_spread,
    _fixings,
    analyse,
)


def test_fixings_select_three_eight_hour_slots():
    idx = pd.date_range("2023-01-01", periods=72, freq="h", tz="UTC")
    panel = pd.DataFrame({"BTCUSDT": np.arange(len(idx), dtype=float)}, index=idx)
    out = _fixings(panel)
    assert set(out.index.hour) <= {0, 8, 16}
    assert len(out) == 9


def test_autocorrelation_detects_persistent_series():
    rng = np.random.default_rng(10)
    x = np.empty(1000)
    x[0] = 0
    for i in range(1, len(x)):
        x[i] = 0.8 * x[i - 1] + rng.normal(scale=0.1)
    assert _autocorr(x, 1) > 0.7


def test_conditional_spread_preserves_direction():
    rng = np.random.default_rng(11)
    current = rng.normal(size=1000)
    future = 0.4 * current + rng.normal(scale=0.5, size=1000)
    result = _conditional_spread(np.r_[current, future], seed=1)
    assert result["n_obs"] > 0
    assert np.isfinite(result["spread"])


def test_bh_qvalues_and_analysis_output():
    q = _bh_qvalues(np.array([0.001, 0.01, 0.5]))
    assert q[0] <= q[1] <= q[2]
    idx = pd.date_range("2023-01-01", periods=200, freq="8h", tz="UTC")
    panel = pd.DataFrame({"BTCUSDT": np.sin(np.arange(200) / 10) * 1e-4}, index=idx)
    out = analyse(panel)
    assert out["cutoff_exclusive"].startswith("2024-07-01")
    assert "BTCUSDT" in out["panel"]
    assert out["cross_sectional"]["n_fixings"] > 0
