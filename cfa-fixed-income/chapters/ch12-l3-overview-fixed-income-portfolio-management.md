# Chapter 12: Overview of Fixed-Income Portfolio Management
> **Source**: CFA Program Curriculum 2022, Level III, Reading 11 · Portfolio Management (Fixed Income) | Bernd Hanke, PhD, CFA, and Brian J. Henderson, PhD, CFA

## Core Idea
A fixed-income portfolio is built around a mandate (liability-based or total return), measured with portfolio-level duration, convexity and spread metrics, and judged on expected return decomposed into coupon, rolldown, rate view, spread view and currency, not on yield to maturity alone. Liquidity, leverage (futures, swaps, repo, securities lending, TRS) and taxes then decide how the exposure is implemented and what risks it carries.

## Learning Outcomes Covered
- Discuss the roles of fixed income in portfolios (diversification, cash flows, inflation hedging) and classify mandates
- Describe portfolio risk/return measures (duration, convexity, spread duration, DTS, dispersion) and correlation behavior
- Describe bond market liquidity across sub-sectors and its effect on pricing, construction and implementation
- Describe and interpret the model for fixed-income returns (expected return decomposition)
- Discuss leverage, methods to leverage (futures, swaps, repo, securities lending) and its risks
- Discuss taxable vs tax-exempt portfolio management

## Frameworks Introduced
- **Classification of fixed-income mandates**: Liability-based (ALM/LDI: cash flow matching, duration matching, derivatives overlay, contingent immunization) vs total return (pure indexing, enhanced indexing, active management).
  - When to use: to identify what a client or fund is really doing, and which risk measure governs.
  - How: liability-based = outflows known, goal is to minimize shortfall; total return = track or beat a market-weighted benchmark (for example Bloomberg Barclays Global Aggregate). Then classify total return by active return and active risk targets (table below).
  - Failure mode: judging by label. Identify the approach from evidence: a duration gap vs benchmark is the strongest signal of active management; near-identical duration/convexity/quality/country weights signal pure indexing; small deviations on all with matched duration signal enhanced indexing.
- **Model for Fixed-Income Returns (expected return decomposition)**: E(R) ≈ coupon income ± rolldown ± E(ΔPrice from benchmark-yield view) ± E(ΔPrice from spread view) ± E(currency gain/loss).
  - When to use: evaluating any strategy or portfolio ex ante; separating "carry" from "views".
  - How: (1) coupon/current yield; (2) reprice at horizon on the unchanged curve, so rolldown = %price change; (3) apply duration plus convexity to the expected yield change; (4) apply the same to the expected spread change; (5) add currency; (6) sum.
  - Why it works / failure mode: rolling yield (coupon + rolldown) is the "if nothing changes" return; the other lines are your views. It is approximate: duration and convexity only, reinvestment at YTM, no local richness/cheapness, no repo financing advantage, no taxes.
- **Leveraged portfolio return decomposition**: rP = rI + (VB/VE)(rI − rB).
  - When to use: sizing whether leverage pays.
  - How: compare the asset return to the borrowing cost; multiply the spread by the leverage ratio VB/VE.
  - Failure mode: leverage is symmetric in the formula, but forced liquidation and financing withdrawal make it asymmetric in practice.
- **Liquidity-yield trade-off in construction**: accept an illiquidity premium only if the horizon and liquidity needs allow it (buy-and-hold vs anticipated cash needs).
- **Tax-aware management (tax-loss harvesting)**: defer gains, realize losses early, control turnover, weigh gains vs income.

