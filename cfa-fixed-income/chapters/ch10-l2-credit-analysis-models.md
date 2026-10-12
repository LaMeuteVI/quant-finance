# Chapter 10: Credit Analysis Models
> **Source**: CFA Program Curriculum 2022, Level II, Reading 31 · Fixed Income | James F. Adams, PhD, CFA, and Donald J. Smith, PhD

## Core Idea
Credit risk has three inputs: the **expected exposure** at each possible default date, the **loss given default** (exposure × (1 − recovery rate)) and the **risk-neutral probability of default**. Discount the expected loss of each date at risk-free rates and sum: that is the **credit valuation adjustment (CVA)**. Fair value = value assuming no default (VND) − CVA. The CVA and the credit spread express the same compensation, one as a Date-0 present value and the other as an annual rate. Put the calculation on a calibrated binomial tree and you can price fixed-rate bonds and floaters, back out implied default probabilities from spreads, and explain why spreads move.

## Learning Outcomes Covered
- Explain expected exposure, LGD, probability of default (POD) and CVA.
- Explain credit scores (retail) and credit ratings (wholesale).
- Calculate a bond's expected return given rating transition (migration) probabilities.
- Explain structural vs reduced-form credit models: assumptions, strengths, weaknesses.
- Calculate a risky bond's value and credit spread from credit-risk parameters (flat curve, then arbitrage-free tree).
- Interpret changes in a credit spread (POD vs recovery vs exposure).
- Explain the determinants of the term structure of credit spreads and interpret its shape.
- Compare credit analysis of securitized debt with credit analysis of corporate debt.

## Frameworks Introduced
- **CVA table (VND − CVA framework)**: fair value = VND − Σₜ (LGDₜ × PODₜ × DFₜ).
  - When to use: to value any risky bond or floater from assumed credit parameters, to decide whether a market price is rich or cheap, or to back out the market-implied hazard rate.
  - How:
    1. **Exposure** for each date t. On a flat curve with no volatility, this is the PV at t of the remaining cash flows at the risk-free rate, plus the coupon paid at t. On a tree, it is the probability-weighted node values at t plus the coupon at t.
    2. **Recovery** = RR × exposure. **LGD** = exposure − recovery = exposure × (1 − RR).
    3. **POD** for each date from a hazard rate h (a conditional default probability). POD₁ = h. PODₜ = h × POSₜ₋₁. POSₜ = POSₜ₋₁ − PODₜ = (1 − h)ᵗ when h is constant.
    4. **Expected loss** = LGD × POD. **PV of expected loss** = expected loss × risk-free DFₜ (DF from bootstrapped government spot rates).
    5. **CVA** = Σ PV of expected loss. **Fair value** = VND − CVA. Solve the YTM on the fair value. **Credit spread** = YTM − benchmark yield.
  - Why it works: under risk-neutral valuation, expected cash flows computed with risk-neutral probabilities are discounted at the risk-free rate. The CVA isolates the PV cost of default.
  - Failure mode: the method assumes default only on coupon dates, instantaneous recovery, and a recovery rate that applies to interest as well as principal. It also treats the whole spread as credit, whereas real spreads also carry liquidity and tax components. Implied PODs are therefore overstated as "credit" measures.
- **Risk-neutral vs actual (historical) default probability**:
  - How: solve P* from `Price = [CF_ND × (1 − P*) + CF_D × P*]/(1 + r_f)`.
  - Rule: P* > actual POD for two reasons. (1) P* embeds a **default risk premium** for uncertainty about the *timing* of default. (2) The observed spread also includes **liquidity and tax** effects.
- **Credit-migration expected return**:
  - `E[R] ≈ YTM + Σᵢ pᵢ × (−ModDur_end × Δspreadᵢ)`, using the transition-matrix row for the current rating, with ModDur the duration at the end of the horizon.
  - Result: migration almost always *reduces* expected return. Transition probabilities are skewed toward downgrades, and downgrade spread jumps are much larger than upgrade spread tightening (the spread has a floor near zero).
  - If the bond is below investment grade, add the default transition as well.
