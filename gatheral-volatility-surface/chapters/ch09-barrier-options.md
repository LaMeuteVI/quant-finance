# Chapter 9: Barrier Options

> Gatheral, *The Volatility Surface*, Chapter 9, pp. 107–121.

## Core Idea

**Barrier options** have a payoff that depends on whether the price crosses a barrier during the option's life. **Knock-out** options cease to exist if the barrier is hit; **knock-in** options come into existence. The pricing requires the joint distribution of the price at the barrier and at maturity, typically computed via the **reflection principle** (for continuous monitoring) or the **continuously-monitored limit** (the discrete-monitoring adjustment).

## Key Concepts

- **Knock-out call/put** — ceases to exist if the price hits the barrier.
- **Knock-in call/put** — comes into existence if the price hits the barrier.
- **Up-and-out, up-and-in, down-and-out, down-and-in** — the four barrier directions.
- **Continuous vs discrete monitoring** — continuous is the standard; discrete requires an adjustment.
- **Reflection principle** — the closed-form for Brownian motion hitting a barrier.
- **Parisian options** — the option knocks out only if the price has been *continuously* beyond the barrier for a specified time.
- **Ladder options** — a sequence of barriers with different payoffs.
- **Lookback options** — the payoff depends on the maximum or minimum of the price path.

## Formulas & Tables

- **Knock-out call (continuous)**: `C_KO = C_BS - (S/H)^(2λ) × C_BS(S_0 = H²/S)`, with `H` the barrier and `λ = (r-q+σ²/2)/σ²`.
- **Reflection principle**: `P(max S_t > H) = 2 × P(S_T > H)` for Brownian motion.
- **Discrete monitoring adjustment**: `C_discrete ≈ C_continuous × exp(-β × √(T / monitoring_freq))` for some constant `β`.

## Key Takeaways

1. The reflection principle gives the closed-form for continuous monitoring.
2. Discrete monitoring requires an adjustment (typically 1-3% lower price for the same barrier).
3. Lookback and Parisian options are path-dependent.

## Connects To

- ch08 (Dynamics), ch10 (Exotic Cliquets), `hull-derivatives` ch20 (Exotic Options), ch26 (Numerical Procedures).
