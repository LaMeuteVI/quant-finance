# Chapter 15: Fixed-Income Active Management: Credit Strategies
> **Source**: CFA Program Curriculum 2022, Level III, Reading 14 · Portfolio Management (Fixed Income) | Campe Goodman, CFA, and Oleg Melentyev, CFA

## Core Idea
Spread-based portfolios earn excess return over the index through the fourth term of the return equation, the view on **yield spreads**. This means positions in credit quality, spread duration, sector, issuer and curve shape, held in cash bonds, CDS, indexes or structured products. The workflow is: choose the right spread measure (OAS), quantify spread risk (spread duration, **DTS**, expected loss), then express a bottom-up, top-down or factor view in the instrument that is cheapest and most liquid. Duration-match the legs of every relative trade.

## Learning Outcomes Covered
- Risk considerations for spread portfolios (POD, LGD, credit migration, spread curves, credit cycle).
- Spread measures for fixed-rate bonds and FRNs; why OAS is the most appropriate.
- Bottom-up approaches (universe definition, ratios, Z-score, reduced-form and structural models, relative value).
- Top-down approaches (macro, ratings and sector allocation) and factor-based/ESG credit strategies.
- Liquidity risk in credit markets and how to manage it; tail risk (VaR, CVaR, stress) and how to manage it.
- CDS strategies: single-name and index, long/short, curve trades.
- Positioning for a spread view: static and dynamic credit-curve strategies, cash vs synthetic.
- International credit: developed vs emerging markets; structured credit as an alternative to bonds; analytics tools.

## Frameworks Introduced
- **Fixed-income return equation (Eq. 1)**: `E(R) ≈ coupon income ± rolldown ± E(ΔP from benchmark-yield view) ± E(ΔP from spread view) ± E(ΔP from currency view)`
  - When to use: to separate the credit bet from the rate and FX bets. Active credit managers usually run rate risk separately.
- **Credit valuation adjustment (CVA) framework**: `EL = POD × LGD`, `LGD = EE × (1 − RR)`, `CVA = Σ PV(expected loss)` discounted at the risk-free rate.
  - Shortcut: `Spread ≈ POD × LGD`, so `POD ≈ Spread / LGD`. It works near par. Distressed bonds trade on price, converging to the recovery rate.
- **Expected excess spread return (Eq. 9–10)**: `E[ExcessSpread] ≈ Spread₀ − (EffSpreadDur × ΔSpread) − (POD × LGD)`
  - When to use: a one-year relative-value screen across ratings, issuers or sectors, and scenario tests.
  - How: (1) take the current OAS or Z-spread; (2) subtract spread duration times the expected spread change (a tightening adds); (3) subtract expected loss; (4) for horizons under a year, scale `Spread₀` and expected loss by the horizon fraction; (5) compare per unit of spread duration.
  - Failure mode: assumes ΔSpread and rates are independent, and uses the same duration for all rating buckets. It breaks down for HY, distressed and flight-to-quality moves.
- **Duration Times Spread (DTS)**: `DTS ≈ EffSpreadDur × Spread`; portfolio DTS is the market-value-weighted average.
  - Why: spread changes are roughly *proportional* (%), not absolute, so wide-spread bonds move more. Estimate spread P&L as `ΔP/P ≈ −DTS × (ΔSpread/Spread)`. Index-relative DTS is the risk-budgeting yardstick.
- **Bottom-up process**: define the universe, then divide it into sectors where company risk dominates industry and macro risk, then compare issuers. For each issuer, combine ratios (EBITDA/assets, debt/capital, EBITDA/interest), reduced-form and structural models, and the issuer's spread curve to decide over/underweight. Watch new-issue concessions, liquidity, call features, split ratings, M&A.
- **Top-down process**: macro view (growth, real rates/inflation, volatility and risk appetite, geopolitics, FX), then a rating and sector allocation, expressed with sector and rating spread curves. Use spread-vs-leverage regressions across sectors.
- **Factor-based credit** (Israel, Palhares, Richardson 2018): four factors with positive risk-adjusted returns and diversification versus equity and credit betas.

