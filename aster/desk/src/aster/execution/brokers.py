"""Brokers. PaperBroker simulates fills locally; CcxtBroker talks to an exchange
(sandbox/testnet or live spot). Neither is ever called directly by strategy
code: orders go through execution.router, which runs the risk gate first.

Live arming needs all of: risk_limits.mode == "live", env ASTER_LIVE_ARMED=1,
and a hypothesis promoted by a human to live_pilot/live (checked in router).
API keys must be trade-only (withdrawals disabled) and IP-restricted.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from aster import paths
from aster.risk.gate import AccountState, Order


@dataclass
class Fill:
    symbol: str
    side: str
    qty: float
    price: float
    fee_usd: float
    exchange_order_id: str | None = None


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


class _DayBook:
    """Start-of-day equity, peak equity and order count, persisted on disk."""

    def __init__(self, p: Path):
        self.p = p
        self.d = json.loads(p.read_text()) if p.exists() else {}

    def update(self, equity: float) -> dict:
        d = self.d
        if d.get("day") != _today():
            d.update(day=_today(), sod_equity=equity, orders_today=0)
        d["peak_equity"] = max(d.get("peak_equity", equity), equity)
        self.save()
        return d

    def count_order(self) -> None:
        self.d["orders_today"] = self.d.get("orders_today", 0) + 1
        self.save()

    def save(self) -> None:
        self.p.parent.mkdir(parents=True, exist_ok=True)
        self.p.write_text(json.dumps(self.d, indent=2))


class PaperBroker:
    mode = "paper"

    def __init__(self, price_feed, initial_cash: float = 10_000.0, fee_bps: float = 10.0,
                 slippage_bps: float = 5.0, state_path: Path | None = None):
        self.price_feed = price_feed          # callable(symbols) -> {symbol: price}
        self.fee_bps, self.slippage_bps = fee_bps, slippage_bps
        self.p = state_path or paths.path("state", "paper_account.json")
        if self.p.exists():
            self.s = json.loads(self.p.read_text())
        else:
            self.s = {"cash": initial_cash, "positions": {}}
        self.book = _DayBook(self.p.with_name(self.p.stem + "_daybook.json"))

    def _save(self) -> None:
        self.p.parent.mkdir(parents=True, exist_ok=True)
        self.p.write_text(json.dumps(self.s, indent=2))

    def account_state(self, symbols: list[str]) -> AccountState:
        syms = sorted(set(symbols) | set(self.s["positions"]))
        prices = self.price_feed(syms) if syms else {}
        equity = self.s["cash"] + sum(q * prices[s] for s, q in self.s["positions"].items())
        d = self.book.update(equity)
        return AccountState(equity=equity, start_of_day_equity=d["sod_equity"], peak_equity=d["peak_equity"],
                            positions=dict(self.s["positions"]), prices=prices,
                            price_age_seconds={s: 0.0 for s in syms}, orders_today=d["orders_today"])

    def submit(self, order: Order) -> Fill:
        sign = 1 if order.side == "buy" else -1
        px = order.price_ref * (1 + sign * self.slippage_bps / 1e4)
        fee = abs(order.qty * px) * self.fee_bps / 1e4
        self.s["cash"] -= sign * order.qty * px + fee
        pos = self.s["positions"].get(order.symbol, 0.0) + sign * order.qty
        if abs(pos) < 1e-12:
            self.s["positions"].pop(order.symbol, None)
        else:
            self.s["positions"][order.symbol] = pos
        self._save()
        self.book.count_order()
        return Fill(order.symbol, order.side, order.qty, px, fee)


class CcxtBroker:
    """Spot account on a ccxt exchange. mode: 'testnet' (sandbox) or 'live'."""

    def __init__(self, exchange_id: str, mode: str, quote: str = "USDT"):
        if mode not in {"testnet", "live"}:
            raise ValueError("CcxtBroker mode must be testnet or live")
        if mode == "live" and os.environ.get("ASTER_LIVE_ARMED") != "1":
            raise PermissionError("live trading is not armed (export ASTER_LIVE_ARMED=1 in a human shell)")
        from aster.data.ccxt_source import make_exchange

        prefix = f"ASTER_{exchange_id.upper()}_{'TESTNET_' if mode == 'testnet' else ''}"
        key, secret = os.environ.get(prefix + "API_KEY"), os.environ.get(prefix + "API_SECRET")
        if not key or not secret:
            raise PermissionError(f"missing {prefix}API_KEY / {prefix}API_SECRET")
        self.mode, self.quote = mode, quote
        self.ex = make_exchange(exchange_id, sandbox=(mode == "testnet"), api_key=key, secret=secret)
        self.ex.load_markets()
        self.book = _DayBook(paths.path("state", f"{exchange_id}_{mode}_daybook.json"))

    def account_state(self, symbols: list[str]) -> AccountState:
        bal = self.ex.fetch_balance()["total"]
        tickers = self.ex.fetch_tickers(symbols) if symbols else {}
        now_ms = time.time() * 1000
        prices, ages, positions = {}, {}, {}
        for s in symbols:
            t = tickers.get(s) or {}
            px = t.get("last") or t.get("close")
            if px:
                prices[s] = float(px)
                ages[s] = (now_ms - (t.get("timestamp") or now_ms)) / 1000
            base = s.split("/")[0]
            if bal.get(base):
                positions[s] = float(bal[base])
        equity = float(bal.get(self.quote, 0.0)) + sum(q * prices.get(s, 0.0) for s, q in positions.items())
        d = self.book.update(equity)
        return AccountState(equity=equity, start_of_day_equity=d["sod_equity"], peak_equity=d["peak_equity"],
                            positions=positions, prices=prices, price_age_seconds=ages,
                            orders_today=d["orders_today"])

    def submit(self, order: Order) -> Fill:
        qty = float(self.ex.amount_to_precision(order.symbol, order.qty))
        if order.order_type == "limit" and order.limit_price:
            px = float(self.ex.price_to_precision(order.symbol, order.limit_price))
            o = self.ex.create_order(order.symbol, "limit", order.side, qty, px)
        else:
            o = self.ex.create_order(order.symbol, "market", order.side, qty)
        self.book.count_order()
        fee = (o.get("fee") or {}).get("cost") or 0.0
        return Fill(order.symbol, order.side, float(o.get("filled") or qty),
                    float(o.get("average") or o.get("price") or order.price_ref), float(fee), o.get("id"))


def public_price_feed(exchange_id: str):
    """Price feed for paper trading from an exchange's public tickers (no keys)."""
    from aster.data.ccxt_source import make_exchange

    ex = make_exchange(exchange_id)

    def feed(symbols: list[str]) -> dict[str, float]:
        t = ex.fetch_tickers(symbols)
        return {s: float(t[s]["last"]) for s in symbols if s in t and t[s].get("last")}

    return feed
