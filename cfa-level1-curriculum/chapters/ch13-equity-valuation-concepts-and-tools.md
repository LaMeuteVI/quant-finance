# Chapter 13: Equity Valuation — Concepts and Basic Tools (Equity)

## Core Idea
Estimate intrinsic value with three families of models and compare it with price:
- **Present value**: DDM or FCFE.
- **Multiples**: P/E, P/B, P/S, P/CF, EV/EBITDA.
- **Asset-based**: fair value of assets minus liabilities.

Good analysis reconciles the three, so that multiples are *justified* by the fundamentals behind the PV models.

## Frameworks Introduced
- **Three model families**:
  - **Present value (DDM, FCFE)**: value = PV of expected future cash flows to shareholders.
  - **Multiplier models**: price or enterprise-value multiples relative to comparables or to justified fundamentals.
  - **Asset-based**: market or fair value of assets − liabilities. Best for firms with few intangibles; otherwise use it as a floor.
- **Dividend terminology and events**:
  - Regular, extra/special, stock dividends. Splits and reverse splits (no economic effect). **Buybacks**.
  - Reasons for buybacks: signaling undervaluation, flexibility, tax efficiency, offsetting option dilution.
  - Timeline: **declaration → ex-dividend date → holder-of-record date → payment**. Buy on or after the ex-date and you do not get the dividend.
- **DDM**:
  - Infinite horizon: `V₀ = Σ Dₜ/(1 + r)ᵗ`.
  - Finite horizon n: `V₀ = Σ_{t=1}^{n} Dₜ/(1 + r)ᵗ + Pₙ/(1 + r)ⁿ`.
- **FCFE approach**: `FCFE = CFO − FCInv + net borrowing`, and `V₀ = Σ FCFEₜ/(1 + r)ᵗ`. Use it when dividends do not reflect the capacity to pay.
- **Required return (CAPM)**: `r = r_f + β × (E(R_m) − r_f)`.
- **Preferred stock**:
  - Non-callable, non-convertible perpetual: `V₀ = D/r`.
  - With maturity n: `V₀ = Σ D/(1 + r)ᵗ + F/(1 + r)ⁿ`.
- **Gordon (constant growth) model**: `V₀ = D₁/(r − g) = D₀(1 + g)/(r − g)`, requiring r > g.
  - Suited to mature, stable dividend payers.
  - **Sustainable growth**: `g = b × ROE`, where b is the retention ratio (1 − payout).
- **Multistage DDM**:
  - Two-stage: high growth, then stable growth. Three-stage: growth → transition → maturity.
  - Value = PV(explicit dividends) + PV(terminal value from Gordon at the start of the stable phase).
- **Multiples**:
  - Common ones: P/E, P/B, P/S, P/CF.
  - **Justified P/E** from Gordon: `P₀/E₁ = (D₁/E₁)/(r − g) = payout/(r − g)`.
  - **Method of comparables** (law of one price): compare with peer or industry medians.
  - Limitations: trailing multiples ignore the future (use forward multiples); comparables can all be mispriced together.
- **Enterprise value**: `EV = market cap + preferred + debt − cash & short-term investments`. The takeover cost; use EV/EBITDA to compare across capital structures.
- **Asset-based caveats**: fair values of hard-to-value (Level 2/3) assets are uncertain, book values differ from fair values, and unrecorded intangibles (brand, synergies) are missed.

## Key Concepts
- **Intrinsic value vs market price**: undervalued if V > P, overvalued if V < P. Allow for model uncertainty.
- **Terminal value**: the value at the end of the explicit forecast horizon.
- **Retention ratio b** = 1 − dividend payout.

## Mental Models
- **Value drivers are r and g.** Small changes in r − g swing Gordon values a lot. Always run a sensitivity table.
- **Multiples are compressed DCFs**: a high P/E needs low r or high g to be justified.
- **Use EV multiples when leverage differs across peers.**

## Anti-patterns
- ⚠ **Correction vs the notes**: the finite-horizon DDM discounts the terminal price at **(1 + r)ⁿ**, not (1 − r)ᵗ.
- ⚠ **Nuance**: buybacks raise EPS mechanically but **create value only if the shares are bought below intrinsic value**. The notes imply they always increase shareholder wealth.
- **Gordon with g ≥ r**, or with a transitory high growth rate.
- **Comparing P/E across firms with very different leverage or accounting**.

## Worked Example
**Gordon + justified P/E.** D₀ = $2.00, g = 4%, β = 1.2, r_f = 3%, ERP = 5%.
- r = 3% + 1.2 × 5% = **9%**. D₁ = 2.08.
- V₀ = 2.08/(0.09 − 0.04) = **$41.60**.
- With a payout of 40% (E₁ = 5.20), the justified P/E = 0.40/0.05 = **8.0×**.

**Two-stage.** Dividends grow 15% for 2 years from D₀ = 1.00, then 5% forever, with r = 10%.
- D₁ = 1.15, D₂ = 1.3225, D₃ = 1.3886.
- P₂ = 1.3886/(0.10 − 0.05) = 27.77.
- V₀ = 1.15/1.1 + (1.3225 + 27.77)/1.1² = 1.045 + 24.04 = **$25.09**.

**Preferred.** A $5 perpetual dividend at r = 8% is worth **$62.50**.

## Key Takeaways
1. PV models (DDM/FCFE), multiples and asset-based models should triangulate.
2. Gordon: V = D₁/(r − g), with r > g and g = b × ROE.
3. Use multistage DDM for firms not yet in steady state.
4. Justified P/E = payout/(r − g). EV = equity + preferred + debt − cash.
5. Asset-based values work as floors when intangibles are material.

## Connects To
- **Ch 12**: equity types, ROE, cost of equity.
- **Ch 11**: life-cycle stage → which model to use.
- **Ch 16**: the same discounting logic for bonds.
- **Ch 10**: intrinsic vs market value.
