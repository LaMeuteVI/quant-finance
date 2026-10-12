# Chapter 2: Financial Data Structures

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 2, pp. 23–42

## Core Idea

The raw data for a financial ML system is a sequence of **events** — ticks, trades, quotes — not the regular time series of bars that the textbooks show. The chapter introduces the **three financial data structures**: (1) the tick, (2) the bar, and (3) the *information-driven* bar (dollar, volume, tick, imbalance). The information-driven bar is the right unit for ML on financial data because the sampling is driven by the *information arrival process*, not by the calendar. The chapter's signature contribution is the **imbalance bar** (a.k.a. *tick imbalance bar*): a bar is created whenever the cumulative signed-volume imbalance exceeds a threshold — a proxy for the information arrival rate.

## Frameworks Introduced

- **The Tick (raw data)**:
  - Each trade is a `(time, price, volume, side)` tuple; each quote is a `(time, bid, ask, bid_size, ask_size)` tuple. The "side" of a trade (buy or sell) is inferred from the quote rule: a trade at the ask is a buy, at the bid is a sell.

- **The Bar (regular sampling)**:
  - A *time bar*: a fixed interval of time (1 minute, 1 hour, 1 day). Simple but **not stationary** — the number of events per bar varies with the activity.
  - A *tick bar*: a fixed number of ticks (e.g. 1000 ticks per bar). More stationary than time bars but ignores the volume of the ticks.
  - A *volume bar*: a fixed volume per bar. Better than time bars but ignores the price change.
  - A *dollar bar*: a fixed dollar volume per bar. The most "balanced" of the standard bars.

- **The Information-Driven Bar (the right unit for ML)**:
  - The bar is created when an *information arrival* event is detected. The information arrival is proxied by the imbalance of signed volume.
  - **Tick Imbalance Bar (TIB)**: a bar is created when the cumulative imbalance `Θ_t = Σ e_{t,i}` exceeds a threshold. The threshold is set adaptively from the expected imbalance.
  - **Volume Imbalance Bar (VIB)**: same idea, but the imbalance is in dollar terms, not tick count.
  - **Tick Run Bar (TRB)**: a bar is created when the run length (consecutive same-side ticks) exceeds a threshold.

- **Why the information-driven bar is the right unit**:
  - Standard bars are not a stationary sampling of the information process; the number of events per bar varies with the activity. The information-driven bar is, by construction, a stationary sampling of the *information arrival* process.
  - *When to use*: every time you train a model on bar data. The information-driven bar makes the features (e.g. realised volatility, order flow imbalance) more stationary, which improves the model's OOS performance.

## Key Concepts

1. **Tick** — a single event in the market; a trade or a quote.
2. **Bar** — a sampling of the tick stream; time, tick, volume, or dollar.
3. **Information-driven bar** — a bar whose sampling is driven by an information-arrival proxy.
4. **Tick Imbalance Bar (TIB)** — the canonical information-driven bar; created when the cumulative signed-volume imbalance exceeds a threshold.
5. **Signed volume `e_i`** — the volume of trade `i` with its sign (positive for buy, negative for sell).
6. **Cumulative imbalance `Θ_t = Σ e_{t,i}`** — the running sum of signed volumes.
7. **Bar sign rule** — `b_t = +1` if `Θ_t > 0`, `b_t = −1` if `Θ_t < 0` (or vice versa; convention).
8. **Realised volatility** — the square root of the sum of squared log-returns over the bar; a feature that benefits from the information-driven bar.
9. **Tick rule** — a heuristic for inferring the sign of a trade: a trade at the ask is a buy, a trade at the bid is a sell, etc.
10. **Multiple-class tick rule** — a more accurate version that considers the relationship between successive trades.

## Formulas & Reference Tables

**Tick Imbalance Bar (TIB) threshold**

`E[Θ] = E[|e|] × P(b = +1) − E[|e|] × P(b = −1) = 0` (under the null of no information).

The bar is created when `|Θ_t| > E[|Θ|] × θ_0`, where `θ_0` is a hyperparameter (typically 1–2).

**The bar sign rule**

`b_t = +1` if `Θ_t > 0`, else `b_t = −1`.

**Realised variance over a bar**

`RV_t = Σ_{i=1}^{N_t} r_{t,i}²`, where `N_t` is the number of ticks in bar `t` and `r_{t,i}` is the i-th log-return.

**The order flow imbalance**

