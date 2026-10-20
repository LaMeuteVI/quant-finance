"""H3 (Review 2026-10-20 b) — re-compute V3 numbers on the H1 trial's
exact returns.csv, with cold-start (2017-2019) treated consistently
in both the strategy and the benchmarks.

Output: a small JSON written to stdout, plus a markdown table to
``research/notes/2026-10-20-H3-results.md``.
"""

import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from pathlib import Path

ROOT = Path("/root/quant-finance/aster/desk")


def annualised_mean(s: pd.Series, ppy: int) -> float:
    return float(s.mean() * ppy)


def annualised_vol(s: pd.Series, ppy: int) -> float:
    return float(s.std(ddof=1) * np.sqrt(ppy))


def sharpe(s: pd.Series, ppy: int) -> float:
    v = annualised_vol(s, ppy)
    if v <= 0:
        return float("nan")
    return annualised_mean(s, ppy) / v


def main() -> None:
    ppy = 365
    rets_path = ROOT / "backtests/H-20261020-014/20261020T132003Z-dev-vol_target_trend_ensemble-v1.1.0/returns.csv"
    rets = pd.read_csv(rets_path, parse_dates=["bar_close_utc"]).set_index("bar_close_utc").sort_index()

    # Effective window = first non-zero strategy return → 2024-07-01 cutoff.
    # The strategy is flat before vol_lookback (180d) + min_history (120d)
    # is satisfied (cold start), so the meaningful window starts ~2020.
    active = rets[rets["ret"] != 0.0]
    start = active.index.min()
    end = pd.Timestamp("2024-07-01", tz="UTC")
    win = rets[(rets.index >= start) & (rets.index < end)].copy()

    # Strategy
    f3 = win["ret"].rename("f3")
    s_f3 = sharpe(f3, ppy)
    v_f3 = annualised_vol(f3, ppy)
    m_f3 = annualised_mean(f3, ppy)

    # Load spot close prices for the 5 majors.
    cols = ["BTC", "ETH", "BNB", "SOL", "XRP"]
    px = {}
    for c in cols:
        path = ROOT / f"data/ohlcv/binance/{c}-USDT/1d.parquet"
        df = pd.read_parquet(path)
        if "date" in df.columns:
            df = df.set_index("date")
        df.index = pd.to_datetime(df.index, utc=True)
        df = df.loc[(df.index >= start) & (df.index < end)]
        px[c] = df["close"]
    px_df = pd.concat(px, axis=1)
    px_df.columns = [f"{c}_close" for c in px_df.columns]

    # BTC b&h
    btc = px_df["BTC_close"].pct_change().dropna()
    s_btc = sharpe(btc, ppy)
    v_btc = annualised_vol(btc, ppy)

    # EW5 b&h
    ew_ret = px_df.pct_change().mean(axis=1).dropna()
    s_ew = sharpe(ew_ret, ppy)
    v_ew = annualised_vol(ew_ret, ppy)

    # Alpha vs BTC, HAC t-stat
    aligned = pd.concat([f3, btc], axis=1, keys=["f3", "btc"]).dropna()
    X = sm.add_constant(aligned["btc"].values)
    mod = sm.OLS(aligned["f3"].values, X).fit(cov_type="HAC", cov_kwds={"maxlags": 5})
    alpha_btc = float(mod.params[0]) * ppy
    tstat_btc = float(mod.tvalues[0])
    beta_btc = float(mod.params[1])
    corr_btc = float(np.corrcoef(aligned["f3"], aligned["btc"])[0, 1])

    # Alpha vs EW5
    aligned_ew = pd.concat([f3, ew_ret], axis=1, keys=["f3", "ew"]).dropna()
    X = sm.add_constant(aligned_ew["ew"].values)
    mod = sm.OLS(aligned_ew["f3"].values, X).fit(cov_type="HAC", cov_kwds={"maxlags": 5})
    alpha_ew = float(mod.params[0]) * ppy
    tstat_ew = float(mod.tvalues[0])

    out = {
        "effective_window": [start.isoformat(), end.isoformat()],
        "n_bars": int(len(win)),
        "strategy": {"sharpe_ann": s_f3, "vol_ann": v_f3, "mean_daily": float(f3.mean())},
        "btc_bh": {"sharpe_ann": s_btc, "vol_ann": v_btc},
        "ew5_bh": {"sharpe_ann": s_ew, "vol_ann": v_ew},
        "vs_btc": {"alpha_ann": alpha_btc, "t_hac": tstat_btc, "beta": beta_btc, "corr": corr_btc},
        "vs_ew5": {"alpha_ann": alpha_ew, "t_hac": tstat_ew},
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()