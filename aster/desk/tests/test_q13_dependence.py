import numpy as np
import pandas as pd

from aster.research import q13_dependence


def test_run_writes_artefact():
    fake = pd.date_range("2022-01-01", periods=20, freq="1d", tz="UTC")
    closes = np.array(
        [
            100.0, 101.0, 100.5, 102.0, 103.0, 102.5, 104.0, 105.0, 104.5, 106.0,
            107.0, 106.5, 108.0, 109.0, 108.5, 110.0, 111.0, 110.5, 112.0, 113.0,
        ]
    )
    panel = pd.DataFrame({sym: closes + i for i, sym in enumerate(q13_dependence.SYMBOLS)}, index=fake)
    log_panel = np.log(panel.astype(float))
    returns = log_panel.diff().dropna()

    corr = returns.corr().values
    n = corr.shape[0]
    denoised, info = q13_dependence._denoise(corr, n / returns.shape[0])
    assert denoised.shape == corr.shape
    assert info["mp_upper"] > 0.0
    clusters, _table = q13_dependence._clusters(denoised)
    assert 2 <= clusters["best_k"] <= 4
    assert len(clusters["chosen_labels"]) == n
    unconditional = q13_dependence._lower_tail(returns, q=0.2)
    assert len(unconditional["pairs"]) == n * (n - 1) // 2


def test_protocol_caps_cutoff():
    assert q13_dependence.CUTOFF == pd.Timestamp("2024-07-01", tz="UTC")
    assert q13_dependence.SYMBOLS[0] == "BNBUSDT"
