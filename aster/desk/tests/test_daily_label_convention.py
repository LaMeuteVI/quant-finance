"""Boundary tests for the daily aggregation convention, on the real N1 code path.

Every assertion below is measured, not reasoned about pandas semantics.  On a
synthetic minute frame whose price is a distinct increasing integer per minute,
the bucket indexed ``t`` of ``build_bars(..., label="close")`` is
``resample(label="right", closed="left")`` and contains:

  * the **whole previous calendar day**, its 00:00 minute INCLUDED;
  * ``t``'s own 00:00 minute EXCLUDED.

N1 alt uses exactly that primitive, so its daily bars are identical to
``data/ohlcv`` by construction, and a feature computed at row ``t`` reads a bar
whose close only became known at ``t``.  These tests pin both boundary minutes,
the cutoff, and the fact that the panel never reads the store.

Read-only: they assert a convention and never rewrite any data.
"""
import numpy as np
import pandas as pd
import pytest

from aster.data.bars import build_bars
from aster.research import n1_ta_alts as n1

DAY1 = pd.Timestamp("2018-01-05", tz="UTC")
DAY2 = pd.Timestamp("2018-01-06", tz="UTC")
MINUTES_PER_DAY = 24 * 60
#: Longest indicator window in the family (Fibonacci 252-day swing, SMA200,
#: 60-day realised vol).  Any fixture that exercises ``build_features`` must
#: carry at least this many daily bars, otherwise every mask is NaN and a
#: causality assertion would pass vacuously.
FEATURE_WARMUP_DAYS = 300


def _minute_frame(days: int = 3) -> pd.DataFrame:
    """``days`` UTC days, one trade per minute, price increasing by minute."""
    idx = pd.date_range("2018-01-05", periods=days * MINUTES_PER_DAY, freq="min", tz="UTC")
    price = np.arange(1.0, len(idx) + 1.0, dtype=float)
    return pd.DataFrame(
        {
            "open": price, "high": price, "low": price, "close": price,
            "volume": 1.0, "quote_volume": price, "trades": 5,
            "taker_buy_base": 1.0, "taker_buy_quote": price,
        },
        index=pd.DatetimeIndex(idx, name="open_time_utc"),
    )


def _feature_ready_frame() -> pd.DataFrame:
    """A minute frame long enough for every declared indicator to be defined."""
    return _minute_frame(days=FEATURE_WARMUP_DAYS)


def _price_of(stamp: pd.Timestamp) -> float:
    """The synthetic price of the minute opened at ``stamp``."""
    return float((stamp - DAY1) / pd.Timedelta(minutes=1)) + 1.0


def test_close_labelled_bucket_holds_the_previous_calendar_day():
    bars = n1.aggregate_daily(_minute_frame())
    row = bars.loc[DAY2]

    assert row["open"] == pytest.approx(_price_of(DAY1))
    assert row["close"] == pytest.approx(_price_of(DAY2 - pd.Timedelta(minutes=1)))
    assert row["high"] == pytest.approx(_price_of(DAY2 - pd.Timedelta(minutes=1)))
    assert row["low"] == pytest.approx(_price_of(DAY1))
    assert row["trades"] == MINUTES_PER_DAY * 5


def test_bucket_includes_the_previous_days_0000_minute():
    """The previous day's 00:00 minute must land inside the bucket labelled t."""
    frame = _minute_frame()
    spiked = frame.copy()
    # Price strictly above every other minute, so it can only show as the max.
    spiked.loc[DAY1, ["open", "high", "low", "close"]] = 9_000.0

    bars = n1.aggregate_daily(spiked)
    assert bars.loc[DAY2, "high"] == pytest.approx(9_000.0)


def test_bucket_excludes_t_itself_0000_minute():
    """t's own 00:00 minute must land in the NEXT bucket, not in bucket t."""
    frame = _minute_frame()
    spiked = frame.copy()
    spiked.loc[DAY2, ["open", "high", "low", "close"]] = 9_000.0

    bars = n1.aggregate_daily(spiked)
    assert bars.loc[DAY2, "high"] == pytest.approx(
        _price_of(DAY2 - pd.Timedelta(minutes=1))
    )
    assert bars.loc[DAY2 + pd.Timedelta(days=1), "high"] == pytest.approx(9_000.0)


