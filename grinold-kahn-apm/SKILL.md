---
name: grinold-kahn-apm
description: "Knowledge base from Richard Grinold & Ronald Kahn, Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk, 2nd ed. (McGraw-Hill, 1999). Use when designing or evaluating active quantitative strategies, building the consensus expected return vector, computing the Information Ratio (IR = IC × √B × TC), applying the Fundamental Law of Active Management, performing Brinson-Fachler performance attribution, or evaluating the persistence of alpha. Covers CAPM/APT consensus, residual alpha, forecasting (information coefficient and breadth), portfolio construction (mean-variance with forecast uncertainty, Black-Litterman), long/short investing, transaction costs and capacity, and the empirical record on active management (with 2026 institutional updates: DSR, PBO, Harvey-Liu 3.0 t-stat)."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Active Portfolio Management (Grinold & Kahn)

**Source**: Grinold & Kahn, *Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk*, 2nd ed. (McGraw-Hill, 1999) | **Domain**: Gestion de portefeuille | **Chapters**: 22 | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview, then drill into the chapters.
- **With a topic or framework name** (e.g. "Fundamental Law", "IR", "consensus", "BBF attribution"): jump to the relevant chapter.
- **With a chapter number**: open `chapters/chNN-*.md`.
- **For institutional performance standards**: see `cheatsheet.md` (Harvey-Liu 3.0 t-stat, DSR threshold, PBO threshold, McLean-Pontiff decay).

## Core Frameworks & Mental Models

1. **The Four-Stage Active Management Process** (ch01): Information → Forecasting → Portfolio Construction → Trading, with Performance Analysis as the feedback loop. The discipline is the master architecture.
2. **The Fundamental Law of Active Management** (ch06): `IR = IC × √B × TC`. IC enters linearly; breadth enters as √B; transfer coefficient ≤ 1. Doubling IC doubles IR; doubling breadth only multiplies IR by √2.
3. **The Rule of Thumb** (ch10): `α = s × IC × σ(θ)`. The universal conversion from raw signal to dollar alpha. IC = 0 collapses alpha to zero — a deliberate safety property.
4. **The Breakeven Information Ratio (BEIR)** (ch10): `√(annual_cost / B)`. The IC needed for a research project to break even. Most signals have IC < 0.10; the BEIR is the floor.
5. **The Brown-Kleiman correction** (ch10, ch11): `R²_OOS ≈ R²_IS − K/N`. The in-sample R² overstates the out-of-sample R² by K/N (K signals, N observations).
6. **The Unconstrained Optimal Active Portfolio** (ch14): `h* = (1/λ) V^(-1) α`. The mean-variance starting point; the constrained optimum is the projection onto the feasible set.
7. **The Certainty-Equivalent Version** (ch14): `h*_CE = (1/λ) (V + P)^(-1) α`. The honest version that accounts for forecast uncertainty `P`; under-estimating `P` is the most common error.
8. **The Breakeven Horizon** (ch13, ch16): `T_breakeven = C / α_1`. The minimum holding period at which gross alpha exceeds trading cost. The strategy's natural horizon must exceed it.
9. **The Square-Root Law of Market Impact** (ch16): `Impact(Q) = σ × √(Q/ADV) × Y`. The canonical impact model; cost is a *function* of size, not a number.
10. **The ½ Power Law of Optimal Size** (ch16): optimal `h ∝ 1/√cost`. Doubling cost reduces optimal size by 30%.
11. **The Brinson-Beebower-Fachler (BBF) Decomposition** (ch17): `R_active = R_AA + R_SS + R_int`. The institutional performance attribution standard. Use Carino smoothing to make components add to the total.
12. **The Skill / Luck Ratio** (ch17): `IR² / (1 + IR²)`. For IR = 0.5, only 20% of the alpha is skill.
13. **The 3.0 t-stat Rule** (ch20, 2026 update): the modern threshold for financial anomalies (Harvey-Liu 2015); most published anomalies fail it.
14. **The Post-Publication Decay** (ch20, 2026 update): academic anomalies decay ~26% OOS and ~58% after transaction costs (McLean-Pontiff 2016).
15. **The 130/30 IR Boost** (ch15): `√(gross/net) ≈ 1.26×` for the gross-to-net = 1.6 case. The boost is real but smaller in practice because of borrow cost, dividend treatment, and short-side capacity.

## Chapter Index

