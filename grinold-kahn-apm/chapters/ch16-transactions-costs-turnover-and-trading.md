# Chapter 16: Transactions Costs, Turnover, and Trading

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 16, pp. 445–476 (Part Four: Implementation)

## Core Idea

A strategy's gross alpha is the *opportunity*; **transactions costs determine what the investor actually keeps**. The chapter gives a complete framework: cost models (fixed, linear, square-root market impact), the *optimal turnover* formula (which scales with the inverse square root of the cost), and the **residual alpha** that survives after costs. The most important formula is the **square-root law of market impact**: cost scales as `σ × √(Q/ADV)` where `Q` is the order size and `ADV` is the average daily volume. The chapter turns this into a closed-form for optimal execution.

This is the chapter that determines whether a backtest survives live trading.

## Frameworks Introduced

- **The Components of Transaction Cost**:
  - *Fixed cost*: commissions and fees, often per share or per dollar traded.
  - *Bid–ask spread*: the half-spread on the trade; the most visible cost.
  - *Market impact*: the price move caused by the order itself; scales with size and inversely with ADV.
  - *Delay cost*: the price move between decision and execution.
  - *Opportunity cost*: the cost of failing to trade when there is an alpha signal.

- **The Square-Root Law of Market Impact (the workhorse model)**:
  `Impact(Q) = σ × √(Q / ADV) × Y`, where `Y` is a constant (typically 0.1–1.0 basis points, depending on the asset class and time horizon).
  - *When to use*: as the default model for market impact. Empirically validated across many asset classes and time scales.
  - *Why it works*: the law is dimensionally consistent (σ × √(fraction of ADV) is dimensionally a return) and is consistent with the *Kyle (1985)* model of informed trading.
  - *Failure mode*: ignoring the *time horizon* of execution — the impact is `σ × √(Q/ADV/T)` over T days; a longer execution window reduces the impact per day but increases the delay cost.

- **The Optimal Position Size (the **½ power law**)**:
  - In a single-asset optimisation, the optimal `h` scales as `1 / √(cost)`. Doubling the cost reduces the optimal size by a factor of `√2`.
  - *Why it matters*: small changes in cost have non-linear effects on the construction. A strategy that is profitable at 5 bps cost can be unprofitable at 20 bps.
  - *Failure mode*: applying the formula with the wrong cost — using the *fixed* cost without including the *variable* market impact.

- **The Breakeven Turnover (the maximum turnover the strategy can sustain)**:
  - `T_max = (gross alpha per year) / (round-trip cost)`. The maximum turnover that still leaves positive net alpha.
  - *When to use*: as a quick back-of-the-envelope check on whether a strategy is tradeable.
  - *Failure mode*: ignoring the *capacity* constraint (a strategy can have positive breakeven turnover but not enough ADV to execute at the size needed for the alpha to be material).

- **The Almgren–Chriss Optimal Execution (previewed in the chapter)**:
  - The optimal execution schedule over T days balances market impact (favours slow execution) against delay cost (favours fast execution).
  - The optimal trajectory is `x*(t) = X × sinh(κ (T − t)) / sinh(κ T)` for the remaining position `x*(t)`, where `κ` is the urgency parameter.
  - The expected cost is `E[Cost] = η × X² × (1/2) × κ / tanh(κ T) + (σ² T / 2) × X² − σ × X × √(κ / (2 sinh(2 κ T)))` in the original formulation.
  - *When to use*: when execution matters enough to justify the math.

## Key Concepts

1. **Transaction cost** — the total cost of trading, including spread, market impact, commission, and delay.
2. **Square-root law of impact** — `σ × √(Q/ADV)`; the canonical impact model.
3. **Half-power law of optimal size** — optimal `h ∝ 1/√cost`.
4. **Breakeven turnover** — the maximum turnover that leaves net alpha ≥ 0.
5. **Capacity constraint** — the maximum AUM at which the strategy can still execute at the assumed cost.
6. **Delay cost** — the price move between decision and execution; the cost of *not* being fast enough.
7. **Opportunity cost** — the cost of *not* trading when there is a signal; the symmetric of the impact cost.
8. **Almgren–Chriss trajectory** — the optimal execution path that balances impact and delay.
9. **VWAP / TWAP execution** — volume-weighted average price / time-weighted average price; the benchmark for execution quality.
10. **Implementation shortfall** — the difference between the decision price and the actual execution price; the empirical cost.

