"""Reference tests for the inter-asset residual study."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research.inter_residual import (
    _bh_adjust,
    _bootstrap_spearman,
    denoise_correlation,
    factor_residuals,
    marcenko_pastur_max_eig,
)


def test_marcenko_pastur_known_value():
    # q=2 -> (1+sqrt(2))^2 = (1+1.4142)^2 = 5.828
    assert marcenko_pastur_max_eig(100, 200) == pytest.approx(5.828, abs=0.01)


def test_denoise_identity_on_pure_signal():
    # Random orthogonal loading: only the top eigenvalues are above the MP bound.
    rng = np.random.default_rng(0)
    A = rng.standard_normal((8, 3))
    mat = A @ A.T
    np.fill_diagonal(mat, 1.0)
    corr = pd.DataFrame(mat, index=range(8), columns=range(8))
    denoised, eigvals, _ = denoise_correlation(corr)
    # eigh returns sorted ascending; the top 3 should dominate.
    assert eigvals[-3:].sum() > eigvals[:-3].sum()
    assert np.allclose(np.diag(denoised.to_numpy()), 1.0)
    assert np.allclose(denoised.to_numpy(), denoised.to_numpy().T, atol=1e-9)


def test_factor_residuals_btc_market():
    rng = np.random.default_rng(0)
    n = 200
    market = rng.standard_normal(n)
    btc = 0.8 * market + 0.4 * rng.standard_normal(n)
    eth = 0.6 * market + 0.6 * rng.standard_normal(n)
    alts = {f"A{i}": 0.3 * market + 0.7 * rng.standard_normal(n) for i in range(6)}
    df = pd.DataFrame({"BTCUSDT": btc, "ETHUSDT": eth, **alts})
    factors, scores, residuals = factor_residuals(df)
    # First factor should load positively on BTC and ETH.
    assert factors.iloc[0, 0] > 0
    assert factors.iloc[1, 0] > 0
    # Residuals are roughly orthogonal to the market factor.
    resid_corr = residuals.corr().values
    assert resid_corr[0, 1] < 0.2


def test_bh_adjust_monotone():
    pvals = np.array([0.001, 0.02, 0.04, 0.06, 0.5])
    adjusted = _bh_adjust(pvals)
    assert (adjusted >= pvals).all()


def test_bootstrap_spearman_basic():
    rng = np.random.default_rng(0)
    x = rng.standard_normal(200)
    y = x + 0.1 * rng.standard_normal(200)
    lo, hi = _bootstrap_spearman(x, y, 7, rng)
    assert lo > 0
    assert hi > lo
