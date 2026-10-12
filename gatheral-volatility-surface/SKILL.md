---
name: gatheral-volatility-surface
description: "Knowledge base from Jim Gatheral, The Volatility Surface: A Practitioner's Guide (Wiley 2004). Use when fitting or pricing options with stochastic or local volatility, fitting the SVI parameterisation to the implied volatility surface, applying arbitrage-free conditions (no-butterfly, no-calendar), pricing variance swaps or volatility swaps (model-free replication), working with barrier options or exotic cliquets, or using the SABR, Heston, Heston-Nandi, SVJ, SVJJ, Merton, or CreditGrades models. Covers 11 chapters on stochastic vs local volatility, the Heston model, the implied vol surface and SVI, the Heston-Nandi model, jumps, default risk, surface asymptotics, surface dynamics, barrier options, exotic cliquets, and volatility derivatives."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# The Volatility Surface (Gatheral)

**Source**: Jim Gatheral, *The Volatility Surface: A Practitioner's Guide*, Wiley 2004 | **Domain**: Finance de marché | **Chapters**: 11 | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview.
- **With a topic or framework name** (e.g. "Heston", "SVI", "Dupire", "variance swap", "SABR"): jump to the relevant chapter.
- **With a chapter number**: open `chapters/chNN-*.md`.

## Core Frameworks & Mental Models

1. **Stochastic Volatility (SV) vs Local Volatility (LV)** (ch01): SV is for the *dynamics*; LV is for the *snapshot*. LV is derived from the market by Dupire's formula; SV is fitted to the time series.
2. **Dupire's Formula** (ch01): `σ_loc²(K, T) = [∂C/∂T + (r-q)K ∂C/∂K - qC] / (0.5 K² ∂²C/∂K²)`. The LV that exactly fits the market smile.
3. **The Heston Model** (ch02): the workhorse SV model; closed-form via the characteristic function.
4. **The SVI Parameterisation** (ch03): `w(k) = a + b(ρ(k - m) + sqrt((k - m)² + σ²))`. 5 parameters; the institutional fit to the surface.
5. **The Arbitrage-Free Conditions** (ch03, 2026 update with Gatheral-Jacquier 2011): the SVI parameters must satisfy the no-butterfly and no-calendar conditions.
6. **The Heston-Nandi Model** (ch04): the closed-form version of Heston; GARCH-like variance.
7. **Jumps** (ch05): SVJ and SVJJ; the SVJJ model is required to reproduce the short-maturity skew.
8. **Merton Structural Model** (ch06): equity is a call on the firm's assets; default when assets < liabilities.
9. **The SABR Model** (ch07): the standard rates model; Hagan expansion for short-maturity asymptotics.
10. **Lee's Moment Formula** (ch07): the asymptotic implied vol at extreme strikes.
11. **Bergomi's Stochastic Implied Vol** (ch08): the implied vol as a stochastic process.
12. **Barrier Options** (ch09): the reflection principle and the discrete-monitoring adjustment.
13. **Exotic Cliquets** (ch10): the locally-capped globally floored cliquet, the reverse cliquet, the Napoleon.
14. **Variance Swaps** (ch11): the model-free replication via the log contract.
15. **The Convexity Adjustment** (ch11): the difference between the vol swap and the variance swap.

## Chapter Index

| # | Title | Key Frameworks | File |
|---|---|---|---|
| 1 | Stochastic Volatility and Local Volatility | SV vs LV, Dupire's formula | [ch01](./chapters/ch01-stochastic-and-local-volatility.md) |
| 2 | The Heston Model | Heston SDE, characteristic function, Feller | [ch02](./chapters/ch02-the-heston-model.md) |
| 3 | The Implied Volatility Surface | SVI, no-butterfly, no-calendar | [ch03](./chapters/ch03-the-implied-volatility-surface.md) |
| 4 | The Heston-Nandi Model | Closed-form Heston | [ch04](./chapters/ch04-the-heston-nandi-model.md) |
| 5 | Adding Jumps | Merton, Kou, SVJ, SVJJ | [ch05](./chapters/ch05-adding-jumps.md) |
| 6 | Modeling Default Risk | Merton structural, CreditGrades | [ch06](./chapters/ch06-modeling-default-risk.md) |
| 7 | Volatility Surface Asymptotics | SABR, Lee, Fouque-Papanicolaou-Sircar | [ch07](./chapters/ch07-volatility-surface-asymptotics.md) |
| 8 | Dynamics of the Volatility Surface | Bergomi, digital cliquets | [ch08](./chapters/ch08-dynamics-of-the-volatility-surface.md) |
| 9 | Barrier Options | Reflection principle, discrete adjustment | [ch09](./chapters/ch09-barrier-options.md) |
| 10 | Exotic Cliquets | Locally-capped globally floored, reverse cliquet | [ch10](./chapters/ch10-exotic-cliquets.md) |
| 11 | Volatility Derivatives | Variance swap, log contract, VIX | [ch11](./chapters/ch11-volatility-derivatives.md) |

