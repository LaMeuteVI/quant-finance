"""Axe 1 — Term structure intra-day (descriptive only).

Mesure, sur klines 1m BTCUSDT et ETHUSDT pré-cutoff :
- profil de vol annualisée par heure UTC (et par jour de semaine × heure) ;
- autocorrélation minute-par-minute à lag 1, 2, 5, 15, 60 dans chaque bucket de vol ;
- mean-reversion à l'intérieur d'un bucket de faible vol (autocorr < 0 = reversal) ;
- lead-lag temporel : corrélation entre buckets asia/eu/us intra-day.

Aucun ledger hypothesis, aucun backtest, aucun holdout.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from aster.data.bars import normalise_clock
from aster.data.r2_klines import read_local

ASSET_DIR = Path("research/assets")

SYMBOLS = ("BTCUSDT", "ETHUSDT")
MIN_BUCKET_MINUTES = 60  # min d'observations par bucket pour autocorr


def _log_return(close: pd.Series) -> pd.Series:
    return np.log(close).diff()


def _bucket_vol_profile(returns: pd.Series) -> pd.DataFrame:
    """Vol annualisée par bucket horaire UTC, jour de semaine × heure."""
    index = pd.DatetimeIndex(returns.index)
    work = pd.DataFrame({"ret": returns.values}, index=index)
    work["abs_ret"] = work["ret"].abs()
    work["sq_ret"] = work["ret"] ** 2
    work["weekday"] = index.dayofweek
    work["hour"] = index.hour
    grouped = work.groupby(["weekday", "hour"])
    return grouped.agg(
        minutes=("ret", "size"),
        median_abs_ret=("abs_ret", "median"),
        mean_sq_ret=("sq_ret", "mean"),
        std_ret=("ret", "std"),
    )


def _bucket_autocorr(returns: pd.Series, lags=(1, 2, 5, 15, 60)) -> pd.DataFrame:
    """Autocorrélations par bucket Asia/EU/US, par jour, lags multiples."""
    index = pd.DatetimeIndex(returns.index)
    work = pd.DataFrame({"ret": returns.values}, index=index)
    work["date"] = index.date
    work["bucket"] = pd.cut(
        index.hour,
        bins=[-1, 7, 15, 23],
        labels=["asia", "eu", "us"],
    )
    rows = []
    for (date, bucket), grp in work.groupby(["date", "bucket"], observed=True):
        r = grp["ret"].dropna()
        if len(r) < MIN_BUCKET_MINUTES:
            continue
        row = {"date": date, "bucket": str(bucket), "n": int(len(r))}
        for lag in lags:
            if len(r) > lag + 5:
                row[f"ac_lag{lag}"] = float(r.autocorr(lag=lag))
            else:
                row[f"ac_lag{lag}"] = float("nan")
        rows.append(row)
    return pd.DataFrame(rows)


def _autocorr_multiframe(close: pd.Series, bars=(1, 5, 15)) -> pd.DataFrame:
    """Autocorr à lag 1 par bar size, jour × bucket.

    Permet de voir si l'autocorr négative se renforce sur 5m/15m (effet
    microstructural plus marqué) ou s'atténue.
    """
    rows = []
    for bar in bars:
        if bar == 1:
            c = close
        else:
            c = close.resample(f"{bar}min").last().dropna()
        ret = np.log(c).diff().dropna()
        index = pd.DatetimeIndex(ret.index)
        work = pd.DataFrame({"ret": ret.values}, index=index)
        work["date"] = index.date
        work["bucket"] = pd.cut(
            index.hour,
            bins=[-1, 7, 15, 23],
            labels=["asia", "eu", "us"],
        )
        for (date, bucket), grp in work.groupby(["date", "bucket"], observed=True):
            r = grp["ret"].dropna()
            if len(r) < max(20, bar * 2):
                continue
            rows.append(
                {
                    "bar_min": bar,
                    "date": date,
                    "bucket": str(bucket),
                    "n": int(len(r)),
                    "ac_lag1": float(r.autocorr(lag=1)),
                }
            )
    return pd.DataFrame(rows)


def _cross_bucket_corr(returns: pd.Series) -> pd.DataFrame:
    """Cross-corrélation jour-par-jour entre buckets intra-day.

    Pour chaque couple (src, dst) ∈ {asia→eu, eu→us, asia→us} et chaque jour,
    on calcule la corrélation entre les sommes de log-returns par minute
    relative des deux buckets (séries 480 points). On garde aussi la corrélation
    signe-miroir (contrôle : si le lead est réel, le signe miroir doit
    s'inverser).
    """
    index = pd.DatetimeIndex(returns.index)
    work = pd.DataFrame({"ret": returns.values}, index=index)
    work["date"] = index.date
    work["hour"] = index.hour
    rows = []
    for date, grp in work.groupby("date"):
        pivots = {}
        for label, (lo, hi) in [("asia", (0, 8)), ("eu", (8, 16)), ("us", (16, 24))]:
            sel = grp[(grp["hour"] >= lo) & (grp["hour"] < hi)]["ret"].dropna()
            if len(sel) < 60:
                pivots[label] = None
                continue
            bucket = sel.groupby(sel.index.hour * 60 + sel.index.minute).sum()
            pivots[label] = bucket.reindex(range(lo * 60, hi * 60), fill_value=0.0).values
        for src, dst in [("asia", "eu"), ("eu", "us"), ("asia", "us")]:
            if pivots[src] is None or pivots[dst] is None:
                continue
            x, y = pivots[src], pivots[dst]
            if x.std() == 0 or y.std() == 0:
                continue
            c = float(np.corrcoef(x, y)[0, 1])
            c_inv = float(np.corrcoef(-x, y)[0, 1])
            rows.append(
                {
                    "date": date,
                    "src": src,
                    "dst": dst,
                    "corr": c,
                    "corr_inverse": c_inv,
                }
            )
    return pd.DataFrame(rows)


def build_payload(symbol: str) -> dict:
    raw = read_local(symbol)
    repaired, _clock = normalise_clock(raw)
    close = repaired["close"].astype(float)
    log_ret = _log_return(close)
    vol_profile = _bucket_vol_profile(log_ret)
    ac = _bucket_autocorr(log_ret)
    cross = _cross_bucket_corr(log_ret)
    mf = _autocorr_multiframe(close)
    return {
        "symbol": symbol,
        "vol_profile": vol_profile,
        "autocorr_per_bucket": ac,
        "cross_bucket_corr": cross,
        "autocorr_multiframe": mf,
    }


def summarise(payload: dict) -> dict:
    ac = payload["autocorr_per_bucket"]
    cross = payload["cross_bucket_corr"]
    out = {
        "symbol": payload["symbol"],
        "n_days_autocorr": int(ac["date"].nunique()) if len(ac) else 0,
        "ac_lag1_median": float(ac["ac_lag1"].median()) if len(ac) else float("nan"),
        "ac_lag1_mean": float(ac["ac_lag1"].mean()) if len(ac) else float("nan"),
        "ac_lag1_p_negative": float((ac["ac_lag1"] < 0).mean()) if len(ac) else float("nan"),
        "ac_lag2_median": float(ac["ac_lag2"].median()) if len(ac) else float("nan"),
        "ac_lag5_median": float(ac["ac_lag5"].median()) if len(ac) else float("nan"),
        "ac_lag15_median": float(ac["ac_lag15"].median()) if len(ac) else float("nan"),
        "ac_lag60_median": float(ac["ac_lag60"].median()) if len(ac) else float("nan"),
    }
    if len(cross):
        for (src, dst), grp in cross.groupby(["src", "dst"]):
            out[f"cross_{src}_to_{dst}_mean"] = float(grp["corr"].mean())
            out[f"cross_{src}_to_{dst}_mean_inverse"] = float(grp["corr_inverse"].mean())
            out[f"cross_{src}_to_{dst}_n"] = int(len(grp))
    return out


def stability_check(payload: dict) -> pd.DataFrame:
    """Stabilité année × année de l'autocorr minute-par-minute (lag 1)."""
    ac = payload["autocorr_per_bucket"].copy()
    if not len(ac):
        return ac
    ac["date"] = pd.to_datetime(ac["date"])
    ac["year"] = ac["date"].dt.year
    out = (
        ac.groupby("year")
        .agg(
            n=("ac_lag1", "size"),
            median_ac1=("ac_lag1", "median"),
            mean_ac1=("ac_lag1", "mean"),
            median_ac2=("ac_lag2", "median"),
            median_ac5=("ac_lag5", "median"),
        )
        .reset_index()
    )
    return out


def multiframe_summary(payload: dict) -> pd.DataFrame:
    """Stabilité autocorr par bar size × année × bucket."""
    mf = payload["autocorr_multiframe"].copy()
    if not len(mf):
        return mf
    mf["date"] = pd.to_datetime(mf["date"])
    mf["year"] = mf["date"].dt.year
    return (
        mf.groupby(["bar_min", "year"])
        .agg(n=("ac_lag1", "size"), median_ac1=("ac_lag1", "median"))
        .reset_index()
    )


def main() -> None:
    rows = []
    stab_rows = []
    mf_rows = []
    for symbol in SYMBOLS:
        payload = build_payload(symbol)
        s = summarise(payload)
        rows.append(s)
        stab = stability_check(payload)
        stab["symbol"] = symbol
        stab_rows.append(stab)
        mf = multiframe_summary(payload)
        mf["symbol"] = symbol
        mf_rows.append(mf)
    summary = pd.DataFrame(rows)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    summary.to_csv(ASSET_DIR / "2026-10-14-axe-1-summary.csv", index=False)
    pd.concat(stab_rows).to_csv(
        ASSET_DIR / "2026-10-14-axe-1-stability.csv", index=False
    )
    pd.concat(mf_rows).to_csv(
        ASSET_DIR / "2026-10-14-axe-1-multiframe.csv", index=False
    )
    print("=== summary ===")
    print(summary.to_string(index=False))
    print("\n=== stability (year × symbol) ===")
    print(pd.concat(stab_rows).to_string(index=False))
    print("\n=== multiframe (bar × year × symbol) ===")
    print(pd.concat(mf_rows).to_string(index=False))


if __name__ == "__main__":
    main()
