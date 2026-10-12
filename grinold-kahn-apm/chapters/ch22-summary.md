# Chapter 22: Summary

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 22, pp. 577–580

## Core Idea

The book ends with a one-chapter summary of the **four-stage active management process** and the **fundamental law**. This chapter is the *checklist* the agent should apply to any new strategy: does the strategy have a clear information source, a sound forecasting process, a defensible construction, and a cost-aware execution? Does the strategy's IR justify the cost of the research?

The chapter's most important message: **the four-stage process is a discipline, not a recipe**. Every strategy that has succeeded in the long run has applied the discipline; every strategy that has failed has skipped a stage.

## The Four-Stage Active Management Process (the master checklist)

1. **Information** — *What is the raw signal?* Where does it come from? How often is it observed? Is it legal to use? Is it available to other market participants?
2. **Forecasting** — *What is the forecast?* How is the raw signal converted into a forecast of residual return? What is the IC? What is the breadth?
3. **Portfolio Construction** — *What is the optimal portfolio?* Given the forecast and the risk model, what is the optimal active portfolio? Does the IR justify the cost of the research?
4. **Trading** — *What is the execution?* How is the portfolio reached? At what cost? Over what horizon? Is the cost within the breakeven horizon?

The four stages are *sequential* and *iterative*: the output of trading (the realised P&L) feeds back into the information and forecasting stages.

## The Fundamental Law (the summary statement)

`IR = IC × √B × TC`

The IR is the product of three factors:
- **IC** (information coefficient): the correlation between forecast and outcome.
- **B** (breadth): the number of independent bets per period.
- **TC** (transfer coefficient): the efficiency of the translation from forecast to portfolio (≤ 1).

`IC` enters *linearly*; `B` enters as a *square root*; `TC` enters *linearly*. Doubling the IC doubles the IR; doubling the breadth increases the IR by √2; doubling the TC doubles the IR.

## The 12 Key Questions a Manager Must Answer

For each strategy, the manager must answer:

1. What is the *consensus* expected return vector?
2. What is the *active view* (the deviation from the consensus)?
3. What is the *IC* of the signal?
4. What is the *breadth* (the number of independent bets per period)?
5. What is the *horizon* (the time between forecast and outcome)?
6. What is the *cost* of trading (round-trip, in basis points)?
7. What is the *breakeven turnover* (the maximum turnover that still leaves positive net alpha)?
8. What is the *capacity* (the AUM at which the cost reaches the breakeven)?
9. What is the *benchmark*? (The manager must have a benchmark, and the benchmark must be investible.)
10. What is the *IR* of the strategy after costs?
11. What is the *t-statistic of the IR*? (≥ 3.0 for the 2026 bar.)
12. What is the *kill switch*? (The performance threshold below which the strategy is paused.)

## The 5 Most Common Failure Modes

1. **No consensus.** The strategy is built on a view of the market, not a deviation from a consensus; the resulting "alpha" is contaminated with consensus error.
2. **In-sample overfit.** The strategy is fit to the backtest data; the OOS performance is much worse.
3. **Capacity over-estimation.** The strategy is profitable in the backtest at $1M but unprofitable at $1B because of the cost scaling.
4. **No kill switch.** The strategy is allowed to lose money indefinitely; the slow leak eventually depletes the capital.
5. **No OOS test.** The strategy is deployed without an honest out-of-sample check.

## Key Takeaways (the final word of the book)

1. **The four-stage process is the discipline.** Every successful strategy applies it; every failed strategy has skipped a stage.
2. **The fundamental law is the metric.** The IR is the single number that defines active management.
3. **The consensus is the anchor.** Every active view is a deviation from a consensus, not from zero.
4. **Cost matters.** A strategy that does not cover its trading cost is value-destructive.
5. **Persistence is rare.** The historical record shows that most active management does not produce alpha.

## The 2026 Update

- **The fundamental law is unchanged** but the bar is higher: the 3.0 t-stat (Harvey–Liu 2015) and the post-publication decay (McLean–Pontiff 2016) are the modern standard.
- **The DSR/PBO/SPA** is the institutional backtest discipline.
- **The 130/30 format has fallen out of favour**; long-only or modest long/short is the modern default.
- **Factor investing is the institutional response** to the failure of stock-picking.
- **The DSR-adjusted backtest** is the only honest backtest.

## Connects To

- **ch01** (Introduction): the four-stage process.
- **ch06** (Fundamental Law): the IR formula.
- **ch14** (Portfolio Construction): the construction is stage 3.
- **ch16** (Transactions Costs): the trading is stage 4; the cost is the binding constraint.
- **ch20** (The Historical Record): the empirical evidence.
- **ch21** (Open Questions): the questions the book identifies as open; many are now answered.
