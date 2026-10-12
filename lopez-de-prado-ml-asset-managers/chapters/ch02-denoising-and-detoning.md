# Chapter 2: Denoising and Detoning

> López de Prado, MLAM, Chapter 2.

## Core Idea

**Denoising** is removing the noise from the observed correlation matrix; **detoning** is removing the *market mode* (the dominant principal component) from the correlation matrix. Both are necessary for accurate portfolio construction and risk estimation. The **Marčenko-Pastur distribution** gives the theoretical spectrum of the noise eigenvalues; eigenvalues above the MP upper bound are signal. **Detoning** removes the first principal component and adjusts the matrix to be PSD.

## Key Concepts

- **Marčenko-Pastur (MP) distribution** — the theoretical spectrum of a random correlation matrix; the basis for denoising.
- **Denoising** — projecting the noisy correlation matrix onto the signal subspace.
- **Detoning** — removing the dominant market mode from the correlation matrix.
- **Random Matrix Theory (RMT)** — the foundation of denoising.
- **Eigenvalue clipping** — replacing the noisy eigenvalues with the average noise value.
- **Constant Residual Eigenvalue (CRE)** — the assumption that all noise eigenvalues are equal.

## Formulas & Tables

- **Marčenko-Pastur**: `ρ(λ) = √((λ_+ - λ)(λ - λ_-)) / (2π σ² q λ)`, with `λ_± = σ² (1 ± √q)²`, `q = N/T`.
- **Denoising**: replace eigenvalues below `λ_+` with `σ²`.
- **Detoning**: subtract the outer product of the first eigenvector from the correlation matrix.

## Key Takeaways

1. The Marčenko-Pastur distribution is the foundation of denoising.
2. Detoning removes the market mode.
3. Both are necessary for accurate risk estimation.

## Connects To

- ch03, ch07, `lopez-de-prado-afml` ch16 (HRP), `grinold-kahn-apm` ch14 (Portfolio Construction).
