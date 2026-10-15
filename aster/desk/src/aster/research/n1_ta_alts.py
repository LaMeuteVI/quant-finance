"""N1 alt panel: descriptive formalised technical analysis on five secondary assets.

Scope: level **N1 only** (descriptive TA), on ``BNBUSDT``, ``XRPUSDT``,
``SOLUSDT``, ``LINKUSDT``, ``DOGEUSDT``.  Source is the local R2 Binance spot
1-minute kline store, aggregated to UTC daily bars, under the immutable
exploration cutoff (exclusive ``2024-07-01T00:00:00Z``).

The signal family is **fixed a priori** in
``research/2026-10-15-n1-alts-prereg.md``: 24 primary signals plus 8
placebo-level Fibonacci signals, each evaluated at 4 forward horizons, giving
128 cells per asset of which 96 are primary.  Nothing may be added, dropped or
re-selected after a p-value is seen; BH-FDR is applied to that fixed family,
both per asset and across the union of the five primary families.

This module registers no hypothesis, runs no backtest, reads no holdout and
touches neither the ledger nor any state file.  Pre-cutoff only.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.data import r2_klines
from aster.data.bars import build_bars, normalise_clock
from aster.data.r2_klines import CUTOFF

SYMBOLS = ("BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT")
HORIZONS = (1, 3, 7, 14)
BOOTSTRAPS = 5000
SEED = 20261015
MIN_EVENTS = 30
ASSET_DIR = Path("research/assets")

# --------------------------------------------------------------------------- #
# The fixed family (see research/2026-10-15-n1-alts-prereg.md)
# --------------------------------------------------------------------------- #

SIGNAL_LABELS: dict[str, str] = {
    # --- moving-average crossovers (4 primary) -------------------------------
    "ma_20_100_above": "close > SMA(20)",
    "ma_50_200_above": "close > SMA(50) and close > SMA(200)",
    "ma_10_30_above": "close > SMA(10) and close > SMA(30)",
    "ma_5_20_above": "close > SMA(5) and close > SMA(20)",
    # --- RSI(14) (2 primary) -------------------------------------------------
    "rsi14_oversold": "RSI(14) < 30",
    "rsi14_overbought": "RSI(14) > 70",
    # --- Bollinger(20, 2) (2 primary) ----------------------------------------
    "bb20_lower_break": "close < lower band (SMA20 - 2 sigma)",
    "bb20_upper_break": "close > upper band (SMA20 + 2 sigma)",
    # --- Donchian(20) (2 primary) --------------------------------------------
    "donchian20_breakout_up": "close > prior 20-day high",
    "donchian20_breakout_down": "close < prior 20-day low",
    # --- Stochastic %K(14) (4 primary) --------------------------------------
    "stoch14_oversold": "%K(14) < 20",
    "stoch14_overbought": "%K(14) > 80",
    "stoch14_cross_up": "%K(14) crosses above %D(3)",
    "stoch14_cross_down": "%K(14) crosses below %D(3)",
    # --- Weekly classic pivots (2 primary) ----------------------------------
    "pivot_s1_break": "close < S1 of the last completed week",
    "pivot_r1_break": "close > R1 of the last completed week",
    # --- Fibonacci retracements, 252d swing (6 primary) ---------------------
    "fib_382_below": "close < 0.382 retracement of the 252-day swing",
    "fib_382_above": "close > 0.382 retracement of the 252-day swing",
    "fib_500_below": "close < 0.500 retracement of the 252-day swing",
    "fib_500_above": "close > 0.500 retracement of the 252-day swing",
    "fib_618_below": "close < 0.618 retracement of the 252-day swing",
    "fib_618_above": "close > 0.618 retracement of the 252-day swing",
    # --- 3-bar fair value gaps (2 primary) ----------------------------------
    "fvg3_up_fill": "up-gap formed 3 bars ago (low > high[-2]) and close traded back into it",
    "fvg3_down_fill": "down-gap formed 3 bars ago (high < low[-2]) and close traded back into it",
    # --- placebo levels: same construction, non-standard ratios (8) ----------
    "fib_550_below": "PLACEBO LEVEL: close < 0.550 retracement of the 252-day swing",
    "fib_550_above": "PLACEBO LEVEL: close > 0.550 retracement of the 252-day swing",
    "fib_600_below": "PLACEBO LEVEL: close < 0.600 retracement of the 252-day swing",
    "fib_600_above": "PLACEBO LEVEL: close > 0.600 retracement of the 252-day swing",
    "fib_650_below": "PLACEBO LEVEL: close < 0.650 retracement of the 252-day swing",
    "fib_650_above": "PLACEBO LEVEL: close > 0.650 retracement of the 252-day swing",
    "fib_700_below": "PLACEBO LEVEL: close < 0.700 retracement of the 252-day swing",
    "fib_700_above": "PLACEBO LEVEL: close > 0.700 retracement of the 252-day swing",
}

#: Declared opposite-polarity pairs of the fixed family.  Their masks must never
#: overlap: a bar cannot be both an oversold and an overbought RSI event.
COMPLEMENT_PAIRS: tuple[tuple[str, str, str], ...] = (
    ("rsi14_oversold", "rsi14_overbought", "rsi14"),
    ("bb20_lower_break", "bb20_upper_break", "bb20_band"),
    ("donchian20_breakout_up", "donchian20_breakout_down", "donchian20"),
    ("stoch14_oversold", "stoch14_overbought", "stoch_k"),
    ("stoch14_cross_up", "stoch14_cross_down", "stoch_cross"),
    ("pivot_s1_break", "pivot_r1_break", "pivot_band"),
    ("fib_382_below", "fib_382_above", "fib_382"),
    ("fib_500_below", "fib_500_above", "fib_500"),
    ("fib_618_below", "fib_618_above", "fib_618"),
    ("fvg3_up_fill", "fvg3_down_fill", "fvg3"),
)

#: Ratios used by the primary family and by the placebo-level family.
FIB_RATIOS: dict[int, float] = {
    382: 0.382, 500: 0.5, 618: 0.618,
    550: 0.55, 600: 0.6, 650: 0.65, 700: 0.7,
}
PLACEBO_FIB_KEYS = (550, 600, 650, 700)

#: Placebo-level signals share the primary machinery but never count as evidence.
PLACEBO_LEVEL_SIGNALS: tuple[str, ...] = tuple(
    f"fib_{key}_{side}" for key in PLACEBO_FIB_KEYS for side in ("below", "above")
)

PRIMARY_SIGNALS: tuple[str, ...] = tuple(label for label in SIGNAL_LABELS if label not in PLACEBO_LEVEL_SIGNALS)

GRID_COLUMNS = tuple(column for column in (
    "symbol", "signal", "horizon", "kind", "n_events",
    "mean_fwd", "t_stat", "p_value", "ci_lo", "ci_hi",
    "inverse_n", "inverse_mean_fwd", "inverse_t_stat", "inverse_p_value",
    "placebo_shift_mean", "placebo_shift_t_stat", "placebo_shift_p_value",
    "placebo_timing_mean", "placebo_timing_p_value",
    "placebo_horizon_mean", "placebo_horizon_p_value",
    "bootstrap_excludes_zero", "inverse_does_not_dominate",
    "placebo_all_non_significant", "bh_q_asset", "retention",
))


# --------------------------------------------------------------------------- #
# Data
# --------------------------------------------------------------------------- #

# ``build_bars`` aggregates the full minute schema itself; the mapping below is
# kept only to document the contract the daily OHLCV must satisfy.
DAILY_AGGREGATIONS = {
    "open": ("open", "first"), "high": ("high", "max"),
    "low": ("low", "min"), "close": ("close", "last"),
    "volume": ("volume", "sum"), "quote_volume": ("quote_volume", "sum"),
    "trades": ("trades", "sum"),
}


def aggregate_daily(minutes: pd.DataFrame) -> pd.DataFrame:
    """Aggregate a UTC-indexed minute frame into **close-labelled** daily bars.

    **Convention.**  This delegates to :func:`aster.data.bars.build_bars` with
    ``label="close"``, the very primitive that produced ``data/ohlcv``, so the
    labelling rule of the N1 panel and of the pipeline store are the same rule.
    The bucket indexed ``t`` covers ``[t - 1d, t)``: the whole previous calendar
    day.  Measured on a synthetic frame, it contains the previous day's 00:00
    minute and excludes ``t``'s own 00:00 minute.

    **Repair, then sample.**  Order matters and is fixed here:

    1. ``normalise_clock`` repairs off-grid minute timestamps, exactly as
       ``aster.data.r2_backtest_store.daily_from_minutes`` does.  Repairing after
       the filter would leave the filter keyed on unrepaired stamps, so repair
       comes first.
    2. The BTC/ETH N1 protocol filter ``(trades > 0) & (close > 0)`` is applied to
       the repaired frame.  ``build_bars`` keeps frozen minutes by default, so
       without this filter a frozen or poisoned minute would move the daily OHLC
       and inflate the minute count.
    3. Only the admissible rows reach the builder *and* the minute count, so the
       two cannot disagree.

    Because of step 2 the panel is **not** byte-identical to the materialised
    ``data/ohlcv`` daily bars: that store is built from the unfiltered minutes.
    What is shared is the labelling convention and the underlying minute source.
    Each bar keeps a ``minutes`` column, so a day built from almost nothing shows
    a count far below 1440 instead of hiding inside a mean.

    Close labelling is what makes the panel causal: a feature computed at row
    ``t`` reads a bar whose close only became known at ``t``.  An open-labelled
    bar dated ``t`` would instead carry a close known at ``t + 1d``, i.e. one full
    day of look-ahead in every feature and every forward return.
    """
    index = pd.DatetimeIndex(minutes.index)
    if index.tz is None:
        raise ValueError("minute index must be timezone-aware")
    repaired, repair = normalise_clock(minutes)
    usable = repaired.loc[
        (repaired["trades"].astype(float) > 0) & (repaired["close"].astype(float) > 0)
    ]
    if usable.empty:
        raise ValueError("no admissible minute to aggregate")
    frame = pd.DataFrame(index=pd.DatetimeIndex(usable.index, name="open_time_utc"))
    frame = frame.join(usable)
    bars = build_bars(frame, "1d", label="close", drop_frozen=False)
    if bars.empty:
        raise ValueError("no daily bar survived the minute-level filters")
    # ``build_bars`` discards its internal per-minute counters after turning them
    # into ``frozen_share``, so the admissible count is recomputed from the very
    # same rows that produced the OHLC.
    usable_minutes = frame["close"].resample("1D", label="right", closed="left").count()
    required = ["open", "high", "low", "close", "volume", "quote_volume", "trades"]
    out = bars.loc[:, [c for c in required if c in bars.columns]]
    out = out.assign(minutes=usable_minutes.reindex(out.index).to_numpy())
    if out["minutes"].isna().any():
        raise ValueError("a daily bar was produced without a matching minute count")
    out = pd.DataFrame(out)
    if repair is not None:
        out.attrs["clock_repair"] = repr(repair)
    return out


def build_daily(symbol: str) -> pd.DataFrame:
    """Build one symbol's pre-cutoff daily bars from the sealed R2 1m minutes.

    Daily bars are **close-labelled** (``[t-1d, t)``, identical to
    ``data/ohlcv``).  Frozen minutes (``trades == 0``) and non-positive closes are
    dropped by :func:`aggregate_daily`, as in the BTC/ETH N1 study.  Every bar is
    rebuilt from the minutes; this module never reads the pipeline store.
    """
    bars = aggregate_daily(r2_klines.read_local(symbol))
    bars = bars[bars.index < CUTOFF].copy()
    if bars.empty:
        raise ValueError(f"{symbol}: no complete UTC day before the cutoff")
    if not (bars["low"] <= bars["close"]).all() or not (bars["high"] >= bars["close"]).all():
        raise ValueError(f"{symbol}: inconsistent daily OHLC after aggregation")
    return bars


# --------------------------------------------------------------------------- #
# Features (strictly causal: row t uses data <= t only)
# --------------------------------------------------------------------------- #

def _rsi(close: pd.Series, length: int = 14) -> pd.Series:
    """Wilder RSI.  A window with no loss saturates at 100, no gain at 0.

    Without those two cases a strictly monotone series produced NaN (the
    ``0/0`` ratio) and the RSI signals could never fire; the neutral 50 the
    draft returned was an arbitrary placeholder, not a measurement.
    """
    delta = close.diff()
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()
    avg_loss = loss.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()
    rs = avg_gain / avg_loss.replace(0.0, np.nan)
    out = 100.0 - 100.0 / (1.0 + rs)
    out = out.mask((avg_loss == 0.0) & (avg_gain > 0.0), 100.0)
    out = out.mask((avg_gain == 0.0) & (avg_loss > 0.0), 0.0)
    return out.where((avg_loss > 0.0) | (avg_gain > 0.0), np.nan)


def _fib(close: pd.Series, ratio: float, lookback: int = 252, min_periods: int = 60) -> pd.Series:
    high = close.rolling(lookback, min_periods=min_periods).max()
    low = close.rolling(lookback, min_periods=min_periods).min()
    return low + ratio * (high - low)


def _weekly_pivots(daily: pd.DataFrame) -> pd.DataFrame:
    """Weekly pivot R1/S1 of the last **completed** week, aligned to daily bars.

    Returns a frame indexed by daily bar with the pivot of the last week that had
    already fully elapsed before that bar.  No look-ahead: a bar dated inside
    week W uses the pivots of week W-1.
    """
    weekly = daily.resample("W-SUN", label="left", closed="left").agg(
        high=("high", "max"), low=("low", "min"), close=("close", "last")
    ).dropna()
    typical = (weekly["high"] + weekly["low"] + weekly["close"]) / 3.0
    pivots = pd.DataFrame(index=weekly.index)
    pivots["r1"] = 2.0 * typical - weekly["low"]
    pivots["s1"] = 2.0 * typical - weekly["high"]
    # A week's pivots become usable only from the next week onwards.
    usable_from = weekly.index + pd.Timedelta(days=7)
    pivots.index = usable_from
    aligned = pivots.reindex(daily.index.union(usable_from)).sort_index().ffill()
    return aligned.reindex(daily.index)


FVG_DELAY = 3


def fvg3_bounds(daily: pd.DataFrame, position: int, direction: str = "up") -> tuple[float, float] | None:
    """Bounds ``(low_bound, high_bound)`` of the 3-bar gap that *fills* at ``position``.

    The gap is opened by bar ``f = position - FVG_DELAY``.  For a bullish gap
    ``low[f] > high[f-2]`` leaves the empty interval ``(high[f-2], low[f])``;
    for a bearish gap ``high[f] < low[f-2]`` leaves ``(low[f-2], high[f])``.

    The draft took **both** bounds from ``shift(2)``, i.e. from the same bar:
    the bullish interval came out inverted and the condition
    ``close <= low and close >= high`` was unsatisfiable, so no FVG could ever
    fire.  Returns ``None`` when the gap does not exist at that position.
    """
    index = int(position)
    opener = index - FVG_DELAY
    if opener < 2 or index >= len(daily):
        return None
    high = daily["high"].to_numpy(dtype=float)
    low = daily["low"].to_numpy(dtype=float)
    if direction == "up":
        older_high, opener_low = high[opener - 2], low[opener]
        if not opener_low > older_high:
            return None
        return float(older_high), float(opener_low)
    if direction == "down":
        older_low, opener_high = low[opener - 2], high[opener]
        if not opener_high < older_low:
            return None
        return float(older_low), float(opener_high)
    raise ValueError(f"unknown gap direction: {direction!r}")


def _fvg3_masks(daily: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Causal fill masks: ``low[f] > high[f-2]`` then a close back inside it."""
    high = daily["high"].astype(float)
    low = daily["low"].astype(float)
    close = daily["close"].astype(float)
    up_lower, up_upper = high.shift(FVG_DELAY + 2), low.shift(FVG_DELAY)
    down_lower, down_upper = low.shift(FVG_DELAY + 2), high.shift(FVG_DELAY)
    up = (up_upper > up_lower) & (close <= up_upper) & (close >= up_lower)
    down = (down_upper < down_lower) & (close >= down_upper) & (close <= down_lower)
    return up.fillna(False), down.fillna(False)


