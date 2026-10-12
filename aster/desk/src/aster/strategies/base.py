"""Strategy contract.

A strategy is a pure, causal function: close prices (UTC index x symbols)
-> target weights (same shape), where row t uses data up to t only.
Execution timing, costs and risk limits are NOT the strategy's business;
the backtest engine and the risk gate own them.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


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
