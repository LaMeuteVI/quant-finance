"""Intraday transaction-cost model (research plan §4.4).

Every number here is the *judge of peace* for an intraday idea: an edge whose
mean gross gain per trade is below three times the round-trip cost is an
anecdote, not a strategy.  Nothing in this module is a tunable that a caller
can quietly relax to make a backtest pass.

Three layers, from measured to assumed, each reported separately so the reader
knows which one is doing the work:

1. **Spread, estimated from the data.**  Corwin-Schultz (2012) and
   Abdi-Ranaldo (2017) read only the high/low/close, so they work on any OHLC
   series; Roll (1984) reads the serial covariance of price changes.  They are
   biased upward by volatility and they cannot see the book, so they are used as
   an upper-ish bound on the *effective* spread, not as a quote.

2. **Market impact, in square-root form.**  ``Y * sigma * sqrt(Q / ADV)``
   (grinold-kahn-apm ch16).  ``sigma`` is measured on the trading horizon
   actually used, and ``ADV`` is the dollar volume of the *bucket* being
   traded, not the annual figure: an order placed in the 03:00 UTC hour
   competes with the 03:00 book, not with a year's worth of volume.

3. **Fees**, passed in explicitly because they are an account fact, not a
   market fact.  A Binance spot taker fee of 10 bps per side is the desk's
   default; the value lives in ``config/desk.yaml`` so a change is a visible
   diff rather than a constant buried in code.

Conventions, stated because they are where such models usually go wrong:

* every spread and cost is returned in **basis points of notional**, so a 5 bp
  cost is 0.0005 in both places;
* a *round trip* pays the spread twice (entry + exit) and impact twice, and one
  fee per side;
* impact is signed as a positive cost; ``sqrt`` of a zero ADV is undefined, so
  an illiquid bucket returns ``inf`` rather than 0.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import pandas as pd

# Katz (1991) constant used by Corwin-Schultz when the two-day spread estimate
# comes out negative.  3 - 2*sqrt(2) = 0.1715728752538099...
KATZ_K = 3.0 - 2.0 * math.sqrt(2.0)

BPS = 1e4


def _clean(frame: pd.DataFrame, columns: tuple[str, ...]) -> pd.DataFrame:
    missing = [c for c in columns if c not in frame.columns]
    if missing:
        raise ValueError(f"cost model needs columns {list(columns)}; missing {missing}")
    return frame.dropna(subset=list(columns))


def spread_by_utc_hour(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Effective spread per UTC hour, estimated **on the bars themselves**.

    The spread estimator is applied to ``high``/``low``/``close`` of the frame
    it is given, then reduced to a per-hour median over the sample.  It is
    deliberately *not* computed on 1-minute bars and averaged up: Abdi-Ranaldo
    returns exactly 0 on most single minutes (the close-to-midpoint term is
    tiny at that horizon), so an upward aggregation would drive the hourly
    spread to ~0 and make every intraday candidate look free to trade.  The
    horizon of the cost must match the horizon of the estimator.

    The **max** of the three estimators is taken per hour, for the same reason
    as :func:`corwin_schultz_spread`: their average flatters a tight spread.
    """
    frame = _clean(pd.DataFrame({"high": high, "low": low, "close": close}),
                   ("high", "low", "close"))
    if frame.empty:
        return pd.Series(dtype="float64", name="spread_bps")
    high_s: pd.Series = frame["high"]
    low_s: pd.Series = frame["low"]
    close_s: pd.Series = frame["close"]
    hours: np.ndarray = pd.DatetimeIndex(frame.index).hour.to_numpy()
    # Each estimator drops observations of its own (Roll needs three points,
    # Corwin-Schultz pairs bars, CHL needs eta_{t+1}), so every estimate is
    # re-indexed onto ``frame`` before being stacked.  Without this the columns
    # have different lengths and the frame cannot even be built.
    def aligned(values: pd.Series) -> np.ndarray:
        return values.reindex(frame.index).to_numpy()

    estimates = pd.DataFrame({
        "hour": hours,
        "chl": aligned(abdi_ranaldo_spread(high_s, low_s, close_s)),
        "cs": aligned(corwin_schultz_spread(high_s, low_s, close_s)),
        "roll": aligned(roll_spread(close_s)),
    }, index=frame.index)
    estimates["best"] = estimates[["chl", "cs", "roll"]].max(axis=1, skipna=True)
    by_hour: pd.Series = estimates.groupby("hour", sort=True)["best"].median()
    return by_hour


