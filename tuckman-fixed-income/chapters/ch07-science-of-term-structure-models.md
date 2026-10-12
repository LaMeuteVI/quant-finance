# Chapter 7: The Science of Term Structure Models
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 7 (Part Three: Term Structure Models), plus the Part Three introduction

## Core Idea
Given (1) today's prices of the **underlying securities** (zeros, i.e. the current term structure) and (2) an assumed tree for the short rate, any interest-rate contingent claim can be priced **by arbitrage**. The price is the cost of a *dynamically* rebalanced replicating portfolio. Equivalently, and far more efficiently, it is the **expected discounted value under risk-neutral probabilities**: the probabilities that make every underlying security's expected discounted value equal its market price. Real-world probabilities never enter directly. Their only influence runs through current bond prices. **OAS** measures a market price's deviation from the model price. With a factor-hedged and financed position, the expected P&L is OAS plus convergence.

## Frameworks Introduced
- **Arbitrage pricing on a one-period binomial tree**:
  - When to use: pricing any claim whose payoff depends on the short rate next period.
  - How:
    1. Write the claim's payoffs in the up and down states.
    2. Solve for face amounts `F.5` (six-month zero) and `F1` (one-year zero) that match both payoffs.
    3. Price = cost of that portfolio today (law of one price).
  - Why it works: if the market price differs, buy the cheap side, short the replicating portfolio, and pocket a riskless profit.
- **Risk-neutral pricing (the four-step argument)**:
  1. Given the trees of the underlying securities, the arbitrage price of a replicable claim does not depend on risk preferences. Everyone agrees on the replicating portfolio.
  2. Imagine an economy with the same bond prices and short-rate outcomes, but with risk-neutral investors who price by expected discounted value. Their probabilities must reprice the underlying bonds: these are the **risk-neutral probabilities**.
  3. In that economy, the claim's price is its expected discounted value under those probabilities.
  4. By step 1 the price is the same in both economies. So **price any derivative as its expected discounted value under the risk-neutral probabilities**.
  - Efficiency: calibrate the tree once (as much work as one arbitrage pricing), then price any number of claims by backward induction.
- **Multi-period calibration (building the risk-neutral tree)**:
  - How: extend the short-rate tree one date at a time. At each date choose the risk-neutral probability, here the same up-probability q from every node on a date, so that the next-longer zero reprices to its market price. Then solve for q by backward induction; the equation is linear in q.
  - Consequence: once the short-rate process and the initial spot curve are fixed, all longer rates at future nodes are *determined*. In a one-factor model you cannot make separate assumptions about the one-year rate.
- **Dynamic vs static replication**:
  - Static: the portfolio of zeros replicating a coupon bond never changes, whatever rates do (Part One).
  - Dynamic: the portfolio replicating an option or other contingent claim must be rebalanced at every date and state.
- **Option-adjusted spread (OAS)**:
  - Definition: the constant spread that, **added to the risk-neutral short rates for discounting only (not for computing cash flows)**, makes model price equal market price.
  - Reading: OAS > 0 means the security is cheap (market price below model value). OAS < 0 means it is rich.
- **P&L attribution with OAS**:
  - Formula: `dP = (r + OAS)P dt + (∂P/∂x)(dx − E[dx]) + (∂P/∂OAS) dOAS`.
  - Terms: carry-roll-down, rate (factor) surprise, spread change or convergence.
  - For a factor-hedged position (∂P/∂x = 0) financed at r: **expected P&L = OAS earned over time + OAS sensitivity × convergence**.
- **Recombining vs non-recombining trees**:
  - Non-recombining trees capture state-dependent volatility naturally but have 2ᴺ terminal nodes: > 500,000 for 10 years semiannual, > 500 billion for 20 years.
  - Recombining trees have N+1 terminal nodes: 1,561 for 30 years weekly. Implement state-dependence another way.
- **Model-to-application map (Part Three introduction)**:

| Model class | Calibrates to | Typical use |
|---|---|---|
| Black-Scholes-style (ch18) | underlying price/rate and its volatility | caplets, floorlets, European swaptions, bond and futures options |
| One-factor short-rate (ch07–ch10) | term structure plus a handful of vol products | interpolating or extrapolating illiquid bonds and swaps (e.g. a 50y swap with a 30y curve), callable bonds, when simplicity beats precision |
| Multi-factor short-rate, e.g. Gauss+ (ch11) | a few curve points plus a few vol products | relative value trading, cross-product risk management, scenario analysis |
| LMM (ch11) | full curve plus a large set of vanilla vols | pricing and hedging exotics (e.g. Bermudan swaptions) |

  - Caveat: these models are for **relative** pricing. With a constant risk premium they say nothing about whether rates are too high. Time-varying risk premia (Cochrane-Piazzesi, Ludvigson-Ng) are outside the book.

