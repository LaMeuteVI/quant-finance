# Chapter 15: Long/Short Investing

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 15, pp. 419–444 (Part Four: Implementation)

## Core Idea

Long/short investing extends the active-management framework by **allowing short positions**. The short extension is non-trivial: short positions are not just negative active weights, they have a different **borrow cost**, a different **dividend treatment**, and they create a **net-long** vs **market-neutral** vs **dollar-neutral** decision. The chapter derives the long/short IR from the same `IC × √B` formula, with the modification that short-side signals and long-side signals have *different* costs and capacities.

The chapter's main practical insight: **the long/short IR is higher than the long-only IR for the same alpha, because the net exposure is controlled and the variance is dominated by alpha, not by market risk**. But the cost structure of the short side is the binding constraint.

## Frameworks Introduced

- **Long/Short = long side + short side as a pair of active portfolios**:
  - The long-side portfolio has its own forecast `α_L`, the short-side portfolio has its own forecast `α_S`, and the manager combines them into a long/short portfolio.
  - The combined IR is `IR_LS = √(IR_L² + IR_S² + 2 ρ_LS IR_L IR_S)`, where `ρ_LS` is the correlation between the long and short sides.

- **The "130/30" Extension**:
  - A 130/30 fund runs 130% long and 30% short; the net exposure is 100%, but the gross is 160%.
  - The IR is multiplied by `√(gross/net)` (approximately), so a 130/30 fund with the same alpha as a 100/0 fund has IR × √1.6 ≈ 1.26× the long-only IR.
  - *Why it matters*: 130/30 was the dominant institutional format in the 2000s because it gave a "free" 25% boost in IR from the leverage on the active side.

- **Borrow Cost and Short-Side Capacity**:
  - The short side has an additional cost: the **borrow fee** for hard-to-borrow names.
  - The cost reduces the net IR of the short side; in the limit of infinite borrow cost, the short side is un-tradeable.

- **Market Neutral vs Dollar Neutral vs Beta Neutral**:
  - *Market neutral*: the portfolio has zero beta to the market. Achieved by balancing long and short market exposure.
  - *Dollar neutral*: the long and short sides have equal dollar notional.
  - *Beta neutral*: the long and short sides have equal beta exposure. *Stronger* than market neutral.
  - The neutralisation choice defines the strategy's *true* market exposure and hence its risk profile.

## Key Concepts

1. **Long/short (LS) portfolio** — a portfolio with both long and short positions; the long and short sides can have separate alphas and constraints.
2. **Net exposure** — the difference between long and short notional; the directional bet of the portfolio.
3. **Gross exposure** — the sum of long and short notional; the *activity* of the portfolio.
4. **Dollar neutral** — long and short notional are equal in dollar terms.
5. **Beta neutral** — long and short betas are equal; the portfolio has zero market beta.
6. **130/30** — a portfolio with 130% long and 30% short, net 100% (or net 0% if balanced).
7. **Borrow cost** — the fee paid to borrow a stock to short it; the constraint on the short side.
8. **Hard-to-borrow** — a name with limited supply of lendable shares; borrow cost can be 5–50% annualised.
9. **Short rebate** — the interest earned on the proceeds of a short sale (collateralised at the cash rate).
10. **Net IR of a long/short** — the IR of the combined long/short portfolio, net of borrow cost and other frictions.

## Formulas & Reference Tables

**Long/Short IR (uncorrelated long and short sides)**

`IR_LS = √(IR_L² + IR_S²)`

With correlation ρ_LS:

`IR_LS = √(IR_L² + IR_S² + 2 ρ_LS IR_L IR_S)`

**Gross-to-net ratio and IR boost (approximate, for symmetric strategy)**

`IR_boost ≈ √(gross / net)` if the alpha scales linearly with gross.

A 130/30 fund has gross/net = 1.6, so `IR_boost = √1.6 ≈ 1.265`. The 25% boost is purely from leverage, not from better signal.

**Net IR after borrow cost**

`α_LS_net = (gross_L × α_L + gross_S × α_S) − borrow_cost × short_notional × days`

Divide by the gross TE to get the net IR.

**Borrow-cost-adjusted breakeven alpha for a short**

`α_S_min = borrow_cost × time_horizon`. The short-side alpha must at least cover the borrow cost.

## Mental Models

- **Short is not free.** Borrow cost is a real, often large, constraint on the short side.
- **Net exposure is the directional bet; gross exposure is the activity.** A 130/30 fund has gross = 1.6, net = 1.0 — the gross is what pays the alpha; the net is what determines the directional risk.
- **The long/short IR formula is exact for symmetric strategies; the asymmetry of costs and capacity makes the real-world number much smaller.**

## Worked Example (RECOMPUTED)