def roll_spread(close: pd.Series) -> pd.Series:
    """Roll (1984) implied spread from the serial covariance of price changes.

    ``spread = 2 * sqrt(-cov(dP_t, dP_{t-1}))``, expressed as a **fraction of
    the mean price** and returned in bps.  Roll derives it from the bid-ask
    bounce: if price changes alternate, part of the observed change is the
    spread crossing itself.  Where the covariance is positive there is no
    evidence of a bounce and the estimate is floored at 0, not at the mean.

    The covariance is taken over the whole series (a single sample estimate),
    which is what Roll's model asks for; a rolling variant would need an
    explicit window and would be a different, slower estimator.
    """
    series = pd.Series(close, dtype="float64").dropna()
    if len(series) < 3:
        return pd.Series([0.0], index=series.index[:1])
    price = float(series.mean())
    delta = series.diff().dropna().to_numpy()
    covariance = float(np.cov(delta[1:], delta[:-1])[0, 1])
    spread = 2.0 * math.sqrt(max(0.0, -covariance)) / price if price > 0 else 0.0
    return pd.Series([spread * BPS], index=series.index[:1])


def corwin_schultz_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corwin-Schultz (2012) two-day high-low spread, in bps, per observation.

    The estimator compares the range spanned by two consecutive bars with the
    sum of the two single-bar ranges.  A genuine move makes the two-bar range
    wider than the sum of the parts; a pure bid-ask bounce does not scale with
    time, so what fails to scale is the spread.  With, for the pair (t-1, t),

        ``beta  = [ln(H_t / L_t)]^2 + [ln(H_t-1 / L_t-1)]^2``   (sum of ranges)
        ``gamma = [ln(max(H,H') / min(L,L'))]^2``               (the 2-bar range)
        ``alpha = (sqrt(2 beta) - sqrt(beta)) / k - sqrt(gamma / k)``
        ``S     = 2 (e^alpha - 1) / (1 + e^alpha)``,  ``k = 3 - 2 sqrt(2)``

    ``alpha`` is the spread-free volatility component and ``S`` is the
    *proportional* effective spread.  A negative ``alpha`` is the normal
    outcome when the two-bar range does not exceed the sum of the bars: it is
    floored at 0, as every implementation does.  That floor biases the pooled
    mean downward, which is why this estimator is never the cost of record on
    its own -- Abdi-Ranaldo is reported beside it.

    The worked example in the test file reproduces the published check: two
    overlapping bars 4998-5002 and 4999-5003 give about 3.2 bps.
    """
    out = []
    h, l, _ = (pd.Series(x, dtype="float64") for x in (high, low, close))
    for i in range(1, len(h)):
        h2, l2 = h.iloc[i - 1], l.iloc[i - 1]
        h1, l1 = h.iloc[i], l.iloc[i]
        if min(h2, l2, h1, l1) <= 0:
            out.append(np.nan)
            continue
        beta = math.log(h1 / l1) ** 2 + math.log(h2 / l2) ** 2      # one-bar ranges
        gamma = math.log(max(h1, h2) / min(l1, l2)) ** 2           # two-bar range
        alpha = ((math.sqrt(2.0 * beta) - math.sqrt(beta)) / KATZ_K
                 - math.sqrt(gamma / KATZ_K))
        if alpha <= 0:
            out.append(0.0)
            continue
        spread = 2.0 * (math.exp(alpha) - 1.0) / (1.0 + math.exp(alpha))
        out.append(spread * BPS)
    index = h.index[1:]
    return pd.Series(out, index=index, dtype="float64")


def abdi_ranaldo_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Abdi-Ranaldo (2017) CHL estimator, in bps, per observation.

    The paper's closed form (RFS 2017, eq. 9) works entirely in **log prices**.
    With the mid-range ``eta_t = (h_t + l_t) / 2`` (log-scale, so the two
    half-spreads cancel in the average) used as a proxy for the efficient price,

        ``s^2 = 4 E[(c_t - eta_t)(c_t - eta_{t+1})]``
        ``s   = sqrt(max(s^2, 0))``

    and the two-day corrected version reported per observation.  The estimate
    is floored at zero because ``(c_t - eta_t)`` and ``(c_t - eta_{t+1})`` are
    signed and their product is often negative on a quiet day; the paper shows
    flooring the two-day estimate then averaging beats removing and averaging.

    This estimator uses the close *and* the high/low, so it has both a smaller
    bias and a smaller variance than Corwin-Schultz on the same data.  It is the
    one the desk uses as its spread of record; Corwin-Schultz is reported beside
    it as a cross-check, never as the cost itself.
    """
    h, l, c = (pd.Series(x, dtype="float64") for x in (high, low, close))
    if (h <= 0).any() or (l <= 0).any() or (c <= 0).any():
        raise ValueError("abdi_ranaldo_spread requires strictly positive prices")

    log_h, log_l, log_c = np.log(h), np.log(l), np.log(c)
    eta = (log_h + log_l) / 2.0                     # mid-range, log scale
    eta_next = eta.shift(-1)
    deviation = (log_c - eta) * (log_c - eta_next)
    spread = 2.0 * np.sqrt(deviation.clip(lower=0.0)) * BPS
    spread[eta_next.isna()] = np.nan
    return spread


