"""The only path from a target portfolio to a broker.

route():   stage check (ledger) -> risk gate -> journal -> broker -> journal
rebalance(): target weights -> orders (sells first) -> route() each
"""

from __future__ import annotations

from aster.execution import journal
from aster.ledger.db import Ledger
from aster.risk.gate import AccountState, Order, RiskLimits, check_order

PAPER_STAGES = {"paper", "paper_passed", "live_pilot", "live"}
LIVE_STAGES = {"live_pilot", "live"}


class StageError(PermissionError):
    pass


def check_stage(broker_mode: str, hypothesis_id: str, ledger: Ledger) -> None:
    status = ledger.get(hypothesis_id)["status"]
    allowed = LIVE_STAGES if broker_mode == "live" else PAPER_STAGES
    if status not in allowed:
        raise StageError(f"{hypothesis_id} is '{status}'; {broker_mode} trading needs one of {sorted(allowed)}")


def route(order: Order, broker, limits: RiskLimits, ledger: Ledger, acct: AccountState | None = None):
    if broker.mode == "live" and limits.mode != "live":
        raise StageError("risk_limits.mode is not 'live'")
    check_stage(broker.mode, order.hypothesis_id, ledger)
    acct = acct or broker.account_state([order.symbol])
    decision = check_order(order, acct, limits)
    journal.append("order_decision", {
        "mode": broker.mode, "order": order.__dict__, "approved": decision.approved,
        "reasons": decision.reasons, "tripped_kill": decision.tripped_kill,
        "equity": acct.equity, "positions": acct.positions,
    })
    if not decision.approved:
        return None
    try:
        fill = broker.submit(order)
    except Exception as exc:  # exchange errors are journaled, never swallowed silently
        journal.append("order_error", {"order": order.__dict__, "error": repr(exc)})
        raise
    journal.append("fill", {"mode": broker.mode, **fill.__dict__, "hypothesis_id": order.hypothesis_id})
    return fill


def rebalance(target: dict[str, float], broker, limits: RiskLimits, ledger: Ledger, hypothesis_id: str,
              strategy: str, version: str, min_trade_usd: float = 10.0, band: float = 0.02) -> list:
    """Move the account toward target weights (fraction of equity per symbol)."""
    symbols = sorted(set(target) | set(limits.allowed_symbols))
    acct = broker.account_state(symbols)
    base = min(acct.equity, limits.capital_cap_usd) if limits.mode == "live" else acct.equity
    orders = []
    for s in symbols:
        px = acct.prices.get(s)
        if not px:
            continue
        cur_q = acct.positions.get(s, 0.0)
        cur_w = cur_q * px / base if base else 0.0
        tgt_w = target.get(s, 0.0)
        if abs(tgt_w - cur_w) < band and tgt_w != 0:
            continue
        delta = tgt_w * base / px - cur_q
        if abs(delta * px) < min_trade_usd:
            continue
        orders.append(Order(s, "buy" if delta > 0 else "sell", abs(delta), px, hypothesis_id, strategy, version))
    orders.sort(key=lambda o: o.side != "sell")  # free cash before buying
    fills = []
    for o in orders:
        acct = broker.account_state(symbols)
        fills.append(route(o, broker, limits, ledger, acct))
    journal.append("rebalance", {"hypothesis_id": hypothesis_id, "target": target,
                                 "orders": len(orders), "filled": sum(f is not None for f in fills)})
    return fills
