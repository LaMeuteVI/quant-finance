"""Reference tests for the N3 realized-volatility study."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research.n3_vol import dm_hln, realized_daily


def _minutes(days: int = 3) -> pd.DataFrame:
    idx = pd.date_range("2022-01-01", periods=days * 1440, freq="1min", tz="UTC")
    r = np.full(len(idx), 0.01, dtype=float)
    log_price = np.log(100.0) + np.cumsum(r)
    close = np.exp(log_price)
    return pd.DataFrame({"close": close, "trades": 1}, index=idx)


def test_realized_variance_reference_and_bipower():
    result = realized_daily(_minutes(3))
    # Prices are in return units; multiplying by 1e8 converts squared returns to bp^2.
    assert result.iloc[0]["rv"] == pytest.approx(1439 * 10000.0)
    assert result.iloc[0]["bv"] == pytest.approx((np.pi / 2) * 1438 * 10000.0)
    assert bool(result["valid"].all())


def test_frozen_minutes_are_not_used_as_returns():
    frame = _minutes(2)
    frame.loc[frame.index[100], "trades"] = 0
    result = realized_daily(frame)
    assert result.iloc[0]["valid_pairs"] == 1437


def test_dm_equal_losses_are_not_significant():
    statistic, pvalue = dm_hln(np.zeros(100))
    assert statistic == 0.0
    assert pvalue == 1.0
