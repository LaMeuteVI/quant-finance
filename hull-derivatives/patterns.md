# Patterns — Pricing & Hedging Recipes (Hull)

## Cash-and-Carry Arbitrage
**When to use**: the market forward/futures price deviates from S₀e^{(r+u−q)T}.
**How**:
- F too high → buy spot, borrow and short the forward.
- F too low → short spot, invest and go long the forward.
**Trade-offs**: needs the ability to short and to borrow. For consumption assets only the upper bound holds (Ch 5).

## Minimum-Variance Futures Hedge
**When to use**: hedging an exposure with futures on a correlated asset.
**How**: h* = ρσ_S/σ_F from a regression of ΔS on ΔF; N* = h*·V_A/V_F. Pick the delivery month just after the hedge ends.
**Trade-offs**: leaves basis risk. Needs funding for margin calls (Ch 3).

## Beta Adjustment with Index Futures
**When to use**: change an equity portfolio's beta without trading its stocks.
**How**: trade (β* − β)·V_A/V_F index futures. A negative number means short.
**Trade-offs**: only systematic risk is hedged; residual idiosyncratic risk remains (Ch 3).

## Duration-Based Hedge
**When to use**: protecting a bond portfolio against parallel rate moves.
**How**: N* = P·D_P/(V_F·D_F), using the CTD's duration for T-bond futures.
**Trade-offs**: fails under twists. Use PCA or bucketed hedges for non-parallel moves (Ch 6, 22).

## Bootstrap a Curve
**When to use**: building zero rates (or hazard rates) from market instruments.
**How**: sort instruments by maturity. Solve for the one unknown rate that reprices each instrument. Interpolate linearly.
**Trade-offs**: the curve is only as smooth as the inputs. The interpolation choice affects forward rates (Ch 4, 7, 24).

## Value by "Forwards Realized, Then Discount"
**When to use**: FRAs, swaps, forwards and most swap variants.
**How**: project each cash flow using forward rates/prices, then discount at OIS.
**Trade-offs**: wrong if the payoff is observed or paid outside its natural numeraire. Then add a convexity, timing or quanto adjustment (Ch 7, 30, 34).

## Replication via Put–Call Parity
**When to use**: creating synthetic positions and spotting option mispricing.
**How**: c − p = S₀ − PV(D) − Ke^{−rT}. Buy the cheap side and sell the rich side.
**Trade-offs**: holds for European options only; American options have bounds (Ch 11).

## Backward Induction on a Tree
**When to use**: American options, options with dividends, convertibles.
**How**: CRR u, d, p. At each node, value = max(exercise, e^{−rΔt}[pf_u + (1 − p)f_d]). Improve accuracy with a control variate (a European option priced by BSM and on the same tree).
**Trade-offs**: dimensionality limit (≤2 factors). Oscillating convergence (Ch 13, 21, 27).

## Monte Carlo with Variance Reduction
**When to use**: path-dependent or multi-asset payoffs.
**How**: simulate ln S exactly under the risk-neutral measure. Use antithetic variates + control variates. Correlate assets with Cholesky. Report the standard error. Use Longstaff–Schwartz for American features.
**Trade-offs**: slow convergence (1/√M). Greeks need common random numbers (Ch 21, 27).

## Delta–Gamma–Vega Neutralization
**When to use**: managing an option book.
**How**: solve for weights in two traded options so that Γ and vega are zero, then neutralize delta with the underlying. Rebalance delta daily.
**Trade-offs**: transaction costs, and model dependence of the Greeks. Works poorly across jumps (Ch 19).

## Synthetic Put (Portfolio Insurance)
**When to use**: protecting an equity portfolio when puts are unavailable or expensive.
**How**: dynamically short index futures in proportion to the put delta, e^{−qT}[1 − N(d₁)].
**Trade-offs**: fails in gaps and illiquidity (Oct 1987) (Ch 19).

## Risk-Neutral Hazard Rate from Spreads
**When to use**: pricing credit-risky instruments and CVA.
**How**: λ̄ ≈ s/(1 − R), or bootstrap from bond or CDS prices.
**Trade-offs**: very sensitive to the assumed R. Risk-neutral PD > real-world PD (Ch 24, 25).

## CVA by Exposure Simulation
**When to use**: pricing counterparty risk on a netting set.
**How**: simulate market variables, revalue the netting set, apply collateral and margin period of risk. Compute EE_t. CVA = Σ q_i(1 − R)EE_i·DF_i.
**Trade-offs**: computationally heavy. Wrong-way risk is often ignored (Ch 9, 24).

## Historical-Simulation VaR / ES
**When to use**: market risk measurement without distribution assumptions.
**How**: apply the last ~500 days of changes to today's positions and take the percentile. ES = the mean of the tail. Add a stressed period.
**Trade-offs**: backward-looking. A slow reaction to regime change unless the data is volatility-scaled (Ch 22).

## Calibrate a Term-Structure Model
**When to use**: pricing Bermudans or path-dependent rate products.
**How**: fix θ(t) to today's curve (Hull–White/BDT). Choose a and σ to minimize errors on caps or swaptions similar to the product.
**Trade-offs**: parameter instability. A one-factor model cannot price correlation-dependent products (Ch 32, 33).

## Static Replication of Exotics
**When to use**: hedging barrier-type options with little rebalancing.
**How**: find vanillas matching the exotic's value on the barrier boundary. Short that portfolio and unwind it when the barrier is hit.
**Trade-offs**: an approximate match between the boundary points (Ch 26).

## Real-Option Valuation
**When to use**: projects with flexibility (defer, expand, abandon).
**How**: use risk-neutral growth μ − λσ for each variable. Build a tree of project value, take the optimal decision at each node, and discount at r.
**Trade-offs**: λ must be estimated, via CAPM or futures (Ch 36).
