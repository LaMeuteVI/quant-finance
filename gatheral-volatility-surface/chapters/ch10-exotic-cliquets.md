# Chapter 10: Exotic Cliquets

> Gatheral, *The Volatility Surface*, Chapter 10, pp. 122–132.

## Core Idea

**Cliquets** are structured products that pay a coupon based on the realised performance of an index over a sequence of observation dates. The **locally-capped globally floored cliquet** is the most common. The **reverse cliquet** and the **Napoleon** are the institutional variants. The pricing requires the joint distribution of the index at each observation date, typically computed via the **forward implied vol** or the **local-vol Monte Carlo**.

## Key Concepts

- **Cliquet** — a structured product with coupons based on the realised performance over a sequence of dates.
- **Locally-capped globally floored** — the most common; the local cap is per-period, the global floor is over the life.
- **Reverse cliquet** — the coupon is paid when the index *underperforms*; the structured short.
- **Napoleon** — a more complex cliquet with multiple features.
- **Forward implied vol** — the implied vol for a forward-starting option; the basis of the cliquet pricing.

## Formulas & Tables

- **Cliquet coupon**: `C = (1/N) × Σ_{i=1}^N max(r_i - cap, floor)`, with `r_i` the realised return over period `i`.
- **Forward implied vol**: `σ_F(T_1, T_2)` — the implied vol for an option starting at `T_1` and ending at `T_2`.

## Key Takeaways

1. Cliquets are sensitive to the forward implied vol, not the spot implied vol.
2. The local cap and global floor are the standard features.
3. The reverse cliquet is the structured short; the Napoleon is a more complex variant.

## Connects To

- ch08 (Dynamics), ch09 (Barrier), `hull-derivatives` ch20 (Exotic Options).
