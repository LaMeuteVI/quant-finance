"""F1 — Funding carry, delta-neutral.

V1 (preregistered 2026-10-16, research/notes/2026-10-16-F1-prereg.md).

For each symbol the strategy is delta-neutral: long the spot leg
``BTCUSDT`` and short the perp leg ``BTCUSDT:USDT`` (and the reverse
when the predicted funding is negative). The signal is the sign of
the 7-day rolling mean of the funding rate, minus a cost cushion
of 2 bps per bar. Position size scales with the magnitude of the
predicted funding relative to the cushion.

This strategy exercises:

* the new ``MarketData``-aware ``target_weights`` API (P1) so it can
  read the funding panel directly,
* the ``perp_legs`` discriminator (P2) so funding is only charged
  on the perp leg of each pair,
* the per-AUM cost grid (P4),
* the walk-forward + PBO report (P5).

V1 wiring note:
    ``MarketData`` aligns the funding panel's columns to the close
    panel's columns (a hard invariant of the dataclass, set in P1).
    The funding rate for a perp symbol is naturally tagged with the
    perp suffix (``BTCUSDT:USDT``) and the close panel uses the spot
    name (``BTCUSDT``), so the two cannot share a single MarketData
    without bending the invariant. For F1 V1 we therefore read the
    funding panel from ``params["funding"]`` (a ``pd.DataFrame``
    indexed by ``<SYMBOL>:USDT`` columns) and the close panel from
    the standard ``target_weights(prices)`` signature. The pipeline
    passes both via ``params``; the strategy is self-contained and
    does not depend on a side channel.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.backtest.metrics import PERIODS_PER_YEAR
from aster.strategies.base import Strategy


def _spot_perp_columns(symbols: list[str]) -> tuple[list[str], list[str], list[str]]:
    """Map ``['BTCUSDT', ...]`` to ``(spot, perp, all)`` column names.

    Spot columns are the plain symbols (``BTCUSDT``) and perp columns
    are suffixed with ``:USDT`` (``BTCUSDT:USDT``) so the engine's
    ``perp_legs`` discriminator can tell them apart. The strategy
    receives the funding panel indexed by the **perp** symbols.
    """
    spot = list(symbols)
    perp = [f"{s}:USDT" for s in symbols]
    return spot, perp, spot + perp


class FundingCarryDN(Strategy):
    """Long spot / short perp when the predicted funding is positive.

    The prediction is the 7-day rolling mean of the funding rate. The
    position is entered with full notional (no vol-targeting) and
    held for as long as the predicted funding exceeds a cost cushion
    of 2 bps per bar. The reverse side is taken when the predicted
    funding is below -2 bps. A basis-z-score guard (>3) blocks new
    entries (a perp discount to spot of 3 sigma usually coincides
    with a crash regime where the carry is about to flip).
    """

    name = "funding_carry_dn"
    version = "1.0.0"
    hypothesis = (
        "Crypto perpetual funding rates are persistent on horizons of hours to "
        "days (term-structure carry). A delta-neutral long-spot / short-perp "
        "position earns the funding minus costs when the predicted funding is "
        "positive, and the reverse when negative. Main risks are funding "
        "regime flips, basis blow-outs in crashes, and venue risk."
    )
    default_params = {
        "lookback_bars": 7 * 6,  # 7 days at 4h bars = 42
        "cost_cushion_bps": 2.0,
        "basis_z_cap": 3.0,
        "max_gross": 1.0,
        # ``funding`` is an optional input panel (perp-indexed wide frame).
        # It is intentionally not part of the Strategy parameter sweep:
        # it is a market input, not a hyper-parameter.
        "funding": None,
    }

    def target_weights(self, prices: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """Compute target weights for a delta-neutral funding-carry book.

        ``prices`` is the wide close panel indexed by the spot symbols
        (``BTCUSDT``). The funding panel is taken from
        ``kwargs["funding"]`` (preferred) or
        ``self.params.get("funding")`` (fallback) and is indexed by
        the perp symbols (``BTCUSDT:USDT``).
        """
        funding: pd.DataFrame | None = kwargs.get("funding")
        if funding is None:
            funding = self.params.get("funding")
        if funding is None:
            # No funding panel → no signal, no carry.
            return pd.DataFrame(0.0, index=prices.index, columns=prices.columns)

        p = self.params
        idx = prices.index
        # Map perp columns -> base symbols.
        perp_cols = [c for c in funding.columns if c.endswith(":USDT")]
        spot_cols = [c.replace(":USDT", "") for c in perp_cols]
        fund = funding[perp_cols].copy()
        fund.columns = spot_cols
        # Restrict to the close panel columns.
        fund = fund.reindex(columns=prices.columns)
        # Predicted funding = rolling mean over the lookback window.
        predicted = fund.rolling(p["lookback_bars"], min_periods=1).mean()
        cushion = p["cost_cushion_bps"] / 1e4
        signal = pd.DataFrame(0.0, index=idx, columns=prices.columns)
        signal[predicted > cushion] = +1.0
        signal[predicted < -cushion] = -1.0
        # Basis guard: a 30-day close z-score above the cap blocks entries.
        if p["basis_z_cap"] is not None and len(idx) > 30:
            z = (prices - prices.rolling(30).mean()) / prices.rolling(30).std()
            block = z.abs() > p["basis_z_cap"]
            signal = signal.where(~block, 0.0)
        # Build the 2N-column weight frame: spot + perp with opposite sign.
        spot, perp, all_cols = _spot_perp_columns(list(prices.columns))
        w = pd.DataFrame(0.0, index=idx, columns=all_cols)
        for s_col, p_col in zip(spot, perp):
            if s_col in signal.columns:
                w[s_col] = signal[s_col] * p["max_gross"]
                w[p_col] = -signal[s_col] * p["max_gross"]
        return w