def sqrt_impact(order_notional: float, adv_notional: float, sigma: float,
                y: float = 1.0) -> float:
    """Square-root market impact in bps: ``y * sigma * sqrt(Q / ADV)`` (GK ch16).

    ``sigma`` must be the volatility **of the horizon the order is worked over**,
    expressed as a fraction (0.05 = 5 %).  A daily ``sigma`` applied to an
    intraday order would overstate the impact by roughly sqrt(24*60/1440);
    passing the wrong horizon is the most common way this law is misused, so
    the parameter is named rather than folded into a default.
    """
    if order_notional <= 0:
        return 0.0
    if adv_notional <= 0:
        # An illiquid bucket has no upper bound on impact; returning 0 here
        # would silently price an untradeable idea as a free one.
        return math.inf
    if sigma <= 0:
        return 0.0
    return y * sigma * math.sqrt(order_notional / adv_notional) * BPS


def kyle_lambda(price_change: pd.Series, signed_flow: pd.Series) -> dict:
    """Kyle (1985) lambda estimated from the kline taker flow, in return per dollar.

    ``lambda = cov(dP, flow) / var(flow)``: the price move per dollar of net
    aggressive volume.  With Binance klines the flow is
    ``2 * taker_buy_quote - quote_volume``.  This is a *measured* impact
    coefficient for the asset as traded, not an assumed one, which is why it is
    reported next to the square-root law rather than instead of it: the two
    answer different questions (local price response vs order-size scaling).
    """
    p = pd.Series(price_change, dtype="float64")
    f = pd.Series(signed_flow, dtype="float64")
    frame = pd.concat([p, f], axis=1).dropna()
    frame.columns = ["dp", "flow"]
    if len(frame) < 30:
        return {"lambda": float("nan"), "n": int(len(frame)), "r_squared": float("nan"),
                "t_stat": float("nan")}
    var = float(frame["flow"].var(ddof=1))
    lam = float(np.cov(frame["dp"], frame["flow"])[0, 1]) / var if var > 0 else float("nan")

    # Ordinary least squares of dp on flow, with the standard error of the
    # slope computed by hand.  ``np.polyfit(..., cov=True)`` and
    # ``scipy.stats.linregress`` both return ``None``/a short tuple when the
    # residuals are degenerate (a perfect fit, which is exactly the synthetic
    # case a reference test must exercise), so the t-stat is computed directly
    # from the OLS covariance matrix instead of being read off a library.
    n = len(frame)
    design = np.column_stack([np.ones(n), frame["flow"].to_numpy()])
    coefficients, *_ = np.linalg.lstsq(design, frame["dp"].to_numpy(), rcond=None)
    residuals = frame["dp"].to_numpy() - design @ coefficients
    dof = n - design.shape[1]
    if dof > 0:
        variance = float(residuals @ residuals) / dof
        covariance = variance * np.linalg.inv(design.T @ design)
        slope_stderr = math.sqrt(max(0.0, float(covariance[1, 1])))
    else:
        slope_stderr = 0.0
    slope = float(coefficients[1])
    intercept = float(coefficients[0])
    flow_var = float(frame["flow"].to_numpy().var())
    r_squared = 0.0 if flow_var == 0 else float(np.corrcoef(frame["flow"], frame["dp"])[0, 1] ** 2)
    return {
        "lambda": lam,
        "slope": slope,
        "intercept": intercept,
        "n": int(n),
        "r_squared": r_squared,
        "t_stat": float(slope / slope_stderr) if slope_stderr else float("inf"),
    }


