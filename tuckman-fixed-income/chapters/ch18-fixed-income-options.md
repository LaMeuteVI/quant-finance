# Chapter 18: Fixed Income Options
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 18 · Selected Securities and Topics

## Core Idea
Practitioners price and hedge the liquid rate options (caps/floors, swaptions, bond options, ED/Euribor futures options, bond futures options) with **Black-Scholes-style formulas applied to the right forward underlying under the right numeraire**. Term structure models are kept for relative value and for path-dependent or Bermudan structures. Each product's formula is `h₀ × E[(S_T − K)⁺]`, where the underlying S is a martingale under a well-chosen numeraire (zero, annuity, or money-market account). The unit of quotation is normal (basis-point) volatility. Because implied volatility varies with strike (**skew/smile**), a flat-vol BS gives wrong deltas. Skew models (shifted lognormal, SABR) exist to get **hedge ratios** right, not just to fit prices.

## Frameworks Introduced
- **Martingale pricing with a numeraire** (the justification for BS in rates)
  - Arbitrage-free pricing ⇔ there exists a measure under which every asset's **normalized gains process** (value plus reinvested cash flows, divided by the numeraire's value) is a martingale: `V₀/N₀ = E₀[V_T/N_T]`.
  - Choose N so that (a) the underlying S is a martingale (`S₀ = E₀[S_T]`) and (b) the payoff divided by N_T is a function of S_T alone. Then `V₀ = h₀·E₀[(S_T−K)⁺]`, and assuming normal or lognormal S_T gives the closed form.
  - Proven in a one-period binomial: with asset A as numeraire, `p = (B̄₀ − B̄₁⁰)/(B̄₁¹ − B̄₁⁰)` makes every normalized asset a martingale.

| Product | Underlying S (martingale) | Numeraire | h₀ | Practitioner distribution | Call / Put |
|---|---|---|---|---|---|
| Caplet / floorlet (reset T, pay T+τ) | forward rate f₀(T,T+τ) | zero maturing T+τ | `τ·d₀(T+τ)` | normal rate | caplet `τd₀(T+τ)ξᴺ`; floorlet `τd₀(T+τ)πᴺ` |
| Payer / receiver swaption (T into τ) | forward par swap rate C₀(T,T+τ) | forward annuity A(T,T+τ) | `A₀(T,T+τ)` | normal rate | payer `A₀ξᴺ`; receiver `A₀πᴺ` |
| European bond option (expiry T) | forward bond price B₀(T) | zero maturing T | `d₀(T)` | lognormal price | call `d₀ξᴸᴺ`; put `d₀πᴸᴺ` |
| Bond futures option | futures price F₀ | money-market account (+ assume discount ⟂ futures) | `d₀(T)` | lognormal price | call `d₀ξᴸᴺ`; put `d₀πᴸᴺ` |
| CME ED futures option ($25/bp) | futures rate f₀ | none clean ("heroic" independence) | `$250,000·d₀(T)` | normal rate | **call on price = put on rate** `πᴺ`; put on price `ξᴺ` |
| NYSE Euronext Euribor futures option (futures-style) | futures price/rate | money-market account | `€250,000` (**no discounting**) | normal | call `πᴺ` (on rate); put `ξᴺ` |

- **Callable bond valuation in a term structure model** (Part Three tree)
  1. Build a risk-neutral short-rate tree, usually on swap or government benchmarks, plus a bond-specific OAS.
  2. Value the **otherwise identical noncallable** bond on the tree.
  3. Value the embedded call by backward induction: at each node `option = max(exercise value, continuation value)`, with continuation the discounted expectation.
  4. `Callable = Noncallable − Call`. The investor is long the bond and short the call.
  - Then: imply the OAS from the market price. Measure risk by shifting the short-rate factor, or shifting the initial curve for a DV01-like number.
  - **BS shortcut** is acceptable when the call is European (FNMA 2s of 2014, one call date), or when the first call date is distant: a 10NC5 is worth slightly more than a European call on the first call date.
