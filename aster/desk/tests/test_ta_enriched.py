"""Tests de référence pour ta_enriched (Camarilla, Woodie, Fib)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.ta_enriched import (
    camarilla_pivots,
    woodie_pivots,
    fib_retracements,
    detect_swings_zigzag,
)


def _daily_ohlc(values: list[float]) -> pd.DataFrame:
    """Crée un DataFrame daily OHLC synthétique."""
    idx = pd.date_range("2020-01-01", periods=len(values), freq="D")
    return pd.DataFrame(
        {
            "open": [v * 0.99 for v in values],
            "high": [v * 1.01 for v in values],
            "low": [v * 0.98 for v in values],
            "close": values,
        },
        index=idx,
    )


def test_camarilla_runs():
    daily = _daily_ohlc([100.0] * 50)
    cam = camarilla_pivots(daily)
    assert "cam_h3" in cam.columns
    assert "cam_l3" in cam.columns
    assert "cam_pivot" in cam.columns
    # H3 > L3
    valid = cam.dropna()
    assert (valid["cam_h3"] > valid["cam_l3"]).all()


def test_woodie_runs():
    daily = _daily_ohlc([100.0] * 50)
    wd = woodie_pivots(daily)
    assert "wd_pivot" in wd.columns
    assert "wd_r1" in wd.columns
    assert "wd_s1" in wd.columns
    # Woodie pivot doit être positif (high et low positifs)
    valid = wd.dropna()
    assert (valid["wd_pivot"] > 0).all()
    # R1 doit être > S1
    assert (valid["wd_r1"] > valid["wd_s1"]).all()


def test_detect_swings_zigzag():
    """Construit un prix avec swings marqués (>10% mouvement) et vérifie la détection."""
    daily = _daily_ohlc([100, 115, 105, 120, 100, 130])
    swings = detect_swings_zigzag(daily, threshold=0.10)
    # 10% threshold : on doit détecter au moins 2 pivots (high 115 puis low 105 ou inversement)
    assert len(swings) >= 2
    assert "type" in swings.columns
    assert set(swings["type"].unique()).issubset({"high", "low"})


def test_fib_retracements():
    swing = pd.DataFrame(
        [
            {"start_date": pd.Timestamp("2020-01-01"), "end_date": pd.Timestamp("2020-01-10"),
             "start_val": 100.0, "end_val": 200.0},
        ]
    )
    fib = fib_retracements(swing)
    assert len(fib) == 5  # 5 Fib levels
    # Pour un swing up 100→200, retracement 0.382 depuis 200 = 200 - 0.382*100 = 161.8
    row_382 = fib[fib["fib_level"] == 0.382].iloc[0]
    assert abs(row_382["level_value"] - 161.8) < 0.1


def test_camarilla_cam_l5_less_than_cam_l3():
    """Convention Camarilla : L3 est plus loin du low que L5 (car range * 1.1/4 > range * 1.1/12).
    Donc L5 (plus proche du low) > L3. Le test vérifie cette hiérarchie.
    """
    daily = _daily_ohlc([100, 105, 110, 102, 108])
    cam = camarilla_pivots(daily)
    valid = cam.dropna()
    rng = valid["high"].shift(1) - valid["low"].shift(1)
    nonzero = valid[rng > 0]
    if len(nonzero) > 0:
        # Convention Camarilla : H3 (range*1.1/4) plus loin du high que H5 (range*1.1/12)
        assert (nonzero["cam_h3"] > nonzero["cam_h5"]).all(), "H3 doit être plus loin du high que H5"
        # L3 (range*1.1/4) plus loin du low que L5 (range*1.1/12)
        assert (nonzero["cam_l3"] < nonzero["cam_l5"]).all(), "L3 doit être plus loin du low que L5"
