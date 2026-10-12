# Chapter 4: The Heston-Nandi Model

> Gatheral, *The Volatility Surface*, Chapter 4, pp. 43–49.

## Core Idea

The **Heston-Nandi model** is a closed-form SV model for the variance that allows analytical tractability for European options. The variance follows `dv = κ(θ - v) dt + σ_v √v dW_2`, with the same Heston dynamics but a different parameterisation of the drift. The closed-form solution for the call price is given by a series expansion; the model is widely used for the VIX and for equity-index option markets.

## Key Concepts

- **Heston-Nandi SDE** — the closed-form version of Heston.
- **GARCH-like variance** — the variance process is similar to GARCH(1,1).
- **Closed-form call price** — via series expansion.
- **Risk premia** — the Heston-Nandi model with a *positive* market price of variance risk fits the VIX term structure.

## Worked Example

The Heston-Nandi closed-form call price is `C = S_0 P_1 - K exp(-rT) P_2`, with `P_1, P_2` computed by an infinite series involving the characteristic function.

## Key Takeaways

1. Heston-Nandi is the closed-form SV model.
2. The variance process is GARCH-like.
3. The model is used for the VIX and equity-index options.

## Connects To

- ch02 (Heston), ch03 (Implied Vol Surface), `tsay-analysis-financial-time-series` ch05 (GARCH).