- **BS shortcut for an agency callable (FNMA 2s of 2014 recipe)**
  - Model the unobserved noncallable forward price as an **OAS to the swap curve**.
  - Take its price volatility from swaptions: `σ_price = σ_bp(swaption) × forward DV01 / forward price`.
  - Solve for the OAS that makes `noncallable − d₀(T)ξᴸᴺ = market price`.
- **Skew modeling**: local-vol form `dSₜ = φ(Sₜ)σ√dt·εₜ`
  - Normal: φ = 1. Lognormal: φ = S. **Shifted lognormal**: φ = a + S (a ≥ 0). **SABR**: `dS = S^β σₜ √dt ε`, `dσ = α σₜ √dt ν`, `corr(ε,ν) = ρ`.
  - When to use: marking any off-ATM or seasoned swaption/cap, and computing deltas.
  - Failure mode: a model that fits today's prices but has the wrong **backbone** (how ATM vol moves with the forward) gives wrong deltas.
- **Early exercise of American futures options (Appendix B)**
  - CME-type futures option: hold if **time value > r × intrinsic value**. Exercise early only when deep ITM. The rule is symmetric for calls and puts.
  - Option on a cash asset (no dividends): **calls never exercised early**. Puts exercised early when `r·K >` time value.
  - Futures-style (Euribor) options: daily settlement leaves no intrinsic value to capture, so **never exercise early**.

## Key Concepts
- **Caplet / floorlet**: pays `τ[L − K]⁺` / `τ[K − L]⁺` at T+τ on LIBOR set at T. The max is contractual, not an exercise decision.
- **Cap / floor**: a strip of caplets/floorlets with one strike. The first (already fixed) caplet is usually dropped. USD caps reference 3M LIBOR. EUR caps reference 3M (short) or 6M (long).
- **Cap (flat) volatility**: a single vol that reprices all caplets. The true **caplet vols** have a term structure and are stripped from caps with strike adjustments.
- **Forward-starting cap** (e.g., 5×5): first reset in 5y, last payment at 10y.
- **Receiver / payer swaption**: the right to receive / pay fixed K. A T-y-τ-y receiver is a **put on the τ-year forward swap rate**, and a payer is a **call** on it.
- **Swaption matrix / volatility cube**: ATM normal vols by expiry × tenor. The cube adds strikes in ±50bp steps.
- **Cash vs physical settlement**: in USD, cash-settled at the swap-curve annuity (no valuation difference). In EUR, cash-settled at a flat-yield annuity at the par rate (minor difference). Premium-at-expiry swaptions (EUR since 2010) reduce sensitivity to the discount curve.
- **Call protection / Bermudan call**: 10NC5 = 10-year bond callable after 5 years, usually at each coupon date. The first call price is typically par + half the coupon, declining linearly to par.
- **Negative convexity**: a callable's price-rate curve bends below both the "NC to maturity" and "to be called" reference bonds. Its DV01 falls as rates fall.
- **Quarterly / serial / mid-curve ED options**: expire with the future / 1–2 months before it / 1, 2 or 5 years before the underlying future.
- **Skew / smile**: implied bp vol rising with strike / higher at both wings.
- **Backbone**: the empirical relation between ATM bp vol and the forward level, the right target for calibrating deltas.
- **Gains process / normalized gains**: value plus reinvested flows / divided by the numeraire.

## Formulas & Reference Tables
**Normal (Bachelier) building blocks**, with S_T ~ N(S₀, σ²T) and σ in rate units (bp vol):
- `ξᴺ(S₀,T,K,σ) = E[(S_T−K)⁺] = (S₀−K)N(d) + σ√T·n(d)`
- `πᴺ(S₀,T,K,σ) = E[(K−S_T)⁺] = (K−S₀)N(−d) + σ√T·n(d)`
- `d = (S₀−K)/(σ√T)`, `n(d) = e^{−d²/2}/√(2π)`
- ATM: `ξᴺ = πᴺ = σ√T/√(2π) ≈ 0.3989·σ√T`

**Lognormal (Black) building blocks**, with ln S_T normal, E[S_T] = S₀:
- `ξᴸᴺ = S₀N(d₁) − KN(d₂)`, `πᴸᴺ = KN(−d₂) − S₀N(−d₁)`
- `d₁ = [ln(S₀/K) + ½σ²T]/(σ√T)`, `d₂ = d₁ − σ√T`

