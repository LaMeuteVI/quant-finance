"""X2 — Intraday signed-flow strategy on Binance spot aggTrades.

Preregistered 2026-10-20 (research/notes/2026-10-20-X2-prereg.md,
family ``intraday-signed-flow`` at n=1, QUEUE review 2026-10-21 item X2).

Q22 measured this signal descriptively and rejected it against a 60 bps
hurdle that its own preregistration had never written down. X2 re-tests
it as an actual tradeable rule at the real C1b cost of the venue traded,
so that the verdict turns on P&L rather than on a quintile table.

The rule, fixed in the preregistration:

* signal: bar ``t`` signed flow over total traded volume, in [-1, 1];
* entry: long above the trailing 80th percentile, short below the 20th;
* holding: ``hold_bars`` bars, one position at a time;
* hysteresis: after an exit the same side cannot be re-entered for
  ``hold_bars`` bars, so rank noise cannot re-shuffle the book;
* thresholds are trailing quantiles, not fixed bps cut-offs, so the
  rule does not encode 2022's volatility level into its parameters.

Causality: the quantile at bar ``t`` is computed from bars strictly
before ``t`` (shifted by one), so a bar's own value can only set its own
position, never its own threshold.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.strategies.base import Strategy


class IntradaySignedFlow(Strategy):
    """Trade the extremes of intraday taker-side signed flow."""

    name = "intraday_signed_flow"
    version = "1.0.0"
    hypothesis = (
        "Order-flow aggression predicts the next few bars: taker buying "
        "that is extreme relative to its own recent history pushes the "
        "price up over the holding horizon, and the reverse for taker "
        "selling. Q22 measured the effect at Spearman 0.13-0.27 with "
        "Kyle lambda t-stats of 16-47 on every axis, so the mechanism is "
        "not in doubt. What is in doubt is whether a 7-14 bps gross "
        "quintile spread can pay a 23-25 bps spot round trip. X2 "
        "preregistered to fail on that arithmetic."
    )

    default_params = {
        # Trailing window for the percentile thresholds.
        "quantile_lookback": 500,
        "quantile_min_periods": 250,
        # Upper / lower entry percentiles.
        "entry_high": 0.80,
        "entry_low": 0.20,
        # Bars to hold a position, and the matching re-entry lockout.
        "hold_bars": 3,
        # Gross exposure cap across the book.
        "max_gross": 1.0,
        # Minimum bars of history before the rule may emit a position.
        "min_history": 500,
        # Optional direct injection of the signal, for callers that have
        # already resampled the aggTrades (the pipeline passes it as a
        # kwarg; this is the fallback path).
        "signed_flow": None,
        "signed_flow_panel": None,
    }

    # ---- helpers ---------------------------------------------------------

    @staticmethod
    def signed_flow(aggtrades: pd.DataFrame) -> pd.Series:
        """Taker-side signed flow per bar, in [-1, +1].

        ``is_buyer_maker`` is True when the *buyer* was the maker, i.e.
        the aggressor was a seller. Taker buying is therefore
        ``~is_buyer_maker``: +1 for a fully taker-bought bar, -1 for a
        fully taker-sold one. Normalising by total volume makes the
        series comparable across the 2022 volatility regime and across
        the BTC and ETH books.
        """
        if aggtrades.empty:
            return pd.Series(dtype=float)
        q = pd.to_numeric(aggtrades["quantity"], errors="coerce").fillna(0.0)
        ibm = aggtrades["is_buyer_maker"].astype(bool)
        bar = aggtrades.index.get_level_values(0)
        frame = pd.DataFrame(
            {
                "signed": np.where(ibm, -q.to_numpy(), q.to_numpy()),
                "total": q.abs().to_numpy(),
            },
            index=pd.Index(bar),
        )
        grouped = frame.groupby(level=0).sum()
        denom = grouped["total"].replace(0.0, np.nan)
        out = grouped["signed"] / denom
        return out.replace([np.inf, -np.inf], np.nan).sort_index()

    def _thresholds(self, signal: pd.Series) -> tuple[pd.Series, pd.Series]:
        """Trailing quantile thresholds, shifted one bar for causality."""
        lookback = int(self.params["quantile_lookback"])
        minp = int(self.params["quantile_min_periods"])
        hi = signal.rolling(lookback, min_periods=minp).quantile(
            float(self.params["entry_high"])).shift(1)
        lo = signal.rolling(lookback, min_periods=minp).quantile(
            float(self.params["entry_low"])).shift(1)
        return hi, lo

    # ---- contract --------------------------------------------------------

    def target_weights(self, prices: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """Target weights from the aggTrades-derived signed-flow signal.

        ``prices`` is the close panel the engine marks against. The
        signal arrives as ``kwargs["signed_flow"]``, a Series already
        resampled to ``prices.index`` and indexed by column name, or as
        per-column frames in ``kwargs["signed_flow_panel"]``. Both are
        optional: with no signal the strategy holds nothing, because a
        missing signal is a flat book by definition, not a guess.
        """
        weights = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)

        panel = kwargs.get("signed_flow_panel")
        if panel is None:
            series = kwargs.get("signed_flow")
            if series is None:
                series = self.params.get("signed_flow")
            if series is None:
                return weights
            if isinstance(series, pd.Series):
                panel = series.to_frame(name=prices.columns[0])
            else:
                panel = series

        panel = panel.reindex(prices.index)
        hold = max(int(self.params["hold_bars"]), 1)
        cap = float(self.params["max_gross"])
        min_hist = int(self.params["min_history"])

        # The signal panel may be indexed by the plain slug while the
        # price panel is keyed by a (venue, symbol) tuple, or vice
        # versa. Positionally align the single-name case instead of
        # silently skipping on a label mismatch, which would leave the
        # book flat without a word.
        n_cols = len(prices.columns)
        if n_cols == 1 and panel.shape[1] == 1:
            aligned = {prices.columns[0]: panel.iloc[:, 0]}
        else:
            aligned = {c: panel[c] for c in prices.columns if c in panel.columns}

        for col, raw in aligned.items():
            s = raw.astype(float)
            s.index = prices.index
            hi, lo = self._thresholds(s)
            first = int(np.argmax(s.notna().values)) if s.notna().any() else -1
            if first < 0:
                continue
            # Warm-up is measured on the signal's own history, not on
            # the price index, so a late-arriving series still trades.
            warm = s.notna().cumsum().values
            sig = s.values
            hivals = hi.values
            lovals = lo.values
            w = np.zeros(len(s), dtype=float)
            i = first
            n = len(s)
            # ``blocked_until`` is the first bar on which a NEW position
            # may open. It is a time window, not a latch: an earlier
            # version compared against ``last_side`` and therefore never
            # allowed a second entry in the same direction for the whole
            # sample, which left the book in exactly three bars.
            blocked_until = 0
            while i < n:
                if warm[i] < min_hist or not np.isfinite(hivals[i]) or not np.isfinite(lovals[i]):
                    i += 1
                    continue
                side = 0
                if sig[i] >= hivals[i]:
                    side = 1
                elif sig[i] <= lovals[i]:
                    side = -1
                if side == 0 or i < blocked_until:
                    # Flat: no extreme, or still inside the post-exit
                    # lockout that stops rank noise re-shuffling the book.
                    i += 1
                    continue
                stop = min(i + hold, n)
                w[i:stop] = float(side) * (cap / max(n_cols, 1))
                blocked_until = stop
                i = stop
            weights[col] = w

        return weights
