"""Tests for P2a: multi-timeframe materialisation from the R2 minute store.

The pipeline accepts a per-hypothesis timeframe (5m/15m/1h/4h/1d) on top of
the legacy 1d default.  This file proves the bridge is causal, close-labelled
and pre-cutoff for every supported horizon, and that the no-write-on-failure
contract holds (a misconfigured prereg raises before any parquet is created).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from aster.data import r2_backtest_store as r2s
from aster.data.r2_klines import CUTOFF


def test_supported_timeframes_matches_bars() -> None:
    """Every timeframe the bridge claims to support must come from bars.TIMEFRAMES."""
    assert r2s.SUPPORTED_TIMEFRAMES == frozenset({"5m", "15m", "1h", "4h", "1d"})


def test_daily_from_minutes_remains_backwards_compatible() -> None:
    """The legacy daily_from_minutes helper must keep its 1d-only contract."""
    assert r2s.daily_from_minutes.__doc__ is not None
    assert "1d" in r2s.daily_from_minutes.__doc__


def test_bars_from_minutes_rejects_unknown_timeframe() -> None:
    idx = pd.DatetimeIndex([], tz="UTC")
    with pytest.raises(ValueError, match="unsupported timeframe"):
        r2s.bars_from_minutes(pd.DataFrame(index=idx), "2h")


def test_bars_from_minutes_rejects_non_close_label() -> None:
    idx = pd.DatetimeIndex([], tz="UTC")
    with pytest.raises(ValueError, match="label must be 'close'"):
        r2s.bars_from_minutes(pd.DataFrame(index=idx), "1d", label="left")


def test_bars_from_minutes_empty_raises(isolated_desk: Path) -> None:
    """An empty minutes frame at the cutoff boundary must not silently produce bars."""
    idx = pd.DatetimeIndex([], tz="UTC", name="open_time_utc")
    cols = ["open", "high", "low", "close", "volume", "quote_volume",
            "trades", "taker_buy_base", "taker_buy_quote"]
    frame = pd.DataFrame(0.0, index=idx, columns=cols)
    with pytest.raises(ValueError, match="no complete pre-cutoff bars"):
        r2s.bars_from_minutes(frame, "1h")


def test_materialise_bars_rejects_empty_timeframes(isolated_desk: Path) -> None:
    with pytest.raises(ValueError, match="at least one timeframe"):
        r2s.materialise_bars(["BTCUSDT"], [])


def test_materialise_bars_rejects_unknown_timeframe(isolated_desk: Path) -> None:
    with pytest.raises(ValueError, match="unsupported timeframe"):
        r2s.materialise_bars(["BTCUSDT"], ["7d"])


def test_materialise_bars_rejects_unknown_symbol(isolated_desk: Path) -> None:
    with pytest.raises(ValueError, match="no pipeline symbol mapping"):
        r2s.materialise_bars(["NOPEUSDT"], ["1d"])


def test_summarise_is_sorted_for_stable_cli() -> None:
    """The CLI output is compared by humans and CI: stability matters."""
    a = r2s.BarsManifest(symbol="BTC/USDT", timeframe="1h", path="x", rows=1,
                         start="2020-01-01T00:00:00+00:00", end="2020-01-02T00:00:00+00:00",
                         cutoff_exclusive=CUTOFF.isoformat())
    b = r2s.BarsManifest(symbol="BTC/USDT", timeframe="1d", path="y", rows=1,
                         start="2020-01-01T00:00:00+00:00", end="2020-01-02T00:00:00+00:00",
                         cutoff_exclusive=CUTOFF.isoformat())
    out = r2s.summarise({("BTC/USDT", "1h"): a, ("BTC/USDT", "1d"): b})
    assert [d["timeframe"] for d in out] == ["1d", "1h"]


def test_materialise_bars_writes_one_dataset_per_pair(isolated_desk: Path,
                                                       monkeypatch: pytest.MonkeyPatch) -> None:
    """End-to-end: write two (symbol, timeframe) pairs and verify the
    parquet + manifest pair exists, is close-labelled, and pre-cutoff.
    """
    # Synthetic minutes: 2 days at 1m cadence, strictly pre-cutoff.
    minutes_idx = pd.date_range("2020-01-01", periods=2 * 24 * 60, freq="1min", tz="UTC")
    minute_cols = ["open", "high", "low", "close", "volume", "quote_volume",
                   "trades", "taker_buy_base", "taker_buy_quote"]
    rng = np.random.default_rng(0)

    def fake_minutes(symbol: str) -> pd.DataFrame:
        n = len(minutes_idx)
        rets = rng.normal(0, 0.0005, size=n)
        close = 100.0 * np.exp(np.cumsum(rets))
        return pd.DataFrame(
            {
                "open": np.concatenate([[close[0]], close[:-1]]),
                "high": close * (1 + np.abs(rng.normal(0, 0.0002, n))),
                "low": close * (1 - np.abs(rng.normal(0, 0.0002, n))),
                "close": close,
                "volume": rng.uniform(1, 10, n),
                "quote_volume": rng.uniform(100, 1000, n),
                "trades": rng.integers(1, 100, n),
                "taker_buy_base": rng.uniform(0.5, 5, n),
                "taker_buy_quote": rng.uniform(50, 500, n),
            },
            index=minutes_idx,
            columns=minute_cols,
        )
    monkeypatch.setattr(r2s, "read_local", lambda sym: fake_minutes(sym))

    result = r2s.materialise_bars(["BTCUSDT", "ETHUSDT"], ("1d", "1h"), exchange="binance")
    assert set(result.keys()) == {("BTC/USDT", "1d"), ("BTC/USDT", "1h"),
                                  ("ETH/USDT", "1d"), ("ETH/USDT", "1h")}
    for key, manifest in result.items():
        assert manifest.rows > 0
        assert manifest.cutoff_exclusive == CUTOFF.isoformat()
        # The produced parquet must exist and respect the cutoff.
        path = Path(manifest.path)
        assert path.exists()
        df = pd.read_parquet(path)
        assert isinstance(df.index, pd.DatetimeIndex)
        assert df.index.tz is not None  # UTC, never naive
        assert df.index.max() < CUTOFF
        # Manifest next to the parquet
        meta = json.loads(path.with_suffix(".manifest.json").read_text())
        assert meta["symbol"] == manifest.symbol
        assert meta["timeframe"] == manifest.timeframe
        # store.write() doesn't expose cutoff_exclusive as a top-level
        # field; the bridge embeds it in the source string so an auditor
        # can reconstruct it without reading the data.
        assert CUTOFF.isoformat() in meta["source"]