| Factor | Rationale | Measure |
|---|---|---|
| Carry | Expected return if POD and risk premium unchanged | OAS |
| Defensive | Safer assets earn higher risk-adjusted return | Market leverage, gross profitability, low duration |
| Momentum | Recent winners keep winning | Trailing 6-month bond and equity excess return |
| Value | Cheap vs fundamentals | Spread less model-implied spread (rating, duration, vol) |

- **ESG in credit**: (1) exclusion screens, (2) best-in-class or ESG-tilted selection while matching index risk, (3) thematic/use-of-proceeds debt such as green and social bonds. Green bonds rank pari passu with senior unsecured, and often price slightly tighter because of demand.
- **CDS strategy menu**: buy protection to underweight or short risk, sell protection to overweight or long risk. Long/short pairs of names, sectors or HY vs IG indexes. Curve trades with **BPV-matched** notionals. Basis and event trades.
- **Static vs dynamic credit-curve strategies**:
  - View equals the forwards (stable spreads and low defaults): **lower credit quality**, **extend spread duration** (carry and roll-down), sell protection.
  - View differs from the forwards: tactical rating/sector/curve tilts, long/short cash, CDX HY/IG, steepeners/flatteners.

## Key Concepts
- **Yield spread compensation**: pays for default risk, downgrade (migration) risk and liquidity (bid–offer) risk.
- **POD / LGD / recovery rate (RR)**: default probability (annual %); loss as % of par; `LGD = 1 − RR`. Recovery depends on seniority and security.
- **Credit loss rate**: default rate × loss severity (realized % of par lost). Moody's 1983–2019: IG average 0.05% (max 0.41%), HY average 2.53% (>5% in some recessions).
- **Credit migration**: downgrade probability exceeds upgrade probability, and the spread widening on downgrade exceeds the tightening on upgrade. So migration is a negative-skew risk even where defaults are rare.
- **Credit cycle**: spread level and slope move with the cycle (Exhibit 8, in Mental Models). HY moves more than IG.
- **Credit spread curve**: spreads by maturity, for an issuer or by rating/sector. Upward slope means low near-term default probability. Flat or inverted means near-term stress.
- **Empirical vs analytical duration**: in flight to quality, government yields fall while HY spreads widen, so measured (regression) duration is lower than modified duration.
- **Effective spread duration / convexity**: sensitivity of value to OAS (or DM), by ±Δ shifts.
- **Weighted vs ordinal rating scale**: Moody's weights (Aaa 1, A2 120, Baa2 360, Ba2 1,350, B2 2,720, Caa2 6,500) reflect the non-linear rise in loss.
- **Distance to default (EDF, DRSK)**: structural models. POD is the probability that market asset value falls below the liabilities default point.
- **Reduced-form model / Altman Z-score**: statistical default score from financial ratios and macro variables.
- **Effective spread (trade cost)**: `(trade price − mid)` for buys, `(mid − trade price)` for sells, per unit size.
- **TRACE**: US post-trade reporting of corporate bond prices and volumes, used to gauge liquidity and trading cost.
- **CDS price**: `1 + (Fixed coupon − CDS spread) × EffSpreadDur_CDS` per 1 of notional. It is the seller's value (see Formulas). Standard coupons: 1% IG, 5% HY.
- **CDX / iTraxx**: standardized CDS indexes (CDX NA IG has 125 names; iTraxx Crossover is European HY, 5% coupon).
- **Payer / receiver option on a CDS index**: right to buy protection (short credit) / to sell protection (long credit) at a strike spread.
- **Sovereign ceiling**: a corporate is usually rated no higher than its sovereign, which concentrates EM credit in low-IG and high-HY ratings.

## Formulas & Reference Tables

**Spread measures for fixed-rate bonds**

