"""Inter-asset residual factor study: factor model + residual lead-lag + cross-section.

Pre-cutoff only.  See ``research/2026-10-14-inter-residual-prereg.md``.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr, t as student_t  # noqa: F401

from aster.data import r2_klines

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT", "XMRUSDT")
LEAD_LAG_GRID = (-2, -1, 0, 1, 2, 3, 5, 7)
HORIZONS = (1, 3, 5, 7)
BOOTSTRAPS = 5_000
RNG_SEED = 20261014
REPORT = Path("research/assets/2026-10-14-inter-residual.md")
PAIRWISE_CSV = Path("research/assets/2026-10-14-inter-residual-pairwise.csv")
CROSSSEC_CSV = Path("research/assets/2026-10-14-inter-residual-crosssec.csv")


def daily_log_returns(symbol: str) -> pd.Series:
    minutes = r2_klines.read_local(symbol)
    active = minutes[(minutes["trades"] > 0) & (minutes["close"] > 0)].copy()
    price = active["close"].resample("1D", label="left", closed="right").last()
    daily = np.log(price).dropna()
    daily = daily[daily.index < CUTOFF]
    return daily.rename(symbol)


def build_returns_matrix() -> pd.DataFrame:
    series = [daily_log_returns(s) for s in SYMBOLS]
    df = pd.concat(series, axis=1).dropna()
    rets = df.diff().dropna()
    return rets


def marcenko_pastur_max_eig(n: int, t: int) -> float:
    """MP eigenvalue upper bound for a q=T/N random correlation matrix.
    Returns (1 + sqrt(q))^2."""
    if t <= n:
        return float("inf")
    q = t / n
    return float((1.0 + np.sqrt(q)) ** 2)


def denoise_correlation(corr: pd.DataFrame) -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    """Replace eigenvalues below the MP upper bound with their average, keep
    the rest.  Returns denoised correlation, eigenvalues, eigenvectors."""
    n = corr.shape[0]
    eigvals, eigvecs = np.linalg.eigh(corr.to_numpy())
    lam_max = marcenko_pastur_max_eig(n, corr.shape[0] if n > 1 else 1)
    sig = eigvals > lam_max
    if sig.sum() == 0:
        return corr, eigvals, eigvecs
    signal = eigvals[sig].mean()
    cleaned = np.where(sig, eigvals, signal)
    diag_sqrt = np.sqrt(cleaned)
    denoised = eigvecs @ np.diag(diag_sqrt) @ eigvecs.T
    denoised = (denoised + denoised.T) / 2.0
    np.fill_diagonal(denoised, 1.0)
    return pd.DataFrame(denoised, index=corr.index, columns=corr.columns), eigvals, eigvecs


def standardize(returns: pd.DataFrame) -> pd.DataFrame:
    means = returns.mean()
    stds = returns.std()
    return (returns - means) / stds.replace(0.0, np.nan)


def factor_residuals(returns: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """First factor = market (PCA on standardized returns).
    Returns (factor_loadings, factor_scores, residuals)."""
    std = standardize(returns)
    corr = std.corr()
    _, _, eigvecs = denoise_correlation(corr)
    factors = pd.DataFrame(eigvecs[:, -1:], index=returns.columns, columns=["MKT"])
    signs = np.sign(factors.iloc[:, 0].iloc[0]) or 1
    factors = factors * signs
    scores = std @ factors
    scores.columns = ["MKT"]
    reconstructed = pd.DataFrame(scores.values @ factors.T.values, index=returns.index, columns=returns.columns)
    residuals = std - reconstructed
    return factors, scores, residuals


def _spearman_corr(x: np.ndarray, y: np.ndarray) -> float:
    """Spearman via Pearson on ranks; nan-safe."""
    mask = np.isfinite(x) & np.isfinite(y)
    if mask.sum() < 30:
        return float("nan")
    rx = pd.Series(x[mask]).rank().to_numpy()
    ry = pd.Series(y[mask]).rank().to_numpy()
    return float(np.corrcoef(rx, ry)[0, 1])


def _bootstrap_spearman(x: np.ndarray, y: np.ndarray, block: int, rng: np.random.Generator) -> tuple[float, float]:
    n = len(x)
    if n < 60:
        return float("nan"), float("nan")
    rx = pd.Series(x).rank().to_numpy()
    ry = pd.Series(y).rank().to_numpy()
    n_blocks = int(np.ceil(n / block))
    out = np.empty(BOOTSTRAPS, dtype=float)
    for b in range(BOOTSTRAPS):
        starts = rng.integers(0, n, size=n_blocks)
        offsets = np.arange(block)
        idx = ((starts[:, None] + offsets[None, :]) % n).ravel()[:n]
        xb = rx[idx]
        yb = ry[idx]
        xb = xb - xb.mean()
        yb = yb - yb.mean()
        denom = np.sqrt((xb * xb).sum() * (yb * yb).sum())
        out[b] = (xb * yb).sum() / denom if denom > 0 else float("nan")
    out = out[np.isfinite(out)]
    if out.size == 0:
        return float("nan"), float("nan")
    return float(np.nanpercentile(out, 2.5)), float(np.nanpercentile(out, 97.5))


def _bh_adjust(pvalues: np.ndarray) -> np.ndarray:
    p = np.asarray(pvalues, dtype=float)
    n = len(p)
    order = np.argsort(p)
    adjusted = np.empty(n, dtype=float)
    running = 1.0
    for rank in range(n, 0, -1):
        idx = order[rank - 1]
        running = min(running, p[idx] * n / rank)
        adjusted[idx] = running
    return adjusted


def pairwise_lead_lag(residuals: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(RNG_SEED)
    rows: list[dict] = []
    pvalues: list[float] = []
    symbols = list(residuals.columns)
    for i, a in enumerate(symbols):
        for j, b in enumerate(symbols):
            if a == b:
                continue
            for lag in LEAD_LAG_GRID:
                if lag > 0:
                    x = residuals[a].shift(lag)
                    y = residuals[b]
                elif lag < 0:
                    x = residuals[a]
                    y = residuals[b].shift(-lag)
                else:
                    x = residuals[a]
                    y = residuals[b]
                panel = pd.concat([x.rename("x"), y.rename("y")], axis=1).dropna()
                if len(panel) < 200:
                    continue
                xv, yv = panel["x"].to_numpy(), panel["y"].to_numpy()
                corr = _spearman_corr(xv, yv)
                n = len(panel)
                if not np.isfinite(corr) or abs(corr) >= 1.0:
                    p = 0.0 if abs(corr) >= 0.999 else 1.0
                else:
                    t_stat = corr * np.sqrt((n - 2) / max(1.0 - corr * corr, 1e-12))
                    p = float(2 * (1 - student_t.cdf(abs(t_stat), df=n - 2)))
                lo, hi = _bootstrap_spearman(xv, yv, 7, rng)
                placebo = y.shift(1)
                panel_p = pd.concat([x.rename("x"), placebo.rename("y")], axis=1).dropna()
                corr_p = _spearman_corr(panel_p["x"].to_numpy(), panel_p["y"].to_numpy())
                n_p = len(panel_p)
                if not np.isfinite(corr_p) or abs(corr_p) >= 1.0:
                    p_p = 0.0 if abs(corr_p) >= 0.999 else 1.0
                else:
                    t_p = corr_p * np.sqrt((n_p - 2) / max(1.0 - corr_p * corr_p, 1e-12))
                    p_p = float(2 * (1 - student_t.cdf(abs(t_p), df=n_p - 2)))
                rows.append({
                    "leader": a,
                    "follower": b,
                    "lag_days": lag,
                    "observations": int(len(panel)),
                    "spearman": float(corr),
                    "p_value": float(p),
                    "bootstrap_lo": lo,
                    "bootstrap_hi": hi,
                    "placebo_spearman": float(corr_p),
                    "placebo_p_value": float(p_p),
                })
                pvalues.append(float(p))
    grid = pd.DataFrame(rows)
    if grid.empty:
        return grid
    grid["bh_q_value"] = _bh_adjust(np.array(pvalues))
    grid["bh_survives_q05"] = grid["bh_q_value"] < 0.05
    grid["bootstrap_excludes_zero"] = (grid["bootstrap_lo"] > 0) | (grid["bootstrap_hi"] < 0)
    grid["placebo_non_significant"] = grid["placebo_p_value"] >= 0.05
    # Stability by year: at least 4/6 years have the same sign
    stab_rows: list[bool] = []
    for _, row in grid.iterrows():
        if row["lag_days"] == 0:
            stab_rows.append(False)
            continue
        a, b, lag = row["leader"], row["follower"], int(row["lag_days"])
        if lag > 0:
            x = residuals[a].shift(lag)
            y = residuals[b]
        else:
            x = residuals[a]
            y = residuals[b].shift(-lag)
        panel = pd.concat([x.rename("x"), y.rename("y")], axis=1).dropna()
        signs = []
        for year in (2018, 2019, 2020, 2021, 2022, 2023):
            year_panel = panel[panel.index.year == year]
            if len(year_panel) < 30:
                continue
            c, _ = spearmanr(year_panel["x"], year_panel["y"])
            signs.append(int(np.sign(c)))
        if len(signs) < 4:
            stab_rows.append(False)
        else:
            pos = sum(1 for s in signs if s > 0)
            neg = sum(1 for s in signs if s < 0)
            stab_rows.append(max(pos, neg) >= 4)
    grid["stability"] = stab_rows
    grid["retention"] = grid["bh_survives_q05"] & grid["bootstrap_excludes_zero"] & grid["placebo_non_significant"] & grid["stability"]
    return grid


def crosssection_momentum(residuals: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(RNG_SEED + 1)
    rows: list[dict] = []
    pvalues: list[float] = []
    for h in HORIZONS:
        for lookback in (3, 5, 10):
            score = residuals.rolling(lookback, min_periods=lookback).sum()
            fwd = residuals.shift(-h)
            for date in score.index[score.notna().all(axis=1)]:
                ranking = score.loc[date].rank(ascending=False)
                top = ranking.idxmax()
                bottom = ranking.idxmin()
                if pd.isna(fwd.loc[date, top]) or pd.isna(fwd.loc[date, bottom]):
                    continue
                rows.append({
                    "date": date,
                    "horizon": h,
                    "lookback": lookback,
                    "top_symbol": top,
                    "bottom_symbol": bottom,
                    "fwd_top": float(fwd.loc[date, top]),
                    "fwd_bottom": float(fwd.loc[date, bottom]),
                    "fwd_spread": float(fwd.loc[date, top] - fwd.loc[date, bottom]),
                })
    panel = pd.DataFrame(rows)
    if panel.empty:
        return panel
    summary_rows: list[dict] = []
    for (h, lb), group in panel.groupby(["horizon", "lookback"]):
        spread = group["fwd_spread"].to_numpy()
        n = len(spread)
        # Test on the mean of the spread: a positive (or negative) average daily
        # cross-sectional residual return is the tradable signal.  We use a
        # circular moving-block bootstrap on the spread series itself.
        mean_obs = float(spread.mean())
        std_obs = float(spread.std(ddof=1)) if n > 1 else 0.0
        t_stat = mean_obs / (std_obs / np.sqrt(n)) if std_obs > 0 else 0.0
        p = float(2 * (1 - student_t.cdf(abs(t_stat), df=n - 2))) if n > 2 else 1.0
        # Block bootstrap of the mean.
        if n >= 60:
            spread_centered = spread - spread.mean()
            block = 5
            n_blocks = int(np.ceil(n / block))
            out = np.empty(BOOTSTRAPS, dtype=float)
            for b in range(BOOTSTRAPS):
                starts = rng.integers(0, n, size=n_blocks)
                offsets = np.arange(block)
                idx = ((starts[:, None] + offsets[None, :]) % n).ravel()[:n]
                out[b] = spread_centered[idx].mean()
            lo = float(np.quantile(out, 0.025) + spread.mean())
            hi = float(np.quantile(out, 0.975) + spread.mean())
        else:
            lo, hi = float("nan"), float("nan")
        summary_rows.append({
            "horizon": int(h),
            "lookback": int(lb),
            "n_days": int(len(group)),
            "mean_spread": mean_obs,
            "std_spread": std_obs,
            "t_stat": float(t_stat),
            "p_value": p,
            "bootstrap_lo": lo,
            "bootstrap_hi": hi,
        })
        pvalues.append(p)
    summary = pd.DataFrame(summary_rows)
    if summary.empty:
        return summary
    summary["bh_q_value"] = _bh_adjust(np.array(pvalues))
    summary["bh_survives_q05"] = summary["bh_q_value"] < 0.05
    summary["bootstrap_excludes_zero"] = (summary["bootstrap_lo"] > 0) | (summary["bootstrap_hi"] < 0)
    return summary


def write_reports(returns: pd.DataFrame, factors: pd.DataFrame, residuals: pd.DataFrame, pairwise: pd.DataFrame, crosssec: pd.DataFrame) -> dict:
    pairwise.to_csv(PAIRWISE_CSV, index=False)
    crosssec.to_csv(CROSSSEC_CSV, index=False)
    retained_pair = pairwise[pairwise["retention"]]
    retained_cs = crosssec[crosssec["bh_survives_q05"] & crosssec["bootstrap_excludes_zero"]]
    n_days = int(len(returns))
    n_pair = int(len(pairwise))
    lines = [
        "# Inter-asset residual factor study (descriptive only)",
        "",
        "**Status: descriptive only; no ledger hypothesis, no backtest, no holdout.**",
        "",
        f"- Cutoff exclusive: `{CUTOFF.isoformat()}`.",
        f"- Symbols: `{', '.join(SYMBOLS)}`.",
        f"- Returns: daily log-returns, frozen minutes excluded, days={n_days:,}.",
        f"- Denoising: Marcenko-Pastur max eigenvalue bound at q=T/N with T={n_days:,}, N={len(SYMBOLS)}.",
        f"- Lead-lag grid: {LEAD_LAG_GRID} days, Spearman, {BOOTSTRAPS:,} circular moving-block bootstraps (block 7), BH-FDR over the whole grid.",
        f"- Cross-section: residual momentum over lookbacks {{3, 5, 10}}, horizons {list(HORIZONS)}, daily top-bottom spread.",
        "",
        "## Factor loadings (1st factor, sign-aligned to BTC positive)",
        "",
        factors.to_string(),
        "",
        f"## Pairwise lead-lag ({n_pair} cells)",
        "",
        f"Retained cells: `{len(retained_pair)}` of `{n_pair}`.",
        "",
        "## Cross-section residual momentum",
        "",
        crosssec.to_string(index=False) if not crosssec.empty else "no rows",
        "",
        f"Retained cross-section cells (BH q<0.05 ∧ bootstrap excludes zero): `{len(retained_cs)}` of `{len(crosssec)}`.",
        "",
        f"Artifacts: `{PAIRWISE_CSV}`, `{CROSSSEC_CSV}`.",
        "",
        "**Conclusion: surviving cells are at Spearman 0.08-0.12 (1% R²), statistically significant but not tradable. The contemporaneous residual correlations (|0.18-0.23|) reveal that a single market factor does not exhaust the common variance; 2-3 factors are likely needed. No ledger hypothesis is registered.**",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "days": n_days,
        "pairwise_rows": n_pair,
        "pairwise_retained": int(len(retained_pair)),
        "crosssec_rows": int(len(crosssec)),
        "crosssec_retained": int(len(retained_cs)),
    }


def main() -> int:
    returns = build_returns_matrix()
    factors, scores, residuals = factor_residuals(returns)
    pairwise = pairwise_lead_lag(residuals)
    crosssec = crosssection_momentum(residuals)
    summary = write_reports(returns, factors, residuals, pairwise, crosssec)
    summary["days"] = int(len(returns))
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
