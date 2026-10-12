# Chapter 9: Valuation in Practice

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 9, pp. 225–260

## Core Idea

Theory assumes the consensus is **known and noise-free**; in practice the consensus must be **estimated**, and the estimate has two components — model error (the wrong factors) and estimation error (the right factors, but `λ` and `β` measured with noise). The first half of the chapter is a tour of practical consensus construction (macro consensus, fundamental consensus, implied cost of capital); the second half is the **decomposition of error** that lets an active manager decide where to invest research dollars.

The chapter's most important message is that **a manager who does not know their consensus is flying blind** — every alpha is contaminated with consensus error.

## Frameworks Introduced

- **Three practical consensus constructions**:
  1. *Historical-consensus*: average realised returns; has the lowest variance but is the noisiest in expected-return terms.
  2. *Macroeconomic-consensus*: factor premia from the macro view (consumption, labor); lower variance, needs strong modelling.
  3. *Fundamental-consensus*: cross-sectional regressions of returns on fundamentals (P/E, P/B, P/CF); mid-variance, often the institutional default.
  - *When to use*: most institutions use a *blend*, weighted by the variance of each method.
  - *Failure mode*: historical consensus dominates long-horizon investors' portfolios and biases every active view.

- **The Tracking-Error Decomposition**: the realised tracking error of an active manager splits into
  `TE = √(α' V^(-1) α + ε' Σ ε)` — signal-based alpha plus consensus estimation error.
  - *Why it matters*: the part of TE that is not signal-driven is dead weight — the manager is being paid for nothing.
  - *Failure mode*: the manager does not measure this decomposition and believes their tracking error reflects their skill.

- **The Value-Added Decomposition**: the mean-variance objective (the basic Grinold–Kahn optimisation) gives value-added
  `VA = 0.5 × (IC × √B)^2 × σ_θ(M)` — proportional to the square of the information ratio and to the benchmark's residual volatility.
  - *Why it matters*: shows that small improvements in IC and breadth translate nonlinearly into value-added.
  - *Failure mode*: treating the IR as the only metric; in fact IR^2 × σ_θ is what the investor captures.

## Key Concepts

1. **Implied cost of capital** — the discount rate that equates a stock's price to the present value of forecasted cash flows; the "consensus" of the equity market.
2. **Consensus estimation error** — the variance of the consensus estimate; one of the two irreducible sources of tracking error.
3. **Realised tracking error** — the ex-post standard deviation of the manager's active return; the empirical analogue of expected tracking error.
4. **Information ratio (IR)** — the ratio of expected active return to tracking error; the single statistic that defines active management.
5. **Earnings yield** — the inverse of the P/E; the simplest fundamental signal.
6. **Graham's formula** — `Value = (EPS × (8.5 + 2g) × 4.4) / Y`, where `Y` is the AAA corporate bond yield, `g` is the expected five-year growth rate, and the constants are the empirical intercept and slope from a 1962 regression of price on earnings.
7. **Bodie–Roe** — the fundamental view's algebra: equilibrium expected return = (dividend yield) + g (the long-run growth rate).
8. **Mean reversion** — the empirical fact that long-horizon returns are *negatively* autocorrelated, suggesting that the historical consensus over-weights long-run premia.

## Formulas & Reference Tables

**Graham's formula (re-stated)**

`V = (EPS × (8.5 + 2g) × 4.4) / Y`

where `EPS` is the trailing earnings per share, `g` is the expected 5-year growth in % (e.g. 8 for 8%), `Y` is the AAA corporate bond yield in %, and the constant `8.5` is Graham's empirical P/E for a no-growth stock, `2` is the multiplier on growth, and `4.4` is the average AAA yield used in the original regression (he used the geometric mean AAA yield to make the result unit-free).

