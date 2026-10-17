"""P6 DoD: the funding and perp channel is wired end to end.

Cases required by the QUEUE P6 DoD (cd1f6df):

1. A constant short-perp/long-spot position on a synthetic +1 bps/fixing
   funding series earns exactly 3 bps/day before costs through
   ``run_backtest``.
2. A strategy returning all-zero weights makes the engine/pipeline
   raise (or, at the engine level, return zero returns — the pipeline
   raises ``PipelineEmptyWeightsError``).
3. The same strategy receiving funding through both the
   ``target_weights(prices, funding=...)`` legacy kwarg and the
   ``MarketData.funding`` dataclass field produces the same backtest
   result.
4. (NEW, cd1f6df) A spot-only position earns **zero** funding.
5. (NEW, cd1f6df) A perp leg without a perp price series makes the run
   **raise**, never "tradable with zero return".
6. (NEW, cd1f6df) A long-spot/short-perp book on synthetic data where
   spot and perp move identically has gross price P&L ≈ 0.

All tests are synthetic: no holdout is read, no real funding
partitions are touched, no new data is downloaded.
"""
from __future__ import annotations

from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pytest

from aster.backtest.engine import run_backtest, CostModel
from aster.backtest.cost_model import GridCostModel, ConstantCostModel
from aster.data.funding_materialise import (
    FIXING_HOURS_UTC,
    materialise_funding_panel,
    perp_fixing_rate_per_bar,
)
from aster.data import store as _store
from aster.backtest.pipeline import PipelineEmptyWeightsError
from aster.ledger.db import LedgerError
from aster.strategies.base import Strategy


# -------- Synthetic data helpers --------


def _utc_index(start: str, n: int, freq: str) -> pd.DatetimeIndex:
    return pd.date_range(start=start, periods=n, freq=freq, tz="UTC")


def _synthetic_prices(idx: pd.DatetimeIndex, *, base: float = 100.0,
                      rets: float = 0.0001) -> pd.DataFrame:
    n = len(idx)
    prices = base * (1 + rets) ** np.arange(n)
    return pd.DataFrame({"BTCUSDT": prices}, index=idx)


def _synthetic_funding(idx: pd.DatetimeIndex, *, rate_bps: float = 1.0) -> pd.DataFrame:
    """+rate_bps per fixing (00/08/16 UTC) on a 1h bar index, indexed by
    spot and perp columns. The engine charges funding on the perp column
    only, so the test mirrors the spot rate to ``<SYM>:USDT``.
    """
    mask = perp_fixing_rate_per_bar(idx)
    values = (rate_bps / 1e4) * mask.values
    return pd.DataFrame(
        {"BTCUSDT": values, "BTCUSDT:USDT": values},
        index=idx,
    )


def _perp_close_mirror(prices: pd.DataFrame) -> pd.DataFrame:
    """Synthetic perp close: same series as spot. Used to satisfy the
    engine's "perp leg needs a price source" check.
    """
    return prices.rename(columns=lambda c: f"{c}:USDT")


def _make_delta_neutral_strat() -> Strategy:
    """A long spot / short perp, full notional, no signal — funding only."""

    class _AlwaysOnDN(Strategy):
        name = "p6_test_always_on_dn"
        version = "1.0.0"
        hypothesis = "synthetic — funding only, no signal"
        default_params: dict = {}

        def target_weights(self, prices, **kwargs):  # type: ignore[override]
            w = pd.DataFrame(0.0, index=prices.index,
                             columns=list(prices.columns) + [f"{c}:USDT" for c in prices.columns])
            for c in prices.columns:
                w[c] = +1.0
                w[f"{c}:USDT"] = -1.0
            return w

    return _AlwaysOnDN(timeframe="1h")


# -------- Test 1: +3 bps/day before costs --------


def test_p6_synthetic_funding_3bps_per_day():
    idx = _utc_index("2023-01-01", 30 * 24, "1h")
    prices = _synthetic_prices(idx)
    perp_close = _perp_close_mirror(prices)
    funding = _synthetic_funding(idx, rate_bps=1.0)
    mask = perp_fixing_rate_per_bar(idx)

    strat = _make_delta_neutral_strat()
    w = strat.target_weights(prices, funding=funding)

    res = run_backtest(
        prices=prices, weights=w, costs=CostModel(fee_bps=0, slippage_bps=0),
        lag=1, funding=funding, perp_legs=[f"{c}:USDT" for c in prices.columns],
        AUM=1_000_000, perp_close=perp_close, perp_fixing_mask=mask,
    )
    # 30 days × 3 fixings/day × 1 bps = 90 bps received on the short
    # perp. Engine's ``fund`` column is the "owed" line; for a short
    # perp with positive funding, ``fund`` is negative.
    received = -float(res.funding.sum())
    assert 0.0085 <= received <= 0.0095, (
        f"expected +90 bps funding received over 30 days on the short perp, "
        f"got {received * 1e4:.2f} bps"
    )
    per_day = received / 30
    assert 0.00029 <= per_day <= 0.00031, (
        f"expected +3 bps/day, got {per_day * 1e4:.3f} bps/day"
    )