**Shifted lognormal (a ≥ 0)**: `C = (a+S₀)N(d₁) − (a+K)N(d₂)`, with `d₁ = [ln((a+S₀)/(a+K)) + ½σ²T]/(σ√T)`, `d₂ = d₁ − σ√T`. a = 0 gives lognormal. a → ∞ with aσ fixed gives normal.

**SABR** (Hagan et al. 2002). Parameters: σ₀ = initial vol, α = vol of vol, β = CEV exponent, ρ = correlation. Approximate **lognormal** implied vol for K near S₀:
`σ_B(K) ≈ (σ₀ / S₀^{1−β}) · {1 − ½(1 − β − ρλ)·ln(K/S₀) + (1/12)[(1−β)² + (2 − 3ρ²)λ²]·ln²(K/S₀)}`, `λ = (α/σ₀)·S₀^{1−β}`.
- β → 1, α → 0 gives lognormal. β → 0, α → 0 gives normal.
- β and ρ drive the **skew** (higher values make bp-vol slope up with strike). α drives the **smile** (fat tails).

**Martingale results**:
- Forward rate: `f_t(T,T+τ) = (1/τ)[d_t(T)/d_t(T+τ) − 1] = E_t[f_T]` under the T+τ zero numeraire.
- Swap rate: `C_t = E_t[C_T]` under the annuity numeraire. Receiver value `[K − C_t]A_t`.
- Forward bond price: `B₀(T) = E₀[B_T]` under the T-zero numeraire.
- Futures price: `F₀ = E₀[F_T]` under the money-market account `M(T) = Π(1+rₜ)`.

**Other**:
- ED futures: `F = 100 − 100f`. Call payoff on price struck 99.25 = `$250,000 × max(0.75% − f, 0)`.
- Put-call parity on swaps: payer − receiver (same K) = forward swap value `(C₀ − K)A₀`. So ATM cap = ATM floor and ATM payer = ATM receiver.
- Price vol from bp vol: `σ_price ≈ σ_bp × DV01_fwd / P_fwd`.
- Normal ↔ Black near ATM: `σ_N ≈ σ_B × S₀`.

**USD ATM normal swaption vols, 9-Feb-2011 (bp, extract of Tuckman Table 18.4)**

| Expiry \ Tenor | 1y | 2y | 5y | 10y | 30y |
|---|---|---|---|---|---|
| 1m | 56.1 | 80.1 | 116.0 | 112.3 | 97.0 |
| 1y | 97.5 | 113.4 | 121.5 | 116.9 | 104.8 |
| 2y | 121.6 | 123.3 | 122.0 | 116.4 | 102.8 |
| 5y | 119.7 | 118.9 | **114.4** | 108.4 | 93.0 |
| 10y | 99.4 | 99.1 | 95.4 | 89.1 | 75.2 |

Shape: a vol "hump". Short-expiry short-tenor vols are pinned low by near-zero policy rates, and vols decline for long expiry × long tenor (mean reversion).

**SABR fits, USD 30-Nov-2010, ρ fixed at 0** (Tables 18.11–18.12): β ranges from ≈0.93–0.97 (1y expiry, short tenors, near lognormal) down to ≈0.17–0.28 (10y expiry or 30y tenor, near normal). α is stable at ≈30–37% except for short expiry × short tenor (1y1y α ≈ 4%). The 5y10y fit is α = 0.35, β = 0.56. No single parameter set spans the whole cube.

## Mental Models
- **"Pick the numeraire that makes the underlying a martingale, then it's just BS."** Caplet → payment-date zero. Swaption → forward annuity. Bond option → expiry zero. Futures option → money-market account.
- **Receiver = put on rates = call on bonds.** ED calls on price are puts on rate. Keep the rate/price inversion straight before choosing ξ or π.
- **Implied vol = gamma-weighted average of the instantaneous vols along the paths from forward to strike.** A skew is the market's forecast that bp vol rises with the rate level.
- **A callable = the noncallable minus a call. Its price-rate curve hugs "NC to maturity" at high rates and "to be called" at low rates.** In between it sits below both. This is negative convexity.
- **BS in rates is an interpolator and hedge-ratio engine, not a relative-value engine.** Use term structure models to judge rich/cheap across products.

