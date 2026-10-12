# Chapter 4: Valuation of Contingent Claims
> **Source**: CFA Program Curriculum 2022, Level II, Reading 34 · Derivatives | Robert E. Brooks, PhD, CFA, and David Maurice Gentle, MEc, BSc, CFA

## Core Idea
An option is worth what it costs to **replicate** it. You hold h units of the underlying and borrow or lend the rest, and you rebalance as the price moves. Because replication removes all price risk, the option value does not depend on anyone's risk preferences or expected return. It equals the **risk-free discounted expected payoff under risk-neutral probabilities**. The binomial tree (discrete time, handles American exercise) and Black–Scholes–Merton (continuous time, European only) are two versions of this one idea. Black's model adapts BSM to futures, caps, floors and swaptions, and the Greeks measure how the replicating hedge must change.

## Learning Outcomes Covered
- Describe and interpret the binomial model and its terms (hedge ratio, RN probability, financing).
- Calculate no-arbitrage values of European and American options in a two-period binomial tree.
- Identify an option mispricing and construct the arbitrage.
- Value an interest rate option in a two-period binomial rate lattice.
- Describe a European option value as the PV of its expected payoff under RN probabilities.
- Identify BSM assumptions. Interpret BSM as a leveraged position in the underlying (stock component and bond component).
- Apply BSM to equities (dividend yield) and currencies (foreign rate as carry).
- Apply Black to futures options, interest rate options (caplets/floorlets) and swaptions.
- Interpret delta, gamma, theta, vega and rho. Execute a delta hedge. Explain gamma risk.
- Define implied volatility and explain its use in quoting and trading options.

## Frameworks Introduced
- **The arbitrageur's two rules**: Rule #1 *do not use your own money*. Rule #2 *do not take any price risk*. Any strategy that obeys both and still produces a positive cash flow today is an arbitrage. Pricing is the level at which no such strategy exists (the **law of one price**).
  - Working assumptions: replicating instruments are identifiable and investable; no frictions (costs, taxes); short selling is allowed with full use of proceeds; the underlying follows a known distribution; borrowing and lending are available at a known risk-free rate.
- **No-arbitrage (replication) approach, one period**:
  - When to use: always valid, for European and American options alike. It is the *only* correct approach when early exercise matters.
  - How:
    1. Build the terminal payoffs c⁺ and c⁻.
    2. Set h = (c⁺ − c⁻)/(S⁺ − S⁻). This makes "write one call and buy h shares" riskless, because −c⁺ + hS⁺ = −c⁻ + hS⁻.
    3. Finance the riskless terminal amount: c = hS + PV(−hS⁻ + c⁻).
  - Interpretation: **long call = long h shares, partly financed by borrowing**. **Long put = short |h| shares plus lending**. Writing reverses these: a call writer shorts stock and lends, a put writer buys stock on margin.
- **Expectations approach**: c = PV_r[π·c⁺ + (1 − π)·c⁻], with π = (1 + r − d)/(u − d).
  - It gives exactly the same value as replication and is faster to compute.
  - π is the **risk-neutral (RN) probability**. It comes out of the arbitrage argument, not from an assumption about investors' risk preferences. It is not the true probability of an up move, and the discount rate is r, not a risk-adjusted rate.
  - Limitation: it is valid only for European payoffs when used over several periods at once. For American options, apply it **one period at a time** and compare the result with the exercise value at every node.
- **Two-period tree = three one-period trees**:
  - Work backward: Time-2 payoffs, then the two Time-1 nodes, then Time 0.
  - With constant u and d the tree **recombines** (S⁺⁻ = S⁻⁺), so n steps give n + 1 terminal nodes instead of 2ⁿ.
  - Replication is **dynamic** (h changes at each node) and **self-financing** (rebalancing is funded by new borrowing or lending inside the strategy, with no outside cash).