## Formulas & Reference Tables

**Square-root market impact**

`Impact(Q) = σ × √(Q / ADV) × Y`

Empirically, `Y` is on the order of 1.0 for equities (Brokmann–Handa–Yadav) — i.e. a 1% of ADV order has impact ≈ σ × 0.1. For futures, `Y` is much smaller (≈ 0.1).

**Total cost per dollar traded (linear cost + impact)**

`Cost(Q) = c_fixed + σ × √(Q/ADV) × Y + spread/2`

**Optimal position size (the ½ power law)**

`h_opt = √(2 α / (λ × ∂²Cost/∂h²))`. For a quadratic cost `c h²`, this is `h_opt = √(α / (λ c))`, scaling as `1/√c` in the cost parameter.

**Breakeven turnover**

`T_max = (annual gross alpha) / (round-trip cost)`.

**Almgren–Chriss optimal trajectory**

`x*(t) = X × sinh(κ (T − t)) / sinh(κ T)`, with `κ = √(λ σ² / η)` and `η` the temporary-impact coefficient.

**Implementation shortfall (Perold 1988)**

`IS = (decision_price − actual_execution_price) × shares`, normalised as basis points of the decision-price notional.

## Mental Models

- **Transaction cost is not a number; it is a function of size.** A 1% of ADV order has a 10× larger impact per dollar than a 0.01% order.
- **Turnover and horizon are linked.** A strategy with horizon 1 day has turnover ≈ 100% (it must re-balance daily); its breakeven alpha must be correspondingly high.
- **Capacity is the binding constraint.** Many strategies are profitable in the backtest at $1M AUM and unprofitable at $1B AUM. The agent must always report the strategy's *capacity*, not just its *alpha*.

## Worked Example (RECOMPUTED)

*Setup.* A momentum strategy with monthly IR = 0.5, monthly α_gross = 2.5% (5% monthly σ_θ), monthly cost = 0.5% (50 bps round-trip). The strategy turns over 50% of the portfolio per month.

*Step 1 — Net monthly alpha*.
- Gross alpha: 2.5%.
- Cost: 0.5% × 50% (only the traded portion incurs cost) = 0.25%? No — for a 50% turnover strategy, the average holding period is 2 months, and the cost per round-trip is 0.5%, so the cost per month is 0.5%/2 = 0.25%.
- Net alpha: 2.5% − 0.25% = 2.25%.

*Step 2 — Annualised net alpha and IR*.
- Net annual alpha = 12 × 2.25% = 27% (if no compounding effect on alpha — in reality, the *return* compounds but the *cost* is per-trade).
- Annual σ_θ = 5% × √12 = 17.3%.
- Net annual IR = 27% / 17.3% = 1.56.
- Gross annual IR = (12 × 2.5%) / 17.3% = 30% / 17.3% = 1.73.
- The cost reduces the IR by ~10%.

*Step 3 — Capacity check*.
- Suppose the strategy trades 1000 stocks, with average $1M traded per day.
- Daily impact per stock: 0.5% × √(1M / 50M) × 1 (assuming σ = 30%, ADV = $50M) = 0.5% × 0.141 = 0.07% per stock per day.
- The strategy AUM at which impact reaches 50 bps per day is `Q/ADV = (50/30)² = 2.78`, i.e. 2.78× the original Q. So the AUM capacity is 2.78× the initial $1M/day = ~$2.8M/day × 250 days = $700M AUM.
- This is the **capacity of the strategy**. Above this, the cost grows and the net alpha collapses.

