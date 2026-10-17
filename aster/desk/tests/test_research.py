import numpy as np
import pandas as pd
import pytest

from aster.data.quality import check_ohlcv
from aster.portfolio.sizing import hrp_weights, vol_target
from aster.research.labeling import cusum_events, frac_diff_ffd, triple_barrier


def test_triple_barrier_labels_and_t1(prices):
    close = prices["BTC/USDT"]
    vol = close.pct_change().ewm(span=20).std()
    ev = cusum_events(close, 0.05)
    lab = triple_barrier(close, ev, vol, 1.0, 1.0, horizon=10)
    assert set(lab["label"].unique()) <= {-1, 0, 1}
    assert (lab["t1"] >= lab.index).all()
    assert ((lab["t1"] - lab.index) <= pd.Timedelta(days=10)).all()


def test_ffd_is_causal_and_d0_is_identity(prices):
    s = prices["BTC/USDT"]
    np.testing.assert_allclose(frac_diff_ffd(s, 0.0).dropna(), s.dropna())
    full = frac_diff_ffd(s, 0.4)
    part = frac_diff_ffd(s.iloc[:800], 0.4)
    assert full.iloc[799] == pytest.approx(part.iloc[799])


def test_vol_target_caps_gross(prices):
    sig = pd.DataFrame(1.0, index=prices.index, columns=prices.columns)
    w = vol_target(sig, prices.pct_change(), 2.0, 365, max_gross=1.0)
    assert (w.abs().sum(axis=1) <= 1.0 + 1e-9).all()


def test_hrp_weights_sum_to_one(prices):
    w = hrp_weights(prices.pct_change().dropna())
    assert w.sum() == pytest.approx(1.0) and (w > 0).all()


def test_quality_flags_bad_bars():
    idx = pd.date_range("2024-01-01", periods=5, freq="D", tz="UTC")
    df = pd.DataFrame({"open": [1, 1, 1, 1, 1], "high": [2, 2, 2, 2, 0.5], "low": [0.5] * 5,
                       "close": [1, 1, 1, 1, 1], "volume": [1] * 5}, index=idx, dtype=float)
    r = check_ohlcv(df, "1d")
    assert not r.ok
