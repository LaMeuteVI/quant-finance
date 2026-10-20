"""Q7 lead-lag grid unit tests."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.q7_intraday_leadlag import (
    _bh_qvalues,
    _block_bootstrap_ci,
    _corr,
    _grid,
    _residualise,
)


def test_corr_and_bh_are_basic_and_monotone():
    x = np.arange(100, dtype=float)
    assert _corr(x, x) > 0.99
    q = _bh_qvalues(np.array([0.001, 0.01, 0.5, np.nan]))
    assert q[0] <= q[1] <= q[2]
    assert np.isnan(q[3])


def test_block_bootstrap_causal_lead_has_positive_ci():
    rng = np.random.default_rng(7)
    leader = rng.normal(size=5000)
    follower = np.roll(leader, 1) + 0.2 * rng.normal(size=5000)
    # follower[t+1] is caused by leader[t]; align the directed pair.
    lo, hi = _block_bootstrap_ci(leader[:-1], follower[1:], seed=1)
    assert lo > 0
    assert hi > lo


def test_residualise_removes_controls():
    rng = np.random.default_rng(2)
    btc = rng.normal(size=1000)
    eth = rng.normal(size=1000)
    alt = 2 * btc - 0.5 * eth + 0.1 * rng.normal(size=1000)
    panel = pd.DataFrame({"BTC/USDT": btc, "ETH/USDT": eth, "SOL/USDT": alt})
    residual = _residualise(panel)
    assert abs(np.corrcoef(residual["SOL/USDT"], btc)[0, 1]) < 0.1
    assert abs(np.corrcoef(residual["SOL/USDT"], eth)[0, 1]) < 0.1


def test_grid_contains_both_directions_and_lags():
    rng = np.random.default_rng(3)
    leader = rng.normal(size=1000)
    follower = np.roll(leader, 1) + rng.normal(scale=0.5, size=1000)
    panel = pd.DataFrame({"BTC/USDT": leader, "SOL/USDT": follower})
    grid = _grid(panel, timeframe="5m", residual=False)
    assert set(grid["leader"]) == {"BTC/USDT", "SOL/USDT"}
    assert set(grid["lag_bars"]) == {1, 2, 5, 15}
    cell = grid.query("leader == 'BTC/USDT' and follower == 'SOL/USDT' and lag_bars == 1").iloc[0]
    assert cell["corr"] > 0.5
