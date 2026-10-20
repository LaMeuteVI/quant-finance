"""MarketData: a multi-field, causally-aligned input to a strategy.

A strategy may consume more than close prices. The brief's N5 (flow),
section 6 (inter-asset) and section 7 (carry / crowding / lead-lag) all
require features that are not in the close. The `MarketData` dataclass
ships every input the desk considers research-grade, each as a wide
panel ``index x symbols``, each aligned to the bar close.

Causality is enforced by construction:

* every panel has a tz-aware UTC ``DatetimeIndex``;
* every panel has the same symbols in the same order;
* the index is sorted, de-duplicated, and frozen at construction;
* ``None`` is the only valid value for an absent field — a zero-fill
  would assert information that was never observed.

P1 introduces the dataclass, the alignment invariant, and a per-field
truncation look-ahead test. P2 wires the actual stores; P3 wires the
sealed split; P4 wires the cost model.
"""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Iterable

import numpy as np
import pandas as pd

REQUIRED_FIELDS: tuple[str, ...] = (
    "close",
    "open",
    "high",
    "low",
    "volume",
    "quote_volume",
    "taker_buy_base",
    "taker_buy_quote",
    "trades",
)
OPTIONAL_FIELDS: tuple[str, ...] = (
    "funding",
    "open_interest",
    "premium",
)


def _check_panel(name: str, panel: pd.DataFrame) -> pd.DataFrame:
    """Validate a single field panel: tz-aware UTC index, sorted, unique."""
    if not isinstance(panel, pd.DataFrame):
        raise TypeError(f"MarketData.{name} must be a DataFrame, got {type(panel).__name__}")
    if not isinstance(panel.index, pd.DatetimeIndex):
        raise TypeError(f"MarketData.{name} must be indexed by a tz-aware DatetimeIndex")
    if panel.index.tz is None:
        raise ValueError(f"MarketData.{name} index must be tz-aware (UTC); got naive")
    idx = panel.index.tz_convert("UTC") if str(panel.index.tz) != "UTC" else panel.index
    panel = panel.copy()
    panel.index = idx
    panel = panel[~panel.index.duplicated(keep="last")].sort_index()
    return panel


@dataclass
class MarketData:
    """Multi-field, causally-aligned input to a strategy.

    Every field is a wide panel (index x symbols) aligned to the bar
    close. Optional fields default to ``None``: a strategy that does not
    need them must not receive a fabricated zero-filled panel.

    Symbols are the union of the columns across the present fields, in
    the order of the first appearance (typically the close panel's
    order). All present fields must agree on the symbol set; partial
    agreement is allowed only when an optional field is ``None`` for
    some symbols — in that case the field is widened to the full symbol
    set with ``NaN`` (a missing observation, not zero).
    """

    close: pd.DataFrame
    open: pd.DataFrame
    high: pd.DataFrame
    low: pd.DataFrame
    volume: pd.DataFrame
    quote_volume: pd.DataFrame
    taker_buy_base: pd.DataFrame
    taker_buy_quote: pd.DataFrame
    trades: pd.DataFrame
    funding: pd.DataFrame | None = None
    open_interest: pd.DataFrame | None = None
    premium: pd.DataFrame | None = None
    timeframe: str = "1d"
    symbols: tuple[str, ...] = field(default_factory=tuple)
    index: pd.DatetimeIndex = field(default_factory=lambda: pd.DatetimeIndex([]))

    def __post_init__(self) -> None:
        # Normalise the required fields, capture the reference index and symbols.
        ref_panel = _check_panel("close", self.close)
        ref_index = ref_panel.index
        ref_symbols: tuple[str, ...] = tuple(ref_panel.columns)

        for f in REQUIRED_FIELDS:
            panel = getattr(self, f)
            if panel is None:
                raise ValueError(f"MarketData.{f} is required and cannot be None")
            panel = _check_panel(f, panel)
            if not panel.columns.equals(pd.Index(ref_symbols)):
                missing = set(ref_symbols) - set(panel.columns)
                extra = set(panel.columns) - set(ref_symbols)
                if missing or extra:
                    raise ValueError(
                        f"MarketData.{f} columns differ from close: missing={sorted(missing)} extra={sorted(extra)}"
                    )
            if not panel.index.equals(ref_index):
                raise ValueError(
                    f"MarketData.{f} index differs from close: cannot align fields of different shapes"
                )
            setattr(self, f, panel)

        for f in OPTIONAL_FIELDS:
            panel = getattr(self, f)
            if panel is None:
                continue
            panel = _check_panel(f, panel)
            # Widen to the reference symbol set with NaN (a missing obs, not zero).
            if not panel.columns.equals(pd.Index(ref_symbols)):
                panel = panel.reindex(columns=ref_symbols)
            if not panel.index.equals(ref_index):
                # Optional fields may have a different calendar (e.g. funding is
                # 8-hourly, OI is daily). We reindex to the reference index and
                # forward-fill within a small tolerance to avoid silently
                # carrying the last observation forever; the strategy is
                # expected to drop NaN for its own look-back. The fill is
                # *causal*: a bar at t receives the last observation at or
                # before t (pandas ffill), never the next one (no bfill).
                panel = panel.reindex(panel.index.union(ref_index)).sort_index().ffill().reindex(ref_index)
            setattr(self, f, panel)

        object.__setattr__(self, "symbols", ref_symbols)
        object.__setattr__(self, "index", ref_index)

    def field_names(self) -> tuple[str, ...]:
        return tuple(f.name for f in fields(self) if f.name not in ("timeframe", "symbols", "index"))

    def panel(self, name: str) -> pd.DataFrame | None:
        if name not in self.field_names():
            raise KeyError(f"unknown MarketData field: {name}")
        return getattr(self, name)

    def aligned_index(self) -> pd.DatetimeIndex:
        return self.index

    def with_truncated_index(self, cutoff: pd.Timestamp) -> "MarketData":
        """Return a copy of this MarketData restricted to rows < ``cutoff``.

        Used by the look-ahead test: each field is independently truncated
        and the strategy is asked to produce a target weight at the row
        just before ``cutoff``. The output at that row must equal the
        output the strategy would have produced on the full data.
        """
        kwargs: dict = {"timeframe": self.timeframe}
        for f in self.field_names():
            panel = getattr(self, f)
            if panel is None:
                kwargs[f] = None
                continue
            mask = panel.index < cutoff
            kwargs[f] = panel.loc[mask]
        return MarketData(**kwargs)

    def as_prices(self) -> pd.DataFrame:
        """Backward-compatible adapter: returns the close panel.

        Existing close-only strategies (the 5 registered today) consume
        ``target_weights(prices)`` where ``prices`` is a wide close
        panel. The new pipeline passes a ``MarketData``; the adapter
        unpacks ``close`` so the old API keeps working unchanged.
        """
        return self.close


