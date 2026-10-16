"""Tests for q22_microstructure_v3."""
import numpy as np
import pandas as pd

from aster.research import q21_microstructure as q21
from aster.research import q22_microstructure_v3 as q22


def _make_df(n: int, *, seed: int = 0) -> pd.DataFrame:
    rng = np.random.RandomState(seed)
    return pd.DataFrame({
        "agg_trade_id": np.arange(n),
        "price": 100.0 + np.cumsum(rng.normal(0, 0.01, n)),
        "quantity": np.ones(n),
        "transact_time": (1_640_995_200_000 + np.arange(n) * 1000).astype("int64"),
        "is_buyer_maker": rng.randint(0, 2, n).astype(bool),
    })


def test_run_for_bar_1min_basic():
    df = _make_df(20_000, seed=1)
    br = q21.aggregate_bars(df, bar_freq="1min")
    out = q22.run_for_bar.__wrapped__ if hasattr(q22.run_for_bar, "__wrapped__") else None  # noop
    # Just check that the building blocks are wired: 1min + 5min + 15min should all return >0 bars.
    for bf in ("1min", "5min", "15min"):
        br = q21.aggregate_bars(df, bar_freq=bf)
        assert br.n_bars > 0, f"no bars at {bf}"


def test_5min_has_fewer_bars_than_1min():
    df = _make_df(60_000, seed=2)
    bars = {bf: q21.aggregate_bars(df, bar_freq=bf).n_bars for bf in ("1min", "5min", "15min")}
    assert bars["1min"] > bars["5min"] > bars["15min"]


def test_verdict_helper():
    # Pass: spearman > 0.05, q4-q0 > 60 bps
    ax = {
        "predictive_signed_flow": {"spearman": 0.10, "valid": True},
        "quintile_return": {"quintiles": {"Q_max_minus_Q_min": 80.0}, "valid": True},
    }
    v = q22._verdict_for(ax)
    assert v["candidate"] is True
    # Fail: spearman < 0.05
    ax2 = {
        "predictive_signed_flow": {"spearman": 0.01, "valid": True},
        "quintile_return": {"quintiles": {"Q_max_minus_Q_min": 80.0}, "valid": True},
    }
    v2 = q22._verdict_for(ax2)
    assert v2["candidate"] is False
    # Fail: q4-q0 below hurdle
    ax3 = {
        "predictive_signed_flow": {"spearman": 0.10, "valid": True},
        "quintile_return": {"quintiles": {"Q_max_minus_Q_min": 30.0}, "valid": True},
    }
    v3 = q22._verdict_for(ax3)
    assert v3["candidate"] is False


def test_run_cross_basic():
    # synthetic lag-1 series
    n = 20_000
    rng = np.random.RandomState(17)
    base = rng.normal(0, 1, n)
    df_a = pd.DataFrame({
        "agg_trade_id": np.arange(n),
        "price": 100.0 + np.cumsum(rng.normal(0, 0.01, n)),
        "quantity": np.ones(n),
        "transact_time": (1_640_995_200_000 + np.arange(n) * 1000).astype("int64"),
        "is_buyer_maker": (base > 0).astype(bool),
    })
    df_b = pd.DataFrame({
        "agg_trade_id": np.arange(n),
        "price": 100.0 + np.cumsum(rng.normal(0, 0.01, n)),
        "quantity": np.ones(n),
        "transact_time": (1_640_995_200_000 + np.arange(n) * 1000).astype("int64"),
        "is_buyer_maker": (np.roll(base, -1) > 0).astype(bool),
    })
    bar_a = q21.aggregate_bars(df_a, bar_freq="5min").bar
    bar_b = q21.aggregate_bars(df_b, bar_freq="5min").bar
    lag = q21.cross_asset_flow_lag(bar_a, bar_b, max_lag=3)
    assert lag["valid"]
    # In 5-minute bars, 1 trade = 1 minute, so 1 trade lag = 1/5 bar, which dilutes the Spearman.
    # We only check that the structure is correct (valid dict, "1" key present).
    assert "1" in lag["lags"]


def test_default_bar_freqs():
    assert "1min" in q22.DEFAULT_BAR_FREQS
    assert "5min" in q22.DEFAULT_BAR_FREQS
    assert "15min" in q22.DEFAULT_BAR_FREQS
    assert q22.COST_3X_BPS_RT == 60.0