def amihud_illiquidity(returns: pd.Series, dollar_volume: pd.Series) -> pd.Series:
    """Amihud (2002): price impact per dollar traded, scaled to 1e6.

    ``ILLIQ_t = |r_t| / ADV_t``.  It is a ratio of a return to a dollar flow,
    so it is reported here times 1e6 to keep the numbers readable.  A rising
    value means the same volume moves the price further: the cost side of
    section 9 of the research plan.
    """
    r = pd.Series(returns, dtype="float64").abs()
    v = pd.Series(dollar_volume, dtype="float64").where(lambda s: s > 0)
    return (r / v) * 1e6


@dataclass(frozen=True)
class RoundTripCost:
    """A full enter-and-exit cost, in bps of notional, with its own audit trail."""

    spread_bps: float
    spread_source: str
    fee_bps_per_side: float
    impact_bps: float
    notional: float
    adv_notional: float
    participation: float
    sigma_horizon: float

    @property
    def total_bps(self) -> float:
        # The spread is crossed on entry and again on exit; impact and fee are
        # paid once per side.  Two sides total.
        return 2.0 * (0.5 * self.spread_bps + self.impact_bps + self.fee_bps_per_side)

    def as_dict(self) -> dict:
        return {
            "round_trip_bps": self.total_bps,
            "spread_bps": self.spread_bps,
            "spread_source": self.spread_source,
            "fee_bps_per_side": self.fee_bps_per_side,
            "impact_bps": self.impact_bps,
            "notional": self.notional,
            "adv_notional": self.adv_notional,
            "participation": self.participation,
            "sigma_horizon": self.sigma_horizon,
        }


def round_trip_cost(spread_bps: float, notional: float, adv_notional: float,
                    sigma: float, *, fee_bps_per_side: float = 10.0,
                    y: float = 1.0, spread_source: str = "corwin_schultz",
                    sigma_horizon: float = 0.0) -> RoundTripCost:
    """Assemble the round-trip cost of one trade on the desk's own fee tier.

    Default ``fee_bps_per_side=10`` is Binance spot taker, which is what an
    edge must beat when it crosses the spread; a maker strategy must pass its
    own number in rather than borrow this one.
    """
    impact = sqrt_impact(notional, adv_notional, sigma, y)
    return RoundTripCost(
        spread_bps=float(spread_bps),
        spread_source=spread_source,
        fee_bps_per_side=float(fee_bps_per_side),
        impact_bps=float(impact),
        notional=float(notional),
        adv_notional=float(adv_notional),
        participation=float(notional / adv_notional) if adv_notional > 0 else math.inf,
        sigma_horizon=float(sigma_horizon or sigma),
    )


def hourly_cost_grid(bars: pd.DataFrame, order_notional: float,
                     spreads: pd.Series, *, sigma_daily: float,
                     fee_bps_per_side: float = 10.0, y: float = 1.0) -> pd.DataFrame:
    """Round-trip cost by UTC hour, which is where intraday edges live or die.

    ``bars`` must carry ``quote_volume`` (the bucket's dollar turnover) and be
    hourly.  ``spreads`` is aligned on the same index and gives the effective
    spread for that bucket.  ``sigma_daily`` is the daily volatility, converted
    to the hourly horizon the order is worked over as
    ``sigma_daily / sqrt(24)`` -- an hourly bar's move is a fraction of a day's,
    and using the daily number overstates impact by sqrt(24) = 4.9x.

    The returned frame is the artifact section 4.4 asks for: cost per asset, per
    UTC hour, per order size.
    """
    if "quote_volume" not in bars.columns:
        raise ValueError("hourly_cost_grid needs quote_volume on the bars")
    sigma_hour = sigma_daily / math.sqrt(24.0)
    spread = spreads.reindex(bars.index)
    hours = pd.DatetimeIndex(bars.index).hour
    rows = []
    for hour in range(24):
        mask = hours == hour
        if not mask.any():
            continue
        adv = float(bars.loc[mask, "quote_volume"].median())
        hour_spread = float(spread.loc[mask].median()) if spread.loc[mask].notna().any() else math.nan
        cost = round_trip_cost(
            hour_spread, order_notional, adv, sigma_hour,
            fee_bps_per_side=fee_bps_per_side, y=y,
            sigma_horizon=sigma_hour,
        )
        row = cost.as_dict()
        row["utc_hour"] = hour
        row["adv_median_usd"] = adv
        rows.append(row)
    out = pd.DataFrame(rows).set_index("utc_hour").sort_index()
    return out