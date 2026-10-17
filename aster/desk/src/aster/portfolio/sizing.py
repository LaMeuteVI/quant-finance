"""Position sizing. All functions are causal: row t uses data up to t only."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import squareform


def ewm_vol(returns: pd.DataFrame, halflife: int = 20, min_periods: int = 20) -> pd.DataFrame:
    return returns.ewm(halflife=halflife, min_periods=min_periods).std()


def vol_target(signal: pd.DataFrame, returns: pd.DataFrame, target_vol_ann: float, ppy: int,
               halflife: int = 20, max_gross: float = 1.0) -> pd.DataFrame:
    """Scale each asset's signal so it contributes target_vol / n_assets, then cap gross exposure.
    Ignores correlations on purpose (robust); portfolio vol is checked in the backtest."""
    vol = ewm_vol(returns, halflife) * np.sqrt(ppy)
    n_active = signal.ne(0).sum(axis=1).replace(0, np.nan)
    w = signal.div(vol).mul(target_vol_ann).div(n_active, axis=0)
    w = w.replace([np.inf, -np.inf], np.nan).fillna(0.0)
    gross = w.abs().sum(axis=1)
    scale = (max_gross / gross).clip(upper=1.0).fillna(1.0)
    return w.mul(scale, axis=0)


def fractional_kelly(mu: float, sigma: float, fraction: float = 0.25) -> float:
    """Kelly leverage mu/sigma^2, shrunk. Full Kelly on estimated inputs is reckless."""
    return 0.0 if sigma <= 0 else fraction * mu / sigma**2


def hrp_weights(returns: pd.DataFrame) -> pd.Series:
    """Hierarchical Risk Parity (Lopez de Prado 2016) on a returns window."""
    cov, corr = returns.cov(), returns.corr()
    dist = np.sqrt(((1 - corr.clip(-1, 1)) / 2).to_numpy())
    np.fill_diagonal(dist, 0.0)
    order = corr.index[leaves_list(linkage(squareform(dist, checks=False), "single"))].tolist()
    w = pd.Series(1.0, index=order)
    clusters = [order]
    while clusters:
        clusters = [c[i:j] for c in clusters for i, j in ((0, len(c) // 2), (len(c) // 2, len(c))) if len(c) > 1]
        for k in range(0, len(clusters), 2):
            left, right = clusters[k], clusters[k + 1]
            v = []
            for c in (left, right):
                sub = cov.loc[c, c]
                ivp = 1 / np.diag(sub)
                ivp /= ivp.sum()
                v.append(float(ivp @ sub.to_numpy() @ ivp))
            alpha = 1 - v[0] / (v[0] + v[1])
            w[left] *= alpha
            w[right] *= 1 - alpha
    return w.reindex(returns.columns)
