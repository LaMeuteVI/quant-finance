# Chapter 10: Bayesian Statistics and MCMC Methods

> Tsay, Chapter 10. Bayesian inference, MCMC, Gibbs sampler, Metropolis-Hastings, applications.

## Core Idea

**Bayesian inference** combines a prior with the data via Bayes' theorem. For complex models (GARCH, SV, multivariate GARCH), the posterior is not closed-form; **Markov Chain Monte Carlo (MCMC)** methods approximate the posterior by drawing samples. The **Gibbs sampler** is the special case where each parameter is updated from its conditional posterior. The **Metropolis-Hastings algorithm** is the general case.

## Key Concepts

- **Prior distribution** — the prior belief about the parameters.
- **Posterior distribution** — `P(θ | data) ∝ P(data | θ) × P(θ)`.
- **Likelihood** — `P(data | θ)`.
- **Gibbs sampler** — iteratively draw each parameter from its conditional posterior.
- **Metropolis-Hastings** — accept or reject a proposal with probability `min(1, p(θ') q(θ | θ') / (p(θ) q(θ' | θ)))`.
- **Convergence diagnostics** — trace plots, R-hat, effective sample size.
- **Bayesian VaR** — the posterior predictive VaR.
- **MCMC standard error** — the standard error of the MCMC estimate.
- **Burn-in period** — the initial samples to discard.
- **Thinning** — keeping every k-th sample to reduce autocorrelation.

## Formulas & Tables

- **Bayes' theorem**: `P(θ | data) = P(data | θ) × P(θ) / P(data)`.
- **Gibbs**: draw `θ_1` from `p(θ_1 | θ_2, ..., θ_k, data)`, then `θ_2` from `p(θ_2 | θ_1, θ_3, ..., data)`, etc.
- **M-H acceptance probability**: `α = min(1, (p(θ') × q(θ | θ')) / (p(θ) × q(θ' | θ)))`.

## Key Takeaways

1. Bayesian inference combines prior and likelihood.
2. MCMC samples the posterior when it's not closed-form.
3. Always check convergence (R-hat < 1.1, effective sample size > 100).

## Connects To

- ch02-08 (the various models fitted via MCMC), `lopez-de-prado-afml` ch14 (DSR — Bayesian Sharpe Ratio).
