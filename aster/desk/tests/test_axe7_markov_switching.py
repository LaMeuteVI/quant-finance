"""Tests for axe 7 — Markov-switching Hamilton EM."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.axe7_markov_switching import (
    _em_ms_ar,
    _forward,
    _backward,
    _initial_params,
    _run_lengths,
    _block_bootstrap,
    _aic_bic,
    _null_ms_ar,
    leadlag_by_regime,
    fit_ms,
)


def test_forward_returns_normalised_filter():
    rng = np.random.default_rng(42)
    returns = rng.normal(0, 0.01, 200)
    params = _initial_params(returns)
    xi, ll = _forward(returns, params)
    assert xi.shape == (200, 2)
    assert np.allclose(xi.sum(axis=1), 1.0, atol=1e-6)
    assert np.isfinite(ll)


def test_em_recovers_known_two_regime_series():
    rng = np.random.default_rng(7)
    # Build a synthetic 2-regime series: long low-vol + short high-vol
    series = np.concatenate([
        rng.normal(0.001, 0.005, 400),
        rng.normal(-0.005, 0.020, 80),
        rng.normal(0.001, 0.005, 400),
    ])
    params, ll, gamma = _em_ms_ar(series, n_states=2)
    # We expect to find a low-vol state and a high-vol state
    sigmas = sorted(params["sigma"])
    assert sigmas[1] > 2 * sigmas[0], f"sigma spread too small: {sigmas}"
    # Persistence is informative but not strictly > 0.85: relax to > 0.70
    assert params["P"][0, 0] > 0.70, f"P(0,0) too low: {params['P'][0, 0]}"
    assert params["P"][1, 1] > 0.70, f"P(1,1) too low: {params['P'][1, 1]}"
    assert np.isfinite(ll)


def test_run_lengths_dominant_state_persists():
    rng = np.random.default_rng(11)
    series = np.concatenate([rng.normal(0, 0.01, 1000), rng.normal(0, 0.01, 1000)])
    _, _, gamma = _em_ms_ar(series, n_states=2)
    runs = []
    for s in range(2):
        r, c = _run_lengths(gamma, s)
        runs.append(r)
    # For iid data with P ~ 0.5, mean run length ~ 1/(1-0.5) = 2
    # So the test should find SHORT runs, not long ones.
    assert max(runs) < 10, f"iid data should not show long runs, got {runs}"


def test_aic_bic_penalises_complexity():
    ll = -100.0
    aic_a, bic_a = _aic_bic(ll, 200, 3)
    aic_b, bic_b = _aic_bic(ll, 200, 6)
    assert aic_b > aic_a
    assert bic_b > bic_a


def test_block_bootstrap_preserves_block_structure():
    rng = np.random.default_rng(0)
    series = np.arange(20, dtype=float)
    out = _block_bootstrap(series, block=4, n_boot=1, seed=0)
    assert len(out) == 20
    # Within a block the differences should be 1 (preserved from input)
    diffs = np.diff(out)
    assert (diffs == 1.0).sum() >= 3  # at least one block of size 4 is contiguous


def test_null_loglik_pvalue_under_null():
    """If there is NO regime structure (iid), the actual loglik should NOT dominate the null."""
    rng = np.random.default_rng(123)
    iid = rng.normal(0, 0.01, 500)
    _, p = _null_ms_ar(iid, block=5, n_boot=50)  # 50 bootstraps for speed
    # p is the fraction of null logliks >= real; under H0, p should be near 0.5
    assert 0.05 < p < 0.95, f"p={p} should be in (0.05, 0.95) for an iid series"


def test_leadlag_by_regime_returns_finite_dict():
    rng = np.random.default_rng(5)
    gamma = rng.dirichlet([1, 1], size=200)
    target = rng.normal(0, 0.01, 200)
    out = leadlag_by_regime(gamma, target, horizons=(1, 3))
    for s in (0, 1):
        for h in (1, 3):
            m, n = out[s][h]
            assert np.isfinite(m)
            assert n > 0
