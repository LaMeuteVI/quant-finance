"""Tests for the Q10 per-alt volatility grid."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.q10_volatility import _bh, _inverse_leverage
from aster.research.n3_vol import dm_hln


def test_bh_is_monotone_and_fdr_bounded():
    q = _bh(np.array([0.001, 0.02, 0.5, 0.9]))
    assert np.all(q[:-1] <= q[1:])
    assert np.all((q >= 0) & (q <= 1))


def test_dm_equal_forecasts_are_null():
    stat, p = dm_hln(np.zeros(100))
    assert stat == 0.0
    assert p == 1.0


def test_inverse_leverage_reference_sign():
    idx = pd.date_range("2022-01-01", periods=100, freq="1d", tz="UTC")
    r = np.where(np.arange(100) % 2, 0.01, -0.01)
    rv = np.where(np.arange(100) % 2 == 0, 2.0, 1.0)
    d = pd.DataFrame({"daily_return": r, "rv": rv, "valid": True}, index=idx)
    out = _inverse_leverage(d)
    assert out["positive_mean"] > out["negative_mean"]
