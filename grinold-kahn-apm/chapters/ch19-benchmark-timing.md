# Chapter 19: Benchmark Timing

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 19, pp. 541–557

## Core Idea

Benchmark timing is the **active bet on the benchmark's return** itself — the decision to be *over* or *under* the benchmark in anticipation of a market move. The chapter derives the optimal benchmark exposure as a function of the manager's view on the market's return and the cost of leverage. The conclusion: benchmark timing is a *low-IR* activity in practice, because the manager's view on the market is typically less accurate than the manager's view on individual assets.

## Frameworks Introduced

- **The Optimal Benchmark Exposure**:
  - Given a market return forecast `r̂_M` and a benchmark market exposure `b_M,B`, the optimal market exposure is:
    `b_M* = b_M,B + (IR_M × σ_M^(-1) × (r̂_M − E[r_M])) / λ`, where `IR_M` is the manager's information ratio on the market timing decision.
  - *When to use*: when the manager has a strong view on the market's direction.
  - *Why it works*: the optimal exposure is a function of the manager's skill (IR) and the cost of leverage (λ).
  - *Failure mode*: the manager's view on the market is *rarely* accurate enough to justify a large bet; the historical evidence shows that market timing is value-destructive for most managers.

- **The "equity premium puzzle"**:
  - The expected market return is around 6–8% per year over the long run, but the realised return is highly variable (standard deviation ~20% per year).
  - The manager's information ratio on market timing is typically < 0.1, so the optimal bet is *small*.

## Key Takeaways

1. **Benchmark timing is a low-IR activity.** Most managers' market timing IR is < 0.1.
2. **The optimal bet is proportional to the manager's IR.** A manager with market timing IR = 0.1 should deviate from the benchmark by a small amount; a manager with IR = 0 has zero optimal bet.
3. **The historical record is poor.** Most managers who try to time the market underperform.
4. **The cost of leverage matters.** A 2x leveraged S&P 500 bet has twice the gross alpha but also twice the cost of leverage.
