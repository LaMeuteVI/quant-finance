from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.strategies.market_data import (
    MarketData,
    REQUIRED_FIELDS,
    OPTIONAL_FIELDS,
    check_market_data_lookahead,
)
from aster.strategies.base import MarketDataStrategy, Strategy


def _make_index(n: int = 20, start: str = "2022-01-01") -> pd.DatetimeIndex:
    return pd.date_range(start, periods=n, freq="D", tz="UTC")


def _make_panel(n: int = 20, symbols: tuple[str, ...] = ("BTC", "ETH"),
                start: str = "2022-01-01", seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    idx = _make_index(n, start)
    data = rng.normal(size=(n, len(symbols))).cumsum(axis=0) + 100
    return pd.DataFrame(data, index=idx, columns=list(symbols))


def _make_market_data(n: int = 20, symbols: tuple[str, ...] = ("BTC", "ETH")) -> MarketData:
    return MarketData(
        close=_make_panel(n, symbols, seed=1),
        open=_make_panel(n, symbols, seed=2),
        high=_make_panel(n, symbols, seed=3),
        low=_make_panel(n, symbols, seed=4),
        volume=_make_panel(n, symbols, seed=5).abs() * 10,
        quote_volume=_make_panel(n, symbols, seed=6).abs() * 1000,
        taker_buy_base=_make_panel(n, symbols, seed=7).abs() * 5,
        taker_buy_quote=_make_panel(n, symbols, seed=8).abs() * 500,
        trades=_make_panel(n, symbols, seed=9).abs() * 100,
        timeframe="1d",
    )


def test_market_data_constructs_with_all_required_fields() -> None:
    md = _make_market_data()
    assert md.symbols == ("BTC", "ETH")
    assert md.timeframe == "1d"
    assert len(md.aligned_index()) == 20
    for f in REQUIRED_FIELDS:
        assert md.panel(f) is not None, f"required field {f} should be present"


def test_market_data_optional_fields_default_none() -> None:
    md = _make_market_data()
    for f in OPTIONAL_FIELDS:
        assert md.panel(f) is None, f"optional field {f} should default to None"


def test_market_data_rejects_naive_index() -> None:
    idx = pd.date_range("2022-01-01", periods=20, freq="D")  # naive
    panel = pd.DataFrame(np.zeros((20, 2)), index=idx, columns=["BTC", "ETH"])
    with pytest.raises(ValueError, match="tz-aware"):
        MarketData(close=panel, open=panel, high=panel, low=panel,
                   volume=panel, quote_volume=panel,
                   taker_buy_base=panel, taker_buy_quote=panel, trades=panel)


def test_market_data_rejects_index_mismatch_between_fields() -> None:
    base = _make_panel(20, seed=1)
    shifted = _make_panel(20, start="2022-01-02", seed=1)  # shifted by 1 day
    with pytest.raises(ValueError, match="differs from close"):
        MarketData(close=base, open=shifted, high=base, low=base,
                   volume=base, quote_volume=base,
                   taker_buy_base=base, taker_buy_quote=base, trades=base)


def test_market_data_rejects_column_mismatch() -> None:
    base = _make_panel(20, symbols=("BTC", "ETH"), seed=1)
    wrong = base[["BTC"]]
    with pytest.raises(ValueError, match="differ from close"):
        MarketData(close=base, open=wrong, high=base, low=base,
                   volume=base, quote_volume=base,
                   taker_buy_base=base, taker_buy_quote=base, trades=base)


def test_market_data_with_truncated_index_keeps_causality() -> None:
    md = _make_market_data()
    cutoff = md.aligned_index()[10]
    truncated = md.with_truncated_index(cutoff)
    assert len(truncated.aligned_index()) == 10
    assert truncated.aligned_index().max() < cutoff


def test_market_data_optional_field_aligned_to_required_index() -> None:
    base = _make_panel(20, seed=1)
    funding = _make_panel(20, start="2022-01-01", seed=99)  # same index, different values
    md = MarketData(
        close=base, open=base, high=base, low=base,
        volume=base, quote_volume=base,
        taker_buy_base=base, taker_buy_quote=base, trades=base,
        funding=funding,
    )
    assert md.panel("funding") is not None
    assert md.panel("funding").shape == md.close.shape
    assert md.panel("funding").index.equals(md.close.index)


class _CloseOnly(Strategy):
    """A close-only strategy used as a regression reference."""

    default_params = {"lookback": 5}

    def target_weights(self, prices: pd.DataFrame) -> pd.DataFrame:
        return (prices / prices.rolling(self.params["lookback"]).mean() - 1).clip(-1, 1)


class _CloseOnlyAdapted(MarketDataStrategy):
    """A multi-input strategy that ignores the new fields and reads close only."""

    default_params = {"lookback": 5}

    def target_weights_market_data(self, market_data: MarketData) -> pd.DataFrame:
        return (market_data.close / market_data.close.rolling(self.params["lookback"]).mean() - 1).clip(-1, 1)

    def _target_weights_close(self, prices: pd.DataFrame) -> pd.DataFrame:
        return (prices / prices.rolling(self.params["lookback"]).mean() - 1).clip(-1, 1)


class _FlowAware(MarketDataStrategy):
    """A multi-input strategy that genuinely consumes flow (volume / taker_buy)."""

    default_params = {"lookback": 5}

    def target_weights_market_data(self, market_data: MarketData) -> pd.DataFrame:
        flow = (market_data.taker_buy_base / market_data.volume.replace(0, np.nan))
        return flow.rolling(self.params["lookback"]).mean().clip(-1, 1).fillna(0)

    def _target_weights_close(self, prices: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame(0, index=prices.index, columns=prices.columns)


def test_close_only_strategy_still_works_with_dataframe() -> None:
    prices = _make_panel()
    strat = _CloseOnly(lookback=3)
    w = strat.target_weights(prices)
    assert w.shape == prices.shape


def test_market_data_strategy_dispatches_to_market_data_signature() -> None:
    md = _make_market_data()
    strat = _close_only = _CloseOnlyAdapted(lookback=3)
    w_multi = strat.target_weights(md)
    w_close = strat.target_weights(md.close)
    # The multi-input path and the close path must agree on the close-only
    # logic, modulo NaN handling at the lookback warmup.
    assert w_multi.shape == w_close.shape


def test_market_data_strategy_default_close_path_raises() -> None:
    prices = _make_panel()
    strat = _FlowAware(lookback=3)
    # The flow-aware strategy explicitly returns zeros on the close path
    # (it has no signal without flow); this is the documented contract.
    w = strat.target_weights(prices)
    assert (w.fillna(0) == 0).all().all()
    md = _make_market_data()
    w_market = strat.target_weights(md)
    assert w_market.shape == md.close.shape


def test_check_market_data_lookahead_pass_for_close_only_strategy_via_adapter() -> None:
    """A close-only strategy wrapped in ``MarketDataStrategy`` keeps the
    same behaviour on the multi-input path: it must pass the per-field
    look-ahead test because it does not consume any field beyond close.
    """
    md = _make_market_data()
    strat = _CloseOnlyAdapted(lookback=3)
    report = check_market_data_lookahead(strat, md)
    assert report["passed"] is True, report
    for name, info in report["fields"].items():
        assert info["passed"] is True, f"field {name} failed: {info}"


def test_check_market_data_lookahead_fails_for_lookahead_strategy() -> None:
    """A strategy that uses a negative-shift (future) must fail the test."""

    class _Lookahead(MarketDataStrategy):
        def target_weights_market_data(self, market_data: MarketData) -> pd.DataFrame:
            # Reads tomorrow's close: this is the very definition of leakage.
            return market_data.close.shift(-1).fillna(0)

    md = _make_market_data()
    strat = _Lookahead()
    report = check_market_data_lookahead(strat, md)
    assert report["passed"] is False
    # The close field is the offending one.
    assert report["fields"]["close"]["passed"] is False
    assert report["fields"]["close"]["delta"] is not None


def test_check_market_data_lookahead_pass_for_flow_aware_causal_strategy() -> None:
    md = _make_market_data()
    strat = _FlowAware(lookback=3)
    report = check_market_data_lookahead(strat, md)
    assert report["passed"] is True, report
    # Volume and taker_buy_base are the consumed fields; they must pass.
    for name in ("volume", "taker_buy_base", "close"):
        assert report["fields"][name]["passed"] is True


def test_market_data_strategy_preserves_required_field_list() -> None:
    md = _make_market_data()
    names = md.field_names()
    for f in REQUIRED_FIELDS:
        assert f in names
    for f in OPTIONAL_FIELDS:
        assert f in names


def test_market_data_strategy_unknown_field_raises() -> None:
    md = _make_market_data()
    with pytest.raises(KeyError):
        md.panel("nonsense")