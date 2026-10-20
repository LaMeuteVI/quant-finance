"""F3 — Vol-targeted trend ensemble on the panel.

Preregistered 2026-10-18, research/notes/2026-10-18-F3-prereg.md.

Trend-following on a cross-section of crypto perps. The signal on
each asset is the sign of a 20/60/120-day blended average return;
positions are sized to a 10 % annual volatility target per asset
and the gross book is capped at 1.5x.

V1.0.0 differs from the rejected H-20261013-001 in three ways:
- 8-10 assets (was: BTC only)
- Long AND short perps (was: long-only / cash)
- Vol targeting (was: full-gross)

The family is ``btc-daily-tsmom``. DSR counts the prior
H-20261013-001 trial as trial 1; F3 v1.0.0 is trial 2.
"""
from __future__ import annotations

from typing import Iterable, Optional

import numpy as np
import pandas as pd

from aster.strategies.base import Strategy


class VolTargetTrendEnsemble(Strategy):
    """Cross-section trend with per-asset vol targeting."""

    name = "vol_target_trend_ensemble"
    version = "1.1.0"
    hypothesis = (
        "A blended 20/60/120-day trend signal across 8-10 liquid "
        "crypto perps, sized to a 10% annual volatility target per "
        "asset and gross-capped at 1.5x, captures the cross-section "
        "of trend persistence while controlling the drawdowns that "
        "killed the BTC-only long-only version (H-20261013-001). "
        "V1.1 reduces turnover by (a) a no-trade band of "
        "rebalance_band_target (default 0.02) on the target weights "
        "(a column whose new target moves less than the band keeps "
        "the previous bar's weight), (b) a longer vol half-life "
        "(vol_lookback_days 60 -> 180, EMA-style), and (c) a "
        "weekly rebalance floor (rebalance_every_n_bars, default 7) "
        "so the book does not churn every day."
    )
    default_params = {
        "timeframe": "1d",
        # 20/60/120 day lookbacks blended equally.
        "lookbacks": [20, 60, 120],
        # Re-entry check: a 5-day return that agrees with the
        # slow trend re-arms the position after an exit.
        "re_entry_lookback": 5,
        # Per-asset vol target.
        "vol_target_ann": 0.10,
        # V1.1: longer vol window (60 -> 180 days) for stability.
        "vol_lookback_days": 180,
        # Max gross exposure across the book.
        "gross_cap": 1.5,
        # Min history before the strategy emits a non-zero weight.
        "min_history": 120,
        # V1.1: no-trade band on target weights (fraction of |w|).
        "rebalance_band_target": 0.02,
        # V1.1: minimum holding period in bars (weekly rebalance).
        "rebalance_every_n_bars": 7,
    }

    def target_weights(self, prices: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """Compute the vol-targeted trend weights.

        ``prices`` is the wide spot close panel (idx x symbols).
        Returns a wide weight DataFrame indexed like ``prices`` with
        perp-leg columns ``[BTC-USDT:USDT, ...]`` (the engine treats
        these as perps via ``perp_legs`` in the prereg). The spot
        leg is held flat (always 0) because the strategy is long/short
        perps only.
        """
        p = self.params
        idx = prices.index
        spot_cols = list(prices.columns)
        perp_cols = [f"{c}:USDT" for c in spot_cols]

        # 1. Trend signal: sign(blended rolling mean) on log returns.
        log_ret = np.log(prices / prices.shift(1))
        # Each lookback produces a 0/+1/-1 signal. We blend by
        # averaging the three normalised signals and re-thresholding.
        sig = pd.DataFrame(0.0, index=idx, columns=spot_cols)
        n_look = len(p["lookbacks"])
        for L in p["lookbacks"]:
            avg = log_ret.rolling(L, min_periods=L // 2).mean()
            sig = sig.add(np.sign(avg).fillna(0.0) / n_look)
        # Re-arm rule: if the slow trend is positive but the most
        # recent 5-day return is strongly negative, we let the
        # position be flat for one bar (the trend has likely
        # flipped). Implemented as: subtract the 5-day signal.
        if p["re_entry_lookback"] and p["re_entry_lookback"] > 0:
            fast = log_ret.rolling(p["re_entry_lookback"],
                                   min_periods=1).mean()
            sig = sig - np.sign(fast).fillna(0.0) / n_look
        sig = sig.clip(-1.0, 1.0)

        # 2. Vol targeting. We use a 60-day rolling vol of the
        # *spot* log returns as the proxy for the asset's risk
        # (the perp return is spot + funding noise, dominated
        # by spot on the daily horizon).
        vol_daily = log_ret.rolling(p["vol_lookback_days"],
                                    min_periods=20).std()
        vol_ann = vol_daily * np.sqrt(365)
        # Per-asset scale = vol_target / vol_ann. Cap at 3.0 to
        # avoid blow-ups when vol collapses (BTC in late 2018).
        scale = (p["vol_target_ann"] / vol_ann).clip(upper=3.0)

        # 3. Combine: weight = sign(blended_trend) * scale.
        raw_w = sig * scale
        # Cap the gross: total |w| <= gross_cap.
        gross = raw_w.abs().sum(axis=1)
        gross_factor = (p["gross_cap"] / gross).where(gross > p["gross_cap"], 1.0)
        scaled = raw_w.mul(gross_factor, axis=0)
        # Suppress weights before min_history is reached.
        history = prices.notna().cumsum().iloc[:, 0]
        cold_start = history < p["min_history"]
        scaled.loc[cold_start, :] = 0.0

        # 4. V1.1: No-trade band + weekly rebalance floor on the
        # perp weights. Without this the strategy re-issues the full
        # target every day; with 31x/y on v1.0.0 the net Sharpe was
        # 0.702 and DSR 0.907. The band suppresses noise-level
        # weight changes; the rebalance_every_n_bars ensures the
        # book does not churn intraday even when the band would
        # permit a re-issue.
        #
        # ``scaled`` at this point is indexed by spot_cols (BTC-USDT,
        # etc.). The rebalance state machine operates on the spot
        # columns; we then mirror the result onto the perp legs in
        # the final assembly step below.
        band = float(p.get("rebalance_band_target", 0.02))
        rebal_every = int(p.get("rebalance_every_n_bars", 7))
        if band > 0 or rebal_every > 1:
            n = len(idx)
            update_mask = pd.Series(
                [(i % rebal_every) == 0 for i in range(n)], index=idx
            )
            smoothed = pd.DataFrame(0.0, index=idx, columns=spot_cols)
            last = pd.Series(0.0, index=spot_cols)
            for i, t in enumerate(idx):
                if update_mask.iloc[i]:
                    last = scaled.iloc[i].fillna(0.0)
                smoothed.loc[t] = last.values
            # No-trade band: keep the held weight when the new
            # target moves by less than ``band * |held|``.
            band_applied = smoothed.copy()
            prev = pd.Series(0.0, index=spot_cols)
            for t in idx:
                new = smoothed.loc[t]
                delta = (new - prev).abs()
                rel = delta / prev.abs().replace(0, np.nan)
                keep = (rel < band) & (prev.abs() > 0)
                out = new.where(~keep, prev)
                band_applied.loc[t] = out.fillna(new).values
                prev = out.fillna(0.0)
            scaled = band_applied

        # 5. Build the 2N-column frame: spot (= 0) + perp.
        all_cols = [c for pair in zip(spot_cols, perp_cols) for c in pair]
        w = pd.DataFrame(0.0, index=idx, columns=all_cols)
        for s_col, p_col in zip(spot_cols, perp_cols):
            if s_col in scaled.columns:
                w[p_col] = scaled[s_col]
        return w

    @staticmethod
    def _weight_columns(spot_cols: pd.Index) -> list[str]:
        return [c for pair in zip(spot_cols, [f"{c}:USDT" for c in spot_cols])
                for c in pair]
