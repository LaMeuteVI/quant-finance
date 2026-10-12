# Patterns — CFA Derivatives Recipes

## Futures Margin Cash-Flow Table
**When to use**: any margin-call question or funding projection for futures.
**How**: 1. balance_t = balance_{t−1} + (f_t − f_{t−1}) × size. 2. If balance < maintenance, deposit initial − balance (not maintenance − balance). 3. Check: deposits + cumulative P&L = ending balance.
**Trade-offs**: daily settlement removes credit risk but creates funding (liquidity) risk that a forward lacks. (ch 01)

## Replicate-then-Price
**When to use**: pricing any forward commitment or European option.
**How**: 1. Write the payoff. 2. Build it from underlying + bond (+ other derivatives). 3. Its cost today is the price. 4. Any other price: sell dear, buy cheap.
**Trade-offs**: needs a storable, shortable underlying, frictionless borrowing at r, known carry. (ch 01, 02)

## Carry Arbitrage / Reverse Carry
**When to use**: market forward differs from F₀ = FV(S₀ + CC − CB).
**How**: 1. Compute model F₀ (dividend compounds only from payment date to T). 2. F too high: sell forward, borrow, buy spot; too low: buy forward, short spot, lend. 3. Profit at T = mispricing; PV at 0 = value today.
**Trade-offs**: fails without short-sale proceeds, with frictions, for non-storable underlyings. (ch 02, 03)

## Value a Forward Commitment Mid-Life
**When to use**: marking a forward, FRA, bond forward, swap.
**How**: 1. Price a fresh contract with the same expiry (F_t). 2. V_long = (F_t − F₀)/(1 + r)^(T−t). 3. Cross-check: S_t − PV(remaining benefits) + PV(remaining costs) − F₀/(1 + r)^(T−t).
**Trade-offs**: use remaining carry only; futures value is zero after settlement. (ch 02, 03)

## FRA Pricing and Settlement
**When to use**: X × Y FRA rate, value, or payoff.
**How**: 1. FRA₀ = {[1 + L_Y t_Y]/[1 + L_X t_X] − 1}/t_m (ACT/360). 2. Long settles at X: NA(L_m − FRA₀)t_m/(1 + D_m t_m). 3. Mid-life: recompute FRA_g on remaining days, discount.
**Trade-offs**: n spot rates give n(n−1)/2 FRA rates; arithmetic-average shortcut is slightly high. (ch 03)

## Bond Futures Price from Carry
**When to use**: pricing a Treasury/Bund futures or testing arbitrage.
**How**: 1. S₀ = B₀ + AI₀. 2. F₀ = FV(S₀) − AI_T − FV(coupons in window). 3. Quoted Q₀ = F₀/CF (for the CTD). 4. CTD = deliverable maximizing invoice − dirty cost.
**Trade-offs**: CTD switches with yield level (above 6%: long duration/low coupon). (ch 03, 06)

## Par Swap Rate and Swap Revaluation
**When to use**: pricing a vanilla swap; marking it later.
**How**: 1. DF_i = 1/(1 + R_i·NAD/NTD). 2. s = (1 − DF_n)/ΣDF_i, annualize. 3. Later, on a payment date: V_payer = N(s_t − s₀)ΣDF_remaining (s_t = today's par rate for remaining tenor). 4. Receiver = −V.
**Trade-offs**: valid on payment dates; between dates floating leg = (N + next coupon) discounted. (ch 02, 03)

## Currency Swap Pricing and Valuation
**When to use**: fixed-for-fixed or fixed-for-floating cross-currency swaps.
**How**: 1. NA_a = S₀ × NA_b. 2. Solve r_a and r_b from each currency's DFs. 3. V_CS (receiver of a) = NA_a[r_a ΣPV_a + PV_n,a] − S_t NA_b[r_b ΣPV_b + PV_n,b]. 4. Counterparty = −V_CS, converted at S_t.
**Trade-offs**: two risk sources (rates in each currency, spot); check which currency is "a". (ch 03)

## Equity Swap Valuation
**When to use**: receive equity, pay fixed.
**How**: 1. Fixed rate = par swap rate. 2. Value to the fixed receiver (pays equity): V = V_FIX − (S_t/S_{t−1})·NA_E − PV(Par − NA_E), with V_FIX the fixed bond valued on today's curve and Par = NA_E when notionals match (the equity receiver's value is −V). 3. Equity leg scales from last reset, not inception.
**Trade-offs**: break-even equity level = S_{t−1} × V_FIX/NA_E. (ch 02, 03)