`OFI_t = Σ_{i=1}^{N_t} sign(e_{t,i})`, the number of buy-initiated trades minus the number of sell-initiated trades in bar `t`.

## Mental Models

- **The right unit of analysis is the *information event*, not the *time interval*.** A time bar at 1:00 PM may have 100 ticks (low activity) or 10,000 ticks (high activity); the information content is wildly different. The information-driven bar captures the *information content* per bar.
- **Standard bars are not stationary.** The information-driven bar is.
- **The tick rule is a heuristic.** A more accurate version uses the *quote* (a trade at the ask is more likely a buy than a trade at the bid).

## Worked Example (RECOMPUTED)

*Setup.* 1000 ticks of trade data. The average trade size is 100 shares. Under the null, the probability of a buy is 0.5.

*Step 1 — Expected imbalance under the null*.
- `E[Θ] = 0` (by symmetry).

*Step 2 — Expected absolute imbalance under the null*.
- For 1000 ticks of independent buy/sell with P(buy) = 0.5, `Θ ~ Binomial(1000, 0.5) − 500`. The expected absolute value is approximately `√(1000 × 0.25) × √(2/π) ≈ 12.6` (using the normal approximation).

*Step 3 — Set the TIB threshold*.
- `|Θ_t| > θ_0 × 12.6`, with `θ_0 = 2` → threshold = 25.2. So a TIB is created when the cumulative imbalance exceeds 25.

*Step 4 — Under genuine information arrival*.
- If the information is positive (e.g. an earnings beat), the buy probability rises to 0.7. Then `E[Θ] = 100` (after 1000 ticks), and the TIB is created earlier — at the first ~70 ticks (when |Θ| > 25.2 for the first time).

*Sanity check (Python).*
```python
import numpy as np
# Under null (P(buy) = 0.5)
np.random.seed(42)
signs = np.random.choice([1, -1], 1000)
abs_imbalance_null = np.abs(np.cumsum(signs))
print(f"Mean |Θ| under null: {abs_imbalance_null.mean():.2f}")
# Under positive info (P(buy) = 0.7)
signs = np.where(np.random.rand(1000) < 0.7, 1, -1)
cum_imbalance = np.cumsum(signs)
first_bar = np.argmax(np.abs(cum_imbalance) > 25.2) + 1
print(f"First TIB at tick: {first_bar}")
```

## Anti-patterns

- **Using time bars as the unit of analysis.** The number of ticks per bar varies by orders of magnitude; the resulting features are non-stationary.
- **Using a tick rule that ignores the quote.** The Lee-Ready (1991) algorithm uses both the trade and the prevailing quote.
- **Treating the threshold `θ_0` as a free parameter.** It should be calibrated to the realised absolute imbalance; `θ_0 = 1–2` is typical.
- **Computing realised volatility on time bars.** The information-driven bar gives a more stationary realised vol.

## Practitioner Notes

- **2026 update.** The information-driven bar is now standard in industry. The Python library `mlfinlab` (by Hudson & Thames) implements the TIB, VIB, and TRB; the `finml` library is the open-source alternative.
- **Crypto markets** are particularly well-suited to the information-driven bar; the tick rate is high and the bar size is more informative.
- **The "buy/sell" classification** is critical for the imbalance bars; the standard is the Lee-Ready (1991) algorithm. For modern HFT data, the Bulk Volume Classification (BVC) of Easley, López de Prado & O'Hara (2012) is the state-of-the-art.

## Key Takeaways

1. **The raw data is a tick stream, not a bar stream.** The bar is a *sampling* of the tick stream.
2. **Standard bars (time, tick, volume, dollar) are not stationary** in their information content.
3. **Information-driven bars** (TIB, VIB, TRB) are the right unit for ML on financial data.
4. **The TIB threshold** is calibrated to the expected absolute imbalance under the null.
5. **The Lee-Ready (1991) algorithm** is the standard for buy/sell classification; BVC (2012) is the modern HFT version.

## Connects To

- **ch03** (Labeling): the bars are the input to the labeling.
- **ch05** (Fractionally Differentiated Features): the FFD features are computed on the bar data.
- **ch07** (Cross-Validation in Finance): the CV purging uses the bar timestamps.
- **`hull-risk-management` ch10 (Volatility)**: the realised volatility is computed on the bars.
- **`tsay-analysis-financial-time-series` ch02 (Linear Time Series Analysis)**: the ARMA models are estimated on bar returns.
