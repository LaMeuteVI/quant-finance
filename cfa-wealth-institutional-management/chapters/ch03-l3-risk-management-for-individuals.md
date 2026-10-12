# Chapter 3: Risk Management for Individuals
> **Source**: CFA Program Curriculum 2023, Level III, Reading 23 · Portfolio Management (Private Wealth) | David M. Blanchett, David M. Cordell, Michael S. Finke, Thomas M. Idzorek

## Core Idea
An individual's real balance sheet is dominated by assets that never appear on a brokerage statement: human capital (PV of future labor income) and pension claims. Risk management for a household means (1) valuing these on an economic (holistic) balance sheet, (2) hedging the idiosyncratic risks that threaten them (death, disability, longevity, health, liability, property) with insurance, annuities or retention, and (3) setting the financial portfolio as a "completion" portfolio that offsets the risk of everything else the household owns.

## Learning Outcomes Covered
- compare human capital vs financial capital; relate both to economic net worth
- describe the seven financial stages of life
- build and interpret an economic (holistic) balance sheet
- discuss earnings, premature death, longevity, property, liability and health risks
- describe insurance types (life, disability, property, health, liability, long-term care)
- explain life insurance elements and pricing (mortality, discount rate, loading)
- explain annuities; compare fixed vs variable; assess appropriateness (mortality credits)
- analyze an insurance program (human life value vs needs analysis)
- adjust asset allocation for human-capital risk; recommend strategies for an investor profile

## Frameworks Introduced
- **Four-step individual risk management process**: (1) specify the objective (maximize household welfare, i.e. stable spending, via a balance of risk and safety); (2) identify risks; (3) evaluate and select methods; (4) monitor and adjust.
  - When to use: every client review; re-run annually and after any life event (birth, marriage, inheritance, job change, relocation, divorce, death).
  - How: list exposures by type, size each as a potential loss to human and/or financial capital, pick a technique per risk, set a review calendar.
- **Four risk techniques and the frequency/severity grid**: avoidance, reduction (loss prevention lowers probability; loss reduction lowers severity), transfer (insurance, annuities, leases, incorporation), retention (self-insurance, deductibles).
  - When to use: choosing how to treat each exposure.
  - How: high severity / high frequency = avoid; high severity / low frequency = transfer; low severity / high frequency = reduce; low severity / low frequency = retain. Retain risks below the household's retention limit; use deductibles to set the optimal retention.
  - Why it works: insurance carries a load, so it is only worth paying for risks that threaten spending. More risk-tolerant, wealthier households retain more.
- **Economic (holistic) balance sheet**: Assets = financial capital + human capital + PV of pension; Liabilities = debts + PV of lifetime consumption needs + PV of bequests; Economic net worth = assets - liabilities (can be a surplus or a shortfall).
  - When to use: sizing risk exposure and consumption/bequest goals for any client, especially young (human capital dominant) or pension-rich.
  - How: put each item at PV with a discount rate matched to its risk (nominal vs real consistency).
  - Failure mode: it is static; it ignores volatility, correlations among components and liquidity (human capital cannot be borrowed against easily).
- **Human life value vs needs analysis (life insurance sizing)**: HLV replaces the PV of the insured's net contribution to the family; needs analysis sums family needs and subtracts capital available.
  - When to use: compute both, treat as a range; pick by fit to the family's situation and insurer premium breakpoints.
- **Total-wealth asset allocation**: financial portfolio = (target total-wealth equity - equity-like part of human capital and pension) / financial capital.
  - When to use: translating a risk-tolerance-based target mix on total wealth into the financial portfolio's mix.
- **Retirement income efficient frontier**: plots wealth (vertical) against probability of having enough money for life (horizontal); higher annuity allocation = higher certainty, lower expected wealth.

