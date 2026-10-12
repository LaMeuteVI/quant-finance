---
name: lopez-de-prado-afml
description: "Knowledge base from Marcos López de Prado, Advances in Financial Machine Learning (Wiley 2018). Use when designing or validating ML-based trading strategies; applying purged k-fold CV with embargo, CPCV, the triple-barrier labeling method, sample-uniqueness weights, fractional differentiation, information-driven bars, meta-labeling, bet sizing, DSR, PBO, MinTRL, MDI/MDA/SFI feature importance, or Hierarchical Risk Parity. Covers 22 chapters on financial data, labeling, weights, FFD, ensembles, CV, feature importance, hyper-parameter tuning, bet sizing, the dangers of backtesting, backtest statistics, strategy risk, ML asset allocation, structural breaks, entropy and microstructural features, and HPC."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Advances in Financial Machine Learning (López de Prado)

**Source**: Marcos López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | **Domain**: Gestion de portefeuille | **Chapters**: 22 | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview.
- **With a topic or framework name** (e.g. "DSR", "purged k-fold", "triple-barrier", "HRP", "CPCV"): jump to the relevant chapter.
- **With a chapter number**: open `chapters/chNN-*.md`.
- **For institutional thresholds**: see `cheatsheet.md` (DSR, PBO, MinTRL, Harvey-Liu 3.0 t-stat, Kelly multiplier, etc.).

## Core Frameworks & Mental Models

1. **The Triple-Barrier Labeling Method** (ch03): vertical barrier + profit-taking + stop-loss. The institutional default for financial labels.
2. **Information-Driven Bars** (ch02): TIB/VIB/TRB. The right unit for ML on financial data; time bars are not stationary.
3. **Sample Uniqueness** (ch03, ch04): the measure of how much an observation "owns" its label; the effective sample size is typically 1/3 to 1/5 of the nominal.
4. **Fractional Differentiation (FFD)** (ch05): `(1−x)^d` with `d ∈ [0, 1]`. The FFD threshold `d*` is the smallest `d` for which the ADF test rejects; typically 0.2–0.5.
5. **Purged K-Fold CV with Embargo** (ch07): the CV for financial time series. Standard k-fold leaks information.
6. **Combinatorial Purged Cross-Validation (CPCV)** (ch07, ch12): the multi-path version; N=6, k=3 gives 20 paths.
7. **The Deflated Sharpe Ratio (DSR)** (ch14): the SR corrected for the number of trials, skew, kurtosis. A SR of 2.5 is *expected* under the null with 100 trials.
8. **The Probability of Backtest Overfitting (PBO)** (ch14): the probability that the best IS strategy is the worst OOS. Computed via CSCV.
9. **The Minimum Track Record Length (MinTRL)** (ch14, ch15): the minimum number of bets to confirm a strategy. For SR=1, 95% confidence: ~5 years of monthly data.
10. **Meta-Labeling + Bet Sizing** (ch03, ch10): primary model → direction; secondary model → probability of being correct; bet size = `meta_prob × 1/σ̂_t`.
11. **The Fractional Kelly Criterion** (ch10): `f* = (p × b − q) / b`; the institutional default is `0.5 × f*`.
12. **The Three Feature Importances** (ch08): MDI (fast, biased), MDA (robust, substitution-affected), SFI (gold standard, expensive).
13. **Hierarchical Risk Parity (HRP)** (ch16): the ML-based asset allocation algorithm. More robust than mean-variance to estimation error.
14. **The Three Sizing Strategies** (ch10): Strategy 1 (constant), Strategy 2 (inverse-vol), Strategy 3 (mixed).
15. **The Seven Pathologies of Backtesting** (ch11): multiple testing, backtest overfitting, leakage, non-stationarity, survivorship, strategy crowding, false discovery.
16. **The Triangular Relationship** (ch15): SR, statistical confidence, time horizon are linked. MinTRL is the institutional measure of the required history.

## Chapter Index