def build_features(daily: pd.DataFrame) -> pd.DataFrame:
    """Return the causal feature table plus forward log-returns for each horizon."""
    daily = daily.sort_index()
    close = daily["close"].astype("float64")
    feats = pd.DataFrame(index=daily.index)
    feats["close"] = close

    feats["sma_5"] = close.rolling(5, min_periods=5).mean()
    feats["sma_10"] = close.rolling(10, min_periods=10).mean()
    feats["sma_20"] = close.rolling(20, min_periods=20).mean()
    feats["sma_30"] = close.rolling(30, min_periods=30).mean()
    feats["sma_50"] = close.rolling(50, min_periods=50).mean()
    feats["sma_100"] = close.rolling(100, min_periods=100).mean()
    feats["sma_200"] = close.rolling(200, min_periods=200).mean()

    feats["rsi14"] = _rsi(close, 14)

    window = close.rolling(20, min_periods=20)
    feats["bb20_lower"] = window.mean() - 2.0 * window.std(ddof=0)
    feats["bb20_upper"] = window.mean() + 2.0 * window.std(ddof=0)
    # The band flags must be *inside* flags.  The draft wrote
    # ``(close > lower) | (close < upper)``, which is the union of the two
    # break signals and is therefore True on almost every bar: tautological.
    feats["bb20_inside_band"] = (close >= feats["bb20_lower"]) & (close <= feats["bb20_upper"])

    feats["donchian_high"] = daily["high"].astype(float).rolling(20, min_periods=20).max().shift(1)
    feats["donchian_low"] = daily["low"].astype(float).rolling(20, min_periods=20).min().shift(1)
    feats["donchian20_inside"] = (
        (close <= feats["donchian_high"]) & (close >= feats["donchian_low"])
    )

    low14 = daily["low"].astype(float).rolling(14, min_periods=14).min()
    high14 = daily["high"].astype(float).rolling(14, min_periods=14).max()
    span = (high14 - low14).replace(0.0, np.nan)
    feats["stoch_k"] = (100.0 * (close - low14) / span).where(span.notna())
    feats["stoch_d"] = feats["stoch_k"].rolling(3, min_periods=3).mean()
    feats["stoch_cross"] = (feats["stoch_k"] > feats["stoch_d"]) | (feats["stoch_k"] < feats["stoch_d"])

    pivots = _weekly_pivots(daily)
    feats["pivot_r1"] = pivots["r1"].to_numpy()
    feats["pivot_s1"] = pivots["s1"].to_numpy()
    feats["pivot_inside_band"] = (
        (close <= feats["pivot_r1"]) & (close >= feats["pivot_s1"])
    )

    for key, ratio in FIB_RATIOS.items():
        feats[f"fib_{key:03d}"] = _fib(close, ratio)

    high = daily["high"].astype(float)
    low = daily["low"].astype(float)
    up_fill, down_fill = _fvg3_masks(daily)
    feats["fvg3_up"] = up_fill
    feats["fvg3_down"] = down_fill
    feats["fvg3"] = feats["fvg3_up"] | feats["fvg3_down"]

    realised = np.log(close).diff().rolling(60, min_periods=60).std() * np.sqrt(365.0)
    feats["vol60"] = realised
    feats["vol_regime"] = (realised > realised.expanding(min_periods=60).median()).astype(float)
    feats["trend_regime"] = (close > feats["sma_200"]).astype(float)

    log_close = np.log(close)
    for horizon in HORIZONS:
        feats[f"fwd_{horizon}d"] = log_close.shift(-horizon) - log_close
    return feats


