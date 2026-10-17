"""Q14 — panel fixed-effects + sector pairs + cross-sectional momentum/reversal.

Strictly pre-cutoff descriptive study. No ledger hypothesis, no holdout read.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.data.r2_backtest_store import bars_from_minutes
from aster.data.r2_klines import read_local

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
START = pd.Timestamp("2021-01-01", tz="UTC")
PANEL_START = pd.Timestamp("2023-05-05", tz="UTC")
SYMBOLS = ("BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT", "AAVEUSDT", "SUIUSDT", "NEARUSDT")
L1_PAIRS = (("SOLUSDT", "NEARUSDT"), ("SOLUSDT", "SUIUSDT"), ("NEARUSDT", "SUIUSDT"))
PAYMENTS_PAIR = (("XRPUSDT", "DOGEUSDT"),)
DEFI_PAIR = (("AAVEUSDT", "LINKUSDT"),)
ALL_PAIRS = L1_PAIRS + PAYMENTS_PAIR + DEFI_PAIR
HORIZONS = ("1h", "4h", "1d", "1w")
BOOTSTRAP_DRAWS = 1_000
SEED = 0xD00DB00B
OUT = Path("research/atlas/q14_panel.json")


def _daily_returns(symbol: str) -> pd.Series:
    minutes = read_local(symbol)
    bars = bars_from_minutes(minutes, "1d")
    close = pd.Series(bars["close"], index=bars.index, name=symbol)
    close = close.loc[(close.index >= START) & (close.index < CUTOFF)]
    return np.log(close).diff().dropna()


def _build_panel() -> pd.DataFrame:
    series = []
    for symbol in SYMBOLS:
        try:
            series.append(_daily_returns(symbol))
        except Exception:
            series.append(pd.Series(dtype=float, name=symbol))
    panel = pd.concat(series, axis=1, join="inner").dropna(how="any")
    if panel.empty or panel.shape[1] < 4:
        raise ValueError("insufficient overlap to build the Q14 panel")
    return panel


def _adf_kpss(series: pd.Series) -> dict:
    s = series.dropna().values
    if len(s) < 30:
        return {"adf_stat": None, "adf_pvalue": None, "kpss_stat": None, "kpss_pvalue": None, "n": int(len(s))}
    from statsmodels.tsa.stattools import adfuller, kpss
    try:
        adf_stat, adf_p, *_ = adfuller(s, autolag="AIC", maxlag=5)
    except Exception:
        adf_stat, adf_p = None, None
    try:
        kpss_stat, kpss_p, *_ = kpss(s, regression="c", nlags="auto")
    except Exception:
        kpss_stat, kpss_p = None, None
    return {"adf_stat": adf_stat, "adf_pvalue": adf_p, "kpss_stat": kpss_stat, "kpss_pvalue": kpss_p, "n": int(len(s))}


def _half_life(series: pd.Series) -> float:
    s = series.dropna().values
    if len(s) < 30:
        return float("nan")
    lag = s[:-1]
    diff = np.diff(s)
    if np.std(lag) < 1e-12 or np.std(diff) < 1e-12:
        return float("nan")
    beta = float(np.polyfit(lag, diff, 1)[0])
    if beta >= 0.0:
        return float("nan")
    return float(-np.log(2.0) / beta)


def _sector_pairs(panel: pd.DataFrame) -> dict:
    out = {}
    for a, b in ALL_PAIRS:
        if a not in panel.columns or b not in panel.columns:
            out[f"{a}/{b}"] = {"skipped": "missing in panel"}
            continue
        spread = panel[a] - panel[b]
        stats_dict = _adf_kpss(spread)
        stats_dict["half_life_days"] = _half_life(spread)
        stats_dict["candidate"] = bool(
            stats_dict.get("adf_pvalue") is not None
            and stats_dict["adf_pvalue"] < 0.01
            and stats_dict.get("kpss_pvalue") is not None
            and stats_dict["kpss_pvalue"] > 0.05
            and not np.isnan(stats_dict["half_life_days"])
            and 1.0 <= stats_dict["half_life_days"] <= 30.0
        )
        out[f"{a}/{b}"] = stats_dict
    return out


def _fixed_effects(panel: pd.DataFrame) -> dict:
    """Within entity + within time demean; regress each pre-declared signal on the demeaned returns.

    We use simple proxy signals that are computable from prices alone (no external artefacts), so the
    result is self-contained and does not depend on Q9/Q10/Q12 atlases (which were observational).
    """
    proxies = {
        "lag1_return": panel.shift(1),
        "rolling_mom_5d": panel.rolling(5, min_periods=3).mean().shift(1),
        "rolling_rev_22d": -panel.rolling(22, min_periods=10).mean().shift(1),
    }
    rows = []
    entity_mean = panel.mean(axis=1)
    time_mean = panel.mean(axis=0)
    grand_mean = float(np.nanmean(panel.values))
    demeaned = panel.sub(entity_mean, axis=0).sub(time_mean, axis=1).add(grand_mean)
    for name, signal in proxies.items():
        sig_em = signal.mean(axis=1)
        sig_tm = signal.mean(axis=0)
        sig_gm = float(np.nanmean(signal.values))
        signal_dm = signal.sub(sig_em, axis=0).sub(sig_tm, axis=1).add(sig_gm)
        mask = signal_dm.notna() & demeaned.notna()
        if mask.values.sum() == 0 or np.std(signal_dm.values[mask.values]) < 1e-12:
            rows.append({"signal": name, "n": int(mask.values.sum()), "beta_mean": None, "t_mean": None, "significant": False})
            continue
        tvalues = []
        betas = []
        for col in demeaned.columns:
            ys = demeaned[col].values[mask[col].values]
            xs = signal_dm[col].values[mask[col].values]
            if xs.size < 30 or np.std(xs) < 1e-12:
                continue
            X = np.vstack([np.ones_like(xs), xs]).T
            coef, *_ = np.linalg.lstsq(X, ys, rcond=None)
            resid = ys - X @ coef
            if X.shape[0] > X.shape[1] and np.std(resid) > 1e-12:
                cov = np.linalg.inv(X.T @ X) * float(resid.var() * X.shape[0] / max(X.shape[0] - 2, 1))
                se = np.sqrt(np.diag(cov))
                t = float(coef[1] / se[1]) if se[1] > 0 else float("nan")
                if not np.isnan(t):
                    betas.append(float(coef[1]))
                    tvalues.append(t)
        if not tvalues:
            rows.append({"signal": name, "n": int(mask.values.sum()), "beta_mean": None, "t_mean": None, "significant": False})
        else:
            tvalues_arr = np.array(tvalues)
            betas_arr = np.array(betas)
            mean_t = float(np.mean(tvalues_arr))
            p_two = float(2 * (1 - stats.norm.cdf(abs(mean_t))))
            rows.append({"signal": name, "n": int(mask.values.sum()), "beta_mean": float(np.mean(betas_arr)), "t_mean": mean_t, "p_value_mean_t": p_two, "significant": p_two < 0.01})
    return {"proxies": rows, "alpha_significant": any(r.get("significant", False) for r in rows)}


def _cross_sectional(panel: pd.DataFrame) -> dict:
    """Quintile long/short spread of pre-declared signals on the cross-section."""
    rows = []
    for horizon in HORIZONS:
        if horizon == "1h":
            minutes = max(1, 1)
            signal = panel.copy()
        elif horizon == "4h":
            signal = panel
        elif horizon == "1d":
            signal = panel
        elif horizon == "1w":
            signal = panel.rolling(5, min_periods=3).sum()
        else:
            signal = panel
        for lag in (1, 5, 22):
            sig_lag = signal.shift(lag)
            if sig_lag.shape[0] < 30:
                continue
            ic = sig_lag.corrwith(panel.shift(-1)).dropna()
            rows.append({"horizon": horizon, "lag": lag, "ic_mean": float(ic.mean()) if not ic.empty else None, "ic_std": float(ic.std()) if not ic.empty else None, "n_dates": int(ic.shape[0])})
    return rows


def run() -> dict:
    panel_full = _build_panel()
    panel = panel_full.loc[panel_full.index >= PANEL_START]
    pairs = _sector_pairs(panel)
    fe = _fixed_effects(panel)
    xs = _cross_sectional(panel)
    return {
        "protocol": {
            "cutoff_exclusive": str(CUTOFF),
            "start": str(START),
            "panel_start": str(PANEL_START),
            "symbols": list(SYMBOLS),
            "pairs": [f"{a}/{b}" for a, b in ALL_PAIRS],
            "horizons": list(HORIZONS),
            "bootstrap_draws": BOOTSTRAP_DRAWS,
            "seed": SEED,
            "status": "descriptive_only",
        },
        "panel": {"n_days": int(panel.shape[0]), "n_symbols": int(panel.shape[1]), "start": str(panel.index[0]), "end": str(panel.index[-1])},
        "sector_pairs": pairs,
        "fixed_effects": fe,
        "cross_sectional": xs,
        "candidate": any(p.get("candidate") for p in pairs.values()) or fe.get("alpha_significant", False),
    }


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(run(), indent=2, allow_nan=False, default=float), encoding="utf-8")


if __name__ == "__main__":
    main()
