import json

import pytest

from aster import paths
from aster.execution import journal
from aster.execution.brokers import PaperBroker
from aster.execution.router import StageError, rebalance, route
from aster.ledger.db import Ledger
from aster.risk.gate import AccountState, Order, RiskLimits, check_order, kill_active, trip_kill

LIM = RiskLimits(mode="paper", max_daily_loss_pct=3, max_drawdown_pct=15, max_gross_leverage=1.0,
                 max_net_leverage=1.0, max_position_pct=40, max_order_notional_usd=5000,
                 max_orders_per_day=10, allowed_symbols=("BTC/USDT", "ETH/USDT"))


def acct(**kw):
    base = dict(equity=10_000, start_of_day_equity=10_000, peak_equity=10_000,
                positions={}, prices={"BTC/USDT": 50_000.0, "ETH/USDT": 2_000.0})
    base.update(kw)
    return AccountState(**base)


def buy(qty=0.05, sym="BTC/USDT", px=50_000.0):
    return Order(sym, "buy", qty, px, "H-1")


def test_normal_order_passes():
    assert check_order(buy(), acct(), LIM).approved


def test_symbol_size_short_leverage_limits():
    assert not check_order(buy(sym="DOGE/USDT"), acct(), LIM).approved
    assert not check_order(buy(qty=0.2), acct(), LIM).approved                  # 10k notional > 5k
    assert not check_order(Order("BTC/USDT", "sell", 0.01, 50_000, "H-1"), acct(), LIM).approved  # short
    full = acct(positions={"BTC/USDT": 0.08, "ETH/USDT": 2.9})                  # 4k + 5.8k
    assert not check_order(buy(qty=0.01), full, LIM).approved                    # gross > 1.0


def test_price_sanity():
    assert not check_order(buy(px=60_000), acct(), LIM).approved                 # 2000 bps off market
    assert not check_order(buy(), acct(price_age_seconds={"BTC/USDT": 999}), LIM).approved


def test_drawdown_latches_kill_and_only_reductions_pass():
    a = acct(equity=8_000, peak_equity=10_000, start_of_day_equity=8_000, positions={"BTC/USDT": 0.05})
    d = check_order(buy(qty=0.01), a, LIM)
    assert not d.approved and d.tripped_kill and kill_active()
    reduce = Order("BTC/USDT", "sell", 0.05, 50_000, "H-1")
    assert check_order(reduce, a, LIM).approved
    # still latched after the account recovers
    assert not check_order(buy(), acct(), LIM).approved


def test_manual_kill():
    trip_kill("test")
    assert not check_order(buy(), acct(), LIM).approved


def test_nan_inputs_rejected():
    assert not check_order(buy(qty=float("nan")), acct(), LIM).approved


@pytest.fixture
def paper_hyp():
    L = Ledger()
    hid = L.register("t", "statement long enough", "mechanism long enough", "falsification long enough",
                     {"sharpe_ann_min": 1}, "fam", "crypto", "test")
    return L, hid


def feed(symbols):
    return {"BTC/USDT": 50_000.0, "ETH/USDT": 2_000.0}


def test_router_refuses_unpromoted_hypothesis(paper_hyp):
    L, hid = paper_hyp
    b = PaperBroker(feed, 10_000)
    with pytest.raises(StageError):
        route(Order("BTC/USDT", "buy", 0.01, 50_000, hid), b, LIM, L)


def test_rebalance_paper_end_to_end(paper_hyp):
    L, hid = paper_hyp
    with L._conn() as c:
        c.execute("UPDATE hypotheses SET status = 'paper' WHERE id = ?", (hid,))
    b = PaperBroker(feed, 10_000, fee_bps=10, slippage_bps=5)
    fills = rebalance({"BTC/USDT": 0.3, "ETH/USDT": 0.3}, b, LIM, L, hid, "tsmom", "1.0.0")
    assert all(f is not None for f in fills) and len(fills) == 2
    st = b.account_state(["BTC/USDT", "ETH/USDT"])
    assert st.positions["BTC/USDT"] == pytest.approx(0.06)
    assert st.equity < 10_000                     # fees + slippage paid
    # over-limit target: 60% in one coin > 40% cap -> rejected, journaled
    fills = rebalance({"BTC/USDT": 0.6}, b, LIM, L, hid, "tsmom", "1.0.0")
    decisions = [r for r in journal.read() if r["kind"] == "order_decision"]
    assert any(not r["payload"]["approved"] for r in decisions)
    assert journal.verify()["ok"]


def test_journal_tamper_detected():
    for i in range(3):
        journal.append("x", {"i": i})
    p = journal.journal_path()
    lines = p.read_text().splitlines()
    rec = json.loads(lines[1]); rec["payload"]["i"] = 99
    lines[1] = json.dumps(rec, sort_keys=True)
    p.write_text("\n".join(lines) + "\n")
    v = journal.verify()
    assert not v["ok"] and v["broken_at_line"] == 2


def test_limits_file_loads():
    lim = RiskLimits.load()
    assert lim.mode == "paper" and lim.allowed_symbols
    assert paths.kill_switch_path().parent.name == "state"