## Key Concepts
- **Underlying securities**: securities whose prices are taken as given (here the zeros that define today's curve). Contingent claims are priced relative to them.
- **Interest rate contingent claim**: a security whose cash flows depend on the level of rates (bond options, CMT swaps, caps, callables).
- **Binomial tree / dates / states**: dates are columns numbered 0, 1, 2… left to right. States are rows numbered from 0 at the bottom. The node (date i, state j) carries the short rate and prices.
- **Expected discounted value**: the probability-weighted average of discounted payoffs. Over many periods, take the expectation of discounted values, not the discounted expected value.
- **True (real-world) probabilities**: the modeller's view of the actual rate evolution.
- **Risk-neutral probabilities**: probabilities under which every underlying security's expected discounted value equals its market price.
- **Drift**: the expected change in the short rate per step. The risk-neutral drift exceeds the true drift when investors demand a risk premium for bearing rate risk.
- **Risk penalty**: the price of a risky bond is below its expected discounted value under true probabilities. Derivatives inherit this penalty through the underlying's price.
- **One-factor model**: a single random variable (the short rate) drives the entire term structure.
- **Dynamic replication**: a replicating portfolio whose composition changes with date and state.
- **OAS**: the spread over risk-neutral discount rates that equates model and market price. It is a relative-value measure *conditional on the model*.
- **Time step Δt**: discounting over one step is `1/(1 + rΔt)`. Smaller steps give a finer rate distribution but more computation and more round-off.
- **State-dependent volatility**: volatility that depends on the rate level. It naturally produces non-recombining trees.

## Formulas & Reference Tables
- Discounting one step (semiannual): `P = V/(1 + r/2)`. In general `P = V/(1 + rΔt)`.
- Replication (one period): `F.5 + P₁,ᵤ·F₁ = Vᵤ` and `F.5 + P₁,d·F₁ = V_d`. Price = `P.5·F.5 + P₁·F₁`, where P₁,ᵤ and P₁,d are the date-1 prices per $1 face of the original one-year zero.
- Risk-neutral probability from the one-year zero: `p = [P₁(1 + r₀/2) − P₁,d]/(P₁,ᵤ − P₁,d)`, where P₁,ᵤ and P₁,d are the date-1 up/down prices of that zero.
- Risk-neutral pricing: `V₀ = [p·Vᵤ + (1 − p)·V_d]/(1 + r₀Δt)`, applied recursively backward (plus any cash flow paid at the node).
- Risk-neutral drift for symmetric ±h moves: `E*[Δr] = (2p − 1)h`.
- OAS valuation: `Vᵢ,ⱼ = [q·Vᵢ₊₁,ⱼ₊₁ + (1 − q)·Vᵢ₊₁,ⱼ + CFᵢ₊₁]/(1 + (rᵢ,ⱼ + OAS)Δt)`. Cash flows still use the unshifted rᵢ,ⱼ.
- Expected return under risk-neutral probabilities: `E*[dP/P] = r dt` for a fairly priced security, and `(r + OAS) dt` for a security with an OAS.
- Taylor decomposition: `dP = (∂P/∂x)dx + (∂P/∂t)dt + (∂P/∂OAS)dOAS`.
- Return decomposition: `dP/P = (r + OAS)dt + (1/P)(∂P/∂x)(dx − E[dx]) + (1/P)(∂P/∂OAS)dOAS`. Under true probabilities, a risk-premium term is added (ch08).
- Tree size: non-recombining 2ᴺ terminal nodes, recombining N + 1.

**Why stock-option models don't transfer directly to bonds**

| Equity (BSM) assumption | Problem for bonds |
|---|---|
| Price follows an unconstrained random process | bond price must pull to par at maturity |
| Constant price volatility | bond price volatility must fall to 0 at maturity |
| Constant short rate (harmless vs stock vol) | indefensible when the underlying *is* a rate-driven asset |
| Model one underlying | a 5y bond becomes a 4.5y bond, so you must model the whole curve, hence short-rate models |

Exception: short-dated options on long bonds, where BSM-style models (Black) are used in practice (ch18).

## Mental Models
- **Probabilities matter only through prices.** Raise the real up-probability and the one-year zero's price falls. Since the call's replicating portfolio is long that zero, the call falls too. Given prices, you do not need probabilities.
- **Risk-neutral = a drift adjustment.** Risk-neutral probabilities are true probabilities tilted toward higher rates (lower bond prices). In the example the 6-month rate's drift goes from 0 (true) to about +30bp in the first period and about +15bp in the second (risk-neutral).
- **Calibrate once, price many.** Risk-neutral pricing wins over explicit replication because the tree is fitted once to the curve, and every claim then prices by backward induction.
- **OAS is the carry of a cheap security.** Hedged and financed, a positive-OAS position earns OAS per unit of time while it stays cheap, plus a windfall if it converges. It is only as good as the model and the assumption that OAS is stationary.
- **Pick the time step for the problem.** Monthly steps can price a 30y callable, but they give only two rates at expiry for a 1-month option. Swaption desks trade precision against quote turnaround time.

## Worked Example
**A. The chapter tree (6-month steps, face $1,000; verified in python).**
- Inputs: spot rates 5% (0.5y), 5.15% (1y), 5.25% (1.5y). Short rate 5%, moving ±50bp per step (true probability ½).
- One-year zero:
  - Date 0 price `1000/1.02575² = 950.42`.
  - Date 1 prices `1000/1.0275 = 973.24` (up) and `1000/1.0225 = 977.995` (down).
  - Expected discounted value under true probabilities `= ½(973.24 + 978.00)/1.025 = 951.82` > 950.42. The difference is the risk penalty.
- Risk-neutral p: `(973.24p + 978.00(1 − p))/1.025 = 950.42`, so **p = 0.8024**. The drift is +30.24bp over the six months.
- Call on the then-6-month zero, struck at 975, expiring on date 1. Payoffs: 0 (up) and 3.00 (down).
  - Replication: `F.5 + .97324F₁ = 0` and `F.5 + .97800F₁ = 3`, giving F₁ = +630.25 and F.5 = −613.39.
  - Cost `= .97561(−613.39) + .95042(630.25) = $0.58`.
  - Risk-neutral: `.1976 × 3/1.025 = $0.58` ✓.
  - True-probability expected discounted value would be $1.46, which is wrong.
- Date 2: short rates 6%/5%/4%, 1.5y zero at 925.21. Solving the linear equation for the date-1 up-probability gives **q = 0.6489** (drift +14.89bp).
  - Date-1 prices of the 1.5y zero: 946.51 (up) and 955.78 (down).
  - Implied one-year spot rates in six months: **5.5736% / 4.5743%**. They are pinned down, not assumed.
- Stylized CMT swap on the 6-month yield, struck at 5%, $1mm notional, paying `(y − 5%)/2 × 1mm`. Payoffs: date 1 ±2,500; date 2 +5,000/0/−5,000.
  - Date-1 values: `.6489 × 5,000/1.0275 + 2,500 = 5,657.66` (up) and `−.3511 × 5,000/1.0225 − 2,500 = −4,216.87` (down).
  - Date-0 value: `(.8024 × 5,657.66 − .1976 × 4,216.87)/1.025` = **$3,616.05**. Under true probabilities it would be ≈ −$5.80, not 0 (ch13 explains why).
- OAS: at a market price of 3,613.25, add 10bp to every *discount* rate (5.6%, 4.6%, 5.1%). This reproduces 3,613.25, so OAS = +10bp and the swap is cheap.
  - Expected six-month risk-neutral return = 2.50% at fair value, 2.55% at OAS 10bp (= 5.10%/2).
- Precision note: the book rounds 977.995 to 978.00. At full precision p = 0.8009, q = 0.6519 and the CMT swap = $3,615.86. When you calibrate, never round intermediate prices.

**B. Second calibrated tree (Exercise 7.2–7.3, recomputed).**
- Inputs: short rate 5%, moving ±100bp per 6 months. Zeros: 97.5610 (0.5y), 95.0908 (1y), 92.5069 (1.5y).
- Calibration:
  - `p = [95.0908 × 1.025/100 − 1/1.02]/(1/1.03 − 1/1.02) = 0.600`.
  - Solving the 1.5y zero for the date-1 probability gives q = 0.700.
- Collared floater, $100 face, 1.5y. Coupon on date i+1 = `½ × min(max(rᵢ, 3.5%), 6.5%)`, with principal at maturity.
  - Date 2: rates 7%/5%/3%. Values `(100 + coupon)/(1 + r/2)` = 99.758 / 100.000 / 100.246.
  - Date 1: `[E*(V₂) + ½·rᵢ]/(1 + rᵢ/2)` gives 99.836 (6% node) and 100.072 (4% node).
  - **Date 0 = 99.932.** The collar is worth −0.068: the 6.5% cap bites more often than the 3.5% floor under the upward-drifting risk-neutral tree.

## Anti-patterns
- **Pricing by expected discounted value under real-world (or "house macro") probabilities**: this ignores the risk penalty embedded in bond prices. The call was worth $0.58, not $1.46. Exercise 7.1 shows a caplet priced off an economist's 25% probability forecast; that is not an arbitrage price.
- **Assuming a separate process for longer rates in a one-factor model**: the short-rate process plus the initial curve already fixes them.
- **Shifting cash flows along with discount rates when computing OAS**: OAS shifts discounting only. Coupons that depend on rates still use the model rates.
- **Reading OAS as model-free cheapness**: OAS is conditional on the model's volatility and drift. A different model gives a different OAS.
- **Using non-recombining trees for long-dated products**: the node count explodes. Implement state-dependent volatility in a recombining way.
- **A time step that is too coarse, or needlessly fine**: too coarse gives poor distributions and misplaced cash flows. Too fine gives round-off and slow quotes.
- **Porting equity BSM to bond options without thought**: it violates pull-to-par and declining price volatility, and it assumes a constant short rate.

## Practitioner Notes
- Tuckman's desk sequence: (1) fix the underlying prices, (2) assume a short-rate tree, (3) calibrate the risk-neutral probabilities (or drifts, in ch09) to reprice the curve, (4) price everything by backward induction, (5) report OAS for anything trading away from the model.
- Relative-value workflow: find a positive-OAS security, buy it, hedge the factor exposure (∂P/∂x = 0 via the model's replicating portfolio), and finance at the short rate. The P&L = OAS × time + OAS duration × convergence. The risk is non-convergence or an OAS that widens.
- Tree steps in practice: vary the step size across the tree (fine near option expiries, coarse later). Daily steps with a 65bp horizon s.d. give a realistic, near-normal six-month rate distribution.
- CMT swaps trade mostly on 2y, 5y and 10y yields. The book's six-month version is stylized.
- One-factor models suit interpolation or extrapolation of liquid bonds and swaps: they bring arbitrage discipline, which some prefer to cubic splines. They also suit callable-bond pricing calibrated to the issuer curve and a few similar swaptions, where precision is less critical.

## Key Takeaways
1. Price contingent claims relative to given bond prices plus an assumed short-rate process. The price is the cost of a dynamic replicating portfolio.
2. Risk-neutral probabilities are those that reprice the underlying bonds. Every claim is then its expected discounted value under them, computed by backward induction.
3. Real-world probabilities enter only through current bond prices, and risk-neutral drift exceeds true drift because of the risk premium.
4. In a one-factor model the initial curve plus the short-rate tree determines all future longer rates.
5. OAS = the spread to risk-neutral discount rates (discounting only) that matches the market price. Positive means cheap.
6. `dP = (r + OAS)P dt + factor surprise + OAS change`. A factor-hedged, financed position earns OAS plus convergence.
7. Use recombining trees with a step size fit for purpose. Never round intermediate calibration prices.
8. Equity option models fail for bonds (pull to par, vanishing volatility, stochastic rates), except for short options on long bonds.

## Connects To
- **ch01–ch02**: static replication and discount factors, the Part One arbitrage that this chapter generalizes to dynamic replication.
- **ch03**: P&L attribution (carry-roll-down, rates, spread), which the OAS decomposition formalizes.
- **ch08**: why risk-neutral drift exceeds true drift, and the expectations/convexity/risk-premium decomposition of the curve.
- **ch09–ch10**: choosing the drift and volatility of the short-rate process (Ho-Lee, Vasicek, CIR, Black-Karasinski).
- **ch11**: multi-factor Gauss+ and LMM.
- **ch13**: why expected discounted cash flows ≠ discounted expected cash flows (forward vs futures, the CMT −$5.80 puzzle).
- **ch18**: when Black-style models replace term structure models.
- **ch20**: OAS for mortgages.
- **`cfa-fixed-income` ch08**: the arbitrage-free valuation framework (binomial trees calibrated to par curves, pathwise valuation).
- **`cfa-fixed-income` ch09**: OAS and callable/putable bonds.
- **`hull-derivatives` ch13**: binomial trees and risk-neutral valuation for equities.
- **`hull-derivatives` ch28**: martingales and measures, the formal counterpart of risk-neutral pricing.
- **`hull-derivatives` ch32**: no-arbitrage short-rate trees.
