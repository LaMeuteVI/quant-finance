# Chapter 4: Artificial Intelligence Techniques

> Chan, *Machine Trading*, Chapter 4. ML for trading: classification, regression, deep learning.

## Core Idea

**AI/ML techniques** for trading include (1) **supervised learning** (random forest, gradient boosting, neural networks), (2) **unsupervised learning** (PCA, k-means, hierarchical clustering), (3) **reinforcement learning** (Q-learning, policy gradient). The institutional caution: ML models overfit easily; the discipline of **purged cross-validation** (LdP ch07) and **DSR** (LdP ch14) is required.

## Key Concepts

- **Supervised learning** — the model learns from labelled examples.
- **Unsupervised learning** — the model finds structure in unlabelled data.
- **Reinforcement learning** — the model learns from rewards.
- **Random forest** — bagging of decision trees.
- **Gradient boosting** (XGBoost, LightGBM, CatBoost) — sequential fitting of residuals.
- **Neural networks** — deep learning; convolutional, recurrent, attention-based.
- **Overfitting** — the model fits noise; the institutional danger.
- **Purged cross-validation** — the discipline of out-of-sample testing on time series.
- **DSR / PBO** — the backtest statistics that correct for overfitting.
- **Feature importance** — MDI, MDA, SFI; see `lopez-de-prado-afml` ch08.

## Key Takeaways

1. ML models can detect non-linear patterns but overfit easily.
2. Purged CV and DSR are the institutional discipline.
3. Feature importance is essential for interpretability.

## Connects To

- ch01 (Basics), ch02 (Factor Models), `lopez-de-prado-afml` ch07 (CV), ch08 (Feature Importance), ch14 (DSR).