**Bodie–Roe (the fundamental view's expected return)**

`E[R_i] ≈ d_i / P_i + g_i`, where `d/P` is the dividend yield and `g` is the long-run growth rate of dividends.

**Realised TE squared (annualised)**

`TE^2 ≈ (12/T) Σ_{t=1}^{T} (r_{P,t} − r_{B,t})^2`, with the active return `r_{P,t} − r_{B,t}` computed monthly.

**Expected TE from the IR**

`TE_expected = (E[α] / IR)`. The IR is *TE per unit of active return*; it defines how much tracking error is required to earn a given alpha.

**Mean reversion (1-year lag of S&P 500)**

`r_{t+1} = a + b · r_t + ε_t`, with `b` estimated in the range `[−0.05, −0.10]` from monthly data, implying long-horizon variance roughly 70–80% of the iid benchmark. ⚠ The exact figure depends on the sample period; treat the 70–80% as a 1990s-era estimate.

## Mental Models

- **The consensus is a model, not a number.** Every consensus construction is a model; every model has estimation error.
- **The active manager's job is to spend tracking error efficiently.** The IR is the *efficiency* of TE; the absolute alpha is what the manager delivers.
- **Mean reversion is a consensus-rebalancing signal, not a free lunch.** Long-horizon investors must accept lower expected return if they believe in mean reversion.

## Worked Example (RECOMPUTED)

*Setup.* A stock with EPS = $5, growth g = 10%, AAA yield Y = 5%.

*Step 1 — Graham's formula.*
- `V = (5 × (8.5 + 2×10) × 4.4) / 5`
- `V = (5 × 28.5 × 4.4) / 5`
- `V = (5 × 125.4) / 5 = 125.4`

So Graham's intrinsic value is $125.40. If the market price is $100, the stock is undervalued by ~25%.

*Step 2 — Implied expected return (Bodie–Roe).* Assume a 2% dividend yield and 6% long-run growth.
- `E[R_i] = 2% + 6% = 8%`
- This is the consensus: anyone who buys at $100 expects to earn 8% per year.

*Step 3 — A fundamental alpha.* Suppose a long-run growth estimate of 8% (not 6%); then
- `E[R_i] = 2% + 8% = 10%`
- `α_i = 10% − 8% = 2%`

*Sanity check (Python).*
```python
EPS, g, Y = 5.0, 10.0, 5.0   # g and Y in %
V = (EPS * (8.5 + 2*g) * 4.4) / Y
print("Graham value:", round(V, 2))   # -> 125.4

d, P, g_low, g_high = 0.02, 100, 0.06, 0.08
consensus = d + g_low
alpha_long = d + g_high
print("Consensus:", consensus)        # -> 0.08
print("Alpha    :", alpha_long - consensus)  # -> 0.02
```

## Anti-patterns

- **Using Graham's formula as a buy/sell signal in isolation.** It is a *consensus* estimator; you still need a separate alpha to deviate from it.
- **Trusting a long-run DCF projection for 30 years.** Discount rates and growth are unstable; the present value of cash flows 20+ years out is essentially a *prior* on the future.
- **Believing historical mean returns are a stable consensus.** They are not — they drift with P/E, the macro cycle, and structural change.

## Practitioner Notes

- **2026 update.** Graham's formula is now taught mostly for its historical context; modern practice uses **residual-income models (Ohlson, RIV)**, **DDM with stage-specific growth**, or **reverse DCF** to extract the implied growth assumption that justifies the current price.
- **Implied cost of capital** is the modern default. Damodaran (NYU) publishes industry-level implied cost-of-capital series; A. Frazzini, D. Kabiller & L. A. N. I. M. Israel (AQR, "Trading Costs of Daily Equities", 2018) and the Pedersen (2015) "Efficiently Inefficient" line of work all converge on implied-cost-of-capital as the consensus of choice.
- **Mean reversion is empirically weaker in the 2010s than the 1990s**; the magnitude of the long-horizon variance reduction is closer to 50% than 70% in modern data. Use the modern estimate; do not hardcode the book's 1999 figure.

## Key Takeaways

1. The consensus is a **model**, not a single number; its variance is a real, measurable, irreducible source of tracking error.
2. The manager's job is to **spend tracking error efficiently**; the IR measures that efficiency.
3. **Implied cost of capital** is the consensus of choice for modern institutional practice; Graham's formula is a teaching anchor, not a signal.
4. **Mean reversion shrinks long-horizon variance** but is weaker in modern data than the 1999 book estimates.
5. The active manager must own the consensus explicitly; no consensus, no alpha, no IR.

## Connects To

- **ch08** (Valuation in Theory): the consensus theory meets reality.
- **ch10** (Forecasting Basics): the consensus is the input to the alpha decomposition.
- **`cfa-equity-valuation` R20–R27**: industry-standard valuation models (DDM, FCFE, FCFF, residual income).
- **`cfa-asset-allocation-cme` Reading 25–28**: capital market expectations build the consensus from the top down.
