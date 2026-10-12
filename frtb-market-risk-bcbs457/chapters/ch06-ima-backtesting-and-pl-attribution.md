# Chapter 6: IMA Backtesting and P&L Attribution

> BCBS 457, MAR32.

## Core Idea

The **IMA backtesting** is the operational validation of the bank's ES model. The bank computes the **hypothetical P&L** (the P&L that would have been realised if the desk had followed the model's positions from yesterday to today) and the **actual P&L**. The exceptions (days when the actual P&L is worse than the VaR at 99%) are counted. The **PLAT** is the formal test of the risk model's accuracy: a chi-squared test of the distribution of `actual_PnL - risk_theoretical_PnL` over the past year. A red-zone flag in either test raises the multiplier `m_t` and may trigger a regulatory response.

## Frameworks Introduced

- **The Backtest** — daily, comparing the 1-day VaR (at 99%) to the actual loss.
- **The Zones** — green (0-4 exceptions), yellow (5-9), red (10+), over 250 days at 99% VaR.
- **The PLAT** — the chi-squared test of the PL distribution.
- **The IMA multiplier `m_t`** — between 1.0 and 1.84, based on the combined backtest + PLAT zone.
- **The Traffic Light Approach** — the visual representation of the backtest.
- **The Spearman Correlation Test** — a secondary test of the rank correlation between hypothetical and actual P&L.
- **The "no excess" test** — the formal condition that the P&L attribution must not be significantly worse than zero.

## Formulas & Tables

- **Backtest exception count**: number of days in the past 250 where `actual_loss > 99% VaR`.
- **PLAT statistic**: a chi-squared test; reject if the statistic is significant at 95%.
- **Multiplier `m_t`**: `m_t = 1.5 + (zone - 1) × 0.21` for zones 1-4 (green to red).

## Key Takeaways

1. The IMA backtest is the operational validation.
2. The PLAT is the formal statistical validation.
3. The multiplier `m_t` is the binding capital adjustment.

## Connects To

- ch01, ch05, `hull-risk-management` ch12 (Traffic Light Backtest), ch25 (Model Risk).
