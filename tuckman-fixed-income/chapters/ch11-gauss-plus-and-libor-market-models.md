# Chapter 11: The Gauss+ and LIBOR Market Models
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 11 (Part Three: Term Structure Models), incl. Appendices A–E

## Core Idea
Production models are richer than the one-factor trees of ch09–ch10. **Gauss+** is a three-state-variable, two-risk-source Gaussian model with a cascade of mean-reverting factors. It reproduces the empirical PCs and the **humped term structure of volatility**, so it is the relative-value and hedging workhorse. The **LIBOR Market Model (LMM)** takes observable forward rates as factors. It matches today's curve automatically, is calibrated to caps and swaptions, and is used to price and hedge exotics, using **forward measures** instead of a short-rate drift.

## Frameworks Introduced
- **Gauss+ cascade form** (short, medium and long factors; eqs. 11.1–11.4):
  - `dr = −αr(r − m)dt`
  - `dm = −αm(m − l)dt + σm[ρ dw₁ + √(1−ρ²) dw₂]`
  - `dl = −αl(l − θ)dt + σl dw₁`, `E[dw₁dw₂] = 0`
  - Story: l = long-term trend (demographics, technology), slow mean reversion to θ; m = business/monetary cycle reverting to l (αm > αl); r = central-bank-controlled rate that tracks m with **zero own volatility**.
  - Why "Gauss+": three state variables (r, m, l) but only two sources of risk (dw₁, dw₂). The "+" is the factor r, which is not a source of risk.
  - Why it matters: zero volatility on r keeps short-term rate vol low, while m and l feed longer rates, so the vol term structure is low at the front, peaks in the middle, then decays (mean reversion). One-factor models cannot do this (Vasicek is monotone declining).
  - Risk premium: only the long factor carries one (inside θ). The horizons of investors are long enough that no premium accrues on central-bank moves, consistent with industry practice and Cochrane-Piazzesi.
- **Gauss+ reduced form** (for solving; eqs. 11.8–11.15):
  - `r = θ + x₁ + x₂ + x₃`
  - `dx₁ = −αr x₁dt + σ₁₁dw₁ + σ₁₂dw₂`
  - `dx₂ = −αm x₂dt + σ₂₁dw₁ − σ₁₂dw₂`
  - `dx₃ = −αl x₃dt − (σ₁₁ + σ₂₁)dw₁`
  - Mapping from cascade parameters (see Formulas).
  - Spot rate closed form: `r(T) = θ + x₁(1−e^(−αrT))/(αrT) + x₂(1−e^(−αmT))/(αmT) + x₃(1−e^(−αlT))/(αlT) + Υ(T)`, where Υ(T) is a convexity-type function of T and the reduced-form parameters only (not of the factors).
- **Gauss+ estimation and daily use (3 steps)**:
  1. **Parameters from PCs**: the model's two PCs, Λ₁(T) and Λ₂(T) (`∂r(T)/∂z₁`, `∂r(T)/∂z₂` with z₁, z₂ uncorrelated unit-variance normals), depend only on αr, αm, αl, σm, σl, ρ. Choose them to minimize squared distance to the first two empirical PCs of swap rates.
  2. **Initial factors daily**: x₁, x₂, x₃ fitted from market prices, e.g. match the 2y, 10y and 30y par rates exactly, or least-squares over the whole curve. Neither dominates: benchmark fit is exact where liquid, least squares gives better overall fit. Errors mostly under 20bp in the book's example.
  3. **θ**: set from views on long-term rate plus premium, or chosen to improve in-sample fit. Re-fitting θ daily is internally inconsistent (θ is a constant in the model) but common.
  - Output for trading: residuals of market vs model rates = rich/cheap indicators (Feb 2011: 5y cheap, 20y rich).
