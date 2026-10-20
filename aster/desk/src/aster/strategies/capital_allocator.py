"""Q19 — N7 synthesis and capital allocation.

Preregistered 2026-10-18, research/notes/2026-10-18-Q19-prereg.md.

The capital allocator takes a panel of (strategy, return_stream)
inputs and produces a portfolio weight vector. It is the N7
synthesis step: it does NOT generate new signals, it only chooses
how to weight the surviving F-strategies.

V1.0.0 supports three schemes:
- ``risk_parity``   (default): weight_i ∝ Sharpe_i / σ_i, capped
- ``min_variance``: weight_i ∝ 1/σ_i
- ``equal``:        weight_i = 1/N

The input return streams are passed as a dict
``{strategy_name: pd.Series}`` via the ``strategy_returns`` kwarg.
The output is a Series indexed by strategy_name, summing to 1.

This strategy is **descriptive** — it does not feed a live book.
The desk decides separately whether to promote any of the input
strategies to paper or live.
"""
from __future__ import annotations

from typing import Optional

import numpy as np
import pandas as pd

from aster.strategies.base import Strategy


class CapitalAllocator(Strategy):
    """Cross-strategy capital allocator for the Q19 synthesis."""

    name = "capital_allocator"
    version = "1.0.0"
    hypothesis = (
        "Risk-parity allocation across the desk's surviving "
        "F-strategies produces a smoother equity curve than "
        "equal-weight or Sharpe-weighted, because volatility "
        "balances risk contribution per dollar of capital."
    )
    default_params = {
        # The allocation scheme: risk_parity, min_variance, equal.
        "scheme": "risk_parity",
        # Cap on a single strategy's weight (0..1).
        "max_weight": 0.6,
        # Annualisation factor (daily).
        "annualisation": 365.0,
        # Min observations to estimate stats.
        "min_obs": 60,
    }

    def target_weights(self, prices: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """Compute the cross-strategy allocation.

        ``prices`` is the spot close panel of the underlyings
        traded (not used for the allocation; only the column
        names matter).

        ``strategy_returns`` (kwarg) is a dict
        ``{strategy_name: pd.Series}`` of return streams on the
        dev sample.

        Returns a wide weight frame (1 row × 2N columns) where
        the first N columns are the spot legs (always 0) and the
        next N columns are the strategy "perp leg" placeholders
        (the column name is the strategy name + ``:USDT`` suffix
        to follow the desk convention).
        """
        p = self.params
        sr: Optional[dict[str, pd.Series]] = kwargs.get("strategy_returns")
        if not sr:
            return pd.DataFrame(0.0, index=prices.index[:1],
                                columns=self._weight_columns(prices.columns))
        weights = self._allocate(sr, p)
        # Build a 1-row frame indexed by prices.index[0] (the
        # dev start). The columns are spot+perp for the underlyings;
        # the allocator is metadata for the desk, not a tradable
        # book.
        spot_cols = list(prices.columns)
        all_cols = [c for pair in zip(spot_cols,
                                      [f"{c}:USDT" for c in spot_cols])
                    for c in pair]
        w = pd.DataFrame(0.0, index=prices.index[:1], columns=all_cols)
        return w

    def allocate(self, strategy_returns: dict[str, pd.Series]) -> pd.Series:
        """Public API: returns the weight vector directly."""
        return self._allocate(strategy_returns, self.params)

    @staticmethod
    def _allocate(strategy_returns: dict[str, pd.Series],
                  p: dict) -> pd.Series:
        names = list(strategy_returns.keys())
        if not names:
            return pd.Series(dtype=float)
        if p["scheme"] == "equal":
            w = np.ones(len(names)) / len(names)
        else:
            stats = {}
            for name, sr in strategy_returns.items():
                sr = sr.dropna()
                if len(sr) < p["min_obs"]:
                    stats[name] = None
                    continue
                vol_ann = sr.std() * np.sqrt(p["annualisation"])
                sharpe = sr.mean() / sr.std() * np.sqrt(p["annualisation"]) \
                    if sr.std() > 0 else 0.0
                stats[name] = (vol_ann, sharpe)
            if p["scheme"] == "min_variance":
                w = np.array([
                    1.0 / stats[n][0] if stats[n] else 0.0
                    for n in names
                ])
            elif p["scheme"] == "risk_parity":
                w = np.array([
                    max(stats[n][1], 0.0) / stats[n][0]
                    if stats[n] and stats[n][0] > 0 else 0.0
                    for n in names
                ])
            else:
                raise ValueError(f"unknown scheme: {p['scheme']!r}")
            s = w.sum()
            if s > 0:
                w = w / s
            else:
                # All Sharpe <= 0: fall back to equal.
                w = np.ones(len(names)) / len(names)
        # Iterative cap: cap -> redistribute excess to under-cap,
        # repeat until all weights are within [0, max_weight] and
        # sum to 1. A single pass of cap-then-renormalise is not
        # enough because the renormalisation can re-push a
        # dominant weight above the cap.
        for _ in range(len(w) + 1):
            over = w > p["max_weight"]
            if not over.any():
                break
            w = np.where(over, p["max_weight"], w)
            under = ~over
            under_sum = w[under].sum()
            if under_sum > 0 and under.any():
                slack = (1.0 - w.sum())
                w[under] = w[under] + slack * (w[under] / under_sum)
            else:
                # All capped: scale down proportionally.
                w = w * (1.0 / w.sum())
                break
        s = w.sum()
        if s > 0:
            w = w / s
        return pd.Series(w, index=names)

    @staticmethod
    def _weight_columns(spot_cols: pd.Index) -> list[str]:
        return [c for pair in zip(spot_cols, [f"{c}:USDT" for c in spot_cols])
                for c in pair]
