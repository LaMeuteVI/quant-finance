---
name: cfasi-fixed-income-guides
description: "CFA Society Italy x Advisor Private practitioner guides 'Fixed Income' (2018, 11 chapters) and 'Unconstrained Fixed Income' (2019, 6 chapters), translated from Italian: bond features, risks, issuer types, market structure, curves and spreads, valuation, ways to invest, immunization and index management, unconstrained and income funds, emerging market debt, IG and HY credit, convertibles, AT1/Tier 2/hybrids, EM local currency, private debt. Use when analysing or selecting bonds and bond funds, or when asked about duration, convexity, Z-spread, OAS, yield to worst, immunization, tracking error, fund selection, AT1 coupon risk, CDS basis, spread duration, convertible delta, carry trade, private debt covenants, ELTIF."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Society Italy Fixed Income Guides (Fixed Income + Unconstrained Fixed Income)
**Source**: CFA Society Italy x Advisor Private guides: "Fixed Income" (May-June 2018) and "Unconstrained Fixed Income" (Sept-Oct 2019), by eight Italian CFA charterholders and practitioners | **Domain**: Gestion de portefeuille | **Chapters**: 17 | **Generated**: 2026-10-05

## How to Use This Skill
- **Without arguments**: load the core frameworks below.
- **With a topic**: ask about `<topic>`; I read the relevant chapter before answering.
- **With a chapter**: ask for `ch09`.
- **Browse**: "what chapters do you have?"

When a topic is not covered in Core Frameworks, I read the relevant chapter file before answering. Chapters ch01-ch11 come from the Fixed Income guide, ch12-ch17 from the Unconstrained Fixed Income guide.

---

## Core Frameworks & Mental Models

**Bond mechanics and risk**
- **Contract decomposition** (ch01): par, coupon type (fixed, zero, floater, reverse floater, linker, step), principal schedule, currency, seniority, options (call, put, conversion, CoCo), covenants; read the indenture first.
- **Risk map** (ch02): rate, curve, credit (default, spread, downgrade), call, reinvestment, liquidity, currency, volatility (callable loses when vol rises, putable gains), event/legal, inflation. Longer maturity, lower coupon, lower yield raise rate sensitivity; calls and puts reduce it.
- **Coupon vs yield rule** (ch02, ch06): coupon = yield: par; coupon < yield: discount.

**Valuation**
- **Yield selector** (ch06): current yield (screen), YTM (hold to maturity, reinvest at YTM), yield to worst (callables), real yield and breakeven (linkers), discount margin (floaters).
- **Spot-forward arbitrage-free pricing** (ch05, ch06): bootstrap spots, `(1+S2)² = (1+S1)(1+1f2)`, price each cash flow at its spot. (A source forward-rate error is corrected in ch06.)
- **Spread ladder** (ch05): nominal spread, Z-spread (curve), OAS (options), ASW; `option cost = Z − OAS`.
- **Duration-convexity** (ch06, ch08): `ΔP/P ≈ −MD Δy + ½ C Δy²`; key rate durations capture non-parallel moves; callables show negative convexity.
- **Term structure theories** (ch05): expectations, liquidity preference, segmentation; curve shape signals the cycle.
- **Convertible = bond floor + call** (ch06, ch14): parity, premium, payback period; delta from 0 (busted) to 100% (quasi-equity); balanced zone near 50%.

**Portfolio management**
- **Immunization** (ch08): cash flow matching, duration matching, derivatives overlay, contingent immunization; liabilities typed by amount/timing.
- **Index replication by risk factors** (ch08): duration, KRDs, sector, quality, issuer caps; tracking error.
- **Bottom-up vs top-down active** (ch08): relative value within homogeneous credit buckets vs macro tilts.
- **Route to bonds** (ch07): size x selection capability matrix; four-cost comparison single bond vs ETP.
- **Fund due diligence** (ch07, ch09): quantitative (risk-adjusted, stress windows, regression, correlation matrices) plus qualitative (team, process, limits, duration decomposition, style drift, capacity, fees).
- **Income fund test** (ch10): distribution yield vs portfolio income; payout is a feature, income is an objective.

