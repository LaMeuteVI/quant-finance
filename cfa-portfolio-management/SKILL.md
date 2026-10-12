---
name: cfa-portfolio-management
description: "CFA Program Portfolio Management across three levels: Level I (2020 R36-R38, R51-R57), Level II (2022 R38-R41, R43-R44), Level III (2023 R25-R27): markets and indexes, efficiency, portfolio theory and CAPM, IPS, risk management, technical analysis, fintech, ETFs, multifactor models, VaR, backtesting, active management, trading and performance evaluation, manager selection. Use when working on efficient frontier, CML, SML, Sharpe, Treynor, Jensen alpha, IPS, TWR vs MWR, margin call, index weighting, VaR, APT, tracking error, information ratio, fundamental law, implementation shortfall, Brinson attribution, manager due diligence, or when preparing CFA portfolio management exam questions."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Portfolio Management (Levels I, II, III)
**Source**: CFA Program Curriculum, L1 2020 R36-R38 and R51-R57, L2 2022 R38-R41 and R43-R44, L3 2023 R25-R27 | **Domain**: Gestion de portefeuille | **Chapters**: 19 | **Generated**: 2026-10-05

## How to Use This Skill
- **Without arguments**: load the core frameworks below
- **With a topic**: ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter**: ask for `ch06`
- **Browse**: "what chapters do you have?"
- **Exam mode**: ask for a quiz on a chapter or level; I build it from its Worked Example and Exam Focus & Traps sections and the Exam traps table in [cheatsheet.md](cheatsheet.md).

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models
**Return and risk basics**
- **Return-measure selector**: HPR for one period, geometric for compounding, arithmetic for forecasts, TWR for managers, MWR (IRR) for the investor's own result; annualize (1+r)^c − 1; tax first, then inflation (ch05).
- **Portfolio risk**: σp² = Σwᵢ²σᵢ² + 2Σwᵢwⱼρσᵢσⱼ; correlation, not asset count, sets the floor; correlations jump in crises (ch04, ch05).
- **CAL, two-fund separation, utility**: U = E(r) − ½Aσ²; tangency portfolio P once, then y* = [E(Rp) − Rf]/(Aσp²); add an asset only if Sharpe_new > ρ × Sharpe_p (ch05).
- **CML, SML, CAPM**: E(R) = Rf + β[E(Rm) − Rf]; σᵢ² = βᵢ²σm² + σₑ²; only β is priced; CML for efficient portfolios, SML for any asset (ch06).
- **Performance ratios**: Sharpe and M² (total risk, whole portfolio) vs Treynor and Jensen α (beta risk, sleeve); M² = SR × σm + Rf (ch06).

**Process and risk management**
- **IPS (RRTTLLU)**: return and risk objectives, then time, tax, liquidity, legal, unique; risk tolerance = lower of ability and willingness; real target inflated by (1+π)ⁿ (ch04, ch07).
- **Risk management loop**: define tolerance, measure, adjust; risk budget in factor terms; avoid, self-insure, transfer, shift (ch08).
- **Markets and efficiency**: weak ⊂ semi-strong ⊂ strong; anomaly triage (persistence, risk adjustment, costs, rationale); margin call P₀(1−e)/(1−m) (ch01, ch03).
- **Index construction**: five design choices; weighting is a hidden factor bet; weights at beginning of period (ch02).

**Level II tools**
- **Multifactor and APT**: E(R) = RF + Σλβ; active return = factor tilts + selection; active risk² = factor + specific (ch12).
- **VaR toolkit**: parametric, historical, Monte Carlo; VaR is a minimum loss; add CVaR, IVaR, stress tests; never scale VaR by √T (ch13).
- **Backtest hygiene**: point-in-time data, rolling windows at each layer, t > 3, drawdown and CVaR beyond Sharpe (ch14).
- **ETF mechanics**: AP creation/redemption keeps price near NAV; short horizon pay liquidity, long horizon pay fee and tracking difference (ch11).
- **Fundamental law**: IR = TC · IC · √BR; σ_A* = TC(IR/SR_B)σ_B; SR² = SR_B² + IR² (ch15).
- **Trading costs**: effective spread for one fill, VWAP for the interval, implementation shortfall for the whole decision (ch16).