| # | Title | Key Frameworks | File |
|---|---|---|---|
| 1 | FML as a Distinct Subject | FML definition; the seven pathologies | [ch01](./chapters/ch01-financial-machine-learning-as-a-distinct-subject.md) |
| 2 | Financial Data Structures | Information-driven bars (TIB, VIB, TRB) | [ch02](./chapters/ch02-financial-data-structures.md) |
| 3 | Labeling | Triple-barrier, meta-labeling, uniqueness | [ch03](./chapters/ch03-labeling.md) |
| 4 | Sample Weights | Sequential bootstrap, snippet bootstrap | [ch04](./chapters/ch04-sample-weights.md) |
| 5 | Fractionally Differentiated Features | FFD, ADF test, fixed-width window | [ch05](./chapters/ch05-fractionally-differentiated-features.md) |
| 6 | Ensemble Methods | Bagging, random forest, boosting, stacking | [ch06](./chapters/ch06-ensemble-methods.md) |
| 7 | Cross-Validation in Finance | Purged k-fold, embargo, CPCV | [ch07](./chapters/ch07-cross-validation-in-finance.md) |
| 8 | Feature Importance | MDI, MDA, SFI, substitution/masking | [ch08](./chapters/ch08-feature-importance.md) |
| 9 | Hyper-Parameter Tuning with CV | (placeholder) | |
| 10 | Bet Sizing | Three strategies, fractional Kelly | [ch10](./chapters/ch10-bet-sizing.md) |
| 11 | The Dangers of Backtesting | The seven pathologies | [ch11](./chapters/ch11-the-dangers-of-backtesting.md) |
| 12 | Backtesting through Cross-Validation | CPCV backtest path, distribution of SR | [ch12](./chapters/ch12-backtesting-through-cross-validation.md) |
| 13 | Backtesting on Synthetic Data | Stress testing, Monte Carlo | [ch13](./chapters/ch13-backtesting-on-synthetic-data.md) |
| 14 | Backtest Statistics | DSR, PBO, MinTRL, BSR | [ch14](./chapters/ch14-backtest-statistics.md) |
| 15 | Understanding Strategy Risk | Triangular relationship, Bayesian update | [ch15](./chapters/ch15-understanding-strategy-risk.md) |
| 16 | Machine Learning Asset Allocation | HRP, NCO, minimum-variance | [ch16](./chapters/ch16-machine-learning-asset-allocation.md) |
| 17 | Structural Breaks | CUSUM, Chow, SupF, Bai-Perron | [ch17](./chapters/ch17-structural-breaks.md) |
| 18 | Entropy Features | (placeholder) | |
| 19 | Microstructural Features | (placeholder) | |
| 20 | Multiprocessing and Vectorization | (placeholder) | |
| 21 | Brute Force and Quantum Computers | (placeholder) | |
| 22 | High-Performance Computational Intelligence | (placeholder) | |

(Chapters 9, 18–22 are placeholders for the next iteration; the load-bearing chapters for the agent are 1–17.)

## Topic Index