- **Structural (company-value) model** (Black–Scholes 1973; Merton 1974):
  - Default happens when asset value A(T) falls below the default barrier K (face value of debt). **Equity** = long call on the assets with strike K. **Debt** = assets − call = risk-free K − put.
  - POD rises with asset volatility, with the horizon T and with leverage.
  - Used internally by banks, rating agencies and Moody's KMV, which calibrates asset volatility from equity prices.
- **Reduced-form (intensity-based, stochastic default rate) model** (Jarrow–Turnbull 1995; Duffie–Singleton 1999):
  - Default is **exogenous**: a Poisson arrival with **default intensity** (the probability of default over the next small time increment).
  - The intensity is regressed on company variables (leverage, NI/assets, cash/assets) and macro variables (unemployment, GDP growth, equity volatility).
  - The model explains **when**, not **why**. Use it to value risky debt and credit derivatives from market data.
- **Arbitrage-free floater valuation and discount margin (DM)**:
  - Value the floater on the tree with coupons paid **in arrears**: the coupon (index at t−1 + quoted margin) × 100 is set at the start of the period and paid at t.
  - Compute the CVA as usual, then find the DM by trial and error: add DM to every tree rate in the discounting until the Date-0 value = VND − CVA.
  - Price < par ⇔ DM > quoted margin.
- **Securitized-debt credit analysis approach** (Scope Ratings, driven by granularity, homogeneity and risk horizon):
  - Short-term, granular, homogeneous pool (credit cards, ABCP, trade receivables) → **book** (statistics-based) approach.
  - Medium-term, granular, homogeneous but dynamic pool (auto, consumer ABS) → **portfolio** approach.
  - Non-granular, heterogeneous pool (CMBS, CRE loans, leveraged-loan CLOs, project-finance CLOs) → **loan-by-loan** approach.
  - RMBS and SME ABS → loan-by-loan or portfolio.
  - Credit-linked notes → pass-through / asset by asset.

## Key Concepts
- **Credit spread (G-spread)**: YTM on the corporate bond − YTM on a government bond of the same maturity. It compensates for expected loss, plus liquidity and tax differences.
- **Default risk vs credit risk**: default risk is the likelihood of default. Credit risk also covers the loss if default happens. A well-collateralized loan can have high default risk but low credit risk.
- **Expected exposure**: the amount at risk at a default date, before recovery. It includes the coupon due on that date.
- **Recovery rate / loss severity**: the recovered fraction of exposure / 1 − RR. The market baseline is 40% for senior unsecured.
- **Hazard rate**: the conditional POD for a period, given survival to its start.
- **Probability of survival (POS)**: the cumulative probability of no default up to date t. Cumulative POD = 1 − POSₜ.
- **CVA**: the PV of expected default losses, computed with risk-neutral PODs and risk-free DFs.
- **VND**: the value of the bond as if default-free, discounted on the benchmark curve or tree.
- **Notching**: the agency adjustment of an issue rating relative to the issuer (senior unsecured) rating to reflect priority and subordination. It is why ratings are "credit" ratings, not "default" ratings.
- **Transition matrix**: the one-year probabilities of moving between rating grades, including to D.
- **FICO score**: a US retail score from 300 to 850. Weights: payment history 35%, debt burden 30%, length of history 15%, types of credit 10%, recent hard inquiries 10%. It excludes age, race, sex, salary, occupation, address and marital status. Soft inquiries (self-checks) have no impact.
- **XVA**: the family of valuation adjustments applied to an OIS-discounted value: CVA, plus funding (FVA), liquidity (LVA) and tax (TVA) adjustments.
- **Discount margin (DM)**: the floater's analogue of the credit spread. It is the margin over the index that reprices the note to its (fair or market) price, assuming no default.
- **Granularity / homogeneity**: the number of obligors in a pool / how similar they are. Together they drive the securitized-debt credit approach.
- **True sale / bankruptcy remoteness**: the legal separation of SPE assets from the originator's estate.
- **Excess spread**: pool yield above expected loss and note coupons. It is the first-loss cushion in consumer ABS.
- **Covered bond**: a senior bank debt with **dual recourse** to the issuer and to a dynamic cover pool (mortgages or public-sector debt). Non-performing and prepaid assets must be replaced. Typically rated several notches above the issuer.
- **Hard-bullet / soft-bullet / conditional pass-through covered bond**: a missed payment triggers default and acceleration / default is delayed to an extended maturity (≈ up to 1 year) / the bond converts to pass-through after the original maturity.

