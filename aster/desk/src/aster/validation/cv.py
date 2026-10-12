"""Leakage-free cross-validation for financial labels (AFML ch. 7).

Labels span time: observation i is known only at t1[i]. Training rows whose
label window overlaps the test window are purged, and rows starting right
after the test window are embargoed (serial correlation leaks backwards).
"""

from __future__ import annotations

from collections.abc import Iterator

import numpy as np
import pandas as pd


class PurgedKFold:
    def __init__(self, n_splits: int, t1: pd.Series, embargo_pct: float = 0.01):
        if not t1.index.is_monotonic_increasing:
            raise ValueError("t1 must be indexed by label start time, sorted")
        self.n_splits, self.t1, self.embargo_pct = n_splits, t1, embargo_pct

    def split(self) -> Iterator[tuple[np.ndarray, np.ndarray]]:
        n = len(self.t1)
        starts = self.t1.index
        ends = self.t1.to_numpy()
        embargo = int(n * self.embargo_pct)
        for test in np.array_split(np.arange(n), self.n_splits):
            t0, t_end = starts[test[0]], ends[test].max()
            overlap = (starts <= t_end) & (ends >= t0)
            last = test[-1]
            embargoed = np.zeros(n, dtype=bool)
            embargoed[last + 1: min(n, last + 1 + embargo)] = True
            train = np.where(~overlap & ~embargoed)[0]
            train = np.setdiff1d(train, test)
            yield train, test


def walk_forward(index: pd.DatetimeIndex, train_bars: int, test_bars: int, step: int | None = None,
                 embargo_bars: int = 0, expanding: bool = False) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    """Rolling (or expanding) train window, followed by an embargo, then a test window."""
    step = step or test_bars
    n = len(index)
    start = 0
    while True:
        tr_end = start + train_bars
        te_start = tr_end + embargo_bars
        te_end = te_start + test_bars
        if te_end > n:
            break
        tr_start = 0 if expanding else start
        yield np.arange(tr_start, tr_end), np.arange(te_start, te_end)
        start += step


def sealed_split(index: pd.DatetimeIndex, holdout_frac: float = 0.25) -> pd.Timestamp:
    """Timestamp where the sealed holdout begins. Everything from it onwards is untouchable
    during research; it is read exactly once per hypothesis (enforced by the ledger)."""
    if not 0 < holdout_frac < 1:
        raise ValueError("holdout_frac must be in (0, 1)")
    return index[int(len(index) * (1 - holdout_frac))]
