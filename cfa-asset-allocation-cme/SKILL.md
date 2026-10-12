---
name: cfa-asset-allocation-cme
description: "CFA Program curriculum on behavioral finance, capital market expectations and asset allocation: Level III 2023 R1-R7 plus Level II 2022 R42: behavioral biases of individuals and in investment processes, CME framework and macro analysis, forecasting asset class returns, economics and investment markets, strategic asset allocation approaches, principles of allocation, real-world constraints. Use when building capital market expectations, forecasting returns, volatility or exchange rates, choosing asset-only, liability-relative or goals-based allocation, or when asked about Taylor rule, business cycle phases, Grinold-Kroner, Singer-Terhaar, building blocks, de-smoothing, shrinkage covariance, Black-Litterman, reverse optimization, risk budgeting, economic balance sheet, rebalancing corridor, behavioral investor types, anchoring, or when preparing a CFA Level III quiz."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Asset Allocation, Capital Market Expectations and Behavioral Finance
**Source**: CFA Program Curriculum Portfolio Management: L3 2023 R1-R7, L2 2022 R42 | **Domain**: Gestion de portefeuille | **Chapters**: 8 | **Generated**: 2026-10-05

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch03`
- **Browse** — "what chapters do you have?"
- **Exam mode** — ask for a quiz on a chapter; I build it from its Worked Example and Exam Focus & Traps sections.

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Behavioral finance**
- **Cognitive vs emotional** (ch01): cognitive errors (belief perseverance, information processing) are moderated with data and records; emotional biases (loss aversion, overconfidence, self-control, status quo, endowment, regret aversion) are adapted to through plan, defaults and neutral questions. Exception: endowment when goals are at risk.
- **Bayesian lens** (ch01, ch02): conservatism overweights the prior, representativeness underweights it. `P(A|B) = [P(B|A)/P(B)]·P(A)`; a 60% analyst against a 20% base rate gives about 27%.
- **Behavioral alpha top-down** (ch02): active/passive, risk level, linked biases, type: Passive Preserver, Friendly Follower, Independent Individualist, Active Accumulator. Emotional types get goals, cognitive types get data.
- **Behavioral portfolio theory and DC findings** (ch02): layered pyramids ignore covariance; inertia, 1/n, employer stock, home bias dominate plan behavior. Committees need diversity, independence and tracked decisions.

**Capital market expectations**
- **Seven-step CME framework** (ch03): universe and horizon, history, methods, sources, interpret, document, monitor. Consistency across asset classes and horizons beats point accuracy.
- **Pitfall checklist** (ch03): survivorship, appraisal smoothing, revisions, asynchronicity, peso problem, data mining, time period, conditioning information, correlation misread, analyst biases, model uncertainty.
- **Trend-growth anchor** (ch03): potential growth = labor input + labor productivity; `V_e = GDP × S_k × PE`, so equity value tracks nominal GDP; real (nominal) yields track real (nominal) growth.
- **Cycle map and Taylor rule** (ch03, ch05): five phases with curve, policy and asset behavior; `i* = r_neutral + π_e + 0.5(Y_e − Y_trend) + 0.5(π_e − π_target)`; policy mix sets real vs nominal rate levels; cycle signal strongest at 1-3 years.
- **Pricing equation and kernel** (ch05): `P = ΣE[CF]/(1 + l + θ + π + γ + κ + φ)^s`; premiums come from negative covariance with marginal utility; BEI = θ + π.
- **Fixed-income and equity forecasts** (ch04): bond `E(R) = r_f + term + credit + liquidity`, horizon vs Macaulay duration; Grinold-Kroner `D/P + %ΔE − %ΔS + %ΔP/E`.
- **Singer-Terhaar** (ch04): `RP = φ·ρσ·SR_GM + (1−φ)·σ·SR_i`; φ 0.75-0.90 developed, 0.50-0.75 EM and real estate; add illiquidity premium.
- **Real estate, FX and volatility** (ch04): `cap rate + NOI growth − %Δcap`; PPP anchor plus current account and capital flows; de-smooth `var(r) = [(1+λ)/(1−λ)]var(R)`, shrink covariance, ARCH.

**Asset allocation**
- **Governance and economic balance sheet** (ch06): six governance elements; human capital about 70% bond-like; economic net worth = assets − liabilities.
- **Three approaches** (ch06, ch07): asset-only (volatility, Sharpe), liability-relative (surplus, funded ratio), goals-based (probability of failing each goal).
- **Asset classes and market portfolio** (ch06): five criteria; start from the global market portfolio and justify each deviation.
- **MVO and its repairs** (ch07): `U = E(R) − 0.005λσ²`; reverse optimization `μ = r_f + λΣw_mkt`, Black-Litterman, resampling; risk budget optimal when excess return per MCTR is equal.
- **Liability-relative and goals-based** (ch07): surplus optimization, hedging/return-seeking, integrated ALM; goals via minimum expectation `E(R)T − zσ√T`.
- **Rebalancing and constraints** (ch06, ch07, ch08): wider corridors for costs, taxes, illiquidity, correlation; after-tax `r(1−t)`, `σ(1−t)`, correlation unchanged, band `R/(1−t)`; screen size, liquidity, horizon, regulation before optimizing; TAA inside IPS ranges.

---

## Chapter Index
| # | Title | Level · Reading | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-l3-behavioral-biases-of-individuals.md) | The Behavioral Biases of Individuals | L3 · R1 | Cognitive vs emotional, moderate vs adapt, 15 biases |
| [ch02](chapters/ch02-l3-behavioral-finance-and-investment-processes.md) | Behavioral Finance and Investment Processes | L3 · R2 | BITs, behavioral alpha, Bayes, committees, anomalies |
| [ch03](chapters/ch03-l3-cme-framework-and-macro.md) | CME Part 1: Framework and Macro Considerations | L3 · R3 | Seven steps, pitfalls, trend growth, cycle, Taylor rule, curve |
| [ch04](chapters/ch04-l3-cme-forecasting-asset-class-returns.md) | CME Part 2: Forecasting Asset Class Returns | L3 · R4 | Grinold-Kroner, building blocks, Singer-Terhaar, FX, covariance |
| [ch05](chapters/ch05-l2-economics-and-investment-markets.md) | Economics and Investment Markets | L2 · R42 | Pricing kernel, BEI, spreads, equity premium, real estate |
| [ch06](chapters/ch06-l3-overview-of-asset-allocation.md) | Overview of Asset Allocation | L3 · R5 | Governance, economic balance sheet, three approaches, GMP, rebalancing |
| [ch07](chapters/ch07-l3-principles-of-asset-allocation.md) | Principles of Asset Allocation | L3 · R6 | MVO, Black-Litterman, risk budgeting, liability-relative, goals-based |
| [ch08](chapters/ch08-l3-asset-allocation-real-world-constraints.md) | Asset Allocation with Real-World Constraints | L3 · R7 | Constraint screen, after-tax, asset location, TAA, behavioral controls |

## Topic Index
- **Active share, tracking risk** → ch06
- **After-tax optimization, asset location** → ch08
- **Analyst biases, forecasting biases** → ch02, ch03
- **Anchoring, status quo, availability** → ch01, ch03
- **Anomalies, momentum, bubbles** → ch02
- **Appraisal smoothing, de-smoothing** → ch03, ch04
- **ARCH, volatility clustering** → ch04
- **Asset class criteria** → ch06
- **Automatic stabilizers** → ch03
- **Bayes' formula, base rate** → ch01, ch02
- **Behavioral investor types** → ch02
- **Black-Litterman, reverse optimization** → ch07
- **Break-even inflation** → ch05
- **Business cycle phases** → ch03, ch05
- **CAPE, valuation** → ch04, ch05
- **Credit spreads, credit premium** → ch04, ch05
- **Current account, capital flows** → ch03, ch04
- **Economic balance sheet, human capital** → ch06, ch07
- **Emerging market risk** → ch04
- **Exchange rate forecasting, UIP** → ch03, ch04
- **Funded ratio, surplus** → ch06, ch07
- **Global market portfolio** → ch06
- **Goals-based allocation** → ch06, ch07
- **Governance, IPS** → ch06
- **Grinold-Kroner** → ch04
- **Inflation and asset classes** → ch03, ch05
- **Investment committees** → ch02
- **Liability-relative allocation** → ch06, ch07
- **Liquidity constraint, illiquidity premium** → ch04, ch08
- **Loss aversion, overconfidence** → ch01
- **Mean-variance optimization** → ch07
- **Mental accounting, framing** → ch01, ch02
- **Monetary and fiscal policy** → ch03, ch05
- **Negative interest rates, QE** → ch03
- **Policy mix, real and nominal rates** → ch03
- **Pricing kernel** → ch05
- **Real estate cap rate** → ch04, ch05
- **Rebalancing corridors** → ch06, ch07, ch08
- **Regime change, nonstationarity** → ch03
- **Resampled optimization** → ch07
- **Risk budgeting, risk parity** → ch06, ch07
- **Seven-step CME framework** → ch03
- **Shrinkage, factor covariance** → ch04
- **Singer-Terhaar** → ch04
- **Tactical asset allocation** → ch06, ch08
- **Taylor rule** → ch03, ch05
- **Term premium** → ch04, ch05
- **Trend growth, GDP decomposition** → ch03
- **Yield curve and cycle** → ch03, ch05

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, exam traps

---

## Related Skills
- `cfa-portfolio-management` — portfolio math, market efficiency and L1-L2 foundations behind this skill
- `cfa-wealth-institutional-management` — IPS, investor types and constraints for individuals and institutions
- `cfa-fixed-income` — yield curve and liability-driven strategies behind the bond forecasts
- `cfa-economics` — business cycles, trade and exchange rates behind the macro layer
- `ilmanen-yield-curve` — term premium and bond return forecasting in depth
- `cfa-derivatives` — currency management and overlays for rebalancing and hedging
- `cfasi-portfolio-construction` — practitioner guides to allocation

## Scope & Limits
Covers L3 2023 Readings 1-7 and L2 2022 Reading 42 (no errata entry found for R42). Check current learning outcome statements, as later curricula revise readings. Source corrections found in the readings are flagged in chapters as Correction. Equity, fixed income and alternatives portfolio construction are covered by other skills; quantitative derivations are summarized, not proved.
