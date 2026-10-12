# Chapter 7: Portfolio Construction

> López de Prado, MLAM, Chapter 7.

## Core Idea

**Portfolio construction** with ML signals: (1) **Hierarchical Risk Parity (HRP)** — the algorithm of `lopez-de-prado-afml` ch16, (2) **Nested Clustered Optimisation (NCO)** — the generalisation, (3) **Equal-Weighted Portfolio (EWP)** — the institutional baseline, (4) **Inverse-Variance Portfolio (IVP)** — the simple Sharpe-maximising alternative, (5) **Minimum-Variance Portfolio (MVP)** — the most robust.

## Key Concepts

- **Equal-Weighted Portfolio (EWP)** — `w_i = 1/N`; the baseline.
- **Inverse-Variance Portfolio (IVP)** — `w_i = (1/σ_i²) / Σ (1/σ_j²)`; the Sharpe-maximising alternative.
- **Minimum-Variance Portfolio (MVP)** — `w* = V^(-1) 1 / (1' V^(-1) 1)`.
- **HRP** — the algorithm of `lopez-de-prado-afml` ch16.
- **NCO** — the generalisation.
- **Critical Line Algorithm (CLA)** — Markowitz's efficient frontier; numerically stable.

## Formulas & Tables

- **IVP**: `w_i = (1/σ_i²) / Σ (1/σ_j²)`.
- **MVP**: `w* = V^(-1) 1 / (1' V^(-1) 1)`.

## Key Takeaways

1. EWP is the baseline; IVP is the Sharpe-maximising alternative; MVP is the most robust.
2. HRP is the ML-based alternative.
3. The choice of portfolio depends on the reliability of the covariance matrix.

## Connects To

- ch04, ch06, `lopez-de-prado-afml` ch16, `grinold-kahn-apm` ch14.
