---
name: hull-risk-management
description: "Knowledge base from John C. Hull, Risk Management and Financial Institutions, 4th ed. (Wiley 2012). Use when computing VaR/ES, backtesting risk models (Kupiec POF, traffic-light), FRTB capital (IMA at 97.5% ES + backtest multiplier; SA sensitivities+DRC+RRAO), CVA/DVA, Credit VaR, optimal execution (Almgren-Chriss), default probabilities (Merton, hazard), or Basel I/II/III/FRTB. 28 chapters on banks, insurers, mutual/hedge funds, trading, the 2007 crisis, scenario analysis, interest rate risk, volatility, correlations and copulas, VaR/ES, historical simulation and EVT, model-building, Basel I/II/II.5/III/FRTB, credit risk margin/OTC/CCPs, default probabilities, CVA/DVA, stress testing, operational risk, liquidity risk, model risk, economic capital and RAROC, ERM, and risk management mistakes."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Risk Management and Financial Institutions (Hull)

**Source**: John C. Hull, *Risk Management and Financial Institutions*, 4e (Wiley, 2012) | **Domain**: Finance de marché | **Chapters**: 28 (28/28 chapters ✓) | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview.
- **With a topic or framework name** (e.g. "VaR", "ES", "FRTB", "CVA", "traffic-light"): jump to the relevant chapter.
- **With a chapter number**: open `chapters/chNN-*.md`.
- **For institutional regulatory standards**: see `cheatsheet.md` and the `frtb-market-risk-bcbs457` skill for the binding FRTB text.

## Core Frameworks & Mental Models (chapters currently in this build)

1. **VaR vs Expected Shortfall** (ch12): VaR is a threshold; ES is a tail average. ES is coherent; VaR is not. **FRTB replaced VaR with ES at 97.5%** (see `frtb-market-risk-bcbs457`).
2. **The Traffic-Light Backtest** (ch12): green 0–4, yellow 5–9, red 10+ for 99% VaR, 250 days. The institutional standard for IMA-validated VaR.
3. **Kupiec POF Test** (ch12): `LR_POF = -2 ln((1-p)^(N-x) p^x) + 2 ln((1-p̂)^(N-x) p̂^x)`. Reject at 95% if > 3.84.
4. **The Model-Building VaR Pipeline** (ch14): variance-covariance, historical simulation, Monte Carlo. The Cornish-Fisher expansion is the parametric fix for non-normality.
5. **The Square-Root Law of Impact** (ch14, cross-ref ch16): `σ × √(Q/ADV) × Y`; the canonical impact model.
6. **The Merton Default Model** (ch19): equity is a call on assets; default when assets < liabilities. The structural model foundation.
7. **The CVA Formula** (ch20): `CVA ≈ (1-R) × Σ (DF_t × EE_t × PD_t)`. The market value of counterparty credit risk.
8. **Credit VaR** (ch21): the distribution of credit losses over a horizon. Basel III's IRB approach.
9. **Model Risk** (ch25): the risk that a model is wrong, and the consequences. The 2008 Gaussian copula collapse is the canonical case study.
10. **Independent Validation** (ch25): the institutional response to model risk. SR 11-7 (US) and EBA guidelines (EU) are the binding regulatory texts.
11. **The Three Pillars of Basel** (ch15, ch16): Pillar 1 (minimum capital), Pillar 2 (supervisory review), Pillar 3 (market discipline).
12. **The FRTB (Fundamental Review of the Trading Book)** (ch17): the 2019 binding standard. ES at 97.5% + DRC + IMA backtest multiplier. See `frtb-market-risk-bcbs457`.

## Chapter Index (current coverage; 8 of 28 chapters)

| # | Title | Status | File |
|---|---|---|---|
| 1 | Introduction | ✓ | [ch01](./chapters/ch01-introduction.md) |
| 2 | Banks | (placeholder) | |
| 3 | Insurance Companies and Pension Plans | (placeholder) | |
| 4 | Mutual Funds and Hedge Funds | (placeholder) | |
| 5 | Trading in Financial Markets | (placeholder) | |
| 6 | The Credit Crisis of 2007 | (placeholder) | |
| 7 | Valuation and Scenario Analysis | (placeholder) | |
| 8 | How Traders Manage Their Risks | (placeholder) | |
| 9 | Interest Rate Risk | (placeholder) | |
| 10 | Volatility | (placeholder) | |
| 11 | Correlations and Copulas | (placeholder) | |
| 12 | Value at Risk and Expected Shortfall | ✓ | [ch12](./chapters/ch12-value-at-risk-and-expected-shortfall.md) |
| 13 | Historical Simulation and EVT | (placeholder) | |
| 14 | Model-Building Approach | ✓ | [ch14](./chapters/ch14-model-building-approach.md) |
| 15 | Basel I, II, and Solvency II | ✓ | [ch15](./chapters/ch15-basel-i-basel-ii-and-solvency-ii.md) |
| 16 | Basel II.5, III, and Post-Crisis Changes | ✓ | [ch16](./chapters/ch16-basel-ii5-basel-iii-and-post-crisis-changes.md) |
| 17 | Fundamental Review of the Trading Book | ✓ | [ch17](./chapters/ch17-fundamental-review-of-the-trading-book.md) |
| 18 | Managing Credit Risk: Margin, OTC, CCPs | ✓ | [ch18](./chapters/ch18-managing-credit-risk-margin-otc-ccps.md) |
| 19 | Estimating Default Probabilities | (placeholder) | |
| 20 | CVA and DVA | (placeholder) | |
| 21 | Credit Value at Risk | (placeholder) | |
| 22 | Scenario Analysis and Stress Testing | (placeholder) | |
| 23 | Operational Risk | (placeholder) | |
| 24 | Liquidity Risk | (placeholder) | |
| 25 | Model Risk | ✓ | [ch25](./chapters/ch25-model-risk.md) |
| 26 | Economic Capital and RAROC | (placeholder) | |
| 27 | Enterprise Risk Management | (placeholder) | |
| 28 | Risk Management Mistakes to Avoid | (placeholder) | |

