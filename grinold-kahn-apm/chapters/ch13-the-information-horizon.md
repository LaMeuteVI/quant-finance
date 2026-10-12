# Chapter 13: The Information Horizon

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 13, pp. 347–376 (Part Three: Information Processing)

## Core Idea

The information horizon is the **time between forecast and outcome** — how long the manager must wait for the alpha to be realised. The horizon interacts with the information ratio through the **square-root-of-time rule** for the standard deviation of returns and the *linear* scaling of expected return with horizon. The horizon is the lever that connects forecasting (ch10–12) to portfolio construction (ch14) and to the trading/turnover choice (ch16).

The chapter's key insight: the information ratio is a **per-period** statistic, not a per-year statistic. The horizon is the period.

## Frameworks Introduced

- **The Horizon Decomposition**:
  - *Expected return* scales **linearly** with horizon: `E[r_T] = T × E[r_1]`.
  - *Standard deviation* scales with **√T**: `σ_T = √T × σ_1`.
  - Therefore the *Sharpe ratio per year* scales as `√T / T = 1/√T`... no wait — the IR per period stays the same; the IR per *year* scales as `√T` if the per-period IC and breadth stay the same.
  - The horizon is the multiplier on the per-period information ratio.

- **The Information Horizon and the Right Time to Trade**:
  - *When to use*: every time you choose the holding period of a strategy. The horizon defines the rate at which alpha is realised; the *breakeven horizon* is when the trading cost equals the gross alpha.
  - *Why it works*: the gross alpha is linear in horizon; the trading cost is roughly independent of horizon (a round-trip cost). The two lines cross at the breakeven horizon.

- **The IC-by-Horizon Profile**: every signal has an IC at every horizon. Short horizons (intraday) have low IC; long horizons (quarterly) have higher IC. The maximum is at the "natural" horizon of the signal (the time scale of the underlying economic mechanism).
  - *When to use*: as a diagnostic — if a fundamental signal has higher IC at monthly than at annual horizons, you are probably overfitting to the annual data.

- **The Breakeven Horizon (cost vs. alpha trade-off)**:
  - `T_breakeven = (round-trip cost) / (alpha per period)`. The minimum holding period at which the gross alpha exceeds the cost.
  - *When to use*: to decide whether a strategy is worth the trading cost. A strategy with T_breakeven = 250 days is essentially un-tradeable in a daily framework.

## Key Concepts

1. **Information horizon** — the time between forecast and outcome; the "speed" of the signal.
2. **Square-root-of-time rule** — the volatility scales as √T over T periods; the IR per period is constant.
3. **Breakeven horizon** — the minimum holding period at which the alpha covers the cost of trading.
4. **Per-period IR** — the IR of a strategy computed over a single forecast horizon; the natural unit.
5. **Annualised IR** — the per-period IR scaled by √(periods per year); the convention for reporting.
6. **Natural horizon** — the time scale of the underlying economic mechanism of the signal.
7. **Holding-period IR** — the IR of a strategy when restricted to a fixed holding period; a more honest measure of "what you actually make".
8. **Time decay of the signal** — the rate at which the IC declines as the horizon extends; signals with slow decay are preferred.

## Formulas & Reference Tables

**Horizon scaling of expected return and standard deviation**

`E[r_T] = T × E[r_1]`,  `σ_T = √T × σ_1`.

Therefore `IR_T (per period) = IR_1` (constant), and `IR_annualised = IR_perPeriod × √(periods per year)`.

**Breakeven horizon**

`T_breakeven = (round-trip cost) / (alpha per period)`. With cost C (decimal) and gross alpha per period α_1:

`T_breakeven = C / α_1`.

**Net IR after transaction costs (over horizon T)**

`IR_net(T) = (T × α_1 − C) / (√T × σ_1)`.

Setting `IR_net = 0` recovers the breakeven horizon.

**IR breakeven for a strategy with target IR\***

`T_breakeven = C² / (IR*² × σ_1²)`. The holding period needed to make a target IR after costs.

**Annualised IR as a function of horizon**

`IR_annualised(T) = IR_perPeriod × √(252/T)` for daily data, and analogous for monthly.

## Mental Models

- **The horizon is a budget constraint.** Short horizons give you more bets per year (high B) but lower per-bet IC; long horizons give you fewer bets but higher per-bet IC.
- **The breakeven horizon is the floor.** Any strategy whose natural horizon is below its breakeven horizon is value-destructive.
- **The per-period IR is the honest unit.** Annualised IR can be inflated by reporting a short horizon over more periods than the strategy actually allows.