- **Gauss+ extensions**:
  - **Exact curve fit**: replace θ with θ(t): `r* = θ(t) + x₁ + x₂ + x₃`. Solve with initial θ = 0 model, then `θ(T) = f*(T) − f(T)` (market minus model continuously compounded forward rates; Appendix D).
  - **Time-dependent volatility η(t)**: multiply all σ's by η(t) (η = 1 is original). Fit η as a step function to ATM swaptions on a fixed underlying (e.g. 10y swap) at expiries 3m, 6m, 1y, …, 10y. Use it for exotics and futures convexity corrections, not for relative value in swaps.
  - **European swaptions in Gauss+**: no closed form. Approximate swap rate `(d(t) − d(t+T))/A(t,t+T)` as a linear function of the Gaussian factors, so it is approximately normal, then use a Black-Scholes-style formula (ch18).
- **LMM set-up** (factors = adjacent τ-year forward rates):
  - Fixed dates T₀, T₁ = T₀+τ, T₂, T₃; forwards `f_t(Tᵢ₋₁, Tᵢ)` with instantaneous volatility σᵢ(t) and correlation ρᵢ,ⱼ(t). Typical τ = .25.
  - Inputs are volatilities and correlations, not drifts. Initial factors are today's forwards, so the initial curve is matched by construction.
  - Key tool: **forward measure**. Under the T+τ measure `f_t(T, T+τ)` is a martingale (11.20), and `V_t/d_t(T+τ) = E_t^(T+τ)[V_s/d_s(T+τ)]` (11.21), so `V_t = d_t(T+τ)·E_t^(T+τ)[V_(T+τ)]` (11.22).
  - **Pricing recipe (terminal measure)**: (1) simulate all forwards from t on with drifts μᵢ(t) under the terminal T₃ measure, from a multivariate normal with given σ and ρ; (2) carry each payment forward to T₃ along the path; (3) average across paths and multiply by d₀(T₃).
  - Payment at T₂ contingent on f_{T₂}(T₂,T₃): value `d_t(T₃)·E^(T₃)[V_{T₂}(1 + τf_{T₂}(T₂,T₃))]` (11.23). A claim paying earlier needs the drifts of the earlier forwards, which are derived below.
- **LMM drift derivation (no-arbitrage drifts)**:
  - Idea: under T₃, the forward f(T₁,T₂) is a martingale only under the T₂ measure. A forward-rate agreement's fair rate is the same under every measure, which forces a covariance-driven drift under T₃.
  - Result (eq. 11.30): `μ₂(t) = −τρ₂,₃(t)σ₂(t)σ₃(t)/(1 + τf_t(T₂,T₃))`.
  - Generalized (11.39–11.41), for forward k under the Tᵢ measure: `i > k`: `μₖ = −Σ_{j=k+1..i} τρₖ,ⱼσₖσⱼ/(1+τf(Tⱼ₋₁,Tⱼ))`; `i = k`: 0; `i < k`: `μₖ = +Σ_{j=i+1..k} τρₖ,ⱼσₖσⱼ/(1+τf(Tⱼ₋₁,Tⱼ))`.
  - Intuition: under a longer (terminal) measure, forwards that end earlier drift **down** (negative covariance with later discounting), forwards that end after the measure date drift **up**.
- **LMM calibration**:
  - **Correlation: from history.** Term correlations drive swaption prices, instantaneous correlations are the model inputs, and the map between them is messy when vols vary in time, so calibrating to swaptions for both is too cumbersome. Specification (11.42–11.43), with Tᵢ > Tⱼ: `ρᵢ,ⱼ(t) = ρ∞ + (1−ρ∞)e^(−κ[Tⱼ−t](Tᵢ−Tⱼ))`, `κ[T−t] = a∞ + (a₀−a∞)e^(−β(T−t))`. Requires 1−ρ∞ > ρ∞ and a₀ > a∞ so that correlation falls with the gap between forwards and rises with the maturity of the earlier forward.
  - **Volatility: from caps/caplets, Eurodollar/Euribor options, or swaptions.** Specification (11.44), time homogeneous, deterministic, independent of the rate level: `σᵢ(t) = l∞ + (l₀ − l∞ + a(Tᵢ₋₁−t))e^(−b(Tᵢ₋₁−t))` (hump at term `1/b + (l∞−l₀)/a`). Caplet implied vol = root-mean-square of the instantaneous vol: `σ̄ᵢ² = [1/(Tᵢ₋₁−t)]∫σᵢ²(s)ds` (11.45).
  - **Swaption calibration**: swap rates are approximately fixed-weight linear combinations of forwards, hence approximately normal with computable volatility from σ and ρ. Compare with market swaption vols.
  - Exact fits: multiply σᵢ(t) by a constant per forward, at the cost of time homogeneity (often acceptable for near-dated forwards).
  - **Mid-curve options** reveal average vol of a forward to an earlier date than the forward's start, information caplets lack.
  - Relative value by-product: calibrate on caps, reprice swaptions, and the gap is cap-versus-swaption richness.

