# Chapter 8: The Arbitrage-Free Valuation Framework
> **Source**: CFA Program Curriculum 2022, Level II, Reading 29 · Fixed Income | Steven V. Mann (binomial trees revised by Donald J. Smith)

## Core Idea
A bond is a portfolio of zero-coupon bonds. Its arbitrage-free value is the sum of its cash flows, each discounted at the **spot rate** for its own date. For option-free bonds, spot-rate discounting is all you need.

Bonds with embedded options (and MBS) have **rate-dependent cash flows**. For those, you need a model of how rates can evolve, given as a **binomial interest rate tree** (or Monte Carlo paths). The model must be **calibrated** so that it reprices the benchmark bonds exactly. A calibrated tree gives the same value as the spot curve for any option-free bond. That is the proof that it is arbitrage-free, and it is what makes it safe to use for options.

## Learning Outcomes Covered
- Explain arbitrage-free valuation, the law of one price, and the two types of arbitrage: value additivity and dominance.
- Calculate the arbitrage-free value of an option-free coupon bond from the spot rates (bootstrapped from par).
- Describe the binomial (lognormal) interest rate tree and how to calibrate it to the term structure.
- Apply backward induction. Show that the tree value equals the spot-curve value for option-free bonds.
- Apply pathwise valuation (Pascal's triangle). Describe Monte Carlo forward-rate simulation with a drift adjustment.
- Describe term structure models: one-factor versus multi-factor, **equilibrium** (CIR, Vasicek) versus **arbitrage-free** (Ho–Lee, KWF), and Gauss+.

## Frameworks Introduced
- **Three-step valuation principle**: (1) estimate the future cash flows; (2) choose the discount rate for each cash flow; (3) take the PV. Value = PV of the **expected** future cash flows.
- **Two types of arbitrage opportunity** (no cash outlay, riskless profit):
  - **Value additivity**: the whole must equal the sum of its parts.
    - Example: a zero paying 1 costs 0.952381, so a claim to 105 must cost 100.
    - If the claim to 105 trades at 97, buy it and sell 105 of the unit zeros. You lock in +3 today and owe nothing net in a year.
  - **Dominance**: a riskless payoff must be priced at the same riskless rate.
    - Example: asset C costs 100 and pays 105; asset D costs 200 and pays 220.
    - Sell 2 C (receive 200), buy 1 D (pay 200). Net cost is zero today and you earn +10 in a year.
- **Stripping and reconstitution**: dealers split a Treasury into zeros (strips) and rebuild it. This keeps coupon bonds equal to their package of zeros. Two bonds with the same maturity but different coupons are *different* packages of zeros. Identical cash flows on the same date get the same discount rate, whichever bond they belong to.
- **Binomial lognormal interest rate tree** (one-factor, one-period short rate at each node):
  - Inputs: (1) an interest rate model (lognormal random walk); (2) a volatility σ; (3) the current benchmark curve.
  - Up and down moves each have probability 0.5.
  - Adjacent rates at the same date differ by a factor of **e^{2σ}**: `i₁,H = i₁,L·e^{2σ}`, `i₂,HH = i₂,LL·e^{4σ}`, `i₂,HL = i₂,LL·e^{2σ}`, `i₃,HHH = i₃,LLL·e^{6σ}`.
  - In centered notation, the Time-t rates are `iₜ·e^{kσ}` with k ∈ {t, t−2, …, −t}.
  - The rates are (nearly) centered on the implied forwards. The mean of the lognormal nodes sits slightly **above** the forward: 1.4032% versus 1.4028% below.
  - The tree **recombines** (HL = LH), so the number of nodes grows linearly, not exponentially.
  - Lognormality gives (i) **no negative rates** and (ii) **higher absolute volatility at higher rates**. The σ of the one-year rate is ≈ i₀·σ: at σ = 10% and i₀ = 2%, that is 20bp.
  - Estimate σ from **historical** rate volatility or from the **implied** volatility of swaptions, caps and floors.
- **Backward induction** (value at a node): `V = [C + 0.5·V_H + 0.5·V_L]/(1 + i)`.
  - Start at maturity (par + final coupon) and move right to left.
  - Discount with the one-period rate *at the node you are valuing*.
  - The coupon paid at T+1 is added at T+1, not at the node being valued.
- **Calibration** (how to make the tree arbitrage-free):
  1. Set i₀ = the one-year par rate, which also equals the spot and forward rate.
  2. Guess i₁,L below the implied forward f₁,₁ and set i₁,H = i₁,L·e^{2σ}.
  3. Price the **two-year par benchmark** with backward induction and adjust i₁,L until its price = 100 (use Solver or goal seek).
  4. For Time 2, start from the middle node at the implied forward f₂,₁ and set the others by e^{±2σ}. Solve until the 3-year par bond prices at 100, keeping the Time-1 rates fixed.
  5. Repeat for each later date.
  - Check: every option-free bond priced on the tree equals its spot-curve price.
  - Why it works: each date adds one unknown (the lowest rate) and one constraint (one benchmark price). σ pins down the spacing.
  - Failure mode: the tree is only as good as σ and the model. A mis-specified σ misprices *options*, never option-free bonds.
- **Effect of σ on the tree**: a higher σ spreads the nodes wider around the forward curve. As σ → 0, the tree collapses to the implied forward curve.
  - At σ = 0.01%, the Time-1 rates are 1.4029% and 1.4026%, around the forward of 1.4028%.
- **Pathwise valuation**: (1) list every path through the tree; (2) discount the cash flows along each path using that path's rates, compounding the one-period rates; (3) average across paths.
  - The number of paths to reach date n is 2^{n−1} for an annual tree (Pascal's triangle counts the paths to each node).
  - It gives the same value as backward induction for path-*independent* cash flows.
- **Monte Carlo forward-rate simulation** (for **path-dependent** cash flows such as MBS prepayments):
  1. Simulate many paths (e.g., 500) of one-month rates under a volatility and distribution assumption.
  2. Generate the spot rates along each path.
  3. Generate the cash flows along each path.
  4. Take the PV of each path.
  5. Average across paths.
  - Add a **drift term** (a constant added to all rates on all paths) so that the benchmark bonds reprice. The model is then **drift-adjusted**, and therefore arbitrage-free.
  - Mean reversion can be added by imposing upper and lower bounds that pull rates toward the implied forwards.
  - More paths raise *statistical* accuracy. They do **not** bring the value closer to the "true" fundamental value, which depends on the model and inputs.
- **Term structure model taxonomy**: see the table below.
  - Use **arbitrage-free** models to price and hedge against today's market.
  - Use **equilibrium** models for dynamic, scenario-type applications where you do not want to be forced onto today's curve.

## Key Concepts
- **Arbitrage-free valuation**: pricing so that no zero-cost, riskless-profit trade exists.
- **Law of one price**: perfect substitutes sell at the same price in the absence of transaction costs.
- **Benchmark securities**: liquid, safe bonds whose yields anchor the other rates. On-the-run Treasuries (US), gilts (UK), Bunds (EUR), or the swap curve where the sovereign market is illiquid. The model assumes they are correctly priced.
- **Spot vs YTM discounting**: on an upward curve, discounting early coupons at the YTM over-discounts them (and under-discounts them on a downward curve). Only spot discounting is arbitrage-free.
- **Lattice model**: an interest-rate tree that both **generates** the rate-dependent cash flows and **supplies** the discount rates.
- **One-factor vs multi-factor**:
  - One-factor models (the short rate) move all rates in the same direction over a short interval, though not by the same amount.
  - Two-factor or multi-factor models add, for example, the long rate or the slope.
- **Recombining tree**: an up-then-down path reaches the same node as down-then-up.
- **Path dependence**: the cash flow depends on the path taken to reach the current rate level, not only on the level itself. MBS prepayments are the classic case (burnout).
- **Drift term**: in a stochastic process, the expected (zero-volatility) change θₜdt. In Monte Carlo, it is the calibration constant.
- **Mean reversion**: rates are pulled toward a long-run level θ at speed k.
- **Equilibrium model**: derived from economic fundamentals, with few parameters. It does **not** automatically match current prices and uses real-world probabilities.
- **Arbitrage-free (no-arbitrage) model**: takes the current curve as given and uses time-dependent parameters to fit it exactly. It uses risk-neutral probabilities.
- **Gauss+**: a multi-factor practitioner model with short, medium and long factors.
  - The long factor mean-reverts and reflects macro trends. The medium factor reverts to the long one.
  - The short rate has no random component (the central bank controls it).
  - Result: a **hump-shaped volatility curve**, with medium tenors the most volatile.

## Formulas & Reference Tables
- Spot-rate valuation: `P₀ = Σ CFₜ/(1 + zₜ)^t`
- Bootstrapping from par: `1 = Σ_{t=1..N−1} par_N/(1 + zₜ)^t + (1 + par_N)/(1 + z_N)^N`
- Lognormal tree spacing: `i_{t,H} = i_{t,L}·e^{2σ}`. Top-to-bottom ratio at date t: `e^{2tσ}`. Example: Time 4 top/bottom = e^{8σ} = e^{0.8} at σ = 10%.
- Node value: `V = [C + 0.5·(V_H + V_L)]/(1 + i_node)`
- Path PV: `PV_path = Σ_t CFₜ / Π_{s=0..t−1}(1 + i_{s,path})`. Value = mean over paths.
- Stochastic process (one-factor): `dr = θₜdt + σₜdZ`, with dZ a Wiener increment (normal).

**Term structure models**

| Model | Type | Process | Drift | Volatility | Negative rates? |
|---|---|---|---|---|---|
| Cox–Ingersoll–Ross (CIR) | Equilibrium | `dr = k(θ − r)dt + σ√r dZ` | Mean reversion to θ at speed k | ∝ √r (rises with the level of rates) | No: the diffusion term shrinks as r → 0 |
| Vasicek | Equilibrium | `dr = k(θ − r)dt + σdZ` | Mean reversion (same as CIR) | Constant | Yes (possible) |
| Ho–Lee | Arbitrage-free | `dr = θₜdt + σdZ` | Time-dependent θₜ (fitted to the curve) | Constant | Yes (normal) |
| Kalotay–Williams–Fabozzi (KWF) | Arbitrage-free | `d ln r = θₜdt + σdZ` | Time-dependent θₜ, no mean reversion | Constant σ on ln r, so r is lognormal | No |
| Gauss+ | Multi-factor (practitioner) | Short, medium and long factors | Long factor mean-reverting; medium reverts to long | Hump-shaped across tenors | — |

- **⚠ Correction**: the curriculum's CIR equation lost its square root in extraction. The correct diffusion term is `σ√rₜ dZ`.
- **⚠ Correction**: the text says KWF has a "constant drift" but its own summary table says "time dependent". As an arbitrage-free model, KWF's drift θₜ is time-dependent. It shares **constant volatility and no mean reversion** with Ho–Lee.
- **⚠ Correction**: practice problem 22 calls Ho–Lee and KWF "equilibrium" models. Both are **arbitrage-free**.

**Choosing the valuation method**

| Instrument | Method | Why |
|---|---|---|
| Option-free, fixed CF | Spot-curve discounting (or any calibrated tree) | CFs don't depend on rates |
| Callable/putable bond, cap/floor, floater with options | Calibrated binomial tree + backward induction | CFs depend on rate *level* at each date; exercise decisions at nodes |
| MBS, ABS with prepayment, path-dependent structures | Drift-adjusted Monte Carlo | CFs depend on the *path* (prepayment history) |

## Mental Models
- **The tree is a measuring instrument, and calibration is its zeroing.** Before using it on an option, check that it reprices the par benchmarks and at least one off-market option-free bond to the spot-curve value. If it does not, any option value it gives is an artifact.
- **σ only matters for optionality.** For an option-free bond the tree value is independent of σ, because calibration absorbs it. For a bond with options, σ is the key input. Use this to sanity-check a model: change σ, and an option-free price must not move.
- **Prefer arbitrage-free models for pricing and hedging today, equilibrium models for "what if" dynamics.** A trader marking a callable to market needs Ho–Lee or KWF-style fit. A strategist simulating regimes may prefer CIR or Vasicek mean reversion.
- **Normal vs lognormal is a tail choice, not only a sign choice.** Normal models (Vasicek, Ho–Lee) allow negative rates, which was realistic in 2015–2021 for EUR, CHF and JPY. Lognormal models (KWF, the CFA tree) forbid them. Deep out-of-the-money option values (floors near zero, far-OTM swaptions) depend on which one you pick.
- **Monte Carlo is backward induction's complement.** Trees handle early exercise naturally but cannot handle path dependence. Monte Carlo handles path dependence but struggles with American-style exercise.

## Worked Example
**A. Calibrate a tree from scratch** (rebuilt and verified in Python with a root-finder).
- Inputs: annual par curve of 2%, 3%, 4% (1–3 years); σ = 15%, so e^{2σ} = e^{0.30} = 1.34986.
- Bootstrapped spots: z₁ = 2.000%, z₂ = 3.015%, z₃ = 4.055%.
- Implied forwards: f₁,₁ = 4.040%, f₂,₁ = 6.166%.

1. **Time 0**: i₀ = 2.000%.
2. **Time 1**: solve so that the 3% two-year par bond = 100.
   - Result: i₁,L = **3.442%**, i₁,H = 3.442% × 1.34986 = **4.646%**. Their mean, 4.044%, is slightly above f₁,₁.
   - Check: 103/1.04646 = 98.427 and 103/1.03442 = 99.573; then [3 + 0.5(98.427 + 99.573)]/1.02 = **100.000**.
3. **Time 2**: start the middle node at 6.166%. This gives 99.898 (too low), so lower the rates.
   - Result: i₂ = **8.167% / 6.050% / 4.482%**, which reprices the 4% three-year par bond at **100.000**.
4. **Use the tree**: a 3-year 5% bond.
   - Time-2 values: 105/1.08167 = 97.072; 105/1.06050 = 99.010; 105/1.04482 = 100.496.
   - Time-1 values: [5 + 0.5(97.072 + 99.010)]/1.04646 = 98.466; [5 + 0.5(99.010 + 100.496)]/1.03442 = 101.267.
   - Time 0: [5 + 0.5(98.466 + 101.267)]/1.02 = **102.810**.
5. **Cross-checks**:
   - Spot curve: 5/1.02 + 5/1.03015² + 105/1.04055³ = 102.810, the same value, so the tree is arbitrage-free.
   - Pathwise: the four paths (UU, UD, DU, DD) give 100.530, 102.345, 103.479 and 104.888. Their average is **102.810**.
   - A bond quoted at 102.7751 (priced at its 4% YTM) is therefore **cheap by 0.035** per 100. The market discounted the early coupons at the YTM instead of the lower spot rates.

**B. The curriculum's four-year tree, reproduced** (σ = 15%; par 1.00/1.20/1.25/1.40%).

| Time | Nodes (high → low) |
|---|---|
| 0 | 1.0000% |
| 1 | 1.6121%, 1.1943% |
| 2 | 1.7863%, 1.3233%, 0.9803% |
| 3 | 2.8338%, 2.0994%, 1.5552%, 1.1521% |

- A 4-year 2% bond on this tree is worth **102.3254**, exactly the spot-curve value (spots 1.0000/1.2012/1.2515/1.4045%).
- At σ = 20% the Time-3 nodes widen to 3.2134–0.9678%. At σ = 0.01% they collapse to about 1.8647%, the implied forward f₃,₁.

## Anti-patterns
- **Discounting all cash flows at the YTM to test for arbitrage**: YTM pricing is not arbitrage-free when the curve is not flat. Use spot rates.
- **Discounting all cash flows at the final-maturity spot rate**: a common wrong answer. It under-prices the bond on an upward curve.
- **Using an uncalibrated tree, or one calibrated to the wrong issuer curve**: the option value absorbs the pricing error.
- **Discounting a node's value at the *next* period's rate**, or forgetting to add the coupon at each node.
- **Treating Monte Carlo accuracy as model truth**: 10,000 paths of a wrong model are still wrong.
- **Using a tree for path-dependent MBS**: recombining lattices lose the path history that drives prepayments.
- **Calling calibration a way to find mispriced benchmarks**: calibration *assumes* the benchmarks are correctly priced. It uses them to fix the tree.

## Exam Focus & Traps
- **Arbitrage identification**: price the bond with spot rates. Buy where it trades below that value and sell where it trades above.
  - The "most profitable" trade is buying at the lowest venue and selling at the highest, even if neither is the fair value.
  - To convert a YTM quote into a price, discount all cash flows at that YTM.
- **Value additivity vs dominance**:
  - Same payoff, different price for the package versus the sum of the parts → additivity.
  - Different implied riskless returns (e.g., 5% vs 10%) → dominance.
- **Node relationships**:
  - Adjacent nodes: × e^{2σ}.
  - Top vs bottom at Time t: × e^{2tσ}. Example: Time 4 with σ = 10% gives e^{0.8}.
  - The middle node at Time 2 ≈ the implied forward f₂,₁.
  - You cannot derive a Time-3 node from a Time-2 node. Only nodes at the same date are linked by σ.
- **Calibration purpose**: it makes the tree arbitrage-free so it can price bonds with **embedded options**. It does *not* identify mispriced benchmarks and does *not* enable strip/reconstitution profits.
- **Higher σ spreads the rates out.** It changes option-free values not at all, once the tree is recalibrated. So "a bond value from a high-σ tree differs from spot discounting" is **false** for option-free bonds.
- **Requirements for a tree**: an interest rate model, a σ assumption **and** the benchmark curve. "Only the benchmark rates and σ" is incomplete.
- **Path counting**: a 3-year annual tree has 4 paths (2²) to maturity. Pascal's triangle 1-2-1 gives the path counts to each Time-2 node.
- **Monte Carlo statements**: more paths → more statistical accuracy (true). Closer to the true fundamental value (false).
- **Model identification**:
  - Fits today's curve → Ho–Lee or KWF.
  - Mean reversion → CIR or Vasicek.
  - Volatility rising with the rate level → CIR.
  - Log of the short rate → KWF.
  - Constant volatility and negative rates possible → Vasicek or Ho–Lee.
  - Vasicek and CIR are one-factor models of the **short** rate.
- **Parameter count**: equilibrium models have **fewer** parameters. Arbitrage-free models have time-varying parameters, which is why they fit the curve more precisely.

## Key Takeaways
1. Arbitrage-free value = the sum of the cash flows discounted at their own spot rates. Violations are exploited through value additivity or dominance (stripping and reconstitution).
2. A binomial lognormal tree needs a rate model, σ and the benchmark curve. Nodes at the same date are spaced by e^{2σ}, and rates stay positive.
3. Calibrate one date at a time so that each par benchmark prices at 100. The tree then reproduces spot-curve values for every option-free bond.
4. Backward induction: `V = [C + ½(V_H + V_L)]/(1 + i)`. Pathwise valuation (the average of path PVs) gives the same answer for path-independent cash flows.
5. Use drift-adjusted Monte Carlo for path-dependent securities (MBS). More paths improve precision, not model truth.
6. Equilibrium models (CIR: √r volatility, no negative rates; Vasicek: constant volatility) mean-revert but do not fit today's curve. Arbitrage-free models (Ho–Lee: normal; KWF: lognormal) fit it through a time-dependent drift.
7. σ matters only for optionality. Use it deliberately when you move to the valuation of callable and putable bonds in ch09.

## Connects To
- **ch07**: spot, forward and par rates and bootstrapping, the inputs to calibration.
- **ch09**: the calibrated tree values callable, putable and floater-option bonds, and gives OAS, effective duration and convexity.
- **ch04**: MBS and ABS prepayment and path dependence, the reason Monte Carlo is needed.
- **ch10**: credit analysis models reuse the tree with default probabilities (CVA on a binomial lattice).
- **`tuckman-fixed-income` ch07**: the science of term structure models (risk-neutral trees). **ch08**: short-rate evolution and curve shape. **ch09–ch10**: the art of term structure models, drift (Vasicek, Ho–Lee) and volatility (CIR, lognormal). **ch11**: Gauss+ and LMM.
- **`hull-derivatives` ch31**: equilibrium short-rate models (Vasicek, CIR). **ch32**: no-arbitrage short-rate models (Ho–Lee, Hull–White, BDT, trinomial trees). **ch21**: basic numerical procedures (trees, Monte Carlo).
- **`ilmanen-yield-curve` ch05**: convexity bias, meaning how rate volatility pulls long yields down through Jensen's inequality. It is the same effect that shows up in the tree as volatility-dependent node spacing.
