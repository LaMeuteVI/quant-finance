# Chapter 9: The Art of Term Structure Models: Drift
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 9 (Part Three: Term Structure Models)

## Core Idea
A short-rate model is a set of building blocks: a distribution (normal), a drift specification (none, constant, time-dependent, mean-reverting) and a volatility specification (ch10). The drift choice fixes what the model can do to the curve: constant and time-dependent drifts only shift levels and fit rates, whereas **mean reversion** changes the factor shape (no longer a parallel shift), pulls down long-term volatility and shrinks long-maturity convexity. Whether to fit today's curve exactly (arbitrage-free, Ho-Lee) or not (equilibrium, Vasicek) depends on the job: quoting and hedging derivatives versus finding relative value.

## Frameworks Introduced
- **Model 1 (normal, no drift)**: `dr = σ dw`
  - Every rate shifts in parallel, volatility term structure is flat, curve slopes down only through convexity.
  - When to use: teaching, benchmark for the convexity effect. Not fit for real curves (cannot match even a simple shape).
- **Model 2 (constant drift = risk premium)**: `dr = λ dt + σ dw`
  - Adds drift; two parameters (r₀, λ) can match e.g. the 2y and 10y par rate. Same vol structure, convexity and parallel shifts as Model 1.
- **Ho-Lee model (time-dependent drift)**: `dr = λₜ dt + σ dw`
  - When to use: fit the initial curve exactly for interpolating swap rates or pricing derivatives given a fair curve.
  - How (calibration): set r₀ to the shortest rate; choose λ₁ so the model reproduces the next spot rate; then λ₂ for the next, and so on along the tree. Equivalent to adjusting probabilities (ch07) if steps are small.
  - Failure mode: still a parallel-shift model with flat volatility, and a jagged fitted drift suggests supply/demand or liquidity noise is being pushed into "expectations".
- **Vasicek model (mean reversion)**: `dr = k(θ − r) dt + σ dw`, with `θ = r∞ + λ/k`
  - When to use: equilibrium relative value; modelling declining long-end volatility; economic interpretation of mean reversion as the length of news.
  - How: choose k from the desired volatility term structure (ch09 fits 10y and 30y implied vols), r₀ and θ to match a couple of par rates, σ for the volatility level.
  - Failure mode: not flexible enough for the observed range of curves, and the volatility term structure declines everywhere (no hump; a second factor is needed, ch11).
- **Shadow-rate trick (Black, "Interest Rates as Options", 1995)**: build the tree with any distribution, then floor observed rates at zero. The shadow rate may be negative while the observed rate stays at zero until the shadow rate recovers. Localizes the change around zero rather than reshaping the whole distribution.
- **Recombining representation of a mean-reverting tree**:
  1. Fix the center node of each date at the drift-only expectation.
  2. From each node compute the mean and standard deviation of the continuous process.
  3. Solve for the up/down rate and probability that match both moments.
  - The naive tree (±σ√dt around each drifted value) does not recombine because drift depends on the level.