## Worked Example
All values below were recomputed with the formulas above.

**A. Caplet (Table 18.1).** Reset 28-Nov-2012, pay 28-Feb-2013, valued 28-Feb-2011, strike 0.97%.
- Inputs: S₀ = 1.9077%, T = 639/365 = 1.7507, τ = 92/360 = 0.2556, σ = 77.22bp, d₀(T+τ) = 0.981801.
- d = (1.9077% − 0.97%)/(0.7722%·√1.7507) = 0.918.
- ξᴺ = 0.9377%·N(0.919) + 1.0217%·n(0.919) = **0.01037**.
- Caplet = 100 × 0.2556 × 0.981801 × 0.01037 = **0.2602** per 100 notional (26 cents).
- The 2y ATM cap (strike = 2y par swap rate 0.97%) sums seven caplets to **0.6688**.
- Exercise 18.1: at σ = 120bp the caplet is worth **0.3035**.

**B. 5y5y receiver swaption (Table 18.3).** Forward swap rate 5.28%, K = 5.28% (ATM), T = 5, forward annuity A₀ = 3.8285, σ = 114.5bp.
- πᴺ = σ√T/√(2π) = 0.01145 × 2.2361 × 0.39894 = **0.010213**.
- Value = $100mm × 3.8285 × 0.010213 = **$3.91mm**. Equivalent Black vol ≈ 114.5/5.28 ≈ 21.7%.
- Exercise 18.2: an ATM 2y5y receiver with a flat 4% curve and σ = 100bp gives πᴺ = 0.005642. With annual payments A = 4.116, so $100mm × 4.116 × 0.005642 ≈ **$2.32mm** (≈$2.34mm with semiannual payments, A = 4.149).

**C. FNMA 2s of 2014, European call on 4-Feb-2011 at par (Table 18.5).** Valued 20-Aug-2010.
- Noncallable forward price at a LIBOR OAS of −6.44bp = 101.9193.
- σ_price = 78.43bp × 0.03656/101.9193 = **2.813%**.
- T = 163/365. d₀ = 1/(1 + 0.2888%×163/360) = 0.998694.
- ξᴸᴺ = 2.0741, so call = **2.0714**.
- Callable = 102.6964 − 2.0714 = **100.625** = market price. This confirms the implied OAS of −6.44bp.

**D. EDM1C 99.25 (Table 18.6).** S₀ = 100 − 99.567 = 0.433%, K = 0.75% (a put on the rate), T = 118/365, d₀ = 0.998965, σ = 62.27bp.
- πᴺ = 0.00352865, so value = $250,000 × 0.998965 × 0.0035287 = **$881.25**.

**E. JGB 7y futures put, 135 strike (Table 18.7).** F₀ = 137.88, T = 109/365, d₀ = 0.999346, σ = 3.635%.
- πᴸᴺ = 0.2001, so value = ¥100mm × 0.999346 × 0.2001/100 ≈ **¥200,000**.

## Anti-patterns
- **Quoting all caplets at the cap's flat vol for risk**: caplet vols have a term structure. Strip caplet vols, adjusting for non-ATM strikes, before comparing with ED options.
- **Marking a seasoned swaption at the ATM vol of its original grid point**: a 5y5y struck 5.28% is, one month later, a 4y11m×5y that is 12bp OTM. Interpolate in expiry and strike, via a stochastic-vol model.
- **Using flat normal-BS deltas under skew**: they ignore the vol change as the forward moves. The normal, lognormal and SABR deltas differ materially even ATM (5y10y payers).
- **Setting SABR ρ = 0 just because the fit is good**: β and ρ are nearly redundant for fitting but not for deltas. Calibrate to the empirical backbone.
- **Applying lognormal BS to a bond futures option while ignoring the delivery option**: the futures DV01 (hence price vol) jumps when the CTD switches. That defeats the point of using BS for accurate deltas.
- **Treating ED futures option BS as rigorous**: the payment timing makes it an approximation. It needs a "heroic" zero correlation between the forward rate and 1 + f.
- **Discounting a futures-style (Euribor) option premium**: there is no upfront premium, so no discounting and no early exercise.
- **Treating a 10NC5 as a European call on the first date for risk**: it is a good price approximation, but the Bermudan rights add value and alter DV01 near the call boundary.

