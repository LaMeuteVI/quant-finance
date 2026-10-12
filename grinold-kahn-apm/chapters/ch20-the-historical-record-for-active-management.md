# Chapter 20: The Historical Record for Active Management

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 20, pp. 559–572

## Core Idea

This is the empirical chapter: what does the historical record say about whether active management can produce alpha? The 1999 book reviews mutual-fund performance studies and concludes that the *consistency* of alpha production is low — most funds underperform in any given year, and the persistence of alpha across years is modest. The chapter is the empirical foundation for the rest of the book: if alpha is hard to produce, the *process* (the four-stage active management process of ch01) is what separates the persistent winners from the losers.

The chapter's most important message for the modern reader: **the historical record is more pessimistic than the book suggests**, and the persistence of alpha is even weaker than the 1999 evidence shows.

## Frameworks Introduced

- **The Mutual-Fund Performance Studies**:
  - The 1990s evidence (reviewed in the book) suggested that:
    1. Most funds underperform the index in any given year.
    2. The persistence of alpha across years is modest.
    3. The few funds that *do* persist are concentrated in a small number of fund families.
  - The 1990s evidence was based on the **CRSP mutual fund database** (US) and equivalent databases in other markets.

- **The SPIVA Scorecard** (the modern update, not in the 1999 book):
  - The S&P Indices Versus Active (SPIVA) scorecards, published since 2002, show the percentage of active funds that underperform the index over various horizons.
  - The 2023 SPIVA US scorecard: over 15 years, ~85% of large-cap active funds underperform the S&P 500; over 20 years, ~92%.
  - The international / emerging market / small-cap scorecards are less pessimistic but still show a majority of active funds underperform.

- **The Fama–French Critique** (post-1999):
  - Fama & French (2010, "Luck versus Skill in the Cross-Section of Mutual Fund Returns") show that the t-statistic of alpha for the average fund is around 1.0, not significant.
  - The few funds that *do* have significant alpha are concentrated in the right tail; their IR is ~0.4.

- **The McLean–Pontiff Critique** (post-2016):
  - McLean & Pontiff (2016, "Does Academic Research Destroy Stock Return Predictability?") show that the post-publication decay of academic anomalies is ~26% out-of-sample and ~58% after transaction costs.
  - This is the most important post-1999 critique of the persistence of alpha.

- **The Harvey–Liu Multiple-Testing Haircut** (post-2015):
  - Harvey, Liu & Zhu (2015, RFS) argue that the standard t-statistic threshold for anomalies should be 3.0, not 2.0.
  - With this haircut, most published anomalies fail the significance test.

## Key Concepts

1. **Persistence of alpha** — the autocorrelation of a fund's alpha across years; the empirical measure of skill.
2. **SPIVA scorecard** — the S&P scorecard of active vs index performance; the modern empirical standard.
3. **Fama–French decomposition** — the decomposition of fund returns into exposures to the Fama–French factors.
4. **Post-publication decay** — the reduction in alpha after an anomaly is published; McLean–Pontiff 2016.
5. **Multiple testing haircut** — the correction for the number of trials; Harvey–Liu 2015.
6. **The 3.0 t-stat** — the modern threshold for statistical significance in finance.

## Formulas & Reference Tables

**Fama–French (2010) "luck vs skill" decomposition**

`α̂ = ā + b × σ(α̂) × t + ε`, where `ā` is the mean alpha, `b` is the regression coefficient, `σ(α̂)` is the cross-sectional standard deviation of the alpha estimates, and `t` is the t-statistic.

For US mutual funds, the cross-sectional distribution of `α̂` is consistent with `ā ≈ 0` and `b ≈ 1` — i.e. the cross-section of alpha is dominated by noise.

**The 3.0 t-stat rule (Harvey–Liu 2015)**

For an anomaly with `T` monthly observations, the t-statistic must exceed 3.0 to be considered significant (after correction for multiple testing). For `T = 600` (50 years of monthly data), the corresponding SR is `3.0 / √600 × √12 = 0.43` — a high bar.

**The McLean–Pontiff decay**

The in-sample alpha of an academic anomaly decays by ~26% out-of-sample and by ~58% after transaction costs.

**The SPIVA scorecard (2023, US Large Cap)**

- 1 year: 60% of active funds underperform.
- 5 years: 75% underperform.
- 10 years: 80% underperform.
- 15 years: 85% underperform.
- 20 years: 92% underperform.

(These are the *survivorship-adjusted* numbers; the gross underperformance is even larger.)

## Mental Models

