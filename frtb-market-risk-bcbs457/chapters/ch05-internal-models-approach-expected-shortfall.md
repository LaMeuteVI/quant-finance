# Chapter 5: Internal Models Approach — Expected Shortfall (IMA-ES)

> BCBS 457, MAR30–MAR33.

## Core Idea

The **Internal Models Approach (IMA)** allows the bank to use its own internal model for market risk capital, subject to regulatory approval. The IMA capital is `ES_t × m_t`, where `ES_t` is the 97.5% Expected Shortfall at time `t` and `m_t` is a **multiplier** between 1.0 and 1.84 that depends on the bank's backtest exception count and the **P&L attribution test (PLAT)**. The IMA also requires a separate **Default Risk Charge (DRC)** and a **Stress Scenario** for non-modellable factors.

## Frameworks Introduced

- **Expected Shortfall (ES)** — the tail-average risk measure; the IMA primary metric.
- **The 97.5% confidence level** — the FRTB IMA confidence; tighter than the pre-FRTB 99%.
- **The 1-day holding period** — for ES, vs the pre-FRTB 10-day.
- **The IMA multiplier `m_t`** — 1.0 (green) to 1.84 (red) based on backtest + PLAT.
- **The P&L attribution test (PLAT)** — compares the bank's hypothetical P&L (from the risk model) to the actual P&L; a systematic mismatch is a red-zone flag.
- **The stress scenario** — the IMA capital uses the worse of today's ES and a 12-week stressed-window ES.
- **Non-Modellable Risk Factors (NMRFs)** — the IMA requires a separate stress scenario for factors that cannot be modelled.

## Formulas & Tables

- **IMA capital**: `ES_t × m_t` (with DRC and NMRF stress scenario added).
- **ES at 97.5%**: `ES_97.5 = E[L | L > VaR_97.5]`.
- **The multiplier `m_t`**: `m_t = min(1.84, 1 + (zone - 1) × 0.21)`, with `zone ∈ [1, 4]` based on the combined backtest + PLAT.
- **PLAT**: a chi-squared test of the distribution of `actual_PnL - risk_theoretical_PnL`; rejection implies model error.

## Key Takeaways

1. The IMA capital is `ES_t × m_t`.
2. The multiplier is between 1.0 and 1.84.
3. The PLAT is the formal validation; the backtest is the operational check.
4. The stress scenario is required.

## Connects To

- ch01, ch06 (Backtesting), `hull-risk-management` ch12 (VaR/ES), ch17 (FRTB preview).
