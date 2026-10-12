# Chapter 20: CVA and DVA

> Hull 4e, pp. 429–445. Counterparty credit risk: the market value of default.

## Core Idea

**CVA (Credit Value Adjustment)** is the market value of the counterparty's default risk to the institution. For an uncollateralised derivative, `CVA ≈ (1 - R) × Σ_{t_i} (DF(t_i) × EE(t_i) × PD(t_{i-1}, t_i))`, where `R` is the recovery, `DF` is the discount factor, `EE` is the expected exposure at time `t_i`, and `PD` is the marginal default probability. **DVA (Debit Value Adjustment)** is the symmetric adjustment for the institution's own default risk. **FVA (Funding Value Adjustment)** is the cost of funding the uncollateralised exposure. **Wrong-way risk** is the dangerous case where exposure and PD are positively correlated (e.g. an oil derivative with an oil-producer counterparty).

## Key Concepts

- **Expected Exposure (EE)** — the expected positive exposure at a future date.
- **Effective Expected Exposure (EEE)** — the running maximum of EE; the basis for the credit limit.
- **Potential Future Exposure (PFE)** — a high quantile (e.g. 97.5%) of the exposure distribution.
- **CVA** — the discounted expected loss from counterparty default.
- **DVA** — the symmetric adjustment for the institution's own default.
- **FVA (Funding Value Adjustment)** — the cost of funding the exposure.
- **ColVA (Collateral Valuation Adjustment)** — the adjustment for the cost of posting collateral.
- **Wrong-way risk** — exposure rises as the counterparty's credit deteriorates.
- **Right-way risk** — exposure falls as the counterparty's credit improves.
- **Close-out netting** — netting the exposure across trades with the same counterparty.
- **Netting set** — the set of trades with the same counterparty that can be netted.
- **ISDA Master Agreement** — the standard agreement governing OTC derivatives.
- **CSA (Credit Support Annex)** — the agreement governing collateral.

## Formulas & Tables

- **CVA**: `CVA ≈ (1 - R) × Σ_t DF(t) × EE(t) × PD(t-1, t)`.
- **DVA**: `DVA ≈ (1 - R_inst) × Σ_t DF(t) × ENE(t) × PD_inst(t-1, t)`, where `ENE` is the expected negative exposure.
- **FVA**: `FVA ≈ -Σ_t (funding_spread(t) × EPE(t) × DF(t))`.
- **EE (risk-neutral)**: `EE(t) = E[max(V(t), 0)]`, the expected positive MTM.
- **PFE**: `PFE_α(t) = Q_α(V(t))`, the α-quantile of the MTM distribution.

## Key Takeaways

1. CVA, DVA, FVA are the three XVAs; the XVA desk is a separate function.
2. Wrong-way risk is dangerous and must be explicitly modeled.
3. Collateral (CSA) and netting (ISDA) reduce CVA.

## Connects To

- ch21 (Credit VaR), ch18 (CCPs), ch25 (Model Risk), `hull-derivatives` ch26 (More on Models — numerical procedures for CVA).
