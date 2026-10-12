# Chapter 4: Sample Weights

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 4, pp. 59–73

## Core Idea

A *sample weight* is a number attached to each observation that tells the model how much to "trust" that observation. In finance, the natural weight is the **sample uniqueness** (ch03): an observation that is *unique* in its label window is more informative than one that is concurrent with many others. The chapter introduces the **average uniqueness** and the **sequentially bootstrapped** algorithm that draws a bootstrap sample respecting the uniqueness.

## Frameworks Introduced

- **Sample Uniqueness `u_i`** (recap from ch03):
  - `c_t = Σ_i 1_{t,i}` (concurrent labels at time `t`).
  - `u_i = (Σ_t c_t × 1_{t,i}) / (c_i × Σ_t c_t)`.
  - `ū = (1/N) × Σ_i u_i`.

- **Sequential Bootstrapping**:
  - The standard bootstrap (iid with replacement) over-represents observations with low uniqueness.
  - The sequential bootstrap is a Markov chain: at each step, draw an observation with probability proportional to its current uniqueness; mark the observation's interval as "used" and reduce the uniqueness of any observation that overlaps.
  - The result: a bootstrap sample that has the same average uniqueness as the original.

- **The "Number of Snippets" Approach**:
  - An alternative to sequential bootstrapping: divide the data into "snippets" (contiguous blocks); each snippet has its own weight; the bootstrap draws snippets with replacement.

- **The "Weighting by Return" Approach**:
  - A simpler alternative: weight each observation by the magnitude of its return. The intuition: large returns are more informative than small ones.
  - The drawback: the weighting is biased toward volatile regimes; the model over-fits to the high-vol period.

## Key Concepts

1. **Sample weight** — a number attached to each observation; the model trusts more-weighted observations more.
2. **Sample uniqueness** — the measure of how much an observation "owns" its label.
3. **Sequential bootstrap** — a Markov chain that draws observations respecting the uniqueness.
4. **Snippet** — a contiguous block of observations; an alternative unit of sampling.
5. **Average uniqueness `ū`** — the mean uniqueness over all observations.
6. **Effective sample size `N_eff = ū × N`** — the number of "independent" observations.
7. **Time-decay weighting** — exponential decay of weights with time; emphasises recent observations.

## Formulas & Reference Tables

**Sample uniqueness**

`u_i = (Σ_t c_t × 1_{t,i}) / (c_i × Σ_t c_t)`, with `c_t = Σ_i 1_{t,i}`.

**Average uniqueness**

`ū = (1/N) × Σ_i u_i`.

**Effective sample size**

`N_eff = ū × N`.

**Sequential bootstrap probability**

`P(i is drawn at step s+1) = u_i^{(s)} / Σ_j u_j^{(s)}`, where `u_i^{(s)}` is the uniqueness of observation `i` after `s` draws.

**Time-decay weighting**

`w_i = exp(−λ × (T − t_i))`, where `T` is the latest date, `t_i` is the date of observation `i`, and `λ` is the decay rate.

## Mental Models

- **Standard bootstrap over-represents non-unique observations.** Use sequential bootstrap.
- **Average uniqueness is the *only* honest measure of sample size.** The nominal N is over-stated.
- **Time-decay weighting is essential in finance.** Recent data is more relevant than old data.

## Worked Example (RECOMPUTED)

*Setup.* 1000 daily observations with 5-day label windows. 200 unique snippets.

*Step 1 — Compute uniqueness*.
- `c_t ≈ 5`, `ū ≈ 0.2`, `N_eff ≈ 200`.

*Step 2 — Sequential bootstrap*.
- At each step, draw an observation with probability proportional to its current uniqueness; reduce the uniqueness of any overlapping observation.

*Step 3 — Verify average uniqueness in the bootstrap*.
- The bootstrap sample should have the same average uniqueness as the original.

## Anti-patterns

- **Using iid bootstrap on financial data.** Always use sequential bootstrap or snippet bootstrap.
- **Ignoring sample uniqueness.** The IC of a signal is much lower when computed on non-unique observations.
- **Equal weighting on time-decayed data.** Recent data should be weighted more.

## Key Takeaways

1. **Sample uniqueness** is the most under-used concept; the effective sample size is typically 1/3 to 1/5 of the nominal size.
2. **Sequential bootstrap** is the institutional default; iid bootstrap over-represents non-unique observations.
3. **Time-decay weighting** is essential in finance.
4. **Snippet bootstrap** is an alternative when sequential bootstrap is too slow.

## Connects To

- **ch03** (Labeling): the `t_0, t_1` interval is the basis for the uniqueness.
- **ch07** (Cross-Validation in Finance): the CPCV purging uses the same interval logic.
- **ch12** (Backtesting through Cross-Validation): the CPCV backtest uses the unique observations.
