import pytest

from aster.backtest import pipeline
from aster.ledger.db import Ledger, LedgerError

PRED = {"sharpe_ann_min": 0.8, "max_drawdown_floor": -0.35}


def _new(L, family="trend"):
    return L.register("TSMOM majors", "Trailing 60d return sign predicts next-day sign on majors.",
                      "Slow diffusion and flow herding create persistent trends.",
                      "Rejected if dev DSR < 0.95 or Sharpe < 0.8 after costs.", PRED, family, "crypto-spot",
                      "test", strategy="tsmom")


def test_prereg_is_immutable_and_verified():
    L = Ledger()
    hid = _new(L)
    assert L.get(hid)["status"] == "preregistered"
    assert L.verify_prereg(hid)
    with L._conn() as c:  # simulate tampering
        c.execute("UPDATE hypotheses SET prediction_json = '{\"sharpe_ann_min\": 0.1}' WHERE id = ?", (hid,))
    assert not L.verify_prereg(hid)


def test_vague_hypothesis_refused():
    with pytest.raises(LedgerError):
        Ledger().register("x", "short", "mechanism text here", "falsification text", {}, "f", "m", "s")


def test_illegal_and_unevidenced_transitions():
    L = Ledger()
    hid = _new(L)
    with pytest.raises(LedgerError):
        L.set_status(hid, "paper", "skip ahead")
    with pytest.raises(LedgerError):
        L.set_status(hid, "backtest_passed", "no evidence")


def test_live_needs_human():
    L = Ledger()
    hid = _new(L)
    with L._conn() as c:
        c.execute("UPDATE hypotheses SET status = 'paper_passed' WHERE id = ?", (hid,))
    with pytest.raises(LedgerError):
        L.set_status(hid, "live_pilot", "agent wants money")
    L.set_status(hid, "live_pilot", "approved", approved_by="Samuel")
    assert L.get(hid)["approved_by"] == "Samuel"


def test_pipeline_counts_trials_and_holdout_is_single_use(prices):
    L = Ledger()
    hid = _new(L)
    r1 = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)
    r2 = pipeline.run(hid, "tsmom", {"lookback": 30}, ledger=L, prices=prices)
    assert r2["statistics"]["n_trials_family"] == r1["statistics"]["n_trials_family"] + 1 == 2
    assert r1["statistics"]["lookahead"]["passed"]
    assert L.n_trials("trend") == 2
    # dev on pure noise must not pass; holdout locked until it does
    with pytest.raises(LedgerError):
        pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)
    with L._conn() as c:
        c.execute("UPDATE hypotheses SET status = 'backtest_passed' WHERE id = ?", (hid,))
    pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)
    with pytest.raises(LedgerError):
        pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)


def test_revision_budget():
    L = Ledger()
    hid = _new(L)
    for v in range(5):
        L.record_trial(hid, "tsmom", f"1.{v}.0", {}, "dev", {}, None, None, 1, False)
    with pytest.raises(LedgerError):
        L.check_revision_budget(hid, "1.9.0")
    L.check_revision_budget(hid, "1.4.0")  # an existing version is fine
