"""Axe 3 — Mean-reversion OU + half-life + pairs (descriptive only).

Tests sur klines daily pré-2024-07-01 :

1. **OU half-life** : pour chaque série (BTC, ETH) et le spread BTC-ETH,
   on estime le coefficient de régression AR(1) sur rolling window 252j
   et on calcule le half-life = log(0.5) / log(phi) si |phi| < 1.
2. **ADF sur le spread** : Augmented Dickey-Fuller sur BTC-ETH spread
   (et autres paires d'alts) pour tester la stationnarité.
3. **Filter** : paires avec ADF p < 0.05 et half-life ∈ [5, 60] jours.

Si la moitié des fenêtres rolling donnent un phi stationnaire, c'est un signal
de mean-reversion lente. Si la majorité des fenêtres donnent phi >= 1, c'est
un signal de marche aléatoire / momentum, pas de pairs.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.data.r2_klines import read_local

ASSET_DIR = Path("research/assets")
SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "LINKUSDT", "XRPUSDT")
WINDOW = 252  # ~1y rolling
HALFLIFE_MIN = 5
HALFLIFE_MAX = 60


def daily_close(symbol: str) -> pd.Series:
    raw = read_local(symbol)
    return raw["close"].astype(float).resample("1D").last().dropna()


def ou_halflife(series: pd.Series, window: int = WINDOW) -> pd.DataFrame:
    """Estimate phi and half-life on rolling windows via AR(1) OLS."""
    rows = []
    y = np.log(series).diff().dropna()
    x = y.shift(1).dropna()
    y = y.loc[x.index]
    for i in range(window, len(x) + 1):
        xx = x.iloc[i - window:i]
        yy = y.iloc[i - window:i]
        # AR(1): y_t = a + b * y_{t-1} + eps
        b, a, r, p, se = stats.linregress(xx.values, yy.values)
        if 0 < b < 0.999:
            hl = np.log(0.5) / np.log(b)
        else:
            hl = np.nan
        rows.append({"end_date": x.index[i - 1], "phi": b, "halflife": hl})
    return pd.DataFrame(rows)


def adf_test_simple(series: pd.Series) -> dict:
    """Augmented Dickey-Fuller simplifié (régression sur Δy = a + b*y_{t-1} + sum)
    Ici version sans lags (rho=0) pour vitesse : suffisant pour screening."""
    y = series.dropna().values
    dy = np.diff(y)
    y_lag = y[:-1]
    # dy = a + b*y_lag
    b, a, r, p, se = stats.linregress(y_lag, dy)
    # H0: b=0 (unit root), H1: b<0 (stationary)
    t_stat = b / se
    # p-value approx pour test bilatéral t-Student grand n
    n = len(y_lag)
    p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df=n - 2))
    return {"adf_stat": t_stat, "p_value": p_val, "n": n, "rho": b}


def adf_with_lag(series: pd.Series, max_lag: int = 5) -> dict:
    """ADF avec lags (Δy_t = a + b*y_{t-1} + sum γ_i Δy_{t-i}).
    Pour screening, max_lag=5 AIC-style."""
    y = series.dropna().values.astype(float)
    if len(y) < max_lag + 30:
        return {"adf_stat": float("nan"), "p_value": float("nan"), "n": int(len(y))}
    dy = np.diff(y)  # length n
    n = len(dy)
    y_lag = y[:-1]  # length n
    # Δy_t = a + b*y_{t-1} + sum γ_i Δy_{t-i}, pour t = max_lag..n-1
    n_eff = n - max_lag
    Y = dy[max_lag:]  # length n_eff
    ones = np.ones(n_eff)
    ylag = y_lag[max_lag:]  # aligner sur Y
    X_cols = [ones, ylag]
    for k in range(1, max_lag + 1):
        # Δy_{t-k} pour t = max_lag..n-1 → indices max_lag - k .. n_eff - 1 + (max_lag - k)
        # Simplifier : on prend dy[max_lag - k : n - k]
        X_cols.append(dy[max_lag - k : n - k])
    X = np.column_stack(X_cols)
    if X.shape[0] != Y.shape[0]:
        # Réaligner : tronquer à la plus petite longueur
        L = min(X.shape[0], Y.shape[0])
        X = X[:L]
        Y = Y[:L]
    else:
        L = X.shape[0]
    beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
    residuals = Y - X @ beta
    sigma2 = float(np.sum(residuals ** 2)) / max(L - max_lag - 2, 1)
    try:
        cov = sigma2 * np.linalg.inv(X.T @ X)
    except np.linalg.LinAlgError:
        return {"adf_stat": float("nan"), "p_value": float("nan"), "n": L}
    se_b = float(np.sqrt(cov[1, 1])) if cov[1, 1] > 0 else float("nan")
    if not np.isfinite(se_b) or se_b == 0:
        return {"adf_stat": float("nan"), "p_value": float("nan"), "n": L}
    t_stat = float(beta[1] / se_b)
    p_val = float(2 * (1 - stats.t.cdf(abs(t_stat), df=max(L - max_lag - 2, 1))))
    return {"adf_stat": t_stat, "p_value": p_val, "n": L}


def cointegration_test(a: pd.Series, b: pd.Series) -> dict:
    """Test de Engle-Granger simplifié : régression OLS log(a) = α + β log(b),
    puis ADF sur les résidus."""
    df = pd.concat([np.log(a), np.log(b)], axis=1, keys=["a", "b"]).dropna()
    if len(df) < 100:
        return {"beta": float("nan"), "spread_adf_p": float("nan"), "n": len(df)}
    beta, alpha, r, p, se = stats.linregress(df["b"].values, df["a"].values)
    spread = df["a"] - alpha - beta * df["b"]
    adf = adf_with_lag(spread, max_lag=5)
    return {"beta": beta, "alpha": alpha, "r2": r ** 2, "spread_adf_p": adf["p_value"], "n": len(df)}


def main() -> None:
    out_rows = []
    closes = {sym: daily_close(sym) for sym in SYMBOLS}

    # 1. OU half-life par série
    print("=== OU half-life (rolling 252j) ===")
    for sym, c in closes.items():
        hl_df = ou_halflife(c)
        valid = hl_df["halflife"].dropna()
        if len(valid) == 0:
            continue
        median = valid.median()
        pct_mean_reverting = ((hl_df["phi"] > 0) & (hl_df["phi"] < 0.999)).mean()
        pct_window_ok = ((valid >= HALFLIFE_MIN) & (valid <= HALFLIFE_MAX)).mean()
        print(f"{sym}: median HL = {median:.1f}j, MR windows = {pct_mean_reverting:.1%}, HL in [5,60] = {pct_window_ok:.1%}")
        out_rows.append(
            {
                "kind": "ou_halflife",
                "asset_or_pair": sym,
                "median_halflife_days": median,
                "pct_mean_reverting": pct_mean_reverting,
                "pct_hl_5_60": pct_window_ok,
            }
        )
        hl_df.to_csv(ASSET_DIR / f"2026-10-14-axe-3-ou-hl-{sym}.csv", index=False)

    # 2. Cointegration BTC-ETH et autres paires
    print("\n=== Cointegration tests (Engle-Granger) ===")
    pairs = [
        ("BTCUSDT", "ETHUSDT"),
        ("ETHUSDT", "SOLUSDT"),
        ("ETHUSDT", "LINKUSDT"),
        ("BTCUSDT", "BNBUSDT"),
        ("BTCUSDT", "XRPUSDT"),
        ("ETHUSDT", "XRPUSDT"),
    ]
    coint_rows = []
    for sym_a, sym_b in pairs:
        a = closes[sym_a].reindex(closes[sym_b].index).dropna()
        b = closes[sym_b].reindex(closes[sym_a].index).dropna()
        coint = cointegration_test(a, b)
        print(
            f"{sym_a}/{sym_b}: beta={coint['beta']:.3f}, r2={coint.get('r2', 0):.3f}, "
            f"spread ADF p={coint['spread_adf_p']:.4f}, n={coint['n']}"
        )
        out_rows.append(
            {
                "kind": "cointegration",
                "asset_or_pair": f"{sym_a}/{sym_b}",
                "beta": coint["beta"],
                "r2": coint.get("r2", 0),
                "spread_adf_p": coint["spread_adf_p"],
                "n": coint["n"],
            }
        )
        coint_rows.append(
            {
                "pair": f"{sym_a}/{sym_b}",
                "a": sym_a,
                "b": sym_b,
                "beta": coint["beta"],
                "r2": coint.get("r2", 0),
                "spread_adf_p": coint["spread_adf_p"],
                "n": coint["n"],
            }
        )

    # 2b. BH-FDR sur les 6 p-valeurs
    coint_df = pd.DataFrame(coint_rows).sort_values("spread_adf_p")
    m = len(coint_df)
    coint_df["rank"] = np.arange(1, m + 1)
    coint_df["bh_threshold"] = coint_df["rank"] / m * 0.05
    coint_df["bh_reject"] = coint_df["spread_adf_p"] <= coint_df["bh_threshold"]
    print("\n=== BH-FDR (q=0.05) sur ADF p-values ===")
    print(coint_df[["pair", "spread_adf_p", "rank", "bh_threshold", "bh_reject"]].to_string(index=False))

    # 3. Stabilité rolling 252j de la cointégration BTC/ETH
    print("\n=== Rolling coint (BTC/ETH, window=252j) ===")
    a = closes["BTCUSDT"].reindex(closes["ETHUSDT"].index).dropna()
    b = closes["ETHUSDT"].reindex(closes["BTCUSDT"].index).dropna()
    log_a = np.log(a)
    log_b = np.log(b)
    roll_rows = []
    for i in range(252, len(log_a) + 1):
        la = log_a.iloc[i - 252:i].values
        lb = log_b.iloc[i - 252:i].values
        beta, alpha, r, p, se = stats.linregress(lb, la)
        spread = la - alpha - beta * lb
        adf = adf_with_lag(pd.Series(spread), max_lag=3)
        roll_rows.append(
            {
                "end_date": log_a.index[i - 1],
                "beta": beta,
                "r2": r ** 2,
                "adf_p": adf["p_value"],
            }
        )
    roll_df = pd.DataFrame(roll_rows)
    roll_df.to_csv(ASSET_DIR / "2026-10-14-axe-3-rolling-coint-BTC-ETH.csv", index=False)
    pct_stationary = (roll_df["adf_p"] < 0.05).mean()
    pct_beta_in_range = ((roll_df["beta"] > 0.4) & (roll_df["beta"] < 1.0)).mean()
    print(
        f"BTC/ETH: {pct_stationary:.1%} of windows stationary, beta in [0.4, 1.0] = {pct_beta_in_range:.1%}, "
        f"median beta = {roll_df['beta'].median():.3f}"
    )

    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(out_rows).to_csv(
        ASSET_DIR / "2026-10-14-axe-3-summary.csv", index=False
    )
    coint_df.to_csv(ASSET_DIR / "2026-10-14-axe-3-bh-fdr.csv", index=False)
    print(f"\nSaved {len(out_rows)} rows.")


if __name__ == "__main__":
    main()
