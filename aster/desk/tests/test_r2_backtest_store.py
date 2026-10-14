"""Reference tests for pre-cutoff R2 -> daily backtest-store materialisation."""
from __future__ import annotations

import pandas as pd
import pytest

from aster.data.r2_backtest_store import daily_from_minutes


def _minutes(start: str, periods: int) -> pd.DataFrame:
    index = pd.date_range(start, periods=periods, freq="min", tz="UTC")
    px = pd.Series(range(len(index)), index=index, dtype=float) + 100.0
    return pd.DataFrame(
        {
            "open": px, "high": px + 1, "low": px - 1, "close": px + 0.5,
            "volume": 1.0, "quote_volume": 100.0, "trades": 1,
            "taker_buy_base": 0.5, "taker_buy_quote": 50.0,
        }, index=index,
    )


def test_daily_from_minutes_keeps_only_complete_pre_cutoff_daily_bars() -> None:
    # The bar labelled 2024-07-01 would contain the final 2024-06-30 day and is
    # excluded: it is the boundary at which the pre-cutoff research reader stops.
    frame = _minutes("2024-06-29", 3 * 24 * 60)
    bars = daily_from_minutes(frame)
    assert list(bars.index) == [pd.Timestamp("2024-06-30", tz="UTC")]
    assert bars.iloc[0]["open"] == pytest.approx(100.0)
    assert bars.iloc[0]["close"] == pytest.approx(100.0 + 24 * 60 - 1 + 0.5)
    assert (bars.index < pd.Timestamp("2024-07-01", tz="UTC")).all()


def test_daily_from_minutes_preserves_required_ohlcv_schema() -> None:
    bars = daily_from_minutes(_minutes("2024-06-28", 2 * 24 * 60))
    assert list(bars.columns) == ["open", "high", "low", "close", "volume", "quote_volume", "trades"]
    assert bars.index.tz is not None
