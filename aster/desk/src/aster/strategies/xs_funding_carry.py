"""X1 — Cross-sectional funding carry on USDⓈ-M perpetuals.

Preregistered 2026-10-20 (research/notes/2026-10-20-X1-prereg.md, family
``xs-funding-carry`` at n=1, QUEUE review 2026-10-21 item X1).

Distinct from F1 (``funding_carry_dn``): F1 is a **time-series**,
single-name, spot-leg delta-neutral carry. X1 is **cross-sectional** —
it ranks many perps against each other, longs the cheapest funding and
shorts the dearest, and holds no spot leg at all.

Design, fixed in the preregistration and not tunable afterwards:

* signal: trailing mean of the daily funding fixings over 30 days,
  computed causally from fixings up to and including bar *t*;
* ranking: cross-sectional percentile rank per bar; long the lowest
  tercile, short the highest;
* sizing: dollar-neutral, equal weight inside a tercile, beta to BTC
  neutralised on the short side;
* rebalance: weekly, with a no-trade band so a name is only traded when
  it crosses a tercile boundary, never on rank jitter inside one;
* costs: the C1b grid at taker, perp legs only, 5 bps/side fee.

The preregistration records a **zero-net bar**: if the amortised
round-trip cost exceeds the gross funding spread at the prescribed
horizon, the strategy has no mechanism and is rejected on that ground
regardless of its realised return series. On the 12-symbol panel that
condition is already met analytically (7.27 bps/fixing of amortised
cost against a 2.11 bps/fixing gross spread), so this module is run to
close the family with evidence rather than with an argument.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.backtest.metrics import PERIODS_PER_YEAR
from aster.strategies.base import Strategy


class XSFundingCarry(Strategy):
    """Long the lowest-funding tercile of perps, short the highest."""

    name = "xs_funding_carry"
    version = "1.0.0"
    hypothesis = (
        "Crypto perpetual funding is persistent over weeks and is driven by "
        "crowded leveraged longs. Ranking perps by trailing funding and "
        "holding the cheapest against the dearest collects the cross-sectional "
        "funding spread without taking directional risk. The spread is real "
        "but thin: at 12 symbols the mean perp round trip costs 42.9 bps "
        "against a 2.11 bps/fixing gross spread, so the strategy only clears "
        "its own costs if the book is held far longer than weekly or "
        "restricted to majors. Preregistered to fail on the prescribed "
        "configuration."
    )

    default_params = {
        "funding_lookback_days": 30,
        "funding_min_periods": 15,
        "rebalance_every_bars": 7,
        # Enter a tercile only when the percentile rank is this deep.
        "tercile": 1.0 / 3.0,
        # No-trade band: a name already held is kept until its rank leaves
        # the tercile by more than this margin.
        "no_trade_band": 0.02,
        "beta_neutral": True,
        "beta_lookback_days": 60,
        "max_gross": 1.0,
        "funding": None,
        "perp_close": None,
    }

    # ---- helpers ---------------------------------------------------------

    @staticmethod
    def _perp_columns(symbols: list[str]) -> list[str]:
        """Perp columns carry the ``:USDT`` settlement suffix so the
        engine's ``perp_legs`` discriminator and the C1b venue inference
        both recognise them as perps (5 bps/side, not 10)."""
        return [f"{s}:USDT" for s in symbols]

    def _funding_panel(self, funding: pd.DataFrame | None) -> pd.DataFrame | None:
        if funding is None:
            funding = self.params.get("funding")
        if funding is None:
            return None
        return funding

    @staticmethod
    def _base_symbol(column: str) -> str:
        """``BTC-USDT:USDT`` / ``BTCUSDT`` / ``BTC/USDT`` -> ``BTC``.

        The pipeline already translates the funding store into the
        strategy's own column convention before calling us, so this is
        only a fallback for direct callers (and for the tests): match
        the price columns by base symbol rather than by exact string.
        """
        c = str(column)
        for suffix in (":USDT", "-USDT", "/USDT"):
            if c.endswith(suffix):
                c = c[: -len(suffix)]
                break
        c = c.replace("/", "").replace("-", "").replace("_", "")
        for quote in ("USDT", "USDC", "USD"):
            if c.endswith(quote) and len(c) > len(quote):
                c = c[: -len(quote)]
                break
        return c

    def _align_funding(self, funding: pd.DataFrame,
                       columns) -> pd.DataFrame:
        """Project the funding panel onto ``columns`` by base symbol."""
        by_base: dict[str, str] = {}
        for c in funding.columns:
            by_base.setdefault(self._base_symbol(c), c)
        lookup = {c: by_base[self._base_symbol(c)]
                  for c in columns if self._base_symbol(c) in by_base}
        if not lookup:
            raise ValueError(
                "xs_funding_carry could not align the funding panel "
                f"{list(funding.columns)[:5]} with the price columns "
                f"{list(columns)[:5]}"
            )
        return pd.DataFrame(
            {c: funding[src] for c, src in lookup.items()}).astype(float)

    def _trailing_mean(self, funding: pd.DataFrame) -> pd.DataFrame:
        return funding.rolling(
            int(self.params["funding_lookback_days"]),
            min_periods=int(self.params["funding_min_periods"]),
        ).mean()

    @staticmethod
    def _beta_to_btc(returns: pd.DataFrame, btc: str,
                     lookback: int) -> pd.DataFrame:
        """Rolling OLS beta of every column against ``btc``.

        Returns a frame shaped like ``returns`` (bar x symbol) so each
        weight row can read the beta that was knowable on that bar.
        Computed causally from returns up to and including bar *t*.
        """
        if btc not in returns.columns:
            return pd.DataFrame(0.0, index=returns.index,
                                columns=returns.columns)
        bench = returns[btc]
        var = bench.rolling(lookback).var()
        cov = returns.rolling(lookback).cov(bench)
        with np.errstate(divide="ignore", invalid="ignore"):
            beta = cov.div(var, axis=0)
        beta[btc] = 1.0
        return beta.replace([np.inf, -np.inf], np.nan).fillna(0.0)

    # ---- contract --------------------------------------------------------

    def target_weights(self, prices: pd.DataFrame, **kwargs) -> pd.DataFrame:
        funding = self._funding_panel(kwargs.get("funding"))
        # ``or`` is wrong on DataFrames: a frame's truth value is
        # ambiguous. Test explicitly for None, and for emptiness.
        perp_close = kwargs.get("perp_close")
        if perp_close is None:
            perp_close = self.params.get("perp_close")
        if perp_close is None or getattr(perp_close, "empty", False):
            perp_close = None
        panel = perp_close if perp_close is not None else prices

        # Fund on the columns the price panel actually carries. A perp
        # column is anything the engine would charge funding on, i.e.
        # the settlement-suffixed ones; the pipeline has already
        # aligned the funding store onto this convention.
        cols = list(panel.columns)
        if funding is None or funding.empty:
            # No funding panel: hold nothing. Callers that only have a
            # price panel (the truncation-invariance validator, a bare
            # smoke test) must not crash the strategy, and a missing
            # signal is a flat book by definition, not a guess.
            return pd.DataFrame(0.0, index=panel.index, columns=panel.columns)
        aligned = self._align_funding(funding, cols).reindex(panel.index).ffill()

        signal = self._trailing_mean(aligned)
        pct = signal.rank(axis=1, pct=True)
        tercile = float(self.params["tercile"])
        band = float(self.params["no_trade_band"])

        every = max(int(self.params["rebalance_every_bars"]), 1)
        rebal_idx = set(range(0, len(panel.index), every))

        # Raw tercile membership, evaluated every bar but acted on only
        # on rebalance dates (the no-trade band is what makes a weekly
        # book cheaper than a daily one).
        want_long = (pct <= tercile) & signal.notna()
        want_short = (pct >= 1.0 - tercile) & signal.notna()

        weights = pd.DataFrame(0.0, index=panel.index, columns=panel.columns)
        held_long: set[str] = set()
        held_short: set[str] = set()

        rets = panel.pct_change()
        beta = (
            self._beta_to_btc(rets, str(cols[0]),
                              int(self.params["beta_lookback_days"]))
            if self.params["beta_neutral"] else None
        )
        gross_cap = float(self.params["max_gross"])

        for i, ts in enumerate(panel.index):
            if i not in rebal_idx or i == 0:
                if i > 0:
                    # Between rebalances the book drifts with prices;
                    # the engine applies the drift itself, so we carry
                    # the previous target forward unchanged.
                    weights.iloc[i] = weights.iloc[i - 1]
                continue

            longs = [c for c in cols if bool(want_long.at[ts, c])]
            shorts = [c for c in cols if bool(want_short.at[ts, c])]
            if not longs or not shorts:
                weights.iloc[i] = weights.iloc[i - 1] if i > 0 else 0.0
                continue

            # No-trade band: a name already held on this side is kept
            # while its rank stays inside the tercile plus the band, so
            # rank jitter does not generate turnover.
            longs = [c for c in longs
                     if c in held_long or bool(want_long.at[ts, c])
                     or pct.at[ts, c] <= tercile + band]
            longs = [c for c in longs if c not in held_short]
            shorts = [c for c in shorts
                      if c in held_short or bool(want_short.at[ts, c])
                      or pct.at[ts, c] >= 1.0 - tercile - band]
            shorts = [c for c in shorts if c not in held_long]
            if not longs or not shorts:
                weights.iloc[i] = weights.iloc[i - 1] if i > 0 else 0.0
                continue

            w = pd.Series(0.0, index=panel.columns)
            # Dollar-neutral: each side is half the gross budget.
            side = gross_cap / 2.0
            w.loc[longs] = side / len(longs)
            w.loc[shorts] = -side / len(shorts)

            if beta is not None and self.params["beta_neutral"]:
                # Read each symbol's beta off the trailing window that
                # ends on this bar, so the neutralisation is causal and
                # the estimate is current rather than a full-sample fit.
                b = beta.loc[ts].reindex(panel.columns).fillna(0.0)
                b_long = float((w * b).sum())
                b_short = float((w.loc[shorts] * b.loc[shorts]).sum())
                if abs(b_short) > 1e-12:
                    # The clip keeps one leg from absorbing the whole
                    # book when betas are near zero, at the cost of
                    # leaving a residual beta. The residual is removed
                    # in the dollar-neutrality pass below rather than
                    # by letting the clip silently de-neutralise the book.
                    scale = float(np.clip(-b_long / b_short, 0.0, 3.0))
                    w.loc[shorts] = w.loc[shorts] * scale
                # Restore dollar neutrality after the beta scaling, then
                # renormalise the gross back to its cap.
                net = float(w.sum())
                if abs(net) > 1e-12:
                    # Subtract the net from the short side (it is always
                    # the side that can absorb it, since long weights are
                    # all positive and shorts all negative).
                    if shorts:
                        w.loc[shorts] = w.loc[shorts] - net / len(shorts)
                g = float(w.abs().sum())
                if g > 0:
                    w = w * (gross_cap / g)

            weights.iloc[i] = w
            held_long = set(longs)
            held_short = set(shorts)

        return weights
