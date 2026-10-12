---
name: cfa-fixed-income
description: "CFA Program fixed income across Level I (2020 R42-R47), Level II (2022 R28-R32) and Level III (2023 R11-R14 plus the 2020 Yield Curve Strategies refresher): bond features, markets, valuation, ABS/MBS, duration and convexity, credit analysis, term structure, binomial trees, embedded options, credit models, CDS, liability-driven investing, yield curve and credit strategies. Use when pricing bonds, computing duration, convexity, OAS, Z-spread, spot and forward rates, building a binomial tree, valuing callable or convertible bonds, analysing MBS prepayment (PSA, CMO, PAC), CVA, CDS upfront and basis, immunization, futures or swap overlays, steepener, barbell, butterfly, carry and rolldown, or preparing CFA fixed income exam questions."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Fixed Income (Levels I–III)
**Source**: CFA Program Curriculum, Fixed Income: L1 2020 R42–R47, L2 2022 R28–R32, L3 2023 R11–R14 + 2020 Yield Curve Strategies refresher | **Domain**: Finance de marché | **Chapters**: 15 | **Generated**: 2026-09-29

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch07`
- **Browse** — "what chapters do you have?"
- **Exam mode** — ask for a quiz on a chapter; I build it from its Worked Example and Exam Focus sections.

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

### Pricing and yields
- **Price = PV of flows; spot rates give the no-arbitrage value** (ch03, ch08). `PV = Σ CF/(1+z_k)^k`. YTM is an IRR that assumes hold-to-maturity, no default and reinvestment at YTM; two bonds with the same YTM can sit on different curves. Use spots for relative value, strips and arbitrage checks.
- **Flat vs full price** (ch03): full = flat + AI, AI = (t/T) × PMT, quote flat, settle full.
- **Spread ladder** (ch03, ch15): G-spread (interpolated government YTM), I-spread (interpolated swap), Z-spread (constant over spot curve), OAS = Z-spread − option cost. Use OAS across structures at the same σ.
- **Money-market toolkit** (ch02, ch03): discount rate vs add-on rate; convert to BEY (365) before comparing; fewer compounding periods needs a higher APR.
- **FRN**: coupon = index + quoted margin, reset in advance, paid in arrears; price is par when quoted margin = discount margin (ch01, ch03, ch10).

### Risk: duration, convexity, curve
- **%ΔP ≈ −ModDur·Δy + ½·Con·Δy²** on the full price (ch05). Yield duration (Macaulay, modified, money, PVBP) for option-free bonds; curve duration (effective, key rate) for anything rate-contingent.
- **Duration gap = MacDur − horizon** (ch05): positive fears higher rates, negative fears lower rates, zero is immunized for a one-time parallel shift.
- **Spots are averages, forwards marginal; forwards are the zero-alpha path** (ch07). Every active rate view is relative to forwards; "unchanged rates" on an upward curve is a bullish bet. Rolldown needs a static upward curve.
- **Level, slope, curvature** (ch07, ch14): level about 82% of curve variance; manage shaping risk with key rate durations (sum = effective duration).
- **Term structure theories** (ch07): pure expectations (risk-neutral), local expectations, liquidity preference (forwards upward-biased), segmented markets, preferred habitat.

### Trees, options, convertibles
- **Calibrated binomial tree** (ch08): nodes spaced e^{2σ}, calibrate date by date so par benchmarks price at 100; backward induction `V = [C + ½(V_H+V_L)]/(1+i)`. σ matters only for optionality. Use Monte Carlo (drift-adjusted) for path-dependent MBS.
- **Equilibrium vs arbitrage-free models** (ch08): CIR (vol ∝ √r, no negative rates) and Vasicek (mean reversion) vs Ho–Lee (normal) and KWF (lognormal) fitting today's curve.
- **Straight ± option** (ch09): callable = straight − call; putable = straight + put; capped FRN = straight − cap; floored FRN = straight + floor. Callable duration is capped and convexity negative near the money; putable always positive. Vol up: callable down, putable up, callable OAS down.
- **Convertible**: minimum value = max(conversion value, straight value); busted, hybrid or equity-like by share vs conversion price (ch01, ch09).

### Securitization
- **Tranching redistributes, never reduces, risk** (ch04). Credit tranching (waterfall, attachment point) moves default loss; time tranching (sequential, PAC/support) moves prepayment risk (contraction and extension). A homeowner holds a call, so MBS are short convexity.
- **Prepayment math** (ch04): SMM = 1 − (1−CPR)^(1/12); PSA 100 = 6% CPR at month 30; average life, not legal maturity.
- **Why SPE lowers funding cost**: true sale, bankruptcy remote; price the collateral, not the originator (ch04).

### Credit
- **Expected loss = PD × (1 − RR)**; four Cs; ratios on level, trend and peers (ch06). Price effect ≈ −MDur·ΔSpread (ch06). IG = spread risk; HY = default and recovery risk.
- **CVA table** (ch10): fair value = VND − Σ LGD × POD × DF, POD_t = h·POS_{t−1}; spread ≈ h(1 − RR). Risk-neutral PD exceeds historical. Structural (why) vs reduced-form (when).
- **Credit migration** lowers expected return (ch10): E[R] ≈ YTM − ModDur × Σ p·Δs.
- **CDS** (ch11): protection leg − premium leg = upfront ≈ (spread − coupon) × risky annuity; payout (1−RR) × notional via ISDA auction on the cheapest-to-deliver; basis = CDS − bond spread; negative basis = buy bond + protection.
- **Credit curve trades** (ch11, ch15): steepener = buy long-dated, sell short-dated protection, BPV-matched.

### Portfolio management
- **Return decomposition** (ch12, ch14, ch15): E(R) ≈ coupon + rolldown ± rate view ± spread view ± FX view. Rolling yield is carry; the rest are bets.
- **Immunization** (ch13): single liability: MV ≥ PV, MacDur = horizon, minimize convexity; multiple: BPV_A = BPV_L, convexity_A > convexity_L. Overlays `N_f = (BPV_L − BPV_A)/(BPV_CTD/CF)`; swaps by notional BPV. Choose swap, collar or receiver swaption by rate view.
- **Curve structures** (ch14): flattener or more curvature or more vol → barbell; steepener or less curvature or calm → bullet; size every leg on PVBP.
- **Spread strategies** (ch15): E[excess] ≈ Spread₀ − SpreadDur × ΔSpread − POD × LGD; DTS for risk budgeting; carry, defensive, momentum, value factors.
- **Leverage**: r_P = r_I + (V_B/V_E)(r_I − r_B); funding and margin risk asymmetric (ch12).

---

## Chapter Index
| # | Title | Level · Reading | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-l1-fixed-income-defining-elements.md) | Fixed-Income Securities: Defining Elements | L1 · R42 | Indenture, covenants, credit enhancement, option owners, convertibles |
| [ch02](chapters/ch02-l1-fixed-income-markets-issuance-trading-funding.md) | Fixed-Income Markets: Issuance, Trading, Funding | L1 · R43 | Issuance mechanisms, single-price auction, repo, CP, structured notes |
| [ch03](chapters/ch03-l1-intro-fixed-income-valuation.md) | Introduction to Fixed-Income Valuation | L1 · R44 | Spot pricing, flat/full price, yield measures, forwards, spread ladder |
| [ch04](chapters/ch04-l1-asset-backed-securities.md) | Introduction to Asset-Backed Securities | L1 · R45 | SPE, tranching, PSA/SMM, CMO, PAC, CMBS, CDO |
| [ch05](chapters/ch05-l1-fixed-income-risk-and-return.md) | Understanding Fixed-Income Risk and Return | L1 · R46 | Duration, convexity, duration gap, effective/key rate duration |
| [ch06](chapters/ch06-l1-fundamentals-of-credit-analysis.md) | Fundamentals of Credit Analysis | L1 · R47 | Expected loss, four Cs, ratios, notching, HY and sovereign |
| [ch07](chapters/ch07-l2-term-structure-and-interest-rate-dynamics.md) | Term Structure and Interest Rate Dynamics | L2 · R28 | Forwards, bootstrapping, rolldown, swap curve, KRD, theories |
| [ch08](chapters/ch08-l2-arbitrage-free-valuation-framework.md) | Arbitrage-Free Valuation Framework | L2 · R29 | Binomial tree, calibration, Monte Carlo, CIR/Vasicek/Ho–Lee |
| [ch09](chapters/ch09-l2-bonds-with-embedded-options.md) | Valuation of Bonds with Embedded Options | L2 · R30 | Callable/putable on tree, OAS, effective duration, convertibles |
| [ch10](chapters/ch10-l2-credit-analysis-models.md) | Credit Analysis Models | L2 · R31 | CVA table, hazard rate, migration, structural vs reduced-form |
| [ch11](chapters/ch11-l2-credit-default-swaps.md) | Credit Default Swaps | L2 · R32 | Upfront, settlement, basis, index, curve trades |
| [ch12](chapters/ch12-l3-overview-fixed-income-portfolio-management.md) | Overview of Fixed-Income Portfolio Management | L3 · R11 | Mandates, return decomposition, leverage, liquidity, tax |
| [ch13](chapters/ch13-l3-liability-driven-and-index-based-strategies.md) | Liability-Driven and Index-Based Strategies | L3 · R12 | Immunization, overlays, DB pension LDI, indexing |
| [ch14](chapters/ch14-l3-yield-curve-strategies.md) | Yield Curve Strategies | L3 · R13 + 2020 refresher | Rolldown, carry, steepener, butterfly, condor, cross-currency |
| [ch15](chapters/ch15-l3-credit-strategies.md) | Fixed-Income Active Management: Credit Strategies | L3 · R14 | OAS, DTS, excess spread, factors, CDS strategies |

## Topic Index
- **Accrued interest** → ch03
- **Arbitrage (value additivity, dominance)** → ch08
- **Asset swap spread** → ch15
- **Auction (single-price)** → ch02
- **Barbell / bullet / ladder** → ch13, ch14
- **Basis (CDS–bond)** → ch11, ch15
- **Binomial tree / calibration** → ch08, ch09
- **Bootstrapping** → ch07, ch08
- **Butterfly / condor** → ch14
- **Callable / putable bonds** → ch01, ch09
- **Carry trade** → ch14
- **Cash flow matching** → ch13
- **CDS (pricing, upfront, settlement)** → ch11
- **CMBS / CDO** → ch04
- **CMO / PAC / sequential** → ch04
- **Commercial paper** → ch02
- **Convertible bonds** → ch01, ch09
- **Convexity** → ch05, ch09
- **Covenants** → ch01, ch06
- **Covered bonds** → ch01, ch10
- **Credit enhancement** → ch01, ch04
- **Credit migration** → ch06, ch10
- **CVA / hazard rate** → ch10, ch11
- **Day count** → ch03
- **Discount margin / FRN** → ch01, ch03, ch10
- **DTS / spread duration** → ch12, ch15
- **Duration (Macaulay, modified, effective, key rate)** → ch05, ch07, ch09
- **Embedded options** → ch01, ch09
- **Expected loss / PD / LGD** → ch06, ch10
- **Forward rates** → ch03, ch07
- **High yield** → ch06, ch15
- **IBOR / SOFR** → ch02, ch07
- **Immunization** → ch13
- **Indexing** → ch13
- **Inflation-linked bonds** → ch01
- **Leverage / repo** → ch02, ch12
- **Liability-driven investing** → ch13
- **Liquidity** → ch02, ch12
- **Money market yields** → ch02, ch03
- **Monte Carlo** → ch08
- **OAS / Z-spread / I-spread / G-spread** → ch03, ch09, ch15
- **Prepayment (CPR, SMM, PSA)** → ch04
- **Ratings / notching** → ch06
- **Repo** → ch02
- **Rolldown** → ch07, ch14
- **Securitization / SPE** → ch04
- **Sovereign credit** → ch06, ch15
- **Spot rates / par curve** → ch03, ch07
- **Steepener / flattener** → ch14
- **Structural vs reduced-form models** → ch10
- **Structured notes** → ch02, ch14
- **Swap curve / swap spread** → ch07
- **Swaption collar / futures overlay** → ch13
- **Term structure theories** → ch07
- **Term structure models (CIR, Vasicek, Ho–Lee)** → ch08
- **Tracking error** → ch12, ch13
- **VaR / CVaR** → ch15
- **Yield curve level/slope/curvature** → ch07, ch14
- **YTM / yield-to-worst** → ch03, ch05

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, exam traps

---

## Related Skills
- `tuckman-fixed-income` — practitioner depth: curve construction, DV01 hedging, futures CTD, swaps, repo, mortgages, CDS
- `ilmanen-yield-curve` — forward-rate analysis, bond risk premium, convexity bias, curve trade frameworks
- `ecb-yield-curve-modelling` — Nelson–Siegel and curve-fitting models
- `cfa-derivatives` — forwards, swaps, futures, option strategies, currency management behind the overlays
- `hull-derivatives` — short-rate models, credit derivatives, interest-rate derivatives
- `cfa-portfolio-management` — indexes, VaR, performance and risk frameworks
- `cfasi-fixed-income-guides` — practitioner (Italian-source) fixed income and unconstrained bond strategies
- `cfa-level1-curriculum` — personal L1 revision notes on the same readings
- `cfa-economics` — monetary policy and exchange-rate drivers of rates

## Scope & Limits
Covers the CFA fixed income readings listed above, in the 2020 (L1), 2022 (L2) and 2023 (L3) curricula; check the current learning outcome statements before relying on a specific exam. Data points (rating studies, CDS market sizes, Libor transition status) are as of the readings. L2 errata for R30 applied; source typos corrected in place and flagged ⚠ Correction. Practice problems are summarized, not reproduced. Not covered: L2 R33+ derivatives (see `cfa-derivatives`), full Level III portfolio construction, ethics.