## Formulas & Reference Tables
- One-period risk-neutral POD: `P₀ = [CF × (1 − P*) + RR·CF × P*]/(1 + r)`, so `P* = [CF − P₀(1 + r)]/[CF × (1 − RR)]`.
- LGD: `LGDₜ = Exposureₜ × (1 − RR)`.
- Hazard-rate PODs: `POD₁ = h`, `PODₜ = h × (1 − h)ᵗ⁻¹`, `POSₜ = (1 − h)ᵗ`, `Cumulative POD_T = 1 − (1 − h)ᵀ = Σ PODₜ`.
  - With time-varying hazard hₜ: `PODₜ = hₜ × POSₜ₋₁`.
- CVA: `CVA = Σₜ LGDₜ × PODₜ × DFₜ`, with `DFₜ = 1/(1 + zₜ)ᵗ` (risk-free spot rates).
- Fair value and spread: `Fair value = VND − CVA`. `Credit spread = YTM(Fair value) − y_benchmark`.
- Rule-of-thumb spread: `Spread ≈ h × (1 − RR)` (annual POD × loss severity). Example: 1.25% × 0.6 = 0.75% vs 0.77% exact.
- Expected exposure on a tree (fixed coupon c):
  - `EEₜ = Σⱼ π_{t,j} × V_{t,j} + c`, with π the node probabilities (binomial: C(t, j)/2ᵗ) and V the ex-coupon node values.
  - At maturity, EE_T = 100 + c.
- Expected exposure on a tree (floater): `EEₜ = Σⱼ π_{t,j} V_{t,j} + Σₖ π_{t−1,k} × 100 × (r_{t−1,k} + QM)`.
  - The coupon uses the **previous date's** node probabilities because the rate is set in advance.
- Node valuation (backward induction): `V_{t,j} = [0.5 V_{t+1,up} + 0.5 V_{t+1,down} + CF_{t+1}]/(1 + r_{t,j} (+ DM))`.
- Migration price change: `%ΔP ≈ −ModDur × (s_new − s_old)`.
- Structural model (debt zero-coupon with face K at T):
  - `D(T) + E(T) = A(T)`.
  - `E(T) = max[A(T) − K, 0]` (long call).
  - `D(T) = A(T) − max[A(T) − K, 0] = K − max[K − A(T), 0]` (risk-free debt minus a put written to shareholders; the put is the value of limited liability).

**Structural vs reduced-form models**

| | Structural (company-value) | Reduced-form (intensity-based) |
|---|---|---|
| Default | Endogenous: A(T) < K | Exogenous random event (Poisson) |
| Explains | **Why** default happens | **When** (default time) |
| Inputs | Asset value, asset volatility, default barrier (liabilities) | Observable data: company ratios + macro variables (regression) |
| Strength | Economic insight; option framing of debt and equity | Observable inputs; reflects the business cycle; fits market prices |
| Weakness | Assets do not trade; hidden debt (Enron, Lehman) makes the barrier hard to measure | No economic cause; treats default as a "surprise" although downgrades usually precede it |
| Best user | Internal risk management, banks' credit measures, rating agencies | Valuing risky debt and credit derivatives |

**Representative one-year transition matrix and 10-year spreads (%)**

