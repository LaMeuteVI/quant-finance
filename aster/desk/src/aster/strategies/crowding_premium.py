"""F2 — Funding and premium as a crowding signal.

Preregistered 2026-10-18, research/notes/2026-10-18-F2-prereg.md.

Directional perp position against extreme funding or premium
z-scores, conditioned on open-interest change. Mechanism: crowded
leveraged positioning is forced out (liquidations).

V1 (this file, ``crowding_premium`` v1.0.0):
- **Perp-only** directional book (no spot leg). The basis P&L is
  the strategy's intended source of return; the funding drag is
  the cost of holding the position between the entry and exit
  premium z-score crossings.
- The position enters when the premium z-score crosses an
  ``entry_z`` threshold (perp rich = short-perp; perp cheap =
  long-perp) AND the open-interest z-score agrees with the
  direction (rising OI = more crowding = stronger reversion).
- The position exits when the premium z-score reverts inside
  the ``exit_z`` band.

The family is ``crowding-premium`` (separate from
``funding-carry-dn``). DSR is computed per-family and starts
at 1 for F2 v1.
"""
from __future__ import annotations

from typing import Optional

import numpy as np
import pandas as pd

from aster.strategies.base import Strategy


class CrowdingPremium(Strategy):
    """Short perp when perp-vs-spot premium is rich and OI is rising."""

    name = "crowding_premium"
    version = "1.0.0"
    hypothesis = (
        "The perp-vs-spot premium is a direct proxy for crowded "
        "leveraged positioning. An extreme premium z-score that is "
        "also accompanied by rising open interest tends to mean-"
        "revert within 1-2 weeks as the over-leveraged side is "
        "liquidated. A directional perp position that fades the "
        "extremes earns the basis reversion net of costs."
    )
    default_params = {
        "timeframe": "4h",
        "premium_lookback_bars": 30 * 6,  # 30 days at 4h
        "entry_z": 2.0,
        "exit_z": 0.5,
        # The default 90-day lookback is too long for the unit
        # tests (200 bars = 33 days). Tests pass a smaller
        # ``oi_lookback_bars`` directly. The dev backtest uses
        # the 90-day default.
        "oi_lookback_bars": 90 * 6,
        "oi_min_z": 0.5,
        "max_gross": 1.0,
        "min_required_history": 60,
        # Market input panels (kwargs). Perp-only book: funding is
        # the cost of carry between entry and exit. Perp close is
        # used to compute the basis z-score. The metrics panel
        # (daily) is the open-interest panel; the loader ffill-aligns
        # it to the bar index.
        "funding": None,
        "perp_close": None,
        "oi": None,
    }

    def target_weights(self, prices: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """Compute target weights for a perp-only directional book.

        ``prices`` is the wide spot close panel (idx x symbols).
        ``perp_close`` is the wide perp close panel (idx x symbols,
        same column names as ``prices`` after the pipeline rename).
        ``funding`` is the wide funding panel (perp-leg columns,
        e.g. ``BTC-USDT:USDT``).
        ``oi`` is the wide open-interest panel (idx x symbols, same
        columns as ``prices``); daily data, forward-filled by the
        loader.

        The strategy emits a 2N-column weight frame: spot leg (= 0
        always) + perp leg. The engine treats only the perp leg as
        a perp (via ``perp_legs`` in the prereg), so the spot leg
        never pays funding and the perp leg does.

        Returns a wide weight DataFrame indexed like ``prices``
        with the columns ``[spot_1, perp_1, spot_2, perp_2, ...]``
        where ``perp_i = f"{spot_i}:USDT"``.
        """
        perp_close: Optional[pd.DataFrame] = kwargs.get("perp_close")
        if perp_close is None:
            perp_close = self.params.get("perp_close")
        oi: Optional[pd.DataFrame] = kwargs.get("oi")
        if oi is None:
            oi = self.params.get("oi")
        if perp_close is None or perp_close.empty:
            # No perp close -> no basis signal. Return zero weights.
            return pd.DataFrame(0.0, index=prices.index,
                                columns=self._weight_columns(prices.columns))
        if oi is None or oi.empty:
            # No OI panel -> disable the OI conditioning (entry on
            # premium z-score alone, treated as a weaker signal).
            oi = None

        p = self.params
        idx = prices.index
        # The pipeline renames ``perp_close`` columns to the perp
        # leg convention (``BTC-USDT:USDT``) before passing them
        # to the strategy. Unit tests use the spot-slug form
        # (``BTC-USDT``). Normalise both to the spot-slug form
        # so the basis calc is ``perp - spot`` on aligned columns.
        spot_cols = list(prices.columns)
        perp_cols = [f"{c}:USDT" for c in spot_cols]
        if list(perp_close.columns) == perp_cols:
            perp_aligned = perp_close.copy()
            perp_aligned.columns = spot_cols
        else:
            perp_aligned = perp_close.reindex(columns=spot_cols)
        basis = (perp_aligned - prices) / prices
        basis_mean = basis.rolling(p["premium_lookback_bars"],
                                   min_periods=20).mean()
        basis_std = basis.rolling(p["premium_lookback_bars"],
                                  min_periods=20).std()
        z = (basis - basis_mean) / basis_std

        # Open-interest z-score (optional).
        if oi is not None:
            oi_aligned = oi.reindex(columns=prices.columns)
            oi_diff = oi_aligned.diff()
            oi_diff_mean = oi_diff.rolling(p["oi_lookback_bars"],
                                          min_periods=20).mean()
            oi_diff_std = oi_diff.rolling(p["oi_lookback_bars"],
                                          min_periods=20).std()
            oi_z = (oi_diff - oi_diff_mean) / oi_diff_std
        else:
            oi_z = pd.DataFrame(0.0, index=idx, columns=prices.columns)

        # Signal: +1 = long perp (perp cheap), -1 = short perp
        # (perp rich), 0 = flat. Entry when |z| > entry_z AND the
        # OI confirms. The signal persists in its last state
        # until the exit band triggers (|z| < exit_z), at which
        # point the position is flattened and the next bar is
        # back to flat waiting for a fresh entry.
        signal = pd.DataFrame(0.0, index=idx, columns=prices.columns)
        long_entry = (z < -p["entry_z"]) & (oi_z < -p["oi_min_z"])
        short_entry = (z > +p["entry_z"]) & (oi_z > +p["oi_min_z"])
        in_band = z.abs() < p["exit_z"]
        # The state machine is: enter on long/short, exit on
        # in_band, otherwise hold. To vectorise: we run a
        # per-column forward fill of the entry, then zero it on
        # the in_band bars.
        for col in prices.columns:
            entered = pd.Series(0.0, index=idx)
            entered[long_entry[col]] = +1.0
            entered[short_entry[col]] = -1.0
            entered = entered.replace(0.0, np.nan).ffill().fillna(0.0)
            entered[in_band[col]] = 0.0
            # Re-apply entries after the in-band exit (a fresh
            # entry on the same bar is allowed only when the
            # exit is followed by an entry; the ffill above
            # already kept 0 for bars after the exit).
            entered[long_entry[col] & in_band[col]] = +1.0
            entered[short_entry[col] & in_band[col]] = -1.0
            signal[col] = entered

        # Build the 2N-column weight frame: spot (= 0) + perp.
        spot_cols = list(prices.columns)
        perp_cols = [f"{c}:USDT" for c in spot_cols]
        all_cols = [c for pair in zip(spot_cols, perp_cols) for c in pair]
        w = pd.DataFrame(0.0, index=idx, columns=all_cols)
        for s_col, p_col in zip(spot_cols, perp_cols):
            if s_col in signal.columns:
                w[p_col] = signal[s_col] * p["max_gross"]
        return w

    @staticmethod
    def _weight_columns(spot_cols: pd.Index) -> list[str]:
        """Build the 2N weight frame column names from the spot cols."""
        return [c for pair in zip(spot_cols, [f"{c}:USDT" for c in spot_cols])
                for c in pair]