## Worked Example (RECOMPUTED)

*Setup.* A momentum strategy with monthly IC = 0.04, monthly breadth B = 100 (100 independent bets per month, recomputed each month). Round-trip trading cost = 0.5% (50 bps).

*Step 1 — Per-month IR*: `IR_monthly = 0.04 × √100 = 0.4`.

*Step 2 — Per-month gross alpha (assuming σ_θ = 5% per month for the active portfolio)*: `α_gross = IR × σ_θ = 0.4 × 5% = 2%` per month.

*Step 3 — Net alpha after cost*:
- `α_net = 2% − 0.5% = 1.5%` per month.

*Step 4 — Breakeven horizon*: `T_breakeven = C / α_1 = 0.5% / 2% = 0.25` months ≈ 1 week. So the strategy is profitable even on a weekly horizon.

*Step 5 — Net annualised IR*:
- `IR_annual = 0.4 × √12 = 1.39`.
- `α_annual_net = 12 × 1.5% = 18%`.
- `σ_annual = 5% × √12 = 17.3%`.
- `IR_annual_net = 18% / 17.3% = 1.04`.

*Step 6 — Diagnostic.* Per-month IR = 0.4 vs. annualised net IR = 1.04. The annualised number is more representative of what the investor actually captures.

*Sanity check (Python).*
```python
import math
IC, B = 0.04, 100
sigma_theta_m = 0.05
cost = 0.005   # 0.5% round-trip
IR_m = IC * math.sqrt(B)
alpha_m_gross = IR_m * sigma_theta_m
alpha_m_net = alpha_m_gross - cost
T_breakeven = cost / alpha_m_gross
IR_annual = IR_m * math.sqrt(12)
alpha_annual_net = 12 * alpha_m_net
sigma_annual = sigma_theta_m * math.sqrt(12)
IR_annual_net = alpha_annual_net / sigma_annual
print("IR monthly       :", round(IR_m, 3))        # 0.4
print("alpha monthly net:", f"{alpha_m_net:.3%}")  # 1.5%
print("T_breakeven (mo) :", round(T_breakeven, 3)) # 0.25
print("IR annualised net:", round(IR_annual_net, 3)) # 1.04
```

## Anti-patterns

- **Annualising a short-horizon IR without checking that the strategy can actually be held for that long.**
- **Confusing per-period IR with annualised IR.** They differ by √(periods/year); the *honest* reporting is both.
- **Trusting an IC measured at one horizon for a strategy traded at another.** The IC is horizon-specific.
- **Ignoring the breakeven horizon.** A strategy with T_breakeven > its natural horizon is value-destructive.

## Practitioner Notes

- **2026 update.** The horizon trade-off is now studied as the **Sharpe ratio by holding period** in López de Prado ch10 (bet sizing) and ch15 (strategy risk). The book is the same algebra; the modern addition is the *embargo* on overlapping positions.
- **High-frequency strategies** push horizon to seconds and minutes; the breakeven horizon collapses to seconds, and the cost must be measured in basis points per trade, not per share.
- **Capacity constraints.** The horizon interacts with capacity: short horizons force higher turnover, which scales trading cost and market impact. The book treats cost as fixed; modern practice uses **Almgren–Chriss** (2001) to model the cost-capacity trade-off.

## Key Takeaways

1. The information horizon is the **fundamental time scale of the strategy**; everything else is a multiplier on it.
2. The **breakeven horizon** is the floor: strategies with T_natural < T_breakeven are un-tradeable.
3. The IR is *per period* by construction; annualising requires the right number of periods.
4. Cost and alpha are in different units (cost is round-trip, alpha is per period); the ratio is the breakeven horizon.
5. The horizon is the *most under-estimated* parameter in real-world quant strategies; getting it wrong is the most common reason for a strategy under-performing its backtest.

## Connects To

- **ch10–11**: the horizon is the period over which the IC is estimated.
- **ch14**: the active portfolio is constructed at the strategy's horizon; mismatches between construction and trading horizons are a common source of backtest error.
- **ch16**: the transaction-cost chapter generalises the breakeven horizon to optimal turnover and execution.
- **`lopez-de-prado-afml` ch10 (Bet Sizing), ch15 (Understanding Strategy Risk)**: the modern version of horizon analysis.
- **`chan-machine-trading` ch03 (Time-Series Analysis) and ch04 (AI Techniques)**: the practical horizon choice for short-horizon systematic strategies.
