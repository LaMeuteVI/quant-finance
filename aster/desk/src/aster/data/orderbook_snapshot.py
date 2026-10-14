"""Public, current Binance order-book snapshots for operational spread checks.

This is explicitly *not* historical research: it is allowed by Samuel as a
post-cutoff operational validation of tick/spread plausibility.  It is never
mixed with pre-cutoff alpha exploration or a hypothesis holdout.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

SYMBOLS = ("BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT", "XRP/USDT", "DOGE/USDT")


def quote_spread_bps(bid: float, ask: float) -> float:
    """Top-of-book quoted spread in bps; rejects invalid books."""
    if bid <= 0 or ask <= 0 or ask < bid:
        raise ValueError("invalid best bid/ask")
    return (ask - bid) / ((ask + bid) / 2.0) * 1e4


def fetch_snapshots(symbols: tuple[str, ...] = SYMBOLS) -> pd.DataFrame:
    """Fetch public best bid/ask using ccxt; no authentication is constructed."""
    import ccxt

    exchange = ccxt.binance({"enableRateLimit": True})
    captured = datetime.now(timezone.utc).isoformat()
    rows: list[dict[str, object]] = []
    for symbol in symbols:
        book = exchange.fetch_order_book(symbol, limit=5)
        if not book["bids"] or not book["asks"]:
            raise ValueError(f"{symbol}: empty order book")
        bid, ask = float(book["bids"][0][0]), float(book["asks"][0][0])
        rows.append({
            "symbol": symbol,
            "captured_at_utc": captured,
            "bid": bid,
            "ask": ask,
            "quoted_spread_bps": quote_spread_bps(bid, ask),
            "source": "ccxt public binance fetch_order_book",
            "purpose": "operational_validation_not_holdout",
        })
    return pd.DataFrame(rows)


def main() -> int:
    output = Path("research/atlas/current-orderbook-snapshot.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    frame = fetch_snapshots()
    frame.to_csv(output, index=False)
    print(frame[["symbol", "bid", "ask", "quoted_spread_bps"]].to_string(index=False))
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
