# Chapter 21: Credit Value at Risk

> Hull 4e, pp. 447–461. The distribution of credit losses: the foundation of Basel IRB.

## Core Idea

**Credit VaR** is the high quantile (e.g. 99.9%) of the loss distribution from defaults over a 1-year horizon. The loss distribution is a **mixture of a binomial (number of defaults) and a Beta (loss given default)**: the **Vasicek model** is the closed-form single-factor model. The Basel IRB (Internal Ratings-Based) approach uses `UL = LGD × [N((1 - R)^(-0.5) × G(PD) + (R / (1-R))^(0.5) × G(0.999)) - PD] × EAD`, with `G` the inverse normal and `R` the asset correlation.

## Key Concepts

- **Loss Given Default (LGD)** — the fraction of EAD lost in default; typically 40-60%.
- **Exposure at Default (EAD)** — the exposure at the time of default.
- **Probability of Default (PD)** — the annual default probability.
- **Maturity (M)** — the effective maturity of the exposure.
- **Asset correlation (R)** — the correlation of the obligor's asset value with the systematic factor; the input to the Vasicek model.
- **Vasicek single-factor model** — the foundation of Basel IRB.
- **Unexpected Loss (UL)** — the loss in excess of expected loss at a high confidence.
- **Expected Loss (EL)** — the average loss; `EL = PD × LGD × EAD`.
- **Granularity adjustment** — the correction for finite-portfolio effects (Gordy 2003).
- **Basel IRB formula** — `K = LGD × [N((1 - R)^(-0.5) × G(PD) + (R / (1-R))^(0.5) × G(0.999)) - PD] × maturity_adjustment × EAD`.

## Formulas & Tables

- **Vasicek PD**: `PD = N(-(1/√R) × N^(-1)(p_default) + √(1/R) × X)`, where `X` is the systematic factor.
- **Conditional PD**: `PD(X) = N((N^(-1)(PD) - √R × X) / √(1-R))`.
- **Vasicek loss rate**: `L(X) = LGD × PD(X)`.
- **Basel IRB capital**: as above.
- **Granularity adjustment**: `GA = (LGD² × PD × (1-PD) × R) / (number of obligors) × ...` (the exact formula is in BCBS 2006 §IV.B).

## Key Takeaways

1. Credit VaR is the high quantile of the loss distribution; the Vasicek model is the closed form.
2. The Basel IRB formula is the institutional standard; it requires PD, LGD, EAD, R, M.
3. Expected Loss is reserved as a provision; Unexpected Loss is the capital.

## Connects To

- ch15-16 (Basel II/III), ch19 (PDs), ch20 (CVA), `tsay-analysis-financial-time-series` ch05 (Credit spread dynamics).