## Key Concepts
- **Cascade form**: intuitive parametrization (r reverts to m, m to l, l to θ).
- **Reduced form**: the same model in uncorrelated-shock coordinates `x₁..x₃` where solutions are simple. Equivalence proven with a linear transform `u = Ax + θ`.
- **State variables vs sources of risk**: Gauss+ has 3 and 2. Not every factor needs its own shock.
- **Humped volatility term structure**: low at the short end, peak at intermediate terms, decay at long terms. Observed in markets, produced by Gauss+ and the LMM vol function.
- **Half-life**: `ln 2/α`. USD fit: 1.0y (αr), 1.1y (αm), about 18y (αl).
- **Λ₁(T), Λ₂(T)**: model PCs: the change in the T-year spot rate per unit of z₁, z₂.
- **Forward measure (T+τ measure)**: pricing measure under which `f_t(T,T+τ)` is a martingale and claims are valued as discounted expected payoffs.
- **Terminal measure**: the forward measure for the last payment date, making all drifts of type i > k.
- **Instantaneous volatility/correlation**: local (infinitesimal-horizon) σ and ρ of forward rates. Distinct from term (expiry-horizon) volatility and correlation.
- **Time homogeneity**: volatility depends only on the forward's term Tᵢ₋₁−t.
- **Caplet volatility**: implied vol of a caplet, which is the average instantaneous vol to its expiry.
- **Cholesky decomposition**: `Σ = AAᵀ` with A lower triangular. Turns independent standard normals z into correlated draws `x = μ + Az`.
- **Mid-curve option**: an option on a forward starting after its expiry (mid-curve futures options).

