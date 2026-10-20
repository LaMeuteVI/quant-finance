"""Tests for the descriptive BTC N0 dossier."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.btc_n0 import hourly_profile


def test_hourly_profile_marks_frozen_minutes_and_avoids_zero_division() -> None:
    index = pd.date_range("2024-06-01", periods=3, freq="min", tz="UTC")
    frame = pd.DataFrame(
        {
            "quote_volume": [100.0, 0.0, 300.0],
            "trades": [2, 0, 3],
            "volume": [1.0, 0.0, 3.0],
            "taker_buy_base": [0.4, 0.0, 1.8],
        },
        index=index,
    )
    result = hourly_profile(frame)
    row = result.loc[(5, 0)]  # 2024-06-01 is Saturday.
    assert row["minutes"] == 3
    assert row["frozen_share"] == 1 / 3
    assert row["mean_taker_buy_ratio"] == 0.5
    assert np.isfinite(row["imbalance_std"])
