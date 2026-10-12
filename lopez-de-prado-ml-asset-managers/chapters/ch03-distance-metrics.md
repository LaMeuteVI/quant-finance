# Chapter 3: Distance Metrics

> López de Prado, MLAM, Chapter 3.

## Core Idea

**Distance metrics** for financial data: (1) **Euclidean** (sensitive to scale), (2) **Mahalanobis** (scale-invariant via covariance), (3) **correlation-based** (directional), (4) **information-theoretic** (KL divergence, mutual information). For **financial time series**, the **angular distance** `d(x, y) = √(0.5 × (1 - corr(x, y)))` is often preferred because it captures the *co-movement* of the returns, not the level.

## Key Concepts

- **Euclidean distance** — `||x - y||_2`.
- **Mahalanobis distance** — `√((x - y)' S^(-1) (x - y))`.
- **Angular distance** — `√(0.5 × (1 - corr(x, y)))`; the basis of HRP.
- **Correlation-based distance** — `1 - corr(x, y)`; the basis of hierarchical clustering.
- **KL divergence** — `KL(p || q) = E_p[log(p/q)]`; the information-theoretic distance.
- **Mutual information** — `MI(X, Y) = E[log p(X, Y) / (p(X) p(Y))]`; the information shared.
- **Cophenetic correlation** — the correlation between the distance matrix and the dendrogram-derived distance; a measure of clustering quality.
- **The "1 - correlation" metric** — the basis of the HRP algorithm.

## Formulas & Tables

- **Euclidean**: `d(x, y) = √(Σ (x_i - y_i)²)`.
- **Mahalanobis**: `d(x, y) = √((x - y)' S^(-1) (x - y))`.
- **Angular**: `d(x, y) = √(0.5 × (1 - corr(x, y)))`.

## Key Takeaways

1. The angular distance is the institutional default for financial clustering.
2. The Mahalanobis distance is scale-invariant.
3. KL divergence is the information-theoretic distance.

## Connects To

- ch04 (Optimal Clustering), ch07 (Portfolio Construction), `lopez-de-prado-afml` ch16 (HRP).
