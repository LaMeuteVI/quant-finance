"""Target-weight backtester with explicit execution lag, costs and funding.

Timing convention (the only one the desk uses):
  weights.loc[t] is decided with information up to and including the close of bar t.
  It is held over bars t+lag ... and earns close-to-close returns from there.
  lag >= 1 is enforced: lag 0 would trade on the close that produced the signal.

Costs are charged on drift-aware turnover: before rebalancing, yesterday's
weights have drifted with prices, and only the gap to the new target trades.

Funding (perps only): a positive rate means longs pay shorts, per bar held.
P2 added the ``perp_legs`` discriminator: funding is now applied only to
columns marked as perp, never to spot columns. A delta-neutral pair
(spot long + perp short on the same underlying) therefore charges funding
on the perp leg only, which is the economic reality.
"""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Protocol

import numpy as np
import pandas as pd

from aster.backtest.cost_model import ConstantCostModel


class _CostLike(Protocol):
    """Anything the engine can ask for a per-bar, per-symbol cost panel."""

    def per_trade_cost_bps(self, weights: pd.DataFrame, prices: pd.DataFrame,
                           AUM: float) -> pd.DataFrame: ...


def _to_cost_model(costs: "_CostLike | CostModel | None") -> _CostLike:
    """Adapt the legacy ``CostModel`` to the new panel interface.

    A scalar ``CostModel`` becomes a :class:`ConstantCostModel`; an
    already-panel model is returned as-is. ``None`` is the desk default
    (10 + 5 bps flat, see :class:`ConstantCostModel` defaults).
    """
    if costs is None:
        return ConstantCostModel()
    if isinstance(costs, CostModel):
        return ConstantCostModel(costs.fee_bps, costs.slippage_bps)
    return costs


def _normalise_perp_legs(perp_legs, columns: pd.Index) -> tuple[str, ...]:
    """Validate and freeze the perp-leg set against the weight frame columns.

    ``perp_legs`` may be ``None`` (no perp leg at all, every column treated as
    spot), an explicit iterable of symbols, or the sentinel ``"all"`` (every
    column treated as a perp; legacy behaviour for tests that don't care).
    Spot symbols are never in the funding column sum.
    """
    if perp_legs is None:
        return ()
    if perp_legs == "all":
        return tuple(columns)
    if isinstance(perp_legs, str):
        raise ValueError(
            f"perp_legs must be None, 'all', or an iterable of symbols; got {perp_legs!r}"
        )
    perp_set: tuple[str, ...] = tuple(perp_legs)
    unknown = [s for s in perp_set if s not in columns]
    if unknown:
        raise ValueError(
            f"perp_legs contains symbols not in the weight frame: {sorted(unknown)}"
        )
    return perp_set


@dataclass
class CostModel:
    fee_bps: float = 10.0        # taker fee per side
    slippage_bps: float = 5.0    # half-spread + impact per side

    def scaled(self, k: float) -> "CostModel":
        return CostModel(self.fee_bps * k, self.slippage_bps * k)

    @property
    def total_bps(self) -> float:
        return self.fee_bps + self.slippage_bps


@dataclass
class BacktestResult:
    returns: pd.Series            # net per-bar portfolio return
    gross_returns: pd.Series
    costs: pd.Series
    funding: pd.Series
    held: pd.DataFrame            # weights actually held during each bar
    turnover: pd.Series
    meta: dict = field(default_factory=dict)

    @property
    def equity(self) -> pd.Series:
        return (1 + self.returns).cumprod()


