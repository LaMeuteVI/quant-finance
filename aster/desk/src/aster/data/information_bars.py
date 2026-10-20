"""Information bars from aggTrades.

Three of the four families from afml ch02 are implemented here:

* **Volume bars** — every bar contains a fixed amount of traded base volume.
  Threshold is per-symbol and per-day, computed as the median daily volume on
  the 30-day prior window. The algorithm emits a bar when cumulative volume
  reaches the threshold, then resets the cumulative.

* **Dollar bars** — same as volume bars but using quote volume (``price *
  quantity``). Quote volatility scales less than base volume, so dollar bars
  yield a more stationary sample than volume bars.

* **Taker-imbalance bars** — a bar closes when the running signed imbalance
  exceeds the running expected imbalance by a multiple ``E[b] + k * sqrt(E[b])``
  where ``E[b]`` is estimated from prior bars. afml ch02 §2.3.3. Threshold is
  per-symbol, recomputed daily from the 30-day prior window of bars.

Tick bars (4th family) are deliberately out of scope: they degenerate on
aggTrades (Binance already aggregates), and the research brief never mentions
them.

The builders are **causal**: every bar is computed from trades with
``transact_time <= bar_close_utc``. The threshold for bar ``t`` is computed on
the rolling window that ends strictly before ``bar_close_utc`` to avoid
look-ahead. Frozen / no-trade periods do not emit empty bars: bars are an
event-driven sample of *information arrival*, not a regular clock.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

import numpy as np
import pandas as pd

AggTradesFrame = pd.DataFrame  # columns: agg_trade_id, price, quantity, transact_time, is_buyer_maker


@dataclass(frozen=True)
class BarSpec:
    """Outcome of one information-bar build."""

    family: str           # "volume", "dollar", "taker_imbalance"
    symbol: str
    threshold: np.ndarray  # per-bar threshold; same length as the bar frame
    bars: pd.DataFrame     # bar_close_utc-indexed OHLCV+buy/sell/imbalance


def _signed_imbalance(trades: AggTradesFrame) -> np.ndarray:
    """+qty if is_buyer_maker == False (aggressive buy), -qty if True."""
    sign = np.where(trades["is_buyer_maker"].to_numpy(), -1.0, 1.0)
    return sign * trades["quantity"].to_numpy()


def _dollar(trades: AggTradesFrame) -> np.ndarray:
    return trades["price"].to_numpy() * trades["quantity"].to_numpy()


def _base_volume(trades: AggTradesFrame) -> np.ndarray:
    return trades["quantity"].to_numpy()


def _rolling_threshold(
    events_per_day: np.ndarray,
    *,
    lookback_days: int = 30,
    fallback: float,
) -> float:
    """Median of the last ``lookback_days`` per-day counts, fallback if empty."""
    if len(events_per_day) == 0:
        return fallback
    tail = events_per_day[-lookback_days:]
    tail = tail[tail > 0]
    if len(tail) == 0:
        return fallback
    return float(np.median(tail))


def _bar_frame_from_trade_groups(
    trades: AggTradesFrame,
    groups: np.ndarray,
    family: str,
    symbol: str,
    threshold: np.ndarray,
) -> pd.DataFrame:
    """Build the bar OHLCV+features frame from ``groups`` (bar id per trade).

    Vectorised: a single ``groupby`` over ``groups`` produces every per-bar
    aggregate (open/high/low/close OHLC, volume, quote volume, trade count,
    buy/sell qty). The previous per-bar loop was O(N * B); this is O(N).
    """
    if len(groups) == 0 or groups.max(initial=-1) < 0:
        return pd.DataFrame()

    times = trades["transact_time"].to_numpy()
    prices = trades["price"].to_numpy()
    qtys = trades["quantity"].to_numpy()
    is_maker = trades["is_buyer_maker"].to_numpy()
    signed = np.where(is_maker, -qtys, qtys)  # buy contribution (positive when aggressive buy)
    buy_qty_arr = np.where(is_maker, 0.0, qtys)  # qty bought aggressively
    sell_qty_arr = np.where(is_maker, qtys, 0.0)  # qty sold aggressively

    frame = pd.DataFrame({
        "groups": groups,
        "open": prices,
        "high": prices,
        "low": prices,
        "close": prices,
        "volume": qtys,
        "quote_volume": prices * qtys,
        "transact_time": times,
        "buy_qty": buy_qty_arr,
        "sell_qty": sell_qty_arr,
    })

    g = frame.groupby("groups", sort=True)
    bar = g.agg(
        open=("open", "first"),
        high=("high", "max"),
        low=("low", "min"),
        close=("close", "last"),
        volume=("volume", "sum"),
        quote_volume=("quote_volume", "sum"),
        trades=("volume", "size"),
        buy_qty=("buy_qty", "sum"),
        sell_qty=("sell_qty", "sum"),
        bar_close_ts=("transact_time", "last"),
    )
    bar.index.name = None

    # Drop empty bars (defensive: shouldn't happen, but keep the invariant).
    bar = bar.dropna(subset=["close"])
    bar = bar[bar["trades"] > 0]

    close_idx = pd.to_datetime(bar["bar_close_ts"].to_numpy(), unit="ms", utc=True).rename("bar_close_utc")
    bar = bar.drop(columns=["bar_close_ts"])
    bar.index = close_idx

    if family == "taker_imbalance":
        denom = bar["buy_qty"] + bar["sell_qty"]
        bar["imbalance"] = np.where(denom > 0, (bar["buy_qty"] - bar["sell_qty"]) / denom, np.nan)
        bar["signed_flow"] = bar["buy_qty"] - bar["sell_qty"]
    bar.attrs["family"] = family
    bar.attrs["symbol"] = symbol
    return bar


def _daily_median_threshold(
    *,
    traded: np.ndarray,
    times_ms: np.ndarray,
    bar_target: float,
    lookback_days: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Per-bar threshold: median daily volume on the prior ``lookback_days`` window.

    Returns ``(bar_threshold, daily_volume)`` arrays aligned with the bar
    position. ``bar_threshold[b]`` is the threshold to use when *forming* bar
    ``b+1``: it is computed from the prior window only, never from trades that
    contribute to bar ``b+1`` itself (no future information).
    """
    ts = pd.to_datetime(times_ms, unit="ms", utc=True)
    # Group by calendar UTC date. We iterate via to_pydatetime() to avoid the
    # fragile DatetimeIndex.date accessor (which is absent in some pandas
    # builds and misclassified by type checkers).
    py_times = ts.to_pydatetime()
    date_keys = np.array([pd.Timestamp(t).date() for t in py_times])
    daily_series = pd.Series(traded).groupby(date_keys).sum()
    daily_index = pd.DatetimeIndex(
        [pd.Timestamp(d).tz_localize("UTC") for d in daily_series.index],
        name="date",
    )
    daily = pd.Series(daily_series.to_numpy(), index=daily_index)
    threshold = pd.Series(index=daily_index, dtype="float64")
    for i, _d in enumerate(daily_index):
        prior = daily.iloc[max(0, i - lookback_days):i]
        prior_pos = prior[prior > 0]
        threshold.iloc[i] = float(prior_pos.median()) if len(prior_pos) else bar_target
    threshold = threshold.ffill().bfill()
    return daily.to_numpy(), threshold.to_numpy()


