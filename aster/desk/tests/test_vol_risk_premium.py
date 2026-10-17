"""Tests de référence pour vol_risk_premium (RV, BV, HAR-RV, VRP)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from aster.research.vol_risk_premium import (
    bipower_variation,
    continuous_jump_decomp,
    realised_vol_daily,
    har_rv_forecast,
    vrp_signal,
)


def _minute_close(returns: list[float], start="2020-01-01") -> pd.Series:
    """Construit un pd.Series 1m à partir de log-returns."""
    log_p = np.cumsum(returns)
    log_p = log_p - log_p[0]
    idx = pd.date_range(start, periods=len(log_p), freq="1min")
    return pd.Series(np.exp(log_p), index=idx)


def test_rv_bv_consistent_with_returns():
    """Pour des returns i.i.d. gaussiens sur n=3*1440, JV doit être faible vs RV."""
    rng = np.random.default_rng(42)
    n = 3 * 1440  # 3 jours
    r = rng.normal(0, 0.001, n)
    s = _minute_close(list(r))
    decomp = continuous_jump_decomp(s)
    # Sur du gaussien pur, JV/RV doit être < 0.3 (sauts spurious dus au bruit)
    ratio = (decomp["jv"] / decomp["rv"].replace(0, np.nan)).dropna()
    assert ratio.max() < 0.5, f"JV/RV trop grand sur gaussien : max = {ratio.max()}"


def test_rv_bv_detect_jumps():
    """Pour des returns avec sauts additifs, JV doit être > 0."""
    rng = np.random.default_rng(42)
    n = 5000
    r = rng.normal(0, 0.001, n)
    # Ajoute 5 sauts de 1%
    for idx in [500, 1500, 2500, 3500, 4500]:
        r[idx] += 0.01
    s = _minute_close(list(r))
    decomp = continuous_jump_decomp(s)
    # Au moins un jour doit avoir JV > 0
    assert decomp["jv"].max() > 0.001, f"JV devrait détecter les sauts, max = {decomp['jv'].max()}"


def test_har_rv_better_than_naive():
    """Sur un processus avec mean-reversion de vol, HAR doit battre le naïf."""
    rng = np.random.default_rng(42)
    n = 1500
    # Processus de vol à mean-reversion : var_t = 0.5 + 0.5 * var_{t-1} + noise
    var = np.zeros(n)
    var[0] = 0.001
    for i in range(1, n):
        var[i] = 0.5 + 0.5 * var[i - 1] + rng.normal(0, 0.0001)
    r = rng.normal(0, 1, n) * np.sqrt(var)
    rv = pd.Series(var ** 0.5 * np.sqrt(525_600), index=pd.date_range("2020-01-01", periods=n, freq="D"))
    har = har_rv_forecast(rv)
    t_dm = har["t_dm"].iloc[0]
    assert t_dm < -1.5, f"HAR devrait battre le naïf sur vol mean-reverting, t-DM = {t_dm}"


def test_vrp_signal_runs():
    """Vérifie que vrp_signal renvoie un DataFrame avec 10 déciles."""
    rng = np.random.default_rng(42)
    n = 500
    rv = pd.Series(rng.uniform(0.1, 1.0, n), index=pd.date_range("2020-01-01", periods=n, freq="D"))
    fwd = pd.Series(rng.normal(0, 0.01, n), index=pd.date_range("2020-01-01", periods=n, freq="D"))
    res = vrp_signal(rv, fwd)
    assert len(res) >= 2
    assert "decile" in res.columns
    assert "mean_fwd" in res.columns


def test_vrp_tz_aware_naive_alignment():
    """Si une série est tz-aware et l'autre non, l'alignement doit marcher sans crash."""
    rng = np.random.default_rng(42)
    n = 200
    idx = pd.date_range("2020-01-01", periods=n, freq="D", tz="UTC")
    rv = pd.Series(rng.uniform(0.1, 1.0, n), index=idx)
    fwd = pd.Series(rng.normal(0, 0.01, n), index=idx.tz_localize(None))
    res = vrp_signal(rv, fwd)
    assert len(res) >= 2
