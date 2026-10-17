"""Axe 2 — Ichimoku Kinko Hyo (descriptive only).

Test systématique des règles Ichimoku (Riguet formation totale) sur klines
daily BTCUSDT et ETHUSDT pré-cutoff 2024-07-01 :

- Tenkan-sen (9-period midpoint)
- Kijun-sen (26-period midpoint)
- Senkou Span A (Tenkan+Kijun)/2 plot 26 forward
- Senkou Span B (52-period midpoint) plot 26 forward
- Chikou span (close plot 26 back)

Trois règles testées :
1. **Cloud trend** : SSA > SSB (tendance haussière) ou SSA < SSB (baissière)
2. **TK cross** : Tenkan croise Kijun (signal d'entrée)
3. **Kijun pullback** : prix revient sur flat Kijun en tendance haussière
4. **Chikou filter** (Riguet ch05) : Chikou span libre d'obstacles (flats SSB, candles) dans la direction du trade

Filtres : aucun ledger hypothesis, aucun backtest, aucun holdout.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from aster.data.r2_klines import read_local

ASSET_DIR = Path("research/assets")
SYMBOLS = ("BTCUSDT", "ETHUSDT")
TENKAN_N = 9
KIJUN_N = 26
SSB_N = 52
DISPLACEMENT = 26


def _midpoint(high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    return (high.rolling(n).max() + low.rolling(n).min()) / 2.0


def ichimoku(daily: pd.DataFrame) -> pd.DataFrame:
    """Calcule les 5 lignes Ichimoku sur un DataFrame daily (OHLC)."""
    high = daily["high"].astype(float)
    low = daily["low"].astype(float)
    close = daily["close"].astype(float)
    tenkan = _midpoint(high, low, TENKAN_N)
    kijun = _midpoint(high, low, KIJUN_N)
    ssa = ((tenkan + kijun) / 2.0).shift(DISPLACEMENT)
    ssb = _midpoint(high, low, SSB_N).shift(DISPLACEMENT)
    chikou = close.shift(-DISPLACEMENT)
    out = daily.copy()
    out["tenkan"] = tenkan
    out["kijun"] = kijun
    out["ssa"] = ssa
    out["ssb"] = ssb
    out["chikou"] = chikou
    out["cloud_top"] = np.maximum(ssa, ssb)
    out["cloud_bot"] = np.minimum(ssa, ssb)
    return out


def _forward_log_return(close: pd.Series, h: int) -> pd.Series:
    return np.log(close).diff().shift(-h)


def _riguet_signals(daily: pd.DataFrame, horizons=(1, 3, 7)) -> pd.DataFrame:
    """Pour chaque jour valide, on calcule :
    - cloud_trend : 1 si SSA > SSB, -1 si SSA < SSB, 0 si plat (diff < seuil)
    - tk_cross : 1 si Tenkan croise Kijun à la hausse, -1 si baisse, 0 sinon
    - chikou_filter_long : 1 si Chikou est au-dessus de tous les obstacles (SSB, flat Kijun, candles)
      sur les DISPLACEMENT derniers bars, et 0 sinon
    - kijun_pullback : 1 si le close est dans la zone ±1% du Kijun plat (Kijun variation < 1% sur 5 bars)
    """
    out = daily.copy()
    ssa = out["ssa"]
    ssb = out["ssb"]
    out["cloud_trend"] = np.sign(ssa - ssb).fillna(0)
    out["ssa_minus_ssb"] = ssa - ssb
    tenkan = out["tenkan"]
    kijun = out["kijun"]
    out["tk_cross"] = np.sign(tenkan - kijun).fillna(0).astype(int)
    out["tk_cross_fresh"] = (
        (np.sign(tenkan - kijun) != np.sign(tenkan.shift(1) - kijun.shift(1)))
        & (np.sign(tenkan - kijun) != 0)
    ).fillna(False).astype(int)
    out["kijun_pullback"] = (
        (kijun.pct_change(5).abs() < 0.01)
        & ((out["close"] - kijun).abs() / kijun < 0.01)
    ).astype(int)
    # chikou = close.shift(-DISPLACEMENT) = close regardé 26 bars en arrière depuis t+26
    # Pour que ce soit causal, il faut que la condition soit vérifiable à t (pas à t+26).
    # Filtre Riguet "Chikou libre d'obstacles" : à t, on regarde le Chikou (=close de t-26 reporté à t)
    # et on vérifie qu'il est au-dessus du close de t-26 et au-dessus de tous les obstacles
    # visibles à t-26 (SSB, Kijun). C'est donc un filtre calculé **à t** sur des données
    # visibles à t (close t-26, SSB/Kijun à t-26).
    # L'astuce : shift(DISPLACEMENT) sur close + recomparaison = exactement le même close vu
    # 26 bars après. Pour la causalité, on doit utiliser close.shift(DISPLACEMENT) (passé)
    # et obstacles.shift(DISPLACEMENT) (passé). Le forward-look de chikou n'apparaît que
    # parce qu'on a shifté close vers l'avant ; on inverse.
    close = out["close"].astype(float)
    out["chikou_causal"] = close.shift(DISPLACEMENT)  # = close de t-26
    cloud_top_past = out["cloud_top"].shift(DISPLACEMENT)
    cloud_bot_past = out["cloud_bot"].shift(DISPLACEMENT)
    out["chikou_filter_long"] = (
        (out["chikou_causal"] > cloud_top_past)
        & (out["chikou_causal"] > close.shift(DISPLACEMENT))
    ).fillna(False).astype(int)
    out["chikou_filter_short"] = (
        (out["chikou_causal"] < cloud_bot_past)
        & (out["chikou_causal"] < close.shift(DISPLACEMENT))
    ).fillna(False).astype(int)
    for h in horizons:
        out[f"fwd_{h}d"] = _forward_log_return(close, h)
    return out


def _event_study(df: pd.DataFrame, signal_col: str, horizons=(1, 3, 7)) -> pd.DataFrame:
    rows = []
    for h in horizons:
        target = df[f"fwd_{h}d"]
        cond = df[signal_col] == 1
        n = int(cond.sum())
        if n < 30:
            rows.append(
                {"signal": signal_col, "horizon": h, "n": n, "mean": float("nan"), "t_stat": float("nan")}
            )
            continue
        m = float(target[cond].mean())
        sd = float(target[cond].std())
        t = m / (sd / np.sqrt(n)) if sd > 0 else 0.0
        rows.append({"signal": signal_col, "horizon": h, "n": n, "mean": m, "t_stat": t})
    return pd.DataFrame(rows)


def build_payload(symbol: str) -> dict:
    raw = read_local(symbol)
    daily = raw.resample("1d").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}
    ).dropna()
    ich = ichimoku(daily)
    rig = _riguet_signals(ich)
    return {"symbol": symbol, "daily_ichimoku": rig}


def main() -> None:
    rows = []
    for symbol in SYMBOLS:
        payload = build_payload(symbol)
        df = payload["daily_ichimoku"]
        # align event study on row where daily_ichimoku is fully populated
        valid = df.dropna(subset=["ssa", "ssb", "chikou", "fwd_7d"])
        for signal in ["tk_cross_fresh", "kijun_pullback", "chikou_filter_long", "chikou_filter_short"]:
            study = _event_study(valid, signal)
            study["symbol"] = symbol
            rows.append(study)
    out = pd.concat(rows)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(ASSET_DIR / "2026-10-14-axe-2-ichimoku-event-study.csv", index=False)
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