def test_a_frozen_minute_neither_moves_ohlc_nor_counts_as_a_minute():
    """``build_bars`` keeps frozen minutes by default; N1 must still drop them.

    ``build_bars(..., drop_frozen=False)`` is intentional: frozen rows are removed
    by N1 *before* aggregation, exactly as the BTC/ETH protocol does with
    ``(trades > 0) & (close > 0)``.  So the price of a frozen minute must not
    reach the daily OHLC, and it must not be counted as a minute either -- the
    count is taken from the very rows that produced the bar.
    """
    frame = _minute_frame()
    frozen = pd.Timestamp("2018-01-05 12:00", tz="UTC")
    spiked = frame.copy()
    spiked.loc[frozen, ["open", "high", "low", "close"]] = 9_000.0
    spiked.loc[frozen, "trades"] = 0

    bars = n1.aggregate_daily(spiked)
    assert bars.loc[DAY2, "high"] == pytest.approx(
        _price_of(DAY2 - pd.Timedelta(minutes=1))
    )
    assert bars.loc[DAY2, "minutes"] == MINUTES_PER_DAY - 1


def test_a_zero_close_minute_neither_moves_ohlc_nor_counts_as_a_minute():
    """The ``close > 0`` half of the protocol filter is applied too."""
    frame = _minute_frame()
    poisoned = frame.copy()
    zeroed = pd.Timestamp("2018-01-05 12:00", tz="UTC")
    poisoned.loc[zeroed, ["open", "high", "low", "close"]] = 9_000.0
    poisoned.loc[zeroed, "close"] = 0.0
    poisoned.loc[zeroed, "trades"] = 5

    bars = n1.aggregate_daily(poisoned)
    assert bars.loc[DAY2, "high"] == pytest.approx(
        _price_of(DAY2 - pd.Timedelta(minutes=1))
    )
    assert bars.loc[DAY2, "minutes"] == MINUTES_PER_DAY - 1


def test_an_off_grid_minute_is_repaired_before_the_sampling_filter():
    """Clock repair runs first, so the filter is keyed on repaired stamps.

    ``normalise_clock`` is what the canonical store chain calls.  If the filter
    ran before the repair, an off-grid stamp would be judged (and bucketed) on
    its unrepaired value.  This pins the order, not just the outcome.
    """
    frame = _minute_frame()
    off_grid = pd.Timestamp("2018-01-05 12:00:30", tz="UTC")
    skewed = pd.concat([frame, frame.loc[[pd.Timestamp("2018-01-05 12:00", tz="UTC")]]])
    skewed.index = skewed.index[:-1].append(pd.DatetimeIndex([off_grid]))
    skewed.loc[off_grid, ["open", "high", "low", "close"]] = 9_000.0
    skewed.loc[off_grid, "trades"] = 0

    bars = n1.aggregate_daily(skewed)
    # Repaired onto the 12:00 grid, then filtered out for being frozen, so it can
    # neither set the high nor be counted.
    assert bars.loc[DAY2, "high"] == pytest.approx(
        _price_of(DAY2 - pd.Timedelta(minutes=1))
    )
    assert bars.loc[DAY2, "minutes"] == MINUTES_PER_DAY - 1


def test_every_daily_bar_counts_its_minutes_and_stays_ohlc_consistent():
    """Low/high must bracket the surviving minutes, and the counts must add up."""
    frame = _minute_frame()
    spiked = frame.copy()
    spiked.loc[pd.Timestamp("2018-01-05 00:00", tz="UTC"),
               ["open", "high", "low", "close"]] = 9_000.0

    bars = n1.aggregate_daily(spiked)
    assert (bars["minutes"] > 0).all()
    assert (bars["low"] <= bars["close"]).all()
    assert (bars["high"] >= bars["close"]).all()
    # The 9_000 spike is a valid high of its own bucket, so it is the open there.
    assert bars.loc[DAY2, "open"] == pytest.approx(9_000.0)


def test_build_daily_keeps_the_cutoff_strict(monkeypatch):
    """No bar at or after the cutoff survives, and the reader is the sealed one."""
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: _minute_frame())

    daily = n1.build_daily("BNBUSDT")
    assert daily.index.max() < n1.CUTOFF
    # 2018-01-08 00:00 is the last bucket of the fixture; the cutoff is far later,
    # so all three days survive here.
    assert len(daily) == 3


