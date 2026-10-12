# Chapter 11: Correlations and Copulas

> Hull 4e, pp. 231–253. Multivariate dependence: linear correlation, copulas, regime dependence.

## Core Idea

**Linear correlation** (Pearson ρ) captures *linear* dependence but is blind to *tail dependence* and *non-linear* dependence. **Copulas** separate the marginal distributions from the dependence structure: `H(x, y) = C(F_X(x), F_Y(y))` where `C` is the copula. The **Gaussian copula** is the workhorse but has zero tail dependence; the **Student-t copula** has symmetric tail dependence; the **Clayton** and **Gumbel** copulas have asymmetric tail dependence (lower for Clayton, upper for Gumbel). **Regime-dependent correlations** matter: correlations rise in stress (2008, 2020); the historical correlation is a poor guide to the stress correlation.

## Key Concepts

- **Linear correlation (Pearson ρ)** — measures linear dependence.
- **Rank correlation (Spearman, Kendall)** — measure of monotone dependence; more robust.
- **Copula** — the function that joins marginal distributions into a joint distribution.
- **Gaussian copula** — the standard; zero tail dependence.
- **Student-t copula** — symmetric tail dependence; the default for credit/equity portfolios.
- **Clayton copula** — lower tail dependence; suited to "things get worse together".
- **Gumbel copula** — upper tail dependence; suited to "things get better together".
- **Tail dependence coefficient** — the probability that a variable is in its tail given that the other is in its tail.
- **DCC (Dynamic Conditional Correlation)** — Engle 2002; time-varying correlation.
- **Regime-dependent correlation** — correlation rises in stress; the empirical fact.

## Formulas & Tables

- **Copula definition**: `C(u, v) = P(U ≤ u, V ≤ v)` for `U, V` uniform.
- **Sklar's theorem**: `H(x, y) = C(F_X(x), F_Y(y))`.
- **Gaussian copula**: `C_ρ(u, v) = Φ_ρ(Φ^(-1)(u), Φ^(-1)(v))`.
- **Tail dependence (Student-t with ν dof)**: `λ = 2 × t_{ν+1}(-√((ν+1)(1-ρ)/(1+ρ)))`.
- **Kendall's tau** for the Student-t copula: `τ = (2/π) × arcsin(ρ)`.

## Key Takeaways

1. The Gaussian copula fails in stress (zero tail dependence).
2. The Student-t copula is the default for credit/equity portfolios.
3. Correlations rise in stress; the historical correlation is a poor guide.

## Connects To

- ch12 (VaR — multi-asset), ch14 (Model-Building — correlations), ch17 (FRTB), `lopez-de-prado-afml` ch02 (Information-driven bars — for multi-asset).