**Level III implementation and evaluation**
- **Trade strategy**: motivation sets urgency and benchmark; trader's dilemma; algorithm by situation; expanded IS = delay + trading + opportunity + fees (ch17).
- **Attribution and appraisal**: Brinson-Fachler (allocation, selection, interaction), benchmark tests, Sortino, capture ratios, drawdown (ch18).
- **Manager selection**: universe by role, quantitative record, investment and operational due diligence, Type I/II errors, fee options (ch19).
- **Technical analysis and fintech**: trend, pattern, oscillator method; train/validate/test, DLT, robo-advice (ch09, ch10).

---

## Chapter Index
| # | Title | Level · Reading | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-l1-market-organization-and-structure.md) | Market Organization and Structure | L1 · R36 | margin math, order types, market structures |
| [ch02](chapters/ch02-l1-security-market-indexes.md) | Security Market Indexes | L1 · R37 | index weighting, divisor, benchmarks |
| [ch03](chapters/ch03-l1-market-efficiency.md) | Market Efficiency | L1 · R38 | three forms, anomalies, behavioral finance |
| [ch04](chapters/ch04-l1-portfolio-management-overview.md) | Portfolio Management: An Overview | L1 · R51 | portfolio approach, process, investor types, funds |
| [ch05](chapters/ch05-l1-portfolio-risk-and-return-part1.md) | Portfolio Risk and Return: Part I | L1 · R52 | return measures, utility, frontier, CAL |
| [ch06](chapters/ch06-l1-portfolio-risk-and-return-part2.md) | Portfolio Risk and Return: Part II | L1 · R53 | CML, CAPM, SML, Sharpe, Treynor, M², alpha |
| [ch07](chapters/ch07-l1-portfolio-planning-and-construction.md) | Basics of Portfolio Planning and Construction | L1 · R54 | IPS, ability vs willingness, SAA, ESG approaches |
| [ch08](chapters/ch08-l1-intro-risk-management.md) | Introduction to Risk Management | L1 · R55 | risk framework, budgeting, VaR, modification |
| [ch09](chapters/ch09-l1-technical-analysis.md) | Technical Analysis | L1 · R56 | charts, patterns, oscillators, cycles, intermarket |
| [ch10](chapters/ch10-l1-fintech-in-investment-management.md) | Fintech in Investment Management | L1 · R57 | Big Data, ML, robo-advice, DLT |
| [ch11](chapters/ch11-l2-exchange-traded-funds.md) | Exchange-Traded Funds | L2 · R38 | creation/redemption, tracking, cost of ownership |
| [ch12](chapters/ch12-l2-multifactor-models.md) | Using Multifactor Models | L2 · R39 | APT, factor models, active risk, IR |
| [ch13](chapters/ch13-l2-measuring-managing-market-risk.md) | Measuring and Managing Market Risk | L2 · R40 | VaR methods, CVaR, stress tests, limits |
| [ch14](chapters/ch14-l2-backtesting-and-simulation.md) | Backtesting and Simulation | L2 · R41 | rolling window, biases, Monte Carlo, scenarios |
| [ch15](chapters/ch15-l2-analysis-of-active-portfolio-management.md) | Analysis of Active Portfolio Management | L2 · R43 | fundamental law, IC, TC, breadth, IR |
| [ch16](chapters/ch16-l2-trading-costs-and-electronic-markets.md) | Trading Costs and Electronic Markets | L2 · R44 | effective spread, VWAP, IS, electronic traders |
| [ch17](chapters/ch17-l3-trade-strategy-and-execution.md) | Trade Strategy and Execution | L3 · R25 | urgency, algorithms, expanded IS, governance |
| [ch18](chapters/ch18-l3-portfolio-performance-evaluation.md) | Portfolio Performance Evaluation | L3 · R26 | Brinson-Fachler, risk attribution, benchmarks |
| [ch19](chapters/ch19-l3-investment-manager-selection.md) | Investment Manager Selection | L3 · R27 | due diligence, Type I/II, capture, fees |

