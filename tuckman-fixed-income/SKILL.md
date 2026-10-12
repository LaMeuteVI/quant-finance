---
name: tuckman-fixed-income
description: "Tuckman & Serrat, Fixed Income Securities (3rd ed., Wiley 2011): the desk-oriented reference on pricing, risk, hedging and relative value of rates products, from discount factors to term structure models, repo, futures, swaps, options, credit and mortgages. Use when working on discount factors, spot forward par rates, bootstrapping, DV01 duration convexity hedging, key-rate and partial 01, regression and PCA hedges, short-rate models (Ho-Lee, Vasicek, CIR, Black-Karasinski, Gauss+, LIBOR market model), OAS, repo and specials, Treasury futures basis and CTD, Eurodollar and fed funds futures, swap valuation, OIS two-curve discounting, CMS convexity, caps swaptions SABR, CDS and asset swaps, MBS prepayment, curve construction."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Fixed Income Securities: Tools for Today's Markets
**Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities*, 3rd ed. (Wiley, 2011) | **Domain**: Finance de marché | **Chapters**: 22 (Overview + 21) | **Generated**: 2026-09-29

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch07`
- **Browse** — "what chapters do you have?"

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering. For desk rules and numbers see [cheatsheet.md](cheatsheet.md).

---

## Core Frameworks & Mental Models

**Pricing and curves**
1. **Discounting = arbitrage pricing (ch01)**. Bootstrap d(t) from full prices; `PV = ΣCF·d(t)`; replicate with `F = C⁻¹c`. Rich/cheap is relative to a stated base set; check specialness, on-the-run premium and bid/ask before trading a gap.
2. **Three curves, one object (ch02)**. `d(t) = (1 + r/2)^(−2t)`, `1 + f(t)/2 = d(t−.5)/d(t)`, `(C/2)A(T) + d(T) = 1`; `P = 1 + ((c − C)/2)·A`. Spot = average of forwards; forwards sit above spot when spot rises; par below spot on a rising curve. Read anomalies in forwards.
3. **Roll-down (ch02, ch03)**. On an unchanged curve a fixed-rate asset rises if its coupon is below the expiring forward. Check "what if nothing happens" before sizing.
4. **Spreads over yields (ch03)**. A spread is a price in rate units; YTM is a quote and suffers the coupon effect. P&L = cash carry + carry-roll-down + rate change + spread change.
5. **Swaps are the benchmark (ch00, ch17, ch21)**. Swaps are fungible; governments carry issue-specific liquidity and repo effects. Build curves with flat forwards and judge them by hedge locality.

**Risk and hedging**
6. **DV01, duration, convexity (ch04)**. `F_B = −F_A·DV01_A/DV01_B`; `ΔP/P ≈ −DΔy + ½CΔy²`; equal-DV01 hedges are local and a hedged book can be short convexity (short vol). Barbell vs bullet: convexity bought with yield.
7. **Curve risk (ch05)**. Key-rate '01s (bond desks), partial '01s (swap desks), bucket '01s (explanation) decompose DV01; zero DV01 can hide a large steepener. Hedge the biggest bucket, then re-neutralize.
8. **Empirical hedges (ch06)**. `F^R = DV01 ratio × β̂`, residual vol `|F|·DV01/100·σ̂`; put the yield with the extra component on the left; test stability. Three PCs (level, slope, short rate) explain > 99%.

**Term structure models**
9. **Risk-neutral pricing (ch07)**. Probabilities that reprice the underlying bonds; calibrate once, price by backward induction; OAS discounts only. Hedged P&L ≈ OAS × time + convergence.
10. **Curve-shape decomposition (ch08)**. `f = r + E[dr]·D + λD − ½Cσ²`: expectations, risk premium (short end), convexity (long end); premium and expectations are twins; convexity is no free lunch.
11. **Model art (ch09–ch11)**. Drift fits the curve (Ho-Lee), mean reversion shapes factors and vol (Vasicek), σ(t) fits options, lognormal/CIR avoids negative rates (BK needs variable Δt), Gauss+ (hump) for relative value, LMM for exotics. Arbitrage-free for pricing, equilibrium for finding value.

**Financing, futures, swaps**
12. **Repo and forwards (ch12, ch13)**. `P_T = P₀(1 + rd/360)`; specialness is a dividend to the owner, capped by the fails charge; forward = FV(full spot) − FV(coupons), drop = carry; futures < forward for bonds, rate futures need convexity adjustment `σ²t²/2 + σ²βt/2`; tail hedges.
13. **Treasury futures (ch14)**. `F_T = min P_i/cf_i`; net basis = quality option price; above 6% the long-duration bond is CTD, below the short one.
14. **Short rates (ch15)**. FRA = forward; ED $25/bp tailed; FF $41.67/bp, `D/30` contracts; FOMC probability from month averages; LIBOR–OIS as stress gauge.
15. **Swaps and discounting (ch16, ch17)**. Swap = fixed bond minus floater; exposure is NPV; hedge legs separately. Discount at the collateral rate (OIS), project LIBOR from a separate curve: `NPV = (c − C)·A_OIS`. Real arbitrage starts at zero cash and needs capital for divergence.

**Options, credit, mortgages**
16. **Rate options (ch18)**. `h₀·E[(S−K)⁺]` with the right numeraire; normal vol is the lingua franca; callable = noncallable − call; SABR for smiles, calibrate to the backbone.
17. **Credit (ch19)**. `s ≈ λ(1 − R)`; upfront = coupon gap × risky annuity; CDS-bond basis is not an arbitrage; credit-adjust DV01 for distressed names.
18. **MBS (ch20)**. Mortgage = bond minus American call at the scheduled balance; CPR = 1 − (1 − SMM)^12; refinancing S-curve plus turnover, defaults, curtailments, burnout; Monte Carlo with OAS; IO negative duration; negative convexity.

---

## Chapter Index
| # | Title | Part | Key Frameworks |
|---|---|---|---|
| [ch00](chapters/ch00-overview-global-fixed-income-markets.md) | Overview of Global Fixed Income Markets | Overview | Bank risks, leverage arithmetic, pensions and LDI, swaps as benchmark |
| [ch01](chapters/ch01-prices-discount-factors-arbitrage.md) | Prices, Discount Factors, and Arbitrage | Part One | Bootstrapping, law of one price, replication, STRIPS |
| [ch02](chapters/ch02-spot-forward-par-rates.md) | Spot, Forward, and Par Rates | Part One | Spot-forward-par, roll-down, forward RV trade |
| [ch03](chapters/ch03-returns-spreads-yields.md) | Returns, Spreads, and Yields | Part One | Spread to curve, YTM, P&L decomposition |
| [ch04](chapters/ch04-one-factor-risk-metrics-hedges.md) | One-Factor Risk Metrics and Hedges | Part Two | DV01, duration, convexity, bullet vs barbell |
| [ch05](chapters/ch05-multi-factor-risk-metrics-hedges.md) | Multi-Factor Risk Metrics and Hedges | Part Two | Key-rate, partial and bucket '01s |
| [ch06](chapters/ch06-empirical-risk-metrics-hedging.md) | Empirical Risk Metrics and Hedging | Part Two | Regression hedge, PCA, butterflies |
| [ch07](chapters/ch07-science-of-term-structure-models.md) | Science of Term Structure Models | Part Three | Risk-neutral pricing, OAS |
| [ch08](chapters/ch08-short-rate-evolution-and-curve-shape.md) | Short-Rate Evolution and Curve Shape | Part Three | Expectations, premium, convexity |
| [ch09](chapters/ch09-art-of-term-structure-models-drift.md) | Art of Term Structure Models: Drift | Part Three | Ho-Lee, Vasicek, shadow rate |
| [ch10](chapters/ch10-art-of-term-structure-models-volatility.md) | Art of Term Structure Models: Volatility | Part Three | σ(t), CIR, lognormal, Black-Karasinski |
| [ch11](chapters/ch11-gauss-plus-and-libor-market-models.md) | Gauss+ and LIBOR Market Models | Part Three | Gauss+, LMM drifts, calibration |
| [ch12](chapters/ch12-repo-and-financing.md) | Repo and Financing | Part Four | GC vs special, haircuts, fails bound |
| [ch13](chapters/ch13-forwards-and-futures-preliminaries.md) | Forwards and Futures: Preliminaries | Part Four | Forward drop, futures-forward, tail |
| [ch14](chapters/ch14-note-and-bond-futures.md) | Note and Bond Futures | Part Four | CTD, conversion factor, net basis |
| [ch15](chapters/ch15-short-term-rates-and-derivatives.md) | Short-Term Rates and Derivatives | Part Four | FRA, ED, TED, fed funds, OIS |
| [ch16](chapters/ch16-swaps.md) | Swaps | Part Four | Fictional notional, reset risk, CMS correction |
| [ch17](chapters/ch17-arbitrage-with-financing-two-curve-discounting.md) | Arbitrage with Financing and Two-Curve Discounting | Part Four | Financed arbitrage, OIS discounting |
| [ch18](chapters/ch18-fixed-income-options.md) | Fixed Income Options | Part Four | Numeraires, caps, swaptions, SABR, callables |
| [ch19](chapters/ch19-corporate-bonds-and-cds.md) | Corporate Bonds and CDS | Part Four | Asset swaps, hazard rate, CDS basis |
| [ch20](chapters/ch20-mortgages-and-mbs.md) | Mortgages and MBS | Part Four | Prepayment model, Monte Carlo, TBA, rolls |
| [ch21](chapters/ch21-curve-construction.md) | Curve Construction | Part Four | Flat forwards, smooth forwards, locality |

## Topic Index
- **Accrued interest** → ch01, ch03
- **Annuity factor** → ch02, ch16, ch17
- **Arbitrage with financing** → ch17
- **Asset swap spread** → ch19
- **Barbell vs bullet** → ch04
- **Basis (CDS-bond)** → ch19
- **Basis (futures), net basis** → ch14
- **Black-Karasinski** → ch10
- **Bootstrapping** → ch01, ch02, ch21
- **Burnout** → ch20
- **Caps and floors** → ch18
- **Carry, roll-down** → ch02, ch03, ch13
- **CDS** → ch19
- **CIR** → ch10
- **CMS convexity** → ch16
- **Conversion factor, CTD** → ch14
- **Convexity** → ch04, ch08
- **Credit triangle, hazard rate** → ch19
- **Curve construction** → ch21
- **DV01, duration** → ch04
- **Dollar roll, TBA** → ch20
- **Eurodollar futures** → ch13, ch15
- **Fed funds futures, FOMC** → ch15
- **Forward rates** → ch02
- **Forwards and futures** → ch13
- **Gauss+** → ch11
- **Ho-Lee** → ch09
- **Key-rate duration** → ch05
- **LIBOR market model** → ch11
- **LIBOR–OIS** → ch15, ch17
- **Mean reversion** → ch09
- **MBS, prepayment** → ch20
- **OAS** → ch07, ch20
- **OIS, two-curve discounting** → ch17
- **Pensions, LDI** → ch00
- **PCA** → ch06
- **Regression hedge** → ch06
- **Repo, specials** → ch12
- **Risk-neutral pricing** → ch07
- **Risk premium** → ch08
- **SABR, skew** → ch18
- **Securitization, bank funding** → ch00
- **Spread to curve** → ch03
- **STRIPS** → ch01
- **Swaps** → ch02, ch16
- **Swaptions** → ch18
- **TED spread** → ch15
- **Vasicek** → ch09
- **Yield-to-maturity** → ch03
- **Yield curve PCs** → ch06

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, tells

---

## Related Skills
- `hull-derivatives` — standard derivatives theory (Black, Greeks, HJM, LMM) when you need Hull's notation or equity/FX products
- `cfa-fixed-income` — exam-level fixed income (L1–L3) for definitions, curriculum views and portfolio strategies
- `ilmanen-yield-curve` — forward-rate analysis, carry/roll-down and yield-curve trade frameworks
- `ecb-yield-curve-modelling` — Nelson-Siegel/Svensson fitting for a central-bank curve
- `cfa-derivatives` — forward and swap pricing at exam level
- `passarelli-option-greeks` — option trading and Greeks when the question is about listed options

## Scope & Limits
Covers the 3rd edition (2011): 2009–2011 market data, USD/EUR/GBP/JPY curves, LIBOR-era conventions (SOFR/€STR replace LIBOR now; the two-curve logic carries over). Exercises were used only for checks. Formulas were recomputed, and source slips are flagged as Correction in the chapters. Not covered: time-varying risk premia research, post-2011 regulation (XVA, margin rules), negative-rate market practice.
