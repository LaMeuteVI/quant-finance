import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

DESK = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def isolated_desk(tmp_path, monkeypatch):
    """Every test runs against a throwaway desk with the real config files."""
    shutil.copytree(DESK / "config", tmp_path / "config")
    monkeypatch.setenv("ASTER_DESK", str(tmp_path))
    return tmp_path


@pytest.fixture
def prices():
    """Synthetic 5-asset daily panel, ~4 years, with a late-listed asset (NaN head)."""
    rng = np.random.default_rng(42)
    idx = pd.date_range("2019-01-01", periods=1500, freq="D", tz="UTC")
    cols = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "BNB/USDT", "XRP/USDT"]
    rets = rng.normal(0.0005, 0.03, size=(len(idx), len(cols)))
    px = pd.DataFrame(100 * np.exp(np.cumsum(rets, axis=0)), index=idx, columns=cols)
    px.iloc[:300, 2] = np.nan
    return px
