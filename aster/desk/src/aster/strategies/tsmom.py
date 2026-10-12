"""Reference strategy: volatility-scaled time-series momentum on liquid coins.

Status: TEMPLATE, NOT VALIDATED. It exists to exercise the pipeline end to
end and to show the expected shape of a strategy file. It must go through
the full protocol (pre-registration, dev backtest, holdout, paper) like any
other idea before it trades anything.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from aster.backtest.metrics import PERIODS_PER_YEAR
from aster.portfolio.sizing import vol_target
from aster.strategies.base import Strategy


class TSMom(Strategy):
    name = "tsmom"
    version = "1.0.0"
    hypothesis = ("Crypto returns show medium-horizon trend persistence (slow information diffusion, "
                  "flow-driven herding), so the sign of the trailing return predicts the next period's sign.")
    default_params = {"lookback": 60, "target_vol": 0.40, "vol_halflife": 20, "max_gross": 1.0, "long_only": True}

    def target_weights(self, prices: pd.DataFrame) -> pd.DataFrame:
        p = self.params
        rets = prices.pct_change(fill_method=None)
        signal = np.sign(prices / prices.shift(p["lookback"]) - 1)
        if p["long_only"]:
            signal = signal.clip(lower=0)
        signal = signal.where(prices.notna(), 0.0).fillna(0.0)
        return vol_target(signal, rets, p["target_vol"], PERIODS_PER_YEAR[self.timeframe],
                          p["vol_halflife"], p["max_gross"])