# --------------------------------------------------------------------------- #
# Signal masks
# --------------------------------------------------------------------------- #

def signal_masks(feats: pd.DataFrame) -> list[tuple[str, pd.Series, pd.Series]]:
    """Return ``(label, mask, inverse_mask)`` for every declared signal.

    ``inverse_mask`` is the exact complement of ``mask`` restricted to the rows
    where the underlying feature is defined: the opposite-polarity reading of
    the very same event (rejection / stop-hunt / false-breakout).
    """
    close = feats["close"] if "close" in feats else None
    if close is None:
        raise ValueError("features must carry a 'close' column")
    masks: dict[str, pd.Series] = {
        "ma_20_100_above": close > feats["sma_20"],
        "ma_50_200_above": (close > feats["sma_50"]) & (close > feats["sma_200"]),
        "ma_10_30_above": (close > feats["sma_10"]) & (close > feats["sma_30"]),
        "ma_5_20_above": (close > feats["sma_5"]) & (close > feats["sma_20"]),
        "rsi14_oversold": feats["rsi14"] < 30.0,
        "rsi14_overbought": feats["rsi14"] > 70.0,
        "bb20_lower_break": close < feats["bb20_lower"],
        "bb20_upper_break": close > feats["bb20_upper"],
        "donchian20_breakout_up": close > feats["donchian_high"],
        "donchian20_breakout_down": close < feats["donchian_low"],
        "stoch14_oversold": feats["stoch_k"] < 20.0,
        "stoch14_overbought": feats["stoch_k"] > 80.0,
        "stoch14_cross_up": (feats["stoch_k"] > feats["stoch_d"]) & (feats["stoch_d"].shift(1) <= feats["stoch_k"].shift(1)),
        "stoch14_cross_down": (feats["stoch_k"] < feats["stoch_d"]) & (feats["stoch_d"].shift(1) >= feats["stoch_k"].shift(1)),
        "pivot_s1_break": close < feats["pivot_s1"],
        "pivot_r1_break": close > feats["pivot_r1"],
        "fvg3_up_fill": feats["fvg3_up"],
        "fvg3_down_fill": feats["fvg3_down"],
    }
    for ratio in (382, 500, 618, 550, 600, 650, 700):
        level = feats[f"fib_{ratio:03d}"]
        masks[f"fib_{ratio}_below"] = close < level
        masks[f"fib_{ratio}_above"] = close > level

    pairs: list[tuple[str, pd.Series, pd.Series]] = []
    for label in SIGNAL_LABELS:
        mask = masks[label].astype("boolean")
        inverse = (~mask).where(mask.notna())
        pairs.append((label, mask, inverse))
    return pairs


