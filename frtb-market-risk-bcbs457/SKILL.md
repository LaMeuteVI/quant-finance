---
name: frtb-market-risk-bcbs457
description: "Binding reference for the Fundamental Review of the Trading Book (FRTB), BCBS 457, January 2019. Use when computing market risk capital under the IMA (Internal Models Approach with ES at 97.5% + DRC + backtest multiplier) or the SA (Standardised Approach with sensitivities-based method, default risk charge, and residual risk add-on), applying the trading book / banking book boundary rules (MAR25), running the IMA backtest and P&L attribution test, or interpreting the regulatory binding standard for any 2026 trading book capital question. Covers 9 chapters: introduction and scope, the Standardised Approach (sensitivities-based method, default risk charge, residual risk add-on), the Internal Models Approach (ES at 97.5%, backtest multiplier, P&L attribution), the Simplified Standardised Approach, the trading book boundary, and stress testing. Replaces the 2012 Hull 4e FRTB preview and the 2006 Basel II market risk framework."
---

<!-- argument-hint: [topic, MAR section, or capital calculation] -->

# FRTB — Market Risk (BCBS 457)

**Source**: Basel Committee on Banking Supervision, *Minimum Capital Requirements for Market Risk* (BCBS 457), January 2019 | **Domain**: Finance de marché | **Chapters**: 9 (selected sections) | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview.
- **With a topic or MAR section** (e.g. "MAR21 sensitivities", "MAR22 DRC", "MAR32 backtest", "ES at 97.5%"): jump to the relevant chapter.
- **For a specific capital calculation**: identify the approach (IMA or SA), the risk type (delta, vega, curvature, default, residual), and the bucket, then apply the prescribed formula.

## Core Frameworks & Mental Models

1. **The Two Approaches**: IMA (Internal Models Approach) and SA (Standardised Approach). Capital = max(IMA, SA).
2. **IMA Capital**: `ES_t × m_t` + DRC + NMRF stress scenario. The multiplier `m_t` ∈ [1.0, 1.84] based on the backtest and PLAT.
3. **SA Capital**: `SA-SBM` (sensitivities-based method) + `SA-DRC` (default risk charge) + `SA-RRAO` (residual risk add-on).
4. **The Trading Book Boundary** (MAR25): trading intent vs. held-to-maturity.
5. **The IMA Backtest** (MAR32): the operational validation; the exception count over 250 days.
6. **The P&L Attribution Test (PLAT)**: the formal statistical validation; the chi-squared test of the PL distribution.
7. **The 12-Week Stressed ES** (MAR99): the binding ES in the IMA.
8. **The Confidence Level**: 97.5% (vs. the pre-FRTB 99%).
9. **The Holding Period**: 1 day (vs. the pre-FRTB 10 days).
10. **The Default Risk Charge (DRC)**: a separate charge for default risk; the IMA does not capture it well.

## Chapter Index (selected MAR sections)

| # | Title | MAR | Key Frameworks | File |
|---|---|---|---|---|
| 1 | Introduction and Scope | MAR10–MAR12 | Two approaches, capital = max(IMA, SA) | [ch01](./chapters/ch01-introduction-and-scope.md) |
| 2 | SA: Sensitivities-Based Method | MAR21 | Delta, vega, curvature; buckets; correlations | [ch02](./chapters/ch02-standardised-approach-sensitivities-based-method.md) |
| 3 | SA: Default Risk Charge | MAR22 | Single-name, multi-name, risk weights | [ch03](./chapters/ch03-standardised-approach-default-risk-charge.md) |
| 4 | SA: Residual Risk Add-On | MAR23 | 1% of notional for non-modellable risk | [ch04](./chapters/ch04-standardised-approach-residual-risk-add-on.md) |
| 5 | IMA: Expected Shortfall | MAR30–MAR33 | ES at 97.5%, multiplier, NMRF stress | [ch05](./chapters/ch05-internal-models-approach-expected-shortfall.md) |
| 6 | IMA Backtesting and P&L Attribution | MAR32 | Backtest zones, PLAT chi-squared | [ch06](./chapters/ch06-ima-backtesting-and-pl-attribution.md) |
| 7 | Simplified Standardised Approach | MAR40 | Small banks, global multiplier | [ch07](./chapters/ch07-simplified-standardised-approach.md) |
| 8 | Trading Book Boundary | MAR25 | Trading intent, switching restrictions | [ch08](./chapters/ch08-trading-book-boundary.md) |
| 9 | Stress Testing and Scenario Analysis | MAR99 | 12-week stressed ES, reverse stress | [ch09](./chapters/ch09-stress-testing-and-scenario-analysis.md) |

## Topic Index

- **Backtest (IMA)** → ch06
- **Buckets (SA)** → ch02
- **Curvature risk** → ch02
- **Default Risk Charge (DRC)** → ch03
- **Delta risk** → ch02
- **ES (Expected Shortfall) at 97.5%** → ch05
- **IMA backtest multiplier** → ch05, ch06
- **Internal Models Approach (IMA)** → ch05, ch06
- **Non-Modellable Risk Factors (NMRFs)** → ch05
- **P&L Attribution Test (PLAT)** → ch06
- **Residual Risk Add-On (RRAO)** → ch04
- **Risk weights** → ch02, ch03
- **Sensitivities-Based Method (SBM)** → ch02
- **Simplified Standardised Approach** → ch07
- **Standardised Approach (SA)** → ch02, ch03, ch04
- **Stress testing** → ch09
- **Trading book / banking book boundary** → ch08
- **Vega risk** → ch02

## Supporting Files

- The full text of BCBS 457 is in `/Users/samuel/Desktop/Livres/Skills/.skillbuild/extract/FRTB_BCBS457/full_text.txt` (the canonical reference).

## Related Skills

- **`hull-risk-management`** (finance-de-marche) — ch12 (VaR/ES), ch14 (Model-Building), ch17 (FRTB preview — the 4e was 2012, pre-FRTB).
- **`gatheral-volatility-surface`** (finance-de-marche) — the SVI parameterisation and the vol surface for the IMA.
- **`hull-derivatives`** (finance-de-marche) — the options pricing book; the input to the option portfolio VaR.
- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — the modern statistical backtest discipline.

## Scope & Limits

- **Coverage**: 9 selected MAR sections of BCBS 457 (Jan 2019). The full BCBS 457 has ~50 MAR sections; this skill covers the load-bearing ones for the IMA and SA capital calculations.
- **Edition year**: 2019 — the binding standard. Updates: BCBS d424 (2017) for CVA; subsequent clarifications (d466, d473, etc.) are not in the source.
- **Implementation in the EU**: CRR3 (2024) phase-in; the EU FRTB implementation is largely aligned with BCBS 457 but with phase-in dates and a few calibration adjustments.
- **Implementation in the US**: Basel III Endgame (2023-2027 phase-in) — the US implementation.
- **What the source does NOT cover**:
  - The CVA Review (BCBS d424, 2017) — see `hull-risk-management` ch20.
  - The detailed bucket-by-bucket risk weights for the SA — the source is regulatory text, not a programming reference; the bank must consult the latest consolidated version.
  - The detailed 12-week stressed-window methodology — the bank must consult the latest consolidated version.
- **OCR / extraction quality**: pdftotext output is clean; the regulatory text is well-structured.
- **Translation**: English.