## Key Concepts
- **Diversification benefit**: lower correlation with equities, real estate, commodities; highest for government bonds, lowest for high yield and EM debt.
- **Excess return correlation**: correlation of returns net of the rate component (duration); used to compare credit-sensitive sectors cleanly.
- **Flight to quality**: in stress, government bond prices rise and risky assets fall, lowering government-equity and government-HY correlation while raising equity-HY correlation.
- **Dedicated portfolio**: bonds selected so cash flows match projected liability timing and size.
- **Liability-based mandate (ALM / LDI)**: managed to cover expected liability payments with projected inflows.
- **Total return mandate**: manage to track or outperform a market-weighted benchmark.
- **Tracking difference / tracking error (active risk)**: active return = portfolio minus benchmark; active risk = annualized standard deviation of active returns.
- **Spread duration**: approximate % price change for a 1% change in credit spread.
- **Duration times spread (DTS)**: spread duration × current spread, reflecting that spreads move proportionally, so higher-spread bonds react more in absolute terms.
- **Portfolio dispersion**: weighted variance of times to cash flows around duration; higher dispersion means higher convexity; used in immunization.
- **Money duration / PVBP (DV01)**: price change in currency per unit yield change / per 1 bp (per 100 par). BPV = money duration × 0.0001.
- **Relative value**: ranking securities by valuation, issuer fundamentals and technicals (supply/demand) over a set horizon.
- **On-the-run vs off-the-run**: newest vs older issue of the same sovereign; on-the-run has tighter bid-ask and lower yield.
- **Liquidity premium**: extra yield for holding an illiquid bond, dependent on issuer, size and maturity.
- **Matrix pricing**: estimate the price of a non-trading bond from liquid benchmark yields plus spreads of comparable bonds.
- **Rolling yield**: coupon income + rolldown return.
- **Haircut**: excess of collateral value over repo principal; also caps the borrower's leverage.
- **Rebate rate**: collateral earnings rate − securities lending rate; can go negative for hard-to-borrow bonds.
- **Fire sale**: forced liquidation below fair value, which can spiral.
- **Pass-through treatment**: realized fund capital gains taxed to investors in the year they arise (US); vs no pass-through (UK), where gains lift NAV and are taxed on sale.

## Formulas & Reference Tables
Portfolio measures (MV = portfolio market value, MVⱼ = value of bond j):
- `AvgModDur = Σⱼ (MVⱼ/MV) × ModDurⱼ`  (1)
- `AvgConvexity = Σⱼ (MVⱼ/MV) × Convexityⱼ`  (2)
- `EffDur = (PV₋ − PV₊) / (2 × ΔCurve × PV₀)`  (3)
- `EffCon = (PV₋ + PV₊ − 2×PV₀) / (ΔCurve² × PV₀)`  (4)  (PV₋/PV₊ = value after curve shifted down/up by ΔCurve)
- `Bond liquidity cost ≈ bid-ask spread (yield) × duration`, e.g. 10 bp × 15 = 1.50% of price
- Zero-coupon rules: Macaulay duration ∝ maturity (30y = 3 × 10y); convexity ≈ ∝ duration² (30y ≈ 9 × 10y). Zeros have the lowest convexity for a given duration; coupon bonds are more convex (cash flows more dispersed).
- Convexity scaling: some vendors report convexity/100. Check before use.

Return model:
- `Coupon income = annual coupon / current price`
- `Rolldown return = (P_end-of-horizon on unchanged curve − P_begin) / P_begin`  (5)
- `Rolling yield = coupon income + rolldown return`
- `E(ΔP | yield view) = (−ModDur × ΔYield) + [½ × Convexity × (ΔYield)²]`  (6)
- `E(ΔP | spread view) = (−ModDur × ΔSpread) + [½ × Convexity × (ΔSpread)²]`  (7)  (⚠ Correction: the reading prints (7) with ΔYield again; it must use ΔSpread, as in its own Example 4. Use effective duration/convexity for embedded options.)
- Currency: `R_DC = (1 + R_FC)(1 + R_FX) − 1`; portfolio: `R_DC = Σᵢ ωᵢ(1 + R_FC,i)(1 + R_FX,i) − 1`  (8)  (R_FX = % change of foreign currency vs domestic; Σωᵢ = 1)

Leverage and financing:
- `rP = [rI(VE + VB) − VB×rB] / VE = rI + (VB/VE)(rI − rB)`  (9)
- `Futures leverage = (Notional value − Margin) / Margin`  (10); notional = price × multiplier
- `Repo interest = principal × repo rate × days/360`; the repurchase price is principal plus interest
- `Rebate rate = collateral earnings rate − securities lending rate`

Total return approaches:

| | Pure indexing | Enhanced indexing | Active management |
|---|---|---|---|
| Objective | Match benchmark return and risk | Modest outperformance (about 20-30 bp) at low active risk (about 50 bp or less) | Higher outperformance (about 50 bp or more), higher active risk |
| Weights | Same or slight mismatches | Small deviations | Significant deviations |
| Risk factors | Match exactly | Primary ones (esp. duration) closely matched; minor sector/quality bets | Large deviations (esp. duration); some active styles instead run high idiosyncratic risk |
| Turnover | Similar to benchmark | Slightly higher | Considerably higher |
| Fees | Lowest | Middle | Highest |

