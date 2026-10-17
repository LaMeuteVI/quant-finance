"""<One-line description of the hypothesis this strategy tests>.

Hypothesis: H-YYYYMMDD-NNN
Status: UNVALIDATED until the ledger says otherwise.
"""

from __future__ import annotations

import pandas as pd

from aster.backtest.metrics import PERIODS_PER_YEAR
from aster.portfolio.sizing import vol_target
from aster.strategies.base import Strategy


class MyStrategy(Strategy):
    name = "my_strategy"            # registry key, snake_case
    version = "1.0.0"               # bump on ANY change that alters weights
    hypothesis = "One sentence: why this should earn money after costs."
    default_params = {"lookback": 20, "target_vol": 0.30, "vol_halflife": 20, "max_gross": 1.0}

    def target_weights(self, prices: pd.DataFrame) -> pd.DataFrame:
        """Causal: row t may only use prices up to t. No full-sample stats, no shift(-k), no bfill."""
        p = self.params
        rets = prices.pct_change(fill_method=None)
        signal = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
        # --- signal logic here (values in [-1, 1]) ---
        signal = signal.where(prices.notna(), 0.0)
        return vol_target(signal, rets, p["target_vol"], PERIODS_PER_YEAR[self.timeframe],
                          p["vol_halflife"], p["max_gross"])
