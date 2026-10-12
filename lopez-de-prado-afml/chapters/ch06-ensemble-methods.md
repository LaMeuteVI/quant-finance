# Chapter 6: Ensemble Methods

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 6, pp. 93–102

## Core Idea

An *ensemble* combines multiple models to produce a single forecast. The chapter introduces the three institutional ensembles: **bagging** (bootstrap-aggregating), **boosting** (sequential fitting of residuals), and **stacking** (meta-learning over the predictions of base models). The signature contribution is the **bagging classifier for an imbalanced dataset**: when one class is rare (e.g. a "long" signal with only 30% positives), the standard bootstrap over-samples the majority class.

## Frameworks Introduced

- **Bagging (Bootstrap-Aggregating)**:
  - Draw `M` bootstrap samples; fit a model to each; predict by majority vote (classification) or average (regression).
  - The variance reduction: `Var(ensemble) = ρ × σ² + (1 − ρ) × σ² / M`, where `ρ` is the correlation between models. Bagging reduces variance only if `ρ < 1`.

- **Random Forest** (the bagging-of-trees):
  - At each split, randomly select a subset of features; this decorrelates the trees.

- **Boosting (AdaBoost, Gradient Boosting)**:
  - Sequential: each model fits the *residual* of the previous.
  - AdaBoost: reweight observations by the previous model's error.
  - Gradient Boosting: fit the negative gradient of the loss function.

- **Stacking**:
  - A meta-model that combines the predictions of base models.
  - The base models are first-level; the meta-model is second-level.
  - The meta-model is trained on out-of-sample predictions of the base models (to avoid leakage).

- **The Bagging Classifier for Imbalanced Classes**:
  - When the positive class is rare, the standard bootstrap (uniform with replacement) draws a sample that is also imbalanced.
  - The fix: under-sample the majority class *or* over-sample the minority class *or* use a *balanced* bootstrap (draw with probability proportional to the inverse class frequency).

## Key Concepts

1. **Bagging** — bootstrap-aggregating; variance reduction via averaging.
2. **Random forest** — bagging of decision trees with random feature selection.
3. **Boosting** — sequential fitting of residuals.
4. **Stacking** — meta-learning over base models.
5. **Balanced bootstrap** — bootstrap that respects the class proportions.
6. **Bagging classifier (imbalanced)** — the sklearn class `BalancedBaggingClassifier`.
7. **The "Out-of-Bag" (OOB) error** — the error of a bagged model on the observations not in its bootstrap sample; an honest OOS estimate.

## Formulas & Reference Tables

**The ensemble variance**

`Var(ensemble) = ρ × σ² + (1 − ρ) × σ² / M`. For `M` uncorrelated models (`ρ = 0`): `Var = σ² / M`. For perfectly correlated models (`ρ = 1`): `Var = σ²` (no reduction).

**The OOB error**

`OOB = (1/N) Σ_i 1{y_i ≠ ŷ_i^OOB}`, where `ŷ_i^OOB` is the average prediction of the models that did *not* see observation `i` in their bootstrap sample.

**The bagging classifier for imbalanced classes**

`P(i is drawn at step s+1) = (1/c_i) / Σ_j (1/c_j)`, where `c_i` is the class of observation `i` (1 for positive, 0 for negative). The result: balanced classes in each bootstrap sample.

## Mental Models

- **Bagging reduces variance; boosting reduces bias.** The two are complementary.
- **Stacking is the most powerful** but the most prone to leakage; the meta-model must be trained on OOS predictions.
- **Imbalanced classes are the default in finance**; the standard bootstrap is wrong.
- **OOB error is a free OOS estimate**; the agent should always report it.

## Worked Example (RECOMPUTED)

*Setup.* A binary classification problem with 1000 observations, 200 positives (20%). Bagging with 100 trees.

*Step 1 — Standard bootstrap*:
- The bootstrap sample has ~63.2% unique observations; the positives are ~20% of the sample.
- The classifier is biased toward the majority class.

*Step 2 — Balanced bootstrap*:
- Draw with probability proportional to 1/class_frequency.
- The bootstrap sample has 50% positives and 50% negatives.
- The classifier is balanced.

*Step 3 — OOB error*:
- For each observation, predict using the trees that did *not* see it.
- The OOB error is the average misclassification rate.

## Anti-patterns

- **Using standard bootstrap on imbalanced data.** Use balanced bootstrap.
- **Stacking with leakage.** The meta-model must be trained on OOS predictions.
- **Trusting the in-sample accuracy of an ensemble.** Use OOB error.

## Key Takeaways

1. **Bagging reduces variance; boosting reduces bias.**
2. **Random forest** is bagging + random feature selection.
3. **Stacking is the most powerful** but requires OOS predictions for the meta-model.
4. **Imbalanced classes are the default in finance**; balanced bootstrap is essential.
5. **OOB error** is a free OOS estimate.

## Connects To

- **ch03** (Labeling): the imbalanced class problem comes from the labelling rule.
- **ch07** (Cross-Validation in Finance): the stacking OOS predictions require purged CV.
- **ch08** (Feature Importance): the ensemble's feature importance is the average of the trees' importances.
- **ch10** (Bet Sizing): the ensemble prediction is the input to the bet sizing.
- **`grinold-kahn-apm` ch11 (Advanced Forecasting)**: the modern version of the refinement problem.
