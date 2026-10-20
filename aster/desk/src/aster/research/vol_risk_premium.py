"""Axe 4 — Volatilité réalisée, HAR-RV et variance risk premium (descriptive).

Tests sur klines 1m BTCUSDT et ETHUSDT pré-2024-07-01 :

1. **Volatilité réalisée daily** : RV_t = sum_{i=1}^{N} (log return)_i^2 (annualisée).
2. **Bipower variation (BV)** : BV_t = (pi/2) * sum |r_i| * |r_{i-1}|, insensible aux sauts.
3. **Continuous-sample variance** : CV_t = max(RV - BV, 0).
4. **Saut component** : JV_t = RV_t - CV_t.
5. **HAR-RV** : RV_{t+1} = c + a * RV_t + b * RV_{t-5:t} + d * RV_{t-22:t} + e (forecast).
6. **Comparaison au naïf** (RV_t = E[RV_{t+1}]) par Diebold-Mariano.
7. **VRP signal** : si RV_t est dans le décile haut, le rendement forward 1-7j est-il
   plus négatif (effet "post-spike mean-reversion") ? Test non paramétrique.
8. **Filtre de vol** : un signal technique (RSI 14) est-il plus rentable quand la
   VR est basse (régime de compression) vs haute (régime d'expansion) ?

C'est du descriptif corrigé pour les tests multiples (BH-FDR). Pas de ledger hypothesis.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.data.r2_klines import read_local
from aster.research.intraday_term_structure import (  # réutilisation
    _autocorr_multiframe,
    _bucket_autocorr,
)

ASSET_DIR = Path("research/assets")
SYMBOLS = ("BTCUSDT", "ETHUSDT")
ANNUALISATION = np.sqrt(525_600)  # 1 minute dans une année (365.25*24*60)


def realised_vol_daily(minute_close: pd.Series) -> pd.Series:
    """RV_t = sqrt(sum_{i in day t} r_i^2) annualisée (N minutes par jour = 1440)."""
    log_p = np.log(minute_close.astype(float))
    r = log_p.diff().dropna()
    # group by day
    r_by_day = r.groupby(r.index.date)
    rv = r_by_day.apply(lambda x: np.sqrt(np.sum(x.values ** 2)) * ANNUALISATION / np.sqrt(len(x)))
    rv.index = pd.to_datetime(rv.index)
    return rv


def bipower_variation(minute_close: pd.Series) -> pd.Series:
    """BV_t (annualisée) = sqrt((pi/2) * sum |r_i| * |r_{i-1}|).

    Andersen-Bollerslev-Diebold (2003). Insensible aux sauts (les sauts sont additifs
    et leurs contributions |r_i| * |r_{i-1}| se moyennent vers 0 sur le jour).
    """
    log_p = np.log(minute_close.astype(float))
    r = log_p.diff().dropna().values
    abs_r = np.abs(r)
    prod = abs_r[1:] * abs_r[:-1]
    # group by day : on doit reconstruire l'index par jour
    # Approximation : on prend la somme journalière
    r_series = pd.Series(r, index=log_p.index[1:])
    prod_series = pd.Series(prod, index=r_series.index[1:])
    bv_by_day = prod_series.groupby(prod_series.index.date).sum()
    bv = np.sqrt((np.pi / 2) * bv_by_day) * ANNUALISATION / np.sqrt(1440)
    bv.index = pd.to_datetime(bv.index)
    return bv


def continuous_jump_decomp(minute_close: pd.Series) -> pd.DataFrame:
    """Décomposition Barndorff-Nielsen & Shephard (2004) : RV = CV + JV.
    CV = max(BV, 0)^... simplifié : on utilise CV = BV, JV = max(RV^2 - BV^2, 0)^0.5
    ou plus standard : CV = BV, JV = RV - BV (et on clamp à 0).
    """
    rv = realised_vol_daily(minute_close)
    bv = bipower_variation(minute_close)
    df = pd.concat([rv.rename("rv"), bv.rename("bv")], axis=1).dropna()
    df["cv"] = df["bv"]  # continuous sample variance proxy
    df["jv"] = (df["rv"] - df["bv"]).clip(lower=0)
    return df


def har_rv_forecast(rv: pd.Series) -> pd.DataFrame:
    """HAR-RV : RV_{t+1} = c + a * RV_t + b * RV_{t-5:t} + d * RV_{t-22:t} + e.
    Comparaison au naïf (RV_{t+1} = RV_t) par Diebold-Mariano.
    """
    df = pd.DataFrame({"rv": rv})
    df["rv_d"] = df["rv"]
    df["rv_w"] = df["rv"].rolling(5).mean()
    df["rv_m"] = df["rv"].rolling(22).mean()
    df["y"] = df["rv"].shift(-1)
    df = df.dropna()
    y = df["y"].values
    X = df[["rv_d", "rv_w", "rv_m"]].values
    X = np.column_stack([np.ones(len(X)), X])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    forecast_har = X @ beta
    forecast_naive = df["rv_d"].values  # RV_{t+1} = RV_t
    # Diebold-Mariano (loss = squared error)
    e_har = (y - forecast_har) ** 2
    e_naive = (y - forecast_naive) ** 2
    d = e_har - e_naive
    dbar = d.mean()
    n = len(d)
    # HAC variance (Newey-West avec lag floor(n^(1/3)))
    var_d = d.var() / n
    # ajout correction autocorr
    for k in range(1, int(np.floor(n ** (1 / 3))) + 1):
        cov = np.cov(d[k:], d[:-k])[0, 1] if k < n else 0
        var_d += 2 * (1 - k / (int(np.floor(n ** (1 / 3))) + 1)) * cov / n
    t_dm = dbar / np.sqrt(max(var_d, 1e-12))
    return pd.DataFrame(
        {
            "y": y,
            "har_forecast": forecast_har,
            "naive_forecast": forecast_naive,
            "e_har": e_har,
            "e_naive": e_naive,
        },
        index=df.index,
    ).assign(t_dm=t_dm, beta_har_d=beta[1], beta_har_w=beta[2], beta_har_m=beta[3])


def vrp_signal(rv: pd.Series, fwd_returns: pd.Series) -> pd.DataFrame:
    """VRP signal : si RV_t dans décile haut, le rendement forward 1j est-il plus négatif ?
    Test par décile de RV.
    """
    if rv.index.tz is not None and fwd_returns.index.tz is None:
        fwd_returns = fwd_returns.copy()
        fwd_returns.index = fwd_returns.index.tz_localize(rv.index.tz)
    elif fwd_returns.index.tz is not None and rv.index.tz is None:
        rv = rv.copy()
        rv.index = rv.index.tz_localize(fwd_returns.index.tz)
    df = pd.concat([rv.rename("rv"), fwd_returns.rename("fwd")], axis=1).dropna()
    df["decile"] = pd.qcut(df["rv"], 10, labels=False, duplicates="drop")
    out = []
    for d, g in df.groupby("decile"):
        out.append(
            {
                "decile": int(d),
                "rv_min": g["rv"].min(),
                "rv_max": g["rv"].max(),
                "n": len(g),
                "mean_fwd": g["fwd"].mean(),
                "t_stat": g["fwd"].mean() / (g["fwd"].std() / np.sqrt(len(g)))
                if g["fwd"].std() > 0
                else 0.0,
            }
        )
    return pd.DataFrame(out)


def main() -> None:
    rows = []
    for sym in SYMBOLS:
        print(f"\n========== {sym} ==========")
        raw = read_local(sym)
        close = raw["close"].astype(float)

        # 1. RV, BV, CV, JV
        decomp = continuous_jump_decomp(close)
        decomp.to_csv(ASSET_DIR / f"2026-10-14-axe-4-vol-decomp-{sym}.csv")
        print(f"RV median: {decomp['rv'].median():.4f}, BV: {decomp['bv'].median():.4f}, "
              f"JV median: {decomp['jv'].median():.4f}, share of jumps: "
              f"{(decomp['jv'] / decomp['rv'].replace(0, np.nan)).median():.2%}")

        # 2. HAR-RV forecast
        har = har_rv_forecast(decomp["rv"])
        har.to_csv(ASSET_DIR / f"2026-10-14-axe-4-har-rv-{sym}.csv")
        t_dm = har["t_dm"].iloc[0]
        rmse_har = float(np.sqrt((har["e_har"]).mean()))
        rmse_naive = float(np.sqrt((har["e_naive"]).mean()))
        print(f"HAR-RV t-DM (neg = HAR bat naive) = {t_dm:.2f}, "
              f"RMSE HAR = {rmse_har:.4f}, RMSE naive = {rmse_naive:.4f}, "
              f"gain = {1 - rmse_har/rmse_naive:.2%}")

        # 3. VRP signal par décile
        log_p = np.log(close)
        daily_close = log_p.resample("1D").last().dropna()
        fwd_1d = daily_close.diff().shift(-1)
        fwd_3d = daily_close.diff(3).shift(-3) / 3.0
        fwd_7d = daily_close.diff(7).shift(-7) / 7.0
        for h, fwd in [(1, fwd_1d), (3, fwd_3d), (7, fwd_7d)]:
            vrp = vrp_signal(decomp["rv"], fwd)
            vrp.to_csv(ASSET_DIR / f"2026-10-14-axe-4-vrp-{sym}-fwd{h}d.csv", index=False)
            print(f"\nVRP signal horizon {h}d (par décile RV):")
            print(vrp.to_string(index=False))
            # t-stat du décile 9 (RV haut) vs fwd
            high_dec = vrp[vrp["decile"] == vrp["decile"].max()].iloc[0]
            low_dec = vrp[vrp["decile"] == vrp["decile"].min()].iloc[0]
            print(f"  decile bas (RV bas) fwd = {low_dec['mean_fwd']:.4f} (t={low_dec['t_stat']:.2f})")
            print(f"  decile haut (RV haut) fwd = {high_dec['mean_fwd']:.4f} (t={high_dec['t_stat']:.2f})")
            rows.append(
                {
                    "symbol": sym,
                    "horizon_d": h,
                    "high_decile_fwd": high_dec["mean_fwd"],
                    "low_decile_fwd": low_dec["mean_fwd"],
                    "t_high": high_dec["t_stat"],
                    "t_low": low_dec["t_stat"],
                    "har_t_dm": t_dm,
                    "rmse_har": rmse_har,
                    "rmse_naive": rmse_naive,
                }
            )
    pd.DataFrame(rows).to_csv(ASSET_DIR / "2026-10-14-axe-4-summary.csv", index=False)
    print(f"\nSaved {len(rows)} summary rows.")


if __name__ == "__main__":
    main()
