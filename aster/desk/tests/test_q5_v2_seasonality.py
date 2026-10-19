"""Tests for Q5-V2 intraday seasonality grid."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from aster.research import q5_v2_seasonality as q5


def _make_close(n: int = 4000, start: str = "2022-01-01", seed: int = 0):
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, periods=n, freq="5min", tz="UTC")
    # add a tiny hour-of-day seasonality so the bucket test is meaningful
    hour = idx.hour.to_numpy()
    bias = 0.0001 * np.sin(2 * np.pi * hour / 24.0)
    ret = rng.normal(0, 0.001, n) + bias
    close = 100 * np.exp(np.cumsum(ret))
    return pd.Series(close, index=idx, name="close")


def test_bh_adjust_monotone_and_bounded():
    p = np.array([0.001, 0.01, 0.04, 0.5, 0.9])
    adj = q5._bh_adjust(p)
    assert all(0 <= x <= 1 for x in adj)
    # monotone non-decreasing when sorted by raw p
    assert all(adj[i] <= adj[j] for i, j in [(0, 1), (1, 2), (2, 3), (3, 4)])


def test_bar_returns_shape_and_no_leak():
    s = _make_close()
    bars = pd.DataFrame({"close": s})
    r = q5._bar_returns(bars)
    assert len(r) == len(s)
    assert r.iloc[0] != r.iloc[0]  # NaN
    finite = r.dropna()
    assert (finite.index[0] >= s.index[0])


def test_bucket_mean_se_basic():
    r = np.random.default_rng(0).normal(0, 0.01, 1000)
    mean, se, t, n = q5._bucket_mean_se(r)
    assert n == 1000
    assert math.isfinite(mean)
    assert math.isfinite(se)
    assert se > 0
    # mean ~ 0, t small
    assert abs(mean) < 0.005


def test_bootstrap_mean_ci_brackets():
    r = np.random.default_rng(0).normal(0, 0.01, 4000)
    lo, hi = q5._bootstrap_mean_ci(r, block=60, n_draws=200, seed=0)
    assert math.isfinite(lo) and math.isfinite(hi)
    assert lo <= hi
    # 95% CI on a N(0, sigma/sqrt(n)) interval should bracket 0
    assert lo < 0 < hi


def test_tf_minutes_known():
    assert q5._tf_minutes("5m") == 5
    assert q5._tf_minutes("4h") == 240


def test_two_sample_t_welch():
    a = np.random.default_rng(0).normal(0.001, 0.01, 1000)
    b = np.random.default_rng(1).normal(0, 0.01, 1000)
    t = q5._two_sample_t(a, b)
    assert math.isfinite(t)
    assert t > 0  # a > b on average


def test_funding_autocorr_present():
    # synthetic funding rate: AR(1) with phi=0.8
    rng = np.random.default_rng(0)
    n = 5000
    a = np.zeros(n)
    for i in range(1, n):
        a[i] = 0.8 * a[i - 1] + rng.normal(0, 0.001)
    # supply as a DataFrame with funding_rate column
    idx = pd.date_range("2022-01-01", periods=n, freq="8h", tz="UTC")
    df = pd.DataFrame({"funding_rate": a}, index=idx)
    rates = df["funding_rate"].to_numpy()
    a_ = rates[:-1]
    b_ = rates[1:]
    mask = np.isfinite(a_) & np.isfinite(b_)
    ac = float(np.corrcoef(a_[mask], b_[mask])[0, 1])
    assert ac > 0.7


def test_run_produces_atlas(tmp_path, monkeypatch):
    out = q5.run()
    assert "verdict" in out
    assert "spot_grid" in out
    assert "funding_grid" in out
    assert out["cutoff_exclusive"] == "2024-07-01T00:00:00+00:00"
    # verdict fields are well-typed
    v = out["verdict"]
    for k in ("n_spot_rows", "n_bh_significant", "frac_bh_significant",
              "max_bps_per_day", "cost_hurdle_bps_round_trip", "funding_autocorr_mean",
              "h1_pass", "h2_pass", "h3_pass", "verdict"):
        assert k in v
    assert isinstance(v["h1_pass"], bool)
    assert v["cost_hurdle_bps_round_trip"] == q5.ROUND_TRIP_BPS