- **The historical record is a *prior* on alpha.** The agent should use the SPIVA / Fama–French / Harvey–Liu evidence as a *prior* that the alpha is hard to produce.
- **A single high-IR year is not a strategy.** The persistence of alpha is weak; a 3-year track record is the minimum for any capital allocation.
- **The bar for "alpha" has been raised.** The 3.0 t-stat and the post-publication decay mean that a backtest SR of 1.0 is not impressive in 2026; the bar is ~2.0 in many contexts.

## Worked Example (RECOMPUTED — illustrative)

*Setup.* A backtest of a momentum strategy from 2000–2024, monthly data, 25 years × 12 = 300 monthly observations. Annualised SR = 0.8.

*Step 1 — t-statistic*:
- `t = SR × √(T/12) = 0.8 × √(300/12) = 0.8 × √25 = 0.8 × 5 = 4.0`. **Significant at 99.9% in the in-sample.**

*Step 2 — Apply the Harvey–Liu haircut*:
- 3.0 t-stat is the new threshold. The strategy passes with t = 4.0.

*Step 3 — Apply the McLean–Pontiff decay*:
- The strategy is *not* an academic anomaly; it's the manager's own. The decay factor is typically less than 26% (closer to 10–20%) for proprietary signals.
- OOS SR = 0.8 × (1 − 0.15) = 0.68.

*Step 4 — Apply the SPIVA haircut*:
- SPIVA says most active funds underperform. The prior on the manager's alpha should be low.
- Adjusted OOS SR = 0.68 × 0.6 (60% adjustment for the SPIVA prior) = 0.41.

*Step 5 — Conclusion*:
- A backtest SR of 0.8 is "good", but after the multiple-testing haircut, the post-publication decay, and the SPIVA prior, the realistic OOS SR is ~0.4. The strategy is still worth trading but the AUM capacity is limited.

*Sanity check (Python).*
```python
import math
SR, T_months = 0.8, 300
t_stat = SR * math.sqrt(T_months/12)
print(f"t-stat: {t_stat:.2f}  (Harvey-Liu threshold: 3.0)")

decay = 0.15
SR_OOS = SR * (1 - decay)
print(f"SR after McLean-Pontiff decay: {SR_OOS:.2f}")

spiva_adj = 0.6
SR_adjusted = SR_OOS * spiva_adj
print(f"SR after SPIVA prior adjustment: {SR_adjusted:.2f}")
```

## Anti-patterns

- **Reporting a backtest SR without the multiple-testing haircut.** Always apply the Harvey–Liu 3.0 t-stat rule.
- **Ignoring the post-publication decay.** Even an academic anomaly decays by 26% OOS; a proprietary signal decays less but it still decays.
- **Extrapolating a 3-year track record.** The minimum is 5 years, and even 5 years is fragile.
- **Trusting a backtest that ignores transaction costs.** The net SR is typically 30–50% of the gross SR.

## Practitioner Notes

- **2026 update.** The 2023 SPIVA scorecard is the most recent empirical reference. The 20-year underperformance rate of 92% for US large-cap is the institutional evidence that *most* active management is value-destructive.
- **Factor investing** is the modern response to the failure of stock-picking: instead of trying to beat the index, the manager harvests well-known factors (value, momentum, quality) that have *some* persistence. The factor IRs are typically 0.2–0.5, much lower than the active-stock-picking IRs that active managers claim.
- **The "smart beta" framework** is the institutional version of factor investing.
- **The Fama–French 5-factor model** is the standard risk model; Carhart's 4-factor model adds momentum; the Hou–Xue–Zhang q-factor model is the modern academic alternative.

## Key Takeaways

1. **The historical record is pessimistic.** Most active funds underperform; persistence of alpha is weak.
2. **The modern bar for alpha is higher** (3.0 t-stat, post-publication decay, SPIVA prior).
3. **The agent's prior on a new strategy should be skeptical.** The empirical evidence says alpha is hard.
4. **Factor investing is the modern institutional response** to the failure of stock-picking.
5. **The "luck vs skill" decomposition** is the framework for any new strategy: is the backtest evidence *really* skill, or is it luck?

## Connects To

- **ch17** (Performance Analysis): the chapter is the *post-mortem* of a single strategy; this chapter is the *meta-analysis* of all active management.
- **ch21** (Open Questions): the open questions the book identifies (factor persistence, transaction costs, etc.).
- **`cfa-performance-measurement` skill (in build)**: the GIPS-aligned performance measurement.
- **`lopez-de-prado-afml` ch15 (Strategy Risk)**: the deeper analysis of strategy risk.
- **`hull-risk-management` ch12 (VaR and ES)**: the backtest of a VaR model uses the same statistical discipline.
- **`diebold-mariano-forecast-accuracy` skill**: the forecast-comparison test that complements the strategy-comparison test.
