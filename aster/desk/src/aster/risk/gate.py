"""Pre-trade risk gate and kill switch. Runs before EVERY order, in code.

A limit written in a prompt is a suggestion; this module is not. No order
reaches a broker unless check_order approves it (see execution.router).

Kill switch semantics:
  - the file desk/state/KILL exists  ->  only exposure-reducing orders pass;
  - a daily-loss or drawdown breach writes KILL automatically (it latches);
  - clearing it is a human action (`desk kill off`, interactive TTY).
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from aster import paths


@dataclass(frozen=True)
class RiskLimits:
    mode: str = "paper"
    capital_cap_usd: float = 1_000.0
    max_daily_loss_pct: float = 2.0
    max_drawdown_pct: float = 10.0
    max_gross_leverage: float = 1.0
    max_net_leverage: float = 1.0
    max_position_pct: float = 35.0
    max_order_notional_usd: float = 500.0
    max_orders_per_day: int = 50
    max_price_deviation_bps: float = 50.0
    stale_price_seconds: float = 180.0
    allow_shorts: bool = False
    allowed_symbols: tuple[str, ...] = ()

    @classmethod
    def load(cls, data: dict | None = None) -> "RiskLimits":
        data = data if data is not None else paths.load_config("risk_limits")
        known = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        if "allowed_symbols" in known:
            known["allowed_symbols"] = tuple(known["allowed_symbols"])
        lim = cls(**known)
        if lim.mode not in {"paper", "testnet", "live"}:
            raise ValueError(f"invalid mode {lim.mode}")
        return lim


@dataclass(frozen=True)
class Order:
    symbol: str
    side: str                 # "buy" | "sell"
    qty: float                # base units, > 0
    price_ref: float          # reference price used for sizing and checks
    hypothesis_id: str = ""
    strategy: str = ""
    strategy_version: str = ""
    order_type: str = "market"
    limit_price: float | None = None

    @property
    def signed_qty(self) -> float:
        return self.qty if self.side == "buy" else -self.qty

    @property
    def notional(self) -> float:
        return abs(self.qty * self.price_ref)


@dataclass
class AccountState:
    equity: float
    start_of_day_equity: float
    peak_equity: float
    positions: dict[str, float] = field(default_factory=dict)   # symbol -> base qty
    prices: dict[str, float] = field(default_factory=dict)      # symbol -> last price
    price_age_seconds: dict[str, float] = field(default_factory=dict)
    orders_today: int = 0


@dataclass(frozen=True)
class Decision:
    approved: bool
    reasons: tuple[str, ...]
    tripped_kill: bool = False


def kill_active(kill_path: Path | None = None) -> dict | None:
    p = kill_path or paths.kill_switch_path()
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text() or "{}")
    except json.JSONDecodeError:
        return {"reason": "unreadable kill file (treated as active)"}


def trip_kill(reason: str, kill_path: Path | None = None) -> None:
    p = kill_path or paths.kill_switch_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text(json.dumps({"reason": reason, "at": datetime.now(timezone.utc).isoformat()}))


def _reduces(old: float, new: float) -> bool:
    return abs(new) < abs(old) - 1e-12 and (new == 0 or math.copysign(1, new) == math.copysign(1, old))


def loss_metrics(acct: AccountState) -> tuple[float, float]:
    daily = (acct.start_of_day_equity - acct.equity) / acct.start_of_day_equity * 100 if acct.start_of_day_equity > 0 else 0.0
    dd = (acct.peak_equity - acct.equity) / acct.peak_equity * 100 if acct.peak_equity > 0 else 0.0
    return daily, dd


def check_order(order: Order, acct: AccountState, limits: RiskLimits, kill_path: Path | None = None) -> Decision:
    reasons: list[str] = []
    tripped = False

    values = (order.qty, order.price_ref, acct.equity)
    if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in values):
        return Decision(False, ("non-finite order or account values",))
    if order.side not in {"buy", "sell"} or order.qty <= 0 or order.price_ref <= 0:
        return Decision(False, ("malformed order",))
    if acct.equity <= 0:
        return Decision(False, ("non-positive equity",))

    old = acct.positions.get(order.symbol, 0.0)
    new = old + order.signed_qty
    reducing = _reduces(old, new)

    # Loss breakers latch the kill switch, then only reductions may pass.
    daily, dd = loss_metrics(acct)
    if daily >= limits.max_daily_loss_pct:
        trip_kill(f"daily loss {daily:.2f}% >= {limits.max_daily_loss_pct}%", kill_path)
        tripped = True
    if dd >= limits.max_drawdown_pct:
        trip_kill(f"drawdown {dd:.2f}% >= {limits.max_drawdown_pct}%", kill_path)
        tripped = True
    kill = kill_active(kill_path)
    if kill and not reducing:
        reasons.append(f"kill switch active: {kill.get('reason', '')}")

    if limits.allowed_symbols and order.symbol not in limits.allowed_symbols:
        reasons.append(f"{order.symbol} not in allowed_symbols")

    last = acct.prices.get(order.symbol)
    if last is None:
        reasons.append("no reference market price")
    else:
        dev = abs(order.price_ref / last - 1) * 1e4
        if dev > limits.max_price_deviation_bps:
            reasons.append(f"price_ref deviates {dev:.0f} bps from market")
    age = acct.price_age_seconds.get(order.symbol, 0.0)
    if age > limits.stale_price_seconds:
        reasons.append(f"stale price ({age:.0f}s)")

    if not reducing:
        if order.notional > limits.max_order_notional_usd:
            reasons.append(f"order notional {order.notional:.2f} > {limits.max_order_notional_usd}")
        if acct.orders_today >= limits.max_orders_per_day:
            reasons.append("max orders per day reached")
        if new < 0 and not limits.allow_shorts:
            reasons.append("shorts not allowed")

        base = min(acct.equity, limits.capital_cap_usd) if limits.mode == "live" else acct.equity
        px = dict(acct.prices)
        px[order.symbol] = order.price_ref
        post = dict(acct.positions)
        post[order.symbol] = new
        expo = {s: q * px.get(s, 0.0) for s, q in post.items()}
        pos_pct = abs(expo[order.symbol]) / base * 100
        gross = sum(abs(v) for v in expo.values()) / base
        net = abs(sum(expo.values())) / base
        if pos_pct > limits.max_position_pct:
            reasons.append(f"position {pos_pct:.1f}% of equity > {limits.max_position_pct}%")
        if gross > limits.max_gross_leverage + 1e-9:
            reasons.append(f"gross leverage {gross:.2f} > {limits.max_gross_leverage}")
        if net > limits.max_net_leverage + 1e-9:
            reasons.append(f"net leverage {net:.2f} > {limits.max_net_leverage}")

    return Decision(not reasons, tuple(reasons), tripped)
