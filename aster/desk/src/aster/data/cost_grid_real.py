"""The desk's cost grid: two execution scenarios, calibrated on real spreads.

Run: ``uv run python -m aster.data.cost_grid_real``

**What changed and why.**  The earlier grid priced the spread with high-low
estimators (Corwin-Schultz, Abdi-Ranaldo, Roll).  Those were built for equities
at 5-50 bps spreads on daily bars.  On crypto they measure **bar volatility,
not spread**: on 1h BTC bars they returned 14-27 bps while the real spread,
measured on the trade tape, is 0.003 bps.  The tell was in the data -- the
"spread" peaked exactly when volatility peaked (Europe/US hours), which is the
signature of a variance measurement wearing a spread's clothes.

Measured on Binance Vision aggTrades, June 2024 (27.8 M trades for BTC):

    asset   spread (bps)   ticks   high-low estimator said
    BTC         0.003      1.7    14-27 (hourly bars)
    ETH         0.045      1.6    ~
    BNB         3.118     18.8    ~
    SOL         1.083      1.6    ~
    XRP         3.791      1.9    ~
    DOGE        1.458      2.0    ~

The grid below therefore uses the **measured** spread, and the high-low
estimators are kept only as an upper bound for illiquid names where no tape
was available.

Two scenarios are priced separately because they have opposite economics:

* **taker** -- pays the spread plus 10 bps per side (Binance spot taker, the
  desk's real tier).  Reliable fill, expensive.
* **maker** -- pays only the fee (1 bps per side on the desk's tier) and earns
  the spread, but only if the order fills.  The grid cannot know the fill
  rate, so the maker cost is reported *net of nothing*: it is a floor, and
  every candidate that relies on it must carry its own fill assumption.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import pandas as pd

BPS = 1e4

# Desk's real fee tier, from config/desk.yaml.  That file defines ONE number:
#   costs.fee_bps: 10   # taker, per side
# It does NOT define a maker fee.  Rather than assume the published Binance VIP-0
# 25 % maker discount -- which may not be the tier this account actually holds --
# the maker fee is left as None and the maker scenario is reported as *pending
# confirmation*.  A fee number invented from a public schedule is exactly the
# kind of unsupported input that makes a backtest look better than it is.
TAKER_FEE_BPS = 10.0
MAKER_FEE_BPS: float | None = None  # TODO(Samuel): confirm the real maker tier

SIZES = (10_000.0, 100_000.0, 1_000_000.0, 10_000_000.0)


@dataclass(frozen=True)
class ExecutionCost:
    scenario: str
    fee_bps: float
    spread_bps: float
    impact_bps: float
    total_bps: float
    participation: float
    fill_risk: str


def sqrt_impact_bps(order_notional: float, adv_notional: float, sigma_horizon: float,
                    y: float = 1.0) -> float:
    """Square-root market impact, in bps.

    ``impact = y * sigma_horizon * sqrt(order / ADV)`` (Grinold & Kahn ch16).
    ``sigma_horizon`` must be the volatility of the horizon the order is worked
    over -- using the daily sigma for a 15-minute order overstates impact by
    sqrt(96).
    """
    if order_notional <= 0:
        return 0.0
    if adv_notional <= 0 or not math.isfinite(adv_notional):
        # An illiquid bucket has no upper bound on impact.  Reporting a number
        # here would price an untradeable idea as a cheap one.
        return math.inf
    return y * sigma_horizon * math.sqrt(order_notional / adv_notional) * BPS


def trade_cost(scenario: str, spread_bps: float, impact_bps: float,
              *, taker_fee_bps: float = TAKER_FEE_BPS,
              maker_fee_bps: float | None = MAKER_FEE_BPS,
              participation: float = 0.0) -> ExecutionCost | None:
    """Round-trip cost of one trade under one execution scenario.

    A taker crosses the spread: it pays ``spread`` once, plus fees on both
    sides.  A maker posts into the book and does **not** cross, so it pays only
    fees -- but it earns the spread only on a filled order, and the fill rate
    is a property of the strategy, not of this function.  The maker row is
    therefore a *floor*: it is only reachable by a strategy that can prove its
    fill rate.

    Returns ``None`` for the maker scenario while the desk's maker fee is
    unconfirmed.  Emitting a cost from an assumed fee would be inventing the
    single input that decides whether a maker idea is viable.
    """
    if scenario == "taker":
        fee, crossed = taker_fee_bps, spread_bps
    elif scenario == "maker":
        if maker_fee_bps is None:
            return None
        fee, crossed = maker_fee_bps, 0.0
    else:
        raise ValueError(f"unknown scenario {scenario!r}")
    total = 2.0 * fee + crossed + impact_bps
    risk = ("fill uncertain: needs a proven fill rate on this signal"
            if scenario == "maker" else "none: market order fills")
    return ExecutionCost(
        scenario=scenario,
        fee_bps=fee,
        spread_bps=crossed,
        impact_bps=impact_bps,
        total_bps=total,
        participation=participation,
        fill_risk=risk,
    )


def scenario_grid(symbol: str, spread_bps: float, hourly_adv: pd.Series,
                  sigma_hour: float, *, sizes: tuple[float, ...] = SIZES,
                  y: float = 1.0, spread_multiplier: float = 3.0) -> pd.DataFrame:
    """Execution-cost grid per size and UTC hour.

    ``spread_bps`` is the aggTrades proxy, not a quote-derived effective spread.
    The desk's conservative reference is ``max(proxy, one_tick) * 3``.  The
    multiplier is explicit so reports can show x1/x3/x10 sensitivity without
    silently turning a proxy into a precision claim.
    """
    if spread_multiplier <= 0:
        raise ValueError("spread_multiplier must be positive")
    applied_spread = spread_bps * spread_multiplier
    rows: list[dict] = []
    for size in sizes:
        for hour in sorted(hourly_adv.index.tolist()):
            adv = float(hourly_adv.loc[hour])
            impact = sqrt_impact_bps(size, adv, sigma_hour, y=y)
            for scenario in ("taker", "maker"):
                cost = trade_cost(scenario, applied_spread, impact,
                                  participation=size / adv if adv > 0 else math.inf)
                if cost is None:
                    # The maker tier is unconfirmed; the row is skipped rather
                    # than filled with an assumed fee.
                    continue
                rows.append({
                    "symbol": symbol, "notional": size, "utc_hour": hour,
                    "adv_usd": adv, "proxy_spread_bps": spread_bps,
                    "spread_multiplier": spread_multiplier,
                    "spread_bps": applied_spread,
                    **vars(cost),
                })
    return pd.DataFrame(rows)


def viable_edge_bps(round_trip_bps: float, *, multiplier: float = 3.0,
                    stress: float = 1.0) -> float:
    """Minimum mean gross gain per trade for an idea to be worth testing.

    The desk rule (plan section 8) is 3x the round-trip cost; ``stress`` is the
    x2 cost scenario the plan also demands.
    """
    return round_trip_bps * multiplier * stress