## Put–Call Parity Arbitrage and Synthetics
**When to use**: option prices look inconsistent; you need a cheaper synthetic.
**How**: 1. Compare S + p with c + PV(X) (or F/PV with forward). 2. Sell expensive side, buy cheap. 3. Synthetics: call = put + S − PV(X); put = call − S + PV(X); asset = call − put + PV(X).
**Trade-offs**: European, no dividends (else use S − PV(D)); American early-assignment. (ch 02, 05)

## Binomial Valuation (1-period, multi-period, American)
**When to use**: option values, exercise timing, mispricing arbitrage.
**How**: 1. u, d; π = (1 + r − d)/(u − d); needs d < 1 + r < u. 2. Terminal payoffs. 3. Roll back one step: [πV⁺ + (1 − π)V⁻]/(1 + r). 4. American: max(continuation, exercise) at each node. 5. h = ΔV/ΔS. 6. Market > model: write option, buy h shares, borrow.
**Trade-offs**: dividends via escrow; rate trees discount node by node. (ch 02, 04)

## BSM / Black Model Selection
**When to use**: pricing European options quickly.
**How**: 1. Spot with carry: BSM with γ (δ or r_f). 2. Futures/forward: Black with e^(−rT). 3. Caplet: AP·e^(−r(t_{j−1}+t_m)) discounting, σ on FRA rate, d1/d2 use expiry. 4. Swaption: AP·PVA, forward swap rate, T = swaption expiry.
**Trade-offs**: European only; smile means the flat-vol assumption fails. (ch 04)

## Delta–Gamma Hedge of an Option Book
**When to use**: neutralizing exposure of a short or long option position.
**How**: 1. Fix gamma/vega with options (stock has zero). 2. N_H = −Δ_portfolio/Δ_H with stock/forwards. 3. Approximate: Δc + Δ·ΔS + ½Γ(ΔS)².
**Trade-offs**: jumps, discrete rebalancing, costs leave gamma risk. (ch 04)

## Strategy Selection (Direction + Volatility)
**When to use**: choosing an option structure.
**How**: 1. State direction and implied-vol view vs your forecast. 2. Map: vol ↓ → write calls/straddle/puts; vol unchanged → collar, calendar, risk reversal; vol ↑ → buy puts/straddle/calls. 3. Check V_T, max gain/loss, breakeven; choose strike by (target − BE)/premium. 4. Check Greeks.
**Trade-offs**: event straddles lose when implied vol already jumped. (ch 05)

## Zero-Cost Collar
**When to use**: protecting a concentrated, low-basis holding.
**How**: 1. Buy OTM put X₁ at p₀. 2. Sell OTM call X₂ so c₀ = p₀ (OTC). 3. Profit range: [X₁ − S₀, X₂ − S₀] net of premium; narrow to X₁ = X₂ for a synthetic T-bill.
**Trade-offs**: forgone upside above X₂ is the cost. (ch 05)

## Duration Adjustment with Swaps
**When to use**: changing portfolio duration without trading bonds, or converting liabilities.
**How**: 1. N_S = [(MDUR_T − MDUR_P)/MDUR_S] × MV_P. 2. Pay-fixed has negative duration. 3. Floating liability → pay fixed; fixed → receive fixed/pay floating.
**Trade-offs**: OTC credit, MTM on unwind, credit spread risk. (ch 06)

