"""Reference tests for the BTC N4/N5 descriptive study."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research.btc_n45 import _active_minute_returns, _block_indices, _bh_adjust


def _minutes(n: int = 240, start: str = "2024-06-03") -> pd.DataFrame:
    idx = pd.date_range(start, periods=n, freq="1min", tz="UTC")
    price = 100.0 + np.arange(n) * 0.01
    return pd.DataFrame(
        {
            "open": price,
            "high": price + 0.05,
            "low": price - 0.05,
            "close": price,
            "volume": np.full(n, 1.0),
            "quote_volume": np.full(n, 100.0),
            "trades": np.full(n, 5),
            "taker_buy_base": np.full(n, 0.5),
            "taker_buy_quote": np.full(n, 50.0),
        },
        index=idx,
    )


def test_active_minute_returns_drops_first_and_frozen():
    frame = _minutes(120)
    frame.iloc[10, frame.columns.get_loc("trades")] = 0
    out = _active_minute_returns(frame)
    # First row is dropped (diff against nothing); 117 of 118 active minutes remain.
    assert len(out) == 117
    assert out["log_return"].isna().sum() == 0


def test_block_indices_circular_within_length():
    rng = np.random.default_rng(0)
    indices = _block_indices(50, 5, rng)
    assert len(indices) == 50
    assert indices.max() < 50
    assert indices.min() >= 0


def test_bh_adjust_is_monotone_in_pvalues():
    pvals = np.array([0.001, 0.02, 0.04, 0.06, 0.5])
    adjusted = _bh_adjust(pvals)
    assert (adjusted >= pvals).all()
    assert adjusted[-1] == pytest.approx(0.5)