- **American-option rule (backward induction)**: at each node, value = Max(continuation value, exercise value).
  - The **early exercise premium** is the American value minus the European value.
  - American **calls on non-dividend-paying stock** are never exercised early, because the call is worth more alive than its exercise value (**⚠ Errata** wording: "non-dividend-paying call options on non-dividend-paying stock").
  - American **puts** can be optimal to exercise early when deep in the money: interest earned on the strike proceeds exceeds the remaining time value.
  - American **calls on dividend-paying stock** can be exercised just before the ex-dividend date to capture the dividend.
- **Escrow method for known dividends**:
  - Split the stock: Ŝ = S − γ, where γ is the PV of the known dividends.
  - Build the tree on Ŝ. The pre-dividend price at a node = Ŝ_node + dividend. Test early call exercise against that price.
- **Interest-rate lattice valuation**:
  - The underlying is the spot rate itself. Take the RN probability as 0.5 when the lattice is built for it.
  - Discount **one period at a time using each node's own rate**, never a single (1 + r)².
- **BSM as a dynamic replicating portfolio**: cost = n_S·S + n_B·B, with B = X·e^(−rT).
  - Call: n_S = e^(−δT)·N(d1) > 0 and n_B = −N(d2) < 0, i.e. buy stock and borrow (**leveraged stock**).
  - Put: n_S = −e^(−δT)·N(−d1) < 0 and n_B = N(−d2) > 0, i.e. short stock and lend.
  - Short put = over-leveraged long stock: the borrowing exceeds 100% of the stock cost.
  - The hedge is "buy high, sell low". Under BSM the cumulative rebalancing losses exactly equal the premium.
- **Black family**: use Black whenever the underlying is costless to carry (a futures or forward price, an FRA rate, a forward swap rate).
  - Adjust for three things: (1) the accrual period AP; (2) where the discounting happens (payment date, or an annuity); (3) which time enters d1 and d2 (option expiry).
- **Gamma-then-delta hedging**:
  1. Stock has zero gamma, so fix gamma first by trading options.
  2. Then neutralize delta with stock. Stock trades change delta without touching gamma.

## Key Concepts
- **Contingent claim**: a derivative giving a right, not an obligation, to a payoff that depends on an underlying.
- **Exercise (intrinsic) value**: Max(0, S − X) for a call and Max(0, X − S) for a put. At expiration the option equals this value.
- **Time value**: option value minus exercise value. It is non-negative because payoffs are asymmetric, and it is zero at expiry.
- **Hedge ratio (h)**: units of the underlying that make an option-plus-underlying position riskless over one step. It is positive for calls and negative for puts.
- **Risk-neutral probability (π)**: the probability that makes the expected return on the underlying equal the risk-free rate. It is independent of the true drift.
- **Dynamic replication / self-financing**: the replicating portfolio is rebalanced over time without any outside cash.
- **Early exercise premium**: American value minus European value.
- **Geometric Brownian motion (GBM)**: continuous price path with lognormal prices and normally distributed log returns. Prices can never go negative.
- **Carry benefit (γ)**: continuous yield from holding the underlying: the dividend yield δ, the foreign rate r_f, or coupons. Carry costs (e.g., storage) are negative carry benefits.
- **N(d2)**: the RN probability that a call finishes in the money, Prob(S_T > X). N(−d2) is the same probability for a put.
- **Caplet / floorlet**: an interest rate call / put on one reset period. A **cap** (floor) is a strip of caplets (floorlets) with the same strike and sequential expiries.
- **Payer swaption**: the right to *pay fixed* and receive floating. **Receiver swaption**: the right to *receive fixed*.
- **Advanced set, settled in arrears**: the rate is fixed at t_{j−1} and paid at t_j = t_{j−1} + t_m.
- **Delta / gamma / theta / vega / rho**: sensitivity of value to, respectively, S, delta itself, calendar time, volatility and the risk-free rate, each with everything else held constant ("static" risk measures).
- **Gamma risk**: the risk that the underlying *jumps* and leaves a delta-hedged book unhedged. This is the non-linearity risk left after delta neutrality.
- **Implied volatility**: the σ that makes the model price equal the market price. It is the market's quoting unit for options.
- **Volatility smile/skew; term structure of volatility; volatility surface**: IV plotted against strike, against expiry, and against both. Under BSM the surface would be flat.