Repo vs securities lending:

| | Repo | Securities lending |
|---|---|---|
| Nature | Sale plus repurchase; collateralized loan | Collateralized lending of bonds |
| Term | Typically overnight/term, in days | Open-ended, recallable at any time |
| Price of borrowing | Repo rate | Lending fee (or rebate rate when bonds are collateral) |
| Collateral cushion | Haircut (1-3% for high-quality government) | Over-collateralization (e.g., 102%) |
| Motive | Cash-driven (general collateral) or security-driven | Short sales; financing (fee then typically negative) |
| Settlement | Bilateral (DVP, security-driven) or tri-party (cash-driven) | Cash collateral (US) or high-quality bonds (elsewhere) |

Liquidity ranking (high to low): on-the-run high-quality sovereign > off-the-run sovereign > high-quality corporate (frequent issuer, large issue) > low-quality corporate / small or infrequent issues / complex structures.

Exhibit 1 correlations with the S&P 500 (monthly, 20 years to Dec 2019): US Aggregate −0.09, 10Y Treasury −0.30, US Corporate 0.20, Global Aggregate 0.15, TIPS 0.02, US High Yield 0.63, EM USD 0.51. Excess-return correlations across those indexes are high (0.74-0.93); HY vs S&P annual returns correlation was 0.69.

## Mental Models
- **Carry vs views**: the rolling yield is what you earn if nothing happens; the other three lines are bets. Report them separately.
- **Duration is the first risk factor, spread is the second, convexity is the third**: convexity is negligible for small moves except when added with derivatives or when short options are embedded (MBS, callables).
- **Convexity is not free**: higher convexity usually means lower YTM. Pay for it only when you expect yield volatility above what the give-up covers.
- **Liquidity is a yield you sell or buy**: a buy-and-hold investor harvests the illiquidity premium; a liquidity-constrained one pays for it.
- **Leverage = long bond, short financing**: a swap receiver is long a fixed bond and short a floater; a futures position is margin-funded notional; repo is a collateralized loan that finances the long.
- **Tax-driven asymmetry**: the manager controls the timing of realized gains, not of coupons, so harvest losses and defer gains.
- **Government bonds hedge equity risk; high yield behaves like equity**: correlations are regime-dependent, higher in stress for risk assets.

## Worked Example
**Expected return decomposition** (GBP corporate portfolio, USD-based investor, 1-year horizon). Inputs: coupon £2.75 on price £97.11, expected price after 1 year on unchanged curve £97.27, ModDur 3.70, convexity 18, benchmark yield +0.26%, spread −0.10%, GBP depreciation 0.50%.
1. Coupon income = 2.75/97.11 = 2.83%.
2. Rolldown = (97.27 − 97.11)/97.11 = 0.17%; rolling yield = 3.00%.
3. Rate view = −3.70×0.0026 + ½×18×0.0026² = −0.962% + 0.006% = −0.96%.
4. Spread view = −3.70×(−0.0010) + ½×18×0.0010² = 0.370% + 0.001% = +0.37%.
5. Currency = −0.50%.
6. Total = 3.00 − 0.96 + 0.37 − 0.50 = **1.91%** (unrounded 1.912%).
Interpretation: carry of 3.00% is largely offset by the rate and currency views; the spread tightening adds a small gain. Convexity contributes under 1 bp at these moves.

**Leverage**: equity 100, borrow 50 (VB/VE = 0.5), rB = 1.5%. If rI = 4%: rP = 4% + 0.5×2.5% = 5.25%. If rI = −2%: rP = −2% + 0.5×(−3.5%) = −3.75%. The gain is proportional to the spread, the loss too, and the second case can trigger margin calls and forced sales.

**Repo**: financing a EUR15m position overnight at 5%: interest = 15,000,000 × 5% × 1/360 = EUR2,083.33; repurchase price EUR15,002,083.33.

**Tax-aware liquidation**: need €10m; A has a +€1m gain (slightly overvalued), B a −€1m loss (slightly undervalued). Tax-exempt fund: sell A (follow the valuation view). Taxable fund with pass-through treatment: sell B, since realizing the loss lowers the distributed net gain; selling A would trigger 28% tax on €1m = €280,000. This assumes no other losses to offset.

