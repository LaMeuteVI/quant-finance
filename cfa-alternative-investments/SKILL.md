---
name: cfa-alternative-investments
description: "CFA Program alternative investments curriculum across three levels: Level I (2020 R50), Level II (2022 R35-R37: real estate, private equity, commodities), Level III (2023 R19-R20: hedge fund strategies, asset allocation to alternatives). Use when valuing property or REITs, analysing LBO or venture deals, decomposing commodity futures returns, evaluating hedge fund strategies and fees, or sizing alternatives in a portfolio: cap rate, NOI, NAVPS, FFO/AFFO, DSCR, LBO, VC method, DPI/TVPI, J-curve, carried interest, high-water mark, hurdle, contango, roll return, merger arbitrage, unsmoothing, commitment pacing, or when preparing a CFA alternatives quiz."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Alternative Investments (Levels I, II, III)
**Source**: CFA Program Curriculum Alternative Investments: L1 2020 R50, L2 2022 R35-R37, L3 2023 R19-R20 | **Domain**: Finance de marché | **Chapters**: 6 | **Generated**: 2026-10-05

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch03`
- **Browse** — "what chapters do you have?"
- **Exam mode** — ask for a quiz on a chapter or level; I build it from its Worked Example and Exam Focus & Traps sections and the Exam traps table in the cheatsheet.

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Alternatives overview and data quality**
- **Six-category map** (ch01): hedge funds, private equity, real estate, commodities, infrastructure, other. Place a vehicle by public/private, equity/debt, active/passive, fund/direct, and what drives return.
- **Data filter** (ch01, ch02, ch06): survivorship and backfill bias inflate returns; appraisal smoothing deflates volatility and correlation. Unsmooth with `r_u = (r − s·r_prev)/(1 − s)` before computing Sharpe or allocating (PE reported 9.5% vs about 14%).
- **Hedge fund fee waterfall** (ch01, ch05): management fee on AUM, incentive on gain (net of management fee, net of hard hurdle), high-water mark per investor, `Net = (V_end − fees − capital)/capital`. FoF adds a second layer: 14% net becomes 11.6%; netting risk raises effective fees when funds diverge.
- **Due diligence grid** (ch01): organization, portfolio management, operations/controls, risk, legal, fund terms. Smooth returns are a fraud flag.

**Real estate**
- **Four quadrants** (ch02): public/private x equity/debt. Equity is residual claim; debt is bond-like with priority on collateral.
- **Cap rate identity** (ch02): `c = r − g`, `Value = NOI1/c`. Terminal value uses NOI(N+1) at a cap rate at or above going-in. Financing never changes property value.
- **Three approaches** (ch02): income, cost, sales comparison, reconciled; highest and best use = highest residual land value.
- **Leverage** (ch02): max loan = min(LTV x V, NOI/DSCR/constant); equity dividend rate = (NOI − debt service)/equity; positive leverage only if property return exceeds loan rate.
- **REIT valuation** (ch02): NAVPS (forward cash NOI/cap + other assets − liabilities), P/FFO, P/AFFO, DDM. AFFO = FFO − straight-line rent − recurring capex.

**Private equity**
- **Three value sources** (ch03): re-engineering, leverage, alignment. Bridge: earnings growth + multiple expansion + deleveraging.
- **LBO model** (ch03): price ceiling from financiers' required returns; exit waterfall EV − debt − preference = residual equity.
- **VC method** (ch03): `Post = Exit/ROI`, `Pre = Post − investment`, `Ownership = investment/Post`, on a fully diluted base.
- **Fund economics** (ch03): fee on committed capital, carry 20% over hurdle, clawback; DPI, RVPI, TVPI = DPI + RVPI per dollar paid in; compare using PME and same-vintage peers.

**Commodities**
- **Total return decomposition** (ch04): spot + roll + collateral. Roll = (near − far)/near x share rolled; contango negative, backwardation positive.
- **Three curve theories** (ch04): insurance (Keynes), hedging pressure, storage (`F = S + storage − convenience yield`). Evidence for a backwardation premium is weak.
- **Index levers** (ch04): breadth, weighting, roll rule, rebalancing, governance; GSCI is energy-heavy, BCOM capped.

**Hedge funds and allocation**
- **Six strategy families and payoff lens** (ch05): merger arb = bond + short binary put; fixed-income arb = short put; convertible arb = long gamma/vega. Classify diversifier vs return enhancer.
- **Conditional factor model** (ch05): add a crisis dummy to equity, credit, USD, VIX factors; crisis exposure = β + β^crisis.
- **Four roles and two-step allocation** (ch06): growth, income, diversification, safety; set the liquid mix first, then split private buckets. Correlation above 0.8 to equities is not a diversifier.
- **Tools** (ch06): constrained MVO, mean-CVaR, Monte Carlo, factor-based; Takahashi-Alexander cash-flow model for commitment pacing and liquidity stress.

---

## Chapter Index
| # | Title | Level · Reading | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-l1-intro-alternative-investments.md) | Introduction to Alternative Investments | L1 · R50 | Six-category map, fee waterfall, HWM, due diligence, data biases |
| [ch02](chapters/ch02-l2-real-estate-investments.md) | Real Estate Investments | L2 · R35 | Four quadrants, cap rate, DCF, LTV/DSCR, NAVPS, FFO/AFFO |
| [ch03](chapters/ch03-l2-private-equity-investments.md) | Private Equity Investments | L2 · R36 | LBO model, VC method, waterfall, DPI/RVPI/TVPI, PME |
| [ch04](chapters/ch04-l2-commodities-and-commodity-derivatives.md) | Commodities and Commodity Derivatives | L2 · R37 | Spot/roll/collateral, contango, curve theories, swaps, indexes |
| [ch05](chapters/ch05-l3-hedge-fund-strategies.md) | Hedge Fund Strategies | L3 · R19 | Six strategy families, conditional factor model, 20% allocation test |
| [ch06](chapters/ch06-l3-asset-allocation-to-alternative-investments.md) | Asset Allocation to Alternative Investments | L3 · R20 | Roles, unsmoothing, mean-CVaR, commitment pacing, liquidity |

## Topic Index
- **AFFO / FFO** → ch01, ch02
- **Appraisal-based indexes, smoothing** → ch01, ch02, ch06
- **Backwardation / contango** → ch01, ch04
- **Bias (survivorship, backfill)** → ch01, ch05
- **Cap rate, NOI** → ch01, ch02
- **Carried interest, clawback** → ch01, ch03
- **Commitment pacing, capital calls** → ch06
- **Commodity indexes (GSCI, BCOM)** → ch04
- **Commodity swaps** → ch04
- **Convertible arbitrage** → ch05
- **Core vs non-core real estate** → ch02
- **CVaR / mean-CVaR** → ch06
- **Direct capitalization vs DCF** → ch02
- **Distressed debt** → ch05
- **Due diligence** → ch01, ch02, ch03, ch06
- **DPI, RVPI, TVPI** → ch03
- **DSCR, LTV** → ch02
- **Equity market neutral** → ch05
- **Fees (hedge fund, PE)** → ch01, ch03, ch06
- **Fixed-income arbitrage** → ch05
- **Fund of funds** → ch01, ch05, ch06
- **Global macro, managed futures** → ch05
- **Hedge fund strategies** → ch01, ch05
- **High-water mark, hurdle** → ch01
- **Highest and best use** → ch02
- **Infrastructure** → ch01
- **Insurance, storage, hedging pressure theories** → ch04
- **J-curve** → ch03, ch06
- **LBO model** → ch03
- **Leases (net, gross, percentage)** → ch02
- **Liquid alts** → ch05
- **Liquidity planning** → ch06
- **Merger arbitrage** → ch05
- **Monte Carlo, MVO** → ch06
- **NAVPS** → ch02
- **Option-payoff lens on strategies** → ch05
- **PME** → ch03
- **Pre/post-money** → ch03
- **REIT / REOC** → ch02
- **Roll return** → ch04
- **Sharpe / Sortino** → ch01, ch05
- **Takahashi-Alexander model** → ch06
- **Terminal cap rate** → ch02
- **Unsmoothing** → ch06
- **Valuation of PE targets** → ch01, ch03
- **VC method** → ch03
- **Vintage year** → ch03, ch06

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, exam traps

---

## Related Skills
- `cfa-portfolio-management` — diversification and asset allocation fundamentals behind ch06
- `cfa-asset-allocation-cme` — policy, factor-based and liability-relative allocation using these assets
- `cfa-derivatives` — futures, options and swaps behind commodity and hedge fund payoffs
- `cfa-equity-valuation` — private company valuation and DDM used for PE targets and REITs
- `cfa-fixed-income` — credit strategies, MBS/CMBS for the real estate debt quadrant
- `cfa-wealth-institutional-management` — institutional liquidity and horizon constraints
- `tian-commodity-price-jumps` — quantitative commodity price dynamics
- `pairs-trading-partial-cointegration` — mean reversion behind equity market neutral

## Scope & Limits
Covers the CFA alternative investments readings only: L1 2020 R50, L2 2022 R35-R37 (errata applied), L3 2023 R19-R20. Check current learning outcome statements, as later curricula revise readings. Source corrections found in the readings are flagged in chapters as Correction or Errata. Infrastructure, collectibles and private credit are only touched; commodity data are dated to 2019 and index facts to April 2019. Practitioner detail is in `cfasi-portfolio-construction` ch15.
