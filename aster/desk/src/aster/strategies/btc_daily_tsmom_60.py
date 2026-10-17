"""Registered BTC daily 60-day long-only time-series momentum baseline.

The rule is intentionally narrow: BTC/USDT only, long after a positive trailing
60-day close return, otherwise cash.  It is causal: row t references prices no
later than t; the engine applies at least a one-bar execution lag.

Status: UNVALIDATED until the immutable ledger entry says otherwise.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.backtest.metrics import PERIODS_PER_YEAR
from aster.portfolio.sizing import vol_target
from aster.strategies.base import Strategy


class BTCDailyTSMom60(Strategy):
    name = "btc_daily_tsmom_60"
    version = "1.0.0"
    hypothesis = (
        "BTC long-only 60-day time-series momentum earns a net daily trend premium "
        "after conservative taker costs."
    )
    default_params = {
        "lookback": 60,
        "target_vol": 0.40,
        "vol_halflife": 20,
        "max_gross": 1.0,
    }

    def target_weights(self, prices: pd.DataFrame) -> pd.DataFrame:
        """Return causal BTC-only cash-or-long volatility-scaled target weights."""
        if "BTC/USDT" not in prices.columns:
            raise ValueError("btc_daily_tsmom_60 requires BTC/USDT in the universe")
        p = self.params
        returns = prices.pct_change(fill_method=None)
        trailing = prices["BTC/USDT"] / prices["BTC/USDT"].shift(p["lookback"]) - 1.0
        signal = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
        signal["BTC/USDT"] = np.where(trailing > 0.0, 1.0, 0.0)
        # NaN warm-up cannot create a position.  Non-BTC columns intentionally
        # remain cash, allowing a BTC-only hypothesis to run through a wider
        # desk data panel without changing its registered universe.
        signal = signal.where(trailing.notna(), 0.0).where(prices.notna(), 0.0)
        return vol_target(signal, returns, p["target_vol"], PERIODS_PER_YEAR[self.timeframe],
                          p["vol_halflife"], p["max_gross"])
