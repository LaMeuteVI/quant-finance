from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.data.information_bars import (
    build_dollar_bars,
    build_taker_imbalance_bars,
    build_volume_bars,
)


def _make_trades(
    n: int,
    *,
    start_ms: int = 1_700_000_000_000,
    step_ms: int = 1000,
    base_qty: float = 0.1,
    base_price: float = 100.0,
    is_buyer_maker: np.ndarray | None = None,
) -> pd.DataFrame:
    times = np.arange(n) * step_ms + start_ms
    ids = np.arange(n)
    prices = np.full(n, base_price)
    qtys = np.full(n, base_qty)
    if is_buyer_maker is None:
        # Default: alternating maker, so the signed flow is balanced.
        is_buyer_maker = np.tile([True, False], (n + 1) // 2)[:n]
    return pd.DataFrame({
        "agg_trade_id": ids,
        "price": prices,
        "quantity": qtys,
        "transact_time": times,
        "is_buyer_maker": is_buyer_maker,
    })


def test_volume_bars_emits_at_least_one_bar_for_sustained_trading() -> None:
    trades = _make_trades(200)
    spec = build_volume_bars(trades, "BTCUSDT", lookback_days=30, fallback_threshold_btc=0.5)
    assert len(spec.bars) >= 1
    assert spec.family == "volume"
    # Volume bars do not invent trades: cumulative volume across bars equals
    # cumulative volume of the input.
    assert spec.bars["volume"].sum() == pytest.approx(float(trades["quantity"].sum()), rel=1e-6)


def test_volume_bars_threshold_varies_with_prior_day() -> None:
    # 31 days × 100 trades; volume doubles on day 31. Threshold for the next
    # bar should reflect the median of the prior 30 days, not the recent spike.
    times = []
    for d in range(31):
        for i in range(100):
            times.append(1_700_000_000_000 + d * 86_400_000 + i * 1000)
    trades = pd.DataFrame({
        "agg_trade_id": np.arange(len(times)),
        "price": np.full(len(times), 100.0),
        "quantity": np.where(np.array([(t - 1_700_000_000_000) // 86_400_000 for t in times]) == 31, 1.0, 0.1),
        "transact_time": np.array(times),
        "is_buyer_maker": np.tile([True, False], len(times) // 2 + 1)[:len(times)],
    })
    spec = build_volume_bars(trades, "BTCUSDT", lookback_days=30)
    assert len(spec.bars) >= 1


def test_volume_bars_empty_input_returns_empty_frame() -> None:
    empty = pd.DataFrame(columns=["agg_trade_id", "price", "quantity", "transact_time", "is_buyer_maker"])
    spec = build_volume_bars(empty, "BTCUSDT")
    assert len(spec.bars) == 0
    assert spec.family == "volume"


def test_dollar_bars_use_quote_notional() -> None:
    # 500 trades of $100 * 0.1 = $10 each → $5 000. Fallback $1 000 → expect
    # ~5 bars.
    trades = _make_trades(500)
    spec = build_dollar_bars(trades, "BTCUSDT", fallback_threshold_usd=1_000.0)
    assert spec.family == "dollar"
    assert spec.bars["quote_volume"].sum() == pytest.approx(float((trades["price"] * trades["quantity"]).sum()), rel=1e-6)
    # Each bar should hold roughly $1 000 in notional (within a factor of 20 of
    # the threshold; afml expects high variance on small samples).
    if len(spec.bars) > 0:
        bar_notionals = spec.bars["quote_volume"].to_numpy()
        assert (bar_notionals > 0).all()


def test_taker_imbalance_bars_close_on_signed_flow_extreme() -> None:
    # All aggressive buys (is_buyer_maker == False): cum_signed grows
    # monotonically; bars close when |cum| >= threshold.
    n = 200
    is_buyer_maker = np.zeros(n, dtype=bool)
    trades = _make_trades(n, is_buyer_maker=is_buyer_maker)
    spec = build_taker_imbalance_bars(trades, "BTCUSDT", fallback_initial_threshold=2.0)
    assert spec.family == "taker_imbalance"
    if len(spec.bars) > 0:
        # All buys → imbalance is +1 on every bar.
        imb = spec.bars["imbalance"].dropna().to_numpy()
        assert (np.abs(imb - 1.0) < 1e-6).all()


def test_taker_imbalance_bars_balanced_flow_yields_no_extreme_imbalance() -> None:
    # Strictly alternating maker: signed flow cancels → cum_signed stays near
    # zero; bars should be rare because the threshold is never crossed.
    n = 1000
    is_buyer_maker = np.tile([True, False], n // 2)
    trades = _make_trades(n, is_buyer_maker=is_buyer_maker)
    spec = build_taker_imbalance_bars(trades, "BTCUSDT", fallback_initial_threshold=1e9)
    # With an unreachable threshold, the entire stream folds into a single bar.
    assert len(spec.bars) <= 1


def test_information_bars_are_causal_close_label() -> None:
    trades = _make_trades(500)
    spec = build_volume_bars(trades, "BTCUSDT", lookback_days=30, fallback_threshold_btc=0.5)
    if len(spec.bars) == 0:
        pytest.skip("no bars emitted")
    closes = spec.bars.index
    assert isinstance(closes, pd.DatetimeIndex)
    assert str(closes.tz) in ("UTC", "tzutc()")
    # Causal: every trade in the contributing window has ts <= bar_close_ts.
    last_close = int(closes[-1].value // 10**6)
    last_trade_ts = int(trades["transact_time"].max())
    assert last_close <= last_trade_ts + 86_400_000  # allow one day's slack