import numpy as np
import pandas as pd

from aster.research import q14_panel


def test_panel_constructs_from_prereg_symbols():
    fake = pd.date_range("2023-05-10", periods=40, freq="1d", tz="UTC")
    rng = np.random.default_rng(42)
    data = {sym: 100 + np.cumsum(rng.normal(0, 1, len(fake))) for sym in q14_panel.SYMBOLS}
    panel = pd.DataFrame(data, index=fake)
    log_panel = np.log(panel.astype(float))
    returns = log_panel.diff().dropna()
    assert returns.shape[1] == len(q14_panel.SYMBOLS)
    assert returns.shape[0] >= 30


def test_half_life_recovers_ar1():
    rng = np.random.default_rng(0)
    s = np.zeros(300)
    for t in range(1, 300):
        s[t] = 0.9 * s[t - 1] + rng.normal(0, 1.0)
    series = pd.Series(s)
    hl = q14_panel._half_life(series)
    assert np.isfinite(hl) and hl > 0


def test_protocol_caps_cutoff():
    assert q14_panel.CUTOFF == pd.Timestamp("2024-07-01", tz="UTC")
    assert q14_panel.PANEL_START == pd.Timestamp("2023-05-05", tz="UTC")
    assert q14_panel.L1_PAIRS == (("SOLUSDT", "NEARUSDT"), ("SOLUSDT", "SUIUSDT"), ("NEARUSDT", "SUIUSDT"))
