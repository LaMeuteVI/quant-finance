---
name: lopez-de-prado-ml-asset-managers
description: "Knowledge base from Marcos López de Prado, Machine Learning for Asset Managers (Cambridge UP 2020). The 8-chapter companion volume to Advances in Financial Machine Learning. Use when denoising and detoning correlation matrices (Marčenko-Pastur, random matrix theory), choosing distance metrics for financial clustering (angular, Mahalanobis), selecting the optimal number of clusters (Gap statistic, silhouette, ONC), constructing financial labels (triple-barrier, dynamic, meta-labelling), computing feature importance with substitution/masking corrections (MDI/MDA/SFI/CFI), building portfolio construction algorithms (EWP, IVP, MVP, HRP, NCO), or testing for backtest overfitting (SPA, Reality Check, PBO). The eight chapters cover the introduction, denoising/detoning, distance metrics, optimal clustering, financial labels, feature importance analysis, portfolio construction, and testing set overfitting."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Machine Learning for Asset Managers (López de Prado)

**Source**: Marcos López de Prado, *Machine Learning for Asset Managers*, Cambridge UP 2020 | **Domain**: Gestion de portefeuille | **Chapters**: 8 | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview.
- **With a topic or framework name** (e.g. "denoising", "angular distance", "CFI", "HRP", "PBO"): jump to the relevant chapter.
- **With a chapter number**: open `chapters/chNN-*.md`.

## Core Frameworks & Mental Models

1. **The 5 Sources of Investment Edge** (ch01): informational, analytical, computational, structural, psychological.
2. **Denoising** (ch02): Marčenko-Pastur; the noisy eigenvalues are below the upper bound.
3. **Detoning** (ch02): removing the dominant market mode from the correlation matrix.
4. **Angular Distance** (ch03): `d(x, y) = √(0.5 × (1 - corr(x, y)))`; the institutional default.
5. **Optimal Clustering** (ch04): Gap statistic, silhouette, ONC; the cophenetic correlation.
6. **Financial Labels** (ch05): triple-barrier, dynamic barrier, meta-labelling, multi-class.
7. **Feature Importance** (ch06): MDI/MDA/SFI, substitution effect, masking effect, CFI.
8. **Portfolio Construction** (ch07): EWP, IVP, MVP, HRP, NCO.
9. **Testing Set Overfitting** (ch08): SPA, Reality Check, PBO via CSCV.

## Chapter Index

| # | Title | Key Frameworks | File |
|---|---|---|---|
| 1 | Introduction | 5 sources of edge; 4 types of ML | [ch01](./chapters/ch01-introduction.md) |
| 2 | Denoising and Detoning | Marčenko-Pastur, RMT | [ch02](./chapters/ch02-denoising-and-detoning.md) |
| 3 | Distance Metrics | Euclidean, Mahalanobis, angular | [ch03](./chapters/ch03-distance-metrics.md) |
| 4 | Optimal Clustering | Gap, silhouette, ONC, cophenetic | [ch04](./chapters/ch04-optimal-clustering.md) |
| 5 | Financial Labels | Triple-barrier, dynamic, meta | [ch05](./chapters/ch05-financial-labels.md) |
| 6 | Feature Importance Analysis | MDI/MDA/SFI, substitution, CFI | [ch06](./chapters/ch06-feature-importance-analysis.md) |
| 7 | Portfolio Construction | EWP, IVP, MVP, HRP, NCO | [ch07](./chapters/ch07-portfolio-construction.md) |
| 8 | Testing Set Overfitting | SPA, Reality Check, PBO | [ch08](./chapters/ch08-testing-set-overfitting.md) |

## Topic Index

- **Angular distance** → ch03
- **Backtest overfitting** → ch08
- **Cophenetic correlation** → ch04
- **CSCV** → ch08
- **Clustered Feature Importance (CFI)** → ch06
- **Detoning** → ch02
- **Denoising** → ch02
- **DSR (Deflated Sharpe Ratio)** → ch08 (cross-ref `lopez-de-prado-afml` ch14)
- **Distance metrics** → ch03
- **Equal-Weighted Portfolio (EWP)** → ch07
- **Feature importance** → ch06
- **Gap statistic** → ch04
- **Hierarchical Risk Parity (HRP)** → ch07
- **Inverse-Variance Portfolio (IVP)** → ch07
- **KL divergence** → ch03
- **Mahalanobis distance** → ch03
- **Marčenko-Pastur distribution** → ch02
- **Masking effect** → ch06
- **Meta-labelling** → ch05
- **Minimum-Variance Portfolio (MVP)** → ch07
- **Mutual information** → ch03
- **Nested Clustered Optimisation (NCO)** → ch07
- **ONC (Optimal Number of Clusters)** → ch04
- **PBO (Probability of Backtest Overfitting)** → ch08
- **Random Matrix Theory (RMT)** → ch02
- **Reality Check (White 2000)** → ch08
- **Silhouette score** → ch04
- **SPA test (Hansen 2005)** → ch08
- **Substitution effect** → ch06
- **Testing set overfitting** → ch08
- **Triple-barrier method** → ch05 (cross-ref `lopez-de-prado-afml` ch03)

## Related Skills

- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — the full 22-chapter volume; the institutional reference.
- **`grinold-kahn-apm`** (gestion-de-portefeuille) — the classical active management framework.
- **`hull-risk-management`** (finance-de-marche) — the institutional risk management.
- **`hull-derivatives`** (finance-de-marche) — the options/futures/swap pricing book.
- **`gatheral-volatility-surface`** (finance-de-marche) — the vol surface.
- **`chan-machine-trading`** (finance-de-marche) — the practitioner AI book.
- **`tsay-analysis-financial-time-series`** (fondamentaux) — the time-series foundation.
- **`diebold-mariano-forecast-accuracy`** (fondamentaux) — the forecast-comparison test.

## Scope & Limits

- **Coverage**: 8 chapters of the 2020 companion volume.
- **Edition year**: 2020 — supplements `lopez-de-prado-afml` (2018) with the more focused topics.
- **What the source does NOT cover**:
  - The full AFML curriculum (see `lopez-de-prado-afml`).
  - The classical active management (see `grinold-kahn-apm`).
  - The risk management (see `hull-risk-management`).
  - The vol surface (see `gatheral-volatility-surface`).
  - The time-series foundation (see `tsay-analysis-financial-time-series`).
- **OCR / extraction quality**: pdftotext output is clean; no reconstruction needed.
- **Translation**: English.
