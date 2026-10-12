# Chapter 6: Modeling Default Risk

> Gatheral, *The Volatility Surface*, Chapter 6, pp. 74–86.

## Core Idea

For **distressed stocks**, the price process has a non-zero probability of a sudden jump to zero (default). The **Merton (1974) structural model** treats equity as a call option on the firm's assets; the **CreditGrades** model is a tractable version with closed-form survival probability. The implied vol surface is steepened by the default risk; the **left-wing** of the smile reflects the *jump-to-default* risk.

## Key Concepts

- **Merton structural model** — equity is a call on the firm's assets.
- **CreditGrades model** — a tractable structural model; closed-form survival probability.
- **Jump-to-default** — the price jumps to zero at default.
- **Capital structure arbitrage** — the put-call parity violation between equity and credit.
- **Survival probability** — the probability that the firm does not default by time T.
- **Equity volatility** — the volatility of the equity; related to asset volatility and leverage.

## Formulas & Tables

- **Merton d1, d2**: `d_1 = (log(V_0/D) + (r + σ_V²/2) T) / (σ_V √T)`, `d_2 = d_1 - σ_V √T`.
- **Merton equity value**: `E = V_0 N(d_1) - D exp(-rT) N(d_2)`.
- **Survival probability** (CreditGrades): closed-form in `V_0, D, r, σ_V, T`.

## Key Takeaways

1. Merton treats equity as a call; default when assets < liabilities.
2. The left-wing of the smile reflects jump-to-default risk.
3. Capital structure arbitrage exploits the put-call parity violation.

## Connects To

- ch05 (Jumps), `hull-risk-management` ch19 (PD), ch20 (CVA), `hull-derivatives` ch24 (Credit Derivatives).