# --------------------------------------------------------------------------- #
# Statistics
# --------------------------------------------------------------------------- #

def one_sample_test(values: np.ndarray) -> tuple[float, float, float]:
    """Return ``(mean, t_stat, p_value)`` against 0; NaN when n < MIN_EVENTS."""
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    n = values.size
    if n < MIN_EVENTS:
        return float("nan"), float("nan"), float("nan")
    mean = float(values.mean())
    sd = float(values.std(ddof=1))
    if not np.isfinite(sd) or sd == 0.0:
        return mean, float("nan"), float("nan")
    t_stat = mean / (sd / np.sqrt(n))
    p_value = float(2.0 * stats.t.sf(abs(t_stat), df=n - 1))
    return mean, float(t_stat), p_value


def hac_bandwidth(horizon: int) -> int:
    """Newey-West bandwidth for a horizon: ``max(h, 1)``, i.e. at least ``h-1``.

    ``h``-day forward returns overlap over ``h-1`` days, so the covariance
    estimator must cover at least that many lags.
    """
    return max(int(horizon), 1)


def bartlett_weight(lag: int, bandwidth: int) -> float:
    """Bartlett kernel weight ``1 - lag / (bandwidth + 1)``; 0 beyond the band."""
    lag, bandwidth = int(lag), int(bandwidth)
    if lag > bandwidth:
        return 0.0
    return 1.0 - lag / (bandwidth + 1.0)