## Topic Index

- **Arbitrage-free conditions** → ch03 (SVI)
- **Bergomi model** → ch08
- **Butterfly arbitrage** → ch03
- **Calendar arbitrage** → ch03
- **Capital structure arbitrage** → ch06
- **Characteristic function** → ch02, ch05
- **Cliquet** → ch10
- **Convexity adjustment** → ch11
- **CreditGrades** → ch06
- **Digital cliquet** → ch08, ch10
- **Digital option** → ch08
- **Dupire's formula** → ch01
- **Extreme strike** → ch07
- **Feller condition** → ch02
- **Forward implied vol** → ch10
- **Hagan expansion** → ch07
- **Heston model** → ch02
- **Heston-Nandi** → ch04
- **Jump-to-default** → ch06
- **Knock-in / Knock-out** → ch09
- **Lee's formula** → ch07
- **Local volatility (LV)** → ch01
- **Log contract** → ch11
- **Merton structural model** → ch06
- **Model-free replication** → ch11
- **Napoleon** → ch10
- **Parisian option** → ch09
- **Quasi-static hedging** → ch08
- **SABR** → ch07
- **Skew** → ch03, ch07
- **Smile** → ch03
- **Stochastic volatility (SV)** → ch01, ch02
- **SVI parameterisation** → ch03
- **Variance swap** → ch11
- **VIX** → ch11
- **Volatility swap** → ch11

## Supporting Files

- [glossary.md](./glossary.md) — Alphabetical glossary.

## Related Skills

- **`hull-derivatives`** (finance-de-marche) — The Hull options/futures/swap pricing book; ch15 (Volatility Smiles) and ch17 (Volatility Surfaces) are the related chapters.
- **`hull-risk-management`** (finance-de-marche) — ch12 (VaR/ES) for the option portfolio VaR.
- **`frtb-market-risk-bcbs457`** (finance-de-marche) — The FRTB market risk framework; the regulatory reference.
- **`tsay-analysis-financial-time-series`** (fondamentaux) — ch05 (GARCH) for the variance dynamics.
- **`grinold-kahn-apm`** (gestion-de-portefeuille) — ch08 (Valuation in Theory) for the consensus.
- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — ch05 (FFD) for stationary features.

## Scope & Limits

- **Coverage**: 11 chapters of the 2004 book. The book predates Gatheral & Jacquier 2011 (the definitive SVI arbitrage-free parameterisation); the practitioner update notes in ch03 cross-reference the 2011 paper.
- **Edition year**: 2004 — supplemented by:
  - Gatheral & Jacquier 2011 "Arbitrage-Free SVI Volatility Surfaces" (the definitive SVI parameterisation).
  - Hagan, Kumar, Lesniewski, Woodward 2002 "Managing Smile Risk" (the SABR paper).
  - Bergomi 2008 "Smile Dynamics" (the stochastic implied vol).
  - The post-2004 VIX futures market developments.
- **What the source does NOT cover**:
  - The Hull options/futures/swap pricing book (see `hull-derivatives`).
  - The risk management / VaR framework (see `hull-risk-management`).
  - The FRTB / Basel (see `frtb-market-risk-bcbs457`).
  - The time-series foundation (GARCH — see `tsay-analysis-financial-time-series` ch05).
- **OCR / extraction quality**: pdftotext output is clean; no reconstruction needed. Some formula notation was rendered with care.
- **Translation**: English.