| # | Title | Key Frameworks | File |
|---|---|---|---|
| 1 | Introduction | Four-Stage Process; Rule of Thumb preview | [ch01](./chapters/ch01-introduction.md) |
| 2 | Consensus Expected Returns: CAPM | CAPM, beta, residual return | [ch02](./chapters/ch02-consensus-expected-returns-capm.md) |
| 3 | Risk | Risk decomposition, residual risk | [ch03](./chapters/ch03-risk.md) |
| 4 | Exceptional Return, Benchmarks, Value Added | Value-added, benchmark | [ch04](./chapters/ch04-exceptional-return-benchmarks-value-added.md) |
| 5 | Residual Risk and Return: IR | Information Ratio definition | [ch05](./chapters/ch05-residual-risk-and-return-information-ratio.md) |
| 6 | The Fundamental Law of Active Management | `IR = IC × √B × TC` | [ch06](./chapters/ch06-the-fundamental-law-of-active-management.md) |
| 7 | Expected Returns and APT | Multi-factor APT | [ch07](./chapters/ch07-expected-returns-and-apt.md) |
| 8 | Valuation in Theory | Factor pricing, consensus | [ch08](./chapters/ch08-valuation-in-theory.md) |
| 9 | Valuation in Practice | Implied cost of capital, Graham | [ch09](./chapters/ch09-valuation-in-practice.md) |
| 10 | Forecasting Basics | Rule of Thumb, BEIR, Brown-Kleiman | [ch10](./chapters/ch10-forecasting-basics.md) |
| 11 | Advanced Forecasting | Refinement, K_eff | [ch11](./chapters/ch11-advanced-forecasting.md) |
| 12 | Information Analysis | IC estimation, refinement | [ch12](./chapters/ch12-information-analysis.md) |
| 13 | The Information Horizon | Breakeven horizon, per-period IR | [ch13](./chapters/ch13-the-information-horizon.md) |
| 14 | Portfolio Construction | Unconstrained + CE optima | [ch14](./chapters/ch14-portfolio-construction.md) |
| 15 | Long/Short Investing | LS IR boost, borrow cost | [ch15](./chapters/ch15-long-short-investing.md) |
| 16 | Transactions Costs, Turnover, Trading | Square-root impact, breakeven turnover | [ch16](./chapters/ch16-transactions-costs-turnover-and-trading.md) |
| 17 | Performance Analysis | BBF, Carino, skill/luck | [ch17](./chapters/ch17-performance-analysis.md) |
| 18 | Asset Allocation | Active factor exposure | [ch18](./chapters/ch18-asset-allocation.md) |
| 19 | Benchmark Timing | Market timing IR | [ch19](./chapters/ch19-benchmark-timing.md) |
| 20 | The Historical Record for Active Management | SPIVA, Fama-French, McLean-Pontiff | [ch20](./chapters/ch20-the-historical-record-for-active-management.md) |
| 21 | Open Questions | 1999 research agenda; 2026 status | [ch21](./chapters/ch21-open-questions.md) |
| 22 | Summary | Master checklist | [ch22](./chapters/ch22-summary.md) |

## Topic Index

- **Alpha** → ch01, ch05, ch08, ch10, ch11, ch14
- **Asset allocation** → ch01, ch18
- **APT** → ch07, ch08
- **Bayesian shrinkage** → ch14
- **Benchmark** → ch01, ch04, ch19
- **Black–Litterman** → ch14
- **Brinson–Beebower–Fachler (BBF)** → ch17
- **Breakeven IC (BEIR)** → ch10
- **Breakeven horizon** → ch13, ch16
- **Breakeven turnover** → ch16
- **Brown–Kleiman correction** → ch10, ch11
- **Capacity** → ch16
- **CAPM** → ch02
- **Carino smoothing** → ch17
- **Certainty-equivalent construction** → ch14
- **Consensus expected return** → ch08, ch09
- **DCF (discounted cash flow)** → ch08, ch09
- **Deflated Sharpe Ratio (DSR, 2026)** → ch20
- **Dollar neutral** → ch15
- **Effective number of signals (K_eff)** → ch11
- **EMH (Efficient Market Hypothesis)** → ch01, ch20
- **Factor investing** → ch07, ch20
- **Factor premium (λ_k)** → ch07, ch08
- **Factor-mimicking portfolio** → ch08
- **Fama–French (2010)** → ch20
- **Forecast efficiency** → ch10
- **Forecast uncertainty (P)** → ch14
- **Fundamental Law of Active Management** → ch06
- **Graham's formula** → ch09
- **Harvey–Liu 3.0 t-stat** → ch20
- **Historical consensus** → ch09
- **IC (Information Coefficient)** → ch06, ch10
- **Implied cost of capital** → ch09
- **Information horizon** → ch13
- **Information matrix (R)** → ch11
- **Information Ratio (IR)** → ch05, ch06, ch17
- **Investibility constraint** → ch08
- **Long/short (LS) portfolio** → ch15
- **Market neutral** → ch15
- **McLean–Pontiff (2016)** → ch20
- **Mean reversion (next-year IR)** → ch17
- **Net exposure** → ch15
- **Net IR** → ch16
- **Noise** → ch10
- **Optimal benchmark exposure** → ch19
- **Optimal turnover** → ch16
- **Per-period IR** → ch13
- **Performance attribution (BBF)** → ch17
- **Position sizing** → ch16
- **Refined alpha** → ch11
- **Residual alpha** → ch08, ch14
- **Residual return** → ch01, ch05
- **Residual volatility (σ_θ)** → ch10, ch14
- **Risk aversion (λ)** → ch14
- **Rule of Thumb** → ch10
- **Score (s_i)** → ch10
- **Skill / luck ratio** → ch17
- **SPIVA scorecard** → ch20
- **Square-root law of impact** → ch16
- **Tracking error (TE)** → ch14
- **Transaction cost** → ch16
- **Transfer coefficient (TC)** → ch06
- **Turnover** → ch16
- **Valuation** → ch08, ch09
- **Value-added (VA)** → ch14
- **130/30 format** → ch15
- **½ Power Law of Optimal Size** → ch16