## Bond-Futures BPV Hedge
**When to use**: changing duration with Bund/Treasury futures.
**How**: 1. BPV_P, BPV_T = MDUR × 0.0001 × MV_P. 2. BPV_CTD = MDUR_CTD × 0.0001 × (price/100 × size). 3. BPVHR = (BPV_T − BPV_P)/BPV_CTD × CF. 4. Round; negative = sell.
**Trade-offs**: CTD switch, convexity, non-parallel shifts. (ch 06)

## Equity Futures Beta Adjustment and Equitization
**When to use**: change beta, equitize cash, reallocate.
**How**: 1. N_f = [(β_T − β_S)/β_f] × (S/F), F = price × multiplier. 2. Cash equitization: β_S = 0. 3. Reallocation: sell leg uses stock beta; buy leg starts at β_S = 0; bonds use BPV_P = 0.
**Trade-offs**: beta instability, roll, cash settlement. (ch 06)

## Rate-Futures Hedge and Fed Funds Probability
**When to use**: locking a borrowing/deposit rate; reading Fed expectations.
**How**: 1. Borrower sells, depositor buys (BPV $25 per $1m 3-month contract). 2. Effective rate = loan rate − futures gain. 3. P(move) = (100 − price − FF_mid)/(FF_mid,after − FF_mid).
**Trade-offs**: month-end FFE dips bias probabilities. (ch 06)

## Variance Swap Marking and Settlement
**When to use**: valuing or settling variance exposure.
**How**: 1. N_var = N_vega/(2K). 2. Expiry: N_var(σ_real² − K²). 3. Mid-life: N_var·PV(T−t)[(t/T)RV² + ((T−t)/T)IV² − K²].
**Trade-offs**: convex; short side has unlimited loss; seller pays buyer if positive. (ch 06)

## Currency Return and Risk Decomposition
**When to use**: home-currency return/risk of foreign assets.
**How**: 1. R_FX on DC/FC quote (invert if needed). 2. R_DC = (1 + R_FC)(1 + R_FX) − 1. 3. σ² ≈ σ²_FC + σ²_FX + 2σσρ. 4. Riskless foreign asset: σ = (1 + R_FC)σ_FX.
**Trade-offs**: approximation drops the cross-term. (ch 07)

## Forward Hedge Mark-to-Market and Roll
**When to use**: valuing an FX forward mid-life; rolling a hedge.
**How**: 1. Offset: selling base → bid, buying base → offer; all-in = spot + points/10,000. 2. Cash flow = N(F_new − F_orig). 3. Discount at cash-flow currency rate for remaining days. 4. Roll: spot leg settles the old forward; forward leg sets new (mismatched swap resizes).
**Trade-offs**: realized loss must be funded in cash while asset gain is unrealized. (ch 07)

## Minimum-Variance Hedge Ratio
**When to use**: cross, macro or joint R_FC/R_FX hedges.
**How**: 1. Regress R_DC on %ΔS (DC/FC). 2. h* = ρσ(R_DC)/σ(ΔS). 3. Direct forward hedge ≈ 100%.
**Trade-offs**: unstable correlation; can exceed 100%. (ch 07)

## FX Option Hedge Building Blocks
**When to use**: hedging currency with options.
**How**: 1. Find base currency. 2. Buying base: long call/long forward; selling base: long put/short forward. 3. Cheapen: OTM, collar, put spread, 1×2, seagull, barriers. 4. Name the residual risk.
**Trade-offs**: every cost cut gives up protection or upside. (ch 07)

## Hedge-or-Not with Roll Yield
**When to use**: deciding hedge ratio per currency.
**How**: 1. Roll yield = |(F − S)/S|, positive if selling base at premium. 2. Compare with forecast move. 3. Risk-neutral: hedge if expected loss avoided > cost; risk-averse may hedge anyway.
**Trade-offs**: forward rate bias means forecasts beat the forward only sometimes. (ch 07)
