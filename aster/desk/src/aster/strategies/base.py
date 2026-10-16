"""Strategy contract.

A strategy is a pure, causal function: market data -> target weights.
The historical contract was close-only (``prices: pd.DataFrame -> pd.DataFrame``);
P1 added a multi-input form (``MarketData -> pd.DataFrame``) so that flow,
funding, premium and OI features can be consumed by the strategy. The
close-only path is kept for every existing strategy; the multi-input
form is opt-in via ``target_weights_market_data`` (the dispatcher in
``target_weights`` recognises the new signature and routes accordingly).

Causality is the strategy's responsibility: a target weight at bar
``t`` must be a function of observations up to and including bar ``t``
only. The backtest engine and the risk gate own execution timing,
costs and risk limits.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Union

import pandas as pd

from aster.strategies.market_data import MarketData

PricesOrMarketData = Union[pd.DataFrame, MarketData]


class Strategy(ABC):
    name: str = "base"
    version: str = "0.0.0"
    hypothesis: str = ""          # one sentence: why this should earn money
    default_params: dict = {}

    def __init__(self, timeframe: str = "1d", **params):
        unknown = set(params) - set(self.default_params)
        if unknown:
            raise ValueError(f"unknown params for {self.name}: {sorted(unknown)}")
        self.timeframe = timeframe
        self.params = {**self.default_params, **params}

    @abstractmethod
    def target_weights(self, prices: pd.DataFrame) -> pd.DataFrame: ...

    def describe(self) -> dict:
        return {"name": self.name, "version": self.version, "hypothesis": self.hypothesis,
                "params": self.params, "timeframe": self.timeframe}


class MarketDataStrategy(Strategy):
    """Mixin: opt-in to the multi-input ``MarketData`` contract.

    Subclasses override ``target_weights_market_data`` instead of (or in
    addition to) ``target_weights``. The default ``target_weights`` below
    dispatches to the multi-input path when a ``MarketData`` is passed and
    falls back to the close-only path otherwise, so old call sites that
    pass a ``pd.DataFrame`` of close prices keep working.
    """

    def target_weights_market_data(self, market_data: MarketData) -> pd.DataFrame:
        raise NotImplementedError(
            f"{type(self).__name__} must override target_weights_market_data"
        )

    def target_weights(self, prices: PricesOrMarketData) -> pd.DataFrame:
        if isinstance(prices, MarketData):
            return self.target_weights_market_data(prices)
        # Close-only path: the legacy contract expects a close panel; pass
        # it through unchanged. New multi-input strategies that want to
        # override both signatures may do so by also overriding this method.
        return self._target_weights_close(prices)

    def _target_weights_close(self, prices: pd.DataFrame) -> pd.DataFrame:
        """Default close-only path. Override in subclasses that want
        to opt out of the multi-input dispatch while keeping the old API."""
        raise NotImplementedError(
            f"{type(self).__name__} inherits the close-only contract; "
            "override target_weights or _target_weights_close"
        )