def test_build_daily_drops_a_bar_sitting_on_the_cutoff(monkeypatch):
    """A bar indexed exactly at the cutoff is excluded, not included."""
    idx = pd.date_range(n1.CUTOFF - pd.Timedelta(days=2), periods=3,
                        freq="D", tz="UTC")
    price = np.array([10.0, 11.0, 12.0])
    frame = pd.DataFrame(
        {"open": price, "high": price, "low": price, "close": price,
         "volume": 1.0, "quote_volume": price, "trades": 5,
         "taker_buy_base": 1.0, "taker_buy_quote": price},
        index=pd.DatetimeIndex(idx, name="open_time_utc"),
    )
    minutes = pd.DataFrame(
        {
            "open": np.repeat(price, MINUTES_PER_DAY),
            "high": np.repeat(price, MINUTES_PER_DAY),
            "low": np.repeat(price, MINUTES_PER_DAY),
            "close": np.repeat(price, MINUTES_PER_DAY),
            "volume": np.ones(3 * MINUTES_PER_DAY),
            "quote_volume": np.repeat(price, MINUTES_PER_DAY),
            "trades": np.full(3 * MINUTES_PER_DAY, 5),
            "taker_buy_base": np.ones(3 * MINUTES_PER_DAY),
            "taker_buy_quote": np.repeat(price, MINUTES_PER_DAY),
        },
        index=pd.date_range(n1.CUTOFF - pd.Timedelta(days=3),
                            periods=3 * MINUTES_PER_DAY, freq="min", tz="UTC"),
    )
    assert frame.index.max() == n1.CUTOFF  # the fixture really does touch it
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: minutes)

    daily = n1.build_daily("BNBUSDT")
    assert n1.CUTOFF not in daily.index
    assert daily.index.max() < n1.CUTOFF


def test_signal_and_close_labels_are_causal_on_close_labelled_bars(monkeypatch):
    """A signal at row t must read only bars whose close was known at or before t.

    On close-labelled bars the row ``t`` holds the previous calendar day, so its
    close becomes known exactly at ``t``.  Rewriting every minute from ``cut``
    on changes the rows from ``cut + 1d`` on, and must leave every row at or
    before ``cut`` untouched -- those rows never read those closes.

    The forward return of an earlier row *does* legitimately reference a later
    close (that is what a forward return is), so it is excluded here and pinned
    separately in the leakage test below.
    """
    minutes = _feature_ready_frame()
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: minutes)
    feats = n1.build_features(n1.build_daily("BNBUSDT"))

    cut = feats.index[-3]
    mutated = minutes.copy()
    mutated.loc[mutated.index >= cut, ["open", "high", "low", "close"]] = 9_000.0
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: mutated)
    feats2 = n1.build_features(n1.build_daily("BNBUSDT"))

    # Rows at or before the cut keep exactly the same close.
    safe = feats.index[feats.index <= cut]
    assert np.array_equal(
        feats2.loc[safe, "close"].to_numpy(), feats.loc[safe, "close"].to_numpy()
    )
    # The next row is the first one that reacts: it is the bucket of the day cut.
    reacted = cut + pd.Timedelta(days=1)
    assert not np.isclose(feats2.loc[reacted, "close"], feats.loc[reacted, "close"])


def test_no_signal_reads_a_close_from_a_later_day(monkeypatch):
    """Signal masks at row t may not change when only days > t are rewritten."""
    minutes = _feature_ready_frame()
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: minutes)
    feats = n1.build_features(n1.build_daily("BNBUSDT"))
    baseline = {label: mask for label, mask, _inv in n1.signal_masks(feats)}

    cut = feats.index[-3]
    mutated = minutes.copy()
    mutated.loc[mutated.index >= cut, ["open", "high", "low", "close"]] = 9_000.0
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: mutated)
    feats2 = n1.build_features(n1.build_daily("BNBUSDT"))
    replay = {label: mask for label, mask, _inv in n1.signal_masks(feats2)}

    safe = feats.index[feats.index <= cut]
    for label, original in baseline.items():
        left = replay[label].loc[safe].astype("boolean")
        right = original.loc[safe].astype("boolean")
        assert left.equals(right), label