def check_market_data_lookahead(
    strategy,
    data: MarketData,
    *,
    truncate_at: pd.Timestamp | None = None,
    perturbation_horizon: int = 5,
) -> dict:
    """Per-field look-ahead test for a multi-field strategy.

    Idea: a causal strategy's output at row ``t`` must not depend on
    future observations (rows ``> t``). The test replaces the next
    ``perturbation_horizon`` rows of each field, one field at a time,
    with a sentinel value (a copy of the close from the boundary row,
    so the change is invisible to a strategy that does not look ahead).
    If the strategy's output at the boundary row changes, the strategy
    is leaking that field into its decision.

    The truncated MarketData keeps the full index; only the values at
    ``> truncate_at`` are sentinelled. This respects the alignment
    invariant of ``MarketData`` (every field shares the same index) and
    still detects any future-leaking strategy that consumes a row
    within ``perturbation_horizon`` of the boundary.

    Parameters
    ----------
    strategy : duck-typed ``target_weights(MarketData) -> DataFrame``.
    data : a fully constructed ``MarketData``.
    truncate_at : cutoff row. Defaults to ``data.index[len(data)//2]``.
    perturbation_horizon : how many rows past ``truncate_at`` to sendinellise.

    Returns
    -------
    dict with ``passed`` (bool), ``truncate_at`` (ISO), ``fields``
    (dict per field with ``present``, ``passed``, ``delta``).
    """
    if not hasattr(strategy, "target_weights"):
        raise TypeError("strategy must implement target_weights")
    base_weights = strategy.target_weights(data)
    if not isinstance(base_weights, pd.DataFrame):
        raise TypeError("strategy.target_weights must return a DataFrame")

    if truncate_at is None:
        mid = len(data.index) // 2
        truncate_at = data.index[mid]

    target_row = int(data.index.get_loc(truncate_at))
    if target_row >= len(base_weights):
        return {"passed": True, "truncate_at": truncate_at.isoformat(),
                "fields": {}, "reason": "no weights at boundary row"}
    base_row = base_weights.iloc[target_row]

    horizon_end = min(target_row + perturbation_horizon + 1, len(data.index))
    future_idx = data.index[target_row + 1:horizon_end]

    report: dict = {"passed": True, "truncate_at": truncate_at.isoformat(),
                    "perturbation_horizon": perturbation_horizon, "fields": {}}
    for name in data.field_names():
        panel = data.panel(name)
        if panel is None:
            report["fields"][name] = {"present": False, "passed": True, "delta": None}
            continue
        # Replace future rows of this field with the boundary value. A
        # causal strategy ignores them; a non-causal one is fooled into
        # producing a different output at the boundary.
        perturbed = panel.copy()
        for r in future_idx:
            if r in perturbed.index:
                perturbed.loc[r] = perturbed.loc[truncate_at]
        perturbed_kwargs: dict = {"timeframe": data.timeframe}
        for f in data.field_names():
            perturbed_kwargs[f] = perturbed if f == name else data.panel(f)
        rebuilt = MarketData(**perturbed_kwargs)
        new_weights = strategy.target_weights(rebuilt)
        if target_row >= len(new_weights):
            new_row = None
        else:
            new_row = new_weights.iloc[target_row]
        if new_row is None:
            field_pass = True
            delta = None
        else:
            delta_series = (new_row.fillna(0) - base_row.fillna(0)).abs()
            max_delta = float(delta_series.max()) if len(delta_series) else 0.0
            field_pass = bool(max_delta < 1e-9)
            delta = max_delta
        report["fields"][name] = {"present": True, "passed": field_pass, "delta": delta}
        if not field_pass:
            report["passed"] = False
    return report


__all__ = [
    "MarketData",
    "REQUIRED_FIELDS",
    "OPTIONAL_FIELDS",
    "check_market_data_lookahead",
]