"""Target-weight backtester with explicit execution lag, costs and funding.

Timing convention (the only one the desk uses):
  weights.loc[t] is decided with information up to and including the close of bar t.
  It is held over bars t+lag ... and earns close-to-close returns from there.
  lag >= 1 is enforced: lag 0 would trade on the close that produced the signal.

Costs are charged on drift-aware turnover: before rebalancing, yesterday's
weights have drifted with prices, and only the gap to the new target trades.
Funding (perps): a positive rate means longs pay shorts, per bar held.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class CostModel:
    fee_bps: float = 10.0        # taker fee per side
    slippage_bps: float = 5.0    # half-spread + impact per side

    def scaled(self, k: float) -> "CostModel":
        return CostModel(self.fee_bps * k, self.slippage_bps * k)

    @property
    def total_bps(self) -> float:
        return self.fee_bps + self.slippage_bps


@dataclass
class BacktestResult:
    returns: pd.Series            # net per-bar portfolio return
    gross_returns: pd.Series
    costs: pd.Series
    funding: pd.Series
    held: pd.DataFrame            # weights actually held during each bar
    turnover: pd.Series
    meta: dict = field(default_factory=dict)

    @property
    def equity(self) -> pd.Series:
        return (1 + self.returns).cumprod()


def run_backtest(prices: pd.DataFrame, weights: pd.DataFrame, costs: CostModel | None = None,
                 lag: int = 1, funding: pd.DataFrame | None = None) -> BacktestResult:
    if lag < 1:
        raise ValueError("lag must be >= 1: a signal cannot trade on the bar that produced it")
    costs = costs or CostModel()
    prices = prices.sort_index()
    weights = weights.reindex(index=prices.index, columns=prices.columns).fillna(0.0)

    rets = prices.pct_change(fill_method=None)
    tradable = prices.notna() & prices.shift(1).notna()
    held = weights.shift(lag).fillna(0.0).where(tradable, 0.0)
    rets = rets.where(tradable, 0.0).fillna(0.0)

    gross = (held * rets).sum(axis=1)
    # weights after bar t's price move, before the next rebalance
    drifted = held * (1 + rets)
    denom = (1 + gross).replace(0, np.nan)
    drifted = drifted.div(denom, axis=0).fillna(0.0)
    turnover = (held - drifted.shift(1).fillna(0.0)).abs().sum(axis=1)
    cost = turnover * costs.total_bps / 1e4

    fund = pd.Series(0.0, index=prices.index)
    if funding is not None:
        f = funding.reindex(index=prices.index, columns=prices.columns).fillna(0.0)
        fund = (held * f).sum(axis=1)

    net = gross - cost - fund
    return BacktestResult(
        returns=net, gross_returns=gross, costs=cost, funding=fund, held=held, turnover=turnover,
        meta={"lag": lag, "fee_bps": costs.fee_bps, "slippage_bps": costs.slippage_bps},
    )
