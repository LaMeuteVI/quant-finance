# Chapter 26: Exotic Options

## Core Idea
Exotics change the payoff rules: path dependence, several assets, triggers, compounding. Under BSM assumptions many have closed forms; the rest are handled by numerical methods. Hedging difficulty varies a lot:
- **Asians** are easier to hedge than vanillas.
- **Barriers** and **binaries** are harder, because delta is discontinuous.

## Frameworks Introduced
- **Packages**: combinations of vanillas, forwards, cash and the underlying (bull spreads, range forwards). Zero-cost structures come from choosing strikes.
- **Perpetual American options**: closed form with an optimal exercise barrier. For a call with q > 0, exercise when S hits H*.
- **Nonstandard American options**:
  - **Bermudan**: exercisable on specific dates only.
  - Exercise window only; strike changes over time.
- **Gap option**: the strike used in the payoff (K₁) differs from the trigger level (K₂).
  - Call: `S₀e^{−qT}N(d₁) − K₁e^{−rT}N(d₂)`, with d₁ and d₂ computed from K₂.
- **Forward start option**: an ATM option that starts at T₁. Its value equals the value of an ATM option today with maturity T₂ − T₁, scaled by e^{−qT₁}.
- **Cliquet (ratchet)**: a series of forward-start options.
- **Compound options**: a call on a call, a put on a call, etc. Priced with the bivariate normal.
- **Chooser option**: at t₁ the holder picks call or put. It decomposes into a call(K, T) plus a put(Ke^{−(r−q)(T−t₁)}, t₁).
- **Barrier options**:
  - Knock-in / knock-out, up / down.
  - **In + Out = vanilla** (in–out parity).
  - Down-and-out calls are cheap. Continuous vs discrete monitoring needs a correction: shift the barrier by e^{±0.5826σ√Δt}.
- **Binary options**:
  - Cash-or-nothing call = `Qe^{−rT}N(d₂)`.
  - Asset-or-nothing call = `S₀e^{−qT}N(d₁)`.
  - A vanilla call = asset-or-nothing − K × cash-or-nothing.
- **Lookback options**: payoff on the max or min over the life.
  - **Floating** lookback call pays S_T − S_min.
  - **Fixed** lookback call pays max(S_max − K, 0).
- **Shout option**: the holder locks in the intrinsic value once, and keeps the upside after that.
- **Asian options**: payoff on the average price.
  - Arithmetic averages are approximated by matching the first two moments to a lognormal.
  - They are cheaper than vanillas (lower volatility) and easier to hedge.
- **Exchange option (Margrabe)**: the option to swap asset U for asset V.
  - `V₀e^{−q_V T}N(d₁) − U₀e^{−q_U T}N(d₂)`, with σ² = σ_U² + σ_V² − 2ρσ_Uσ_V. No interest rate appears.
- **Multi-asset options**: rainbow, basket and best-of/worst-of options. Correlation-sensitive; usually priced by Monte Carlo.
- **Volatility and variance swaps**:
  - A variance swap pays (realized variance − K_var) × notional.
  - It is replicated by a strip of OTM options weighted by 1/K², so it is **model-free**.
  - Volatility swaps need a convexity adjustment, since √E[V] ≠ E[√V].
  - **VIX** = the 30-day variance-swap rate computed from S&P 500 options.
- **Static options replication**: match the exotic's value on a boundary with a portfolio of vanillas, then short that portfolio. It needs little rebalancing. Works well for barriers.

## Key Concepts
- **Path-dependent options**: payoff depends on the history of S (Asian, lookback, barrier).
- **Rebate**: cash paid when a barrier is hit (knock-out) or never hit (knock-in).
- **Parisian option**: the barrier must be breached for a set time before it counts.
- **Quanto**: an option on a foreign asset with the payoff paid in the domestic currency (Ch 30).

## Mental Models
- **Decompose first**: most exotics are vanillas, binaries or barriers in disguise. Parity-style identities (in + out = vanilla) give free checks.
- **Barrier delta explodes near the barrier.** Hedge statically, or price in a smile-consistent model.
- **Averaging reduces volatility** by about 1/√3 for an arithmetic Asian, which is why Asians are cheaper.

## Anti-patterns
- **Pricing barriers with a flat ATM volatility**: they are very sensitive to the skew and to the volatility near the barrier.
- **Dynamic delta hedging of binaries near expiry and the strike**: gamma is unbounded. Over-hedge with a call spread instead.
- **Ignoring discrete monitoring** in barrier contracts. Apply the Broadie–Glasserman–Kou shift.

## Worked Example
**Gap put in insurance (Example 26.1).** An asset is worth $500,000, σ = 20%, r = 5%, T = 1. The insurer buys the asset for $400,000 if it falls below that level.
- Priced as a regular put (K = 400k), the policy is worth **$3,436**.
- Now suppose claiming costs the policyholder $50,000. They claim only if S_T < 350k, but the insurer still pays 400k − S_T.
- That is a gap put with K₁ = 400k and K₂ = 350k, worth **$1,896**. Claim costs cut the insurer's cost by ≈ 45%.

**Variance swap (Example 26.4).** 3-month swap: receive realized variance, pay 0.045, on $100m. r = 4%, q = 1%, index = 1020, implied volatilities 29%→21% for strikes 800→1,200.
- F₀ = 1,027.68. The option strip gives expected variance **Ê(V) = 0.0621**.
- Value = 100m × (0.0621 − 0.045) × e^{−0.01} ≈ **$1.69m**.

## Key Takeaways
1. In + Out = vanilla. Vanilla call = asset-or-nothing − K × cash-or-nothing.
2. Many exotics have BSM closed forms: gap, forward start, chooser, barrier, binary, lookback, exchange.
3. Asians are cheap and easy to hedge. Barriers and binaries are hard (discontinuous delta).
4. A variance swap is replicated by a 1/K²-weighted strip of options, independent of any model.
5. Static replication hedges barrier-type exotics with vanillas.

## Connects To
- **Ch 12**: packages.
- **Ch 15 / Ch 17**: BSM building blocks.
- **Ch 20**: exotics' smile sensitivity.
- **Ch 21 / Ch 27**: numerical valuation (path-dependent trees, barrier grids).
- **Ch 28**: change of numeraire for exchange options.
- **Ch 30**: quantos.
