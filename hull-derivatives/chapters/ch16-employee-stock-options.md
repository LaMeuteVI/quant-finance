# Chapter 16: Employee Stock Options

## Core Idea
ESOs are long-dated American calls that vest, cannot be sold, and are often exercised early. They must be expensed at fair value, which is usually estimated with BSM using an *expected life* or with trees or exercise-multiple models. Their incentive effects are double-edged.

## Frameworks Introduced
- **Contract features**: at-the-money grants, 10-year life, vesting period (often 3–4 years; cliff or graded), forfeiture on leaving, and early-exercise behavior (employees cannot sell, so they exercise to diversify).
- **Incentive analysis**: options reward volatility and short-term price spikes. They may encourage risk-taking, earnings management and bad timing of announcements. Restricted stock aligns more symmetrically.
- **Accounting**: since 2005 (FAS 123R / IFRS 2) the fair value at grant date is expensed over the vesting period. Before 2005, at-the-money grants had zero intrinsic-value expense.
- **Valuation approaches**:
  1. **BSM with expected life**: T = the expected time to exercise or expiry, S adjusted for dividends.
  2. **Binomial tree** with vesting, employee exit rates and an exercise-probability function.
  3. **Exercise multiple**: assume exercise when S/K reaches a barrier multiple (e.g., 2.0).
  4. **Market-based**: sell instruments that replicate ESO payoffs (Zions Bancorporation).
- **Dilution**: exercise creates new shares. The market usually prices the dilution at announcement, so no further adjustment is needed at valuation.

## Key Concepts
- **Vesting**: the period before options can be exercised.
- **Forfeiture**: unvested options are lost when the employee leaves.
- **Expected life**: the average time from grant to exercise or expiry.
- **Backdating**: illegally picking a past grant date with a lower price while claiming ATM. Detected via abnormal pre-grant returns. Prosecutions began in 2007.
- **Springloading / bullet-dodging**: timing grants around news.
- **Reload options / repricing**: resetting K after declines, which undermines incentives.

## Mental Models
- **ESOs are worth less to the employee than their fair value**: they are undiversified and non-transferable.
- **An option grant is a convex payoff**. It rewards variance, so expect more risk-seeking behavior.
- **Expected-life BSM is a shortcut**. It is acceptable for accounting but misses path-dependent exercise.

## Anti-patterns
- **Backdating**: the stock price history before grants showed a suspicious V-shape. It is illegal and reputationally catastrophic.
- **Ignoring early exercise and forfeiture**: this overstates the expense.
- **Using ATM grants as a "free" compensation**: it was an accounting artifact before 2005.

## Worked Example
**Example 16.1.** 1,000,000 ATM options granted with S = K = $30, a 10-year life, 3-year vesting and an expected life of 4.5 years. σ = 25%, PV(dividends over 4.5 years) = $4 and r = 5%.
- BSM with S₀ = 30 − 4 = 26, K = 30, T = 4.5 → **$6.31 per option**.
- The income statement expense is **$6.31m**, recognized over the vesting period.

## Key Takeaways
1. ESOs are long-dated, non-transferable, vesting American calls with early exercise.
2. Fair value must be expensed. The standard shortcut is BSM with the expected life.
3. Trees with vesting/exit/exercise rules or exercise multiples are more accurate.
4. Options reward volatility and timing, so the incentive design matters.
5. Backdating is fraud, and detectable statistically.

## Connects To
- **Ch 10**: warrants and convertibles.
- **Ch 15**: BSM with dividends and dilution.
- **Ch 13 / Ch 21**: trees with custom exercise rules.
- **Ch 26**: barrier-like exercise (exercise multiple).
