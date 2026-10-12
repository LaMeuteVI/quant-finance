# Chapter 4: An Empirical Example

> **Source**: Diebold & Mariano (1995), Section 4. ⚠ OCR source; reconstructed.

## Core Idea

The DM test is applied to the exchange-rate forecast comparison: the random walk (forecast 2) vs an alternative model (forecast 1). The result: the alternative model is *marginally* better than the random walk, with a DM statistic of about -2.0 (significant at 95% in a two-sided test). The forecast differences are tiny in absolute terms; the DM test's power comes from the long sample.

## The Empirical Setup

- *Data*: monthly exchange rates (pound/dollar, yen/dollar) from 1981 to 1991.
- *Forecast 1*: a regressive forecast (using the lagged exchange rate).
- *Forecast 2*: the random walk (no-change forecast).
- *Loss function*: squared error.

## Key Findings

1. The regressive forecast is *marginally* better than the random walk.
2. The DM statistic is about -2.0 (two-sided) for the pound/dollar; smaller for the yen/dollar.
3. The forecast differences are tiny in absolute terms (a few basis points per month); the DM test's power comes from the 120-month sample.
4. The results are *fragile*: the marginal significance depends on the choice of loss function and the sample period.

## Key Takeaways

1. **The DM test can detect small differences** when the sample is large.
2. **The results depend on the loss function**; an asymmetric loss might give different conclusions.
3. **The results depend on the sample period**; the agent should test the sensitivity.

## Connects To

- **ch01** (DM test setup).
- **ch03** (size and power).
- **ch05** (conclusions and future research).