def build_volume_bars(
    trades: AggTradesFrame,
    symbol: str,
    *,
    lookback_days: int = 30,
    fallback_threshold_btc: float = 50.0,
    fallback_threshold_eth: float = 500.0,
) -> BarSpec:
    """Build volume bars (fixed BTC-equivalent volume per bar)."""
    if len(trades) == 0:
        empty = pd.DataFrame()
        return BarSpec(family="volume", symbol=symbol, threshold=np.array([]), bars=empty)

    fallback = fallback_threshold_btc if symbol.startswith("BTC") else fallback_threshold_eth
    base = _base_volume(trades)
    daily_volume, _ = _daily_median_threshold(
        traded=base,
        times_ms=trades["transact_time"].to_numpy(),
        bar_target=fallback,
        lookback_days=lookback_days,
    )

    # Compute a per-day threshold and convert to per-trade lookups.
    dates = pd.to_datetime(trades["transact_time"], unit="ms", utc=True).dt.date.to_numpy()
    daily_threshold = np.zeros(len(daily_volume))
    for i in range(len(daily_volume)):
        prior = daily_volume[max(0, i - lookback_days):i]
        prior = prior[prior > 0]
        daily_threshold[i] = float(np.median(prior)) if len(prior) else fallback
    date_to_thr = dict(zip(pd.to_datetime(pd.Series(daily_volume).index).date, daily_threshold))
    per_trade_thr = np.array([date_to_thr.get(d, fallback) for d in dates])

    # Form groups: each bar accumulates ``per_trade_thr`` of base volume.
    groups = np.zeros(len(trades), dtype="int64")
    cum = 0.0
    current = 0
    for i in range(len(trades)):
        if cum == 0.0:
            current_thr = per_trade_thr[i]
        cum += base[i]
        if cum >= current_thr and current_thr > 0:
            groups[i] = current
            current += 1
            cum = 0.0
        else:
            groups[i] = current

    n_bars = int(groups.max()) + 1 if len(groups) else 0
    bars = _bar_frame_from_trade_groups(trades, groups, "volume", symbol, per_trade_thr[:n_bars])
    return BarSpec(family="volume", symbol=symbol, threshold=per_trade_thr, bars=bars)


