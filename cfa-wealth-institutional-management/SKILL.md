---
name: cfa-wealth-institutional-management
description: "CFA Program Level III (2023) wealth and institutional management: private wealth overview, taxes and estate, risk management for individuals, institutional investors, and three case studies (endowment portfolio management, household risk across life stages, sovereign wealth fund risk). Use when building a private client IPS, sizing life or disability insurance, analyzing capital sufficiency, tax-aware allocation, concentrated positions, estate planning, DB pension funded status, endowment spending rules, SWF types, bank or insurer equity duration, liquidity budgets, time-to-cash, commitment pacing, illiquidity premium, unsmoothing, TAA overlays with futures or total return swaps, rebalancing, ESG integration, or a CFA Level III quiz on these readings."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Wealth and Institutional Management (Level III)
**Source**: CFA Program Curriculum 2023, Level III, Portfolio Management: R21-R24 (private wealth and institutions), R28-R30 (case studies) | **Domain**: Gestion de portefeuille | **Chapters**: 7 | **Generated**: 2026-10-05

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch05`
- **Browse** — "what chapters do you have?"
- **Exam mode** — ask for a quiz on a chapter; I build it from its Worked Example and Exam Focus & Traps sections.

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering. The three case-study chapters are written as playbooks (situation → analysis → decision → why).

---

## Core Frameworks & Mental Models

**Private clients (ch01-ch03)**
- **Intake to IPS** (ch01): information set (personal, financial, tax, other) → quantified, ranked goals → risk tolerance as the lower of willingness and capacity, goal by goal → capital sufficiency (Monte Carlo, 75%-90% success, check shortfall size) → six-part IPS → threshold rebalancing and annual review. Goals-based aggregate can sit off the total-portfolio frontier.
- **After-tax measurement** (ch02): `R' = (V1 − V0 + income − tax)/V0`; `TER = R'/R` (breaks for negative returns); post-liquidation return deducts `embedded gain × t`; `tax alpha = (R'−B') − (R−B)`. Accounts: taxable `(1+R(1−t))^n`, deferred `(1+R)^n(1−t)`, exempt `(1+R)^n`.
- **Asset location and decumulation** (ch02): tax-efficient assets taxable, tax-inefficient sheltered; spend taxable first at a flat rate; fill low brackets first under progressive tax. SMA/ETF, HIFO or specified lots, year-round loss harvesting (wash sale 30 days) with substitutes.
- **Concentrated positions** (ch02): six routes (sell, staged with completion portfolio, collar plus loan, exchange fund, charitable, deferral or step-up); the baseline is sell-and-diversify; avoid a hedge that is a constructive sale.
- **Gift vs bequest** (ch02): `RV = [1+r_g(1−t_g)]^n / ([1+r_e(1−t_e)]^n(1−T_e))`; equal returns give 1/(1−T_e). Match trusts, foundations, insurance and governance to control, protection and tax goals.
- **Economic balance sheet** (ch03, ch06): human capital `Σ p(s_t) w_t / (1+r_f+y)^t` as a bond-like asset; financial portfolio is the completion portfolio; keep it uncorrelated with the earner's job.
- **Insurance sizing** (ch03, ch06): disability = PV (annuity due, rate `(1+r)/(1+g)−1`) of net pay minus state benefit; life = human life value and needs analysis, choose inside the range; retain small risks (six-month buffer); re-run at each life event.

**Institutional investors (ch04)**
- **IPS checklist**: stakeholders, liabilities, horizon, liquidity, constraints; risk measure by type (DB surplus volatility, SWF loss probability, endowment total return volatility, bank/insurer VaR and stress).
- **Four operating models**: Norway (passive, cheap), Endowment (alternatives, outsourced), Canada (reference portfolio plus total portfolio approach, internal), LDI (hedging plus growth portfolio). Pick the one the organization can run.
- **DB plans**: manage the surplus; risk tolerance rises with funded ratio, sponsor strength, low sponsor-plan correlation, young workforce; higher discount rate lowers liabilities (cosmetic).
- **Endowment spending**: `S = w·S_prev(1+π) + (1−w)·s·AUM_avg`; test expected real return against the spending rate before choosing a mix; liquidity band `(illiquid NAV + uncalled)/AUM`.
- **SWF types**: stabilization (liquid), reserve (50%-70% equity), savings and pension reserve (growth and alternatives), development (mandate).
- **Bank and insurer leverage**: `ΔE/E = (A/E)(ΔA/A) − ((A/E)−1)(ΔL/L)`; equity duration `(A/E)D_A − ((A/E)−1)D_L(Δi/Δy)`; equity variance subtracts the covariance term.

**Case-study playbooks (ch05-ch07)**
- **Liquidity budget and stress** (ch05, ch07): cumulative time-to-cash minimums (10/35/50, illiquid cap 50 in the case), vehicle-level profiling, stress of calls, gates and smoothing, five-step plan (parameters, assessment, cash-flow model, stress, emergency plan).
- **More illiquids** (ch05): unsmoothed, net-of-fee inputs; Monte Carlo on purchasing power; approve if volatility is inside tolerance and the stressed liquidity budget holds; phase in by commitment pacing. Unsmoothing: `r* = (r_t − ρr_{t−1})/(1−ρ)` or a public proxy.
- **Overlay vehicle** (ch05): total bp cost = commission + spread + impact + fee + mispricing + roll + funding; leverage term = borrowed share × (Libor + spread) for ETF, × Libor for futures and TRS; case: ETF 35 vs futures 42 vs TRS 51 unlevered, futures 192 vs ETF 222.5 at 4x.
- **Rebalancing** (ch05): derivatives for small, temporary, fast moves (24 vs 30 bp for 0.5%); cash managers for large, permanent ones (60 vs 82 bp for 2.5%); illiquids by commitment pacing.
- **Conflicted manager search** (ch05): disclose, recuse, verify returns; Standards I(B), I(C), III(D), III(E), IV(A), V(A), VI(A).
- **Household stage loop** (ch06): re-run balance sheet, risk list and cover at 28, 45, 55, 65; goals-based sub-portfolios (care goal in inflation-linked bonds, bequest in equities); annuity vs lump sum vs stay invested.
- **Direct investing risk review** (ch07): seven lenses of risk; scenario analysis with a conditional action plan; climate (physical, transition, opportunity) and social risks; reputational materiality does not scale with size; distressed minority playbook (engage, lobby, redesign incentives, deadline, exit).

---

## Chapter Index
| # | Title | Level · Reading | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-l3-overview-private-wealth-management.md) | Overview of Private Wealth Management | L3 · R21 | Client information set, risk tolerance, Monte Carlo sufficiency, six-part IPS, goals-based investing |
| [ch02](chapters/ch02-l3-topics-in-private-wealth-management.md) | Topics in Private Wealth Management | L3 · R22 | TER and tax alpha, asset location, tax lots, concentrated positions, gift vs bequest, trusts, family governance |
| [ch03](chapters/ch03-l3-risk-management-for-individuals.md) | Risk Management for Individuals | L3 · R23 | Economic balance sheet, human capital, human life value vs needs analysis, annuities, total-wealth allocation |
| [ch04](chapters/ch04-l3-institutional-investors.md) | Portfolio Management for Institutional Investors | L3 · R24 | IPS by type, four models, DB funded status, spending rules, SWF types, bank/insurer equity duration |
| [ch05](chapters/ch05-l3-case-study-institutional-portfolio-management.md) | Case Study in Portfolio Management: Institutional | L3 · R28 | Liquidity budget, illiquidity premium, TAA vehicle choice, rebalancing, manager ethics, ESG integration |
| [ch06](chapters/ch06-l3-case-study-risk-management-private-wealth.md) | Case Study in Risk Management: Private Wealth | L3 · R29 | Stage playbooks, insurance sizing, concentration fix, goals-based sub-portfolios, decumulation |
| [ch07](chapters/ch07-l3-integrated-cases-risk-management-institutional.md) | Integrated Cases in Risk Management: Institutional | L3 · R30 | Seven risk lenses, unsmoothing, five-step liquidity plan, direct deals, climate and social risk, ERM review |

## Topic Index
- **Active risk budget** → ch05
- **Annuity vs lump sum, indexed annuity** → ch03, ch06
- **Asset location** → ch01, ch02
- **Bank and insurer balance sheet, equity duration** → ch04
- **Capital sufficiency, Monte Carlo** → ch01, ch07
- **Climate risk (physical, transition)** → ch07
- **Commitment pacing** → ch05, ch07
- **Concentrated positions, collar, exchange fund** → ch02
- **Currency risk in frontier markets** → ch07
- **DB and DC pension plans, funded ratio** → ch04
- **Decumulation, retirement drawdown** → ch02, ch03, ch06
- **Denominator effect** → ch07
- **Direct vs fund investing** → ch07
- **Disability insurance sizing** → ch03, ch06
- **ESG integration, engagement, divestment** → ch05, ch07
- **Endowment and foundation spending rules** → ch04, ch05
- **Enterprise risk management** → ch07
- **Estate planning, trusts, foundations** → ch02
- **Family governance** → ch02
- **Goals-based investing** → ch01, ch06
- **Human capital** → ch03, ch06
- **Illiquidity premium** → ch05
- **IPS (private and institutional)** → ch01, ch04
- **Leverage and overlay cost** → ch05
- **Life insurance, human life value, needs analysis** → ch03, ch06
- **Liquidity budget, time-to-cash** → ch05, ch07
- **Liquidity management plan** → ch07
- **Longevity risk** → ch01, ch03, ch06
- **Manager selection ethics, GIPS benchmark fees** → ch05
- **Operating models (Norway, Endowment, Canada, LDI)** → ch04
- **Rebalancing bands and corridors** → ch05
- **Reputational risk** → ch05, ch07
- **Risk tolerance and capacity** → ch01
- **Santiago Principles** → ch04
- **Scenario analysis** → ch07
- **Social risks, just transition** → ch07
- **Sovereign wealth funds** → ch04, ch07
- **Tactical asset allocation overlay** → ch05
- **Tax lots, loss harvesting, wash sale** → ch02
- **Tax-efficiency ratio, tax alpha, post-liquidation return** → ch02
- **Total return swap vs futures vs ETF** → ch05
- **Total-wealth asset allocation** → ch03
- **Universal ownership** → ch07
- **Unsmoothing returns** → ch05, ch07

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, exam traps

---

## Related Skills
- `cfa-portfolio-management` — portfolio planning, risk management intro, manager selection, performance evaluation behind the IPS and monitoring steps
- `cfa-asset-allocation-cme` — capital market expectations, asset allocation principles and real-world constraints that feed the IPS
- `cfa-alternative-investments` — private equity, hedge fund and real asset mechanics behind illiquid allocations
- `cfa-derivatives` — futures, swaps, collars and currency tools used in overlays and monetization
- `cfa-fixed-income` — liability-driven investing and duration matching for DB plans, banks and insurers
- `cfa-ethics-gips` — Standards of Professional Conduct and GIPS cited in the manager-selection case
- `cfa-quantitative-methods` — annuity, growing-annuity and Monte Carlo arithmetic

## Scope & Limits
Covers CFA Level III 2023 Portfolio Management readings R21-R24 and R28-R30 only; other Level III readings (asset allocation, CMEs, trading, performance, ethics) are in sibling skills. Tax figures are from the curriculum's illustrative jurisdictions (US, UK, Eurolandia) and are not current tax advice. Case numbers are the curriculum's hypothetical data; a few source inconsistencies and one derived breakeven are flagged in the chapters. Two source charts (unsmoothing exhibits) were not machine-readable and are described without exact values.