| From/To | AAA | AA | A | BBB | BB | B | CCC–C | D |
|---|---|---|---|---|---|---|---|---|
| AAA | 90.00 | 9.00 | 0.60 | 0.15 | 0.10 | 0.10 | 0.05 | 0.00 |
| AA | 1.50 | 88.00 | 9.50 | 0.75 | 0.15 | 0.05 | 0.03 | 0.02 |
| A | 0.05 | 2.50 | 87.50 | 8.40 | 0.75 | 0.60 | 0.12 | 0.08 |
| BBB | 0.02 | 0.30 | 4.80 | 85.50 | 6.95 | 1.75 | 0.45 | 0.23 |
| BB | 0.01 | 0.06 | 0.30 | 7.75 | 79.50 | 8.75 | 2.38 | 1.25 |
| B | 0.00 | 0.05 | 0.15 | 1.40 | 9.15 | 76.60 | 8.45 | 4.20 |
| CCC–C | 0.00 | 0.01 | 0.12 | 0.87 | 1.65 | 18.50 | 49.25 | 29.60 |
| Spread | 0.60 | 0.90 | 1.10 | 1.50 | 3.40 | 6.50 | 9.50 | |

Migration drag, recomputed: A-rated with ModDur 7.2 → **−0.6342%**. AAA-rated with ModDur 7.3 → **−0.3249%** (≈ −32.5bp).

**Implied risk-neutral hazard rates** (5-year 3.50% bond, 10% volatility tree, RR = 40%):

| Rating | Spread | Annual POD | Cumulative 5-year POD |
|---|---|---|---|
| AAA | 0.60% | 1.01% | 4.95% |
| AA | 0.90% | 1.49% | 7.23% |
| A | 1.10% | 1.83% | 8.82% |
| BBB | 1.50% | 2.48% | 11.80% |
| BB | 3.40% | 5.64% | 25.19% |
| B | 6.50% | 10.97% | 44.07% |
| CCC–C | 9.50% | 16.50% | 59.41% |

These rates are far above historical AAA default experience (no AAA default since 1995) because they are *risk-neutral*: they embed the timing-risk premium, migration risk, and liquidity and tax spread.

## Mental Models
- **Two currencies for one risk**: the CVA (a PV per 100 of par today) and the spread (bp per year to maturity) are interchangeable views of the same compensation. Convert through the fair value and its YTM.
- **For a given price, PD and RR move together**: for a fixed market price and spread, a lower assumed recovery implies a lower implied POD (RR 40% → h = 1.25%; RR 30% → h = 1.0675%). Never quote an implied PD without its recovery assumption.
- **POD matters more than recovery**: doubling h (1.5% → 3%) widened the spread by 92bp. Halving RR (40% → 20%) widened it by only 31bp. Doubling h roughly doubles expected loss, whereas halving RR raises LGD only from 60% to 80% of exposure (+33%).
- **Volatility touches CVA, not VND**: a calibrated tree returns the same VND for option-free bonds at any volatility. Higher volatility slightly *lowers* expected exposure because lognormal rates spread asymmetrically (up moves are larger than down moves), which lowers the CVA marginally (3.5394 → 3.5390).
- **Distressed debt trades on price, not spread**: when default is near-certain, all maturities converge to the recovery value (with cross-default). The computed spread curve then becomes steeply inverted as an "optical" artifact, not a signal about maturity risk.

## Worked Example
**Rebuilt and verified CVA table on a 10% volatility binomial tree (5-year 3.50% annual bond, h = 1.25%, RR = 40%).**

Inputs:
- Government par curve: −0.25%, 0.75%, 1.50%, 2.25%, 2.75%.
- Bootstrapped DFs: 1.002506, 0.985093, 0.955848, 0.913225, 0.870016.
- One-year forwards: 1.7677%, 3.0596%, 4.6674%, 4.9664%.

One-year rate tree (node probabilities are binomial):

| Date | Rates (top → bottom) | Probabilities |
|---|---|---|
| 0 | −0.2500% | 1 |
| 1 | 1.9442, 1.5918 | ½ each |
| 2 | 3.7026, 3.0315, 2.4820 | ¼, ½, ¼ |
| 3 | 6.2197, 5.0922, 4.1692, 3.4134 | ⅛, ⅜, ⅜, ⅛ |
| 4 | 7.2918, 5.9700, 4.8878, 4.0018, 3.2764 | 1/16, ¼, ⅜, ¼, 1/16 |

