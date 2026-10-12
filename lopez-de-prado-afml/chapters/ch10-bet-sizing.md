# Chapter 10: Bet Sizing

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 10, pp. 141–149

## Core Idea

A *prediction* (a signal that says "long" or "short") is not a *bet* (a sized position). The chapter introduces the three institutional ways to size a bet from a prediction: **average sizing** (constant fraction of capital), **bet-adjusted sizing** (size proportional to the inverse of the asset's volatility), and **mixed sizing** (a convex combination of the two). The signature contribution is the **meta-labeling + bet sizing pipeline**: the primary model predicts a direction; the secondary (meta) model predicts whether the primary is correct; the bet size is proportional to the meta-label probability.

## Frameworks Introduced

- **Average Sizing**:
  - `b_t = z / N`, where `z` is the total capital and `N` is the number of assets.
  - *When to use*: as the *baseline* bet sizing; the default for a long-only portfolio with no conviction.
  - *Why it works*: simple, transparent, and unbiased.
  - *Failure mode*: ignores the differing volatilities and correlations of the assets; the resulting portfolio is *not* the optimal mean-variance portfolio.

- **Bet-Adjusted Sizing (the inverse-vol sizing)**:
  - `b_i = z × s_i / Σ_j s_j`, where `s_i = 1 / σ̂_{i,t}` is the inverse of the asset's volatility.
  - *When to use*: when the manager wants the position's *dollar* volatility to be constant.
  - *Why it works*: the resulting portfolio has equal *dollar* volatility per asset, which is closer to the optimal mean-variance portfolio.
  - *Failure mode*: ignores the correlations between assets; the resulting portfolio's *total* volatility is not the target.

- **The Bet Sizing Formula `b_t = (σ̂ / σ̂_t) × m_i`**:
  - The most common institutional form: `b_t = (target_daily_dollar_vol) / (current_daily_dollar_vol) × m_i`, where `m_i` is the meta-label.
  - *When to use*: when the manager has a target vol and a meta-label.
  - *Why it works*: the formula ensures the bet size is *inversely proportional* to the realised volatility; the meta-label scales the bet by the manager's confidence.

- **The Three Sizing Strategies (the chapter's taxonomy)**:
  - *Strategy 1 (Constant)*: `b_t = 1`. Every bet is the same.
  - *Strategy 2 (Bet-adjusted)*: `b_t ∝ 1/σ̂_t`. The bet scales inversely with the asset's volatility.
  - *Strategy 3 (Mixed)*: `b_t = c × 1 + (1−c) × 1/σ̂_t`. A convex combination of constant and bet-adjusted.

- **The Meta-Labeling + Bet Sizing Pipeline**:
  1. Primary model predicts a direction (long/short/no-bet).
  2. Meta-labeler predicts whether the primary is correct (binary classification).
  3. Bet size = `meta_prob × z × 1/σ̂_t`.

## Key Concepts

1. **Average sizing** — constant fraction of capital per bet.
2. **Bet-adjusted sizing** — `1/σ̂_t` scaling; equal dollar vol per bet.
3. **Mixed sizing** — a convex combination of average and bet-adjusted.
4. **Meta-label** — the secondary model's probability that the primary model's bet is correct.
5. **Bet size** — the actual position size; the product of the meta-label and the inverse-vol scaling.
6. **Strategy 1/2/3** — the chapter's taxonomy of sizing rules.
7. **The bet sizing formula** — `b_t = (target_vol / realised_vol) × m_i`.
8. **Kelly criterion** — the optimal sizing for a binary bet; `f* = (p × b − q) / b` where `p` is the probability of winning, `q = 1−p`, `b` is the win/loss ratio. (Not the chapter's focus, but the institutional alternative.)

## Formulas & Reference Tables

**The three sizing strategies**

Strategy 1 (Constant): `b_t = 1`.
Strategy 2 (Bet-adjusted): `b_t = 1 / σ̂_t`.
Strategy 3 (Mixed): `b_t = c × 1 + (1−c) × 1 / σ̂_t`, `c ∈ [0, 1]`.

**The bet sizing formula**

`b_t = (σ̂_target / σ̂_t) × m_i`.

For a long-only portfolio, `b_t > 0`; for a long-short, `b_t ∈ [−1, 1]`.

**The Kelly criterion (binary bet)**

`f* = (p × b − q) / b`, where `p = P(win)`, `q = 1 − p`, `b = win_amount / loss_amount`.

For `p = 0.55, b = 1`: `f* = (0.55 × 1 − 0.45) / 1 = 0.10`, i.e. bet 10% of capital.

**The fractional Kelly**

`f*_fractional = 0.5 × f*` (the institutional default; halves the Kelly bet to account for estimation error and the heavy tail of returns).

## Mental Models

- **A prediction is not a bet.** A model that predicts 60% accuracy is not a strategy until the bets are sized.
- **Inverse-vol sizing is the minimum.** Equal dollar vol per bet is the institutional default; the optimal is mean-variance.
- **The meta-label scales the bet by confidence.** A high-confidence bet is larger; a low-confidence bet is smaller (or zero).
- **The Kelly criterion is dangerous in finance.** The full Kelly assumes no estimation error and a stationary win probability; the fractional Kelly is the institutional default.

## Worked Example (RECOMPUTED)

*Setup.* A long-only portfolio of 100 assets. Daily target vol = 1% of capital. Realised vol of asset `i` at time `t` is `σ̂_{i,t} = 2%` (annualised 30%). The meta-label for asset `i` is `m_i = 0.7` (70% probability of being correct).

*Step 1 — Inverse-vol scaling*.
- For each asset `i` with `σ̂_{i,t} = 0.02` (daily), the bet-adjusted size is `1 / 0.02 = 50`.
- For the portfolio, the size is `50 / Σ_j 1/σ̂_{j,t}` for the equal-weight inverse-vol portfolio.

*Step 2 — Meta-label scaling*.
- `b_t = (0.01 / 0.02) × 0.7 = 0.35`. So the bet is 35% of the target vol × meta-label product.

*Step 3 — Kelly (binary bet, p = 0.7, b = 1)*.
- `f* = (0.7 × 1 − 0.3) / 1 = 0.4`, i.e. 40% of capital.
- Fractional Kelly (0.5×): `f*_fractional = 0.20`. So the bet is 20% of capital.
- Note: the Kelly criterion is for a *single* binary bet; for a portfolio of correlated bets, the Kelly is reduced by the average correlation.

*Sanity check (Python).*
```python
sigma_d, sigma_target, m = 0.02, 0.01, 0.7
b = (sigma_target / sigma_d) * m
print(f"Bet size (target-vol × meta-label): {b:.2%}")

p, b_kelly = 0.7, 1.0
f_kelly = (p * b_kelly - (1-p)) / b_kelly
print(f"Kelly f*: {f_kelly:.2%}, Fractional: {f_kelly/2:.2%}")
```

## Anti-patterns

- **Confusing prediction with strategy.** A model that predicts 60% accuracy is not a strategy without the bet sizing.
- **Using equal weights (no inverse-vol scaling).** The resulting portfolio's vol is dominated by the highest-vol assets.
- **Using the full Kelly.** The full Kelly assumes no estimation error; the fractional Kelly is the institutional default.
- **Sizing by variance, not by uncertainty of the forecast.** The bet size should be inversely proportional to the *forecast uncertainty*, not the realised vol.

## Practitioner Notes

- **2026 update.** The meta-labeling + bet sizing pipeline is now standard; the `mlfinlab` library implements it. The fractional Kelly is the institutional default.
- **Vol-targeting** (the inverse-vol sizing) is the dominant institutional form. A 1% daily vol target is typical for an equity long-short fund; a 5% target is typical for a global macro fund.
- **The Kelly criterion** in continuous time is the *log-utility* optimal; in discrete time it is the geometric-mean optimal. The fractional Kelly is the institutional compromise.

## Key Takeaways

1. **A prediction is not a bet**; the bet sizing is a separate decision.
2. **Inverse-vol scaling** is the minimum; the optimal is mean-variance.
3. **Meta-labeling** scales the bet by the manager's confidence.
4. **The Kelly criterion** is dangerous in finance; the fractional Kelly is the default.
5. **Vol-targeting** is the institutional standard; a 1% daily vol is typical for an equity long-short fund.

## Connects To

- **ch03** (Labeling): the meta-label is the basis for the bet sizing.
- **ch06** (Ensemble Methods): the meta-label can be derived from an ensemble of primary models.
- **ch15** (Understanding Strategy Risk): the bet sizing is the input to the strategy risk.
- **`hull-risk-management` ch14 (Model-Building Approach)**: the bet size is the input to the portfolio VaR.
- **`grinold-kahn-apm` ch14 (Portfolio Construction)**: the bet sizing is the equivalent of the construction in a Kelly-style framework.