def build_dollar_bars(
    trades: AggTradesFrame,
    symbol: str,
    *,
    lookback_days: int = 30,
    fallback_threshold_usd: float = 1_000_000.0,
) -> BarSpec:
    """Build dollar bars (fixed USD notional per bar)."""
    if len(trades) == 0:
        empty = pd.DataFrame()
        return BarSpec(family="dollar", symbol=symbol, threshold=np.array([]), bars=empty)

    dollars = _dollar(trades)
    daily_dollars, _ = _daily_median_threshold(
        traded=dollars,
        times_ms=trades["transact_time"].to_numpy(),
        bar_target=fallback_threshold_usd,
        lookback_days=lookback_days,
    )

    daily_threshold = np.zeros(len(daily_dollars))
    for i in range(len(daily_dollars)):
        prior = daily_dollars[max(0, i - lookback_days):i]
        prior = prior[prior > 0]
        daily_threshold[i] = float(np.median(prior)) if len(prior) else fallback_threshold_usd
    dates = pd.to_datetime(trades["transact_time"], unit="ms", utc=True).dt.date.to_numpy()
    date_to_thr = dict(zip(pd.to_datetime(pd.Series(daily_dollars).index).date, daily_threshold))
    per_trade_thr = np.array([date_to_thr.get(d, fallback_threshold_usd) for d in dates])

    groups = np.zeros(len(trades), dtype="int64")
    cum = 0.0
    current = 0
    for i in range(len(trades)):
        if cum == 0.0:
            current_thr = per_trade_thr[i]
        cum += dollars[i]
        if cum >= current_thr and current_thr > 0:
            groups[i] = current
            current += 1
            cum = 0.0
        else:
            groups[i] = current

    n_bars = int(groups.max()) + 1 if len(groups) else 0
    bars = _bar_frame_from_trade_groups(trades, groups, "dollar", symbol, per_trade_thr[:n_bars])
    return BarSpec(family="dollar", symbol=symbol, threshold=per_trade_thr, bars=bars)


def build_taker_imbalance_bars(
    trades: AggTradesFrame,
    symbol: str,
    *,
    lookback_days: int = 30,
    expected_imbalance_k: float = 1.5,
    fallback_initial_threshold: float = 100.0,
) -> BarSpec:
    """Build taker-imbalance bars (afml ch02 §2.3.3).

    The threshold is the expected absolute imbalance on the prior window plus a
    multiple of its standard deviation: ``E[|b|] + k * std[|b|]``. Each bar
    closes when ``|cumulative_signed|`` exceeds the threshold.
    """
    if len(trades) == 0:
        empty = pd.DataFrame()
        return BarSpec(family="taker_imbalance", symbol=symbol, threshold=np.array([]), bars=empty)

    signed = _signed_imbalance(trades)
    cum_signed = np.cumsum(signed)
    abs_cum = np.abs(cum_signed)

    # Per-day absolute-imbalance series.
    dates = pd.to_datetime(trades["transact_time"], unit="ms", utc=True).dt.date.to_numpy()
    df_daily = pd.DataFrame({"abs": abs_cum, "date": dates})
    daily_abs = df_daily.groupby("date")["abs"].max().fillna(0.0)

    daily_threshold = np.zeros(len(daily_abs))
    for i in range(len(daily_abs)):
        prior = daily_abs.iloc[max(0, i - lookback_days):i].to_numpy()
        prior = prior[prior > 0]
        if len(prior) == 0:
            daily_threshold[i] = fallback_initial_threshold
        else:
            mu = float(np.mean(prior))
            sd = float(np.std(prior))
            daily_threshold[i] = mu + expected_imbalance_k * sd
    date_to_thr = dict(zip(daily_abs.index, daily_threshold))
    per_trade_thr = np.array([date_to_thr.get(d, fallback_initial_threshold) for d in dates])

    # Walk the trades and close a bar when |cum_signed| exceeds today's threshold.
    groups = np.zeros(len(trades), dtype="int64")
    cum = 0.0
    current = 0
    last_thr = fallback_initial_threshold
    for i in range(len(trades)):
        if cum == 0.0:
            last_thr = per_trade_thr[i]
        cum += signed[i]
        if abs(cum) >= last_thr and last_thr > 0:
            groups[i] = current
            current += 1
            cum = 0.0
        else:
            groups[i] = current

    n_bars = int(groups.max()) + 1 if len(groups) else 0
    bars = _bar_frame_from_trade_groups(trades, groups, "taker_imbalance", symbol, per_trade_thr[:n_bars])
    return BarSpec(family="taker_imbalance", symbol=symbol, threshold=per_trade_thr, bars=bars)


__all__ = [
    "BarSpec",
    "build_volume_bars",
    "build_dollar_bars",
    "build_taker_imbalance_bars",
]