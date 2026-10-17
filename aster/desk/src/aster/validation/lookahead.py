"""Generic look-ahead detector: truncation invariance.

A causal strategy's weight at bar t depends only on data up to t, so computing
it on prices[:t] or on the full history must give the same number. Any
difference means the strategy reads the future (centered windows, full-sample
normalization, shift(-1), bfill, global fitting...).
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
import pandas as pd


def check_truncation_invariance(weights_fn: Callable[[pd.DataFrame], pd.DataFrame], prices: pd.DataFrame,
                                n_checks: int = 8, min_history: int = 50, seed: int = 0,
                                atol: float = 1e-9) -> dict:
    full = weights_fn(prices)
    rng = np.random.default_rng(seed)
    lo = min(min_history, len(prices) - 2)
    cuts = sorted(set(rng.integers(lo, len(prices) - 1, size=n_checks).tolist()))
    violations = []
    for c in cuts:
        partial = weights_fn(prices.iloc[: c + 1])
        ts = prices.index[c]
        a = full.loc[ts].reindex(prices.columns).fillna(0.0).to_numpy(dtype=float)
        b = partial.loc[ts].reindex(prices.columns).fillna(0.0).to_numpy(dtype=float)
        if not np.allclose(a, b, atol=atol):
            violations.append({"ts": ts.isoformat(), "max_abs_diff": float(np.max(np.abs(a - b)))})
    return {"passed": not violations, "checked": len(cuts), "violations": violations}