| Measure | Definition | Pros | Cons |
|---|---|---|---|
| Yield spread | YTM − YTM of on-the-run government of similar maturity | Simple, works for illiquid bonds | Maturity mismatch, curve-slope bias, benchmark changes over time |
| G-spread | YTM − interpolated government (constant-maturity) yield | Maturity-matched and transparent | Sensitive to government supply and demand |
| I-spread | YTM − interpolated swap (MRR) rate | Market-based, hedgeable, good for carry | Single point on the curve; option-free only |
| ASW (asset swap spread) | Bond coupon − swap rate for the bond's cash-flow dates; equals spread over MRR when bought at par | Tradable | A traded spread, not a cash-flow measure; option-free; swap MTM survives default |
| Z-spread | Constant spread over the *spot* curve: `PV = Σ PMT/(1+z_t+Z)^t + FV/(1+z_N+Z)^N` | Uses the whole term structure | Option-free only; needs a solver |
| CDS basis | Bond Z-spread vs CDS spread (same issuer, same tenor) | Compares the cash and derivative markets | See ⚠ Correction below |
| **OAS** | Constant spread over the zero curve so that the arbitrage-free value (with rate vol) equals price; for an option-free bond OAS = Z-spread | Comparable across option-free, callable, putable and structured | Model, volatility and prepayment dependent; option-embedded bonds may not realize it |

- **Interpolation**: `w_short = (T_long − T) / (T_long − T_short)`; `r_T = w_short·r_short + (1 − w_short)·r_long`.
- **Portfolio OAS** = market-value-weighted average (use full price, i.e. price + accrued).

**FRNs**
- `PV = Σ [(MRR + QM)·FV/m] / (1 + (MRR + DM)/m)^t + FV / (1 + (MRR + DM)/m)^N`. QM is the quoted margin, DM the discount margin, and `m` the payments per year.
- Par if QM = DM; discount if QM < DM; premium if QM > DM (on a reset date).
- **Z-DM** uses forward MRR (spot curve) instead of flat MRR. On an upward-sloping curve, Z-DM < DM.
- Effective rate duration of a par floater on reset date ≈ 0 (slightly negative below par). Spread duration is roughly the remaining life (annuity-like).
- QM is fixed at issue and does not track credit changes.

**Spread risk**
- `%ΔPV_spread ≈ −(EffSpreadDur × ΔSpread) + ½ × EffSpreadCon × (ΔSpread)²`
- `EffSpreadDur = (PV₋ − PV₊)/(2 × PV₀ × ΔSpread)`; `EffSpreadCon = (PV₋ + PV₊ − 2PV₀)/(PV₀ × ΔSpread²)`
- `%ΔSpread-based`: `ΔSpread_bp ≈ DTS × (ΔSpread/Spread)` at the portfolio level.

**Credit VaR**
- Parametric ΔY = `σ_Y × z × √t` with z = 1.65 (95%) or 2.33 (99%); `ΔP ≈ −ModDur × ΔY × MV`.
- Methods: parametric (simple, poor for options and non-normal returns), historical simulation (real data but history-bound), Monte Carlo (flexible but model-dependent). Add scenarios.
- **CVaR** = mean loss beyond VaR. **Incremental VaR** = VaR impact of one position change. **Relative VaR** = VaR of active positions vs benchmark, approximating tracking-error risk.

**CDS**
- `CDS Price ≈ 1 + (Fixed coupon − CDS spread) × EffSpreadDur_CDS`
- Upfront: spread < coupon → protection buyer *receives* `(coupon − spread) × dur`; spread > coupon → buyer *pays* `(spread − coupon) × dur`.
- `ΔCDS value (protection seller) ≈ −ΔSpread × EffSpreadDur × Notional`. The buyer's P&L has the opposite sign.
- **Curve trade sizing**: `Notional_short-tenor = Notional_long-tenor × (Dur_long / Dur_short)`, so that `BPV = Dur × Notional / 10,000` matches on both legs.
- **Currency conversion for unhedged foreign exposure**: `R_DC = (1 + R_FC)(1 + R_FX) − 1`.