def run_backtest(prices: pd.DataFrame, weights: pd.DataFrame,
                 costs: "CostModel | _CostLike | None" = None,
                 lag: int = 1, funding: pd.DataFrame | None = None,
                 perp_legs: str | Iterable[str] | None = None,
                 AUM: float | None = None,
                 perp_close: pd.DataFrame | None = None,
                 perp_fixing_mask: pd.Series | None = None) -> BacktestResult:
    """Run a target-weight backtest with explicit lag, costs and (perp-only) funding.

    Parameters
    ----------
    prices : DataFrame
        Wide price panel (UTC index x symbols). Symbols missing from
        ``weights`` are ignored; symbols missing from ``prices`` cannot
        earn any return, only funding.
    weights : DataFrame
        Target weights. A positive value is a long, a negative value is
        a short, columns are per-leg (spot leg and perp leg carry
        distinct symbols).
    costs : CostModel, optional
        Costs per side. Default is 10 + 5 bps.
    lag : int, default 1
        Number of bars between signal and execution. Must be >= 1.
    funding : DataFrame, optional
        Funding-rate panel. The per-bar dollar charge on a column ``c`` is
        ``held[c] * funding[c]`` **only if** ``c`` is in ``perp_legs``;
        spot columns never pay funding.
    perp_legs : None, ``"all"`` or iterable of symbols
        Which columns of ``weights`` are perp legs and therefore pay
        funding. ``None`` (default) means no perp leg at all — the
        delta-neutral contract of P2. ``"all"`` is the legacy behaviour,
        kept for back-compat in tests. The intersection of ``perp_legs``
        with ``weights.columns`` is used; symbols listed in
        ``perp_legs`` but missing from ``weights`` raise ``ValueError``.
    """
    if lag < 1:
        raise ValueError("lag must be >= 1: a signal cannot trade on the bar that produced it")
    cost_model = _to_cost_model(costs)
    prices = prices.sort_index()
    # Reindex weights to (prices.index, union(prices.columns, weights.columns))
    # so the perp leg column survives: a delta-neutral book has BOTH
    # ``BTCUSDT`` and ``BTCUSDT:USDT`` columns in the weight frame, and
    # the engine must keep them both. The perp-leg's return is supplied
    # by ``perp_close`` (or zero, if the perp is on a hedge leg whose
    # return the engine doesn't need to model).
    all_cols = prices.columns.union(weights.columns)
    prices = prices.reindex(columns=all_cols)
    weights = weights.reindex(index=prices.index, columns=all_cols).fillna(0.0)

    perp_set = set(_normalise_perp_legs(perp_legs, weights.columns))

    # When ``perp_close`` is provided, the perp leg's per-bar return is
    # the perp close return (not the spot close return). The engine
    # otherwise assumes ``prices`` is the only return source and the
    # perp leg earns zero return — which is fine for unit tests of
    # funding-only P&L, but wrong for a real delta-neutral book where
    # the perp leg must be marked to its own price.
    if perp_close is not None:
        perp_rets = perp_close.sort_index().pct_change(fill_method=None)
        perp_rets = perp_rets.reindex(index=prices.index, columns=weights.columns)
        # Spot columns fall through to the spot return; perp columns
        # are overwritten by the perp return. Missing perp columns are
        # treated as zero (legacy fallback).
        merged = perp_rets.where(perp_rets.notna(), 0.0)
        rets = prices.pct_change(fill_method=None).where(
            prices.notna() & prices.shift(1).notna(), 0.0
        ).copy()
        perp_cols = [c for c in merged.columns if c in weights.columns]
        for c in perp_cols:
            rets[c] = merged[c]
    else:
        rets = prices.pct_change(fill_method=None)
    # A column is tradable when its price panel is present and the
    # bar is not the first row. The ``prices`` panel may be the spot
    # panel only — a perp leg's price comes from ``perp_close`` (or is
    # zero, when the perp is on a hedge leg whose return is irrelevant
    # because funding is the only P&L the strategy collects on it).
    # We therefore build ``tradable`` from the union of the two
    # price panels and the weight frame's column set; a perp leg
    # with no price is still tradable because the funding charge is
    # a per-bar cash flow that does not need a price to compute.
    price_source = prices.copy()
    if perp_close is not None:
        for c in perp_close.columns:
            if c not in price_source.columns:
                price_source[c] = perp_close[c]
    price_aligned = price_source.reindex(columns=weights.columns)
    # Tradable: present in either prices or perp_close, AND not the
    # first row of the panel.
    spot_leg_ok = price_aligned.notna()
    perp_leg_ok = pd.DataFrame(False, index=price_aligned.index, columns=price_aligned.columns)
    if perp_set:
        for c in perp_set:
            if c in perp_leg_ok.columns:
                perp_leg_ok[c] = True
    has_price = spot_leg_ok | perp_leg_ok
    tradable = has_price & has_price.shift(1).fillna(False)
    held = weights.shift(lag).fillna(0.0).where(tradable, 0.0)
    rets = rets.where(tradable, 0.0).fillna(0.0)

    gross = (held * rets).sum(axis=1)
    # weights after bar t's price move, before the next rebalance
    drifted = held * (1 + rets)
    denom = (1 + gross).replace(0, np.nan)
    drifted = drifted.div(denom, axis=0).fillna(0.0)
    turnover = (held - drifted.shift(1).fillna(0.0)).abs().sum(axis=1)
    # Per-bar, per-symbol cost in bps. The panel model needs an AUM to
    # know the order notional per turnover unit. Without AUM the desk
    # falls back to the scalar ``total_bps`` for back-compat with the
    # existing ledger tests; the new ``pipeline.run`` always passes AUM.
    if AUM is None or AUM <= 0:
        cost = turnover * cost_model.per_trade_cost_bps(
            weights, prices, 1.0).mean().mean() / 1e4
    else:
        cost_panel = cost_model.per_trade_cost_bps(weights, prices, AUM)
        per_leg_turnover = (held - drifted.shift(1).fillna(0.0)).abs()
        per_leg_cost = per_leg_turnover * cost_panel / 1e4
        cost = per_leg_cost.sum(axis=1)

    fund = pd.Series(0.0, index=prices.index)
    if funding is not None and perp_set:
        f = funding.reindex(index=prices.index, columns=weights.columns).fillna(0.0)
        # Only perp legs pay funding. Spot columns are zeroed out so the
        # held*funding sum cannot be polluted by a spot leg with a
        # forward-filled funding cell.
        perp_panel = f.copy()
        for col in f.columns:
            if col not in perp_set:
                perp_panel[col] = 0.0
        # Funding is the per-8h rate, announced at the 00/08/16 UTC
        # fixings and constant in between. Without a fixing mask, the
        # naive ``held * ffill(rate)`` would charge 8 bars' worth of
        # ``r`` instead of one — triple-counting the daily carry. When
        # ``perp_fixing_mask`` is given, the per-bar charge is
        # ``held * ffill(rate) * mask`` so the day-total equals
        # ``3 * r``. When ``perp_fixing_mask`` is None, the engine
        # keeps the legacy per-bar charge (the rate is treated as
        # already per-bar, e.g. for the 1d/4h legacy tests).
        if perp_fixing_mask is not None:
            mask = perp_fixing_mask.reindex(prices.index).fillna(0.0)
            fund = (held * perp_panel * mask.to_frame().values).sum(axis=1)
        else:
            fund = (held * perp_panel).sum(axis=1)
    # else: no perp leg in this book, funding is informational only and
    # is NOT subtracted from gross. (Legacy tests with perp_legs='all'
    # still apply funding to every column.)

    net = gross - cost - fund
    return BacktestResult(
        returns=net, gross_returns=gross, costs=cost, funding=fund, held=held, turnover=turnover,
        meta={"lag": lag, "AUM": AUM,
              "fee_bps": getattr(cost_model, "fee_bps", None),
              "slippage_bps": getattr(cost_model, "slippage_bps", None),
              "cost_model": type(cost_model).__name__,
              "perp_legs": sorted(perp_set)},
    )
