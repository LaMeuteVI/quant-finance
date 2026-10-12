# Chapter 36: Real Options

## Core Idea
Traditional NPV discounts expected cash flows at a single risk-adjusted rate. That fails when a project contains options (to expand, abandon, defer, switch), because the risk of those options differs from the project's risk. Instead:
1. Adjust each variable's growth to its risk-neutral value, **μ − λσ**.
2. Discount at the risk-free rate.
3. Value the embedded options with trees.

## Frameworks Introduced
- **Capital investment appraisal problem**: NPV with a WACC is inconsistent for options, whose risk differs from the underlying project's risk. The same logic explains why BSM does not use μ.
- **Risk-neutral valuation for real assets**:
  - For each state variable θ with real-world growth m, volatility s and market price of risk λ, use the risk-neutral growth **m − λs**.
  - Compute expected cash flows under these drifts and discount at r.
- **Estimating λ**:
  - From CAPM: `λ = ρ(μ_m − r)/σ_m`, where ρ is the correlation of the variable with market returns.
  - Or from futures prices when they exist (commodities).
- **Valuing a business (Amazon.com, 1999)**:
  - Model revenue growth with mean-reverting growth rates and volatilities, plus a bankruptcy barrier.
  - Monte Carlo under risk-neutral drifts gave a value close to the market price.
- **Embedded options**:
  - Abandon = a put on the project.
  - Expand/contract = a call/put on a fraction of the project.
  - Defer = an American call on the project.
  - Extend life, switch inputs or outputs.
  - Value them on a tree of the project value or commodity price, with a decision at each node.

## Key Concepts
- **Real option**: an option on a real asset: land, a plant, R&D, a mine.
- **Market price of risk λ**: the excess return per unit of volatility demanded by investors for exposure to the variable.
- **Project value tree**: the underlying is the PV of the project's cash flows.
- **Operating flexibility**: the value of being able to respond to information.

## Mental Models
- **"Strategic NPV" = static NPV + value of options.** Flexibility is valuable when uncertainty is high and decisions are reversible or deferrable.
- **Use μ − λσ, not a risk-adjusted discount rate.** It keeps valuation consistent across the project and its options.
- **A negative-NPV project can still be worth holding** if the option to wait or expand is valuable.

## Anti-patterns
- **Discounting option-like payoffs at the project's WACC**: this systematically misprices the flexibility.
- **Ignoring that exercising a real option destroys it**: deferring loses cash flows (it acts like a dividend yield).
- **Overstating real option values with volatility estimates that are too high**, or with options that are not truly exercisable.

## Worked Example
**Option to rent (Example 36.1).**
- Rent is $30/sq ft/yr. Real-world growth m = 12%, volatility 20%, λ = 0.3, r = 5%.
- A company can pay $1m now for the right to rent 100,000 sq ft at $35 for 5 years, starting in 2 years (rent paid annually in advance).
- Risk-neutral growth = 0.12 − 0.3 × 0.2 = **6%**, so Ê(V) = 30e^{0.12} = 33.82.
- Annuity factor A = 1 + e^{−0.05} + … + e^{−0.20} = 4.5355.
- Expected payoff = 453,550 × [33.82N(d₁) − 35N(d₂)] = $1.5015m.
- Value = 1.5015e^{−0.10} = **$1.3586m** > $1m cost, so buy the option.

## Key Takeaways
1. Replace real-world growth m with m − λs, then discount everything at r.
2. Estimate λ via CAPM (correlation with the market) or from futures prices.
3. Real options (abandon, expand, defer, switch) are valued on trees of project value or commodity prices.
4. Flexibility can turn a negative static NPV into a positive strategic NPV.
5. Business valuation (Amazon 1999) can be done by risk-neutral Monte Carlo of fundamentals.

## Connects To
- **Ch 28**: market price of risk.
- **Ch 13 / Ch 21**: trees and Monte Carlo.
- **Ch 35**: commodity processes for extraction projects.
- **Corporate finance**: NPV, WACC, CAPM.