*Step 4 — Square-root scaling**.
- If we double the AUM to $1.4B (each day's trading goes from $1M to $2M), the impact per stock grows from 7 bps to `7 × √2 = 9.9` bps. The cost per month grows from 25 bps to 35 bps. The net alpha drops to `2.5% − 0.35% = 2.15%` per month, an IR of `2.15% × 12 / 17.3% = 1.49` — a 4.5% drop from doubling AUM.

*Sanity check (Python).*
```python
import math
alpha_gross_m = 0.025
sigma_theta_m = 0.05
cost_rt = 0.005
turnover_m = 0.5
cost_m = cost_rt * turnover_m     # 0.0025 (25 bps)
alpha_net_m = alpha_gross_m - cost_m
IR_m = alpha_gross_m / sigma_theta_m
IR_m_net = alpha_net_m / sigma_theta_m
print(f"IR monthly gross: {IR_m:.3f}, net: {IR_m_net:.3f}")
print(f"Cost ratio      : {cost_m/alpha_gross_m:.1%}")   # 10% of gross

# Capacity scaling
Q0 = 1.0   # initial trading $M/day per stock
ADV = 50.0
sigma_d = 0.30 / math.sqrt(252)
impact_per_d = cost_rt * math.sqrt(Q0/ADV) * 1.0
print(f"Impact @ 1M: {impact_per_d*1e4:.1f} bps")
Q_cap = (cost_rt / impact_per_d)**2 * Q0
print(f"AUM capacity (single-stock): ~${Q_cap:.1f}M/day")
```

## Anti-patterns

- **Reporting gross alpha without subtracting cost.** A backtest that ignores cost is fiction.
- **Using a flat 5 bps cost for all names.** Cost varies by 100× across the universe; treating it as constant hides the real-world problem.
- **Ignoring capacity.** A backtest at $1M AUM that is un-tradeable at the strategy's actual AUM is not a strategy.
- **Using turnover without thinking about it.** A 200% per month turnover strategy with 5 bps cost is a 1% per month drag, often enough to wipe out the alpha.

## Practitioner Notes

- **2026 update.** The square-root law is still the default, but modern execution algorithms (VWAP, TWAP, Implementation Shortfall, Liquidity-seeking, dark-pool aggregators) are more sophisticated than the Almgren–Chriss trajectory. The agent should treat *execution algorithm choice* as a separate decision from *alpha*; the cost model is no longer a single number but a *function* of the algo.
- **Transaction Cost Analysis (TCA)** has become a sub-industry. The institutional standard is to measure implementation shortfall ex post, attribute it to delay/impact/spread, and use the result to refine the cost model.
- **Capacity** in modern practice is the binding constraint. Most institutional quant strategies have to choose between capacity and alpha — the high-IR strategies are capacity-constrained, the high-capacity strategies have lower IR.
- **Borrow cost for shorts** (ch15) and **financing cost for futures/derivatives** are real and should be included in the cost model.

## Key Takeaways

1. **Transaction cost is a function of size**, not a number. The square-root law is the canonical model.
2. **Optimal position size scales as `1/√cost`.** Doubling the cost reduces the optimal `h` by 30%.
3. **Breakeven turnover** is the floor: any strategy with actual turnover above it is value-destructive.
4. **Capacity is the binding constraint.** A strategy that is profitable at $1M AUM and unprofitable at $1B AUM has a *capacity*, not just an alpha.
5. **Net IR = gross IR × (1 − cost_ratio).** The cost ratio (cost / gross alpha) is the single number that determines the strategy's viability.

## Connects To

- **ch13**: the breakeven horizon and breakeven turnover are the same trade-off in different units.
- **ch14**: the cost enters the construction via `V` and `λ`; under-estimating cost leads to over-trading.
- **ch15**: short-side transaction cost is the dominant friction in long/short strategies.
- **`lopez-de-prado-afml` ch15 (Understanding Strategy Risk)**: the cost-adjusted strategy risk.
- **`cfa-derivatives` R8 (Option Markets)**: the bid–ask spread and the cost of option replication.
- **`tuckman-fixed-income` ch7–8 (Mortgage-Backed and Other Asset-Backed Securities)**: the cost of trading structured products is *much* higher than equities; the agent must model it separately.
