# Chapter 4: Nonlinear Models and Their Applications

> Tsay, Chapter 4. Threshold AR, Markov switching, smooth transition, neural networks.

## Core Idea

**Nonlinear time series** models capture asymmetries and regime changes that linear models miss. **Threshold Autoregressive (TAR)** models switch between regimes based on a threshold variable. **Markov-Switching (MS) models** have regime-dependent parameters with the regime following a Markov chain. **Smooth Transition Autoregressive (STAR)** models use a smooth transition function. **Neural network models** (the early NAR, NN-AR) are the predecessors of modern deep learning.

## Key Concepts

- **TAR (Tong 1978)** — Threshold AR; two regimes separated by a threshold.
- **SETAR** — Self-Exciting TAR; the threshold is the lagged dependent variable.
- **M-TAR** — Markov-switching TAR; the threshold is exogenous.
- **MS-AR (Hamilton 1989)** — Markov-Switching AR; the regime follows a Markov chain.
- **STAR (Tong 1990)** — Smooth Transition AR; logistic or exponential transition.
- **LSTAR** — Logistic STAR.
- **ESTAR** — Exponential STAR.
- **NAR (Nonlinear AR)** — `X_t = f(X_{t-1}, ..., X_{t-p}) + ε_t` with a non-linear `f`.
- **NN-AR** — Neural network AR; the predecessor of LSTM/Transformer.
- **Bilinear model** — `X_t = α + Σ β_i X_{t-i} + Σ γ_{ij} X_{t-i} ε_{t-j} + ε_t`; an early non-linear model.

## Formulas & Tables

- **TAR(2; 1, 1)**: `X_t = φ_0^(1) + φ_1^(1) X_{t-1} + ε_t` if `X_{t-d} ≤ r`, else `φ_0^(2) + φ_1^(2) X_{t-1} + ε_t`.
- **MS-AR(1)**: `X_t = φ_0(S_t) + φ_1(S_t) X_{t-1} + σ(S_t) ε_t`, with `S_t` a 2-state Markov chain.
- **LSTAR**: `X_t = φ_0 + φ_1 X_{t-1} + (φ_0' + φ_1' X_{t-1}) × G(X_{t-d}; γ, c) + ε_t`, with `G` the logistic function.

## Key Takeaways

1. TAR captures regime-dependent behaviour.
2. Markov-switching models the regime as a Markov chain.
3. STAR is the smooth alternative.

## Connects To

- ch02 (Linear), ch05 (Financial applications), ch09 (Bayesian), `lopez-de-prado-afml` ch17 (Structural Breaks).
