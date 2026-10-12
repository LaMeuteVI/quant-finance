# Chapter 6: Feature Importance Analysis

> López de Prado, MLAM, Chapter 6.

## Core Idea

**Feature importance analysis** for ML models: (1) **substitution effects** (correlated features can be substituted; MDI over-credits both), (2) **masking effects** (informative combinations are missed by single-feature measures), (3) **the Clustered Feature Importance (CFI)** algorithm (cluster the features, compute SFI per cluster, aggregate). The chapter also introduces the **Structural Feature Importance** (SFI) for time-series features.

## Key Concepts

- **MDI (Mean Decrease Impurity)** — fast, biased.
- **MDA (Mean Decrease Accuracy)** — robust, substitution-affected.
- **SFI (Single Feature Importance)** — gold standard, expensive.
- **Substitution effect** — correlated features fool MDI.
- **Masking effect** — informative combinations are missed.
- **CFI (Clustered Feature Importance)** — the institutional response.
- **Structural feature importance** — features that are *imposed* by the model (e.g. lags).
- **Random feature importance** — the importance of a randomly permuted feature; the null reference.

## Formulas & Tables

- **MDA**: `MDA_f = Acc(X) - Acc(X with feature f permuted)`.
- **CFI**: `CFI_f = (1/K) × Σ_k SFI_f` for the k-th cluster.
- **SFI**: `SFI_f = Acc(model trained only on feature f)`.

## Key Takeaways

1. MDI is fast but biased.
2. MDA is the institutional default.
3. CFI is the response to the substitution effect.

## Connects To

- ch04, ch07, `lopez-de-prado-afml` ch08.
