"""Bailey & Lopez de Prado backtest statistics (AFML ch. 14; skill lopez-de-prado-afml).

All Sharpe ratios here are PER PERIOD (not annualized), with skew and
NON-excess kurtosis of the same return series.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import norm

EULER_GAMMA = 0.5772156649015329


def _sr_var_term(sr: float, skew: float, kurt: float) -> float:
    v = 1 - skew * sr + (kurt - 1) / 4 * sr**2
    return max(v, 1e-12)


def probabilistic_sharpe(sr: float, n_obs: int, skew: float, kurt: float, sr_benchmark: float = 0.0) -> float:
    """P(true SR > sr_benchmark) given the observed SR and its non-normality."""
    if n_obs < 2:
        return float("nan")
    z = (sr - sr_benchmark) * np.sqrt(n_obs - 1) / np.sqrt(_sr_var_term(sr, skew, kurt))
    return float(norm.cdf(z))


def expected_max_sharpe(n_trials: int, sr_variance: float) -> float:
    """Expected maximum SR among n_trials independent zero-skill strategies."""
    if n_trials <= 1 or sr_variance <= 0:
        return 0.0
    a = (1 - EULER_GAMMA) * norm.ppf(1 - 1.0 / n_trials)
    b = EULER_GAMMA * norm.ppf(1 - 1.0 / (n_trials * np.e))
    return float(np.sqrt(sr_variance) * (a + b))


def deflated_sharpe(sr: float, n_obs: int, skew: float, kurt: float, n_trials: int, sr_variance: float) -> float:
    """PSR against the SR you would expect from the best of n_trials pure-noise attempts."""
    return probabilistic_sharpe(sr, n_obs, skew, kurt, expected_max_sharpe(n_trials, sr_variance))


def min_track_record_length(sr: float, skew: float, kurt: float, sr_benchmark: float = 0.0,
                            confidence: float = 0.95) -> float:
    """Bars needed before the observed SR beats sr_benchmark at `confidence`."""
    if sr <= sr_benchmark:
        return float("inf")
    z = norm.ppf(confidence)
    return float(1 + _sr_var_term(sr, skew, kurt) * (z / (sr - sr_benchmark)) ** 2)


def haircut_sharpe_bonferroni(sr_ann: float, years: float, n_trials: int) -> float:
    """Harvey-Liu style haircut: annualized SR implied by a Bonferroni-adjusted p-value."""
    if years <= 0 or n_trials < 1:
        return float("nan")
    t = sr_ann * np.sqrt(years)
    p = 2 * (1 - norm.cdf(abs(t)))
    p_adj = min(1.0, p * n_trials)
    t_adj = norm.ppf(1 - p_adj / 2) if p_adj < 1 else 0.0
    return float(np.sign(sr_ann) * t_adj / np.sqrt(years))