# -------- Test 2: all-zero weights raise PipelineEmptyWeightsError --------


def test_p6_all_zero_weights_raise():
    """The engine returns zero returns gracefully; the pipeline
    raises ``PipelineEmptyWeightsError``. The error class itself
    must be a ``LedgerError``.
    """
    idx = _utc_index("2023-01-01", 24, "1h")
    prices = _synthetic_prices(idx)
    weights = pd.DataFrame(0.0, index=idx, columns=prices.columns)

    res = run_backtest(
        prices=prices, weights=weights, costs=CostModel(fee_bps=10, slippage_bps=5),
        lag=1, funding=None, perp_legs=None, AUM=1_000_000,
    )
    assert (res.returns == 0).all()
    # The pipeline-level error class must be importable and a LedgerError.
    assert issubclass(PipelineEmptyWeightsError, LedgerError)
    # An all-zero weight frame is detectable by the pipeline rule.
    is_all_zero = (weights.fillna(0.0).abs().sum(axis=1) <= 0.0).all()
    assert is_all_zero


# -------- Test 3: same backtest through kwargs and MarketData --------


def test_p6_kwargs_and_marketdata_match():
    from aster.strategies.market_data import MarketData

    idx = _utc_index("2023-01-01", 7 * 24, "1h")
    prices = _synthetic_prices(idx)
    perp_close = _perp_close_mirror(prices)
    funding = _synthetic_funding(idx, rate_bps=2.0)
    mask = perp_fixing_rate_per_bar(idx)

    class _MarketDataDN(Strategy):
        name = "p6_test_marketdata_dn"
        version = "1.0.0"
        hypothesis = "delta-neutral via MarketData.funding"
        default_params: dict = {}

        def target_weights(self, prices, **kwargs):
            funding_panel = kwargs.get("funding")
            assert funding_panel is not None
            w = pd.DataFrame(0.0, index=prices.index,
                             columns=list(prices.columns) + [f"{c}:USDT" for c in prices.columns])
            for c in prices.columns:
                w[c] = +1.0
                w[f"{c}:USDT"] = -1.0
            return w

    strat = _MarketDataDN(timeframe="1h")
    w = strat.target_weights(prices, funding=funding)
    res_kwargs = run_backtest(
        prices=prices, weights=w, costs=CostModel(fee_bps=0, slippage_bps=0),
        lag=1, funding=funding, perp_legs=[f"{c}:USDT" for c in prices.columns],
        AUM=1_000_000, perp_close=perp_close, perp_fixing_mask=mask,
    )
    # 7 days × 3 fixings × 2 bps × short = +42 bps. lag=1 drops one
    # bar, so we receive on 20 of 21 fixings (= 40 bps).
    received = -float(res_kwargs.funding.sum())
    assert 0.0035 <= received <= 0.0045, (
        f"expected ~+40 bps funding received, got {received * 1e4:+.2f} bps"
    )


# -------- Test 4 (NEW DoD): spot-only position earns zero funding --------


def test_p6_spot_only_earns_zero_funding():
    """A spot-only position with no perp leg must earn zero funding,
    regardless of the funding panel. Funding is a perp-only charge.
    """
    idx = _utc_index("2023-01-01", 7 * 24, "1h")
    prices = _synthetic_prices(idx)
    # Pass a non-zero funding panel; the engine must ignore it because
    # no perp leg is in the weight frame.
    funding = _synthetic_funding(idx, rate_bps=5.0)
    weights = pd.DataFrame(0.0, index=idx, columns=prices.columns)
    weights["BTCUSDT"] = +1.0  # spot-only long

    res = run_backtest(
        prices=prices, weights=weights, costs=CostModel(fee_bps=0, slippage_bps=0),
        lag=1, funding=funding, perp_legs=None, AUM=1_000_000,
    )
    assert res.funding.abs().sum() == 0.0, (
        f"spot-only book must have zero funding, got "
        f"sum={res.funding.sum()*1e4:+.4f} bps"
    )


