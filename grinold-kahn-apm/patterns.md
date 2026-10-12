# Patterns — Active Portfolio Management (Grinold & Kahn)

> The "how to" recipes derived from the book. Each pattern: When to use, How, Trade-offs, Reference.

## 1. The Rule of Thumb `α = s × IC × σ(θ)` (ch10)

- **When to use**: every time a manager turns a raw signal into a forecast.
- **How**: rank securities on the signal, standardise ranks to `~N(0,1)`, multiply by the IC estimate, multiply by residual volatility to get a dollar alpha.
- **Trade-offs**: linear and tamed; cannot capture non-linear signal-to-return mappings. Use the rule as the *baseline*; reach for non-linearity only when the relationship is known to be non-linear.
- **Reference**: ch10.

## 2. The Fundamental Law `IR = IC × √B × TC` (ch06)

- **When to use**: every time you evaluate a strategy's *capacity* to produce alpha.
- **How**: estimate IC (skill), B (breadth), TC (transfer coefficient). The IR is the product.
- **Trade-offs**: IC is hard to estimate out-of-sample; B can be inflated by correlated signals; TC is bounded by 1.
- **Reference**: ch06.

## 3. The Breakeven IC (ch10)

- **When to use**: when pricing a research project.
- **How**: `BEIR = √(annual_cost / B)`. The manager should not invest in a signal whose expected IC is below the BEIR.
- **Trade-offs**: most signals have IC < 0.10; many research projects have BEIR > 0.10 and are value-destructive.
- **Reference**: ch10.

## 4. The Breakeven Horizon (ch13, ch16)

- **When to use**: when deciding whether a strategy is tradeable.
- **How**: `T_breakeven = C / α_1`. The strategy's natural horizon must exceed the breakeven.
- **Trade-offs**: short-horizon strategies are constrained by execution cost; long-horizon strategies are constrained by signal decay.
- **Reference**: ch13, ch16.

## 5. The Unconstrained Optimal `h* = (1/λ) V^(-1) α` (ch14)

- **When to use**: as the *starting point* for any portfolio construction.
- **How**: compute the inverse of the residual covariance matrix, multiply by the alpha vector, scale by `1/λ`.
- **Trade-offs**: the *unconstrained* optimum is rarely implementable; the constrained optimum is the unconstrained optimum projected onto the feasible set.
- **Reference**: ch14.

## 6. The Certainty-Equivalent `h*_CE = (1/λ) (V + P)^(-1) α` (ch14)

- **When to use**: when the manager's alpha has non-trivial estimation error.
- **How**: estimate the forecast uncertainty covariance `P`, add it to the residual covariance `V`, then solve.
- **Trade-offs**: under-estimating `P` is the most common error; the resulting `h` is over-confident.
- **Reference**: ch14.

## 7. The Black–Litterman Expected Return (ch14)

- **When to use**: when the manager's α is uncertain and the benchmark is informative.
- **How**: `E[R_BL] = [(τΣ)^(-1) + P^(-1)]^(-1) [(τΣ)^(-1) Π + P^(-1) Q]`. Combine the equilibrium return `Π` with the manager's view `Q`.
- **Trade-offs**: the prior strength `τ` is set by the manager; the literature suggests `τ = 0.05` as a default, but the optimal value is asset-class-specific.
- **Reference**: ch14.

## 8. The Brown–Kleiman `R²_OOS ≈ R²_IS − K/N` (ch10, ch11)

- **When to use**: every time you interpret an in-sample R².
- **How**: subtract `K/N` from the in-sample R² to estimate the out-of-sample R².
- **Trade-offs**: the correction is approximate; for non-normal returns, the actual OOS R² may be lower.
- **Reference**: ch10, ch11.

## 9. The BBF Decomposition (ch17)

- **When to use**: every performance report.
- **How**: split the active return into asset allocation, security selection, and interaction.
- **Trade-offs**: the decomposition is not unique (Brinson–Hood–Beebower 1986 vs Brinson–Beebower 1991 differ); pick one and stick to it.
- **Reference**: ch17.

## 10. The Brinson–Beebower–Fachler with Carino Smoothing (ch17)

- **When to use**: when the BBF decomposition does not sum to the total active return.
- **How**: scale the raw decomposition by a single factor to match the total.
- **Trade-offs**: the Carino smoothing is the institutional default; the unsmoothed decomposition is a "ballpark".
- **Reference**: ch17.

## 11. The Capacity Limit (ch16)

- **When to use**: when scaling a strategy.
- **How**: estimate the AUM at which the trading cost reaches the strategy's breakeven cost.
- **Trade-offs**: the capacity is hard to estimate in advance; the agent should monitor the realised cost as AUM grows.
- **Reference**: ch16.

## 12. The Long/Short IR Boost (ch15)

- **When to use**: when designing a long/short strategy.
- **How**: `IR_LS ≈ IR_LS,net × √(gross/net)`, with the gross-to-net multiplier representing the leverage on the active side.
- **Trade-offs**: the boost is smaller in practice because of borrow cost, dividend treatment, and short-side capacity.
- **Reference**: ch15.

## 13. The Square-Root Law of Market Impact (ch16)

- **When to use**: every time you size an order.
- **How**: `Impact(Q) = σ × √(Q/ADV) × Y`. Order size `Q` should be small relative to `ADV`.
- **Trade-offs**: the impact is `Y`-dependent; the empirical value of `Y` is asset-class-specific.
- **Reference**: ch16.

## 14. The Optimum Trading Size `h ∝ 1/√cost` (ch16)

- **When to use**: when calibrating the construction to the trading cost.
- **How**: scale the active weights inversely with the square root of the trading cost.
- **Trade-offs**: small changes in cost have non-linear effects on the construction.
- **Reference**: ch16.

## 15. The Skill / Luck Ratio `IR² / (1 + IR²)` (ch17)

- **When to use**: when interpreting a high-IR year.
- **How**: for an IR of 0.5, only 20% of the alpha is skill; for an IR of 1.0, 50%; for an IR of 2.0, 80%.
- **Trade-offs**: the decomposition is a *theoretical* estimate; the actual skill/luck split depends on the persistence of the manager's alpha.
- **Reference**: ch17.

## 16. The Mean-Reverting Next-Year IR (ch17)

- **When to use**: when forecasting next-year performance.
- **How**: `IR_next ≈ IR_this × ρ̂`, where `ρ̂` is the empirical autocorrelation of the manager's annual IR.
- **Trade-offs**: the autocorrelation is hard to estimate from a short track record.
- **Reference**: ch17.

## 17. The DSR-Adjusted SR (ch20, 2026 update)

- **When to use**: every time a backtest SR is reported.
- **How**: `DSR` corrects the SR for the number of trials, skew, and kurtosis. A SR of 2.5 is *expected* under the null with 100 trials.
- **Trade-offs**: the DSR is necessary but not sufficient; the OOS test is the only sufficient test.
- **Reference**: ch20; see also `lopez-de-prado-afml` ch14 for the formal definition.

## 18. The Harvey–Liu 3.0 t-stat (ch20, 2026 update)

- **When to use**: when setting the bar for statistical significance in finance.
- **How**: t-stat ≥ 3.0 for individual signals (after multiple-testing correction).
- **Trade-offs**: a stricter bar than the textbook 2.0; most published anomalies fail the bar.
- **Reference**: ch20.
