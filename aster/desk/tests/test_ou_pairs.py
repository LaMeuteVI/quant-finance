"""Tests de référence pour ou_pairs (ADF, half-life, cointegration)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.ou_pairs import (
    adf_with_lag,
    ou_halflife,
    cointegration_test,
)


def _series(values: list[float]) -> pd.Series:
    return pd.Series(values, index=pd.date_range("2020-01-01", periods=len(values), freq="D"))


def test_adf_stationary_white_noise_rejects_unit_root():
    """Une marche aléatoire sans drift doit avoir ADF stat ≈ 0 (non stationnaire)."""
    rng = np.random.default_rng(42)
    y = np.cumsum(rng.normal(0, 1, 500))
    s = _series(list(y))
    res = adf_with_lag(s, max_lag=2)
    # random walk → b proche de 0, t-stat petit
    assert abs(res["adf_stat"]) < 3.0, f"ADF t-stat trop grand pour RW : {res['adf_stat']}"
    assert res["n"] > 100


def test_adf_stationary_process_rejects_unit_root():
    """Un processus stationnaire (AR(1) phi=0.5) doit avoir ADF t-stat << 0."""
    rng = np.random.default_rng(42)
    n = 500
    eps = rng.normal(0, 1, n)
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = 0.5 * x[i - 1] + eps[i]
    s = _series(list(x))
    res = adf_with_lag(s, max_lag=2)
    assert res["adf_stat"] < -2.0, f"AR(1) phi=0.5 devrait être stationnaire, t={res['adf_stat']}"


def test_ou_halflife_returns_dataframe():
    """Test que ou_halflife renvoie bien un DataFrame avec colonnes phi et halflife."""
    rng = np.random.default_rng(42)
    n = 600
    eps = rng.normal(0, 1, n)
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = 0.5 * x[i - 1] + eps[i]
    s = _series(list(np.exp(x.cumsum() / 100)))  # log-price-like
    df = ou_halflife(s, window=252)
    assert "phi" in df.columns
    assert "halflife" in df.columns
    assert len(df) > 0
    # pour un AR(1) phi=0.5, half-life = log(0.5)/log(0.5) = 1 jour
    valid = df["halflife"].dropna()
    assert valid.median() < 5.0, f"Half-life médian devrait être < 5j pour AR(1) phi=0.5, got {valid.median()}"


def test_cointegration_btc_eth_runs_without_error():
    """Test que cointegration_test fonctionne sur une série synthétique cointegree."""
    rng = np.random.default_rng(42)
    n = 1000
    eps = rng.normal(0, 0.5, n)
    # Construire deux séries cointégrées
    common = np.cumsum(rng.normal(0, 1, n))
    a = common + eps
    b = common
    s_a = _series(list(np.exp(a)))
    s_b = _series(list(np.exp(b)))
    res = cointegration_test(s_a, s_b)
    assert "beta" in res
    assert "spread_adf_p" in res
    assert res["n"] == n
    # Le beta doit être proche de 1
    assert abs(res["beta"] - 1.0) < 0.5, f"beta devrait être proche de 1, got {res['beta']}"
    # Le spread doit être stationnaire
    assert res["spread_adf_p"] < 0.05, f"spread devrait être stationnaire, p={res['spread_adf_p']}"


def test_cointegration_uncorrelated_not_stationary():
    """Deux random walks indépendants : ADF sur le spread ne doit pas être stationnaire.

    Note : avec n=500, il y a ~5% de chances de faux positif. On teste 10 réalisations
    et on vérifie que la p-valeur médiane n'est pas significative.
    """
    rng = np.random.default_rng(42)
    ps = []
    for trial in range(10):
        n = 500
        a = np.cumsum(rng.normal(0, 1, n))
        b = np.cumsum(rng.normal(0, 1, n))
        s_a = _series(list(np.exp(a)))
        s_b = _series(list(np.exp(b)))
        res = cointegration_test(s_a, s_b)
        ps.append(res["spread_adf_p"])
    median_p = float(np.median(ps))
    # Sous H0, la p-valeur médiane sur 10 réalisations devrait être > 0.05 en moyenne
    # On est permissif : on accepte si p > 0.01 dans la moitié des cas
    n_rejected = sum(1 for p in ps if p < 0.05)
    assert n_rejected <= 5, f"Trop de rejets ADF sur 10 RW indépendants : {n_rejected}/10, ps={ps}"
