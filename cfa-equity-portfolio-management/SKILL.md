---
name: cfa-equity-portfolio-management
description: "CFA Level III 2023 Equity Portfolio Management (R15-R18): overview, passive investing, active strategies, active portfolio construction. Use when asked about equity segmentation, securities lending and fees, index weighting schemes, HHI, full replication vs stratified sampling vs optimization, tracking error, equitizing cash with futures or swaps, smart beta, fundamental vs quantitative investing, bottom-up and top-down strategies, value and growth traps, GARP, information coefficient, pairs trading, merger arbitrage, activism, style analysis, active return decomposition, Active Share vs active risk, closet indexer, fundamental law of active management, transfer coefficient, risk budgeting, 130/30, long/short, market neutral, capacity, or when preparing a CFA equity portfolio management quiz."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Equity Portfolio Management (Level III)
**Source**: CFA Program Curriculum 2023, Level III, Portfolio Management R15-R18 | **Domain**: Gestion de portefeuille | **Chapters**: 4 | **Generated**: 2026-10-05

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch03`
- **Browse** — "what chapters do you have?"
- **Exam mode** — ask for a quiz on a chapter; I build it from its Worked Example and Exam Focus sections.

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Setting the mandate**
- **Four roles of equities** (ch01): capital appreciation, dividend income, diversification, partial inflation hedge; diversification fades in crises.
- **Segmentation follows the thesis** (ch01): size/style, geography, economic activity; GICS is market-oriented, ICB/TRBC/RGS production-oriented.
- **Net-of-everything view** (ch01): net return = gross − management − performance − admin − trading costs (+ lending income). Alpha must clear all of it; high-water mark prevents paying twice.
- **Passive-active spectrum** (ch01): confidence to outperform, client preference, benchmark suitability, mandate, risks/costs, taxes.

**Passive investing**
- **Usable index** (ch02): rules-based, transparent, investable. Default weighting is float-adjusted cap; check concentration with `1/HHI`.
- **Non-cap weights are factor bets** (ch02): equal, fundamental, min-variance, dividend, multi-factor carry size/value tilts, crowding and cost.
- **Construction** (ch02): full replication (liquid, large mandate) → stratified sampling (many names, small AUM) → optimization (min TE, needs total-vol constraint); blended for cap-spanning indexes. TE is U-shaped in holdings.
- **Control tracking error** (ch02): market-on-close, net flows, equitize cash (futures, ETFs, swaps), beta near 1.0. Contracts = exposure / (multiplier × futures price).
- **Securities lending** (ch01, ch02): fee plus collateral reinvestment; borrower gets votes; collateral risk is the real exposure.

**Active strategies**
- **Fundamental vs quantitative** (ch03): judgment, depth, ~50 names, company risk vs systematic, breadth, ~400 names, factor risk.
- **Seven-step fundamental process** (ch03): thesis, prescreen, industry/financial analysis, forecast, valuation, construction, rebalance with sell discipline.
- **Value and growth have traps** (ch03): no catalyst = value trap; priced-in growth = growth trap. GARP uses `PEG = P/E ÷ growth%`.
- **Quant hygiene** (ch03): point-in-time data, delisted names, Spearman rank IC, quantile spread, out-of-sample, costs, crowding.
- **Event and arbitrage** (ch03): pairs spread `ln(P_A/P_B)` entered at ±2σ; merger arbitrage earns deal spread with failure risk; activism targets slow, weakly governed firms (<10% stake).
- **Style analysis** (ch03): holdings-based (current, bottom-up) and returns-based (Sharpe 1992 regression); use both.

**Active portfolio construction**
- **Active return decomposition** (ch04): `R_A = Σ ΔW·R = Σ(β_p − β_b)F + α + ε`. Factor-explained return is alternative beta.
- **Four building blocks** (ch04): factor weights, alpha skills, position sizing, breadth.
- **Fundamental law** (ch04): `E(R_A) = IC × √BR × σ_RA × TC`; BR counts independent decisions; long-only TC ~0.25-0.6.
- **Active Share vs active risk** (ch04): `AS = ½ Σ|Δw|`. Closet: AS ~0.25, TE <2%. Multi-factor: ~0.7, ~3%. Stock picker: >0.9, 8-12%+.
- **Risk budgeting** (ch04): absolute measures for absolute-return mandates, active risk for benchmark-relative; budget only where skill exists. Risk contribution `CV_i = x_i·C_ip`.
- **Relaxing long-only** (ch04): 130/30 (net 100, gross 160), long/short, equitized market neutral raise TC at cost of borrow, collateral, recall and fees.
- **Capacity** (ch04): AUM forces more names, larger caps, slower turnover; leverage optimum ≈ (R_a − funding)/σ².

---

## Chapter Index
| # | Title | Level · Reading | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-l3-overview-equity-portfolio-management.md) | Overview of Equity Portfolio Management | L3 · R15 | Roles of equities, segmentation, income and cost ledger, engagement, passive-active spectrum |
| [ch02](chapters/ch02-l3-passive-equity-investing.md) | Passive Equity Investing | L3 · R16 | Index weighting, HHI, replication/sampling/optimization, tracking error, futures and swaps, lending |
| [ch03](chapters/ch03-l3-active-equity-strategies.md) | Active Equity Investing: Strategies | L3 · R17 | Fundamental vs quant, value/growth/GARP, factor tests and IC, stat arb, activism, style analysis |
| [ch04](chapters/ch04-l3-active-equity-portfolio-construction.md) | Active Equity Investing: Portfolio Construction | L3 · R18 | Return decomposition, fundamental law, Active Share vs active risk, risk budgeting, 130/30, capacity |

## Topic Index
- **Active return decomposition, alternative beta** → ch04
- **Active Share, closet indexer** → ch01, ch04
- **Activist investing, defenses** → ch01, ch03
- **Authorized participant, ETFs** → ch02
- **Back-test, survivorship, look-ahead bias** → ch03
- **Behavioral biases (discretionary)** → ch03
- **Benchmark selection** → ch02
- **Breadth, fundamental law, transfer coefficient** → ch04
- **Buffering, packeting, reconstitution** → ch02
- **Capacity, slippage, AUM** → ch04
- **Cash drag, equitizing** → ch02
- **Covered call, cash-covered put, dividend capture** → ch01
- **Equity swap, futures overlay, basis risk** → ch02
- **Event-driven, merger arbitrage** → ch03
- **Factor tilt, smart beta, fundamental indexation** → ch02, ch03
- **Fees, performance fee, high-water mark** → ch01
- **Free-float adjustment, weighting schemes, HHI** → ch02
- **Information coefficient** → ch03, ch04
- **Leverage and volatility drag** → ch04
- **Long extension 130/30, long/short, market neutral** → ch04
- **Pairs trading, statistical arbitrage** → ch03
- **Passive-active spectrum** → ch01
- **Return attribution (sector)** → ch02
- **Risk budgeting, risk contribution, VaR, CVaR** → ch04
- **Securities lending, specials, empty voting** → ch01, ch02
- **Segmentation, GICS, style box** → ch01, ch03
- **Style analysis (holdings, returns-based)** → ch03
- **Top-down vs bottom-up** → ch03, ch04
- **Tracking error** → ch02, ch04
- **Value trap, growth trap, GARP, PEG** → ch03

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, exam traps

---

## Related Skills
- `cfa-portfolio-management` — multifactor models, fundamental law, VaR, trading costs, manager selection behind ch02-ch04
- `cfasi-equity-investment-styles` — value, factor and systematic investing practice
- `cfa-derivatives` — equity swaps and futures overlays used for equitizing
- `cfa-equity-valuation` — DCF and multiples behind the fundamental process
- `cfa-alternative-investments` — hedge fund strategies (activist, event-driven, long/short, market neutral)
- `cfa-asset-allocation-cme` — behavioral biases and risk budgeting at asset allocation level
- `pairs-trading-partial-cointegration` — formal pairs trading

## Scope & Limits
Covers the four CFA Level III 2023 equity portfolio management readings only. Check current learning outcome statements, as later curricula revise readings. Source corrections found in the chapters are flagged as Correction or clarification (fundamental law breadth example, margin percentage). Equity valuation, ETF mechanics in depth, performance evaluation and trading execution are only touched here; see the related skills.
