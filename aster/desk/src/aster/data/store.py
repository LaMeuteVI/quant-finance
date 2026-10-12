"""Parquet store with a provenance manifest per dataset.

Layout: data/<kind>/<exchange>/<symbol>/<timeframe>.parquet + .manifest.json
Every write records source, fetch time, row count, span and a content hash,
so any backtest can cite exactly which bytes it ran on.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from aster import paths


def _slug(symbol: str) -> str:
    return symbol.replace("/", "-").replace(":", "_")


def dataset_path(kind: str, exchange: str, symbol: str, timeframe: str) -> Path:
    return paths.path("data", kind, exchange, _slug(symbol), f"{timeframe}.parquet")


def content_hash(df: pd.DataFrame) -> str:
    h = hashlib.sha256(pd.util.hash_pandas_object(df, index=True).values.tobytes())
    return h.hexdigest()


def write(df: pd.DataFrame, kind: str, exchange: str, symbol: str, timeframe: str, source: str) -> Path:
    if not isinstance(df.index, pd.DatetimeIndex) or df.index.tz is None:
        raise ValueError("index must be a tz-aware DatetimeIndex (UTC)")
    df = df.sort_index()
    df = df[~df.index.duplicated(keep="last")]
    p = dataset_path(kind, exchange, symbol, timeframe)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(p)
    manifest = {
        "kind": kind,
        "exchange": exchange,
        "symbol": symbol,
        "timeframe": timeframe,
        "source": source,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "rows": int(len(df)),
        "start": df.index[0].isoformat() if len(df) else None,
        "end": df.index[-1].isoformat() if len(df) else None,
        "sha256": content_hash(df),
    }
    p.with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=2))
    return p


def read(kind: str, exchange: str, symbol: str, timeframe: str) -> pd.DataFrame:
    p = dataset_path(kind, exchange, symbol, timeframe)
    if not p.exists():
        raise FileNotFoundError(f"no dataset at {p}; run `desk data fetch` first")
    return pd.read_parquet(p)


def manifest(kind: str, exchange: str, symbol: str, timeframe: str) -> dict:
    p = dataset_path(kind, exchange, symbol, timeframe).with_suffix(".manifest.json")
    return json.loads(p.read_text())


def load_closes(exchange: str, symbols: list[str], timeframe: str) -> pd.DataFrame:
    """Wide close-price panel (UTC index x symbols). Missing bars stay NaN:
    a coin that did not trade yet must not be forward-filled into existence."""
    cols = {s: read("ohlcv", exchange, s, timeframe)["close"] for s in symbols}
    return pd.DataFrame(cols).sort_index()


def load_funding(exchange: str, symbols: list[str], timeframe: str) -> pd.DataFrame | None:
    frames = {}
    for s in symbols:
        try:
            frames[s] = read("funding", exchange, s, timeframe)["rate"]
        except FileNotFoundError:
            continue
    return pd.DataFrame(frames).sort_index() if frames else None
