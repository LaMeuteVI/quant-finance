# Chapter 5: Adding Jumps

> Gatheral, *The Volatility Surface*, Chapter 5, pp. 50–73.

## Core Idea

Pure SV models cannot reproduce the *short-maturity* skew observed in equity-index options. **Jumps** (Merton 1976, Kou 2002) are the standard fix: the price has a continuous component plus a Poisson-driven jump component. The **SVJ (SV + Jump in price)** and **SVJJ (SV + Simultaneous Jumps in price and vol)** models are the workhorses. The **SVJJ model** with `ρ < 0` and positive correlation between the vol jump and the price jump produces the steep short-maturity skew observed empirically.

## Key Concepts

- **Merton (1976) jump-diffusion** — the price has a continuous component plus a Poisson-driven jump.
- **Kou (2002) double-exponential jumps** — the jump size is double-exponential; tractable.
- **SVJ (SV + Jump)** — variance is stochastic; price has jumps.
- **SVJJ (SV + Jump in vol and price)** — both the price and the vol jump simultaneously; reproduces the short-maturity skew.
- **Lévy processes** — the general class of jump processes; the basis for the characteristic-function approach.
- **Characteristic function of common jump processes** — Merton, Kou, VG (Variance Gamma), CGMY.

## Formulas & Tables

- **Merton jump-diffusion**: `dS/S = (μ - λ κ) dt + σ dW + (J - 1) dN`, with `N` Poisson(λ) and `J` log-normal.
- **SVJ**: `dS/S = (μ - λ κ) dt + √v dW_1 + (J - 1) dN`, `dv = κ(θ - v) dt + σ_v √v dW_2`.
- **SVJJ**: `dS/S = ... + (J - 1) dN + (V - 1) dN_V`, with `V` the vol jump.
- **Characteristic function** — the Fourier transform of the log-price; closed-form for Merton, Kou, CGMY.

## Key Takeaways

1. Jumps are required to reproduce the short-maturity skew.
2. SVJ fits the smile; SVJJ fits the short-maturity skew.
3. The Merton and Kou jump processes have closed-form characteristic functions.

## Connects To

- ch01-04 (SV/LV), ch06 (Default), ch07 (Asymptotics).
