# Chapter 8: Testing Set Overfitting

> López de Prado, MLAM, Chapter 8.

## Core Idea

**Testing set overfitting** is the problem that the test set itself can be overfit if the model is selected on it. The chapter introduces the **SPA test** (Hansen 2005), the **Reality Check** (White 2000), and the **PBO (Probability of Backtest Overfitting)** via CSCV. The institutional response: (1) never use the test set for model selection, (2) use CPCV for the OOS performance, (3) use the DSR/PBO/SPA for statistical validation.

## Key Concepts

- **Testing set overfitting** — the test set is overfit if used for model selection.
- **SPA test** — Hansen 2005; the bootstrap-based test.
- **Reality Check** — White 2000; the familywise error rate.
- **PBO** — the probability that the best IS strategy is the worst OOS.
- **CSCV** — the basis for PBO.
- **The "look-ahead" bias in the test set** — the same as the training set; the institutional danger.
- **The DSR** — the multiple-testing correction.
- **The "best strategy" trap** — the best IS strategy is often the worst OOS.

## Formulas & Tables

- **SPA test**: `T_SPA = max_{k=1..N_t} (SR_k - SR_benchmark)`, with bootstrap p-value.
- **PBO**: `PBO = (1/M) × Σ I{best_IS = worst_OOS}` over `M` CSCV splits.

## Key Takeaways

1. Never use the test set for model selection.
2. Use SPA / Reality Check / PBO for statistical validation.
3. The DSR is the multiple-testing correction.

## Connects To

- ch04, `lopez-de-prado-afml` ch11, ch12, ch14, `diebold-mariano-forecast-accuracy`.
