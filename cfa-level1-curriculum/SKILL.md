---
name: cfa-level1-curriculum
description: "Knowledge base from CFA Level I study notes (CFA Program curriculum 2019) covering Economics, Equity, Fixed Income and Derivatives readings. Use when studying for CFA Level I, reviewing elasticities, market structures, AD/AS, monetary/fiscal policy, FX parity, indexes, market efficiency, industry analysis, DDM/multiples, bond features, YTM/spot/forward rates, duration/convexity, ABS/MBS, credit analysis, or derivative instruments."
---

<!-- argument-hint: [topic, reading name, or chapter number] -->

# CFA Level I — Study Notes (Economics, Equity, Fixed Income, Derivatives)
**Author**: Personal study notes based on the CFA Institute Program Curriculum (2019) | **Pages**: ~160 | **Chapters**: 20 | **Generated**: 2026-09-29

## How to Use This Skill

- **Without arguments**: load the core formulas and frameworks below.
- **With a topic**: ask about `duration`, `Gordon growth`, `covered interest parity` and so on, and I read the relevant chapter.
- **With a chapter**: ask for `ch16` and I load that reading.
- **Browse**: ask "what chapters do you have?" to see the full index.
- **Exam mode**: ask for a quiz on a chapter and I build questions from its Worked Example and Key Takeaways.

Each chapter keeps the notes' structure. It adds verified worked examples and flags the places where the original notes contain an error (**⚠ Correction**).

---

## Core Frameworks & Formulas

**Economics**
- **Elasticity** `E = %ΔQ/%ΔP`. Total expenditure is maximized at |E| = 1. Cross-price elasticity: > 0 for substitutes, < 0 for complements. Income elasticity: > 0 for normal goods, < 0 for inferior goods (ch01).
- **Shutdown rules**: short run P < AVC, long run P < ATC. Profit-maximizing output at **MR = MC**. Monopoly price `P = MC/(1 − 1/|E|)` (ch01–02).
- **Sectoral balances** `(S − I) = (G − T) + (X − M)`. Recessionary gap → buy defensives and bonds. Inflationary gap → cyclicals and commodities. Stagflation → commodities (ch03).
- **Leading indicators predict, lagging ones confirm** (unemployment lags). Laspeyres overstates inflation; Fisher = √(L × P) (ch04).
- **Fisher effect** `i = r + πᵉ`. **Neutral rate** = trend growth + inflation target. **Fiscal multiplier** `1/[1 − c(1 − t)]` (ch05).
- **Comparative advantage** comes from opportunity cost. BOP: CA + KA + FA = 0 (ch06).
- **Covered interest parity** `F = S(1 + i_price)/(1 + i_base)`: the higher-yield currency trades at a forward discount. **Marshall–Lerner** ε_X + ε_M > 1, with a J-curve (ch07).

**Equity**
- Leverage = 1/IM. **Margin-call price** = P₀(1 − IM)/(1 − MM) (ch08).
- Price-weighted indexes favor high-priced stocks, equal-weighted favor small caps, cap-weighted favor momentum (ch09).
- **Market efficiency**: weak (technical analysis fails), semi-strong (public information is priced), strong (fails in practice) (ch10).
- **Five forces + life cycle** explain ROIC − WACC. Strategies: cost leadership vs differentiation (ch11).
- Preferred shares rank between debt and common. **ROE vs cost of equity** decides whether value is created (ch12).
- **Gordon** `V₀ = D₁/(r − g)`, with `g = b × ROE`. Justified P/E = payout/(r − g). **EV** = equity + preferred + debt − cash (ch13).

**Fixed income**
- Coupon < YTM means the bond trades at a discount. **Callable → higher yield; putable → lower yield**. Covered bonds offer dual recourse (ch14).
- **Repo** is a collateralized loan with a haircut. CP carries rollover risk (ch15).
- **Price** = PV of cash flows at spot rates. Full price = flat + AI. `(1 + z_A)^A(1 + f)^{B−A} = (1 + z_B)^B`. Spreads: G, I, Z, OAS (ch16).
- **SMM → CPR**: `1 − (1 − SMM)¹²`. PAC tranches are protected; support tranches absorb prepayment risk. CMBS use DSC and LTV (ch17).
- `%ΔP ≈ −ModDur·Δy + ½·Conv·Δy²`, with `ModDur = MacDur/(1 + r)`. Use **effective duration for bonds with options**. Horizon = MacDur immunizes (ch18).
- **EL = PD × LGD**. The four Cs. IG ≥ BBB−. Ratings lag spreads (ch19).

**Derivatives**
- Forward commitments (obligations) vs contingent claims (rights). Futures settle daily and converge to spot (ch20). **Pricing and valuation → use the `hull-derivatives` skill.**

---

## Chapter Index

