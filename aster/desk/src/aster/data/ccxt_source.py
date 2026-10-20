"""Exchange data via ccxt: paginated OHLCV and perp funding history.

The bar that is still forming is always dropped: using it in a backtest or a
live signal is look-ahead (its close is not known yet).
"""

from __future__ import annotations

import time
from datetime import datetime, timezone

import pandas as pd

TIMEFRAME_MS = {
    "1m": 60_000, "5m": 300_000, "15m": 900_000, "1h": 3_600_000,
    "4h": 14_400_000, "1d": 86_400_000, "1w": 604_800_000,
}


def make_exchange(exchange_id: str, sandbox: bool = False, api_key: str | None = None, secret: str | None = None):
    import ccxt

    cls = getattr(ccxt, exchange_id)
    params = {"enableRateLimit": True}
    if api_key:
        params.update({"apiKey": api_key, "secret": secret})
    ex = cls(params)
    if sandbox:
        ex.set_sandbox_mode(True)
    return ex


def _to_ms(since: str | int | None) -> int | None:
    if since is None or isinstance(since, int):
        return since
    return int(pd.Timestamp(since, tz="UTC").timestamp() * 1000)


def fetch_ohlcv(exchange, symbol: str, timeframe: str = "1d", since: str | int | None = None,
                limit: int = 1000, now_ms: int | None = None) -> pd.DataFrame:
    tf_ms = TIMEFRAME_MS[timeframe]
    cursor = _to_ms(since)
    rows: list[list] = []
    while True:
        batch = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=cursor, limit=limit)
        if not batch:
            break
        rows.extend(batch)
        nxt = batch[-1][0] + tf_ms
        if cursor is not None and nxt <= cursor:
            break
        cursor = nxt
        if len(batch) < limit:
            break
        time.sleep(exchange.rateLimit / 1000)
    df = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume"])
    df = df.drop_duplicates("ts").sort_values("ts")
    now_ms = now_ms if now_ms is not None else int(datetime.now(timezone.utc).timestamp() * 1000)
    df = df[df["ts"] + tf_ms <= now_ms]  # drop the bar that has not closed yet
    df.index = pd.to_datetime(df.pop("ts"), unit="ms", utc=True)
    df.index.name = "ts"
    return df.astype(float)


def fetch_funding(exchange, symbol: str, since: str | int | None = None, limit: int = 1000) -> pd.DataFrame:
    cursor = _to_ms(since)
    rows: list[dict] = []
    while True:
        batch = exchange.fetch_funding_rate_history(symbol, since=cursor, limit=limit)
        if not batch:
            break
        rows.extend(batch)
        nxt = batch[-1]["timestamp"] + 1
        if cursor is not None and nxt <= cursor:
            break
        cursor = nxt
        if len(batch) < limit:
            break
        time.sleep(exchange.rateLimit / 1000)
    df = pd.DataFrame([{"ts": r["timestamp"], "rate": r["fundingRate"]} for r in rows])
    if df.empty:
        return df
    df = df.drop_duplicates("ts").sort_values("ts")
    df.index = pd.to_datetime(df.pop("ts"), unit="ms", utc=True)
    df.index.name = "ts"
    return df.astype(float)