- **Bagging** → ch06
- **Bar (information-driven)** → ch02
- **Bayesian Sharpe Ratio (BSR)** → ch14
- **Betting sizing** → ch10
- **BVC (Bulk Volume Classification)** → ch02
- **Carino smoothing** → cf. `grinold-kahn-apm` ch17
- **Clustered feature importance** → ch08
- **Combinatorial Purged Cross-Validation (CPCV)** → ch07, ch12
- **Combinatorially Symmetric Cross-Validation (CSCV)** → ch14
- **CUSUM test** → ch17
- **Deflated Sharpe Ratio (DSR)** → ch14
- **Dollar bar** → ch02
- **Embargo** → ch07
- **Ensemble** → ch06
- **Entropy features** → ch18
- **Feature importance** → ch08
- **FML (Financial Machine Learning)** → ch01
- **Fractional differentiation (FFD)** → ch05
- **Harvey-Liu 3.0 t-stat** → ch11, ch14
- **Hierarchical Risk Parity (HRP)** → ch16
- **Imbalance bar (TIB, VIB)** → ch02
- **Information-driven bar** → ch02
- **K-fold cross-validation** → ch07
- **Kelly criterion (fractional)** → ch10
- **Label** → ch03
- **Lee-Ready algorithm** → ch02
- **Mark-to-market vs Mark-to-model** → ch01
- **Masking effect** → ch08
- **MDA (Mean Decrease Accuracy)** → ch08
- **MDI (Mean Decrease Impurity)** → ch08
- **Meta-labeling** → ch03, ch10
- **Microstructural features** → ch19
- **Minimum Track Record Length (MinTRL)** → ch14, ch15
- **Multiple testing haircut** → ch11, ch14
- **NCO (Nested Clustered Optimisation)** → ch16
- **Out-of-bag (OOB) error** → ch06
- **Out-of-sample (OOS) test** → ch07, ch11, ch12, ch14
- **Probability of Backtest Overfitting (PBO)** → ch14
- **Purged k-fold** → ch07
- **Sample uniqueness** → ch03, ch04
- **Sample weight** → ch04
- **Sequential bootstrap** → ch04
- **SFI (Single Feature Importance)** → ch08
- **Snippet bootstrap** → ch04
- **Stacking** → ch06
- **Structural break** → ch17
- **Substitution effect** → ch08
- **Synthetic data** → ch13
- **Tick Imbalance Bar (TIB)** → ch02
- **Tick rule** → ch02
- **Time bar** → ch02
- **Triple-barrier method** → ch03
- **Volume bar** → ch02

## Supporting Files

- [glossary.md](./glossary.md) — Alphabetical glossary.
- [patterns.md](./patterns.md) — 19 patterns (the "how to" recipes).
- [cheatsheet.md](./cheatsheet.md) — The judgment layer: decision rules, thresholds, tells & smells.

## Related Skills

- **`grinold-kahn-apm`** (gestion-de-portefeuille) — The classical active management framework. AFML is the modern statistical continuation.
- **`lopez-de-prado-ml-asset-managers`** (gestion-de-portefeuille) — The 10-chapter companion volume; portfolio construction with ML signals.
- **`hull-risk-management`** (finance-de-marche) — The risk management framework; backtest of a VaR model uses the same DSR/PBO discipline.
- **`hull-derivatives`** (finance-de-marche) — Pricing and Greeks for options.
- **`diebold-mariano-forecast-accuracy`** (fondamentaux) — The DM test for forecast comparison; complements the strategy comparison.
- **`cfa-performance-measurement`** (gestion-de-portefeuille) — The GIPS-aligned performance measurement.
- **`cfa-quantitative-methods`** (fondamentaux) — The CFA QM curriculum; ARIMA, regression, hypothesis testing.
- **`tsay-analysis-financial-time-series`** (fondamentaux) — The time series foundation; GARCH, VAR, state space.
- **`chan-machine-trading`** (finance-de-marche) — Practical machine trading; factor models, time-series, AI techniques.

## Scope & Limits

- **Coverage**: 22 chapters; the 2018 edition of the canonical AFML book.
- **Edition year**: 2018 — supplemented by:
  - The 2020 companion *Machine Learning for Asset Managers* (see `lopez-de-prado-ml-asset-managers`).
  - The mlfinlab open-source library (Hudson & Thames, 2019+).
  - The finml alternative.
  - The post-2018 papers on DSR/PBO applications.
- **What the source does NOT cover**:
  - The classical active management framework (see `grinold-kahn-apm`).
  - The risk management / VaR / ES framework (see `hull-risk-management`).
  - The time-series foundation / GARCH (see `tsay-analysis-financial-time-series`).
  - The forecast evaluation tests (DM, SPA — see `diebold-mariano-forecast-accuracy`).
  - The volatility surface (see `gatheral-volatility-surface`).
  - The FRTB / Basel (see `frtb-market-risk-bcbs457`).
  - The institutional performance measurement (GIPS — see `cfa-ethics-gips`).
- **OCR / extraction quality**: pdftotext output is clean; no reconstruction needed. Some formula notation was rendered with care; agent verifies arithmetic in worked examples via Python.
- **Translation**: English.
- **Authoring quality**: every chapter file follows the standard 12-section template. Worked examples are recomputed in Python. The Connects To section links to real chapters and skills.
