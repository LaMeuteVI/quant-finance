# Chapter 8: The Evolution of Short Rates and the Shape of the Term Structure
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 8 (Part Three: Term Structure Models), including the Appendix (proof of the expected-return equation) and the USD/JPY swap-curve application

## Core Idea
Any forward (or spot) rate splits into three pieces: **expectations** of future short rates, an **interest rate risk premium** (proportional to duration), and a **convexity** term (negative, proportional to convexity times variance). The market curve at one date cannot separate expectations from risk premium, so only the risk-neutral drift matters for pricing. But the decomposition is the best sanity check on whether a model's drift and volatility are economically reasonable. In USD swaps the risk-premium and convexity effects roughly cancel, so forwards approximate expected rates.

## Frameworks Introduced
- **Three-effect decomposition of the curve (Tuckman's "expectations, convexity, risk premium")**:
  - When to use: to explain a curve's shape, to interpret a model's drift, or to back out implied rate expectations.
  - How:
    1. Start from expectations alone (no volatility, no risk aversion): spot rates are geometric averages of expected one-period rates.
    2. Add volatility with risk-neutral pricing: convexity pulls spot/forward rates down (Jensen: `E[1/(1+r)] > 1/(1+E[r])`).
    3. Add risk aversion: discount at rates above true rates (risk-neutral rates = true rates + premium per year of duration): this pushes rates up.
  - Why it works: a zero's price is convex in r, so volatility raises price (lowers yield). Risk-averse holders of duration demand extra expected return, which lowers price (raises yield).
- **Forward-rate decomposition (equation 8.28)**: `fᶜ(T) = rₜ + E[dr/dt]·D + λD − ½Cσ²`
  - When to use: to split any instantaneous forward rate into its components, given a volatility and a premium assumption.
  - How: (a) compute `−½Cσ²` from a convexity measure and the swaption-implied volatility; (b) set λ from a plausible Sharpe ratio; (c) the residual is the expectations term.
  - Failure mode: the answer depends on the assumed λ and σ. It is an illustration, not an observation.
- **Expected-return equilibrium condition (8.26)**: `E[dP/P] = r dt + λ D dt`
  - Risk premium is proportional to duration with respect to the single factor. Equivalently `S = λ/σ` (Sharpe ratio of every bond is the same).
  - Proof idea (Appendix, Ingersoll): hedge P with Q so the dw terms cancel. The riskless portfolio earns r. Hence `(αₚ − r)/(−Pᵣ/P) = (α_Q − r)/(−Q_r/Q) ≡ λ(r,t)` for all securities.
- **Return decomposition of a zero (8.23)**: `dP/P = fᶜ(T) dt − D dr + ½Cσ² dt`: carry/roll-down at the forward rate, duration loss/gain, convexity gain.
- **Equilibrium vs arbitrage-free models**:
  - Equilibrium: assumes a rate process plus a risk premium and derives the curve, so it does **not** match today's curve.
  - Arbitrage-free: takes today's curve as input (ch07) and derives the risk-neutral process.
  - Both are arbitrage-free within their own assumptions. The names are conventional.

## Key Concepts
- **Expectations effect**: forward rates rise with expected future short rates. With flat expectations and no volatility the spot curve is flat.
- **Convexity effect (value of convexity)**: the reduction in a rate due to `E[1/(1+r)] > 1/(1+E[r])`. It grows with maturity and with the square of volatility.
- **Interest rate risk premium**: extra expected return demanded per unit of duration. Positive if bond returns correlate with good times (falling rates when inflation falls).
- **λ (lambda)**: the risk premium parameter, in bp per year of duration. Sharpe ratio `S = λ/σ`.
- **Sharpe ratio (bond)**: `(E[dP/P] − r dt)/(Dσ√dt)`. Constant across bonds in a one-factor model.
- **Risk-neutral vs true drift**: risk-neutral drift = true expected change + λ (in short-rate terms). Only the sum is observable.
- **Jensen's inequality**: for a convex function, expectation of the function exceeds the function of the expectation.
- **Duration risk (in trees)**: in the stylized annual tree a two-year zero has one year of duration risk, a three-year zero has two. In reality rates move continuously, so risk is full maturity.
- **Instantaneous forward rate fᶜ(T)**: `∂[rᶜ(T)·T]/∂T`. Also `∂P/∂t = fᶜ(T)·P`.
- **Arbitrage-free model**: fits the initial curve by construction (Ho-Lee, ch09).
- **Equilibrium model**: derives the curve from rate process and premium (Vasicek, CIR, ch09/ch10).
- **Ito's Lemma**: `dP = P_r dr + P_t dt + ½P_rr σ² dt` for a price depending on r and t.

## Formulas & Reference Tables
Symbols: r = instantaneous short rate, σ = annual basis-point volatility of r, D = `−(1/P)∂P/∂r`, C = `(1/P)∂²P/∂r²`, λ = premium per year of duration.

| Item | Formula |
|---|---|
| Spot from flat expectations | `(1 + r(T))ᵀ = (1 + r₀)(1 + E[r₁])…` (annual compounding) |
| Jensen | `E[1/(1+r)] > 1/(1 + E[r])` |
| Ito for a zero | `dP = (∂P/∂r)dr + (∂P/∂t)dt + ½(∂²P/∂r²)σ² dt` |
| Zero price | `Pₜ = exp(−rᶜₜ(T)·T)`, `∂P/∂t = fᶜ(T)·P` |
| Return breakdown | `dP/P = fᶜ(T)dt − D dr + ½Cσ² dt` |
| Expected return, breakdown | `E[dP/P] = fᶜ(T)dt − D·E[dr] + ½Cσ² dt` |
| Risk-neutral investors | `E[dP/P] = r dt` |
| Risk-averse investors | `E[dP/P] = r dt + λD dt` |
| Sharpe ratio | `S = λ/σ` |
| **Forward-rate decomposition** | `fᶜ(T) = rₜ + E[dr/dt]·D + λD − ½Cσ²` |
| Risk premium ≡ drift | +x bp premium is indistinguishable from +x bp expected rate change |

Numbers to remember: with r = 1%, D = 5, λ = 10bp: expected return = 1% + 5 × 0.1% = 1.5%. λ = 10bp with σ = 100bp gives S = 10%. Convexity value in the tree: 1.8bp (2y) and 4.8bp (3y) at σ = 200bp/yr. Table 8.1 swaption spot-rate volatilities (bp/yr, 28 May 2010):

| Term | USD | JPY |
|---|---|---|
| 2y | 105.46 | 17.23 |
| 5y | 114.45 | 30.01 |
| 10y | 112.91 | 45.73 |
| 25y | 91.79 | 67.02 |

## Mental Models
- **Three forces on a forward rate**: expectations (any sign), risk premium (usually positive, grows linearly with maturity via duration), convexity (negative, grows like maturity squared via C·σ²). Short end: risk premium dominates and the curve slopes up. Long end: convexity dominates and the curve bends down.
- **Convexity is not free lunch**: convexity adds `½Cσ²dt` to expected return but subtracts exactly the same amount from the forward rate. A bond priced by arbitrage gets no expected-return advantage from convexity. Convexity helps only if realized volatility exceeds the volatility priced in.
- **Premium and expectations are twins**: the curve cannot distinguish them. Fix the long-end expectation (about 5% = 3% real + 2% inflation) and infer the premium.
- **Only the upward-sloping average curve needs a premium**: expectations cannot be up on average forever, convexity is negative, so a persistently positive slope implies a risk premium. Historical evidence is mixed (earlier periods were flat).
- **Short horizon: forecasts matter. Long horizon: only the level of expectations does.** Nobody can defend different expectations for the rate 29 and 30 years out.

## Worked Example
**A. Expectations only (annual compounding, r₁ = 10%; recomputed in python).**
- Expected one-year rates 10%, 12%, 14%: `r(2) = (1.10·1.12)^½ − 1 = 10.995%`, `r(3) = (1.10·1.12·1.14)^⅓ − 1 = 11.988%`. Upward-sloping.
- Expected 10%, 8%, 6%: `r(2) = 8.995%`, `r(3) = 7.988%`. Downward-sloping.
- ⚠ Correction: the source prints the three-year spot as both 11.998% and 11.988% in one paragraph. The correct value is **11.988%**.

**B. Adding volatility (risk-neutral, true expected rate 10% each year).**
- σ = 200bp/yr tree: date 1 rates 12%/8%, date 2 rates 14%/10%/6%. Two-year zero = 0.826720, so `r(2) = 9.982%` (convexity −1.8bp). Three-year zero = 0.752309, so `r(3) = 9.952%` (−4.8bp).
- σ = 400bp tree (date 1: 14%/6%, date 2: 18%/10%/2%): `r(2) = 9.927%`, `r(3) = 9.806%`. Convexity rises with volatility and with maturity.

**C. Adding a risk premium (σ = 400bp, λ = 20bp per year of duration).**
- Risk-neutral (true rates + 20bp at date 1, + 40bp at date 2): two-year zero = 0.826035 (vs 0.827541 with no premium), so `r(2) = 10.027%`. Expected one-year return of that zero under the true tree `= [.5(1/1.14 + 1/1.06) − .826035]/.826035 = 10.20%`, i.e. 20bp above the one-year zero.
- Three-year zero = 0.751184: risk-neutral prices next year 0.769067 and 0.889587 give expected return **10.40%** (40bp for two years of duration risk). `r(3) = 10.006%`.
- With λ = 20bp the curve is mildly upward at 1–2y and mildly downward at 2–3y (premium wins early, convexity late). With 40bp it slopes up throughout (`r(2) = 10.128%`, `r(3) = 10.207%`).

**D. USD swap application (28 May 2010, λ = 9bp/yr).**
- Six-month rate 10 years forward, 10y spot 3.512%, σ = 112.91bp, convexity of a 10y zero ≈ 10 × 10.5 in semiannual terms.
- Convexity term `= −½ × [10×10.5/(1 + 3.512%/2)²] × (112.91/10,000)² = −0.646%`.
- Risk-premium term `= λD = [10/(1 + 3.512%/2)] × 9bp = 0.884%` (88bp).
- The two roughly cancel (+24bp net), so forwards are close to expected rates, which are then about flat at 5% at long maturities. The Sharpe ratio is about 9bp/100bp = 9%.

## Anti-patterns
- **Attributing the entire slope to expectations**: ignores that premium and convexity both bend the curve. Average slope is positive while expected rates cannot rise on average.
- **Reading the risk-neutral drift as a forecast**: it is expectations plus premium. A 1.9bp/month drift could be all expectation or a mix.
- **Assuming convexity earns excess return**: priced convexity has zero expected advantage. The convexity term also lowers the forward.
- **Ignoring convexity at long maturity**: the effect scales with T² (−135bp on the 30y par swap in a 113bp-vol Gaussian model, see ch09) and is negligible only at the front end.
- **Calibrating a decomposition and treating it as data**: the split depends on the assumed λ and σ (Tuckman fixes λ so that long-run expectations are flat and S is historically plausible).
- **Applying a positive-premium story to EUR/GBP long ends**: pension and insurer demand for duration depresses long forwards. A flat-expectation decomposition there requires zero or slightly negative premium.

## Practitioner Notes
- Use the decomposition as a diagnostic on model parameters: does the drift imply a Sharpe ratio near 10% and flat long-run expectations near 5% (3% real + 2% inflation)? Model 2 in ch09 needs a Sharpe ratio of about 0.21, which is too high to read as a pure premium.
- Term-structure volatility inputs come from swaptions: the average of caplet volatilities over a term proxies the spot-rate volatility of that term.
- JPY: the lower volatility makes convexity smaller, and the same 9bp premium gives much higher implied Sharpe ratios.
- Sharpe ratio for bonds in the book: about 9% is "historically plausible".
- For pricing you never need to split drift into premium and expectations. For a reasonableness check, you do.

## Key Takeaways
1. Forward rate = short rate + expected change × duration + λ × duration − ½ × convexity × σ².
2. Volatility lowers rates through convexity, and the effect grows with maturity and volatility squared.
3. A risk premium raises rates in proportion to duration. It dominates the short end, convexity the long end.
4. Premium and expected rate change are observationally equivalent in today's curve, so only the risk-neutral process prices securities.
5. In a one-factor model every bond has the same Sharpe ratio `λ/σ`, by the hedging argument.
6. Convexity's extra return is exactly offset by a lower forward rate: no free lunch.
7. Persistent upward slope can only be explained by a positive premium. The evidence is unsettled.
8. In USD swaps premium (about 9bp/yr) and convexity roughly cancel, so forwards approximate expected rates.

## Connects To
- **ch07**: risk-neutral pricing. This chapter explains why risk-neutral drift exceeds true drift.
- **ch04**: convexity and duration definitions used in `−D dr + ½Cσ² dt`.
- **ch02**: forward-rate mathematics behind `∂P/∂t = fᶜ(T)P`.
- **ch09**: Models 1, 2, Ho-Lee and Vasicek turn drift choices into a curve shape.
- **ch10**: volatility specification, and closed-form spot rates for these models.
- **ch03**: carry and roll-down (forward-rate return term).
- **`cfa-fixed-income` ch08**: risk-neutral valuation and arbitrage-free trees.
- **`hull-derivatives` ch31**: equilibrium models (Vasicek, CIR) and the market price of risk λ.