## Key Concepts
- **Human capital**: mortality-weighted PV of expected future labor income; usually bond-like, the largest asset of young households.
- **Financial capital**: all tangible and intangible assets outside human capital, personal assets, investment assets and vested pensions; accrued DB and government pensions are classified here by this reading.
- **Personal vs investment assets**: personal assets are consumed (cars, furniture); investment assets are held for growth; a home and collectibles are "mixed" assets.
- **Economic net worth**: traditional net worth plus human capital and pension PV, minus PV of consumption and bequest goals.
- **Mortality-weighted NPV (mNPV)**: PV of future benefits weighted by survival probability; used for vested DB pensions.
- **Earnings risk**: loss of earning power from unemployment, underemployment or health; raises the discount rate and/or lowers expected earnings in the human capital model.
- **Premature death risk**: death before the household's needs are funded; eliminates human capital and adds death, transition and estate costs.
- **Longevity risk**: outliving financial resources; partly mitigated by working longer (more human capital) or by annuities.
- **Direct vs indirect loss (property)**: direct is the property value lost; indirect is consequential cost (temporary housing, lost rent).
- **Liability risk**: legal responsibility for injury or damage; can exceed total wealth, with wage garnishment possible.
- **Insurable interest**: the policy owner must suffer a loss if the insured dies (spouse, key executive); blocks wagering on strangers.
- **Adverse selection**: high-risk people apply disproportionately; countered by underwriting.
- **Moral hazard (disability)**: benefits near full income reduce the incentive to return to work; hence 60-80% replacement caps.
- **Mortality credit**: the gain survivors in an annuity pool receive from the capital of members who died early; the source of the annuity's extra income vs self-insuring.
- **Load**: the amount added to the net premium for expenses and profit.
- **Surrender cost index / net payment cost index**: per-$1,000-per-year costs of a whole life policy at a given horizon and discount rate; lower is better.

## Formulas & Reference Tables
- Human capital (simple): `HC₀ = Σₜ₌₁ᴺ wₜ / (1+r)ᵗ`
- Human capital (full): `HC₀ = Σₜ₌₁ᴺ p(sₜ)·wₜ₋₁(1+gₜ) / (1 + r_f + y)ᵗ`; `p(sₜ)` survival probability to t, `wₜ` income, `g` nominal wage growth, `r_f` nominal risk-free rate, `y` occupational risk premium, `N` working years. Lower r_f or y raises HC; riskier/more cyclical occupation means higher y (and lower HC).
- Vested DB pension: `mNPV₀ = Σₜ₌₁ᴺ p(sₜ)·bₜ / (1+r)ᵗ`. Discount at a rate reflecting funding status, sponsor credit and guarantees (e.g. UK Pension Protection Fund lowers it). Government pension is bond-like, often CPI-indexed (TIPS-like).
- Equity in a leveraged home: with 20% down, equity moves 5x the house value change.
- Net premium (one-year term): `Net premium = q × Benefit / (1 + i)`, `q` mortality probability, `i` insurer's portfolio return. Gross premium = net premium + load (expenses + profit).
- Policy reserve: `PV(future benefits) - PV(future net premiums)`; rises toward the endowment value.
- Net payment cost index (NPCI), per $1,000/yr: FV(premiums, annuity due) - FV(dividends, ordinary annuity) = N-year cost; convert to an annuity-due payment of equal FV; divide by thousands of face value.
- Surrender cost index (SCI): same, but also subtract the year-N cash value before annualizing.
- Human life value: `HLV = PV of growing annuity due of [(pre-tax pay × (1-t_work) - expenses attributable to insured + non-taxable benefits) / (1 - t_replacement)]`; use adjusted rate `i = (1+discount)/(1+growth) - 1` with level-payment annuity-due keystrokes.
- Needs analysis: `Insurance need = cash needs + PV(survivor and children living costs) - PV(survivor income) - capital available`.
- Total-wealth allocation: `FC equity % = (TW × target equity % - HC × HC equity %) / FC`.
- Annuity income yield: `annual payout / purchase price`.
- Inflation erosion: at 3% inflation, a nominal payment halves in real terms in about 23-24 years (ln2/ln1.03 = 23.4).

| Life stage (approx. age) | Human capital | Key risks / priorities |
|---|---|---|
| Education | being built | little saving; insure only if dependents |
| Early career (to mid-30s) | very large | death/disability hedge most valuable; housing, kids |
| Career development (35-50) | large | retirement saving accelerates; education funding |
| Peak accumulation (51-60) | declining | max earnings; start de-risking; tax; job-loss risk bites |
| Pre-retirement | small | restructure to lower volatility; distribution tax planning |
| Early retirement (first ~10 yrs) | ~0 | active years; still needs growth (20+ year horizon) |
| Late retirement | 0 | longevity, long-term care, cognitive decline |

