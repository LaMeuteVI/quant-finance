# Chapter 5: Financial Labels

> López de Prado, MLAM, Chapter 5.

## Core Idea

**Financial labels** are the targets for ML models. Beyond the **triple-barrier** (see `lopez-de-prado-afml` ch03), this chapter introduces the **dynamic meta-labelling**: the primary model generates a *direction*; the secondary model (the meta-labeller) is trained on the *side* of the primary model's bet. The labels are then **categorical** (the side, the size, the holding period), not just binary.

## Key Concepts

- **Triple-barrier label** — vertical, profit-taking, stop-loss (ch03 of AFML).
- **Dynamic barrier** — the barriers depend on the realised vol.
- **Meta-label** — the secondary model's target (binary: primary was right or wrong).
- **Multi-class label** — the side (long/short/no-bet) and the size.
- **Side bet** — long or short; the institutional position.
- **Size bet** — the meta-labeller; the institutional size.
- **The "what to predict" question** — direction, side, size, holding period; the institutional framework.

## Key Takeaways

1. Triple-barrier is the institutional default.
2. Meta-labelling is for *sizing*, not for *predicting*.
3. Multi-class labels are essential for institutional strategies.

## Connects To

- ch06 (Feature Importance), ch07 (Portfolio Construction), `lopez-de-prado-afml` ch03, ch10.