## Formulas & Reference Tables
**Binomial (per-period rate r, up factor u = S⁺/S, down factor d = S⁻/S)**
- `h = (c⁺ − c⁻)/(S⁺ − S⁻)` (calls, h ≥ 0); `h = (p⁺ − p⁻)/(S⁺ − S⁻)` (puts, h ≤ 0)
- `c = hS + PV(−hS⁻ + c⁻) = hS + (−hS⁻ + c⁻)/(1 + r)`; the same form for puts: `p = hS + PV(−hS⁻ + p⁻)`
- `π = (1 + r − d)/(u − d)`; no-arbitrage requires `d < 1 + r < u`
- One period: `c = [πc⁺ + (1 − π)c⁻]/(1 + r)`, and likewise for puts.
- Two periods (European only): `c = [π²c⁺⁺ + 2π(1 − π)c⁺⁻ + (1 − π)²c⁻⁻]/(1 + r)²`
- Terminal nodes: `S⁺⁺ = u²S`, `S⁺⁻ = udS`, `S⁻⁻ = d²S`
- Put–call parity (any model, European): `S + p = PV(X) + c`
- Escrow: `Ŝ = S − PV(dividends)`

**BSM (continuous r, carry benefit γ: γ = δ for stocks, γ = r_f for FX; 0 for a non-dividend stock)**
- `c = S·e^(−γT)·N(d1) − X·e^(−rT)·N(d2)`
- `p = X·e^(−rT)·N(−d2) − S·e^(−γT)·N(−d1)`
- `d1 = [ln(S/X) + (r − γ + σ²/2)·T]/(σ√T)`, `d2 = d1 − σ√T`
- Carry-adjusted parity: `p + S·e^(−γT) = c + X·e^(−rT)`
- PV of expected payoff: `c = e^(−rT)·E(c_T)`, with `E(c_T) = S·e^((r−γ)T)·N(d1) − X·N(d2)`
- `N(−x) = 1 − N(x)`; the continuous and annual rates are linked by `e^r = 1 + r_annual`
- FX: S and X are quoted in **domestic currency per unit of foreign**, r is the domestic rate and γ = r_f is the foreign rate. Multiply the formula value by the notional.

**Black (futures/forward underlying)**
- `c = e^(−rT)·[F₀(T)·N(d1) − X·N(d2)]`, `p = e^(−rT)·[X·N(−d2) − F₀(T)·N(−d1)]`
- `d1 = [ln(F₀(T)/X) + (σ²/2)·T]/(σ√T)`, `d2 = d1 − σ√T`
- Parity: `c − p = e^(−rT)·[F₀(T) − X]`

**Standard market model: interest rate options (notional 1; rates in decimals)**
- Caplet: `c = AP·e^(−r(t_{j−1} + t_m))·[FRA(0,t_{j−1},t_m)·N(d1) − R_X·N(d2)]`
- Floorlet: `p = AP·e^(−r(t_{j−1} + t_m))·[R_X·N(−d2) − FRA(0,t_{j−1},t_m)·N(−d1)]`
- `d1 = [ln(FRA/R_X) + (σ²/2)·t_{j−1}]/(σ√t_{j−1})`, `d2 = d1 − σ√t_{j−1}`
- Here AP = accrual period (e.g., 90/360), t_{j−1} = option expiry (ACT/365), t_m = tenor of the underlying deposit, and σ = volatility of the FRA rate.

