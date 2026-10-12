# Chapter 3: Standardised Approach — Default Risk Charge (SA-DRC)

> BCBS 457, MAR22.

## Core Idea

The **Default Risk Charge (DRC)** is the FRTB SA capital charge for default risk. The ES model does not capture default risk well; the FRTB requires a separate, model-based charge. The bank calculates the DRC as the loss from the default of a single obligor (or a correlated group of obligors) at a 99.9% confidence level. The risk weights and correlations are prescribed.

## Frameworks Introduced

- **Single-name DRC** — the loss from a single obligor default.
- **Multi-name DRC** — the loss from correlated defaults.
- **PD (Probability of Default)** — the 1-year default probability; the input to the DRC.
- **LGD (Loss Given Default)** — the loss in default; typically 50% for senior unsecured.
- **Maturity adjustment** — a scaling factor for the time-to-maturity.
- **Correlation parameters** — the prescribed inter-obligor correlations.

## Formulas & Tables

- **DRC for a single name**: `RW × EAD × LGD × PD`, where `RW` is the risk weight based on the obligor's rating and maturity.
- **DRC for a portfolio**: aggregated using the prescribed correlation structure (similar to the IRB formula in `hull-risk-management` ch21).
- **Risk weights** (illustrative): AAA-A = 0.5-2%, BBB = 5-8%, BB = 12-20%, B = 20-30%, CCC = 50%, defaulted = 100%.

## Key Takeaways

1. The DRC is required in addition to the ES-based capital.
2. The DRC is at 99.9% confidence (one-year).
3. The risk weights and correlations are prescribed.

## Connects To

- ch01, ch02, ch04, `hull-risk-management` ch19 (PDs), ch21 (Credit VaR).