- **Choosing arbitrage-free vs equilibrium (Tuckman's decision test)**:

| Purpose | Prefer | Why |
|---|---|---|
| Quote off-the-run swaps, interpolate | Arbitrage-free | Uses economics (expectations, premium, convexity) rather than cubic splines |
| Price/hedge derivatives on a fairly priced curve | Arbitrage-free | Matches underlyings by construction |
| Find rich/cheap bonds or swaps | Equilibrium (or partial fit) | Fitting everything exactly says everything is fair relative to everything else |
| Practical compromise | Hybrid | Fit only 2y/5y/10y/30y, or a short deterministic drift then constant drift |

## Key Concepts
- **Gaussian (normal) model**: terminal distribution of r is normal. Simple and tractable, but it allows negative rates.
- **Basis-point volatility σ**: annual standard deviation of rate changes in bp. Over T years, the standard deviation of r is `σ√T` with no mean reversion.
- **dw**: normal shock with mean 0 and standard deviation √dt.
- **Drift**: `E[dr]`, in the risk-neutral process a combination of expectations and premium (ch08).
- **Time-dependent drift**: the drift λₜ varies by date, giving free parameters to fit the curve.
- **Mean reversion speed k / long-run level θ**: the drift pulls r toward θ at a rate proportional to the gap.
- **Half-life**: `τ = ln 2 / k`, the time to cover half of the distance to θ.
- **Shadow rate vs observed rate**: shadow rate is the unconstrained model rate. Observed = max(shadow, 0).
- **Long-lived vs short-lived news**: mean reversion measures how long a shock lasts. Low k means long-lived news.
- **Term structure of volatility**: volatility of par/spot rates by term. Flat in Models 1–2 and Ho-Lee, declining in Vasicek, humped in the market.
- **Factor shape (shift)**: change in each spot rate for a unit move in the short rate. Flat under no mean reversion, declining under Vasicek.
- **Equilibrium vs arbitrage-free**: see ch08. Fitting drives whether the model treats market prices as fair.
- **Convexity effect (par rate)**: par yield with volatility minus par yield in the same model at zero volatility.

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| Model 1 tree step | `r ± σ√dt`, probability ½ each. `E[dr] = 0`, `V[dr] = σ²dt` |
| Model 2 tree step | `r + λdt ± σ√dt` |
| Ho-Lee | `dr = λₜ dt + σ dw`; date-i rates `r₀ + (λ₁+…+λᵢ)Δt + (2j − i)σ√Δt` (j = number of up moves) |
| Vasicek | `dr = k(θ − r)dt + σ dw` |
| θ decomposition | `θ = r∞ + λ/k` (only θ is observable in prices) |
| Vasicek mean | `E[r_T] = r₀e^(−kT) + θ(1 − e^(−kT))` |
| Distance to goal | `θ − E[r_T] = (θ − r₀)e^(−kT)` |
| Half-life | `τ = ln(2)/k` |
| Vasicek std dev | `√[(σ²/2k)(1 − e^(−2kT))]` (→ σ√T as k→0) |
| Sharpe ratio (Model 2 as premium) | `λ/σ` |
| Matching two moments at a node | choose up value r_u and probability p with `p·r_u + (1−p)·r_d = m`, `p(r_u−m)² + (1−p)(r_d−m)² = s²` |

| Par-rate convexity (bp) | 2y | 5y | 10y | 30y |
|---|---|---|---|---|
| Model 1, σ = 113bp (Table 9.1) | −0.8 | −5.1 | −18.8 | −135.3 |
| Vasicek, k = .025, σ = 126bp (Table 9.2) | −1.0 | −5.8 | −19.1 | −74.7 |

Data point: with a 10bp rise in the factor, the Vasicek 30y spot rate rises only about 7bp (vs 10bp in Model 1).

## Mental Models
- **Drift shifts levels, mean reversion bends everything else.** Constants and deterministic drift change curve fit but not the factor structure, vol term structure or convexity. Only mean reversion does.
- **Mean reversion = length of news.** Short rates follow current conditions, long rates follow long-run conditions (θ), so a shock to the short rate moves short rates more than long rates. Low k = long-lived news; high k = short-lived.
- **Fitting is only as good as the model**: a bad model calibrated to the curve is still a bad model (a parallel-shift model with a fitted drift is still parallel), and fitted-drift noise reflects flows and liquidity, not rates expectations.
- **Negative-rate risk grows with horizon and option asymmetry**: coupon bonds care about average path, so tolerate Gaussian models. Options struck near zero rates do not.
- **Mean reversion is a bet that no catastrophe happens**: rates mean-revert until they don't (hyperinflation ends the series).

## Worked Example
**A. Small risk-neutral Ho-Lee tree, calibrated to a curve (recomputed in python).**
- Inputs: semiannual steps (Δt = 0.5), σ = 100bp/yr so `σ√Δt = 70.71bp`, r₀ = 5%, spot rates (semiannual compounding) 5.00% / 5.15% / 5.25% at 0.5y / 1y / 1.5y. Zero prices 0.975610, 0.950423, 0.925210.
- Step 1: solve for λ₁ so the two-step zero equals 0.950423. Result **λ₁ = 60.51bp/yr**. Date-1 rates: `5% + 0.6051% × 0.5 ± 0.7071%` = **6.0097% / 4.5954%**.
- Step 2: solve for λ₂ so the three-step zero equals 0.925210: **λ₂ = 30.98bp/yr**. Date-2 rates: `5% + (60.51 + 30.98)bp × 0.5 + {−1.414%, 0, +1.414%}` = **6.8717% / 5.4574% / 4.0432%**.
- Check: the tree reprices both zeros exactly. Note that the fitted drift shrinks from 60.5bp to 31.0bp: it absorbs the convexity effect of the tree (with zero drift and the same volatility the tree's 1y and 1.5y spots would be 4.999% and 4.997%, versus 5.15%/5.25% in the market).
- Use: a call on the 6-month zero at date 1 with strike 0.9756 has payoffs 0.001939 (rate down), 0 (rate up), so its value is `½ × 0.001939/1.025 = 0.000946` per $1 face (about $0.95 per $1,000). The calibrated tree prices any such claim by backward induction.

**B. Vasicek numbers (source parameters: k = .025, σ = 126bp, r₀ = 5.121%, θ = 15.339%).**
- Monthly drift `.025 × (15.339% − 5.121%)/12 = 2.13bp`; monthly standard deviation `126bp/√12 = 36.4bp`.
- Mean after 10y: `15.339% − 10.218% × e^(−.25) = 7.381%`. Half-life `ln2/.025 = 27.7y`.
- Standard deviation after 10y: `1.26% × √[(1 − e^(−.5))/.05] = 353bp`, against `1.26% × √10 = 398bp` without mean reversion.
- Recombining node solve: from the up node 5.5060%, mean 5.5265% and standard deviation 36.37bp with the lower child at the center value 5.1635% give **r_uu = 5.8910%, p = 0.4989** (book: 5.8909%, 0.4990). From the down node 4.7786%: **r_dd = 4.4361%, q = 0.5011**.

**C. Model 1 and 2 checks.** Model 1 (6.18%, σ = 113bp): one-month standard deviation 32.6bp, tree nodes 6.506%/5.854%. Ten-year standard deviation 357.3bp, so rates go negative at 1.73 σ. Model 2 (r₀ = 5.138%, λ = 22.9bp, σ = 110bp): ten-year mean 7.428%, standard deviation 347.9bp. Implied Sharpe ratio `.229/1.10 = 0.21`, too high to read as a pure premium.

## Anti-patterns
- **Fitting a jagged time-dependent drift to every bar**: it assumes expectations or premium differ from the 15th to the 16th year; more likely you are absorbing liquidity, taxes or supply-demand noise (e.g. a seven-year bulge from a big liquidation).
- **Using an arbitrage-free model to find cheap bonds**: it takes all fitted securities as fair, so it cannot find relative value among them.
- **Believing calibration rescues the model**: a parallel-shift model fitted to the curve still fails when the application needs non-parallel moves.
- **Gaussian model for options struck near zero**: too much probability of negative rates overprices e.g. a 10y call on a bond at a 0% yield.
- **Mixing up k and volatility**: with mean reversion, "σ per year" no longer means standard deviation grows like √T.
- **Reading θ as a forecast**: θ = r∞ + λ/k mixes expectation and premium. Many (r∞, λ) pairs price identically.
- **Assuming the naive mean-reverting tree recombines**: the drift depends on the level so an up-down and a down-up path end at different rates.
- **Trusting the fitted parameters of a rigid model**: Model 2 overshot the 30y par rate by about 25bp when fitted to 2y and 10y.

## Practitioner Notes
- Swap desks use arbitrage-free models to interpolate (a 3y4m swap between liquid 3y and 4y, or 2y and 5y). It beats linear or spline interpolation only when the volatility (convexity) assumption is decent.
- Model curves fitted to just 2y and 10y par rates (Models 2 and Vasicek) still miss shapes: the number of free parameters must match the shapes you need.
- Tuckman's blend: a short deterministic drift for a few years (reflecting forecasts) then a constant drift, or fit only the liquid 2/5/10/30y points.
- Volatility parameters are chosen for the desk's use: Model 2 uses the average of 2y and 10y implied volatility, Vasicek fits 10y and 30y volatilities via k and σ. Model 1's 113bp equals the 10y implied volatility on the data date (16 Feb 2001).
- Low-rate environments (the 2010s) make negative-rate handling urgent: use shadow rates or lognormal-style volatility (ch10), knowing that lognormal choices change volatility behaviour.
- Half-life is the easier quoting convention for k. A 28y half-life (k = .025) means almost no mean reversion inside 10y.

## Key Takeaways
1. Model 1 (`dr = σdw`) is a parallel-shift, flat-volatility, convexity-only curve. It cannot fit realistic shapes.
2. A constant drift (Model 2) adds level flexibility only. A time-dependent drift (Ho-Lee) fits the whole curve. Neither alters volatility or factor structure.
3. Vasicek's `k(θ − r)` makes long rates less sensitive to the short rate (factor slope), declines volatility with term and cuts long convexity (30y: −135bp to −75bp).
4. Choose arbitrage-free for pricing derivatives and interpolation, equilibrium for relative-value; blend by fitting only liquid points.
5. Treat any fitted drift that jumps year to year as contamination by non-rate effects.
6. Handle negative rates with shadow rates (floor observed at 0) or by changing the distribution (ch10).
7. Build recombining mean-reverting trees by matching the mean and standard deviation node by node.
8. Half-life `ln2/k` and terminal standard deviation `σ√((1 − e^(−2kT))/2k)` are the two quick checks on k.

## Connects To
- **ch07**: the calibration of a tree to today's curve. Ho-Lee here adjusts rates where ch07 adjusts probabilities.
- **ch08**: drift = expectations + premium, and convexity effect on rates.
- **ch10**: volatility specifications (lognormal, Black-Karasinski, CIR, Hull-White) and closed-form spot rates.
- **ch11**: two-factor Gauss+ for humped volatility and non-parallel factors.
- **ch04–ch05**: duration/convexity and multi-factor hedges (why one-factor parallel shifts limit hedges).
- **ch21**: curve construction as the alternative to model-based interpolation.
- **`hull-derivatives` ch31 / ch32**: Vasicek (ch31); Ho-Lee and Hull-White (ch32) in Hull's notation and closed forms.
- **`cfa-fixed-income` ch08**: arbitrage-free tree calibration.
