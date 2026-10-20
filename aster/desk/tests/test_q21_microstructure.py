"""Tests for q21_microstructure."""
import math

import numpy as np
import pandas as pd

from aster.research import q21_microstructure as q21


def test_tick_rule_sign_up_down():
    is_bm = np.array([False, True, False, True, False])  # prices go 100, 101, 99, 100, 101
    prices = np.array([100.0, 101.0, 99.0, 100.0, 101.0])
    sign = q21.tick_rule_sign(prices)  # we pass prices by name, but the function
    # accepts any numeric array; the test is on the tick-rule logic.
    assert sign[0] == 1
    # tick goes up 100→101 → +1, 101→99 → -1, 99→100 → +1, 100→101 → +1
    assert list(sign[1:]) == [1, -1, 1, 1]


def test_is_buy_aggressor():
    is_bm = np.array([False, True, False, True])
    buy = q21.is_buy_aggressor(is_bm)
    assert list(buy) == [True, False, True, False]


def test_aggregate_bars_basic():
    n = 1000
    df = pd.DataFrame({
        "agg_trade_id": np.arange(n),
        "price": 100.0 + np.cumsum(np.random.RandomState(0).normal(0, 0.01, n)),
        "quantity": np.ones(n),
        "transact_time": (1_640_995_200_000 + np.arange(n) * 100).astype("int64"),
        "is_buyer_maker": np.random.RandomState(0).randint(0, 2, n).astype(bool),
    })
    br = q21.aggregate_bars(df, bar_freq="1min")
    assert br.n_bars >= 1
    assert br.n_trades_total == n
    assert "vwap" in br.bar.columns
    assert "signed_flow_imbalance" in br.bar.columns


def test_kyle_lambda_returns_value():
    # 200 bars: spread 20_000 trades over ~200 minutes (~100 trades/bar)
    n = 20_000
    rng = np.random.RandomState(42)
    df = pd.DataFrame({
        "agg_trade_id": np.arange(n),
        "price": 100.0 + np.cumsum(rng.normal(0, 0.01, n)),
        "quantity": np.ones(n),
        "transact_time": (1_640_995_200_000 + np.arange(n) * 1000).astype("int64"),
        "is_buyer_maker": rng.randint(0, 2, n).astype(bool),
    })
    br = q21.aggregate_bars(df, bar_freq="1min")
    out = q21.kyle_lambda(br.bar)
    assert out["valid"], f"kyle_lambda returned invalid: {out}"
    assert isinstance(out["lambda"], float)
    assert isinstance(out["t_stat"], float)


def test_amihud_returns_value():
    n = 20_000
    rng = np.random.RandomState(7)
    df = pd.DataFrame({
        "agg_trade_id": np.arange(n),
        "price": 100.0 + np.cumsum(rng.normal(0, 0.01, n)),
        "quantity": np.ones(n) * 0.5,
        "transact_time": (1_640_995_200_000 + np.arange(n) * 1000).astype("int64"),
        "is_buyer_maker": rng.randint(0, 2, n).astype(bool),
    })
    br = q21.aggregate_bars(df, bar_freq="1min")
    out = q21.amihud(br.bar)
    assert out["valid"], f"amihud returned invalid: {out}"
    assert out["mean"] is not None
    assert out["mean"] > 0


def test_roll_spread_valid():
    n = 20_000
    rng = np.random.RandomState(11)
    df = pd.DataFrame({
        "agg_trade_id": np.arange(n),
        "price": 100.0 + np.cumsum(rng.normal(0, 0.01, n)),
        "quantity": np.ones(n),
        "transact_time": (1_640_995_200_000 + np.arange(n) * 1000).astype("int64"),
        "is_buyer_maker": rng.randint(0, 2, n).astype(bool),
    })
    br = q21.aggregate_bars(df, bar_freq="1min")
    out = q21.roll_spread(br.bar)
    if out["valid"]:
        assert out["roll_spread_bps"] is not None
        assert out["roll_spread_bps"] >= 0


def test_vpin_returns_value():
    n = 20_000
    rng = np.random.RandomState(13)
    df = pd.DataFrame({
        "agg_trade_id": np.arange(n),
        "price": 100.0 + np.cumsum(rng.normal(0, 0.01, n)),
        "quantity": rng.uniform(0.1, 1.0, n),
        "transact_time": (1_640_995_200_000 + np.arange(n) * 1000).astype("int64"),
        "is_buyer_maker": rng.randint(0, 2, n).astype(bool),
    })
    br = q21.aggregate_bars(df, bar_freq="1min")
    out = q21.vpin(br.bar, n_buckets=20, min_bars=200)
    assert out["valid"], f"vpin returned invalid: {out}"
    assert 0.0 <= out["vpin"] <= 1.0


def test_cross_asset_flow_lag_basic():
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
        "is_buyer_maker": (np.roll(base, -1) > 0).astype(bool),  # 1-bar lag
    })
    bar_a = q21.aggregate_bars(df_a, bar_freq="1min").bar
    bar_b = q21.aggregate_bars(df_b, bar_freq="1min").bar
    out = q21.cross_asset_flow_lag(bar_a, bar_b, max_lag=3)
    assert out["valid"]
    assert "1" in out["lags"]
    # with the synthetic lag-1, lag=1 should be positive
    lag1 = out["lags"]["1"]["rho"]
    assert lag1 is not None and lag1 > 0.1


def test_net_3x_cost():
    # 100 bps gross, 10 bps/side: net = 100 − 60 = 40
    assert q21.net_3x_cost(100.0, cost_bps_side=10.0) == 40.0
    # 50 bps gross: net = 50 − 60 = −10
    assert q21.net_3x_cost(50.0, cost_bps_side=10.0) == -10.0
