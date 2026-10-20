"""Q12 flow unit tests."""
import numpy as np
import pandas as pd

from aster.research.q12_intraday_flow import _seed


def test_seed_is_stable_and_symbol_specific() -> None:
    assert _seed("BTCUSDT", "imbalance", 1) == _seed("BTCUSDT", "imbalance", 1)
    assert _seed("BTCUSDT", "imbalance", 1) != _seed("ETHUSDT", "imbalance", 1)


def test_cutoff_is_strict() -> None:
    idx = pd.DatetimeIndex(["2024-06-30 23:59:00+00:00", "2024-07-01 00:00:00+00:00"])
    assert (idx < pd.Timestamp("2024-07-01", tz="UTC")).tolist() == [True, False]
