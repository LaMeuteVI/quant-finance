"""F1 — Funding carry, delta-neutral.

V1 (preregistered 2026-10-16, research/notes/2026-10-16-F1-prereg.md,
H-20261016-002, rejected on infrastructure: the pipeline did not
inject the funding panel into the strategy).

V2 (preregistered 2026-10-18, research/notes/2026-10-18-F1v2-prereg.md,
H-20261018-001). The infrastructure bottleneck is fixed: P6 wires the
funding panel into ``pipeline.run -> run_backtest`` and Q3b wires the
perp close panel. The strategy now also reads the perp close to build
the basis guard (a perp discount to spot of 3 sigma usually coincides
with a crash regime where the carry is about to flip).

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

V2 wiring note:
    The pipeline now passes the perp close panel through
    ``kwargs["perp_close"]`` (F1v2 reads it from there) and the
    funding panel through ``kwargs["funding"]`` (V1 used that path
    too). The legacy ``target_weights(prices)`` signature is kept so
    the strategy is self-contained. Strategies that consume a
    ``MarketData`` directly are a future refactor (P1 left the
    adapter in place for the old API; F1v2 keeps the same API).

V2 signal change:
    The basis guard now uses the **perp close** (from Q3b) vs the
    spot close to compute ``basis = (perp - spot) / spot`` and
    z-scores basis over 30 bars. A basis z-score above the cap
    blocks new entries. V1 used the spot return z-score, which is a
    different signal and a worse crash proxy.
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
    funding is below -2 bps.

    V2 basis guard: a 30-bar z-score of ``(perp_close - spot_close) /
    spot_close`` above 3.0 blocks new entries. A perp discount to
    spot of 3 sigma usually coincides with a crash regime where the
    carry is about to flip. If the perp close panel is not supplied,
    V2 falls back to V1's spot-return z-score so unit tests that
    don't supply a perp close still work.
    """

    name = "funding_carry_dn"
    version = "1.1.0"
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
        # V2: ``perp_close`` is the perp close panel from Q3b (spot-indexed).
        "perp_close": None,
    }

    def target_weights(self, prices: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """Compute target weights for a delta-neutral funding-carry book.

        ``prices`` is the wide close panel indexed by the spot symbols
        (``BTCUSDT``). The funding panel is taken from
        ``kwargs["funding"]`` (preferred) or
        ``self.params.get("funding")`` (fallback) and is indexed by
        the perp symbols (``BTCUSDT:USDT``). The perp close panel
        (Q3b) is taken from ``kwargs["perp_close"]`` (preferred) or
        ``self.params.get("perp_close")`` (fallback); it is indexed
        by the spot symbols so it shares the close panel's columns.
        """
        funding: pd.DataFrame | None = kwargs.get("funding")
        if funding is None:
            funding = self.params.get("funding")
        if funding is None:
            # No funding panel -> no signal, no carry.
            return pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
        perp_close: pd.DataFrame | None = kwargs.get("perp_close")
        if perp_close is None:
            perp_close = self.params.get("perp_close")

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
        # V2 basis guard: z-score of (perp - spot)/spot over 30 bars.
        # V1 used the spot return z-score, which is a different signal
        # and a worse crash proxy. If the perp close panel is missing
        # we fall back to the V1 spot-return z-score (preserves the V1
        # contract for unit tests that don't supply a perp close).
        if p["basis_z_cap"] is not None and len(idx) > 30:
            if perp_close is not None and not perp_close.empty:
                basis_source = perp_close.reindex(columns=prices.columns)
                # Need at least some overlap; if not, fall back.
                if basis_source.notna().sum().sum() > 0:
                    basis = (basis_source - prices) / prices
                    basis_mean = basis.rolling(30, min_periods=5).mean()
                    basis_std = basis.rolling(30, min_periods=5).std()
                    z = (basis - basis_mean) / basis_std
                    block = z.abs() > p["basis_z_cap"]
                    signal = signal.where(~block, 0.0)
            else:
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
