"""P5 — Walk-forward and PBO by default (tests).

Contract:

* ``pipeline.run`` always emits a ``walk_forward`` block on the dev
  sample. The block has ``n_folds >= 4`` on a 3-year daily sample, the
  per-fold records carry Sharpe / drawdown / start / end / n_obs, and
  the stability summary has mean / std / worst / best.
* The walk-forward uses ``train_bars=252, test_bars=63,
  embargo_bars=5, expanding=True`` (one trading-week embargo, quarterly
  test window, expanding train).
* When ``params_grid`` is supplied, ``pipeline.run`` also emits a
  ``pbo_cscv`` block with ``n_configs`` >= 4 and ``pbo`` in [0, 1].
  When it is not supplied, ``pbo_cscv`` is an empty dict (the legacy
  single-config backtest path).
* The walk-forward contract is exercised on a deterministic synthetic
  price series; the PBO contract is exercised on a small tsmom grid
  with three ``lookback`` values.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.backtest import pipeline
from aster.ledger.db import Ledger, LedgerError

PRED: dict = {"sharpe_ann_min": 0.0, "max_drawdown_floor": -0.99}


def _new(L, family="trend", title="TSMOM P5"):
    return L.register(title,
                      "Trailing 60d return sign predicts next-day sign.",
                      "Slow diffusion and flow herding create persistent trends.",
                      "Rejected if dev DSR < 0.95 or Sharpe < 0.8 after costs.",
                      PRED, family, "crypto-spot", "test", strategy="tsmom")


def _make_prices(n_days: int = 1200, n_syms: int = 3, seed: int = 7) -> pd.DataFrame:
    """Deterministic 3-symbol daily price panel, n_days bars, tz-aware UTC."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2021-01-01", periods=n_days, freq="D", tz="UTC")
    cols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"][:n_syms]
    rets = rng.normal(0.0005, 0.02, size=(n_days, n_syms))
    prices = pd.DataFrame(100.0 * np.exp(np.cumsum(rets, axis=0)),
                          index=idx, columns=cols)
    return prices


def test_walk_forward_block_present_on_dev_run(prices):
    """Every dev pipeline.run emits a walk_forward block."""
    L = Ledger()
    hid = _new(L)
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)
    assert "walk_forward" in rep
    wf = rep["walk_forward"]
    assert wf["n_folds"] >= 4
    assert "stability" in wf and wf["stability"] is not None
    assert "worst_fold_sharpe_ann" in wf["stability"]
    assert wf["config"] == {"train_bars": 252, "test_bars": 63,
                            "embargo_bars": 5, "expanding": True}


def test_walk_forward_skipped_on_holdout(prices):
    """The walk-forward block is dev-only; the holdout run reports {}."""
    L = Ledger()
    hid = _new(L)
    # Force the dev gate to pass.
    with L._conn() as c:
        c.execute("UPDATE hypotheses SET status = 'backtest_passed' WHERE id = ?", (hid,))
    # The sealed store is empty; the call must raise FileNotFoundError
    # BEFORE building the report. The walk-forward block therefore
    # never gets a chance to fire. This test pins the order: a
    # holdout run with an empty sealed store must raise, not silently
    # return a report with an empty walk-forward block.
    with pytest.raises((FileNotFoundError, ValueError)):
        pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)


def test_walk_forward_too_short_returns_reason(prices):
    """A dev sample shorter than 252+5+63 = 320 bars must report a
    reason, not crash, and n_folds must be 0.
    """
    short = _make_prices(n_days=200)
    L = Ledger()
    hid = _new(L)
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=short)
    wf = rep["walk_forward"]
    assert wf["n_folds"] == 0
    assert "reason" in wf


def test_walk_forward_per_fold_record_shape(prices):
    """Each fold record has the documented keys."""
    L = Ledger()
    hid = _new(L)
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)
    for fold in rep["walk_forward"]["folds"]:
        assert set(fold.keys()) == {"start", "end", "n_obs", "sharpe_ann", "max_drawdown"}
        assert fold["n_obs"] > 0
        assert fold["max_drawdown"] <= 0.0


def test_pbo_block_empty_when_no_grid(prices):
    """Without params_grid the PBO block is an empty dict."""
    L = Ledger()
    hid = _new(L)
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)
    assert rep["pbo_cscv"] == {}


def test_pbo_block_populated_with_grid(prices):
    """With a params_grid the PBO block has n_configs and pbo in [0, 1]."""
    L = Ledger()
    hid = _new(L)
    grid = [{"lookback": lb} for lb in (20, 40, 60, 90, 120)]
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices,
                       params_grid=grid)
    pbo = rep["pbo_cscv"]
    assert pbo["n_configs"] == 5
    assert pbo["n_splits"] == 16
    assert 0.0 <= pbo["pbo"] <= 1.0
    assert "logit_mean" in pbo


def test_pbo_block_handles_too_few_configs(prices):
    """Fewer than 4 configs: PBO block has a reason and pbo=None."""
    L = Ledger()
    hid = _new(L)
    grid = [{"lookback": lb} for lb in (20, 40)]  # only 2
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices,
                       params_grid=grid)
    pbo = rep["pbo_cscv"]
    assert pbo["pbo"] is None
    assert "reason" in pbo


def test_pbo_block_skipped_on_holdout(prices):
    """PBO is dev-only."""
    L = Ledger()
    hid = _new(L)
    with L._conn() as c:
        c.execute("UPDATE hypotheses SET status = 'backtest_passed' WHERE id = ?", (hid,))
    grid = [{"lookback": lb} for lb in (20, 40, 60, 90, 120)]
    with pytest.raises((FileNotFoundError, ValueError)):
        pipeline.run(hid, "tsmom", {"lookback": 60}, sample="holdout",
                      ledger=L, prices=prices, params_grid=grid)
