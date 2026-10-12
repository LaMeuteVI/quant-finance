# Chapter 10: The Art of Term Structure Models: Volatility and Distribution
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 10 (Part Three: Term Structure Models), including the closed-form spot-rate appendix

## Core Idea
Chapter 9 fixed the drift; this chapter fixes the **volatility and the shape of the distribution**. A time-dependent volatility σ(t) lets the model fit option prices at many expiries. Making volatility depend on the rate level (CIR, lognormal) rules out negative rates and changes out-of-the-money option values, even when mean and standard deviation are identical. Black-Karasinski combines lognormality, mean reversion and time-dependent parameters, at the price of a variable time step needed to keep the tree recombining. Choose the specification for the job: quoting options, valuing/hedging, or relative value.

## Frameworks Introduced
- **Model 3 (time-dependent volatility)**: `dr = λ(t)dt + σe^(−αt)dw`; general form `dr = λ(t)dt + σ(t)dw` (eq. 10.1)
  - When to use: to match the prices of caplets (or similar options) expiring on many dates, e.g. to interpolate unobservable option prices from observable ones.
  - How: pick σ(t) so that the terminal distribution of the short rate at each expiry has the implied standard deviation; λ(t) fits the curve (as in Ho-Lee).
  - Failure mode: no mean reversion means a **parallel-shift** model with a **flat** term structure of volatility (flat at a level that changes over time). It relies on the market "knowing" distant future short-rate volatility.
  - Equivalence: with σ = 126bp, α = .025 (Vasicek's k) Model 3 has the same terminal standard deviations as Vasicek, and identical terminal distributions if the drift matches Vasicek's average path. Same distributions, very different factor shape and volatility term structure.
- **Level-dependent volatility family** (basis-point vol as a function of rate r):
  - Constant (normal, Ch 9): `dr = … + σdw`, bp vol = σ.
  - **Cox-Ingersoll-Ross (CIR)**: `dr = k(θ − r)dt + σ√r dw` (10.3), bp vol = σ√r.
  - **Courtadon**: `dr = k(θ − r)dt + σr dw` (10.4), bp vol = σr.
  - **Model 4** (simplest lognormal): `dr = a r dt + σr dw` (10.5), σ is **yield volatility** (a % of the rate).
  - When to use: high-inflation/high-rate regimes are unstable (vol rises with level) and vol is squeezed near zero rates; also when option strikes are far from the forward.
  - Non-negativity: bp vol = 0 at r = 0 plus positive drift at r = 0 keeps the rate from going negative.
  - Trade-off: a trader who believes constant vol fits best, that negative rates barely affect the securities at hand, and that computational simplicity is valuable, may rationally keep a normal model.
- **Original Salomon Brothers model (lognormal Ho-Lee)**: `dr = a′(t) r dt + σr dw`; by Ito `d ln r = (a′(t) − ½σ²)dt + σdw`, redefined as `d ln r = a(t)dt + σdw` (10.12)
  - When to use: fit the initial curve with a rate that cannot go negative and has constant yield vol.
  - How (tree): build the Ho-Lee tree on ln r, then exponentiate every node. Perturbations become multiplicative: `r₀e^(a₁Δt ± σ√Δt)`. Choose a₁, a₂, … one date at a time so the zeros reprice (same calibration loop as ch07 and ch09, now nonlinear in a).
  - Why it works: `eˣ ≈ 1 + x`, so the up-state is about `r₀(1+σ)`, a fixed % move (eq. 10.13).
- **Black-Karasinski (BK)**: `d ln r = k(t)[ln θ(t) − ln r]dt + σ(t)dw` (10.15); equivalently `dr = k(t)[ln θ̃(t) − ln r]r dt + σ(t) r dw` form (10.14)
  - When to use: the flexible workhorse: lognormal, mean reverting, and with time-dependent k, σ, θ. "Firmly in the arbitrage-free class": you can switch off as much time-dependence as you want.
  - Reading: ln r is a time-dependent Vasicek process.
  - **Recombination problem**: with a fixed step Δt the tree recombines only if `k(2) = [σ(1) − σ(2)]/[σ(1)Δt]` (10.20). This ties mean reversion to the vol function, but they do different jobs: **mean reversion controls the term structure of volatility, time-dependent volatility controls the future volatility of the short rate (option prices at different expiries)**.
  - Fix: let the time step vary. The tree recombines if `k(2) = (1/Δt₂)[1 − σ(2)√Δt₂ / (σ(1)√Δt₁)]` (10.23). Set Δt₁ freely and solve for Δt₂ (and so on forward), so k(t) and σ(t) can be chosen independently.
- **Choosing the distribution (decision rule)**:

| Purpose | Prefer |
|---|---|
| Quote unobservable option prices by interpolation across expiries | time-dependent σ(t) (Model 3 style) |
| Value and hedge securities incl. options | mean reversion (declining factor shape and vol term structure match PCA, ch06) |
| Avoid negative rates / OTM option skew matters | CIR or lognormal (BK) |
| Speed, near-the-money options, stable regime | normal models with closed forms |

## Key Concepts
- **Time-dependent (deterministic) volatility**: σ(t) is a known function of time, not of the rate. Popular with market makers in rate options.
- **Term structure of volatility**: volatility of rates by term. Model 3 is flat at every date, Vasicek declines, markets are humped (ch11 Gauss+).
- **Basis-point (normal) volatility**: annualized standard deviation of dr in rate units (e.g. 100bp). Constant in Ch 9 models.
- **Yield (proportional, lognormal) volatility**: bp vol as a percentage of the rate: bp vol = σ_y × r.
- **CIR square-root volatility**: bp vol = σ√r. σ is constant, bp vol is not. Unit of σ is √(rate)-related, so it is not comparable with yield vol.
- **Lognormal rate**: ln r is normal, so r > 0 and has a right-skewed distribution. Volatility is a percent of the rate.
- **Terminal distribution**: the distribution of the short rate at a future horizon. It determines prices of options expiring then. Three models with equal mean and standard deviation (5%, 2.32% at 10 years) still price OTM options differently.
- **Ito correction (−½σ²)**: the drift adjustment when moving from dr/r to d ln r.
- **Time-homogeneous**: parameters depend on time to maturity, not calendar time.
- **Variable time step**: choosing Δt by node date so a BK tree recombines.
- **Spot rate closed form**: model-implied continuously compounded r(T), obtained in closed form for Models 1–3, Vasicek and (as a bond price) CIR.
- **Convexity term in spot rates**: the negative `σ²`-dependent term in r(T), which grows fast with T.

## Formulas & Reference Tables
Notation: r(T) = continuously compounded T-year spot rate; r₀ the short rate; P(T) the zero price.

- Model 3 terminal std dev (same as Vasicek with k = α): `σ√[(1 − e^(−2αT))/(2α)]`.
- Volatility calibration constants: `σ_CIR = 1%/√8% = .0354`; `σ_y = 1%/8% = 12.5%` (both give 100bp at 8%, eqs. 10.6–10.8).
- Lognormal tree date 1: `r₀e^(a₁Δt ± σ√Δt)`; date 2 recombined nodes `r₀e^((a₁+a₂)Δt + σ√Δt·{2, 0, −2})`.
- Spot-rate closed forms (appendix, eqs. 10.24–10.31):

| Model | r(T) |
|---|---|
| Model 1 | `r₀ − σ²T²/6` |
| Model 2 | `r₀ + λT/2 − σ²T²/6` |
| Vasicek | `θ + [(1−e^(−kT))/(kT)](r₀ − θ) − (σ²/2k²)[1 + (1−e^(−2kT))/(2kT) − 2(1−e^(−kT))/(kT)]` |
| Model 3 (λ(t) = λ) | `r₀ + λT/2 − σ²[2α²T² − 2αT + 1 − e^(−2αT)]/(8α³T)` |

- **CIR zero price**: `P(T) = A(T)e^(−B(T)r₀)`, with
  - `h = √(k² + 2σ²)`
  - `A(T) = [2h·e^((k+h)T/2) / (2h + (k+h)(e^(hT) − 1))]^(2kθ/σ²)`
  - `B(T) = 2(e^(hT) − 1) / (2h + (k+h)(e^(hT) − 1))`
  - spot rate `r(T) = −ln P(T)/T`. Note: CIR needs numerical care with k, θ, σ²: `2kθ ≥ σ²` (Feller) keeps r > 0 strictly, consistent with the book's "positive drift at zero" condition.
- BK recombination: `k(2) = [σ(1) − σ(2)]/[σ(1)Δt]` (fixed step); `k(2) = (1/Δt₂)[1 − σ(2)√Δt₂/(σ(1)√Δt₁)]` (variable step).

## Mental Models
- **Drift fits the curve, volatility fits the options.** λ(t) or a(t) calibrate to bonds and swaps; σ(t) calibrates to caps, swaptions. Do not ask a parameter to do both jobs.
- **Mean reversion and time-dependent vol are substitutes in the terminal distribution, not in the dynamics.** Identical terminal standard deviations can hide a parallel-shift model versus a declining-factor model. Hedge ratios and curve-shape risk differ.
- **Match the first two moments and you still do not match the option.** Mean and s.d. equal, tails differ: normal has a fat left tail into negative rates, lognormal a long right tail, CIR in between. Price far OTM options with the distribution you believe.
- **Lognormal = multiplicative tree; normal = additive tree.** Up-and-down moves compound as `e^(±σ√Δt)`, so positive rates come for free.
- **If a model cannot be calibrated independently in k and σ, change the time grid, not the model.** BK's variable Δt is the trick.

## Worked Example
**A. Volatility units (verified).** Want 100bp vol at r = 8%: constant σ = 1%; CIR `σ = .01/√.08 = .0354`; proportional `σ_y = .01/.08 = 12.5%`. At r = 4% the bp vols become 100bp, 70.7bp (`.0354√.04`) and 50bp respectively. At 16%: 100, 141.4, 200bp.

**B. Model 3 versus Vasicek (σ = 126bp, α = k = .025).**
- Terminal standard deviation: 124.4bp at 1y, 353.5bp at 10y, 496.7bp at 30y (rises quickly, then flattens, like Vasicek).
- Convexity term in the spot rate with λ = 0 (closed form 10.27, cross-checked by numerical integration of `−(1/2T)∫σ²e^(−2αu)(T−u)²du`): −1.0bp at 2y, −23.5bp at 10y, −170.1bp at 30y. Vasicek closed form 10.26 at k = .025, θ = 15.339%, r₀ = 5.121%, σ = 126bp gives spot rates 5.245% (1y), 6.078% (10y), 6.742% (30y), also matching direct integration.

**C. Small lognormal (Salomon) tree, calibrated (verified in python).**
- Inputs: Δt = .5, σ = 15% yield vol, r₀ = 5%, semiannual spots 5.00%, 5.15%, 5.25% (zeros .975610, .950423, .925210), probabilities ½.
- Step 1: solve a₁ so the 1y zero reprices: **a₁ = .1059**. Date-1 rates: 5.862% (up), 4.741% (down).
- Step 2: solve a₂ for the 1.5y zero: **a₂ = .0458**. Date-2 rates: 6.669% / 5.394% / 4.363%.
- Check: model 1y zero .950423 and 1.5y zero .925210 match the market.
- Caplet on the 6-month rate struck 5.3% (rate set date 1, paid date 2, per $1, payoff `(r−K)⁺Δt`): discounted at the node, present value **.001331** per $1 (13.3bp of notional). The same-strike caplet set at date 2: .001787. Every node is positive, unlike a normal tree with the same drift at large σ.
- Interpretation: drift constants a_i are nuisance parameters absorbing the curve, the risk premium and convexity. They are not forecasts.

**D. BK recombination with a variable step.** σ(1) = 20%, σ(2) = 18%, Δt₁ = .5, desired k(2) = .10. Equation (10.23) requires **Δt₂ = .5511**. Check: with ln θ(2) = ln 6%, up-down and down-up rates both equal 5.0505%. A fixed step would have forced `k(2) = (.20 − .18)/(.20×.5) = .20`.

## Anti-patterns
- **Reading the same terminal standard deviation as the same model**: Model 3 and Vasicek have equal terminal s.d. but different factor structure and volatility term structure.
- **Using a deterministic σ(t) as a forecast of future volatility**: it is an interpolation device. The argument that the market forecasts distant short-rate volatility is weak; if used, let σ(t) vary near-term and settle at a constant.
- **Comparing σ across families**: σ_CIR = .0354, σ_y = 12.5% and σ_bp = 1% are the same economic volatility at 8%, not different.
- **Assuming lognormal or CIR is always better**: if negative-rate probability is negligible, constant-vol models are simpler and may fit current-regime vol better.
- **Forcing k(2) = (σ₁−σ₂)/(σ₁Δt)** in a BK tree to keep it recombining. It ties mean reversion to the vol schedule.
- **Calibrating a parallel-shift model to caplets and then hedging a curve position with it**: parallel shifts and a flat vol term structure misprice spread risk (PCA evidence, ch06).
- **Forgetting the Ito term**: `d ln r` drift is `a′ − ½σ²`, not `a′`.

## Practitioner Notes
- Market makers in caps and floors like deterministic σ(t), because each caplet expiry can be matched by one volatility value. Relative-value and hedging desks prefer mean reversion and more factors.
- The standard compromise: BK with time-dependent volatility for options, constant mean reversion chosen to fit the volatility term structure (ch09 "k controls the vol slope").
- Tuckman's caution: choose by purpose and the size of the error that matters. Negative rates (a normal model) rarely matter for near-ATM options in normal regimes, and matter a lot in low-rate regimes or for deep OTM options.
- Yield volatility (percent of rate) is the quoting convention for caplets in Black's lognormal framework (ch18), so lognormal short-rate models line up naturally with quoted cap vols.
- Numbers to remember: 10y terminal distributions with mean 5%, s.d. 2.32% correspond to a lognormal σ of about 44%. The lognormal has zero probability below 0 but a fat right tail.

## Key Takeaways
1. A time-dependent volatility function calibrates a model to options at many expiries, but without mean reversion it remains a parallel-shift model with a flat volatility term structure.
2. Matching mean and standard deviation of the terminal distribution does not match option prices: the shape (normal, CIR, lognormal) matters away from the money.
3. CIR bp vol is σ√r, lognormal is σr: both vanish at zero rates, so with positive drift they cannot go negative.
4. Lognormal tree = Ho-Lee tree on ln r, exponentiated. Calibrate the drift constants one date at a time.
5. Black-Karasinski is ln r as a time-dependent Vasicek. Keep it recombining by varying the step, not by tying k to σ.
6. Mean reversion controls the term structure of volatility, σ(t) controls future short-rate volatility and the option expiry structure.
7. Use the closed-form spot-rate formulas (Models 1–3, Vasicek, CIR) for intuition and quick calibrations: the convexity term grows with T² (Model 1: −σ²T²/6).
8. Pick the model for the purpose: quoting, hedging, or relative value.

## Connects To
- **ch07**: the tree-calibration machinery (risk-neutral probabilities, backward induction) used here for lognormal and BK trees.
- **ch08**: rate drift, convexity and risk premium that the a(t), λ(t) constants absorb.
- **ch09**: drift specifications (Ho-Lee, Vasicek) that this chapter complements with volatility and distribution choices.
- **ch11**: Gauss+ fixes the humped volatility term structure one-factor models cannot produce, and LMM takes forward rates as factors.
- **ch06**: PCA evidence (declining shifts, humped volatility) behind the preference for mean reversion.
- **ch18**: caplet pricing with Black/normal models, skew, and the cap/floor quoting that σ(t) is calibrated to.
- **ch15**: convexity corrections to futures rates, which use calibrated volatility.
- **`hull-derivatives` ch31 / ch32**: CIR (ch31); Black-Karasinski and Hull-White (ch32) in Hull's notation.
- **`cfa-fixed-income` ch08**: arbitrage-free trees with interest rate volatility.