## Practitioner Notes
- **Model hierarchy on a desk**: BS-type (normal) formulas for quoting, interpolating the vol cube and computing hedges. Term structure models (ch07–ch11) for rich/cheap, Bermudans, callables and MBS. SABR (or shifted SABR) for the cube in strike.
- **Normal vol is the lingua franca in rates** (ATM payer = receiver; bp vols comparable across rate levels). The lognormal model matched the Nov-2010 skew well for high strikes but not for low strikes. Shifted lognormal with a = 1% did likewise, too low at low strikes.
- **Swaption matrix read** (Feb 2011): a peak of ≈120–124bp around 2y–3y expiries. The front 1m×1y was only 56bp because rates were anchored by Fed policy.
- **Callables**: the original purpose of the call was capital-structure flexibility and escaping covenants. It later became priced as a pure rate option. The typical corporate structure is non-call period, then callable on coupon dates, first call price par + ½ coupon, declining linearly to par.
- **Settlement conventions matter at the margin**: USD swaptions are almost always cash-settled on the swap-curve annuity. In EUR about half are cash-settled on a flat-yield annuity (the IRR annuity), which creates small valuation differences and a convexity effect.
- **Early exercise**: ignore it for liquid ED and bond futures options except deep ITM. Euribor options are never exercised early.
- ⚠ **Correction**: in the 5y5y example the text says the right "to receive 5.85%". The strike is **5.28%**, consistent with Table 18.3.
- ⚠ **Correction**: the SABR correlation is stated as 0 ≤ ρ ≤ 1. In general **−1 ≤ ρ ≤ 1**, and negative ρ is common for rate vols in lognormal terms.
- ⚠ Minor: Figure 18.5 is dated "November 30, 2011" but the calibration it uses is from 30-Nov-2010. FNMA pricing date "August 20, 20140" should read 2010.

## Key Takeaways
1. Every liquid rate option is `h₀ × E[(S−K)⁺]`, with S the forward rate, swap rate or price that is a martingale under the matching numeraire: caplet `τd(T+τ)`, swaption `A₀(T,T+τ)`, bond option `d(T)`, Euribor option `1`.
2. Receiver swaption = put on the forward swap rate. ED call on price = put on rate. Map before pricing.
3. Caps are quoted at one flat vol, but caplet vols have a term structure and a skew.
4. Callable = noncallable − call, done on a tree with an OAS. The BS shortcut works for European or distant first calls, with price vol = bp vol × DV01/price.
5. Skew means no single BS vol per expiry-tenor. SABR fits each point (β high at short expiries, low at long ones; α ≈ 30–35%), but deltas depend on the backbone.
6. Futures options: exercise early only when time value < r × intrinsic value. Futures-style options are never exercised early.

## Connects To
- **ch07–ch10**: risk-neutral trees, OAS and the normal vs lognormal volatility art that underlie callable valuation and skew intuition.
- **ch11**: the LIBOR market model, a consistent multi-caplet/swaption framework beyond single-option BS.
- **ch13**: forward vs futures prices and why futures are martingales under the money-market account.
- **ch14**: the bond futures delivery option that breaks the constant-vol assumption.
- **ch15**: ED/Euribor futures mechanics.
- **ch16**: swap annuities and forward swaps.
- **ch17**: the choice of discount curve and premium-at-expiry swaptions.
- **ch19**: corporate callables and OAS versus credit spread.
- **ch20**: prepayment as a short (American) call in MBS and negative convexity.
- **`hull-derivatives` ch18**: Black's model for futures options.
- **`hull-derivatives` ch20**: vol smiles.
- **`hull-derivatives` ch28–ch29**: numeraires/martingales and standard market models for caps and swaptions.
- **`cfa-fixed-income` ch09**: bonds with embedded options, OAS, effective duration and convexity.