## Anti-patterns
- **Ranking bonds by YTM alone**: ignores rolldown, spread and currency views, reinvestment and liquidity.
- **Using nominal (modified) duration/convexity for bonds with embedded options**: use effective measures.
- **Using last-traded prices for illiquid bonds**: stale; use matrix pricing.
- **Treating average correlations as constant**: they shift in stress (flight to quality).
- **Confusing tracking error with tracking difference**: a pure indexer targets zero active risk but still lags the index by costs and fees.
- **Ignoring the cost side of leverage**: haircuts, margin calls, funding withdrawal and rollover risk in TRS.
- **Ignoring taxes for taxable investors**: pre-tax decisions can be wrong after tax.
- **Mixing convexity scalings** (raw vs /100) in the return equation.

## Exam Focus & Traps
- Identify an approach from a table: duration mismatch = active; near-identical = pure indexing; small mismatches with matched duration = enhanced.
- Convexity in the return model is `½ × Convexity × (Δ)²`; Δ in decimals (0.0026 not 0.26). Sign of the spread term: spread tightening (negative Δ) gives a positive return.
- Rolldown uses the unchanged curve and price at horizon; the coupon-return denominator is the beginning price.
- Currency: multiplicative `(1+R_FC)(1+R_FX) − 1`; in the decomposition it is a single additive line.
- "Same duration, higher convexity" outperforms when yields fall a lot or rise a lot, but usually costs yield.
- Zero-coupon: duration ∝ maturity, convexity ∝ duration² (30y zero ≈ 9× the 10y).
- Dispersion is the variance of cash flow timing, not credit or spread risk (spread duration).
- Repo vs securities lending: repo has a term and a haircut; securities lending is open-ended, recallable and has a rebate rate. A negative rebate means the security is hard to borrow.
- Tax: US-style pass-through means the manager's realizations affect investors' tax timing; UK-style does not.
- Total return swap: receiver has no legal ownership; counterparty and rollover risk; requires less cash than an ETF/fund.
- Source note: Example 4 prints the price as £97.12 in Exhibit 11 but uses £97.11 in the solution. Using £97.12 gives coupon 2.83% and rolldown 0.15%; the printed answer 1.91% uses £97.11.

## Key Takeaways
1. Fixed income adds diversification, dependable cash flows and (through FRNs and linkers) inflation protection; linkers can improve real risk-adjusted returns and have lower volatility because they depend on real rates.
2. Classify the mandate first: liability-based (ALM/LDI) versus total return, then pure/enhanced/active by active return and tracking error targets.
3. Portfolio duration is the market-value-weighted average of bond durations; use effective duration and convexity when cash flows are rate-contingent; control spread duration and DTS for credit exposure.
4. Evaluate strategies on expected return (coupon + rolldown + rate view + spread view + currency), not YTM, and remember its approximations.
5. Expect illiquidity premia: match bond liquidity to the horizon; use matrix pricing; trading cost ≈ bid-ask yield spread × duration; consider funds, ETFs, futures, swaps and TRS as alternatives to physical bonds, weighing fees against bid-offer costs.
6. Leverage magnifies return by (VB/VE)(rI − rB) and creates forced-sale, financing-withdrawal and counterparty risks, particularly in crises.
7. For taxable clients, manage after-tax: harvest losses, defer gains, limit turnover, and know the vehicle's tax treatment (pass-through or not).

## Connects To
- **ch05**: duration, convexity, PVBP and spread measures that this chapter aggregates to portfolio level.
- **ch13**: liability-driven strategies (cash flow and duration matching, immunization, contingent immunization) and index-based strategies expanded from the mandate classification.
- **ch14**: yield curve strategies build on the rolldown and rate-view return components.
- **ch15**: credit strategies extend spread duration, DTS, and relative value.
- **ch02**: repo, funding and issuance market mechanics.
- **ch11**: credit default swaps as alternative credit exposure.
- **`tuckman-fixed-income` ch03**: return, spread and yield decomposition; **`tuckman-fixed-income` ch04**: risk metrics and hedges.
- **`cfa-derivatives`**: futures, swaps and TRS mechanics used for leverage and overlays.
