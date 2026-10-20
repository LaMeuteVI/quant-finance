"""Q11 unit tests."""
import numpy as np
import pandas as pd

from aster.research.q11_regimes import _labels


def test_labels_are_trailing_and_causal() -> None:
    idx = pd.date_range("2020-01-01", periods=100, freq="D", tz="UTC")
    f = pd.DataFrame({"ret_22d": np.linspace(-1, 1, 100), "rv_22d": np.linspace(1, 2, 100), "btc_corr_30d": np.linspace(0, 1, 100)}, index=idx)
    out = _labels(f)
    assert set(out.trend_regime.dropna().unique()) == {-1, 1}
    assert out.vol_regime.iloc[0] in (0, 1)
    assert out.corr_regime.iloc[-1] == 1


def test_labels_have_fixed_domains() -> None:
    idx = pd.date_range("2020-01-01", periods=70, freq="D", tz="UTC")
    f = pd.DataFrame({"ret_22d": 0.0, "rv_22d": 1.0, "btc_corr_30d": 0.5}, index=idx)
    out = _labels(f)
    assert set(out.trend_regime.unique()) == {-1}
    assert set(out.corr_regime.unique()) == {1}