| Product | Protects | Key terms |
|---|---|---|
| Term life | death over a set term | cheaper; level vs annually renewing premiums |
| Whole life | death, lifetime | fixed premium, cash value, participating or not, non-forfeiture options |
| Universal life | death, lifetime | flexible premium and investments |
| Disability income | earnings | "own occupation" definition best; benefit 60-80% of income; elimination period (~90 days); non-cancelable and guaranteed renewable |
| Homeowner/auto | property | replacement cost vs actual cash value; deductible; ~80% coinsurance rule |
| Umbrella | liability above base limits | cheap, pays only past primary limits |
| Long-term care | custodial care | inflation rider; adds to longevity protection |

| Annuity type | Features |
|---|---|
| Immediate fixed (SPIA) | irrevocable lump sum for guaranteed income; most common; highest certainty |
| Immediate variable | payments vary with portfolio; floor rider possible |
| Deferred fixed | accumulates then annuitizes; most are eventually annuitized |
| Deferred variable | mutual-fund-like, fees higher; few annuitize; income needs GMWB-type rider |
| ALDA (longevity insurance) | payments start at ~80-85; cheapest per dollar of late-life income; no cash-out |
| Payout methods | life only (highest payout), period certain (usually 10 yrs), refund, joint life (lower payout, survivor 50-100%) |

Payout behavior: higher with age, higher for men than women, lower for joint, lower with period certain (60-year-old male 6.28% life-only vs 6.15% with 10-year certain; at 90, 20.10% vs 10.66%).

## Mental Models
- **Human capital is a bond; the financial portfolio is the completion portfolio.** More human capital (or pension) means a riskier financial portfolio is acceptable; as human capital depletes, shift to bonds (the logic behind target-date funds).
- **Correlate-check the job.** The financial portfolio should be uncorrelated or negatively correlated with the earner's income: sell employer stock, underweight the employer's sector (real-estate worker underweights real estate, oil worker overweights transport).
- **Insurance is for catastrophes, not for convenience.** Retain small frequent risks, transfer large rare ones; more wealth and liquidity means more retention. Pseudo-insurance (extended warranties) is expensive.
- **Annuity = longevity insurance with a price.** Expected value is not positive by design; you buy certainty and mortality credits and give up bequest wealth. Demand rises with longer life expectancy, risk aversion, low other guaranteed income, weak bequest motive.
- **Two-spouse diversification.** Dual earners with uncorrelated jobs lower household income risk; a low-mobility or employer-specific skill set lowers HC value and raises its risk.

## Worked Example
**Human capital (verified).** John, 60, retires in 5 years. Wage 50,000 growing 2%, risk-free 4%, occupational adjustment 3%, so discount rate 7%. Survival 99, 98, 98, 97, 96%.
Steps: wage_t = 50,000 × 1.02ᵗ; PV = wage_t/1.07ᵗ; multiply by survival.
Result: HC = 211,997. Rerun with 0% growth and discount 4% (2%+2%): HC = 217,371, higher because the lower discount rate more than offsets zero growth. Interpretation: HC is highly sensitive to r_f and y.

**Needs analysis (Perrier case, recomputed).** Jacques, 40, earns 100,000. HLV: 100,000 less 30% tax = 70,000; less 20,000 own expenses = 50,000; plus 15,000 non-taxable benefits = 65,000; gross up at 20% replacement tax: 65,000/0.8 = 81,250. Growth 3%, discount 5%: `i = 1.05/1.03 - 1 = 1.94%`; annuity due, n = 20: HLV ≈ 1.362 m (1,361,996 unrounded). Subtract existing 250,000 cover: about 1.11 m extra.
Needs: cash needs 445,000 (final 10k, taxes 5k, mortgage 190k, other debt 10k, education 200k, emergency 30k). Capital needs: Marion's living costs 60,000 × 52 yrs = 1.99 m; children 124k + 139k; transition 20k; less Marion's earnings 184k + 399k = 1,692k (source; recomputed within rounding). Total 2,137k; capital available 645k (savings 30k, vested retirement 200k, insurance 250k, rental house 165k). Need ≈ 1.49 m. Range 1.11-1.49 m; pick by context and insurer price breakpoints (e.g. 250k/500k/1m); use 20-year level term, keep the whole life policy, name Marion as beneficiary rather than the estate.

**Total-wealth allocation (verified).** Target 45% equity, HC 30% equity-like: George (HC 500k, FC 150k) = 95%; John (800k, 300k) = 85%; Sam (150k, 150k) = 60%. The larger the HC relative to FC, the higher the financial equity weight.

**Why high HC permits more risk (verified).** 40% loss on a 500k portfolio = 200k. Spread over 40 years: -13.2% of annual spending (38k budget) vs -5.7% (88k budget).

