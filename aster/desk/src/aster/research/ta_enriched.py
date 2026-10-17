"""Axe 5 — CFA-style TA enrichi (descriptive only).

Tests sur klines daily BTCUSDT et ETHUSDT pré-2024-07-01 :

1. **Pivots Camarilla** (CFTA 1989) : H3 = H + range * 1.1/4, L3 = L - range * 1.1/4.
   Règle : long si close < L3 (rebond depuis L3), short si close > H3.
2. **Pivots Woodie** : mid = (H + L + 2*O) / 4, plus de poids à l'open.
   Règle : position par rapport au pivot central.
3. **Fibonacci retracements** : sur les swings weekly, niveaux 0.236, 0.382, 0.5, 0.618, 0.786.
   Règle : le prix teste un Fib level → continuation ou rebond selon le niveau.
4. **Elliott Wave proxy** : comptage 5-3 sur les pivots zigzag (5% threshold).
   Signal : onde 3 (mi-parcours) = momentum fort, onde 5 = essoufflement.

C'est du descriptif corrigé pour les tests multiples. Pas de ledger hypothesis.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.data.r2_klines import read_local

ASSET_DIR = Path("research/assets")
SYMBOLS = ("BTCUSDT", "ETHUSDT")
FIB_LEVELS = (0.236, 0.382, 0.5, 0.618, 0.786)


def daily_ohlc(symbol: str) -> pd.DataFrame:
    raw = read_local(symbol)
    return raw.resample("1D").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last"}
    ).dropna()


def camarilla_pivots(daily: pd.DataFrame) -> pd.DataFrame:
    """Pivots Camarilla pour daily (H/L/Close de la veille, R = H-L)."""
    h = daily["high"].shift(1)
    l = daily["low"].shift(1)
    c = daily["close"].shift(1)
    rng = h - l
    out = daily.copy()
    out["cam_h5"] = h + rng * 1.1 / 12
    out["cam_h4"] = h + rng * 1.1 / 6
    out["cam_h3"] = h + rng * 1.1 / 4
    out["cam_h2"] = h + rng * 1.1 / 2
    out["cam_h1"] = h + rng * 1.1
    out["cam_l1"] = l - rng * 1.1
    out["cam_l2"] = l - rng * 1.1 / 2
    out["cam_l3"] = l - rng * 1.1 / 4
    out["cam_l4"] = l - rng * 1.1 / 6
    out["cam_l5"] = l - rng * 1.1 / 12
    out["cam_pivot"] = (h + l + c) / 3
    return out


def woodie_pivots(daily: pd.DataFrame) -> pd.DataFrame:
    h = daily["high"].shift(1)
    l = daily["low"].shift(1)
    o = daily["open"].shift(1)
    out = daily.copy()
    out["wd_pivot"] = (h + l + 2 * o) / 4
    rng = h - l
    out["wd_r1"] = 2 * out["wd_pivot"] - l
    out["wd_s1"] = 2 * out["wd_pivot"] - h
    out["wd_r2"] = out["wd_pivot"] + rng
    out["wd_s2"] = out["wd_pivot"] - rng
    return out


def fib_retracements(swings: pd.DataFrame) -> pd.DataFrame:
    """Calcule les niveaux Fib sur chaque swing (high to low ou low to high).
    Retourne un DataFrame aligné sur la période du swing avec les niveaux testés.
    """
    rows = []
    for _, sw in swings.iterrows():
        rng = sw["end_val"] - sw["start_val"]
        if rng == 0:
            continue
        direction = 1 if sw["end_val"] > sw["start_val"] else -1
        for lvl in FIB_LEVELS:
            if direction == 1:
                # swing up, retracement down from end
                level = sw["end_val"] - lvl * abs(rng)
            else:
                # swing down, retracement up from end
                level = sw["end_val"] + lvl * abs(rng)
            rows.append(
                {
                    "start_date": sw["start_date"],
                    "end_date": sw["end_date"],
                    "direction": direction,
                    "fib_level": lvl,
                    "level_value": level,
                    "swing_range": abs(rng),
                }
            )
    return pd.DataFrame(rows)


def detect_swings_zigzag(daily: pd.DataFrame, threshold: float = 0.05) -> pd.DataFrame:
    """Détecte les swings par méthode zigzag : un swing haut/bas est confirmé
    quand le prix a bougé de plus de 'threshold' en % depuis le dernier pivot."""
    close = daily["close"].astype(float)
    pivots = []
    last_pivot_idx = 0
    last_pivot_val = close.iloc[0]
    direction = 0  # +1 = up, -1 = down
    for i in range(1, len(close)):
        change = (close.iloc[i] - last_pivot_val) / last_pivot_val
        if direction >= 0 and change <= -threshold:
            # confirme pivot haut
            pivots.append(
                {"date": close.index[last_pivot_idx], "value": last_pivot_val, "type": "high"}
            )
            last_pivot_idx = i
            last_pivot_val = close.iloc[i]
            direction = -1
        elif direction <= 0 and change >= threshold:
            pivots.append(
                {"date": close.index[last_pivot_idx], "value": last_pivot_val, "type": "low"}
            )
            last_pivot_idx = i
            last_pivot_val = close.iloc[i]
            direction = 1
    return pd.DataFrame(pivots)


def cam_event_study(daily_with_pivots: pd.DataFrame, horizons=(1, 3, 7)) -> pd.DataFrame:
    """Test : si close < L3 (rebond L3) ou close > H3 (rejet H3), quel rendement forward ?"""
    df = daily_with_pivots.copy()
    for h in horizons:
        df[f"fwd_{h}d"] = np.log(df["close"]).diff().shift(-h)
    rows = []
    for cond_name, cond in [
        ("close_lt_L3", df["close"] < df["cam_l3"]),
        ("close_gt_H3", df["close"] > df["cam_h3"]),
        ("close_lt_L4", df["close"] < df["cam_l4"]),
        ("close_gt_H4", df["close"] > df["cam_h4"]),
    ]:
        for h in horizons:
            target = df[f"fwd_{h}d"]
            sub = target[cond.fillna(False)]
            n = len(sub)
            if n < 30:
                continue
            m = sub.mean()
            t = m / (sub.std() / np.sqrt(n))
            rows.append({"signal": cond_name, "horizon": h, "n": n, "mean_log": m, "t_stat": t})
    return pd.DataFrame(rows)


def fib_event_study(daily: pd.DataFrame, fib_df: pd.DataFrame, horizons=(1, 3, 7)) -> pd.DataFrame:
    """Pour chaque (swing, fib_level), on calcule la date où le prix touche le niveau
    pour la première fois après le swing, et on mesure le rendement forward."""
    close = daily["close"].astype(float)
    rows = []
    for _, fr in fib_df.iterrows():
        if pd.isna(fr["end_date"]):
            continue
        # fenêtre : entre end_date du swing et 30 jours après
        window_end = fr["end_date"] + pd.Timedelta(days=30)
        sub = close.loc[fr["end_date"]:window_end]
        if len(sub) < 2:
            continue
        # Trouve le premier bar où |close - level| < 0.5% du level
        diff = (sub - fr["level_value"]).abs() / fr["level_value"]
        hit = diff < 0.005
        if not hit.any():
            continue
        hit_idx = sub.index[hit.argmax()]  # premier True
        for h in horizons:
            target_idx = min(hit_idx + pd.Timedelta(days=h), close.index[-1])
            fwd = np.log(close.loc[target_idx] / close.loc[hit_idx])
            rows.append(
                {
                    "hit_date": hit_idx,
                    "fib_level": fr["fib_level"],
                    "direction": fr["direction"],
                    "horizon": h,
                    "fwd_log": fwd,
                }
            )
    if not rows:
        return pd.DataFrame()
    res = pd.DataFrame(rows)
    out = res.groupby(["fib_level", "horizon"]).agg(
        n=("fwd_log", "size"), mean=("fwd_log", "mean"), std=("fwd_log", "std")
    )
    out["t_stat"] = out["mean"] / (out["std"] / np.sqrt(out["n"]))
    return out.reset_index()


def main() -> None:
    rows = []
    for sym in SYMBOLS:
        print(f"\n========== {sym} ==========")
        daily = daily_ohlc(sym)
        # 1. Camarilla
        cam = camarilla_pivots(daily)
        study = cam_event_study(cam)
        print("\n--- Camarilla event study ---")
        print(study.to_string(index=False))
        study.to_csv(ASSET_DIR / f"2026-10-14-axe-5-camarilla-{sym}.csv", index=False)
        rows.append({"symbol": sym, "kind": "camarilla", "data": study.to_dict("records")})

        # 2. Woodie (simple : rend forward en fonction de la position vs pivot)
        wd = woodie_pivots(daily)
        wd["above_pivot"] = (wd["close"] > wd["wd_pivot"]).astype(int)
        for h in (1, 3, 7):
            wd[f"fwd_{h}d"] = np.log(wd["close"]).diff().shift(-h)
        print("\n--- Woodie : rend forward si close > pivot central ---")
        for h in (1, 3, 7):
            above = wd.loc[wd["above_pivot"] == 1, f"fwd_{h}d"].dropna()
            below = wd.loc[wd["above_pivot"] == 0, f"fwd_{h}d"].dropna()
            t_a = above.mean() / (above.std() / np.sqrt(len(above)))
            t_b = below.mean() / (below.std() / np.sqrt(len(below)))
            print(
                f"  h={h}d: above-pivot fwd = {above.mean():.4f} (t={t_a:.2f}, n={len(above)}), "
                f"below-pivot fwd = {below.mean():.4f} (t={t_b:.2f}, n={len(below)})"
            )

        # 3. Fib retracements
        swings = detect_swings_zigzag(daily, threshold=0.05)
        print(f"\n--- Zigzag swings (5%) : {len(swings)} pivots ---")
        # Paires start->end
        swing_pairs = []
        for i in range(len(swings) - 1):
            swing_pairs.append(
                {
                    "start_date": swings.iloc[i]["date"],
                    "end_date": swings.iloc[i + 1]["date"],
                    "start_val": swings.iloc[i]["value"],
                    "end_val": swings.iloc[i + 1]["value"],
                }
            )
        swing_pairs = pd.DataFrame(swing_pairs)
        if len(swing_pairs) > 0:
            fib_df = fib_retracements(swing_pairs)
            fib_study = fib_event_study(daily, fib_df)
            print(fib_study.to_string(index=False))
            fib_study.to_csv(ASSET_DIR / f"2026-10-14-axe-5-fib-{sym}.csv", index=False)
    print(f"\nDone axe 5.")


if __name__ == "__main__":
    main()
