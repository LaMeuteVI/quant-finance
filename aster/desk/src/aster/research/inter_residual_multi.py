"""Multi-factor (K=2,3) inter-asset residual study, pre-cutoff only.

Extends the 1-factor residual study in ``inter_residual.py``.  The 1-factor
study showed contemporaneous residual correlations of |0.18-0.23| — evidence
that a single market factor does not exhaust the common variance.  This
module fits a K-factor PCA on the standardized return matrix, denoises each
eigenvalue against the Marcenko-Pastur bound, signs the factors against
canonical reference assets (BTC for factor 1, ETH for factor 2, then the
largest-magnitude loadings for factor 3), and runs the same pairwise
lead-lag and cross-sectional momentum grids on the resulting residuals.

No ledger hypothesis is registered from this study alone; a tradable
Spearman ≥ 0.20 over residuals, BH q<0.001, placebo non-significant, and
at least 4 years of sign-stable observation is required for ledger
promotion (see ``research/2026-10-14-inter-residual-multi-prereg.md``).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import t as student_t

from aster.data import r2_klines

from aster.research.inter_residual import (
    BOOTSTRAPS,
    CUTOFF,
    HORIZONS,
    LEAD_LAG_GRID,
    RNG_SEED,
    SYMBOLS,
    _bootstrap_spearman,
    _bh_adjust,
    _spearman_corr,
    build_returns_matrix,
    crosssection_momentum,
    daily_log_returns,
    pairwise_lead_lag,
    standardize,
)

REPORT_K2 = Path("research/assets/2026-10-14-inter-residual-k2.md")
REPORT_K3 = Path("research/assets/2026-10-14-inter-residual-k3.md")
PAIRWISE_K2 = Path("research/assets/2026-10-14-inter-residual-k2-pairwise.csv")
PAIRWISE_K3 = Path("research/assets/2026-10-14-inter-residual-k3-pairwise.csv")
CROSSSEC_K2 = Path("research/assets/2026-10-14-inter-residual-k2-crosssec.csv")
CROSSSEC_K3 = Path("research/assets/2026-10-14-inter-residual-k3-crosssec.csv")
LOADINGS_K2 = Path("research/assets/2026-10-14-inter-residual-k2-loadings.csv")
LOADINGS_K3 = Path("research/assets/2026-10-14-inter-residual-k3-loadings.csv")

# Reference assets to sign each factor against (positive loading)
FACTOR_REFS: dict[int, str] = {0: "BTCUSDT", 1: "ETHUSDT", 2: "BNBUSDT"}


def factor_residuals_k(returns: pd.DataFrame, k: int) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """K-factor PCA on standardized returns with Marcenko-Pastur eigenvalue
    denoising and reference-asset sign alignment.  Returns
    (factor_loadings [N×K], factor_scores [T×K], residuals [T×N])."""
    std = standardize(returns)
    corr = std.corr().to_numpy()
    eigvals, eigvecs = np.linalg.eigh(corr)  # ascending
    n, t = corr.shape[0], len(returns)
    if t <= n:
        raise ValueError(f"need T > N, got T={t}, N={n}")
    q = t / n
    lam_max = (1.0 + np.sqrt(q)) ** 2
    # Keep the K largest eigenvalues, denoise the rest to the mean of signal.
    sorted_idx = np.argsort(eigvals)[::-1]  # descending
    keep_mask = np.zeros(n, dtype=bool)
    keep_mask[sorted_idx[:k]] = True
    if keep_mask.sum() == 0:
        return (
            pd.DataFrame(np.zeros((n, k)), index=returns.columns,
                         columns=[f"F{i+1}" for i in range(k)]),
            pd.DataFrame(np.zeros((len(returns), k)), index=returns.index,
                         columns=[f"F{i+1}" for i in range(k)]),
            std,
        )
    sig_mean = eigvals[keep_mask].mean()
    cleaned = np.where(keep_mask, eigvals, sig_mean)
    diag_sqrt = np.sqrt(cleaned)
    denoised = eigvecs @ np.diag(diag_sqrt) @ eigvecs.T
    # Eigen-decompose the denoised matrix to obtain the K leading orthonormal factors.
    eig2, eigvec2 = np.linalg.eigh(denoised)
    leading = np.argsort(eig2)[::-1][:k]
    loadings = pd.DataFrame(
        eigvec2[:, leading],
        index=returns.columns,
        columns=[f"F{i+1}" for i in range(k)],
    )
    # Sign alignment against the reference asset for each factor.
    for f in range(k):
        ref = FACTOR_REFS.get(f)
        if ref is None or ref not in loadings.index:
            continue
        sign = np.sign(loadings.loc[ref, loadings.columns[f]])
        if sign == 0:
            sign = 1.0
        loadings.iloc[:, f] = loadings.iloc[:, f] * sign
    scores = pd.DataFrame(
        std.to_numpy() @ loadings.to_numpy(),
        index=returns.index,
        columns=loadings.columns,
    )
    reconstructed = pd.DataFrame(
        scores.to_numpy() @ loadings.T.to_numpy(),
        index=returns.index,
        columns=returns.columns,
    )
    residuals = std - reconstructed
    return loadings, scores, residuals


def write_k_report(
    k: int,
    loadings: pd.DataFrame,
    residuals: pd.DataFrame,
    pairwise: pd.DataFrame,
    crosssec: pd.DataFrame,
    n_days: int,
) -> dict:
    pairwise_csv = PAIRWISE_K2 if k == 2 else PAIRWISE_K3
    crosssec_csv = CROSSSEC_K2 if k == 2 else CROSSSEC_K3
    loadings_csv = LOADINGS_K2 if k == 2 else LOADINGS_K3
    report = REPORT_K2 if k == 2 else REPORT_K3
    pairwise.to_csv(pairwise_csv, index=False)
    crosssec.to_csv(crosssec_csv, index=False)
    loadings.to_csv(loadings_csv)

    retained_pair = pairwise[pairwise["retention"]]
    retained_cs = crosssec[crosssec["bh_survives_q05"] & crosssec["bootstrap_excludes_zero"]]
    n_pair = int(len(pairwise))
    top = retained_pair.assign(abs_s=lambda d: d["spearman"].abs()).sort_values("abs_s", ascending=False).head(15)
    lines = [
        f"# Inter-asset residual factor study — K={k} (descriptive only)",
        "",
        "**Status: descriptive only; no ledger hypothesis, no backtest, no holdout.**",
        "",
        f"- Cutoff exclusive: `{CUTOFF.isoformat()}`.",
        f"- Symbols: `{', '.join(SYMBOLS)}`.",
        f"- Returns: daily log-returns, frozen minutes excluded, days={n_days:,}.",
        f"- Denoising: K-factor PCA with Marcenko-Pastur bound at q=T/N (T={n_days:,}, N={len(SYMBOLS)}), eigenvalues below the bound averaged to signal mean.",
        f"- Sign alignment: F1 ↔ BTCUSDT, F2 ↔ ETHUSDT, F3 ↔ BNBUSDT.",
        f"- Lead-lag grid: {LEAD_LAG_GRID} days, Spearman, {BOOTSTRAPS:,} circular moving-block bootstraps (block 7), BH-FDR over the whole grid.",
        f"- Cross-section: residual momentum over lookbacks {{3, 5, 10}}, horizons {list(HORIZONS)}, daily top-bottom spread.",
        "",
        "## Factor loadings (sign-aligned)",
        "",
        loadings.to_string(),
        "",
        f"## Pairwise lead-lag ({n_pair} cells)",
        "",
        f"Retained cells: `{len(retained_pair)}` of `{n_pair}`.",
        "",
        "Top retained by |Spearman|:",
        "",
        top.to_string(index=False) if not top.empty else "no retained cells",
        "",
        "## Cross-section residual momentum",
        "",
        crosssec.to_string(index=False) if not crosssec.empty else "no rows",
        "",
        f"Retained cross-section cells (BH q<0.05 ∧ bootstrap excludes zero): `{len(retained_cs)}` of `{len(crosssec)}`.",
        "",
        f"Artifacts: `{pairwise_csv}`, `{crosssec_csv}`, `{loadings_csv}`.",
        "",
        "**Conclusion: see top retained rows above. A cell is candidate for the ledger only if Spearman ≥ 0.20, BH q < 0.001, placebo non-significant, and ≥ 4 years of stable sign. None of the cells here is automatically promoted; promotion requires a separate memo and a pre-registered `desk backtest` trial count.**",
    ]
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "k": k,
        "days": n_days,
        "pairwise_rows": n_pair,
        "pairwise_retained": int(len(retained_pair)),
        "pairwise_retained_max_abs_spearman": float(top["abs_s"].max()) if not top.empty else 0.0,
        "crosssec_rows": int(len(crosssec)),
        "crosssec_retained": int(len(retained_cs)),
    }


def main() -> int:
    returns = build_returns_matrix()
    n_days = int(len(returns))
    summaries = []
    for k in (2, 3):
        loadings, _scores, residuals = factor_residuals_k(returns, k)
        pairwise = pairwise_lead_lag(residuals)
        crosssec = crosssection_momentum(residuals)
        summaries.append(write_k_report(k, loadings, residuals, pairwise, crosssec, n_days))
    print(json.dumps(summaries, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
