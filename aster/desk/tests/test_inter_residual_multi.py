"""Reference tests for the multi-factor residual extension."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research.inter_residual_multi import factor_residuals_k


def test_factor_residuals_k2_extracts_two_factors():
    rng = np.random.default_rng(0)
    n_days = 600
    f1 = rng.standard_normal(n_days)
    f2 = rng.standard_normal(n_days)
    noise = {f"A{i}": 0.3 * rng.standard_normal(n_days) for i in range(8)}
    btc_like = 0.7 * f1 + 0.5 * noise["A0"]
    eth_like = 0.6 * f1 + 0.4 * f2 + 0.3 * noise["A1"]
    b2 = 0.3 * f1 + 0.6 * f2 + 0.5 * noise["A2"]
    b3 = 0.4 * f1 + 0.5 * f2 + 0.5 * noise["A3"]
    b4 = 0.3 * f1 + 0.6 * f2 + 0.5 * noise["A4"]
    b5 = 0.4 * f1 + 0.4 * f2 + 0.4 * noise["A5"]
    b6 = 0.3 * f1 + 0.5 * f2 + 0.4 * noise["A6"]
    bnb = 0.2 * f1 + 0.7 * f2 + 0.5 * noise["A7"]
    df = pd.DataFrame({
        "BTCUSDT": btc_like, "ETHUSDT": eth_like, "BNBUSDT": bnb,
        "B2USDT": b2, "B3USDT": b3, "B4USDT": b4, "B5USDT": b5, "B6USDT": b6,
    })
    loadings, scores, residuals = factor_residuals_k(df, k=2)
    assert loadings.shape == (8, 2)
    # F1 should load positively on BTCUSDT (sign alignment)
    assert loadings.loc["BTCUSDT", "F1"] > 0
    # F2 should load positively on ETHUSDT
    assert loadings.loc["ETHUSDT", "F2"] > 0
    # Residuals should have lower cross-correlation than the standardized returns
    orig_corr = df.corr().abs().values
    res_corr = residuals.corr().abs().values
    off_diag_orig = orig_corr[~np.eye(8, dtype=bool)].mean()
    off_diag_res = res_corr[~np.eye(8, dtype=bool)].mean()
    assert off_diag_res < off_diag_orig


def test_factor_residuals_k3_adds_third_factor():
    rng = np.random.default_rng(0)
    n_days = 800
    f1 = rng.standard_normal(n_days)
    f2 = rng.standard_normal(n_days)
    f3 = rng.standard_normal(n_days)
    df = pd.DataFrame({
        "BTCUSDT": 0.7 * f1 + 0.1 * f2 + 0.1 * f3,
        "ETHUSDT": 0.6 * f1 + 0.4 * f2 + 0.1 * f3,
        "BNBUSDT": 0.4 * f1 + 0.3 * f2 + 0.5 * f3,
        "XRPUSDT": 0.3 * f1 + 0.4 * f2 + 0.5 * f3,
        "SOLUSDT": 0.4 * f1 + 0.3 * f2 + 0.4 * f3,
        "LINKUSDT": 0.5 * f1 + 0.3 * f2 + 0.3 * f3,
        "DOGEUSDT": 0.3 * f1 + 0.5 * f2 + 0.4 * f3,
        "XMRUSDT": 0.4 * f1 + 0.4 * f2 + 0.4 * f3,
    })
    loadings, _scores, residuals = factor_residuals_k(df, k=3)
    assert loadings.shape == (8, 3)
    assert loadings.loc["BTCUSDT", "F1"] > 0
    assert loadings.loc["ETHUSDT", "F2"] > 0
    assert loadings.loc["BNBUSDT", "F3"] > 0
    # Three factors should reduce residual correlation further than two
    loadings2, _, residuals2 = factor_residuals_k(df, k=2)
    off3 = residuals.corr().abs().values[~np.eye(8, dtype=bool)].mean()
    off2 = residuals2.corr().abs().values[~np.eye(8, dtype=bool)].mean()
    assert off3 < off2


def test_factor_residuals_k2_handles_short_panel():
    """When T is only slightly above N, MP bound is large and only the top
    K eigenvalues are kept.  Sanity: the function returns and residuals
    have shape (T, N)."""
    rng = np.random.default_rng(0)
    n_days = 100
    f1 = rng.standard_normal(n_days)
    f2 = rng.standard_normal(n_days)
    df = pd.DataFrame({sym: f1 + 0.3 * f2 + 0.5 * rng.standard_normal(n_days)
                       for sym in ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT", "XMRUSDT"]})
    loadings, scores, residuals = factor_residuals_k(df, k=2)
    assert loadings.shape == (8, 2)
    assert residuals.shape == (n_days, 8)
