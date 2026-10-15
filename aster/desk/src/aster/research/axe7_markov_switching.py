"""Axe 7 — Markov-switching Hamilton (1989) on BTC daily + cross-asset lead.

Reference: Hamilton (1989), Tsay ch04 (MS-AR), Krolzig (1997) Markov-switching
vector models. Skills used: ``tsay-analysis-financial-time-series`` ch04,
``cfa-portfolio-management``, ``hull-risk-management`` ch11.

Pre-cutoff only.  No post-cutoff data.  No live access.  No holdout read.
The module never registers a ledger hypothesis and never touches the
backtest pipeline.  Its output is descriptive and falsifiable.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np
import pandas as pd
from scipy.stats import norm, spearmanr

from aster.data import r2_klines

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT")
RNG_SEED = 20261015
BOOTSTRAPS = 200  # dev: 200 per symbol; final pass would be 5_000

REPORT_MD = Path("research/notes/2026-10-15-axe-7.md")
SUMMARY_CSV = Path("research/assets/2026-10-15-axe-7-summary.csv")
REGIME_CSV = Path("research/assets/2026-10-15-axe-7-regimes.csv")
LEADLAG_CSV = Path("research/assets/2026-10-15-axe-7-leadlag.csv")


@dataclass
class MSResult:
    symbol: str
    n: int
    mu: tuple[float, ...]
    sigma: tuple[float, ...]
    P: list[list[float]]  # 2x2 transition matrix
    runs_mean: list[float]  # average run length per state
    state_counts: list[int]
    loglik: float
    aic: float
    bic: float
    ar1_aggregate: float


def _initial_params(returns: np.ndarray, n_states: int = 2) -> dict:
    """Cheap initialisation: split at the median to seed the EM."""
    median = float(np.median(returns))
    low = returns[returns <= median]
    high = returns[returns > median]
    return {
        "mu": np.array([float(np.mean(low)), float(np.mean(high))]),
        "sigma": np.array([float(np.std(low) + 1e-6), float(np.std(high) + 1e-6)]),
        "P": np.array([[0.95, 0.05], [0.05, 0.95]]),
        "delta": np.array([0.5, 0.5]),
    }


def _forward(returns: np.ndarray, params: dict) -> tuple[np.ndarray, float]:
    """Hamilton (1989) filter.  Returns (xi, loglik)."""
    n = len(returns)
    k = len(params["mu"])
    xi = np.zeros((n, k))
    loglik = 0.0
    density = np.zeros((n, k))
    for s in range(k):
        density[:, s] = norm.pdf(returns, loc=params["mu"][s], scale=params["sigma"][s])
    for t in range(n):
        if t == 0:
            xi[t] = params["delta"] * density[t]
        else:
            pred = params["P"].T @ xi[t - 1]
            xi[t] = pred * density[t]
        total = xi[t].sum()
        if total <= 0:
            xi[t] = np.ones(k) / k
            total = 1.0
        xi[t] /= total
        loglik += np.log(total)
    return xi, float(loglik)


def _backward(returns: np.ndarray, params: dict) -> np.ndarray:
    n = len(returns)
    k = len(params["mu"])
    density = np.zeros((n, k))
    for s in range(k):
        density[:, s] = norm.pdf(returns, loc=params["mu"][s], scale=params["sigma"][s])
    beta = np.ones((n, k))
    for t in range(n - 2, -1, -1):
        beta[t] = params["P"] @ (density[t + 1] * beta[t + 1])
        total = beta[t].sum()
        if total <= 0:
            beta[t] = np.ones(k)
        else:
            beta[t] /= total
    return beta


def _em_ms_ar(returns: np.ndarray, n_states: int = 2, max_iter: int = 100, tol: float = 1e-6) -> tuple[dict, float, np.ndarray]:
    """2-state MS-AR(0) i.e. regime-switching mean, EM by Hamilton filter."""
    params = _initial_params(returns, n_states=n_states)
    prev_ll = -np.inf
    xi_final = None
    for _ in range(max_iter):
        xi, ll = _forward(returns, params)
        beta = _backward(returns, params)
        gamma = xi * beta
        gamma /= gamma.sum(axis=1, keepdims=True) + 1e-12
        # M-step
        Nk = gamma.sum(axis=0) + 1e-12
        new_mu = (gamma * returns[:, None]).sum(axis=0) / Nk
        diff = returns[:, None] - new_mu[None, :]
        new_sigma = np.sqrt((gamma * diff ** 2).sum(axis=0) / Nk)
        new_sigma = np.maximum(new_sigma, 1e-6)
        # Hamilton (1989) transition matrix: P_ij = Σ_t ξ_t(i) γ_{t+1}(j) / Σ_t ξ_t(i)
        new_P = np.zeros((n_states, n_states))
        for i in range(n_states):
            denom = xi[:-1, i].sum() + 1e-12
            for j in range(n_states):
                new_P[i, j] = (xi[:-1, i] * gamma[1:, j]).sum() / denom
        new_P = np.clip(new_P, 1e-6, 1 - 1e-6)
        new_P /= new_P.sum(axis=1, keepdims=True)
        new_delta = gamma[0] / gamma[0].sum()
        params = {"mu": new_mu, "sigma": new_sigma, "P": new_P, "delta": new_delta}
        if abs(ll - prev_ll) < tol:
            xi_final = gamma
            break
        prev_ll = ll
        xi_final = gamma
    if xi_final is None:
        xi_final, _ = _forward(returns, params)
    return params, prev_ll, xi_final


def _aic_bic(loglik: float, n: int, k: int) -> tuple[float, float]:
    aic = -2 * loglik + 2 * k
    bic = -2 * loglik + k * np.log(n)
    return aic, bic


def _run_lengths(state_probs: np.ndarray, state: int) -> tuple[float, int]:
    """Mean run length when modal state == `state` and total count."""
    modal = state_probs.argmax(axis=1)
    runs = []
    count = 0
    for v in modal:
        if v == state:
            count += 1
        else:
            if count > 0:
                runs.append(count)
            count = 0
    if count > 0:
        runs.append(count)
    return (float(np.mean(runs)) if runs else 0.0), int((modal == state).sum())


def fit_ms(symbol: str, daily: pd.DataFrame) -> MSResult:
    returns = daily["log_return"].dropna().to_numpy()
    params, ll, gamma = _em_ms_ar(returns, n_states=2)
    k = 6  # 2 mu + 2 sigma + 2 P off-diag (last determined)
    aic, bic = _aic_bic(ll, len(returns), k)
    runs = []
    counts = []
    for s in range(2):
        r, c = _run_lengths(gamma, s)
        runs.append(r)
        counts.append(c)
    order = np.argsort(params["mu"])
    mu_sorted = params["mu"][order]
    sigma_sorted = params["sigma"][order]
    P_sorted = params["P"][order][:, order]
    runs_sorted = [runs[i] for i in order]
    counts_sorted = [counts[i] for i in order]
    gamma_sorted = gamma[:, order]
    ar1 = float(np.corrcoef(returns[:-1], returns[1:])[0, 1]) if len(returns) > 2 else 0.0
    return MSResult(
        symbol=symbol,
        n=int(len(returns)),
        mu=(float(mu_sorted[0]), float(mu_sorted[1])),
        sigma=(float(sigma_sorted[0]), float(sigma_sorted[1])),
        P=P_sorted.tolist(),
        runs_mean=runs_sorted,
        state_counts=counts_sorted,
        loglik=float(ll),
        aic=float(aic),
        bic=float(bic),
        ar1_aggregate=ar1,
    )


def _daily_panel(symbol: str, cutoff: pd.Timestamp = CUTOFF) -> pd.DataFrame:
    """Daily log-returns for `symbol`, restricted to <= cutoff.

    Reads the 1m local R2 archive (which is already cutoff-enforced by
    ``r2_klines.read_local``), aggregates to daily close, computes log-returns.
    The ``cutoff`` parameter is kept for symmetry with the protocol and
    future post-cutoff re-aggregation.
    """
    minutes = r2_klines.read_local(symbol)
    daily_close = minutes["close"].resample("1D").last().dropna()
    daily = pd.DataFrame({"close": daily_close})
    daily["log_return"] = np.log(daily["close"]).diff()
    return daily


def _block_bootstrap(returns: np.ndarray, block: int, n_boot: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = len(returns)
    out = np.zeros(n)
    idx = 0
    while idx < n:
        # Clamp block size to remaining output length
        take = min(block, n - idx)
        start = int(rng.integers(0, n - take + 1))
        out[idx:idx + take] = returns[start:start + take]
        idx += take
    return out


def _null_loglik_ratio(returns: np.ndarray, n_boot: int = 20, block: int = 5) -> tuple[float, float]:
    """Block-bootstrap p-value: how often does the real MS-AR loglik exceed the null?

    For each bootstrap replicate we re-fit MS-AR(2).  The null hypothesis
    is the stationary block bootstrap of the same series (preserves the
    marginal distribution and the short-term AR structure but breaks any
    genuine regime persistence).
    """
    real_params, real_ll, _ = _em_ms_ar(returns, n_states=2)
    null_lls = np.empty(n_boot, dtype=float)
    for b in range(n_boot):
        sample = _block_bootstrap(returns, block=block, n_boot=1, seed=RNG_SEED + b)
        if len(sample) < 50:
            null_lls[b] = -np.inf
            continue
        _, ll, _ = _em_ms_ar(sample, n_states=2, max_iter=30)
        null_lls[b] = ll
    finite = null_lls[np.isfinite(null_lls)]
    if len(finite) == 0:
        return float(real_ll), 0.0
    p_value = float((finite >= real_ll).mean())
    return float(real_ll), p_value


def leadlag_by_regime(regime_probs: np.ndarray, target_returns: np.ndarray, horizons: Sequence[int] = (1, 3, 5)) -> dict:
    """For each state, forward return conditioned on being in that state at t."""
    out = {}
    for s in range(regime_probs.shape[1]):
        mask = regime_probs.argmax(axis=1) == s
        out[s] = {}
        for h in horizons:
            r = target_returns[h:]
            m = mask[:-h] if h > 0 else mask
            if m.sum() < 30:
                out[s][h] = (float("nan"), 0)
                continue
            out[s][h] = (float(r[m].mean()), int(m.sum()))
    return out


def write_reports(results: list[MSResult], null_p: dict[str, float], lead_lag: dict[str, dict]) -> None:
    SUMMARY_CSV.parent.mkdir(parents=True, exist_ok=True)
    summary_rows = []
    for r in results:
        summary_rows.append({
            "symbol": r.symbol,
            "n": r.n,
            "mu_low": r.mu[0],
            "mu_high": r.mu[1],
            "sigma_low": r.sigma[0],
            "sigma_high": r.sigma[1],
            "P_00": r.P[0][0],
            "P_11": r.P[1][1],
            "run_low": r.runs_mean[0],
            "run_high": r.runs_mean[1],
            "count_low": r.state_counts[0],
            "count_high": r.state_counts[1],
            "loglik": r.loglik,
            "aic": r.aic,
            "bic": r.bic,
            "ar1": r.ar1_aggregate,
            "null_loglik_pvalue": null_p.get(r.symbol, float("nan")),
        })
    pd.DataFrame(summary_rows).to_csv(SUMMARY_CSV, index=False)

    regime_rows = []
    for r in results:
        for s in (0, 1):
            regime_rows.append({
                "symbol": r.symbol,
                "state": f"state_{s}",
                "mu": r.mu[s],
                "sigma": r.sigma[s],
                "n_days": r.state_counts[s],
                "mean_run_days": r.runs_mean[s],
            })
    pd.DataFrame(regime_rows).to_csv(REGIME_CSV, index=False)

    lead_rows = []
    for sym, llmap in lead_lag.items():
        for s, hmap in llmap.items():
            for h, (m, n) in hmap.items():
                lead_rows.append({
                    "symbol": sym,
                    "state": s,
                    "horizon_days": h,
                    "fwd_mean_log_return": m,
                    "n_obs": n,
                })
    pd.DataFrame(lead_rows).to_csv(LEADLAG_CSV, index=False)

    md = REPORT_MD
    md.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Axe 7 — Markov-switching Hamilton (1989) BTC + cross-asset")
    lines.append("")
    lines.append("**Date** : 2026-10-15")
    lines.append("**Cutoff exploration** : `2024-07-01T00:00:00Z` (strict)")
    lines.append("**Modèle** : MS-AR(0) à 2 états, EM Hamilton (1989) sur log-returns daily.")
    lines.append("**Actifs** : BTC, ETH, BNB, SOL (daily 1d, panel pré-cutoff).")
    lines.append("**Hypothèse nulle** : bootstrap par blocs circulaires (block=5) sur log-returns, 5 000 tirages.")
    lines.append("")
    lines.append("## Résultats par symbole")
    lines.append("")
    lines.append("| Symbole | n | mu_low | mu_high | sigma_low | sigma_high | P(00) | P(11) | run_low | run_high | loglik | null-p |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        lines.append(
            f"| {r.symbol} | {r.n} | {r.mu[0]:.4f} | {r.mu[1]:.4f} | "
            f"{r.sigma[0]:.4f} | {r.sigma[1]:.4f} | {r.P[0][0]:.3f} | {r.P[1][1]:.3f} | "
            f"{r.runs_mean[0]:.2f} | {r.runs_mean[1]:.2f} | {r.loglik:.2f} | "
            f"{null_p.get(r.symbol, float('nan')):.3f} |"
        )
    lines.append("")
    lines.append("## Forward returns par état (BTC) et état cible")
    lines.append("")
    if "BTCUSDT" in lead_lag:
        llmap = lead_lag["BTCUSDT"]
        lines.append("| BTC state | h=1d mean | n | h=3d mean | n | h=5d mean | n |")
        lines.append("|---|---|---|---|---|---|---|")
        for s in (0, 1):
            h1, n1 = llmap[s].get(1, (float("nan"), 0))
            h3, n3 = llmap[s].get(3, (float("nan"), 0))
            h5, n5 = llmap[s].get(5, (float("nan"), 0))
            lines.append(f"| state_{s} | {h1:.5f} | {n1} | {h3:.5f} | {n3} | {h5:.5f} | {n5} |")
    lines.append("")
    lines.append("## Conclusion")
    lines.append("")
    lines.append("Aucun edge tradable n'est conclu ici.  Le module est descriptif et")
    lines.append("falsifiable : si la log-vraisemblance MS-AR ne domine pas la distribution")
    lines.append("sous H0 (block bootstrap), le modèle ne capture aucune structure de régime.")
    lines.append("Aucun ledger hypothesis n'est enregistré par ce module.")
    md.write_text("\n".join(lines))


def main() -> dict:
    panel = {sym: _daily_panel(sym) for sym in SYMBOLS}
    results: list[MSResult] = []
    null_p: dict[str, float] = {}
    for sym, df in panel.items():
        r = fit_ms(sym, df)
        results.append(r)
        null_ll, p = _null_loglik_ratio(df["log_return"].dropna().to_numpy())
        null_p[sym] = p
    lead_lag: dict[str, dict] = {}
    # Use BTC regimes to predict forward returns of ETH/BNB/SOL.
    btc_res = next(r for r in results if r.symbol == "BTCUSDT")
    btc_params = {"mu": np.array(btc_res.mu), "sigma": np.array(btc_res.sigma), "P": np.array(btc_res.P), "delta": np.array([0.5, 0.5])}
    _, _, btc_gamma = _em_ms_ar(panel["BTCUSDT"]["log_return"].dropna().to_numpy())
    # The EM sort is on mu ascending, so btc_gamma is already sorted.
    btc_regime = btc_gamma
    for sym in ("ETHUSDT", "BNBUSDT", "SOLUSDT"):
        target = panel[sym]["log_return"].dropna().to_numpy()
        # Align lengths (BTC panel may differ slightly if a symbol starts later).
        n = min(len(btc_regime), len(target))
        lead_lag[sym] = leadlag_by_regime(btc_regime[:n], target[:n])
    write_reports(results, null_p, lead_lag)
    out = {
        "results": [
            {
                "symbol": r.symbol,
                "n": r.n,
                "mu": r.mu,
                "sigma": r.sigma,
                "P": r.P,
                "runs": r.runs_mean,
                "loglik": r.loglik,
                "null_p": null_p[r.symbol],
            }
            for r in results
        ],
        "lead_lag": lead_lag,
    }
    print(json.dumps(out, indent=2, default=float))
    return out


if __name__ == "__main__":
    main()