**Credit and special segments**
- **Rates vs spread** (ch12): since 2009 spread is >100% of euro IG index yield; rate rises can be offset by spread compression; curve trades (steepener, flattener) are duration-neutral.
- **HY spread formula** (ch13): `spread = PD × (1 − recovery) + excess spread`; spread duration with mean-reversion bands; CDS basis `CDS − Z`; sovereign vs quasi-sovereign pairs.
- **Capital stack and hybrid risks** (ch03, ch15): CET1, AT1, Tier 2, senior non-preferred, senior preferred; bail-in, extension, conversion, coupon cancellation; reset spread logic for non-calls.
- **EM local valuation** (ch16): MM, MM2Y, 2Y10Y from a risk factor (10Y spread − 5Y CDS − inflation differential); carry trade and UIP/CIP.
- **Private debt** (ch17): senior/structured/direct lending, covenants and pricing ratchets, six-step fund process, ELTIF.
- **EM risk families** (ch11): sovereign, political, economic, transfer, currency, position, liquidity.

---

## Chapter Index
| # | Title | Guide · Chapter | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-fi-bond-characteristics.md) | Main Characteristics of Fixed Income Securities | FI · 1 | Contract decomposition, coupon taxonomy, breakeven, call structures |
| [ch02](chapters/ch02-fi-main-risks.md) | The Main Risks of Fixed Income Securities | FI · 2 | Risk map, rate-sensitivity drivers, volatility-option rule |
| [ch03](chapters/ch03-fi-bond-types-overview.md) | Overview of Fixed Income Securities Types | FI · 3 | Issuer classification, HY, hybrids, bank capital stack, covered bonds |
| [ch04](chapters/ch04-fi-bond-market-structure.md) | The Fixed Income Market: Peculiarities | FI · 4 | Auctions, bookbuilding, liquidity checklist, negative-yield regime |
| [ch05](chapters/ch05-fi-yield-curve-and-spreads.md) | The Yield Curve and Spread Types | FI · 5 | Term structure theories, nominal/Z/OAS/ASW spreads |
| [ch06](chapters/ch06-fi-bond-valuation.md) | Introduction to Fixed Income Valuation | FI · 6 | Yield measures, bootstrapping, duration/convexity, credit 4 Cs, convertibles |
| [ch07](chapters/ch07-fi-ways-to-invest.md) | The Different Ways of Investing in Fixed Income | FI · 7 | Route matrix, replication, mandate types, due diligence, amortized cost |
| [ch08](chapters/ch08-fi-active-passive-portfolio-management.md) | Active and Passive Portfolio Management | FI · 8 | Immunization, KRD replication, tracking error, bottom-up/top-down |
| [ch09](chapters/ch09-fi-unconstrained-products.md) | Unconstrained Fixed Income Products | FI · 9 | Fund vs bond, UCITS origins, duration decoding, selection and monitoring |
| [ch10](chapters/ch10-fi-coupon-income-products.md) | Coupon (Income) Products | FI · 10 | Payout source, hidden risk check, reinvestment |
| [ch11](chapters/ch11-fi-emerging-market-bonds.md) | Emerging Market Bonds | FI · 11 | EM tiers, seven risk families, risk-return table |
| [ch12](chapters/ch12-unconstrained-rates-and-ig-corporates.md) | Interest Rates and IG Corporate Bonds | UFI · 1 | Term premium, curve trades, spread vs rate returns |
| [ch13](chapters/ch13-unconstrained-high-yield-credit.md) | The High Yield Credit Market | UFI · 2 | Credit spread formula, spread duration, CDS, pair trades |
| [ch14](chapters/ch14-unconstrained-convertible-bonds.md) | Convertible Bonds | UFI · 3 | Delta regimes, gamma trade, prospectus protections |
| [ch15](chapters/ch15-unconstrained-bank-subordinated-and-hybrids.md) | Bank Subordinated Debt and Hybrids | UFI · 4 | Tier 2/AT1 risks, DB 2016, Santander 2019 |
| [ch16](chapters/ch16-unconstrained-em-local-currency.md) | EM Local Currency Bonds | UFI · 5 | Building-block curve, carry trade, UIP/CIP |
| [ch17](chapters/ch17-unconstrained-private-debt.md) | Private Debt | UFI · 6 | Segments, covenants, fund process, ELTIF |