Steps:
1. **VND by backward induction.** The Date-4 node values are 103.50/(1 + r): 96.4659, 97.6692, 98.6769, 99.5175, 100.2165. Rolling back gives Date 0 = **103.5450**. Check: Σ 3.5 × DFₜ + 100 × DF₅ = 103.5450, so the tree is correctly calibrated.
2. **Expected exposure.** Date 4: 0.0625 × 96.4659 + 0.25 × 97.6692 + 0.375 × 98.6769 + 0.25 × 99.5175 + 0.0625 × 100.2165 + 3.50 = **102.0931**.
3. **CVA table:**

| Date | Expected exposure | LGD (60%) | POD | DF | PV of expected loss |
|---|---|---|---|---|---|
| 1 | 103.2862 | 61.9717 | 1.2500% | 1.002506 | 0.7766 |
| 2 | 101.5481 | 60.9289 | 1.2344% | 0.985093 | 0.7409 |
| 3 | 101.0433 | 60.6260 | 1.2189% | 0.955848 | 0.7064 |
| 4 | 102.0931 | 61.2559 | 1.2037% | 0.913225 | 0.6734 |
| 5 | 103.5000 | 62.1000 | 1.1887% | 0.870016 | 0.6422 |
| Σ | | | 6.0957% | | **CVA = 3.5394** |

4. **Fair value** = 103.5450 − 3.5394 = **100.0056**. YTM = **3.4988%**. Spread over the 5-year par yield (2.75%) = **74.88bp**.

Interpretation: the analyst should buy if the market price is below 100.0056. Sensitivities, all recomputed:
- RR 30% with h = 1.83% → CVA 5.9781, fair value 97.5670, YTM 4.05%, spread 1.30%. This is the subordinated-notching case: about 20bp wider than the 1.10% of an A-rated senior bond.
- At 20% volatility → CVA 3.5390, fair value 100.0060.

**Flat-curve cross-check (5-year zero, government curve flat at 3%, h = 1.25%, RR = 40%).**
- Exposures are 100/1.03⁵⁻ᵗ: 88.8487 … 100.
- CVA = **3.1549**. VND = 86.2609. Fair value = **83.1060**. YTM = 3.7704%. **Spread = 77bp** (rule of thumb: 1.25% × 0.6 = 75bp).
- Realized IRR if default occurs on Dates 1 to 5: −57.24%, −33.63%, −23.16%, −17.32%, −13.61%. With no default (POS = 93.90%): +3.77%.
- Timing uncertainty is itself priced (the default risk premium).

## Anti-patterns
- **Discounting expected cash flows at the bond's own YTM**: risk-neutral expected values must be discounted at *risk-free* rates. Using historical PODs with risk-free discounting overprices the bond (100.365 vs an observed 100 in the one-year example).
- **Using unconditional hazard as each year's POD**: POD for Date t is h × POSₜ₋₁, not h. Summing h × T overstates cumulative default.
- **Forgetting the coupon in exposure**: exposure at a coupon date includes the coupon due. Only the final date is 100 + c.
- **Reading implied PODs as real-world forecasts**: they are risk-neutral and include liquidity and tax components.
- **Using the par benchmark yield when asked for a spread over a same-coupon government bond**: the two spreads differ. In the Level II problem set: 108bp over the theoretical 6% government bond vs 101bp over the 4-year par bond.
- **Building a credit curve from mixed securities**: use only senior unsecured, option-free issues. Exclude callables, secured or lien issues and special provisions. Interpolate benchmarks or use the swap curve for off-the-run maturities.
- **Applying a portfolio/statistical approach to a lumpy CMBS or CLO pool**: non-granular, heterogeneous pools need loan-by-loan analysis.

