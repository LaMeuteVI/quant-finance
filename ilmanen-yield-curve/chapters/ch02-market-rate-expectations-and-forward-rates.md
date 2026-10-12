# Chapter 2: Market's Rate Expectations and Forward Rates
> **Source**: Antti Ilmanen, *Understanding the Yield Curve, Part 2: Market's Rate Expectations and Forward Rates*, Salomon Brothers U.S. Fixed-Income Research (June 1995)

## Core Idea
"The forwards imply rising rates" and "the market expects rising rates" are different statements. The first is arithmetic: forwards are the break-even rates that equalize one-period returns across bonds. The second holds only under the **pure expectations hypothesis** (zero risk premia) with negligible convexity bias. Treasury data from 1970–94 and survey data from 1981–94 reject the PEH. Forwards predict **near-term return differentials** better than rate changes, long rates tend to move *against* the forward-implied direction, and forwards are upward-biased measures of rate expectations. The trading consequence is that rolling-yield advantages tend to be *kept*, so rolling yields and break-even yield changes are usable relative-value indicators.

## Frameworks Introduced
- **Two polar readings of the forward curve** (Ilmanen's Figure 6):

  | Question | Pure expectations hypothesis (BRP = 0) | Risk premium hypothesis (E(Δs) = 0) |
  |---|---|---|
  | What do forwards contain? | market's rate expectations | required risk premia |
  | What should forwards forecast? | future rate changes | near-term return differentials across bonds |
  | Best forecast of the n-year zero's one-period return | the riskless one-period rate | the one-year forward fₙ₋₁,ₙ (its rolling yield) |
  | Best forecast of next period's spot curve | the implied spot curve one year forward | **today's** spot curve |
  | corr(FSPₙ, Δsₙ₋₁) | positive | 0 |
  | corr(FSPₙ, realized BRPₙ) | 0 | positive |

  - When to use: whenever someone reads forwards as "what the market expects". Ask which column they are implicitly assuming.
  - The truth lies in between, but if you must pick a pole, the **risk premium hypothesis** fits the data better.
  - Break-even interpretation is valid under both.
- **Decomposition of the break-even yield change** (linear, ignores convexity):
  - `Δfₙ₋₁ ≡ f₁,ₙ − sₙ₋₁ ≈ E(Δsₙ₋₁) + BRPₙ/(n−1)`
  - `FSPₙ ≡ fₙ₋₁,ₙ − s₁ ≈ (n−1)·E(Δsₙ₋₁) + BRPₙ`
  - so `FSPₙ = (n−1)·Δfₙ₋₁`.
  - Read f₁,ₙ − sₙ₋₁ loosely as "steepness": steepness = expected rate rise + risk premium/duration.
- **Break-even yield change = carry cushion + rolldown cushion**:
  - `Δfₙ₋₁ = (f₁,ₙ − sₙ) + (sₙ − sₙ₋₁)`
  - The first term is the rise in the bond's own yield that offsets its yield carry: `(sₙ − s₁)/Durₙ₋₁`, spread over duration at horizon.
  - The second term is the rolldown the bond would enjoy on an unchanged curve.
  - How: to find how far a constant-maturity rate can rise before a bullish carry trade loses, add the two cushions.
- **Break-even spread change for duration-neutral curve trades**:
  - Any self-financed position breaks even if the implied spot curve one year forward is realized.
  - Positive-carry trades must lose on the spread move, and negative-carry trades must gain.
  - In a **concave** spot curve (the typical shape), a barbell vs bullet flattener gives up yield *and* rolldown. The forwards therefore imply flattening.
  - Linear curve: no implied reshaping. Convex curve: the barbell picks up yield and the forwards imply steepening.
  - The implied flattening depends on the curvature of the **rolling-yield (one-year forward) curve**, which is more concave than the spot curve.
- **Curvature measurement**:
  - Draw a straight line between two zeros. Each point on it is a barbell.
  - The vertical gap to the duration-matched bullet on the **spot** curve gives the bullet–barbell yield spread.
  - On the **forward** curve it gives the bullet–barbell rolling-yield differential.
  - A bigger gap means a more expensive barbell, which needs more flattening to break even.
- **Timing the curve view**: to express a view on the 2s–4s spread *one year ahead*, trade 3y and 5y zeros plus 1y cash, because maturities shorten by a year over the horizon. For an immediate view, trade 2s vs 4s plus cash.

## Key Concepts
- **Pure expectations hypothesis (PEH)**: risk-neutral traders equalize near-term expected returns across all government bonds, so yield spreads only reflect expected capital gains or losses.
- **Risk premium hypothesis**: forwards reflect only expected return differentials, with E(Δs) = 0. The current curve is the best forecast of the future curve.
- **Local expectations hypothesis (LEH)**: equal expected one-period returns.
- **Unbiased expectations hypothesis (UEH)**: forwards equal expected future spots. The two differ by the **convexity bias**. Even with a flat curve where forwards equal expected spots, long (more convex) bonds have higher expected returns.
- **Break-even (implied) spot rate** f₁,ₙ: the selling rate at which the n-year zero's one-year return equals s₁.
- **Implied spot curve one year forward** (f₁,₂ … f₁,₁₀) vs **curve of one-year forward rates** (f₀,₁ … f₉,₁₀). Both are called "forward curves", so always say which one you mean.
- **Rolling yield**: yield + rolldown on an unchanged curve, equal to fₙ₋₁,ₙ.
- **Forward-spot premium (FSP)** fₙ₋₁,ₙ − s₁ = term spread (sₙ − s₁) + rolldown (n−1)(sₙ − sₙ₋₁). On a linear spot curve FSP = 2 × term spread.
- **Realized bond risk premium** hₙ − s₁: the excess holding-period return.
- **Persistence factor (PF)**: the slope from regressing realized BRPₙ on FSPₙ. PF = 0 means forwards are unbiased forecasts (PEH), and PF = 1 means today's curve persists (risk premium hypothesis).
- **Cushion**: the yield (and rolldown) advantage that absorbs adverse rate moves before a position loses.
- **Market price of convexity (survey-based)**: the gap between forward-implied and survey-expected curve flattening.

## Formulas & Reference Tables
- Spot as geometric average of forwards: `(1+sₙ)ⁿ = (1+f₀,₁)(1+f₁,₂)…(1+fₙ₋₁,ₙ)`
- Forward: `(1+f_m,n)ⁿ⁻ᵐ = (1+sₙ)ⁿ/(1+sₘ)ᵐ`. Linear approximation: `f_m,n ≈ (n·sₙ − m·sₘ)/(n−m)`, so `f₁,ₙ ≈ (n·sₙ − s₁)/(n−1)`.
- Break-even: `(1+sₙ)ⁿ/(1+f₁,ₙ)ⁿ⁻¹ = 1 + s₁`
- Holding-period return of a zero: `hₙ ≈ sₙ + (n−1)(sₙ − s*ₙ₋₁)`
- Carry break-even rule of thumb: `f₁,ₙ − sₙ ≈ (sₙ − s₁)/(n−1)`, from `sₙ − Durₙ₋₁·(f₁,ₙ − sₙ) ≈ s₁`
- Break-even constant-maturity change: `Δfₙ₋₁ = f₁,ₙ − sₙ₋₁ = (f₁,ₙ − sₙ) + (sₙ − sₙ₋₁)`
- Expectations + premium: `Δfₙ₋₁ ≈ E(Δsₙ₋₁) + BRPₙ/(n−1)`. Equivalently `f₁,ₙ ≈ E(s*ₙ₋₁) + BRPₙ/(n−1)`
- One-year forward = rolling yield: `fₙ₋₁,ₙ ≈ sₙ + (n−1)(sₙ − sₙ₋₁) = hₙ + (n−1)·Δsₙ₋₁`. It equals hₙ when Δs = 0.
- `FSPₙ ≈ (n−1)·E(Δsₙ₋₁) + BRPₙ = (n−1)·Δfₙ₋₁`
- Coupon bonds: apply the same relations approximately, with duration in place of n, end-of-horizon duration in place of n−1, and yield in place of sₙ.

**Empirical scorecard, U.S. Treasuries 1970–94 (monthly)**

| Maturity | 3m | 6m | 2y | 3y | 4y | 5y |
|---|---|---|---|---|---|---|
| corr(FSPₙ, next-month Δsₙ₋₁) | 0.12 | 0.05 | −0.05 | −0.07 | −0.11 | −0.08 |
| corr(FSPₙ, realized BRPₙ) | 0.37 | 0.22 | 0.17 | 0.17 | 0.19 | 0.15 |

- Persistence factors: about **0.8** below one year (forwards at least get the direction right), and **1.4–2.3** beyond one year (rates move *away* from the forwards).
- The negative long-end correlations are only about 1 s.e. from zero. The BRP correlations are about 2 s.e.

**WSJ survey, 27 semiannual surveys Dec 1981–Dec 1994, 6.5-month horizon**

| | Forward-implied | Survey | Actual |
|---|---|---|---|
| Avg Δ 3-month bill | +0.80 | −0.26 | −0.25 |
| Avg Δ 30-year | +0.10 | −0.14 | −0.24 |
| Avg Δ spread (30y − 3m) | −0.70 | +0.12 | +0.01 |
| Mean abs. error Δ3m / Δ30y / Δspread | 1.21 / 0.88 / 0.91 | 1.03 / 1.00 / 0.75 | no-change: 1.03 / 0.86 / 0.81 |

## Mental Models
- **"Forwards imply" ≠ "market expects".** Implied rate changes are break-evens. Only under BRP = 0 do they become expectations.
- **Same two-year return, different path.** With s₁ = 6% and s₂ = 7%, the 2y zero earns 14.49% over two years either way. Under PEH it earns 6% then 8.01%. Under the risk premium hypothesis it earns 8.01% then 6%. The forward does not tell you which.
- **Level views set the slope, and reshaping views set the curvature.** Expected parallel rises give a linearly rising curve, and expected flattening gives a concave curve. So a concave curve says "flattening expected" *or* "convexity is valuable".
- **Use a blend at the front end and the current curve at the long end.** For bills, the optimal forecast weights the spot and the forward. Beyond one year, the current spot is the better forecast.
- **Survey vs forward gaps are the market's premia.** The rate gap measures the risk premium, and the flattening gap measures the price of convexity.

## Worked Example
**Break-even yield changes on Ilmanen's Figure 1 curve** (spots 6.00, 7.00, 7.75, 8.31, 8.73%, …, recomputed).
1. **2y zero vs 1y zero**:
   - Price today 100/1.07² = **87.34**.
   - f₁,₂ = 1.07²/1.06 − 1 = **8.01%**. At that selling rate the price is 100/1.0801 = **92.58**, a 6.00% return.
   - The bond's own yield must rise 101bp (7.00 → 8.01), but the constant-maturity 1y rate must rise **201bp** (6.00 → 8.01). The difference is rolldown.
2. **3y zero, rule of thumb**:
   - Carry cushion = (7.75 − 6.00)/2 = **0.875%**.
   - Rolldown cushion = 7.75 − 7.00 = **0.75%**.
   - Δf₂ ≈ **1.625%**, so f₁,₃ ≈ 8.625%. The exact value is **8.64%**. The linear rule is about 1.5bp low because it ignores convexity.
3. **Barbell–bullet flattener** (sell the 3y zero; buy equal market values of the 1y and 5y zeros, which is duration-neutral):
   - Yield carry = 0.5(6.00 − 7.75) + 0.5(8.73 − 7.75) = **−39bp**.
   - Rolling-yield carry = 0.5·6.00 + 0.5·10.43 − 9.27 = **−105bp**, using one-year forwards f₀,₁ = 6.00, f₂,₃ = 9.27, f₄,₅ = 10.43.
   - Break-even change of the 2s–4s spread over the year = Δf₄ − Δf₂ = 1.11 − 1.64 = **−52bp**.
   - Interpretation: you need more than 52bp of 2s–4s flattening just to break even. If you only expect 30bp, the "correct" flattening call loses money.

**Implied risk premia from surveys.**
- Forwards implied 106bp more 3-month bill rise than the survey (80 − (−26)).
- Multiply by the duration at horizon (0.25): 26.5bp per six months, about **53bp per year** for rolling 9-month bills.
- For the 30-year: 24bp × horizon duration (about 10) = 240bp per half-year, about **480bp per year**.

## Anti-patterns
- **Saying "the market expects hikes" because forwards slope up**: this ignores BRP. The WSJ survey showed forwards implying +80bp for bills when surveys (and outcomes) were about −25bp.
- **Assuming PEH must hold "or there would be arbitrage"**: this is only true in the risk-neutral pricing world. Arbitrage fixes forwards relative to spots, not the split between expectations and premia (see Asness 1993).
- **Confusing the bond's yield change with the constant-maturity rate change**: they differ by rolldown (101bp vs 201bp above).
- **Mixing up the two "forward curves"**: the one-year forward curve (rolling yields) is not the implied spot curve one year forward.
- **Reading implied flattening as flattening expectations**: forwards almost always imply flattening, while surveys often predicted steepening. Most of the implied flattening is the value of convexity.
- **Trusting surveys as forecasts**: surveys are no more accurate than "no change". The survey correlation with actual 30y moves was −0.22.

## Practitioner Notes
- All three forecasts (forward, survey, no-change) are poor: mean absolute errors are about **100bp per 6 months**, the same size as the moves themselves. Forwards had somewhat larger errors than "no change" (not significant).
- The survey-implied bill premium was highest around the **1982 recession** and after the **1987 crash**. It was low in **1993** despite a steep curve and rose sharply in **1994**, so premia are time-varying and countercyclical.
- Aggregation insight: changing risk *preferences* move the curve more than changing rate *views* do, even though individual views are more volatile. In high volatility everyone demands more premium whatever their view.
- Rate expectation drivers: the central bank sets the front end and long-run inflation expectations set the long end. Easing and tightening come in trends, so the first moves raise expectations of more. Expectations mean-revert when rates are abnormal (1981–82 high, 1992–93 low).
- The finding that forwards give the "wrong sign" at the long end goes back to Macaulay (1938) and to Fama, Shiller–Campbell–Schoenholtz, Mankiw and Fama–Bliss in the 1980s.
- **Desk use**: rolling-yield differentials (for duration extension) and break-even spread changes (for barbell/bullet) are the relative-value indicators this evidence justifies. The implied moves are not realized on average, so high-rolling-yield bonds tend to keep their advantage.

## Key Takeaways
1. Treat forward-implied rate changes as break-evens: expected change + BRP/(duration at horizon).
2. The break-even move of a constant-maturity rate = carry cushion (spread/duration) + rolldown.
3. In a concave curve, flatteners pay negative carry and negative rolldown. Size them against the forward-implied flattening, not against zero.
4. Empirically the current curve is the better forecast beyond one year (PF > 1). Forwards overstate rate rises and flattening.
5. Survey-minus-forward gaps give direct estimates of the bond risk premium (about 53bp/yr for bills, larger for the long bond) and of the price of convexity.
6. The failure of PEH is good news for active managers: yield-seeking and rolling-yield-seeking strategies have positive expected value.

## Connects To
- **ch01**: notation, bootstrapping, and the three-component decomposition.
- **ch03**: the size of the long-run average BRP by duration.
- **ch04**: time-varying BRP and predictors beyond curve steepness.
- **ch05**: LEH vs UEH and the convexity bias magnitude.
- **ch06**: the four-component expected return and break-even analysis of barbell/bullet trades.
- **`tuckman-fixed-income` ch02**: forward-rate algebra.
- **`tuckman-fixed-income` ch03**: carry and roll-down in P&L attribution.
- **`tuckman-fixed-income` ch08**: expectations, risk premium and convexity in the short-rate framework.
- **`cfa-fixed-income` ch07**: expectations theories and riding the yield curve.
