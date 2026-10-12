"""Probability of Backtest Overfitting via CSCV (Bailey, Borwein, Lopez de Prado, Zhu 2016).

Input: a T x N matrix of per-bar returns, one column per configuration that
was tried. PBO is the share of IS/OOS splits where the in-sample winner ranks
in the bottom half out of sample. PBO > 0.5 means selection is worse than a coin.
"""

from __future__ import annotations

from itertools import combinations

import numpy as np
import pandas as pd


def _sharpe(block: np.ndarray) -> np.ndarray:
    sd = block.std(axis=0, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(sd > 0, block.mean(axis=0) / sd, 0.0)


def pbo_cscv(returns: pd.DataFrame, n_splits: int = 16) -> dict:
    if n_splits % 2:
        raise ValueError("n_splits must be even")
    m = returns.dropna().to_numpy()
    t, n = m.shape
    if n < 2:
        raise ValueError("need at least 2 configurations")
    usable = t - t % n_splits
    blocks = np.array_split(m[:usable], n_splits)
    logits = []
    for is_ids in combinations(range(n_splits), n_splits // 2):
        oos_ids = [i for i in range(n_splits) if i not in is_ids]
        is_sr = _sharpe(np.vstack([blocks[i] for i in is_ids]))
        oos_sr = _sharpe(np.vstack([blocks[i] for i in oos_ids]))
        best = int(np.argmax(is_sr))
        rank = (oos_sr < oos_sr[best]).sum() + 1           # 1 = worst ... n = best
        omega = rank / (n + 1)
        logits.append(np.log(omega / (1 - omega)))
    logits = np.array(logits)
    return {"pbo": float((logits <= 0).mean()), "n_combinations": len(logits),
            "logit_mean": float(logits.mean()), "n_configs": n}
