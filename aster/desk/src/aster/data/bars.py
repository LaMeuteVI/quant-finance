"""Temporal and information bars from audited pre-cutoff 1-minute klines.

Phase 0 of the research plan (section 4.2).  Two separate jobs live here, and
they are deliberately kept apart:

1. :func:`normalise_clock` repairs a *source* defect, not a market fact.
   Binance served BTC/ETH/BNB klines in December 2017 and around 2018-02-09
   with a constant wall-clock offset of roughly +15 ms to +22 ms on
   ``open_time_utc``.  The prices and the 1-minute spacing are intact, so the
   bars are real, but their timestamps do not sit on the minute grid.  Left
   alone this fabricates sub-minute jitter that a resampler would smear across
   two buckets.  The repair is a pure, tested, logged step, never silent.

2. :func:`build_bars` and :func:`build_information_bars` build the analysis
   units.  Temporal bars are labelled at their **close** (a bar stamped t is
   only knowable at t + period), so no consumer can read row t and use
   information from inside it.  Information bars carry the order-flow content
   that a pure OHLC bar destroys (lopez-de-prado-afml ch02, ch19): dollar
   volume, the aggressive taker imbalance, and the frozen-minute share.

Nothing in this module writes to disk, and nothing here ever reads a
post-cutoff row: the reader is :func:`aster.data.r2_klines.read_local`, which
refuses to hand back a frame crossing the exploration cutoff.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

# Resampling offsets.  Weekly anchors are deliberately absent: crypto trades
# continuously and a weekly bar has no microstructure meaning here.
TIMEFRAMES: dict[str, str] = {
    "5m": "5min",
    "15m": "15min",
    "1h": "1h",
    "4h": "4h",
    "1d": "1D",
}

# Columns the bar builders read.  Anything else is ignored on purpose.
_MINUTE_COLUMNS = (
    "open", "high", "low", "close", "volume", "quote_volume",
    "trades", "taker_buy_base", "taker_buy_quote",
)

_MINUTES = "minutes_in_bar"
_FROZEN = "frozen_minutes"


@dataclass(frozen=True)
class ClockRepair:
    """What :func:`normalise_clock` did, so a report can cite it."""

    rows_before: int
    rows_after: int
    off_grid_before: int
    off_grid_after: int
    dropped_duplicates: int
    dropped_nan: int
    offsets: tuple[str, ...]

    @property
    def changed(self) -> bool:
        return bool(self.off_grid_before)

    def as_dict(self) -> dict:
        return {
            "rows_before": self.rows_before,
            "rows_after": self.rows_after,
            "off_grid_before": self.off_grid_before,
            "off_grid_after": self.off_grid_after,
            "dropped_duplicates": self.dropped_duplicates,
            "dropped_nan": self.dropped_nan,
            "offsets": list(self.offsets),
        }


def normalise_clock(frame: pd.DataFrame) -> tuple[pd.DataFrame, ClockRepair]:
    """Snap minute bars back onto the UTC minute grid and report what changed.

    ``floor`` to the minute is used rather than ``round``: a bar stamped
    09:59:14.789 belongs to the 09:59 bucket, and rounding would push it into
    10:00 and invent a future observation.  Ties after flooring are resolved by
    keeping the **last** row, because Binance appends the corrected print last;
    the number of rows dropped is returned so nothing is lost silently.

    A frame already on the grid is returned untouched (checked first), which
    keeps this free on the hot path for 99 % of partitions.
    """
    if not isinstance(frame.index, pd.DatetimeIndex):
        raise TypeError("normalise_clock requires a DatetimeIndex")
    if frame.index.tz is None:
        raise ValueError("normalise_clock requires a tz-aware index (UTC)")
    if len(frame) == 0:
        return frame.copy(), ClockRepair(0, 0, 0, 0, 0, 0, ())

    index = frame.index
    off_grid = int((index.floor("min") != index).sum())
    if off_grid == 0:
        return frame, ClockRepair(len(index), len(index), 0, 0, 0, 0, ())

    deltas = (index - index.floor("min")).unique()
    offsets = tuple(sorted(str(pd.Timedelta(d)) for d in deltas))

    out = frame.copy()
    out.index = index.floor("min")
    out = out[~out.index.isna()]
    nan_rows = int(len(index) - len(out))
    duplicated = int(out.index.duplicated(keep="last").sum())
    out = out[~out.index.duplicated(keep="last")].sort_index()

    repair = ClockRepair(
        rows_before=int(len(index)),
        rows_after=int(len(out)),
        off_grid_before=off_grid,
        off_grid_after=int((out.index.floor("min") != out.index).sum()),
        dropped_duplicates=duplicated,
        dropped_nan=nan_rows,
        offsets=offsets,
    )
    return out, repair


def _require_minutes(frame: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in _MINUTE_COLUMNS if c not in frame.columns]
    if missing:
        raise ValueError(f"minute frame is missing required columns: {missing}")
    return frame


def build_bars(frame: pd.DataFrame, timeframe: str = "1h",
               *, label: str = "close", drop_frozen: bool = False) -> pd.DataFrame:
    """Resample audited 1-minute bars into ``timeframe`` bars labelled at the close.

    ``label='close'`` is the default and the only correct choice for research:
    the returned index is the bar's closing timestamp, so the bar at ``t``
    contains information from ``(t - period, t]`` and is not usable at ``t``.
    ``label='left'`` is offered for plotting only and is documented as such.

    Frozen minutes (``trades == 0``) are *kept* by default, and their count is
    carried into the ``frozen_minutes`` column so illiquidity stays visible.
    Dropping them silently would change the sampling and hide exactly what the
    quality gate measures; a caller who wants them gone must ask explicitly.
    """
    if timeframe not in TIMEFRAMES:
        raise ValueError(f"unsupported timeframe {timeframe!r}; expected one of {sorted(TIMEFRAMES)}")
    if label not in ("close", "left"):
        raise ValueError("label must be 'close' (research default) or 'left' (plotting)")
    _require_minutes(frame)

    work = frame.copy()
    work[_MINUTES] = 1
    work[_FROZEN] = (work["trades"] == 0).astype(int)
    if drop_frozen:
        work = work[work["trades"] > 0]
        if len(work) == 0:
            raise ValueError("dropping frozen minutes left an empty frame")

    agg = {
        "open": "first", "high": "max", "low": "min", "close": "last",
        "volume": "sum", "quote_volume": "sum", "trades": "sum",
        "taker_buy_base": "sum", "taker_buy_quote": "sum",
        _MINUTES: "sum", _FROZEN: "sum",
    }
    # pandas spells a closed-bar label 'right'; with closed='left' the bucket is
    # (t - period, t] and the label t is the bar's CLOSE, which is the only
    # label a researcher may act on.  'left' is kept for plotting alone.
    resample_label = "right" if label == "close" else "left"
    bars = work[list(_MINUTE_COLUMNS) + [_MINUTES, _FROZEN]].resample(
        TIMEFRAMES[timeframe], label=resample_label, closed="left",
    ).agg(agg)

    # A resampler invents rows for intervals that contain no data at all.  An
    # empty bucket is an unknown price, not a flat close, so the row is dropped
    # rather than filled with a carried-forward or zero price.
    bars = bars.dropna(how="all", subset=["close"])
    # Frozen share is a share of MINUTES, not of trades: dividing the frozen
    # count by the trade total would be a dimensionless but meaningless ratio.
    bars["frozen_share"] = bars[_FROZEN] / bars[_MINUTES].replace(0, np.nan)
    bars = bars.drop(columns=[_MINUTES, _FROZEN])
    bars.index.name = "bar_close_utc" if label == "close" else "bar_open_utc"
    bars.attrs["timeframe"] = timeframe
    bars.attrs["label"] = label
    bars.attrs["drop_frozen"] = bool(drop_frozen)
    return bars


def build_information_bars(frame: pd.DataFrame, timeframe: str = "1h", **kwargs) -> pd.DataFrame:
    """Temporal bars plus the order-flow content OHLC alone destroys.

    Binance klines carry ``taker_buy_base`` / ``taker_buy_quote``: the volume
    that lifted the offer, i.e. the aggressive side of the book.  The signed
    imbalance

        ``imbalance = 2 * taker_buy_ratio - 1``,  ``taker_buy_ratio = taker_buy_base / volume``

    runs from -1 (every trade sold into the bid) to +1 (every trade lifted the
    offer) and is 0 by construction when the taker mix is balanced.  It is the
    kline-level analogue of the order-flow imbalance of afml ch19 and of the
    imbalance-bar sign rule of ch02: the cheapest information-arrival proxy
    available without tick data, and stationary in a way the bar's own return
    is not.

    ``signed_dollar`` is the imbalance expressed in dollars, so a feature built
    on it scales with the asset's own size rather than with a raw ratio.  A
    bucket with no volume at all carries no order-flow information, so its
    imbalance is NaN, not zero: zero would assert a balanced flow that was
    never observed.
    """
    bars = build_bars(frame, timeframe, **kwargs)
    volume = bars["volume"].where(bars["volume"] > 0)
    bars["taker_buy_ratio"] = (bars["taker_buy_base"] / volume).clip(0.0, 1.0)
    bars["imbalance"] = 2.0 * bars["taker_buy_ratio"] - 1.0
    bars["signed_dollar"] = 2.0 * bars["taker_buy_quote"] - bars["quote_volume"]
    bars["dollar_volume"] = bars["quote_volume"]

    no_flow = bars["volume"] <= 0
    for column in ("taker_buy_ratio", "imbalance", "signed_dollar", "dollar_volume"):
        bars.loc[no_flow, column] = np.nan
    return bars


def bars_frame_report(symbol: str, frame: pd.DataFrame, timeframe: str, **kwargs) -> dict:
    """JSON-ready shape of a built information-bar frame, for the atlas and CLI."""
    bars = build_information_bars(frame, timeframe, **kwargs)
    index = pd.DatetimeIndex(bars.index)
    imbalance = bars["imbalance"].dropna()
    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "bars": int(len(bars)),
        "start": index.min().isoformat() if len(index) else None,
        "end": index.max().isoformat() if len(index) else None,
        "columns": list(bars.columns),
        "nan_close": int(bars["close"].isna().sum()),
        "nan_imbalance": int(bars["imbalance"].isna().sum()),
        "mean_imbalance": float(imbalance.mean()) if len(imbalance) else None,
        "imbalance_dispersion": float(imbalance.std()) if len(imbalance) > 1 else None,
        "mean_frozen_share": float(bars["frozen_share"].mean()) if len(bars) else None,
        "index": str(bars.index.name),
        "close_labeled": bars.index.name == "bar_close_utc",
    }