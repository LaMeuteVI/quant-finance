# Chapter 9: Principal Components and Factor Models

> Tsay, Chapter 9. PCA, factor analysis, statistical factor models.

## Core Idea

**Principal Component Analysis (PCA)** reduces the dimensionality of a multivariate series by finding the orthogonal directions of maximum variance. **Factor models** assume that the common variation of a set of returns is driven by a small number of latent factors. **Statistical factor models** (PCA-based) and **macroeconomic factor models** (Chen-Roll-Ross 1986, Fama-French 1993, 2015) are the two main approaches.

## Key Concepts

- **Principal components** — the orthogonal directions of maximum variance; the eigenvectors of the covariance matrix.
- **Scree plot** — the plot of eigenvalues vs. component number; the basis for choosing the number of factors.
- **Factor model** — `r_t = α + β f_t + ε_t`, with `f_t` the latent factors.
- **Statistical factor model** — `f_t` is estimated by PCA or maximum likelihood.
- **Macroeconomic factor model** — `f_t` is an observable macroeconomic variable (e.g. inflation, industrial production).
- **Fama-French factors** — Mkt-RF, SMB, HML, RMW, CMA, UMD; the institutional reference for US equities.
- **Asymptotic PCA** — the Connor-Korajczyk matrix; for large N.
- **Factor mimicking portfolio** — a tradable portfolio that mimics a factor; see `grinold-kahn-apm` ch08.

## Formulas & Tables

- **PCA**: `Σ = P Λ P'`, with `P` the matrix of eigenvectors and `Λ` the diagonal of eigenvalues.
- **Factor model**: `r_t = α + β f_t + ε_t`, with `E[ε_t] = 0`, `Cov(ε_t, f_t) = 0`.
- **The Fama-French 5-factor model**: `R_i - R_f = α_i + β_M (Mkt-RF) + β_S SMB + β_V HML + β_R RMW + β_C CMA + ε_i`.

## Key Takeaways

1. PCA reduces dimensionality; 3-5 factors typically explain 80%+ of variance.
2. The Fama-French 5-factor model is the institutional reference.
3. The factors are estimable; the betas are the loadings.

## Connects To

- ch07 (Multivariate), ch08 (Multivariate Vol), `grinold-kahn-apm` ch07, ch08, `lopez-de-prado-afml` ch16 (HRP), `cfa-portfolio-management`.