## Topic Index
- **Active share** → ch15, ch19
- **Alpha, Jensen's** → ch06, ch15
- **Anomalies** → ch03
- **APT** → ch06, ch12
- **Arbitrage (ETF, APT)** → ch11, ch12
- **Asset class definition** → ch07
- **Backtesting biases** → ch14
- **Behavioral finance** → ch03
- **Benchmark quality** → ch18
- **Beta** → ch06
- **Blockchain, DLT** → ch10
- **Brinson attribution** → ch18
- **Candlestick, point and figure** → ch09
- **Capital allocation line** → ch05, ch06
- **Capture ratios, drawdown** → ch18, ch19
- **CAPM, SML, CML** → ch06
- **Correlation, diversification** → ch04, ch05
- **CVaR, expected shortfall** → ch13
- **DB vs DC plans** → ch04
- **Efficient frontier** → ch05
- **Efficient market forms** → ch03
- **ESG approaches** → ch07
- **ETF premium and discount** → ch11
- **Event study** → ch03
- **Fama-French, Carhart** → ch06, ch12, ch18
- **Fee structures, HWM** → ch04, ch19
- **Fundamental law of active management** → ch15
- **Hedge funds, private equity** → ch04, ch19
- **Implementation shortfall** → ch16, ch17
- **Index weighting** → ch02
- **Information ratio** → ch12, ch15, ch18
- **IPS** → ch04, ch07
- **Machine learning** → ch10
- **Margin and leverage** → ch01
- **Market structure, orders** → ch01
- **Momentum, overreaction** → ch03
- **Monte Carlo** → ch13, ch14
- **MWR vs TWR** → ch05
- **Oscillators (RSI, MACD)** → ch09
- **Quote-driven vs order-driven** → ch01
- **Rebalancing, TAA, SAA** → ch07
- **Return measures** → ch05
- **Risk budgeting** → ch07, ch08, ch13
- **Risk parity** → ch07, ch12, ch14
- **Robo-advisers** → ch10
- **Sharpe, Treynor, M²** → ch05, ch06, ch15
- **Sortino ratio** → ch18
- **Style analysis (RBSA, HBSA)** → ch19
- **Technical analysis** → ch09
- **Tracking error** → ch11, ch12, ch13, ch15
- **Trading algorithms** → ch16, ch17
- **Transfer coefficient, IC, breadth** → ch15
- **Type I and II errors** → ch19
- **Utility, risk aversion** → ch05, ch07
- **VaR methods** → ch08, ch13
- **Venue, dark pools** → ch01, ch16, ch17

## Supporting Files
- [glossary.md](glossary.md): key terms with definitions
- [patterns.md](patterns.md): techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md): decision rules, thresholds, exam traps

---

## Related Skills
- `cfa-asset-allocation-cme`: SAA, CMEs, mean-variance optimisation and real-world constraints after the IPS (ch07)
- `cfa-equity-portfolio-management`: passive and active equity portfolio construction (L3)
- `cfa-wealth-institutional-management`: IPS for individuals, pensions, endowments, insurers
- `cfa-derivatives`: Greeks and instruments behind risk shifting and synthetic ETFs
- `cfa-quantitative-methods`: regression, probability, machine learning behind beta, VaR and fintech chapters
- `cfa-alternative-investments`: hedge fund, private equity and fee mechanics
- `cfa-level1-curriculum`: personal Level I revision notes (markets, indexes, efficiency)
- `cfa-ethics-gips`: suitability, best execution, GIPS presentation

## Scope & Limits
Covers CFA Level I 2020 (R36-R38, R51-R57), Level II 2022 (R38-R41, R43-R44) and Level III 2023 (R25-R27) portfolio management readings, translated and condensed from extracted curriculum text. Check current LOS before sitting an exam, since the portfolio management topic has been reorganised since these editions. Source corrections and errata are flagged inline (ch04 diversification ratio, ch09 momentum and RSI notes, ch12 errata, ch13 Monte Carlo CVaR, ch16 VWAP, ch17 rounding). Level I chapters ch01-ch03 were produced from re-extracted PDF text; worked examples were recomputed in Python.
