"""F1 — Funding carry, delta-neutral.

V1 (preregistered 2026-10-16, research/notes/2026-10-16-F1-prereg.md,
H-20261016-002, rejected on infrastructure: the pipeline did not
inject the funding panel into the strategy).

V2 (preregistered 2026-10-18, research/notes/2026-10-18-F1v2-prereg.md,
H-20261018-001/003). The infrastructure bottleneck is fixed: P6 wires the
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

V3 (preregistered 2026-10-19, research/notes/2026-10-19-F1v3-prereg.md,
R3 of QUEUE). Diagnosis (from `research/memos/2026-10-18-F1v2-N15.md`
§8): v1.1 used a fixed 2 bps/fixing signal threshold against a panel
whose unconditional mean is 1.23 bps/fixing, so the rule "predicted
funding > 2 bps" was effectively "funding persistently above its
mean + 0.77 bps", which is rarely true and barely identifiable with
vol-of-funding noise. V3 inverts the test:

  * amortised_round_trip_cost = (spot_fee_bps + perp_fee_bps + grid_bps)
                                * 2 / expected_holding_fixings
    (= 35 bps × 2 / 42 fixings ≈ 1.67 bps/fixing at the default hold).
  * entry (0→1): signal = mean_funding_lookback - amortised_cost > 0
                 AND funding_rate_now > 0
  * exit (1→0): funding_rate_now < 0 OR (funding has been ≤ 0 for
                 ``exit_persistence_bars`` consecutive bars).
  * NO inverse (no spot short) — when funding is negative, the rule
    is "stay flat" not "short spot / long perp". The Q5-V2 funding
    autocorrelation panel (autocorr 0.785) does not justify flipping
    on negative carry: it confirms persistence, not directional mean.

V3 also exposes the R1 decomposition: ``time_in_market`` is now reported
through the new ``pipeline.evaluate`` fields (gross_price_pnl_ann,
funding_pnl_ann, cost_pnl_ann, time_in_market, turnover_ann).
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
    """Long spot / short perp when the predicted funding clears the
    amortised round-trip cost, with hysteresis (V3).

    The prediction is the 7-day rolling mean of the funding rate.
    Entry requires both the rolling-mean signal AND the realised
    funding to be positive. Exit fires when the realised funding has
    been non-positive for ``exit_persistence_bars`` consecutive bars.
    V3 is long-only (no inverse when funding is negative) on the
    hypothesis that Q5-V2's 0.785 panel autocorrelation measures
    persistence, not directional mean.
    """

    name = "funding_carry_dn"
    version = "1.3.0"
    hypothesis = (
        "Crypto perpetual funding rates are persistent on horizons of hours to "
        "days. A delta-neutral long-spot / short-perp position earns the "
        "funding minus amortised round-trip costs when the predicted funding "
        "net of amortisation is positive. Entry: mean_funding_lookback - "
        "amortised_round_trip_cost > 0 AND funding_rate_now > 0. Exit: "
        "funding_rate_now < 0 OR funding_rate non-positive for "
        "exit_persistence_bars consecutive bars. No inverse side. Main risks "
        "are funding regime flips, basis blow-outs in crashes, and venue risk."
    )
    default_params = {
        "lookback_bars": 7 * 6,  # 7 days at 4h bars = 42
        # V3 cushion is now the amortised round-trip cost in bps/fixing.
        # Default 1.67 bps/fixing = (10+5+5 spot/perp/grid side-fee, both
        # sides, amortised over 42 fixings = 7 days expected hold).
        "amortised_round_trip_bps_per_fixing": 1.67,
        "exit_persistence_bars": 18,  # 3 days at 4h bars
        "expected_holding_fixings": 42,
        "basis_z_cap": 3.0,
        "max_gross": 1.0,
        "funding": None,
        "perp_close": None,
    }

    def target_weights(self, prices: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """Compute target weights for a delta-neutral funding-carry book
        with V3 entry/exit hysteresis.

        ``prices`` is the wide close panel indexed by the spot symbols
        (``BTCUSDT``). The funding panel is taken from
        ``kwargs["funding"]`` (preferred) or
        ``self.params.get("funding")`` (fallback) and is indexed by
        the perp symbols (``BTCUSDT:USDT``). The perp close panel
        (Q3b) is taken from ``kwargs["perp_close"]`` (preferred) or
        ``self.params.get("perp_close"]`` (fallback); it is indexed by
        the spot symbols so it shares the close panel's columns.
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
        amortised = p["amortised_round_trip_bps_per_fixing"] / 1e4
        # V3 signal:
        #   entry signal  = (predicted - amortised) > 0 AND fund_now > 0
        #   exit trigger  = (fund_now < 0) OR (fund non-positive for
        #                    exit_persistence_bars consecutive bars)
        signal_long = (predicted > amortised) & (fund > 0)
        # exit when current funding is negative, or non-positive for
        # ``exit_persistence_bars`` consecutive bars
        fund_nonpos = fund <= 0
        # rolling-sum of "non-positive" indicator over exit_persistence_bars;
        # if it equals the full window, exit
        nonpos_streak = fund_nonpos.rolling(
            p["exit_persistence_bars"], min_periods=1
        ).sum()
        exit_now = (fund < 0) | (nonpos_streak >= p["exit_persistence_bars"])
        # Build the held-state series: enter when signal_long True, exit
        # when exit_now True, hold otherwise.
        # Implementation: cumulative state machine per column.
        held = pd.DataFrame(False, index=idx, columns=prices.columns)
        for col in prices.columns:
            in_pos = False
            for t in idx:
                if not in_pos and bool(signal_long.at[t, col]):
                    in_pos = True
                elif in_pos and bool(exit_now.at[t, col]):
                    in_pos = False
                held.at[t, col] = in_pos
        # V3 basis guard (carried over from v1.1): z-score of
        # (perp - spot)/spot over 30 bars above cap blocks entries.
        # V1 used the spot return z-score, which is a different signal
        # and a worse crash proxy. If the perp close panel is missing
        # we fall back to the V1 spot-return z-score.
        if p["basis_z_cap"] is not None and len(idx) > 30:
            if perp_close is not None and not perp_close.empty:
                basis_source = perp_close.reindex(columns=prices.columns)
                if basis_source.notna().sum().sum() > 0:
                    basis = (basis_source - prices) / prices
                    basis_mean = basis.rolling(30, min_periods=5).mean()
                    basis_std = basis.rolling(30, min_periods=5).std()
                    z = (basis - basis_mean) / basis_std
                    block = z.abs() > p["basis_z_cap"]
                    held = held & ~block
            else:
                z = (prices - prices.rolling(30).mean()) / prices.rolling(30).std()
                block = z.abs() > p["basis_z_cap"]
                held = held & ~block
        # Build the 2N-column weight frame: spot + perp with opposite sign.
        spot, perp, all_cols = _spot_perp_columns(list(prices.columns))
        w = pd.DataFrame(0.0, index=idx, columns=all_cols)
        for s_col, p_col in zip(spot, perp):
            if s_col in held.columns:
                w[s_col] = held[s_col].astype(float) * p["max_gross"]
                w[p_col] = -held[s_col].astype(float) * p["max_gross"]
        return w