*Setup.* A 130/30 fund.
- Long side: 100 stocks, IC = 0.05, breadth = 100 → `IR_L = 0.05 × √100 = 0.5`
- Short side: 30 stocks, IC = 0.05, breadth = 30 → `IR_S = 0.05 × √30 = 0.274`
- Assume ρ_LS = 0 (long and short alphas uncorrelated).

*Step 1 — Combined IR*:
- `IR_LS = √(0.5² + 0.274²) = √(0.25 + 0.075) = √0.325 = 0.570`

*Step 2 — IR boost vs long-only*:
- Long-only IR = 0.5. LS IR = 0.57. The boost is 0.57/0.5 = 1.14 — a 14% boost from the short side, not the theoretical 26.5% from `√1.6` because the short side has lower breadth.

*Step 3 — Borrow cost adjustment*.
- If the average short-side borrow cost is 3% annualised and the short side is held for 1 year, the net short alpha is `0.274 × σ_θ − 0.03`.
- Assuming σ_θ = 5%, gross short alpha = 0.274 × 0.05 = 1.37% per year. Borrow cost = 3%. **Net short alpha is negative — the short side is value-destructive at 3% borrow cost.**

*Step 4 — Practical fix.* Use only *easy-to-borrow* names on the short side; require short-side IC ≥ 0.08 to break even at 3% borrow. This caps the short-side universe to ~5–10% of the long-side universe, materially reducing the breadth and the LS IR.

*Sanity check (Python).*
```python
import math
IC_L, B_L = 0.05, 100
IC_S, B_S = 0.05, 30
rho = 0
IR_L = IC_L * math.sqrt(B_L)
IR_S = IC_S * math.sqrt(B_S)
IR_LS = math.sqrt(IR_L**2 + IR_S**2 + 2*rho*IR_L*IR_S)
print("IR long-only:", round(IR_L, 3))   # 0.5
print("IR LS       :", round(IR_LS, 3))   # 0.570
boost = IR_LS / IR_L
print("IR boost    :", round(boost, 3))   # 1.14
gross_to_net = 1.6
print("Theoretical boost:", round(math.sqrt(gross_to_net), 3))  # 1.265
```

## Anti-patterns

- **Assuming the gross-to-net IR boost applies uniformly.** Real-world constraints (borrow, capacity, market impact) make the boost smaller.
- **Ignoring borrow cost on the short side.** A 3% borrow cost is the difference between a profitable and a value-destructive short.
- **Forgetting dividend treatment on shorts.** A short pays the dividend *to the lender*, not the reverse. This is a real cost on dividend-paying names.
- **Running 150/50 or higher without a corresponding increase in signal strength.** The leverage amplifies the alpha but also the estimation error.

## Practitioner Notes

- **2026 update.** 130/30 has fallen out of favour; many institutional long/short funds now run 100/0 or 120/20 — the short-side cost structure and the regulatory burden (in the EU, UCITS funds cannot short at all) have made the strategy less attractive. Market-neutral hedge funds (L/S equity, equity-market-neutral) are a separate universe with different capacity and risk characteristics.
- **Prime brokerage** is the modern mechanism for shorting; the borrow cost is set by the prime broker and reflects the lendable supply. The Hard-to-Borrow list changes daily; the agent should treat borrow cost as a *real-time* constraint.
- **Regulatory constraints.** UCITS (European retail funds) cannot short at all. AIFMD allows shorting but with constraints. For US-based managers, Reg T and locate requirements make shorting capital-intensive. The agent must encode the *jurisdiction* of the strategy before evaluating any short-side alpha.

## Key Takeaways

1. **Long/Short ≠ Long-Only with negatives.** Borrow cost, dividend treatment, and capacity make the short side a fundamentally different game.
2. The **IR boost** from gross-to-net is real but smaller in practice; the agent should not assume the textbook `√(gross/net)` value.
3. **The short-side IR must cover borrow cost.** Without this filter, the short side is value-destructive.
4. **Capacity is asymmetric.** Most institutional equity universes have a long side of ~1000–3000 names and a short side of 50–300 (after the borrow-cost filter).
5. The 130/30 format is now rare; long-only or modest long/short (100/0, 120/20) is the modern default.

## Connects To

- **ch14**: the construction problem is the same; the long/short is the multi-asset case.
- **ch16**: short-side trading cost is the dominant friction; transactions cost on the short side is much higher than on the long side.
- **ch18**: asset allocation across long and short sides.
- **`cfa-derivatives` R33–R34 (Equity Portfolio Management)**: practical implementation of long/short in institutional settings.
- **`cfasi-equity-investment-styles`**: equity style strategies (Value, Growth, Quality) typically run long-only; long/short is more often a factor-neutral extension.
