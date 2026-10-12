# Chapter 8: Dynamics of the Volatility Surface

> Gatheral, *The Volatility Surface*, Chapter 8, pp. 101–106.

## Core Idea

The **dynamics** of the implied vol surface are driven by the dynamics of the underlying variance. Under SV dynamics, the skew is *mean-reverting*; under LV dynamics, the skew is *path-dependent*. **Stochastic implied volatility models** (Bergomi 2008) directly model the implied vol as a stochastic process. **Digital options** and **digital cliquets** are exotic payoffs that depend on the realised skew.

## Key Concepts

- **Skew dynamics under SV** — the skew is mean-reverting to the long-run value.
- **Skew dynamics under LV** — the skew is path-dependent; deterministic in the path of the price.
- **Bergomi's stochastic implied vol** — the implied vol is itself a stochastic process.
- **Digital options** — a payoff of 1 if `S_T > K`, else 0; sensitive to the skew.
- **Digital cliquets** — a sum of digital options over a sequence of dates; the standard structured product.
- **Quasi-static hedging** — hedging a digital option with a position in the underlying options.

## Key Takeaways

1. Skew dynamics differ between SV and LV.
2. Bergomi's model directly models the implied vol.
3. Digital cliquets are sensitive to the skew and the term structure.

## Connects To

- ch01 (SV/LV), ch09 (Barrier), ch10 (Exotic Cliquets), `hull-derivatives` ch17 (Volatility Surfaces), ch20 (Exotic Options).