**Reference values**
- Average recovery, US corporates 1983–2019: 1st-lien loan 64%, 2nd-lien loan 29%, senior unsecured loan 44%, 1st-lien bond 55%, 2nd-lien bond 45%, senior unsecured bond 35%, senior subordinated 27%, subordinated 28%, junior subordinated 14%.
- Two-year default probability (S&P, 1981–2019): AAA 0.03%, AA 0.06%, A 0.14%, BBB 0.45%, BB 1.96%, B 7.83%, CCC 36.49%.
- Spread as share of total YTM (2009–2020): BB about 60% on average, A about 33%.
- Z-score (Altman 1968, as quoted): `1.2·WC/TA + 1.4·RE/TA + 3.3·EBIT/TA + 0.6·MVE/TL + 0.999·Sales/TA`. Above 3.0 is sound, 1.8–3.0 is a grey zone, below 1.8 is distressed. (These are the 1968 manufacturing coefficients, applied in the reading to non-manufacturers.)

| Credit-cycle phase | Early expansion | Late expansion | Peak | Contraction |
|---|---|---|---|---|
| Profitability | Rising | Peak | Stable | Falling |
| Leverage | Falling | Stable | Rising | Peak |
| Defaults | Peak | Falling | Stable | Rising |
| Spread level | Stable | Falling | Rising | Peak |
| Spread slope | Stable (IG), inverted (low ratings) | Steeper | Steeper | Flatter (IG), inverted (low ratings) |

## Mental Models
- **Separate the bets**: manage rate risk with swaps or futures, and let spread duration carry the credit view. A credit portfolio's P&L is `carry − spread duration × ΔSpread − expected loss`.
- **Spreads move in percentages**: judge risk with DTS, not spread duration alone. A 4-duration BB bond at 300 bp is 3 times as risky as a 4-duration A bond at 100 bp.
- **Ratings are ordinal, losses are convex**: average on the *weighted* scale, or better, on OAS. Half A1 and half Ba3 is Ba1/BB+ on the weighted scale, not Baa2.
- **Default is rare, migration is common**: IG investors mainly bear downgrade and spread-widening risk. HY investors bear default risk as well, and near default the price tracks the recovery rate, not the rate curve.
- **CDS is the liquid, unfunded, one-sided credit tool**: use it to short, to reach tenors the cash market lacks, and to duration-match long/short trades. But it brings basis risk, and standardized coupons that create upfront payments.
- **Lower quality equals more carry only if the cycle cooperates**: lowering quality and extending spread duration work under a static curve. In a slowdown, spread curves flatten or invert (HY first).
- **Liquidity is a portfolio input**: tactical trades in on-the-runs, new issues, ETFs, CDS. Illiquid off-the-runs are for buy-and-hold, to earn the illiquidity premium.

## Worked Example
**A. DTS and expected excess return** (source data, recomputed).
- Portfolio 50/50: A-rated (OAS 100, dur 3.0) and BB-rated (OAS 300, dur 4.0). DTS = 0.5×100×3 + 0.5×300×4 = **750**. Index OAS widens 10 bp on a 125 bp base, so +8%. Expected spread move = 750 × 8% = **60 bp** portfolio-equivalent widening.
- Two industrials: A2 (spread 100, dur 5, POD 0.27%) and B2 (spread 350, dur 7, POD 3.19%), RR 40% so LGD 60%. With no spread change: A gives `1% − 0.27%×0.6 = 0.84%` (recomputed 0.838%); B gives `3.5% − 3.19%×0.6 = 1.59%` (1.586%). If spreads widen 10% (10 bp and 35 bp): A = `1 − 5×0.10 − 0.162 = 0.34%`; B = `3.5 − 7×0.35 − 1.914 = −0.86%`. B pays only if spreads hold. Its duration and volatility (spread beta) are what hurt.

**B. Duration-matched CDS curve steepener.** German issuer 5y CDS 130 bp (dur 4.669), 10y CDS 175 bp (dur 8.680). View: the curve steepens, so buy 10y protection (short risk) and sell 5y protection. Notional: €10m 10y, so 5y notional = 10m × 8.68/4.669 = **€18.59m**, giving BPV = €8,680 on each leg. If 5y widens 10 bp and 10y widens 20 bp: 5y seller loses 18.59m × 0.10% × 4.669 = €86,800; 10y buyer gains 10m × 0.20% × 8.68 = €173,600. Net **+€86,800** = BPV × 10 bp of steepening.

