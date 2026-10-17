"""Tests for the Q9 pre-cutoff N2 grid."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research.q9_intraday_n2 import CUTOFF, describe


def _series(phi: float, n: int = 8192) -> pd.Series:
    rng = np.random.default_rng(123)
    eps = rng.standard_normal(n) * 0.01
    r = np.zeros(n)
    for i in range(1, n):
        r[i] = phi * r[i - 1] + eps[i]
    idx = pd.date_range("2022-01-01", periods=n, freq="5min", tz="UTC")
    return pd.Series(100 * np.exp(np.cumsum(r)), index=idx)


def test_q9_describe_matches_q5_contract():
    out = describe(_series(-0.2))
    assert out["n_obs"] > 8000
    assert out["ret_autocorr"]["lag1"] < 0
    assert out["abs_ret_autocorr"]["lag1"] > -0.1
    assert out["variance_ratio"]["q2"] < 1.0
    assert 0.2 < out["hurst_rs"] < 0.8


def test_q9_positive_serial_dependence_has_vr_above_one():
    out = describe(_series(0.3))
    assert out["ret_autocorr"]["lag1"] > 0
    assert out["variance_ratio"]["q2"] > 1.0


def test_q9_rejects_post_cutoff_input():
    idx = pd.date_range("2024-06-30 23:55", periods=3, freq="5min", tz="UTC")
    with pytest.raises(ValueError, match="cutoff"):
        describe(pd.Series([100.0, 100.1, 100.2], index=idx))


def test_q9_rejects_empty_input():
    with pytest.raises(ValueError, match="empty"):
        describe(pd.Series(dtype=float, index=pd.DatetimeIndex([], tz="UTC")))