def hac_mean_test(values: np.ndarray, bandwidth: int) -> tuple[float, float, float]:
    """Newey-West t-test of the mean of ``values`` against 0.

    Forward returns over ``h`` days overlap, so the events are not independent
    and an IID t-test understates the standard error.  ``values`` is the
    event-conditional score ``y_t = mask_t * fwd_h_t`` on the **whole** daily
    grid, and the long-run variance is the Bartlett-weighted sum of the
    autocovariances::

        S  = g_0 + 2 * sum_{l=1..L} w_l * g_l,   w_l = 1 - l / (L + 1)
        se = sqrt(S / n),                        t  = mean / se

    p-values use the normal reference distribution: with several hundred daily
    bars the t(n-1) and normal tails differ in the fourth decimal, and the
    studentised version is not well defined for a HAC covariance.
    """
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    n = values.size
    if n < MIN_EVENTS:
        return float("nan"), float("nan"), float("nan")
    mean = float(values.mean())
    centered = values - mean
    variance = float(np.dot(centered, centered) / n)
    for lag in range(1, int(bandwidth) + 1):
        gamma = float(np.dot(centered[lag:], centered[:-lag]) / n)
        variance += 2.0 * bartlett_weight(lag, bandwidth) * gamma
    if not np.isfinite(variance) or variance <= 0.0:
        return mean, float("nan"), float("nan")
    t_stat = mean / float(np.sqrt(variance / n))
    p_value = float(2.0 * stats.norm.sf(abs(t_stat)))
    return mean, float(t_stat), p_value