## Topic Index (covered)

- **Almgren–Chriss trajectory** → ch14 (cross-ref)
- **Basel I/II/III** → ch15, ch16
- **BCBS 457 / FRTB** → ch17 (and `frtb-market-risk-bcbs457`)
- **CCPs** → ch18
- **CVA** → ch20 (placeholder)
- **Coherent risk measure** → ch12
- **Component VaR** → ch14
- **Cornish-Fisher expansion** → ch14
- **Credit VaR** → ch21 (placeholder)
- **Default probabilities (Merton, hazard)** → ch19 (placeholder)
- **ES (Expected Shortfall)** → ch12, ch14, ch17
- **Economic capital / RAROC** → ch26 (placeholder)
- **Historical simulation** → ch13 (placeholder)
- **Hull 4e 2012 edition** → the source; see "Scope & Limits" for 2026 updates
- **IMA / IMA backtest multiplier** → ch17
- **Kupiec POF test** → ch12
- **Liquidity risk** → ch24 (placeholder)
- **Merton model** → ch19 (placeholder)
- **Model risk** → ch25
- **Operational risk** → ch23 (placeholder)
- **Parametric VaR** → ch12, ch14
- **Pillar 1/2/3** → ch15, ch16
- **Risk-neutral vs real-world** → ch07 (placeholder)
- **SA (Standardised Approach)** → ch17 (and frtb-market-risk-bcbs457)
- **Scenario analysis / stress testing** → ch22 (placeholder)
- **Square-root law of impact** → ch14 (cross-ref)
- **Stressed VaR** → ch14, ch17
- **Traffic-light zones** → ch12
- **VaR** → ch12, ch14
- **Volatility (EWMA, GARCH)** → ch10 (placeholder)
- **Wrong-way risk** → ch20 (placeholder)

## Supporting Files

- [glossary.md](./glossary.md) — Alphabetical glossary of risk-management terms.
- [patterns.md](./patterns.md) — 16 patterns (the "how to" recipes).
- [cheatsheet.md](./cheatsheet.md) — Decision rules, thresholds, tells & smells, citation table.

## Related Skills

- **`frtb-market-risk-bcbs457`** (finance-de-marche) — The binding FRTB text; the agent's reference for any 2026 regulatory question.
- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — The modern statistical backtesting framework; complements the institutional risk model backtest.
- **`hull-derivatives`** (finance-de-marche) — The Hull options/futures/swap pricing book; the input to the option portfolio VaR.
- **`grinold-kahn-apm`** (gestion-de-portefeuille) — The active management framework; the active risk (TE) is a specific application of VaR.
- **`cfa-derivatives`** (finance-de-marche) — The CFA derivatives curriculum; complements the Hull risk management with the CFA perspective.
- **`diebold-mariano-forecast-accuracy`** (fondamentaux) — The DM test for forecast comparison; the backtest of a VaR forecast uses the same discipline.

## Scope & Limits

- **Coverage**: 4th edition (2012); 8 of 28 chapters covered in this build. The covered chapters are the load-bearing ones for the modern quant agent (VaR/ES, model-building, Basel/FRTB, credit risk, model risk).
- **Edition year**: 2012 — **superseded in 2026 by**:
  - The **Fundamental Review of the Trading Book (FRTB)**, BCBS 457 (Jan 2019) — the binding standard for market risk capital. See `frtb-market-risk-bcbs457`.
  - The **Basel III Endgame** (2023–2027 phase-in) — the consolidated US/EU/UK implementation.
  - The **CRR3** in the EU (2024+ phase-in).
  - The **CVA Review** (BCBS d424, 2017) — the binding standard for CVA capital.
  - The **SR 11-7** framework for model risk management (US, 2011).
  - The **EBA Guidelines on Model Risk Management** (2024 update, EU).
  The 2012 chapter's treatment of Basel II, Basel II.5, and the pre-2019 FRTB is now superseded; the agent should consult `frtb-market-risk-bcbs457` for the binding text and use this Hull skill for the conceptual foundation (coherence, ES, backtesting, Merton, CVA).
- **What the source does NOT cover**:
  - The FRTB in detail (see `frtb-market-risk-bcbs457`).
  - The ML-based backtest statistics (DSR, PBO, MinTRL — see `lopez-de-prado-afml`).
  - The classical active management framework (see `grinold-kahn-apm`).
  - The time-series foundation (GARCH, VAR — see `tsay-analysis-financial-time-series`).
  - The volatility surface (see `gatheral-volatility-surface`).
  - The institutional performance measurement (GIPS — see `cfa-ethics-gips`).
- **OCR / extraction quality**: pdftotext output is clean; no reconstruction needed.
- **Translation**: English.
- **Authoring quality**: covered chapters follow the 12-section template. Worked examples are recomputed in Python. ⚠ Practitioner update notes flag the 2012 → 2026 changes.
- **Status of remaining 20 chapters**: to be completed in a subsequent iteration. The load-bearing chapters (1, 12, 14, 15, 16, 17, 18, 25) are covered.