## Formulas & Reference Tables
Cascade to reduced-form parameters (eqs. 11.13–11.15):
- `σ₁₁ = [αrαm/((αr−αm)(αr−αl))]σl − [αr/(αr−αm)]ρσm`
- `σ₂₁ = [αr/(αr−αm)]ρσm − [αrαm/((αr−αm)(αm−αl))]σl`
- `σ₁₂ = −[αr/(αr−αm)]σm√(1−ρ²)`
- Transform (Appendix A): `r = u₁, m = u₂, l = u₃`; `u = Ax + θ`, `A = [[1, 1, 1], [0, (αr−αm)/αr, (αr−αl)/αr], [0, 0, (αr−αl)(αm−αl)/(αrαm)]]` (rows; the PDF's matrix print is garbled, and this A is rederived and verified: `A·Σ = [[0,0],[ρσm, σm√(1−ρ²)],[σl,0]]`).
- Model PCs (Appendix C): `[Λ₁(T), Λ₂(T)] = b_ml S`, with `b = [(1−e^(−αrT))/(αrT), (1−e^(−αmT))/(αmT), (1−e^(−αlT))/(αlT)]`, `b_ml` = last two entries of `bA⁻¹`, `S = [[ρσm, σm√(1−ρ²)], [σl, 0]]`. They depend only on αr, αm, αl, σm, σl, ρ.
- Fit of the initial curve: `θ(T) = f*(T) − f(T)` (11.86).
- LMM pricing: `V_t = d_t(T+τ)E_t^(T+τ)[V_(T+τ)]`; martingale `f_t(T,T+τ) = E_t^(T+τ)[f_s(T,T+τ)]`.
- Drift under T₃ (simple model): `μ₂ = −τρ₂,₃σ₂σ₃/(1+τf(T₂,T₃))`; `μ₁ = −τρ₁,₂σ₁σ₂/(1+τf(T₁,T₂)) − τρ₁,₃σ₁σ₃/(1+τf(T₂,T₃))` (11.38).
- Multivariate normal draw of 2 forwards: `Δf₁ = μ₁Δt + σ₁√Δt z₂'`-style; for the book's pair with z₁, z₂ independent: `Δf(T₁,T₂) = σ₂√Δt z₂`, `Δf(T₂,T₃) = μ₃Δt + σ₃√Δt[z₁ρ₂,₃ + z₂√(1−ρ₂,₃²)]`. (The book labels draws inconsistently: it puts z₂ on the first forward and z₁ on the second with the correlation. Any Cholesky ordering works.)
- Cholesky, 2D: `A = [[σ₁, 0], [ρσ₂, σ₂√(1−ρ²)]]`.

USD and EUR Gauss+ estimates (Aug 2001 – Dec 2010, Table 11.1):

| Parameter | USD | EUR |
|---|---|---|
| αr (half-life) | .729 (1.0y) | .719 (1.0y) |
| αm | .629 (1.1y) | .619 (1.1y) |
| αl | .038 (about 18y) | .01 (about 67y) |
| σm | 2.58% | 1.78% |
| σl | 1.79% | 1.05% |
| ρ | .15 | −.05 |
| θ | 9.04% | 8.00% |

Time-dependent vol fit η(t) to 10y-swap ATM swaptions, 11 Feb 2011: implied vol (bp/day) and η: .25y 6.9/.87; .5y 7.0/.86; 1y 7.1/.82; 2y 7.1/.75; 3y 7.0/.68; 4y 6.9/.63; 5y 6.7/.61. Low η means the market implies lower future vol than the historical fit.

LMM USD calibrations (Table values): correlations ρ∞ = .25, a₀ = .610029, a∞ = .029683, β = 1.861247 (Feb 2002–Mar 2011). Model correlations (t = 0): 3m fwd vs 2y = .63; 2y vs 5y = .91; 2y vs 10y = .78; 5y vs 10y = .90; 10y vs 30y = .66. Volatility fit to caplets (6 Jul 2006): l∞ = .508%, l₀ = .602%, a = .00398, b = .29773, peak at term 3.12y (about 104bp). Market-minus-model caplet vols: 6m −1.4bp, 2y +2.1, 5y −4.4, 10y +1.2, 20y +5.1, 30y −7.9 (calibrated to caplets).

Model-choice map (from the Part Three intro, ch07): one-factor short rate for interpolation/callables, Gauss+ for relative value and cross-product risk, LMM for exotics calibrated to a large set of vanilla vols.

## Mental Models
- **A cascade of central-bank behavior.** Short rate follows the business cycle, the cycle follows the long-term trend. Shocks enter at m and l, never at r. That is what produces the hump.
- **Two shocks explain the curve.** Gauss+ has two sources of risk, matching the first two PCs (level/slope-like). Think of r(T) as a function of two uncorrelated normals z₁, z₂ and two loading curves Λ₁, Λ₂.
- **Fit statistics by purpose.** History (PCs) for dynamics and hedge ratios, today's curve for levels, swaption vols (η(t)) for exotics. Do not calibrate everything to everything.
- **LMM: model the observable, derive the drift.** Drift is a consequence of no-arbitrage and the chosen measure, not an input. Volatility and correlation are the inputs.
- **Pick the measure for the last payment.** Terminal measure means every payment is brought forward to T₃ and discounted once. Fewer drift computations if most claims depend on the longest forward.
- **Bond-and-swap vs option-market divergence is information.** Calibrate on caps and price swaptions to see the richness of one versus the other (caps = floating-rate borrowers' rate hedges, swaptions = MBS prepayment hedges).

## Worked Example
**A. Gauss+ reduced-form parameters from the USD cascade (verified).** αr = .729, αm = .629, αl = .038, σm = 2.58%, σl = 1.79%, ρ = .15.
- `σ₁₁ = 9.06%`, `σ₁₂ = −18.60%`, `σ₂₁ = −11.07%`, and `−(σ₁₁+σ₂₁) = +2.01%` (loading of x₃ on dw₁).
- Check: multiplying by A reproduces `ρσm = .387%`, `σm√(1−ρ²) = 2.551%` for m and `σl = 1.79%` for l, with zero for r, so volatility of r is zero in the cascade form.
- Half-lives: ln 2/.729 = 1.0y, ln 2/.629 = 1.1y, ln 2/.038 = 18.2y (the book prints 18.4y from unrounded α).

**B. Model PCs and humped volatility (verified via the Appendix C formula).** With the same parameters, `Λ = b_ml S` gives (bp per unit z₁, z₂):

| Term | Λ₁ | Λ₂ | Vol (bp/day, /√250) |
|---|---|---|---|
| 0.25y | 3.9 | 20.8 | 1.3 |
| 1y | 18.8 | 59.9 | 4.0 |
| 2y | 40.5 | 79.4 | 5.6 |
| 5y | 88.3 | 69.0 | 7.1 |
| 10y | 115.7 | 40.2 | 7.7 |
| 20y | 114.9 | 20.3 | 7.4 |
| 30y | 102.7 | 13.5 | 6.6 |

The term structure of volatility is low, peaks near 10y and then declines: a hump, unlike Vasicek's monotone decline.

**C. LMM exotic (book example, recomputed).** Time 0 = 6 Jul 2006. Payoff at T₂: geometric mean of the 3m forward to Dec 2006 (observed on 3 dates) minus the geometric mean of the 3m forward to Mar 2007. Pricing measure: T₂ measure, so `f(T₁,T₂)` has zero drift, and `f(T₂,T₃)` drift is (11.41) with i = 2, k = 3: `μ₃ = τσ₃²/(1+τf(T₂,T₃))`.
- Inputs: f(T₁,T₂) = 5.68%, f(T₂,T₃) = 5.65%, σ₃(0) = .8121% (`σ₃ = l∞ + (l₀−l∞ + a·x)e^(−bx)` at a term of .46y gives σ₂ = .7489%, reproduced), ρ₂,₃(0) = .9499.
- Drift: `μ₃(0) = .25(.008121)²/(1 + .25×.0565) = .163bp per year`, so ×.208y = **.034bp**. The book prints ".034" without units: it is bp.
- One path: forwards after the first step 5.507% and 5.365%, after the second 5.299% and 5.262%. Geometric means: `(5.680×5.507×5.299)^(1/3) = 5.493%`, `(5.650×5.365×5.262)^(1/3) = 5.423%`. Payoff = **.070%** (7bp). Average many paths, then multiply by d₀(T₂).
- Note: the book writes "May 21, 2007" once for the payment date; it is March 21, 2007 = T₂.

**D. LMM correlation and volatility functions (verified).**
- (11.42)–(11.43) with the USD parameters give `ρ(2y,5y) = .91`, `ρ(2y,10y) = .78`, `ρ(5y,10y) = .90`, `ρ(3m,2y) = .63`, matching Table 11.3.
- Peak term of (11.44): `1/b + (l∞−l₀)/a = 3.359 − .236 = 3.12y`.

## Anti-patterns
- **Treating θ as a daily fit parameter and still trusting the model's risk numbers**: θ is a constant in the model.
- **Fitting Gauss+ factors to only 2y/10y/30y and trusting the 5y and 20y**: the mismatch is the signal (cheap 5y, rich 20y) only if you trust the model. Check stability.
- **Reading α_m and α_r as sharply identified**: half-lives 1.0y vs 1.1y are hard to separate. Only αl (long half-life) is clearly distinct.
- **Calibrating LMM correlations to swaptions**: term correlations (not instantaneous ones) drive swaption prices and the mapping is complex. Use history.
- **Using a time-homogeneous deterministic vol function for derivatives that need skew or stochastic vol**: the (11.44) function is pedagogical. Production LMMs add skew and stochastic vol.
- **Pricing a cash flow at T₁ under the T₃ measure without the T₁ and T₂ drifts**: only the forward ending at the measure date is driftless.
- **Expecting Gauss+ to match swaption vols out of the box**: historical PCs fix dynamics, not implied volatilities. Add η(t).
- **Mixing up the simple LMM drift sign conventions**: forwards ending before the measure date have negative drift under a longer measure, after it positive.

## Practitioner Notes
- Tuckman's division of labor: Gauss+ for **relative value trading and hedging** and cross-product risk. For relative value in swaps, **precise volatility calibration is normally not worth the effort**. LMM for **exotics (e.g. Bermudans) and market making**, where calibrating to many vols matters.
- Gauss+ desk routine: estimate α, σ, ρ infrequently from PCs (exponentially weighted; the book used decay .5 per year), refit x₁–x₃ daily (benchmark par swaps are the most traded, so fit those), and watch the residual curve.
- The volatility limit of the book's swaption fit: near-dated implied vols of 6.7–7.1bp/day versus historical fit imply η of .6–.9, so the market priced future rate vol well below history in Feb 2011.
- LMM in practice: 30 annual or 120 quarterly forwards, Monte Carlo under the terminal or spot measure, Cholesky for correlated draws, variance reduction. Expect volatility-skew extensions.
- Cap vs swaption richness follows hedging flows: fear of rising rates makes caps rich, fear of falling rates (MBS convexity hedging) makes swaptions rich. In July 2006 (Fed done tightening) caps traded cheap to swaptions, and market caplet vols sat below the swaption-implied ones (for example 30y: −23.6bp).
- Mid-curve options are the source of information on forward volatility before the forward's start.

## Key Takeaways
1. Gauss+ = three state variables, two shocks, cascade r → m → l → θ with zero vol on r. It yields a humped volatility term structure and PCs that match the data.
2. Solve it in reduced form (closed-form spot rates), estimate α, σ, ρ from PCs, fit x₁–x₃ daily to benchmark par rates or by least squares, and read residuals as rich/cheap.
3. Time-dependent θ(t) fits the curve exactly (θ(T) = market forwards minus model forwards). A volatility multiplier η(t) fits swaption prices. Use only for exotics and convexity adjustments.
4. LMM uses observable forwards as factors, so today's curve is matched by construction. Inputs are volatilities and correlations, and drifts come from no-arbitrage.
5. Under the T+τ forward measure the forward f(T,T+τ) is driftless and claims are discounted expectations. In the terminal measure, earlier forwards get drift `−Στρσσ/(1+τf)`.
6. Calibrate LMM correlations from history and volatilities from caplets, futures options or swaptions. Use the gap between instruments as relative-value information.
7. Simulation routine: draw correlated normals by Cholesky, step each forward with its drift, carry payoffs to the terminal date, average, discount.
8. The LMM volatility function in the chapter is deterministic and level-independent, hence without skew: real desks extend it.

## Connects To
- **ch06**: PCA of swap rates that Gauss+ is estimated against.
- **ch07**: risk-neutral pricing, OAS, and the one-factor trees that Gauss+ and LMM generalize.
- **ch09**: mean reversion, Ho-Lee θ(t) fitting (used again in Gauss+ Appendix D) and the Vasicek volatility term structure that Gauss+ corrects.
- **ch10**: time-dependent volatility and lognormal dynamics (the η(t) and (11.44) specifications).
- **ch15**: Eurodollar/Euribor futures convexity correction using calibrated volatility models.
- **ch16**: swaps and swap-rate formula `(d(t)−d(t+T))/A` used in swaption approximations.
- **ch18**: caplets, swaptions, Black/normal models, and the derivation of numeraires and forward measures (the "more formal connection").
- **ch20**: MBS and swaption demand, which drive cap/swaption richness.
- **`hull-derivatives` ch33**: LMM (BGM) and multi-factor models in Hull's notation.
- **`hull-derivatives` ch28**: martingales and measures underlying the forward-measure pricing.
- **`cfa-fixed-income` ch08**: binomial tree basics.