## Topic Index
- **ABS / covered bonds** → ch03
- **Active vs passive** → ch07, ch08
- **Amortized cost (segregated accounts)** → ch07
- **AT1, CoCo, Tier 2** → ch03, ch15
- **Auctions, bookbuilding, grey market** → ch04
- **Bail-in, TLAC, senior non-preferred** → ch03, ch15
- **Benchmarks, index replication** → ch07, ch08
- **Bid-ask spread, liquidity** → ch02, ch04, ch13
- **Bond floor, parity, convertibles** → ch06, ch14
- **Bootstrapping, spot, forward rates** → ch05, ch06
- **Breakeven inflation, linkers** → ch01, ch06
- **Callable, putable, negative convexity** → ch02, ch06
- **Carry trade, UIP, CIP, NDF** → ch16
- **CDS, XOVER, CDX, basis** → ch13
- **Coupon vs distributing funds, Income funds** → ch10
- **Credit analysis, four Cs** → ch06, ch13
- **Credit spread decomposition** → ch13
- **Currency risk** → ch02, ch11, ch16
- **Curve trades (steepener/flattener)** → ch12
- **Default and recovery rates** → ch13
- **Duration, convexity, KRD** → ch06, ch08
- **ELTIF, private debt** → ch17
- **Emerging markets (hard, local)** → ch11, ch13, ch16
- **ETFs and ETPs** → ch07
- **Fallen angels, rising stars** → ch03, ch13
- **Floaters, discount margin** → ch01, ch06
- **Fund selection and monitoring** → ch07, ch09
- **High yield** → ch03, ch13
- **Hybrids (corporate)** → ch03, ch15
- **Immunization (ALM)** → ch08
- **Inflation-linked bonds** → ch01, ch03, ch06
- **Liquid Alternatives, UCITS** → ch09
- **Mini-bonds, private placements** → ch03, ch17
- **OAS, Z-spread, ASW** → ch05
- **Quantitative easing, negative rates** → ch04, ch12
- **Rating scale, outlook** → ch02, ch06, ch12
- **Reinvestment risk** → ch02, ch10
- **Spread duration** → ch13
- **Term premium** → ch12, ch16
- **Term structure theories** → ch05
- **Tracking error** → ch07, ch08
- **Unconstrained funds** → ch09
- **Yield measures (YTM, YTW, current)** → ch06

## Supporting Files
- [glossary.md](glossary.md): key terms with definitions
- [patterns.md](patterns.md): techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md): decision rules, thresholds, tells

---

## Related Skills
- `cfa-fixed-income`: use for the CFA curriculum treatment (duration, credit, securitization, curves) when exam-grade formulas or Level II detail are needed.
- `tuckman-fixed-income`: use for rigorous term-structure models, KRD hedging, swaps and futures.
- `ilmanen-yield-curve`: use for term premium, carry and curve-trade evidence.
- `ecb-yield-curve-modelling`: use for curve fitting and euro-area curve estimation.
- `cfa-alternative-investments`: use for private debt, hedge fund strategies behind Liquid Alternatives.
- `cfa-portfolio-management` and `cfa-wealth-institutional-management`: use for liability-driven investing and income planning.
- `hull-derivatives` and `cfa-derivatives`: use for CDS, forwards, NDFs and option Greeks behind ch13, ch14, ch16.
- `cfasi-portfolio-construction`: use for fund selection and portfolio design context.

## Scope & Limits
Covers two Italian practitioner guides published by CFA Society Italy with Advisor Private (2018 and 2019), translated to English with Italian named terms kept where useful. Market data, yields and examples are dated (2017-2019) and illustrate mechanisms, not current levels. Sponsored inserts ("Uno sguardo al futuro obbligazionario", "Serenita in un contesto sfidante") are summarized briefly and attributed, not treated as neutral analysis. Source corrections found are flagged in chapters (forward-rate formula, rating table, duration table, option decomposition rounding). Chapter 6 formulas and some tables were reconstructed from garbled PDF text; all worked examples are recomputed. Retail suitability is outside scope; the guides are informational, not investment advice.