**Net payment cost index (verified).** Whole life 100k face, premium 2,000 (start of year), dividend 500 (end of year), 20 years at 5%: FV premiums 69,439 - FV dividends 16,533 = 52,906; annuity-due payment 1,524; /100 = 15.24 per $1,000. SCI also subtracts the 22,500 cash value: 30,406 gives 8.76.

## Anti-patterns
- **Optimizing only the liquid portfolio**: ignores human capital and pensions that drive total risk.
- **Holding employer stock (or own-industry assets) when income is correlated**: concentrates human and financial capital in one risk factor.
- **Naming the estate as life insurance beneficiary**: slower payout, possible greater tax; use named beneficiaries, custodian or trust for minors.
- **Underinsuring property**: below ~80% of replacement cost, claims are scaled down; the owner silently retains the excess.
- **Delaying annuitization to time rates**: forgoes mortality credits and exposes to longevity-improvement risk.
- **Buying annually renewable term as a "loss leader" then switching**: a health event can make you uninsurable.
- **Comparing whole life policies on first-year premium**: use cost indexes, which consider cash value and time value.
- **Using the wrong discount rate for human capital**: bond-like for tenure/government, above the equity premium for volatile cyclical income.

## Exam Focus & Traps
- Human capital falls when r_f or y rises; it rises when growth or survival rises. A lower risk-free rate raises HC.
- **Vested** pension = financial capital; **unvested** pension (contingent on future work) = human capital. Government accrued benefits are financial capital in this reading.
- Traditional balance sheet excludes future earnings; the economic balance sheet includes them and also lists consumption and bequests as liabilities.
- Economic net worth is lower than traditional net worth when PV(consumption + bequests) exceeds PV(HC + unvested pension).
- Adjusted rate `(1+d)/(1+g) - 1` uses an annuity-due setting when the first payment is immediate; discount the PV back at the unadjusted rate when there is a gap before payments start (Marion, 10 years).
- NPCI assumes death at horizon end (ignores cash value); SCI assumes surrender (subtracts cash value). Premiums = annuity due; dividends = ordinary annuity.
- Disability: "own occupation" is best for specialists; the 60-80% cap addresses moral hazard.
- Annuity payout rises with age; joint, female and period-certain features reduce it; ALDA is the cheapest late-life income.
- Non-forfeiture options: cash surrender, reduced paid-up, extended term.
- HMO fits "avoid paying for minor visits"; PPO = network discount.
- Policy "owner, insured, beneficiary, insurer" are four distinct roles; premium payer is the owner.
- Source inconsistency: the text first cites about 1.25 m for the needs analysis method but the exhibit computes 1,492,478; use the exhibit. Also, **⚠ Correction**: Jacques's coverage is 200,000 whole life + 50,000 term = 250,000 (used in the calculation).

## Key Takeaways
1. Value human capital by discounting mortality-weighted expected wages at a risk-adjusted rate; treat it as bond-like unless income is cyclical.
2. Build the economic balance sheet, including consumption and bequests as liabilities, before setting allocation.
3. Financial equity weight = (target total equity - equity share of HC and pension) / FC; young and pension-rich households can hold more equity.
4. Hedge idiosyncratic human-capital risk (death, disability) with cheap term and own-occupation disability cover; retain small risks with deductibles.
5. Size life insurance with both human life value and needs analysis, then choose within the range.
6. Annuitize partially for longevity risk; prefer immediate fixed for certainty, ALDA for cheap tail protection, variable for upside at higher fees and inflation protection.
7. Underweight securities correlated with the earner's job and sell employer stock.
8. Review the plan annually and at every life event.

## Connects To
- **ch01**: private wealth overview (client risk profile, life-cycle goals feed this framework).
- **ch02**: private wealth topics (concentrated positions, estate, tax) extend the hedging and bequest ideas.
- **ch06**: case study applying this chapter's human capital, insurance sizing and goals-based allocation to one family from age 28 to 65.
- **ch05, ch07**: institutional counterpart (liquidity, enterprise risk management) of the same identify-measure-manage-monitor discipline.
- **`cfa-asset-allocation-cme` ch07**: principles of asset allocation (liability-relative and goals-based allocation, total-wealth thinking).
- **`cfa-asset-allocation-cme` ch08**: real-world constraints (taxes, liquidity) on asset allocation.
- **`cfa-fixed-income` ch13**: liability-driven strategies mirror matching consumption liabilities with bond-like assets.
