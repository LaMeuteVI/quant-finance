# Chapter 8: Feature Importance

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 8, pp. 113–127

## Core Idea

A *feature importance* tells you which input features the model relies on. The chapter introduces three families: **mean decrease impurity (MDI)** (the total reduction in impurity from splits on the feature, summed over all trees), **mean decrease accuracy (MDA)** (the decrease in OOS accuracy when the feature is randomly permuted), and **single feature importance (SFI)** (the OOS accuracy of a model trained on a single feature). The signature contribution is the **substitution effect** and the **masking effect**: when two features are highly correlated, MDI can over-credit the redundant feature; MDA can be fooled by the permutation finding a different redundant feature; the result is *misleading* feature importance.

## Frameworks Introduced

- **MDI (Mean Decrease Impurity)**:
  - For each tree, sum the impurity reduction from all splits on the feature; aggregate over the forest.
  - Fast (computed during training).
  - Biased toward high-cardinality features (features with many unique values get more splits).

- **MDA (Mean Decrease Accuracy, a.k.a. permutation importance)**:
  - For each feature, permute its values; measure the OOS accuracy of the model.
  - The decrease in accuracy is the feature's importance.
  - Robust to feature cardinality.
  - Subject to the *substitution* effect: if two features are highly correlated, permuting one may not affect the prediction because the model uses the other.

- **SFI (Single Feature Importance)**:
  - Train a model on a single feature; measure the OOS accuracy.
  - Robust to substitution and masking.
  - The cost: requires `K` separate models (one per feature).

- **The Substitution and Masking Effects**:
  - *Substitution*: feature A and feature B are correlated; MDI credits both, but the model could use either.
  - *Masking*: feature A is informative only in combination with feature B; MDI credits A but the individual importance is low.

- **The Clustered Feature Importance (CFI)**:
  - Cluster features by correlation; compute the SFI for each cluster; aggregate.

## Key Concepts

1. **Feature importance** — a measure of how much the model relies on a feature.
2. **MDI (Mean Decrease Impurity)** — fast, biased toward high-cardinality features.
3. **MDA (Mean Decrease Accuracy)** — robust, subject to substitution effect.
4. **SFI (Single Feature Importance)** — robust, expensive.
5. **Substitution effect** — correlated features can be substituted; MDI over-credits both.
6. **Masking effect** — informative combinations are missed by single-feature measures.
7. **CFI (Clustered Feature Importance)** — clusters features; computes SFI per cluster.

## Formulas & Reference Tables

**MDI**

`MDI_f = (1/M) Σ_{m=1}^{M} Σ_{t ∈ T_m, t splits on f} ΔI(t)`, where `ΔI(t)` is the impurity reduction at split `t`.

**MDA (permutation importance)**

`MDA_f = Acc_OOS (X) − Acc_OOS (X with feature f permuted)`.

**SFI**

`SFI_f = Acc_OOS (model trained only on feature f)`.

## Mental Models

- **MDI is fast but biased.** Use it as a first filter; not for the final feature set.
- **MDA is the institutional default.** Use it for the final feature set.
- **SFI is the gold standard** but expensive; use it for the top 10–20 features.
- **Correlated features are the default in finance**; the substitution effect is pervasive.

## Worked Example (RECOMPUTED)

*Setup.* 1000 observations, 50 features, 20 of which are informative. Random forest with 100 trees.

*Step 1 — MDI*:
- The 20 informative features get high MDI; the 30 noise features get low MDI.
- But correlated features (e.g. 5 features measuring the same underlying) all get high MDI; the model over-counts the *effective* number of features.

*Step 2 — MDA**:
- Permute each feature; measure the accuracy drop.
- The 20 informative features get high MDA; the 30 noise features get low MDA.
- The substitution effect: 5 highly correlated features may all get low MDA (because the model uses the other 4).

*Step 3 — SFI**:
- Train 50 separate models, each on a single feature.
- The 20 informative features get high SFI; the 30 noise features get low SFI.
- The substitution effect is avoided (each model is forced to use only one feature).

## Anti-patterns

- **Trusting MDI for the final feature set.** Always use MDA or SFI.
- **Ignoring the substitution effect.** With correlated features, MDI over-counts; MDA under-counts.
- **Using SFI on 100+ features.** Too expensive; use MDA as a pre-filter.

## Key Takeaways

1. **MDI is fast but biased**; use it as a first filter.
2. **MDA is the institutional default** for the final feature set.
3. **SFI is the gold standard** but expensive; use for top 10–20 features.
4. **The substitution effect** is pervasive in finance; correlated features fool all three measures.
5. **Clustered feature importance (CFI)** is the institutional response to the substitution effect.

## Connects To

- **ch05** (Fractionally Differentiated Features): the FFD features can be ranked by MDI / MDA / SFI.
- **ch06** (Ensemble Methods): the ensemble's feature importance is the average over the trees.
- **ch09** (Hyper-Parameter Tuning with Cross-Validation): the feature set is one of the hyper-parameters.