| # | Reading | Area | Key Frameworks |
|---|---------|------|----------------|
| [ch01](chapters/ch01-demand-and-supply-analysis.md) | Topics in Demand and Supply Analysis | Economics | Elasticities, shutdown, scale |
| [ch02](chapters/ch02-the-firm-and-market-structures.md) | The Firm and Market Structures | Economics | Monopoly, oligopoly, Cournot, cartels |
| [ch03](chapters/ch03-aggregate-output-prices-and-growth.md) | Aggregate Output, Prices and Economic Growth | Economics | IS-LM, AD/AS, gaps, Solow |
| [ch04](chapters/ch04-understanding-business-cycles.md) | Understanding Business Cycles | Economics | Phases, schools, unemployment, indexes |
| [ch05](chapters/ch05-monetary-and-fiscal-policy.md) | Monetary and Fiscal Policy | Economics | Tools, neutral rate, multiplier |
| [ch06](chapters/ch06-international-trade-and-capital-flows.md) | International Trade and Capital Flows | Economics | Comparative advantage, tariffs, BOP |
| [ch07](chapters/ch07-currency-exchange-rates.md) | Currency Exchange Rates | Economics | Quotes, CIP, regimes, Marshall–Lerner |
| [ch08](chapters/ch08-market-organization-and-structure.md) | Market Organization and Structure | Equity | Intermediaries, orders, margin |
| [ch09](chapters/ch09-security-market-indexes.md) | Security Market Indexes | Equity | Weighting, rebalancing, biases |
| [ch10](chapters/ch10-market-efficiency.md) | Market Efficiency | Equity | EMH forms, anomalies, behavioral |
| [ch11](chapters/ch11-industry-and-company-analysis.md) | Introduction to Industry and Company Analysis | Equity | GICS, life cycle, five forces |
| [ch12](chapters/ch12-overview-of-equity-securities.md) | Overview of Equity Securities | Equity | Common/preferred, DRs, ROE |
| [ch13](chapters/ch13-equity-valuation-concepts-and-tools.md) | Equity Valuation: Concepts and Basic Tools | Equity | DDM, Gordon, multiples, EV |
| [ch14](chapters/ch14-fixed-income-defining-elements.md) | Fixed-Income Securities: Defining Elements | Fixed Income | Indenture, enhancements, options |
| [ch15](chapters/ch15-fixed-income-markets-issuance-trading-funding.md) | Fixed-Income Markets: Issuance, Trading and Funding | Fixed Income | Auctions, CP, repo |
| [ch16](chapters/ch16-introduction-to-fixed-income-valuation.md) | Introduction to Fixed-Income Valuation | Fixed Income | YTM, spot/forward, spreads |
| [ch17](chapters/ch17-introduction-to-asset-backed-securities.md) | Introduction to Asset-Backed Securities | Fixed Income | SPV, RMBS, CMO, CMBS, CDO |
| [ch18](chapters/ch18-fixed-income-risk-and-return.md) | Understanding Fixed-Income Risk and Return | Fixed Income | Duration, convexity, horizon |
| [ch19](chapters/ch19-fundamentals-of-credit-analysis.md) | Fundamentals of Credit Analysis | Fixed Income | EL, seniority, ratings, 4 Cs |
| [ch20](chapters/ch20-derivative-markets-and-instruments.md) | Derivative Markets and Instruments | Derivatives | Forwards, futures, swaps, options, CDS |

## Topic Index

- **ABS / MBS / CMO / CMBS** → ch17, ch14
- **Aggregate demand & supply** → ch03
- **Balance of payments** → ch06
- **Bond features, covenants, enhancements** → ch14
- **Business cycle, indicators** → ch04
- **Callable / putable / convertible** → ch14, ch18
- **Central bank, policy rate, QE** → ch05
- **Commercial paper, repo** → ch15
- **Convexity** → ch18
- **Credit analysis, ratings, EL** → ch19
- **Currency quotes, cross rates, forwards** → ch07
- **DDM / Gordon / FCFE** → ch13
- **Derivative instruments** → ch20
- **Duration (Macaulay, modified, effective, key rate)** → ch18
- **Efficient market hypothesis** → ch10
- **Elasticity** → ch01, ch07
- **Enterprise value, multiples** → ch13
- **Fiscal multiplier** → ch05
- **Five forces, life cycle** → ch11
- **Forward rates, spot curve** → ch16
- **Index weighting** → ch09
- **Inflation, CPI, price indexes** → ch04, ch05
- **Margin, leverage, orders** → ch08
- **Market structures** → ch02
- **Preferred shares, depository receipts** → ch12
- **Prepayment (SMM, CPR, PSA)** → ch17
- **Spreads (G, I, Z, OAS)** → ch16, ch19
- **Tariffs, quotas, trade blocs** → ch06
- **Unemployment types** → ch04

## Supporting Files

- [glossary.md](glossary.md): key terms with definitions
- [patterns.md](patterns.md): reusable calculation recipes
- [cheatsheet.md](cheatsheet.md): formulas, decision rules and exam traps

---

## Scope & Limits

This skill covers 20 readings of personal CFA Level I notes: Economics, Equity, Fixed Income, Derivatives. It does **not** cover Ethics, Quantitative Methods, Financial Reporting & Analysis, Corporate Finance, Portfolio Management or Alternative Investments, because those notes are not in the repo. The "Basics of Derivative Pricing and Valuation" reading is an empty draft in the source repo; use `hull-derivatives` for pricing. The notes date from the 2019 curriculum, so check current CFA Institute learning outcome statements (LOS) before the exam. Where the notes contained errors, chapters flag them with ⚠ and give the corrected statement.

## Related Skills (official-curriculum skills that go deeper)

These notes are a compact personal revision aid. For full detail with worked examples, exam traps and Level II/III extensions, switch to:

- `cfa-economics` — ch01–ch07 here map to its ch01–ch07 (Level I), plus Level II FX equilibrium, growth, regulation.
- `cfa-fixed-income` — ch14–ch19 here map to its ch01–ch06; adds Level II term structure, embedded options, credit models, CDS, and Level III strategies.
- `cfa-derivatives` — ch20 here maps to its ch01–ch02; adds forward and option valuation and strategies.
- `cfa-equity-valuation` and `cfa-portfolio-management` — ch08–ch13 here (markets, indexes, efficiency, equity securities, industry analysis, valuation).
- Topics these notes do not cover: `cfa-quantitative-methods`, `cfa-financial-statement-analysis`, `cfa-corporate-finance`, `cfa-ethics-gips`, `cfa-alternative-investments`, `cfa-asset-allocation-cme`.
