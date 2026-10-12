---
name: diebold-mariano-forecast-accuracy
description: "Knowledge base from Diebold & Mariano (1995) Comparing Predictive Accuracy, JBES 13(3) 253-280. Use when comparing the predictive accuracy of two competing forecasts (with the DM test, including the Harvey-Leybourne-Newbold 1997 small-sample correction, the Clark-West 2001 nested-forecast correction, and the 2026 extensions: White Reality Check 2000, Hansen SPA 2005, Harvey-Liu 2015 multiple-testing haircut, Bailey-Lopez de Prado Deflated Sharpe Ratio 2014). Covers the loss-function framework (squared, absolute, asymmetric Linex), the HAC variance estimator (Newey-West 1987), the asymptotic N(0,1) distribution, and the 2026 institutional decision tree for forecast comparison."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Comparing Predictive Accuracy (Diebold & Mariano, 1995)

**Source**: Francis X. Diebold & Roberto S. Mariano, "Comparing Predictive Accuracy", *Journal of Business & Economic Statistics* 13(3), 253–280 (1995) | **Domain**: Fondamentaux | **Chapters**: 5 | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview.
- **With a topic or framework name** (e.g. "DM test", "HLN correction", "Clark-West", "SPA", "Reality Check"): jump to the relevant chapter.
- **With a chapter number**: open `chapters/chNN-*.md`.
- **For the 2026 institutional decision tree**: see ch05.

## Core Frameworks & Mental Models

1. **The Diebold–Mariano (DM) Test Statistic** (ch01): `DM = d̄ / √(V̂(d̄))`, with `d_t = e_{1t} − e_{2t}`. Under H0 (equal accuracy), `DM ~ N(0, 1)` asymptotically.
2. **The General Loss Function** (ch01): the loss `L(e_t)` can be squared, absolute, asymmetric, or any other function; the DM test is *non-parametric* in the loss.
3. **The HAC Variance Estimator** (ch01, ch02): the Newey-West (1987) estimator with bandwidth `H = ⌊N^(1/3)⌋`; robust to serial and contemporaneous correlation in the loss differences.
4. **The HLN (1997) Small-Sample Correction** (ch01, ch05): `DM* = DM / √((N + 1 − 2h + h(h−1)/N) / N)`. Essential for N < 100.
5. **The Clark-West (2001) Nested-Forecast Correction** (ch05): when forecast 2 nests forecast 1, the standard DM test reverses sign in small samples. The Clark-West adjustment subtracts the sample variance of the forecast-error-difference increment.
6. **The Hansen (2005) Superior Predictive Ability (SPA) Test** (ch05): the bootstrap-based test for whether the *best* of many models is significantly better than a benchmark. Use when comparing many models.
7. **The White (2000) Reality Check** (ch05): the bootstrap-based test for the familywise error rate. Use when comparing a model against a set of alternatives.
8. **The Harvey-Liu 2015 Multiple-Testing Haircut** (ch05): the 3.0 t-stat threshold for financial anomalies. Use when comparing anomalies across the cross-section.
9. **The Deflated Sharpe Ratio (DSR)** (ch05, cross-ref `lopez-de-prado-afml`): the SR corrected for the number of trials, skew, and kurtosis. Use when comparing backtest SRs.
10. **The Diebold-Mariano (2002) Multivariate Extension** (ch05): the multivariate DM test for vector forecasts. Use when forecasting multiple time series simultaneously.

## Chapter Index

| # | Title | File |
|---|---|---|
| 1 | Testing Equality of Forecast Accuracy | [ch01](./chapters/ch01-testing-equality-of-forecast-accuracy.md) |
| 2 | Extant Tests (the pre-1995 landscape) | [ch02](./chapters/ch02-extant-tests.md) |
| 3 | Monte Carlo Analysis (size and power) | [ch03](./chapters/ch03-monte-carlo-analysis.md) |
| 4 | An Empirical Example (exchange rates) | [ch04](./chapters/ch04-an-empirical-example.md) |
| 5 | Conclusions and Future Research (with 2026 update) | [ch05](./chapters/ch05-conclusions-and-future-research.md) |

## Topic Index

- **Asymptotic distribution** → ch01
- **Bandwidth `H`** → ch01
- **Cox (1961) test** → ch02
- **DM statistic** → ch01
- **Differential loss `d_t`** → ch01
- **Diebold-Granger (1983) sign test** → ch02
- **Familywise error rate** → ch05
- **HAC variance** → ch01, ch02
- **HLN (1997) small-sample correction** → ch01, ch05
- **Loss function `L(e)`** → ch01
- **MGN (1980) test** → ch02
- **Newey-West (1987) estimator** → ch01
- **Reality Check (White 2000)** → ch05
- **SPA (Hansen 2005)** → ch05
- **SPA nested (Clark-West 2007)** → ch05
- **DSR (Bailey-Lopez de Prado 2014)** → ch05, cross-ref `lopez-de-prado-afml` ch14

## Supporting Files

- [glossary.md](./glossary.md) — Alphabetical glossary.

## Related Skills

- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — ch14 (Backtest Statistics) covers the DSR, PBO, MinTRL — the modern extensions of the DM test.
- **`hull-risk-management`** (finance-de-marche) — ch12 (VaR and ES) — the backtest of a VaR model uses the same DM-style comparison.
- **`grinold-kahn-apm`** (gestion-de-portefeuille) — ch20 (The Historical Record) — the comparison of mutual fund performance uses related tests.
- **`tsay-analysis-financial-time-series`** (fondamentaux) — ch08 (VAR) — the multivariate DM test is used in multivariate forecasting.
- **`cfa-quantitative-methods`** (fondamentaux) — the regression and time-series foundation.

## Scope & Limits

- **Coverage**: 5 sections of the 1995 paper. The paper is short (11 pages, 8 pages of body); the skill is correspondingly compact.
- **OCR / extraction quality**: ⚠ The source PDF is scanned; the extraction was done with tesseract (400 dpi). Mathematical notation in the extraction is unreliable; every formula in the skill is *reconstructed* from expertise and marked with **⚠ reconstructed (OCR source)**.
- **Edition year**: 1995 — supplemented by 30 years of extensions:
  - HLN (1997): small-sample correction.
  - Clark-West (2001, 2007): nested-forecast correction.
  - White (2000) Reality Check: many-model test.
  - Hansen (2005) SPA: superior predictive ability.
  - Harvey, Liu & Zhu (2015): 3.0 t-stat haircut for the cross-section of anomalies.
  - Bailey & López de Prado (2014): DSR for backtest SRs.
  These extensions are integrated into ch05 as a "⚠ Practitioner update" with a 2026 institutional decision tree.
- **What the source does NOT cover**:
  - The ML-based backtest statistics (see `lopez-de-prado-afml`).
  - The volatility surface (see `gatheral-volatility-surface`).
  - The classical active management framework (see `grinold-kahn-apm`).
  - The FRTB / Basel (see `frtb-market-risk-bcbs457`).
- **Translation**: English.