## Exam Focus & Traps
- **Ranking credit risk = ranking expected loss (LGD × POD)**, not POD alone. Example: bond B (LGD 63, POD 0.90%, EL 0.567) is riskier than C (62, 0.80%, 0.496), which is riskier than A (64, 0.75%, 0.480). Price is needed before recommending a trade.
- The **POD column sums to the cumulative POD**, and cumulative POD + final POS = 100%.
- **A change in h does not change the tree, the VND, the exposures, the LGDs or the DFs.** Only the PODs and the CVA change. Recovery changes only the LGD.
- **Floater exposure**: bond value uses Date-t probabilities, the coupon uses Date-(t−1) probabilities. A floater paying index flat is worth 100 at every node. A positive quoted margin puts it above par.
- **The DM is added to the discount rates only, not to the coupon rates.** DM > QM ⇔ price < par.
- **Structural model signs**: equity = long call on the assets. Debt = assets − call = K − put. The shareholders hold the put, which is the value of limited liability.
- **Reduced-form "tell"**: regressions on leverage, ROA and macro variables using public data. **Structural "tell"**: option pricing, equity volatility, default barrier, "inside" information.
- **Migration expected return**: use ModDur at the *end* of the horizon, the current rating's row, and a sign of −ModDur × Δs. Example (BBB, ModDur 7.54, YTM 5.50%): drag −1.767%, E[R] = 3.73%.
- **Term structure of credit spreads**:
  - High IG: flat or slightly upward (spreads can only migrate one way from near zero).
  - HY: steeper, and inverted near distress.
  - Spreads are **countercyclical**: strong growth brings higher benchmark yields and tighter spreads.
  - Liquidity: new or recent issues drive the curve.
  - Micro: higher equity volatility raises implied PD and steepens the curve.
  - Upward slope → high-quality issuer (low leverage, strong cash flow, high margin, stable industry).
  - Inverted → HY cyclical at the trough, or post-LBO deleveraging expected.
- **Trade from a curve view**: if you think near-term default risk is overpriced and declines over time, sell short-dated CDS protection and buy long-dated protection.
- **Rating agencies move incrementally**: an improved credit view on a BBB → "watch positive / positive outlook", not a jump to AAA.

## Key Takeaways
1. Build every credit valuation as exposure → LGD → hazard-based POD → risk-free discounting → CVA. Fair value = VND − CVA.
2. Risk-neutral PODs exceed historical ones (timing premium, liquidity, tax). Use them for pricing, not for default forecasting.
3. POD and recovery are jointly identified only through the price. For a given spread they are positively related, and a spread moves more for POD shocks than for comparable recovery shocks.
4. A calibrated tree extends the CVA to volatile rates and floaters. Volatility changes the CVA slightly through asymmetric lognormal exposure, but never the VND of option-free bonds.
5. Migration risk lowers expected return even without default: subtract Σ p × ModDur × Δs from the YTM.
6. Pick structural models for insight and internal risk, reduced-form models for valuation and credit derivatives.
7. Read credit curves by quality, cycle, liquidity and issuer fundamentals. Near default, the curve inverts because prices converge to recovery.
8. For securitized debt, let granularity, homogeneity and horizon choose book, portfolio or loan-by-loan analysis. Also analyse the servicer, true sale and credit enhancement (overcollateralization, tranching, excess spread, triggers).

## Connects To
- **ch06**: Level I fundamentals of credit analysis (four Cs, ratings, recovery and priority of claims) behind these parameters.
- **ch07**: the term structure, spot and forward rates used for bootstrapping DFs.
- **ch08**: the arbitrage-free binomial tree calibration reused here for VND and expected exposure.
- **ch09**: embedded options, OAS, and why volatility matters for option-embedded bonds.
- **ch11**: CDS pricing uses the same hazard-rate, LGD and PV-of-expected-loss machinery (protection leg).
- **ch15**: Level III credit strategies (spread duration, excess return, credit curve trades).
- **ch04**: ABS structures and credit enhancement.
- **`tuckman-fixed-income` ch19**: corporate bonds and CDS, hazard rates, the recovery conventions and the CDS–bond basis.
- **`hull-derivatives` ch24–25**: credit risk (Merton model, real-world vs risk-neutral PD, CVA/DVA) and credit derivatives.
- **`cfa-portfolio-management` ch13**: market and credit risk measurement in portfolios.
