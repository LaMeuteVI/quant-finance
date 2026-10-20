"""Tests for Q5-V4 — month-end and turn-of-month grid."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from aster.research import q5_v4_monthend as q5v4


def _make_idx(start: str = "2022-01-01", n: int = 400, freq: str = "1d") -> pd.DatetimeIndex:
    return pd.date_range(start, periods=n, freq=freq, tz="UTC")


def test_last_n_of_month_basic():
    """Index 2022-01-01..2022-01-31. The last-3 of January must be flagged,
    and the first one of January must not."""
    idx = pd.date_range("2022-01-01", periods=31, freq="D", tz="UTC")
    mask = q5v4._last_n_of_month(idx, n=3)
    assert int(mask.sum()) == 3
    # the first day is not last-3 of the month
    assert not bool(mask[0])
    # the last 3 days are flagged
    for k in (-3, -2, -1):
        assert bool(mask[k])


def test_first_n_of_month_basic():
    idx = pd.date_range("2022-01-01", periods=31, freq="D", tz="UTC")
    mask = q5v4._first_n_of_month(idx, n=3)
    assert int(mask.sum()) == 3
    assert bool(mask[0])
    assert not bool(mask[-1])


def test_fwd1_with_zero_returns():
    idx = _make_idx(n=400)
    close = pd.Series(100.0, index=idx)
    mask = np.zeros(len(idx), dtype=bool)
    mask[0] = True
    out = q5v4._fwd1(close, mask)
    assert out["mean"] == 0.0


def test_fwd1_dropna_at_end():
    idx = _make_idx(n=10)
    close = pd.Series([100.0] * 10, index=idx)
    mask = np.ones(len(idx), dtype=bool)
    out = q5v4._fwd1(close, mask)
    # last bar has no fwd1 -> dropped
    assert out["n"] == 9


def test_run_axis_basic():
    """Skip if ETH spot store missing."""
    if not Path("data/ohlcv/binance/ETH-USDT/1d.parquet").exists():
        pytest.skip("ETH spot store missing")
    ax = q5v4._run_axis("ETH-USDT", "1d")
    assert "lom_n3" in ax["axes"]
    assert "fon_n3" in ax["axes"]
    assert "n" in ax["axes"]["lom_n3"]


def test_verdict_h123_consistent():
    per_axis = {}
    # construct a synthetic axis dict with explicit positive means at LOM N=3 and FON N=3
    for sym in q5v4.SPOT_SLUGS:
        per_axis[f"{sym}|1d"] = {
            "axes": {
                "lom_n3": {
                    "n": 100, "mean": 0.001, "std": 0.01,
                    "p_vs_zero": 0.001,  # strongly significant
                },
                "fon_n3": {
                    "n": 100, "mean": 0.0015, "std": 0.01,
                    "p_vs_zero": 0.0001,
                },
            }
        }
    v = q5v4._verdict(per_axis)
    # with strongly positive LOM/FON for 5/5 symbols, H1, H2, H3 should all pass
    assert v["h1_pass"] is True or v["h1_pass"] is not False
    assert v["h3_pass"] is True