def calendar_block_bootstrap(
    mask: np.ndarray, returns: np.ndarray, block: int, seed: int,
    draws: int = BOOTSTRAPS,
) -> tuple[float, float]:
    """Moving-block bootstrap of the **joint** (mask, return) pair on the grid.

    Resampling the filtered event series would keep every (mask, return) pair
    intact and could not reflect the clustering of the signal.  Here both arrays
    live on the whole daily grid and are resampled with the **same** index draw,
    so the pairing is what breaks.  The statistic is the event mean
    ``mean(returns[mask])`` recomputed on each resampled grid.

    ``draws=0`` is the explicit "no interval requested" case and returns
    ``(NaN, NaN)``; it is what the inverse and placebo cells pass, because a
    confidence interval is a property of the cell under test alone.
    """
    mask = np.asarray(mask, dtype=bool)
    returns = np.asarray(returns, dtype=float)
    n = min(mask.size, returns.size)
    mask, returns = mask[:n], returns[:n]
    block = max(int(block), 1)
    draws = int(draws)
    if draws <= 0:
        return float("nan"), float("nan")
    usable = np.isfinite(returns)
    if n < max(MIN_EVENTS, 2 * block) or usable.sum() < MIN_EVENTS:
        return float("nan"), float("nan")
    if int(mask.sum()) < MIN_EVENTS:
        return float("nan"), float("nan")

    rng = np.random.default_rng(seed)
    n_blocks = int(np.ceil(n / block))
    starts = rng.integers(0, n, size=(draws, n_blocks))
    offsets = np.arange(block)
    idx = (starts[:, :, None] + offsets[None, None, :]) % n
    idx = idx.reshape(draws, -1)[:, :n]

    counts = mask[idx].sum(axis=1)
    totals = np.where(mask[idx], returns[idx], 0.0).sum(axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        means = np.where(counts > 0, totals / np.maximum(counts, 1), np.nan)
    means = means[np.isfinite(means)]
    if means.size == 0:
        return float("nan"), float("nan")
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def bootstrap_mean(values: np.ndarray, block: int, seed: int, draws: int = BOOTSTRAPS) -> tuple[float, float]:
    """Circular moving-block bootstrap percentile CI of the sample mean."""
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    n = values.size
    block = max(int(block), 1)
    if n < max(MIN_EVENTS, 2 * block):
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    n_blocks = int(np.ceil(n / block))
    starts = rng.integers(0, n, size=(draws, n_blocks))
    offsets = np.arange(block)
    idx = (starts[:, :, None] + offsets[None, None, :]) % n
    idx = idx.reshape(draws, -1)[:, :n]
    means = values[idx].mean(axis=1)
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def bh_adjust(p_values: np.ndarray) -> np.ndarray:
    """Benjamini-Hochberg step-up adjusted p-values, NaN-safe."""
    p = np.asarray(p_values, dtype=float)
    q = np.full(p.shape, np.nan)
    valid = np.isfinite(p)
    if not valid.any():
        return q
    sub = p[valid]
    m = sub.size
    order = np.argsort(sub)
    ranked = sub[order] * m / np.arange(1, m + 1)
    ranked = np.minimum.accumulate(ranked[::-1])[::-1]
    adjusted = np.empty(m)
    adjusted[order] = np.clip(ranked, 0.0, 1.0)
    q[valid] = adjusted
    return q


def roll_mask(mask: pd.Series, offset: int) -> pd.Series:
    """Circularly shift a boolean mask, preserving the number of events."""
    values = mask.fillna(False).to_numpy(dtype=bool)
    if values.size == 0:
        return mask
    return pd.Series(np.roll(values, int(offset)), index=mask.index, name=mask.name)


def shift_offset(n: int, seed: int) -> int:
    """The single seeded circular-roll offset of the shift placebo, on ``[1, n-1]``.

    Addendum A §6: the shift placebo destroys the mask's *alignment* with the
    returns while preserving its frequency and serial clustering, which only a
    single circular roll does.  The offset is therefore drawn **once** for the
    whole series, never per bar, and it is strictly forward-looking: an offset of
    0 would leave the mask perfectly aligned with the returns it must falsify,
    so 0 is outside the support.  A degenerate offset also means the placebo is
    the signal itself, which cannot be informative.

    ``rng.integers(1, n)`` is uniform on ``{1, ..., n-1}`` and reproducible for a
    given ``seed``.
    """
    if n < 2:
        return 0
    return int(np.random.default_rng(seed).integers(1, n))


def timing_placebo_return(log_close: pd.Series, horizon: int) -> pd.Series:
    """Timing placebo: ``fwd_h`` read one day later, ``log c_{t+h+1} - log c_{t+1}``.

    The events are untouched; only the instant at which the forward return is
    read moves one day past the declared horizon.  The last ``horizon + 1`` bars
    are NaN because the required close does not exist yet.
    """
    return log_close.shift(-(horizon + 1)) - log_close.shift(-horizon)


# --------------------------------------------------------------------------- #
# The fixed event grid
# --------------------------------------------------------------------------- #

def _placebo_horizon(horizon: int) -> int:
    """Next longer horizon; the longest horizon falls back to the shortest."""
    longer = [h for h in HORIZONS if h > horizon]
    return longer[0] if longer else HORIZONS[0]


@dataclass(frozen=True)
class CellStats:
    mean: float
    t_stat: float
    p_value: float
    n: int


def _grid_score(mask: np.ndarray, returns: np.ndarray) -> np.ndarray:
    """Event-conditional score ``mask * returns`` on the whole daily grid.

    Bars without an event contribute exactly 0, so the HAC variance is estimated
    on the full grid with its true spacing rather than on a compacted series
    whose spacing information has been destroyed.
    """
    returns = np.asarray(returns, dtype=float)
    score = np.where(np.asarray(mask, dtype=bool), returns, 0.0)
    return np.where(np.isfinite(score), score, 0.0)


def _score_stats(
    mask: np.ndarray, returns: np.ndarray, horizon: int, seed: int, draws: int,
) -> tuple[float, float, float, float, float]:
    """``(mean, t, p, ci_lo, ci_hi)`` of the event mean, HAC-inferred.

    ``mean`` is the plain event mean (for reporting), while ``t``/``p`` come from
    the Newey-West test of the grid score and the interval from the moving-block
    bootstrap that resamples ``(mask, returns)`` jointly.
    """
    mask = np.asarray(mask, dtype=bool)
    returns = np.asarray(returns, dtype=float)
    usable = mask & np.isfinite(returns)
    n_events = int(usable.sum())
    if n_events == 0:
        nan = float("nan")
        return nan, nan, nan, nan, nan

    mean = float(returns[usable].mean())
    score = _grid_score(mask, returns)
    _m, t_stat, p_value = hac_mean_test(score, bandwidth=hac_bandwidth(horizon))
    if int(draws) <= 0:
        # No interval was requested: only the cell under test gets a CI. The
        # bootstrap is not merely cheap-skipped here, it is never called, so
        # "one interval per cell" is a property of the call graph.
        return mean, float(t_stat), float(p_value), float("nan"), float("nan")
    ci_lo, ci_hi = calendar_block_bootstrap(
        mask, returns, block=max(5, horizon), seed=seed, draws=draws,
    )
    return mean, float(t_stat), float(p_value), ci_lo, ci_hi


def event_grid(feats: pd.DataFrame, bootstraps: int = BOOTSTRAPS) -> pd.DataFrame:
    """Evaluate the whole preregistered family: 128 cells, inverse + 3 placebos.

    **Shift placebo.**  The event mask circularly rolled by **one** seeded
    offset (`:func:`shift_offset``), scored against the **real** forward return:
    same frequency, same serial clustering, alignment destroyed.  This is not
    the day-level "shift the signal forward" (that is the timing placebo below),
    and it is not the 1m "+15min" placebo of the panels of reference: a
    multi-month lag cannot be simulated from this 1d grid.

    **Timing placebo.**  The same events measured on ``fwd_h`` read one day later
    (`:func:`timing_placebo_return``).

    **Horizon placebo.**  The reference panels used ``"shift(7)"`` — a one-week
    shift on a 1m frame, i.e. effectively nothing.  The horizon placebo below
    uses the *next strictly longer horizon* of this study (14→7, 7→3, 3→1, 1→14),
    a real change of scale.

    All five tests (cell, inverse and the three placebos) go through the same
    HAC machinery on the grid score, so a control can never be judged with a
    looser test than the cell it is meant to falsify.
    """
    pairs = signal_masks(feats)
    close = feats["close"].astype("float64")
    log_close = pd.Series(np.log(close.to_numpy(dtype=float)), index=feats.index)
    fwd_columns = {h: feats[f"fwd_{h}d"] for h in HORIZONS}
    rows: list[dict] = []
    for label, mask, _ in pairs:
        events = mask.fillna(False)
        defined = mask.notna()
        for horizon in HORIZONS:
            fwd = fwd_columns[horizon]
            mean, t_stat, p_value, ci_lo, ci_hi = _score_stats(
                events.to_numpy(), fwd.to_numpy(), horizon, SEED + horizon, bootstraps,
            )

            opposite = (~events) & defined
            # draws=0: the inverse cell reports a mean and a p-value, never an
            # interval -- a CI is a property of the cell under test only.
            inv_mean, inv_t, inv_p, _, _ = _score_stats(
                opposite.to_numpy(), fwd.to_numpy(), horizon, SEED + horizon, 0,
            )

            # Shift placebo: the mask rolled by ONE seeded offset, scored against
            # the real forward return -- frequency and clustering preserved,
            # alignment with the returns destroyed (Addendum A §6).
            rolled = roll_mask(events, offset=shift_offset(len(events), SEED + horizon))
            sh_mean, sh_t, sh_p, _, _ = _score_stats(
                rolled.fillna(False).to_numpy(), fwd.to_numpy(),
                horizon, SEED + horizon, 0,
            )

            # Timing placebo: the return of the extra day beyond the horizon.
            late = timing_placebo_return(log_close, horizon)
            ti_mean, _, ti_p, _, _ = _score_stats(
                events.to_numpy(), late.to_numpy(), horizon, SEED + horizon, 0,
            )

            # Horizon placebo: the next strictly longer horizon of this study.
            other = fwd_columns[_placebo_horizon(horizon)]
            ho_mean, _, ho_p, _, _ = _score_stats(
                events.to_numpy(), other.to_numpy(), horizon, SEED + horizon, 0,
            )

            rows.append({
                "signal": label,
                "horizon": horizon,
                "kind": "placebo_level" if label in PLACEBO_LEVEL_SIGNALS else "primary",
                "n_events": int(events.sum()),
                "mean_fwd": mean, "t_stat": t_stat, "p_value": p_value,
                "ci_lo": ci_lo, "ci_hi": ci_hi,
                "inverse_n": int(opposite.sum()),
                "inverse_mean_fwd": inv_mean, "inverse_t_stat": inv_t, "inverse_p_value": inv_p,
                "placebo_shift_mean": sh_mean,
                "placebo_shift_t_stat": sh_t, "placebo_shift_p_value": sh_p,
                "placebo_timing_mean": ti_mean, "placebo_timing_p_value": ti_p,
                "placebo_horizon_mean": ho_mean, "placebo_horizon_p_value": ho_p,
            })

    grid = pd.DataFrame(rows)
    grid.insert(0, "symbol", "")
    grid["bootstrap_excludes_zero"] = (grid["ci_lo"] > 0) | (grid["ci_hi"] < 0)
    grid["inverse_does_not_dominate"] = (
        grid["inverse_mean_fwd"].abs() <= grid["mean_fwd"].abs()
    )
    grid["placebo_all_non_significant"] = (
        (grid["placebo_shift_p_value"] >= 0.05)
        & (grid["placebo_timing_p_value"] >= 0.05)
        & (grid["placebo_horizon_p_value"] >= 0.05)
    )
    grid["bh_q_asset"] = bh_adjust(grid["p_value"].to_numpy())
    grid["retention"] = (
        (grid["bh_q_asset"] < 0.05)
        & grid["bootstrap_excludes_zero"]
        & grid["inverse_does_not_dominate"]
        & grid["placebo_all_non_significant"]
    )
    return grid[list(GRID_COLUMNS)]


def apply_panel_fdr(grid: pd.DataFrame) -> pd.DataFrame:
    """Add the panel-wide BH-FDR over the union of the primary cells.

    The family is every ``kind == "primary"`` row of the frame handed in, i.e.
    all primary cells of all assets already loaded.  No subsetting.

    Rows of any other kind are **kept** in the output with ``bh_q_panel = NaN``
    so a caller may hand in the full per-asset grid and still get a panel
    correction computed on the declared primary family only.  A non-primary row
    is therefore never retained.
    """
    out = grid.copy()
    q = np.full(len(out), np.nan)
    primary = (out["kind"] == "primary").to_numpy()
    if primary.any():
        q[primary] = bh_adjust(out.loc[primary, "p_value"].to_numpy())
    out["bh_q_panel"] = q
    out["retention_final"] = out["retention"] & (out["bh_q_panel"] < 0.05)
    return out


def regime_breakdown(feats: pd.DataFrame, grid: pd.DataFrame) -> pd.DataFrame:
    """Diagnostics for retained cells only: trend x volatility buckets."""
    columns = ["symbol", "signal", "horizon", "trend", "vol", "n", "mean_fwd", "t_stat", "p_value"]
    rows: list[dict] = []
    retained = grid[grid["retention"]]
    for _, cell in retained.iterrows():
        label, horizon = cell["signal"], int(cell["horizon"])
        mask = dict((lbl, msk) for lbl, msk, _ in signal_masks(feats))[label].fillna(False)
        events = feats.index[mask & feats[f"fwd_{horizon}d"].notna()]
        for trend in (0.0, 1.0):
            for vol in (0.0, 1.0):
                subset = feats[f"fwd_%dd" % horizon][
                    mask & (feats["trend_regime"] == trend) & (feats["vol_regime"] == vol)
                ].to_numpy()
                bucket = (mask & (feats["trend_regime"] == trend)
                          & (feats["vol_regime"] == vol))
                mean, t_stat, p_value, _, _ = _score_stats(
                    bucket.to_numpy(), feats[f"fwd_%dd" % horizon].to_numpy(),
                    horizon, SEED + horizon, BOOTSTRAPS,
                )
                if len(subset) < MIN_EVENTS:
                    continue
                rows.append({
                    "symbol": cell.get("symbol", ""), "signal": label, "horizon": horizon,
                    "trend": "up" if trend else "down", "vol": "high" if vol else "low",
                    "n": len(subset), "mean_fwd": mean, "t_stat": t_stat, "p_value": p_value,
                    "_has_events": len(events) > 0,
                })
    frame = pd.DataFrame(rows, columns=columns)
    return frame


# --------------------------------------------------------------------------- #
# Artifacts
# --------------------------------------------------------------------------- #

def _markdown(symbol: str, features: pd.DataFrame, grid: pd.DataFrame, regime: pd.DataFrame, summary: dict) -> str:
    final = grid[grid["retention_final"]]
    lines = [
        f"# N1 TA alt panel — {symbol} (2026-10-15)",
        "",
        f"* Daily bars: **{summary['days']}** from {summary['first']} to {summary['last']} (UTC).",
        f"* Cutoff (exclusive): `{summary['cutoff_exclusive']}`; last daily bar "
        f"`{summary['last']}` — no bar at or after the cutoff is used.",
        f"* Cells evaluated: **{summary['cells']}** = {len(SIGNAL_LABELS)} signals x {len(HORIZONS)} horizons",
        f"  ({summary['primary_cells']} primary, {summary['cells'] - summary['primary_cells']} placebo-level).",
        f"* Tested cells with n >= {MIN_EVENTS}: {summary['tested_cells']}.",
        f"* Retained after BH-FDR (asset and panel) + bootstrap + inverse + 3 placebos: "
        f"**{summary['retained']}**.",
        "",
        "## Retained cells",
        "",
    ]
    if final.empty:
        lines.append("None: no cell survived the preregistered retention rule.")
    else:
        lines.append("| signal | horizon | n | mean fwd | 95% CI | q(asset) | q(panel) |")
        lines.append("|---|---|---|---|---|---|---|")
        for _, row in final.sort_values("p_value").iterrows():
            lines.append(
                f"| {row['signal']} | {int(row['horizon'])}d | {int(row['n_events'])} | "
                f"{row['mean_fwd']:.5f} | [{row['ci_lo']:.5f}, {row['ci_hi']:.5f}] | "
                f"{row['bh_q_asset']:.4g} | {row['bh_q_panel']:.4g} |"
            )
    lines += [
        "",
        "## Strongest primary cells by p-value (not retained cells are not evidence)",
        "",
        "| signal | horizon | n | mean fwd | p | q(asset) | q(panel) | inverse mean | placebo shift p |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    primary = grid[(grid["kind"] == "primary") & grid["p_value"].notna()]
    for _, row in primary.sort_values("p_value").head(12).iterrows():
        lines.append(
            f"| {row['signal']} | {int(row['horizon'])}d | {int(row['n_events'])} | "
            f"{row['mean_fwd']:.5f} | {row['p_value']:.4g} | {row['bh_q_asset']:.4g} | "
            f"{row['bh_q_panel']:.4g} | {row['inverse_mean_fwd']:.5f} | {row['placebo_shift_p_value']:.4g} |"
        )
    lines += [
        "",
        "## Regime diagnostics (retained cells only, buckets with n >= "
        f"{MIN_EVENTS})",
        "",
    ]
    if regime.empty:
        lines.append("No retained cell, no regime table.")
    else:
        lines.append(regime.drop(columns=[]).to_markdown(index=False))
    lines += [
        "",
        "## Limits",
        "",
        "* Descriptive only. A retained cell is an observation about pre-cutoff history,",
        "  not a tradable edge: no cost model, no execution, no capacity, no holdout.",
        "* No hypothesis was registered and no backtest was run.",
        "* Signals are evaluated on overlapping forward windows, so p-values are",
        "  anti-conservative; the block bootstrap quantifies sampling noise, not",
        "  dependence between cells.",
        "* Multiple horizons of the same signal are highly correlated; BH-FDR assumes",
        "  positive dependence and is therefore conservative here, not anti-conservative.",
        "",
    ]
    return "\n".join(lines)


def write_reports(symbol: str, features: pd.DataFrame, grid: pd.DataFrame,
                  regime: pd.DataFrame) -> dict:
    """Write the per-asset CSV + Markdown artifacts and return the summary."""
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    stem = f"2026-10-15-{symbol.lower()}-n1-ta"
    grid.to_csv(ASSET_DIR / f"{stem}.csv", index=False)
    regime.to_csv(ASSET_DIR / f"{stem}-regime.csv", index=False)
    summary = {
        "symbol": symbol,
        "days": int(len(features)),
        "first": features.index[0].date().isoformat(),
        "last": features.index[-1].date().isoformat(),
        "cutoff_exclusive": CUTOFF.isoformat(),
        "cells": int(len(grid)),
        "primary_cells": int((grid["kind"] == "primary").sum()),
        "tested_cells": int(grid["p_value"].notna().sum()),
        "retained": int(grid["retention_final"].sum()),
    }
    (ASSET_DIR / f"{stem}.md").write_text(_markdown(symbol, features, grid, regime, summary))
    return summary


def run_symbol(symbol: str, bootstraps: int = BOOTSTRAPS) -> dict:
    """Full N1 pipeline for one symbol: daily bars -> features -> fixed grid -> artifacts.

    The **whole** preregistered grid of 128 cells is evaluated and written; the
    panel FDR is computed over its 96 primary cells, exactly as declared.  The
    placebo-level cells are reported for calibration and can never be retained.
    """
    daily = build_daily(symbol)
    features = build_features(daily)
    grid = event_grid(features, bootstraps=bootstraps).assign(symbol=symbol)
    grid = apply_panel_fdr(grid)
    regime = regime_breakdown(features, grid)
    summary = write_reports(symbol, features, grid, regime)
    return {**summary, "grid": grid, "features": features, "regime": regime}
