"""Tests de référence pour le module intraday_term_structure."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.intraday_term_structure import (
    _bucket_autocorr,
    _bucket_vol_profile,
    _cross_bucket_corr,
    _log_return,
    summarise,
)


def _toy_returns(n: int = 600, seed: int = 0) -> pd.Series:
    rng = np.random.default_rng(seed)
    # autocorr lag1 cible ~ -0.3 : r_t = -0.3 * r_{t-1} + noise
    noise = rng.normal(0, 0.001, n)
    r = np.zeros(n)
    for i in range(1, n):
        r[i] = -0.3 * r[i - 1] + noise[i]
    index = pd.date_range("2024-01-01", periods=n, freq="1min", tz="UTC")
    return pd.Series(r, index=index)


def test_log_return_basic():
    s = pd.Series([100.0, 110.0, 121.0])
    out = _log_return(s)
    assert out.iloc[1] == pytest_approx(0.0953102)  # log(110/100)
    assert out.iloc[2] == pytest_approx(0.0953102)  # log(121/110)
    assert pd.isna(out.iloc[0])


def test_bucket_vol_profile_shape():
    r = _toy_returns(600)
    df = _bucket_vol_profile(r)
    # 1 day = 1 row per (weekday, hour). 600 minutes = 10h, donc max 10 lignes.
    assert "median_abs_ret" in df.columns
    assert df["minutes"].min() >= 1


def test_bucket_autocorr_negative():
    r = _toy_returns(600)
    df = _bucket_autocorr(r)
    # une seule journée de 600 minutes, donc potentiellement 1-3 buckets
    assert len(df) >= 1
    # autocorr lag1 doit être ~ -0.3 (cible du toy)
    vals = df["ac_lag1"].dropna()
    assert vals.mean() < 0  # négatif


def test_cross_bucket_corr_empty_for_toy():
    r = _toy_returns(600)
    df = _cross_bucket_corr(r)
    # 1 jour, donc 1 ligne par couple (src, dst) qui apparaît
    # 600 minutes = 10h, couvre asia (0-8) et eu (8-16), donc au moins (asia, eu) et (asia, us)
    if len(df):
        for col in ["corr", "corr_inverse"]:
            assert df[col].abs().max() <= 1.0001


def test_summarise_keys():
    r = _toy_returns(600)
    ac = _bucket_autocorr(r)
    cross = _cross_bucket_corr(r)
    payload = {
        "symbol": "TOY",
        "vol_profile": _bucket_vol_profile(r),
        "autocorr_per_bucket": ac,
        "cross_bucket_corr": cross,
        "autocorr_multiframe": pd.DataFrame(),
    }
    s = summarise(payload)
    assert s["symbol"] == "TOY"
    assert "ac_lag1_median" in s
    assert "n_days_autocorr" in s


def pytest_approx(x):
    import pytest

    return pytest.approx(x, rel=1e-6)
