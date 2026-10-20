"""V5 — Capacity that actually varies with size.

The AUM sweep in F3 v1.1 (``H-20261020-004``) shows
``sharpe_ann_net`` constant from 100k to 50M USD, because the
pipeline's default cost model is the scalar ``CostModel`` (10+5 bps
flat). The desk has a per-(symbol, hour, notional) grid in
``research/atlas/cost-grid.csv`` (``GridCostModel``), which is what
the capacity report must consume to detect that AUM *does* shrink
edge after edge. This test proves the grid model produces a
strictly decreasing net Sharpe as AUM grows on the F3 v1.1 weights.
"""
from __future__ import annotations

import glob

import numpy as np
import pandas as pd

from aster.backtest.cost_model import GridCostModel
from aster.backtest.engine import run_backtest
from aster.strategies.vol_target_trend_ensemble import VolTargetTrendEnsemble


def _panel_5_majors_1d() -> pd.DataFrame:
    files = sorted(glob.glob("data/ohlcv/binance/*-USDT/1d.parquet"))
    panels = {}
    for f in files:
        df = pd.read_parquet(f)
        sym = f.split("/")[-2]
        panels[sym] = df["close"]
    px = pd.concat(panels, axis=1)
    px.columns = [c.replace("-", "/") for c in px.columns]
    return px[["BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT", "XRP/USDT"]]


def _weights_f3_v1_1(px: pd.DataFrame) -> pd.DataFrame:
    s = VolTargetTrendEnsemble(timeframe="1d")
    return s.target_weights(px)


def test_v5_grid_model_sharpe_decreases_with_aum():
    """With the real per-asset / per-hour / per-notional cost grid,
    the net Sharpe at 50M USD is strictly smaller than at 100k USD on
    the F3 v1.1 weights, on the same dev panel.
    """
    px = _panel_5_majors_1d()
    w = _weights_f3_v1_1(px)
    perp_legs = [f"{c}:USDT" for c in px.columns]
    w_perp = w[perp_legs].copy()
    # Cost grid is keyed by R2 perp slug (``BTCUSDT``).
    grid = pd.read_csv("research/atlas/cost-grid.csv")
    # The grid symbol is the R2 perp slug, e.g. ``BTCUSDT`` (no
    # ``-`` or ``:USDT`` suffix). The strategy emits column names
    # like ``BTC/USDT:USDT`` (pipeline convention); the engine
    # matches per-column cost with the perp_legs list, so we need
    # both conventions in sync. The grid stays in R2 form here;
    # the engine's per-column symbol lookup uses the column name
    # as the lookup key, so we must rename the columns to the R2
    # form before running.
    m = GridCostModel(grid)
    # ``run_backtest`` prices panel needs the perp-leg columns,
    # renamed to the R2 form (``BTCUSDT``) so the cost lookup
    # finds the grid rows.
    r2_perp_legs = [c.replace("/", "").replace(":USDT", "") for c in perp_legs]
    px_perp = px.copy()
    px_perp.columns = r2_perp_legs
    w_perp = w_perp.rename(columns=dict(zip(perp_legs, r2_perp_legs)))
    res_100k = run_backtest(
        px_perp, w_perp, costs=m, lag=1, funding=None,
        perp_legs=r2_perp_legs, AUM=1e5,
    )
    res_50m = run_backtest(
        px_perp, w_perp, costs=m, lag=1, funding=None,
        perp_legs=r2_perp_legs, AUM=5e7,
    )
    sh_100k = res_100k.returns.mean() / res_100k.returns.std() * np.sqrt(365)
    sh_50m = res_50m.returns.mean() / res_50m.returns.std() * np.sqrt(365)
    assert sh_50m < sh_100k, (
        f"GridCostModel: 50M ({sh_50m:.3f}) must be < 100k ({sh_100k:.3f})"
    )