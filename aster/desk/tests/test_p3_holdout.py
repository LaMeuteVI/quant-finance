"""Tests for P3: the pipeline holdout is the sealed store, not a quantile of
the pre-cutoff index.  Every test in this file proves one part of the
contract; the existing test_ledger tests cover the persistence path.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import pytest

from aster import paths
from aster.backtest import pipeline
from aster.data import r2_klines
from aster.ledger.db import Ledger, LedgerError
from aster.data.r2_klines import CUTOFF, SYMBOLS

PRED: dict = {"sharpe_ann_min": 0.8, "max_drawdown_floor": -0.35}


def _new(L, family="trend"):
    return L.register("TSMOM majors", "Trailing 60d return sign predicts next-day sign on majors.",
                      "Slow diffusion and flow herding create persistent trends.",
                      "Rejected if dev DSR < 0.95 or Sharpe < 0.8 after costs.", PRED, family,
                      "crypto-spot", "test", strategy="tsmom")


def test_holdout_start_is_the_exploration_cutoff(prices):
    """The P3 pipeline hard-codes the holdout_start to 2024-07-01 UTC;
    no prereg may move it earlier.  A pre-P3 ledger row carrying a
    quantile-based holdout_start must be rejected, not silently honoured.
    """
    L = Ledger()
    hid = _new(L)
    # Force a pre-cutoff holdout_start that a legacy pipeline would have
    # accepted; the new code must refuse it.
    with L._conn() as c:
        c.execute("UPDATE hypotheses SET holdout_start = ? WHERE id = ?",
                  ("2023-12-31T00:00:00+00:00", hid))
    with pytest.raises(LedgerError, match="pre-P3 holdout_start"):
        pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)


def test_holdout_start_default_seals_the_cutoff(prices):
    """A prereg without a holdout_start gets the 2024-07-01 cutoff sealed,
    not a 25% quantile.  The ledger row must reflect that and the report
    must carry the same date in its holdout_start field.
    """
    L = Ledger()
    hid = _new(L)
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)
    sealed = L.get(hid)["holdout_start"]
    assert sealed == CUTOFF.isoformat()
    assert rep["holdout_start"] == CUTOFF.isoformat()


def test_dev_run_filters_out_post_cutoff_rows(prices):
    """The dev branch filters by ``prices.index < holdout_start`` (= the
    exploration cutoff).  A frame that crosses the cutoff is therefore
    silently truncated, not rejected; that is the right behaviour for the
    data layer the bridge writes.  This test pins the contract: a
    leaky input loses every post-cutoff row before the look-ahead
    detector and the engine see it.
    """
    L = Ledger()
    hid = _new(L)
    leaky = prices.copy()
    post_cutoff_idx = CUTOFF + pd.Timedelta(days=10)
    leaky.loc[post_cutoff_idx] = leaky.iloc[-1]
    leaky = leaky.sort_index()
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=leaky)
    period = rep.get("period")
    # The backtest period must be entirely before the cutoff.
    assert period is not None
    start, end = period
    assert pd.Timestamp(end) < CUTOFF, f"dev backtest crossed the cutoff: end={end}"


def test_holdout_sample_unreachable_when_sealed_store_empty(prices):
    """A holdout run on an empty sealed store must raise a clear error
    BEFORE the ledger gate is consumed.  The dev gate must also have
    passed; otherwise the standard LedgerError is raised.
    """
    L = Ledger()
    hid = _new(L)
    with pytest.raises(LedgerError):
        pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)
    with L._conn() as c:
        c.execute("UPDATE hypotheses SET status = 'backtest_passed' WHERE id = ?", (hid,))
    with pytest.raises(FileNotFoundError, match="no local sealed holdout store"):
        pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)


def test_holdout_path_refuses_to_use_legacy_25pct_quantile(prices):
    """A non-sealed prereg that supplies a pre-cutoff holdout_start must be
    rejected even if the dev branch is bypassed.  This is the
    back-compat guard that closes the audit-flagged leak.
    """
    L = Ledger()
    hid = _new(L)
    with L._conn() as c:
        # Pretend the prereg was sealed at the legacy 25% quantile.
        quantile = prices.index[int(len(prices) * 0.75)]
        c.execute("UPDATE hypotheses SET holdout_start = ? WHERE id = ?",
                  (quantile.isoformat(), hid))
    with pytest.raises(LedgerError, match="pre-P3 holdout_start"):
        pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)
    with L._conn() as c:
        c.execute("UPDATE hypotheses SET status = 'backtest_passed' WHERE id = ?", (hid,))
    with pytest.raises(LedgerError, match="pre-P3 holdout_start"):
        pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)