## Supporting Files

- [glossary.md](./glossary.md) — Alphabetical glossary of all significant terms.
- [patterns.md](./patterns.md) — 18 patterns (the "how to" recipes) with When to use, How, Trade-offs.
- [cheatsheet.md](./cheatsheet.md) — The judgment layer: decision rules, thresholds, tells & smells, citation table.

## Related Skills

- **`hull-risk-management`** (finance-de-marche) — Risk management framework; the institutional complement to active management.
- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — The modern statistical continuation: purged CV, CPCV, DSR, PBO, MinTRL.
- **`lopez-de-prado-ml-asset-managers`** (gestion-de-portefeuille) — Short companion volume to AFML; portfolio construction with ML signals.
- **`cfa-asset-allocation-cme`** (gestion-de-portefeuille) — Capital market expectations; the consensus-building framework.
- **`cfa-equity-portfolio-management`** (gestion-de-portefeuille) — Equity portfolio management; passive vs active.
- **`cfa-portfolio-management`** (gestion-de-portefeuille) — The broader portfolio management curriculum.
- **`cfasi-portfolio-construction`** (gestion-de-portefeuille) — CFA Society Italy practitioner guides on portfolio construction.
- **`hull-derivatives`** (finance-de-marche) — Pricing and Greeks for options and other derivatives.
- **`gatheral-volatility-surface`** (finance-de-marche) — The vol surface and SVI parameterisation; relevant for options-based alpha.

## Scope & Limits

- **Coverage**: 2nd edition (1999); 22 chapters; CAPM/APT, IC/IR, portfolio construction, long/short, transactions, performance attribution.
- **Edition year**: 1999 — superseded in 2026 by:
  - The 3.0 t-stat rule for multiple testing (Harvey-Liu 2015)
  - The Deflated Sharpe Ratio and PBO (Bailey-López de Prado 2014, 2016)
  - The post-publication decay (McLean-Pontiff 2016)
  - The factor investing consensus (Fama-French 5-factor, Hou-Xue-Zhang q-factor)
  - The DSR-adjusted backtest as the institutional standard
  - The shift from 130/30 to long-only / 120/20
  - The adoption of Black-Litterman / Idzorek in construction
  These updates are integrated as "⚠ Practitioner update" notes in the relevant chapters; they do not replace the book's framework, but they update the bar.
- **What the source does NOT cover**:
  - Volatility surface / option-implied vol as an alpha source (see `gatheral-volatility-surface`)
  - ML-derived signals and overfitting (see `lopez-de-prado-afml`)
  - VaR/ES / market risk (see `hull-risk-management`)
  - FRTB and Basel (see `frtb-market-risk-bcbs457`)
  - Time-series modelling of returns / GARCH (see `tsay-analysis-financial-time-series`)
  - Forecast evaluation tests (DM, SPA, Reality Check — see `diebold-mariano-forecast-accuracy`)
  - ML trading in production (see `chan-machine-trading`)
  - Performance measurement standards (GIPS — see `cfa-ethics-gips`)
- **OCR / extraction quality**: pdftotext output is clean; no reconstruction needed. Some formula notation was rendered with care; agent verifies arithmetic in worked examples via Python.
- **Translation**: English.
- **Authoring quality**: every chapter file is a `chapters/chNN-*.md` and follows the standard 12-section template. Worked examples are recomputed in Python. The Connects To section links to real chapters and skills.
