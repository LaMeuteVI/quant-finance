"""Performance metrics. Crypto trades 24/7: a year is 365 days of bars."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

PERIODS_PER_YEAR = {
    "1m": 525_600, "5m": 105_120, "15m": 35_040, "1h": 8_760, "4h": 2_190, "1d": 365, "1w": 52,
}


def max_drawdown(returns: pd.Series) -> float:
    eq = (1 + returns).cumprod()
    return float((eq / eq.cummax() - 1).min()) if len(eq) else 0.0


def summary(returns: pd.Series, timeframe: str = "1d", turnover: pd.Series | None = None) -> dict:
    r = returns.dropna()
    ppy = PERIODS_PER_YEAR[timeframe]
    n = len(r)
    if n < 2 or r.std(ddof=1) == 0:
        return {"n_obs": n, "error": "not enough variation to compute statistics"}
    mu, sd = r.mean(), r.std(ddof=1)
    sr_pp = mu / sd
    downside = r[r < 0].std(ddof=1)
    total = float((1 + r).prod() - 1)
    years = n / ppy
    cagr = float((1 + total) ** (1 / years) - 1) if total > -1 else -1.0
    mdd = max_drawdown(r)
    out = {
        "n_obs": n,
        "years": round(years, 3),
        "total_return": total,
        "cagr": cagr,
        "vol_ann": float(sd * np.sqrt(ppy)),
        "sharpe_pp": float(sr_pp),                       # per-period, used by PSR/DSR
        "sharpe_ann": float(sr_pp * np.sqrt(ppy)),
        "sortino_ann": float(mu / downside * np.sqrt(ppy)) if downside and downside > 0 else None,
        "max_drawdown": mdd,
        "calmar": float(cagr / abs(mdd)) if mdd < 0 else None,
        "hit_rate": float((r > 0).sum() / (r != 0).sum()) if (r != 0).any() else None,
        "skew": float(stats.skew(r)),
        "kurtosis": float(stats.kurtosis(r, fisher=False)),  # non-excess; normal = 3
        "worst_bar": float(r.min()),
        "best_bar": float(r.max()),
    }
    if turnover is not None:
        out["turnover_ann"] = float(turnover.mean() * ppy)
    return out


def worst_windows(returns: pd.Series, window: int, k: int = 5) -> list[dict]:
    """The k worst non-overlapping rolling-window returns: the stress periods to inspect."""
    roll = (1 + returns).rolling(window).apply(np.prod, raw=True) - 1
    out, taken = [], pd.Series(False, index=returns.index)
    for ts in roll.sort_values().dropna().index:
        loc = returns.index.get_loc(ts)
        lo = max(0, loc - window + 1)
        if taken.iloc[lo:loc + 1].any():
            continue
        taken.iloc[lo:loc + 1] = True
        out.append({"end": ts.isoformat(), "start": returns.index[lo].isoformat(), "return": float(roll[ts])})
        if len(out) == k:
            break
    return out
