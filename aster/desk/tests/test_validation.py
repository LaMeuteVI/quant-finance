import numpy as np
import pandas as pd
import pytest

from aster.strategies.tsmom import TSMom
from aster.validation.cv import PurgedKFold, sealed_split, walk_forward
from aster.validation.lookahead import check_truncation_invariance
from aster.validation.pbo import pbo_cscv
from aster.validation.stats import (deflated_sharpe, expected_max_sharpe, min_track_record_length,
                                    probabilistic_sharpe)


def test_psr_basics():
    assert probabilistic_sharpe(0.0, 500, 0.0, 3.0) == pytest.approx(0.5)
    assert probabilistic_sharpe(0.1, 1000, 0.0, 3.0) > probabilistic_sharpe(0.1, 100, 0.0, 3.0)
    # negative skew and fat tails lower confidence
    assert probabilistic_sharpe(0.1, 500, -1.0, 8.0) < probabilistic_sharpe(0.1, 500, 0.0, 3.0)


def test_psr_reference_value():
    # z = 0.1 * sqrt(499) / sqrt(1 + 0.5*0.01) ; Phi(z)
    from scipy.stats import norm
    z = 0.1 * np.sqrt(499) / np.sqrt(1 + (3 - 1) / 4 * 0.01)
    assert probabilistic_sharpe(0.1, 500, 0.0, 3.0) == pytest.approx(norm.cdf(z))


def test_dsr_penalizes_many_trials():
    psr = probabilistic_sharpe(0.08, 1000, 0.0, 3.0)
    dsr = deflated_sharpe(0.08, 1000, 0.0, 3.0, n_trials=100, sr_variance=0.002)
    assert dsr < psr
    assert expected_max_sharpe(100, 0.002) > expected_max_sharpe(10, 0.002) > 0
    assert expected_max_sharpe(1, 0.002) == 0.0


def test_min_trl():
    assert min_track_record_length(0.0, 0, 3) == float("inf")
    assert min_track_record_length(0.2, 0, 3) < min_track_record_length(0.05, 0, 3)


def test_pbo_of_noise_is_near_half():
    rng = np.random.default_rng(1)
    m = pd.DataFrame(rng.normal(0, 0.01, size=(1600, 20)))
    res = pbo_cscv(m, n_splits=10)
    assert 0.25 < res["pbo"] < 0.75


def test_pbo_of_real_edge_is_low():
    rng = np.random.default_rng(2)
    m = pd.DataFrame(rng.normal(0, 0.01, size=(1600, 10)))
    m[0] += 0.004
    assert pbo_cscv(m, n_splits=10)["pbo"] < 0.1


def test_purged_kfold_has_no_overlap():
    idx = pd.date_range("2020-01-01", periods=300, freq="D", tz="UTC")
    t1 = pd.Series(idx + pd.Timedelta(days=5), index=idx)
    for train, test in PurgedKFold(5, t1, embargo_pct=0.02).split():
        t0, t_end = idx[test[0]], t1.iloc[test].max()
        tr_start, tr_end = idx[train], t1.iloc[train].to_numpy()
        assert not ((tr_start <= t_end) & (tr_end >= t0)).any()
        assert len(np.intersect1d(train, test)) == 0


def test_walk_forward_and_seal():
    idx = pd.date_range("2020-01-01", periods=100, freq="D", tz="UTC")
    splits = list(walk_forward(idx, 40, 10, embargo_bars=2))
    assert all(tr[-1] + 2 < te[0] for tr, te in splits)
    assert sealed_split(idx, 0.25) == idx[75]


def test_tsmom_is_causal(prices):
    assert check_truncation_invariance(TSMom().target_weights, prices)["passed"]


def test_lookahead_detector_catches_cheat(prices):
    def cheat(px):
        z = (px - px.mean()) / px.std()   # full-sample normalization = future leak
        return z.clip(-1, 1) / 5
    assert not check_truncation_invariance(cheat, prices)["passed"]