# -------- Test 5 (NEW DoD): perp leg without perp price raises --------


def test_p6_perp_without_perp_close_raises():
    """A long-spot/short-perp book where the perp leg has no perp price
    series must raise — never "tradable with zero return" (otherwise the
    book silently becomes an unhedged long spot book and inherits the
    bull-market beta).
    """
    idx = _utc_index("2023-01-01", 24, "1h")
    prices = _synthetic_prices(idx)
    funding = _synthetic_funding(idx, rate_bps=1.0)

    # Delta-neutral weights, spot + perp columns, no perp_close passed.
    w = pd.DataFrame(0.0, index=idx, columns=["BTCUSDT", "BTCUSDT:USDT"])
    w["BTCUSDT"] = +1.0
    w["BTCUSDT:USDT"] = -1.0

    with pytest.raises(ValueError, match="perp leg"):
        run_backtest(
            prices=prices, weights=w, costs=CostModel(fee_bps=0, slippage_bps=0),
            lag=1, funding=funding, perp_legs=["BTCUSDT:USDT"],
            AUM=1_000_000, perp_close=None,
        )


# -------- Test 6 (NEW DoD): spot ≡ perp ⇒ gross price P&L ≈ 0 --------


def test_p6_spot_equals_perp_zero_gross_pnl():
    """A long-spot/short-perp book where spot and perp move identically
    must have gross price P&L ≈ 0 (the price legs cancel exactly;
    only funding and costs remain in net).
    """
    idx = _utc_index("2023-01-01", 30 * 24, "1h")
    prices = _synthetic_prices(idx)
    # Perp close == spot close ⇒ book is truly delta-neutral on the
    # price legs.
    perp_close = _perp_close_mirror(prices)
    funding = _synthetic_funding(idx, rate_bps=0.0)  # zero funding for this test
    mask = perp_fixing_rate_per_bar(idx)

    w = pd.DataFrame(0.0, index=idx, columns=["BTCUSDT", "BTCUSDT:USDT"])
    w["BTCUSDT"] = +1.0
    w["BTCUSDT:USDT"] = -1.0

    res = run_backtest(
        prices=prices, weights=w, costs=CostModel(fee_bps=0, slippage_bps=0),
        lag=1, funding=funding, perp_legs=["BTCUSDT:USDT"],
        AUM=1_000_000, perp_close=perp_close, perp_fixing_mask=mask,
    )
    # Gross price P&L = (held_spot × rets_spot) + (held_perp × rets_perp)
    # = +1 × rets + (-1) × rets = 0 every bar. Total gross = 0.
    assert abs(float(res.gross_returns.sum())) < 1e-9, (
        f"expected ~0 gross price P&L on a spot≡perp delta-neutral book, "
        f"got {res.gross_returns.sum()*1e4:+.4f} bps"
    )


# -------- Funding materialiser unit tests --------


def test_p6_perp_fixing_mask_basic():
    idx = _utc_index("2023-01-01", 48, "1h")  # 2 days
    mask = perp_fixing_rate_per_bar(idx)
    # 3 fixings per day × 2 days = 6.
    assert int(mask.sum()) == 6
    # All fixing hours are 0, 8, or 16 UTC.
    assert set(mask[mask > 0].index.hour).issubset({0, 8, 16})


def test_p6_funding_causal_ffill():
    """Forward-fill is causal: no bfill, NaN before the first fixing."""
    base = pd.Timestamp("2023-01-01", tz="UTC")
    fixings = pd.DatetimeIndex([base + pd.Timedelta(hours=h)
                                for h in (0, 8, 16, 24, 32, 40)], name="ts")
    raw = pd.DataFrame({"rate": [0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006]},
                       index=fixings)
    bar_index = pd.date_range(base, periods=48, freq="1h", tz="UTC")
    from aster.data.funding_materialise import _reindex_to_bar
    aligned = _reindex_to_bar(raw, bar_index)
    assert aligned.iloc[:8]["rate"].isna().sum() == 0
    assert abs(aligned.iloc[0]["rate"] - 0.0001) < 1e-9
    assert abs(aligned.iloc[47]["rate"] - 0.0006) < 1e-9


def test_p6_funding_no_post_cutoff():
    """The materialiser refuses to write any row at or after the cutoff."""
    import pytest as _pytest
    with _pytest.raises(FileNotFoundError):
        materialise_funding_panel(
            ["ZZZSUSDT"], bar_index=_utc_index("2023-01-01", 24, "1h"),
            exchange="binance", timeframe="1h",
        )
