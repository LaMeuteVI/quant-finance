# Chapter 7: Volatility Surface Asymptotics

> Gatheral, *The Volatility Surface*, Chapter 7, pp. 87–100.

## Core Idea

The implied volatility surface has **predictable asymptotic behaviour** at the short-maturity, long-maturity, and extreme-strike limits. The **short-maturity asymptotics** are governed by the **SABR model**: `σ_BS(K, T) ≈ σ_0 × (1 + (ρ σ_0 / 2 + (2-3 ρ²) σ_0² / 12 + (1-ρ²)² ν² / 24) × log(K/F) + ...)` for the Hagan expansion. The **long-maturity asymptotics** are flat; the **extreme-strike asymptotics** are governed by **Lee's moment formula** `lim_{K→0} σ²_BS(K, T) T log²(1/K) = 2(1-ρ)` for SVJ models.

## Key Concepts

- **SABR model** — `dF/F = σ F^β dW_1`, `dσ = ν σ dW_2`, with `dW_1 dW_2 = ρ dt`. The standard rates model.
- **SABR asymptotics** — the Hagan expansion for short-maturity implied vol.
- **Lee's moment formula** — the asymptotic implied vol at extreme strikes.
- **Fouque-Papanicolaou-Sircar asymptotics** — the long-maturity asymptotics of SV models.
- **Lewis (2000) small-vol-of-vol asymptotics** — the corrections for small `σ_v`.
- **Medvedev-Scaillet (2007) short-expiration** — the rigorous short-expiration asymptotics.
- **Roger Lee (2004) extreme strikes** — the bounds on the slope of the smile.

## Formulas & Tables

- **Hagan SABR expansion**: `σ_BS(K, T) = (α / (S_0 K)^(1-β)/2) × [1 + ((1-β)² σ_0² / 24 + ρ β ν σ_0 / 4 + (2-3 ρ²) ν² / 24) T + ...] × z / x × (1 + ...)` with `x = log(F/K)`, `z = ν log(F/K) / α × [1 + ...]`.
- **Lee's formula**: `lim_{K → 0} σ_BS(K, T) × T^0.5 × log(1/K) = √2`, and `lim_{K → ∞} σ_BS(K, T) × T^0.5 × log(K) = √(1 - ρ)` for SVJ.
- **The implied vol slope at the wings**: bounded by the moment formula.

## Key Takeaways

1. The short-maturity asymptotics are governed by the SABR model.
2. The extreme-strike asymptotics are governed by Lee's formula.
3. The long-maturity asymptotics are flat.

## Connects To

- ch03 (Implied Vol Surface), ch04 (Heston-Nandi), ch05 (Jumps), `hull-derivatives` ch17 (Volatility Surfaces).