**C. Cash roll-down decomposition (static curve).** Overweight AUD 50m of 15y over 10y (semiannual). Extra coupon: 0.65%/2 × 50m = $162,500, split into $87,500 benchmark and $75,000 credit. Price gain: 15y $431,700 vs 10y $89,660, so incremental $342,040. The 15y yield drop of 7 bp is half benchmark and half spread, so $215,850 is credit. The trade earns about **$504,540** over six months, of which about **$290,850** is credit-curve roll-down.

**D. Correct CDX slowdown trade** (see ⚠ Correction). Sell IG protection, buy HY protection, $10m each. CDX IG at 120 bp (dur 4.67, price 0.99066), HY at 300 bp (dur 4.65, price 1.0930). With unchanged spreads and one-year-ahead durations (3.78, 3.76): IG leg +$17,800, HY leg +$178,000, coupon −$400,000 (pay 5%, receive 1%). **Net −$204,200 as pure carry cost.** In the downturn (IG +50% to 180 bp, HY doubles to 600 bp): IG −$209,000, HY +$1,306,000, coupon −$400,000. **Net +$697,000.**

## Anti-patterns
- **Using yield spread or G-spread on callable or MBS paper**: ignores option value. Compare across structures with OAS, and remember it is model-dependent.
- **Averaging ratings ordinally**: understates the loss weight of the low-rated bonds.
- **Using analytical duration to hedge HY against Treasuries**: in flight to quality, spreads widen while yields fall, so empirical duration is lower than modified duration. Over-hedging shorts too much rate risk.
- **Assuming spread shocks are absolute (bp)**: cheap-credit spread moves are larger. Use %ΔSpread and DTS.
- **Sizing curve or long/short CDS trades on notional**: unequal spread durations make it a hidden outright bet. Match BPV.
- **Relying on VaR alone**: it understates frequency and severity of tail events, ignores stress correlations and liquidity, and gives no expected loss beyond the threshold. Add CVaR, scenarios and position limits.
- **Assuming shorting cash HY is free**: borrow availability and cost worsen in downturns. The CDS route is the practical implementation.
- **Buying tail hedges after the panic**: option-based protection (swaption, CDS swaption) is expensive in high volatility and drags on excess spread.
- **Ratings-only credit work**: ratings lag, differ in focus (S&P on POD, Moody's on expected loss) and horizon.

## Exam Focus & Traps
- **Which spread when**: "best for comparing across callable, putable, structured" is **OAS**. "Term-structure aware, option-free" is **Z-spread**. "Tradable, converts coupon to MRR + spread" is **ASW**. Yield spread above G-spread means the benchmark maturity is shorter than the bond's on an upward-sloping curve. ASW uses the coupon, I-spread uses YTM, so they differ by the premium or discount.
- **FRN**: QM vs DM decides premium, par or discount. QM > DM means premium (credit improved). FRN price sensitivity is to DM and Z-DM, not to MRR.
- **Signs in CDS**: spread < coupon → protection buyer **receives** upfront. Protection buyer = short risk, gains when spreads widen. Seller = long risk. Sold protection on a wider spread loses value.
- **HY vs IG curve in a downturn**: HY flattens or inverts, IG flattens; in recovery IG spreads stay stable and HY steepens. Steepening means low near-term default expectations.
- **Curve trades**: steepener = buy long-tenor protection, sell short-tenor protection (BPV matched). Flattener is the reverse. Buying HY protection and selling IG protection is the "economic slowdown" trade.
- **Liquidity hedge (Example 19)**: a long bond position that is being sold gradually is hedged with a **pay-fixed** asset swap unwound **in proportion to the amount sold**, not all at once.
- **Structured credit**: housing slowdown → move from BBB to A within MBS (keeps real estate exposure, cuts spread beta). Rising short rates and flattening → CLO tranches (floating rate) over fixed CDOs. Covered bonds → dual recourse, lower yield and lower risk.
- **EM**: reserves/GDP = liquidity. External debt/GDP = leverage to foreign creditors. Deficit/GDP = fiscal stability. Forward rate bias lets an unhedged high-yield currency beat UIP if it depreciates less than the rate differential implies.
- **Sovereign ceiling** applies to corporates. **Distance-to-default**: higher equity volatility and higher leverage raise POD.
- **Recompute for VaR**: use `σ × z × √t`. Note z of 2.33 for 99% and 1.65 for 95%.
- **⚠ Correction (CDS basis)**: the reading first defines basis as Z-spread minus CDS spread, then labels the sign inconsistently ("negative basis if yield spread is above CDS spread; positive... in excess"). Both sentences describe the same case. Market convention is `Basis = CDS spread − bond Z-spread`, so **negative basis means the bond spread is wider than CDS**. This can be exploited (buy the bond, buy protection). Check which definition the question gives.
- **⚠ Correction (Example 29, CDX slowdown)**: the text says buy IG protection and sell HY protection, then adds +$400,000 premium and reports $595,800 and $1,497,000. The price legs match the opposite position (sell IG, buy HY, the correct slowdown trade), for which the coupon flow is **−$400,000**. Correct results are −$204,200 (flat spreads) and +$697,000 (downturn). Use the sign logic, not the printed totals.
- **⚠ Correction (Example 20, VaR)**: "daily yield volatility 1.75%" must be **1.75 bp** (0.0175%); then 1.75 × 2.33 × √21 = 18.7 bp, and VaR ≈ $1.0m. Read literally, the percent version gives 18.7 percentage points.
- Example 30's printed tactical return is 7.795% and the passive return 7.059%. Recomputed with unrounded inputs they are 7.797% and 7.060%. Rounding only.

## Key Takeaways
1. Use the return equation to isolate the spread term, then run spread views with spread duration and DTS, not ratings alone.
2. Screen relative value with `E[ExcessSpread] = Spread₀ − dur × ΔSpread − POD × LGD`. Extra spread is worth it only if it beats expected loss and the widening you can tolerate.
3. Prefer OAS as the portfolio-wide spread measure. Use Z-spread for option-free bonds, ASW or I-spread when hedging or carrying with swaps, and CDS basis when trading cash versus derivatives.
4. Expect spread curves to steepen through recovery and expansion and flatten or invert in the downturn, HY first and hardest. Tilt quality and spread duration with the cycle.
5. Manage liquidity by holding liquid/on-the-run/new issues for tactical positions, illiquid bonds for buy-and-hold, and using ETFs and CDS to close gaps quickly.
6. Treat VaR as a floor. Add CVaR, scenario tests, position limits, risk budgets, and (when affordable) swaptions or CDS swaptions.
7. Express credit views synthetically when cash shorting is costly, with BPV-matched notionals, and remember the standard 1%/5% coupons drive upfront cash.
8. For unhedged international credit, add the FX return with `(1+R_FC)(1+R_FX)−1`. In EM, start with the sovereign (ability and willingness to pay, reserves and external debt, currency regime).

## Connects To
- **ch12**: the fixed-income mandate framework (return decomposition, benchmarks, risk budgeting) that this chapter applies to spreads.
- **ch14**: the parallel toolkit for the rate term structure (rolldown, steepeners, butterflies, key-rate durations). Credit-curve trades mirror those, using spread duration instead.
- **ch13**: indexing, ETFs, TRS and derivative overlays that supply liquid credit exposure.
- **ch10**: reduced-form and structural credit models and CVA details behind POD, LGD and distance to default.
- **ch11**: CDS mechanics, standard coupons, upfront payments, basis and index products used in the synthetic strategies.
- **ch09**: OAS and option-adjusted analytics for callable/putable bonds and MBS.
- **ch06**: fundamentals of credit analysis (ratios, seniority, ratings) used in bottom-up work.
- **ch04**: ABS/MBS/CDO tranching and prepayment risk behind the structured credit section.
- **`cfa-portfolio-management` ch13**: VaR, CVaR and stress-testing methods.
- **`tuckman-fixed-income` ch19**: corporate bonds, CDS and credit spread measurement.