**Swaptions (T = swaption expiry; notional 1)**
- `PVA = Σⱼ₌₁ⁿ PV(0, tⱼ)` (annuity discount factor over the swap's payment dates)
- Payer: `PAYSWN = AP·PVA·[R_FIX·N(d1) − R_X·N(d2)]`
- Receiver: `RECSWN = AP·PVA·[R_X·N(−d2) − R_FIX·N(−d1)]`
- `d1 = [ln(R_FIX/R_X) + (σ²/2)·T]/(σ√T)`, `d2 = d1 − σ√T`, where R_FIX is the **forward** swap rate.
- There is no separate e^(−rT) factor, because PVA already embeds the discounting.

**Greeks (BSM, dividend yield δ)**. Delta and gamma are the reading's formulas. The rest are the standard BSM results, added for completeness.
| Greek | Call | Put | Sign (long) |
|---|---|---|---|
| Delta | `e^(−δT)·N(d1)`, in [0, e^(−δT)] | `−e^(−δT)·N(−d1)`, in [−e^(−δT), 0] | call +, put − |
| Gamma | `e^(−δT)·n(d1)/(S·σ·√T)` | same as call | + (peaks ATM) |
| Vega | `S·e^(−δT)·n(d1)·√T` | same as call | + (peaks ATM) |
| Theta (per yr) | `−S·e^(−δT)·n(d1)·σ/(2√T) − rX·e^(−rT)·N(d2) + δS·e^(−δT)·N(d1)` | `−S·e^(−δT)·n(d1)·σ/(2√T) + rX·e^(−rT)·N(−d2) − δS·e^(−δT)·N(−d1)` | usually − |
| Rho | `X·T·e^(−rT)·N(d2)` | `−X·T·e^(−rT)·N(−d2)` | call +, put − |
Here n(x) = e^(−x²/2)/√(2π) is the standard normal density.
- Delta hedge: `N_H = −Portfolio delta / Delta_H`. A negative N_H means short the hedging instrument.
- Delta approximation: `ĉ ≈ c + Delta_c·(Ŝ − S)`
- Delta-plus-gamma approximation: `ĉ ≈ c + Delta_c·(Ŝ − S) + (Gamma_c/2)·(Ŝ − S)²`

**Model component map (Exhibit 14 generalized)**
| Model | Call: underlying leg | Call: financing leg | Put: underlying leg | Put: financing leg |
|---|---|---|---|---|
| Binomial | hS (h > 0) | PV(−hS⁻ + c⁻) < 0 (borrow) | hS (h < 0) | PV(−hS⁻ + p⁻) > 0 (lend) |
| BSM | S·e^(−δT)·N(d1) | −X·e^(−rT)·N(d2) | −S·e^(−δT)·N(−d1) | X·e^(−rT)·N(−d2) |
| Black | F·e^(−rT)·N(d1) | −X·e^(−rT)·N(d2) | −F·e^(−rT)·N(−d1) | X·e^(−rT)·N(−d2) |

**Equivalences (put–call parity for rates)**
| Position | Equivalent |
|---|---|
| Long cap + short floor, strike = swap rate | Pay-fixed / receive-floating swap (zero cost at inception) |
| Long floor + short cap, same strike | Receive-fixed / pay-floating swap |
| Long IR call − IR put, strike = FRA rate | Receive-floating, pay-fixed FRA |
| Long payer − short receiver swaption, same strike | Pay-fixed forward swap. Equal values ⇔ strike = at-market forward swap rate |
| Long callable fixed-rate bond | Long straight bond + **short receiver swaption** |

## Mental Models
- **Think of every option as "some stock plus some bond".** A call is leveraged stock and a put is shorted stock plus lending. Delta is the stock part and the N(d2) term is the bond part. You then know the sign of every Greek without memorizing it.
- **Risk-neutral pricing is an accounting shortcut, not a belief.** π and N(d2) are the probabilities that *make replication consistent*. Use them for pricing, never as forecasts of exercise likelihood.
- **Use the binomial tree when path or exercise timing matters** (American puts, dividend-motivated call exercise, rate-dependent discounting). **Use BSM/Black for European payoffs** when you want closed forms and Greeks.
- **Pick the model by its underlying.** Spot with carry → BSM with γ. Futures/forward price → Black. FRA rate → caplet model, discounted to the *payment* date. Forward swap rate → swaption model with an annuity.
- **Gamma is the price of convexity and theta is the rent.** A long option position is long gamma and long vega and pays theta. A delta-hedged short option makes money when nothing happens and loses on jumps.

## Worked Example
**1. Two-period tree, European vs American put.** Inputs: S = 72, X = 75, u = 1.356, d = 0.541, r = 3% per period, no dividends.
- RN probability: π = (1.03 − 0.541)/(1.356 − 0.541) = **0.60**.
- Time-2 prices and payoffs:

| Node | Price | Call payoff | Put payoff |
|---|---|---|---|
| S⁺⁺ | 132.389 | 57.389 | 0 |
| S⁺⁻ | 52.819 | 0 | 22.181 |
| S⁻⁻ | 21.073 | 0 | 53.927 |

- Time-1 values:
  - Up node (S⁺ = 97.632): p⁺ = (0.6×0 + 0.4×22.181)/1.03 = **8.614**, hedge ratio −0.2788. c⁺ = 0.6×57.389/1.03 = **33.430**, h = 0.7212.
  - Down node (S⁻ = 38.952): p⁻ = (0.6×22.181 + 0.4×53.927)/1.03 = **33.864**, h = −1.
- Time 0, European: c = 0.6×33.430/1.03 = **19.474** (h = 0.5697). p = (0.6×8.614 + 0.4×33.864)/1.03 = **18.169** (h = −0.4303).
  - Check with the two-period formula: 0.6²×57.389/1.03² = 19.474 ✓.
  - Put–call parity: 19.474 + 75/1.03² − 72 = 18.169 ✓.
- American put:
  - At the down node, the exercise value 75 − 38.952 = 36.048 exceeds the continuation value 33.864, so **exercise**. The node premium is 2.184.
  - p_Am = (0.6×8.614 + 0.4×36.048)/1.03 = **19.017**. The hedge ratio moves to (8.614 − 36.048)/(97.632 − 38.952) = −0.4675.
  - Early exercise premium at t = 0: 19.017 − 18.169 = **0.848**.
- American call = European call = 19.474 (no dividends).
- Replication at t = 0: buy 0.5697 shares (cost 41.02) and borrow 0.5697×38.952/1.03 = 21.545, so net cost = 19.47 = c.
- Interpretation: the put's value at the down node is worth more as cash earning 3% than as an option. That is the typical deep-ITM American put case.

**2. BSM price and Greeks.** Inputs: S = X = 100, r = 5% (continuous), T = 1, σ = 30%, δ = 0.
- d1 = [0 + (0.05 + 0.045)×1]/0.30 = **0.3167**, d2 = **0.0167**.
- N(d1) = 0.6243, N(d2) = 0.5066, PV(X) = 95.123.
- Prices:
  - c = 100×0.6243 − 95.123×0.5066 = **14.23**.
  - p = 95.123×0.4934 − 100×0.3757 = **9.35**.
  - Parity check: c − p = 4.88 = S − PV(X) ✓.
- Replication:
  - Call: buy 0.6243 shares and short 0.5066 zero-coupon bonds priced at 95.123.
  - Put: short 0.3757 shares and buy 0.4934 bonds.
- Greeks:

| Greek | Call | Put | Notes |
|---|---|---|---|
| Delta | 0.6243 | −0.3757 | |
| Gamma | 0.0126 | 0.0126 | |
| Vega | 37.94 per 1.00 of σ | same | ≈ 0.38 per vol point |
| Theta | −8.10 per year | −3.35 per year | call ≈ −0.022 per day |
| Rho | 48.19 | −46.93 | ≈ +0.48 / −0.47 per 1% of r |
- Approximation check (actual BSM value in parentheses):

| New S | Delta only | Delta + gamma | Actual | Comment |
|---|---|---|---|---|
| 90 | 7.99 | 8.62 | 8.66 | both approximations low |
| 110 | 20.47 | 21.11 | 21.06 | delta + gamma slightly high |
| 150 | 45.44 | 61.25 | 55.88 | gamma overshoots on large up moves |

- This matches the reading's exhibits. Delta alone is biased low both ways for a long call. Delta + gamma is low on down moves and high on up moves.
- Same inputs with δ = 5%: call delta 0.532, put delta −0.419. To hedge a short position in puts on 10,000 shares:
  - With stock: portfolio delta = +4,190, so N_H = −4,190/1, i.e. **short 4,190 shares**.
  - With calls: N_H = −4,190/0.532, i.e. **sell 7,876 calls**.

**3. Interest-rate option on a binomial lattice.** Two-year European call and put on the 1-year rate. Strike 3.25%, notional US$1m, RN probability 0.5, cash settled at t = 2 (deferred settlement ignored).
- Lattice:
  - t = 0: rate 3.0454% (discount factor 0.970446).
  - t = 1: rates 3.9084% and 2.6034% (discount factors 0.962386 and 0.974627).
  - t = 2: rates 3.9706%, 3.2542% and 2.2593%.
- Call payoffs per 1: 0.007206, 0.000042, 0.
  - c⁺ = 0.962386×½(0.007206 + 0.000042) = 0.003488.
  - c⁻ = 0.974627×½(0.000042) = 0.0000205.
  - c = 0.970446×½(0.003488 + 0.0000205) = 0.0017022, i.e. **US$1,702**.
- The put works the same way: **US$2,343**.
- Each node uses its own discount factor.

## Anti-patterns
- **Using true (subjective) probabilities or a risk-adjusted discount rate**: this breaks the arbitrage-free price. Use π and r only.
- **Discounting a two-period expectation by (1 + r) once**: the two-period PV factor is 1/(1 + r)².
- **Valuing an American put with the multi-period expectation formula (Equation 9)**: it ignores exercise at interior nodes. Roll back node by node with Max(continuation, exercise).
- **Using a single flat rate in an interest-rate tree**: rates are the underlying and vary by node.
- **Feeding spot into Black**: the Black underlying is the futures/forward price. The risk-free rate is r, not the dividend yield.
- **Discounting a caplet from option expiry**: the payoff is set at t_{j−1} but paid at t_{j−1} + t_m, so discount to the payment date. d1 and d2 still use t_{j−1}.
- **Using the swap tenor as T in a swaption**: T is the swaption's expiry. The tenor enters only through PVA.
- **Adjusting gamma with stock**: stock has zero gamma. Only options change gamma or vega.
- **Treating delta hedging as a full hedge**: it only covers small moves. Jumps, discrete rebalancing and transaction costs leave gamma risk and hedging costs.

## Exam Focus & Traps
- **Hedge-ratio sign**: call h ∈ [0, 1] (buy stock), put h ∈ [−1, 0] (short stock). When both terminal puts are ITM, h = −1.
- **Replication legs**: call = buy stock + borrow; put = short stock + lend; short call = short stock + lend; short put = buy stock + borrow.
- **Arbitrage when the market call > model value**: write the call, buy h shares and borrow PV(hS⁻ − c⁻). Pocket the difference with zero cash flow at t = 1 (e.g., Alpha: model 3.714, market 4.50, profit 0.787). When the market price is below model, reverse all legs.
- **Changing the strike changes the payoffs, not π.** π depends only on u, d and r (for rate trees, on the lattice).
- **N(d1) vs N(d2)**: N(d1) drives delta and the number of shares. N(d2) is the RN probability of finishing ITM and the number of bonds.
- **Carry effects**: higher dividend yield or foreign rate → lower call, higher put, fewer shares to buy for a call and more to short for a put.
- **FX options**: domestic r is the discount rate and the foreign rate is the carry. A euro put for a yen-based exporter is quoted in ¥/€.
- **Black for index futures (Example 14)**: F = 1,851.65, X = 1,860, r = 0.2%, T = 0.25, σ = 15% → c = **51.41**, p = **59.76**. Parity: c − p = e^(−rT)(F − X) = −8.35 ✓.
- **Delta hedge signs**: short calls → buy stock; short puts → *short* stock; long stock → sell calls (10,000 shares hedged with 0.6232-delta calls means selling ≈ 16,046 calls).
- **Spot vs futures delta**: a delta computed against the *spot* index with a dividend yield (e.g., 0.6232) differs from Black's futures delta e^(−rT)N(d1) (≈ 0.627 on the same inputs). Check which one the question uses.
- **Gamma**: call gamma = put gamma, and call vega = put vega (parity: S − PV(X) has delta 1, gamma 0, vega 0). Buying any option raises gamma. A delta-hedged short option is short gamma.
- **Implied vs historical vol**: if the model price at historical σ > market price, then implied σ < historical σ.
- **Theta** is usually negative and accelerates near expiry for ATM options. Theta has no uncertainty (time only moves forward).
- **Vega**: the option value is most sensitive to σ among the BSM inputs. At σ → 0 a European call → Max(0, S − PV(X)) (e.g., 4.88 for S = X = 100, r = 5%, T = 1).
- **Rho**: call positive, put negative, small relative to delta and vega. For interest rate options, the rate exposure is captured by *delta*, not rho.
- **⚠ Correction**: the reading's Practice Problem 11 solution writes the put bond position as "n_B = −N(d2) > 0". The correct expression is **n_B = N(−d2) > 0**.

## Key Takeaways
1. Option value = cost of self-financing replication = e^(−rT) × expected payoff under RN probabilities. The two approaches always agree for European options.
2. In a tree, compute π = (1 + r − d)/(u − d) and h = Δoption/ΔS, and roll back one step at a time. For American options, take Max(continuation, exercise) at every node.
3. Early exercise matters for American puts (deep ITM) and for calls just before a dividend. It never matters for calls on non-dividend-paying stock.
4. BSM = long e^(−δT)N(d1) shares financed by short N(d2) bonds (call). Carry benefits enter as e^(−γT) on S and in d1.
5. Black-family models price options on costless-to-carry underlyings. Caplets add AP and discount to the payment date. Swaptions add AP × PVA.
6. Delta-hedge with N_H = −Δ_portfolio/Δ_H. Manage gamma and vega with options first, then set delta with stock.
7. Implied volatility is the market's quoting currency. A non-flat smile or surface is evidence that BSM's assumptions fail.

## Connects To
- **ch02**: L1 basics: replication, put–call parity, the one-period binomial model and the lower bounds used here.
- **ch03**: forward/futures/swap pricing supplies the F, FRA and forward swap rates that feed Black models.
- **ch05**: options strategies are applied here. Greeks, delta hedging and implied-vol trading (straddles, spreads, skew) build directly on this chapter.
- **ch06**: swaps/forwards/futures strategies. Swaptions and caps as rate-risk tools.
- **`hull-derivatives` ch13**: binomial trees in depth (u = e^(σ√Δt), American options, dividends).
- **`hull-derivatives` ch15**: BSM derivation, lognormal property and implied volatility.
- **`hull-derivatives` ch19**: the Greek letters, dynamic delta/gamma/vega hedging in practice.
- **`hull-derivatives` ch20**: volatility smiles and surfaces.
- **`passarelli-option-greeks` ch02**: a trader's view of delta, gamma, theta and vega.
- **`passarelli-option-greeks` ch12–ch13**: delta-neutral trading of implied vs realized volatility, the practical side of gamma risk.
- **`cfa-fixed-income` ch08–ch09**: binomial interest-rate lattices and valuing callable/putable bonds (the callable bond is a straight bond minus a receiver swaption).
