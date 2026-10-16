import pytest

from aster.backtest import pipeline
from aster.ledger.db import Ledger, LedgerError

PRED: dict = {"sharpe_ann_min": 0.8, "max_drawdown_floor": -0.35}


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


def test_pipeline_counts_trials_and_holdout_is_single_use(prices, monkeypatch):
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
    # P3: the holdout is the sealed store, not the pre-cutoff index. The
    # sealed store is empty in the test fixture, so the first call raises
    # a ``FileNotFoundError`` from the sealed reader *after* the ledger
    # gate has been consumed. The second call therefore raises
    # ``LedgerError("holdout already read")`` — the single-use gate fires
    # before the missing partition is even looked at.
    with pytest.raises((FileNotFoundError, ValueError)):
        pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)
    with pytest.raises(LedgerError, match="holdout already read"):
        pipeline.run(hid, "tsmom", {}, sample="holdout", ledger=L, prices=prices)


def test_revision_budget():
    L = Ledger()
    hid = _new(L)
    for v in range(5):
        L.record_trial(hid, "tsmom", f"1.{v}.0", {}, "dev", {}, None, None, 1, False)
    with pytest.raises(LedgerError):
        L.check_revision_budget(hid, "1.9.0")
    L.check_revision_budget(hid, "1.4.0")  # an existing version is fine


# --------------------------------------------------------------------------- #
# P2 pipeline tests: prereg-driven timeframe + perp_legs                      #
# --------------------------------------------------------------------------- #


def test_pipeline_reads_timeframe_from_prereg(prices):
    """A prereg that pins a 1h timeframe must be accepted by the pipeline,
    and the resulting report must carry that horizon everywhere."""
    L = Ledger()
    pred = dict(PRED)
    pred["timeframe"] = "1d"  # legacy default; the desk's 1d is supported
    hid = L.register("TSMOM 1d prereg", "Same statement, but locked to 1d in the prereg.",
                     "Slow diffusion and flow herding create persistent trends.",
                     "Rejected if dev DSR < 0.95 or Sharpe < 0.8 after costs.",
                     pred, "trend", "crypto-spot", "test", strategy="tsmom")
    rep = pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)
    # base and every stress block record the timeframe
    assert rep["base"]["timeframe"] == "1d"
    for stress in rep["stress"].values():
        assert stress["timeframe"] == "1d"


def test_pipeline_rejects_unknown_timeframe_in_prereg(prices):
    L = Ledger()
    pred = dict(PRED)
    pred["timeframe"] = "7d"  # not in the bar bridge
    hid = L.register("Bogus 7d", "x" * 20, "y" * 20, "z" * 20, pred, "trend", "crypto-spot",
                     "test", strategy="tsmom")
    with pytest.raises(ValueError, match="not supported by the bar bridge"):
        pipeline.run(hid, "tsmom", {"lookback": 60}, ledger=L, prices=prices)
