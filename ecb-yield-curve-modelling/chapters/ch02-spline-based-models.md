# Chapter 2: Spline-Based Models (McCulloch, FNZ, Waggoner, Variable Roughness Penalty)
> **Source**: ECB Statistics Paper No 27 (2018), §3 and §3.1, Appendix 2 (B.2, B.3) and Appendix 3 | Nymand-Andersen

## Core Idea
Spline methods fit a piecewise cubic polynomial, joined smoothly at knot points, to the discount function or the forward curve. Their power is local flexibility (segments move almost independently); their danger is oscillation and over-fitting, which is controlled by a roughness penalty on the curve's curvature. Waggoner and Anderson-Sleath make that penalty vary with maturity, stiff at the long end and loose at the short end.

## Frameworks Introduced
- **McCulloch (1971, 1975) regression spline**: cubic (basis) spline fitted to the **discount function**; smoothness is implicit (set by the number of knots).
  - When to use: decent short-end fit with few design choices.
  - How: choose knots, build the B-spline basis, regress bond prices on cash-flow-weighted basis functions.
  - Failure mode: forward rates become unstable, fluctuating and rising steeply with maturity.
- **Fisher-Nychka-Zervos (FNZ, 1995) smoothing spline**: cubic spline on the **forward rate function** with an explicit, **constant roughness penalty**.
  - How: minimise squared errors plus a penalty on curvature; nodes about one-third of the number of bonds, spaced so that roughly equal numbers of bonds mature between adjacent knots.
  - Why/failure: the constant penalty stiffens the spline and cuts oscillation but misprices short maturities (Bliss 1997), where true curvature is greatest.
- **Waggoner (1997) variable roughness penalty**: same forward-rate cubic spline, but the penalty **varies with maturity** through a three-tier step function with steps at 1 and 10 years.
  - How: low penalty below 1 year (flexible), medium from 1 to 10 years, very high beyond 10 years (nearly straight forward curve).
  - Why it works: keeps short-end flexibility and damps long-end oscillation; beats McCulloch at all maturities and FNZ at short maturities (Waggoner's own test).
- **Anderson-Sleath (2001) continuous penalty (VRP)**: the penalty varies continuously with maturity and needs only three parameters (L, S, μ) versus Waggoner's five (two step dates plus three step levels). The ECB paper calls this the VRP (variable roughness penalty) model, used by the Bank of England.
- **Other spline relatives**: Vasicek-Fong (1982) exponential splines on the discount function; Mastronikola (1991) par-yield fit (cannot discount same-date bonds at the same rate).

## Key Concepts
- **Knot point**: maturity at which two cubic segments join; continuity constraints make the curve look smooth.
- **Regression spline**: smoothness from knot count only; **smoothing spline**: explicit penalty term on roughness.
- **Basis spline (B-spline)**: building-block cubic functions; any spline is a linear combination (vector β of P+2 coefficients).
- **De Boor augmented knot set**: {d_k}, k = 1..K+6, with d₁=d₂=d₃=d₄=s₁ and d_{K+4}=d_{K+5}=d_{K+6}=s_K, d_{k+3}=s_k.
- **Roughness penalty λ(m)**: weight on ∫[f″(m)]² dm; higher means stiffer curve.
- **Step-wise penalty**: constant on [min,m₁), [m₁,m₂), [m₂,max): levels a, b, c.
- **Continuous penalty**: λ(m) between S (short) and L (long), rate governed by μ.
- **Minimum support**: a B-spline is non-zero over a few segments only, so local data changes do not propagate far (makes Waggoner more stable to small price changes).
- **Over-flexible curve**: too low a penalty; fits errors, oscillates, unstable out of sample.
- **Number of parameters**: knots + 2 (Bank of Greece and BoE tables).
- **Discount function vs forward function**: the quantity modelled by the spline (McCulloch: discount; FNZ and Waggoner: forward).

## Formulas & Reference Tables
- **Cubic B-spline recursion** (r = 4, m ∈ [0, M], 1 ≤ k ≤ P):
  `Θᵏ_r(m) = Θᵏ_{r−1}(m)·(m − d_k)/(d_{k+r−1} − d_k) − Θᵏ⁺¹_{r−1}(m)·(m − d_{k+r})/(d_{k+r} − d_{k+1})`
  (identical to the standard De Boor-Cox form `Θᵏ_{r−1}(m)(m−d_k)/(d_{k+r−1}−d_k) + Θᵏ⁺¹_{r−1}(m)(d_{k+r}−m)/(d_{k+r}−d_{k+1})`). Start: `Θᵏ_1(m) = 1 if m ∈ [d_k, d_{k+1}), else 0`. Curve: `f(m) = Σ β_k Θ_k(m)`.
- **Objective (Waggoner, yield fit)** Bank of Greece: `min Σᵢ (Yᵢ − Ŷᵢ)² + ∫₀ᴹ λ(m)[f″(m)]² dm`
- **Objective (BoE, price divided by duration)**: `min Σᵢ ((Pᵢ − Πᵢ(β))/Dᵢ)² + ∫₀ᴹ λ(m)[f″(m)]² dm`
  Pᵢ observed price, Πᵢ(β) model price, Dᵢ duration. Dividing by duration converts price error to approximate yield error.
- **Step penalty**: `λ(m) = a for m<m₁; b for m₁≤m<m₂; c for m≥m₂`. ECB chart: a=0.1, b=100, c=100,000, m₁=1y, m₂=10y.
- **Continuous penalty (Anderson-Sleath)**: `λ(m) = 10^[ log₁₀L − (log₁₀L − log₁₀S)·exp(−m/μ) ]`, equivalently `log₁₀ λ(m) = log₁₀L − (log₁₀L − log₁₀S)·e^(−m/μ)`. L = 100,000, S = 0.1, μ = 1 (ECB/BoE test values).
  ⚠ Correction: Appendix 2 of the paper writes `log₁₀λ = L − (L−S)·exp(−m/μ)` with the raw values of L and S; with L=100,000 that is absurd. The footnote version above (logs of L and S) is the consistent one. Check: λ(0)=S=0.1, λ(1)=620.5, λ(2)=15,417, λ(10)≈99,937, λ(∞)→L (recomputed).

| Method | Fits | Penalty | Parameters to fix | Known weakness |
|---|---|---|---|---|
| McCulloch | Discount function | Implicit (knots) | Knots | Unstable forwards |
| FNZ | Forward function | Constant | Knot count, λ | Poor short end |
| Waggoner | Forward function | 3-step, at 1y and 10y | m₁, m₂, a, b, c | Choice of steps is ad hoc |
| Anderson-Sleath (VRP) | Forward function | Continuous | L, S, μ | Long-end volatility, sensitive to settings |

## Mental Models
- **Penalty as a stiffness dial per maturity**: think of a flexible ruler that you stiffen where data are sparse (long end) and loosen where data are dense (short end).
- **Knots buy flexibility, penalty buys smoothness**: the optimal penalty is conditional on the knot set; tune them together, not separately.
- **Segmented-market reading of a step penalty**: steps at 1 and 10 years mirror money-market / capital-market / long-bond segments; document that assumption.
- **Spline fit is cheap, credibility is expensive**: in-sample they fit almost anything; judge them out of sample (ch06).

## Worked Example
Continuous penalty weights with L = 100,000, S = 0.1, μ = 1 (all recomputed):

| m (years) | 0 | 0.5 | 1 | 2 | 5 | 10 | 30 |
|---|---|---|---|---|---|---|---|
| λ(m) | 0.1 | 22.95 | 620.5 | 15,417 | 91,111 | 99,937 | ≈100,000 |

Interpretation: at the very short end the curve may bend freely (λ = 0.1), by 2 years the penalty is already 150,000 times larger, and beyond 5 years forward-curve curvature is almost forbidden, so the long forward is nearly straight. Compare the Waggoner step version (0.1 / 100 / 100,000): same range, but a jump at exactly 1 and 10 years.

## Anti-patterns
- **Placing a knot every 3-4 bonds on a large euro-area sample**: FNZ and Anderson-Sleath advice suits small national samples; on hundreds of bonds it clusters knots. Use equal numbers of maturing bonds between knots (Bank of Greece: roughly every sixth bond).
- **Tuning only on in-sample error**: splines fit arbitrarily well in sample (Bliss 1996) and can do poorly out of sample.
- **Using a constant penalty and expecting a good short end** (FNZ).
- **Undocumented penalty choices**: smoothness/flexibility balance is chosen by the modeller and should be justified in writing.

## Practitioner Notes
- Different optimisation algorithm, smoothing parameters, penalty function and knot placement can each change results; the paper finds no conceptual reason either Waggoner variant must win.
- Best BoE smoothing combination found in the exercise: L=100,000, S=0.1, μ=1.
- Waggoner minimised yield errors in the Greek test and price/duration in the BoE test; starting values: average YTM of all bonds.
- Spline results are harder to communicate (many parameters, no economic meaning per parameter).
- Spline curves suit identifying abnormal maturities or individual bonds better than parametric curves.

## Key Takeaways
1. Splines model the discount function (McCulloch) or forward function (FNZ, Waggoner, VRP).
2. A roughness penalty on f″ trades fit against smoothness.
3. A maturity-varying penalty (Waggoner, Anderson-Sleath) preserves short-end flexibility and damps the long end.
4. Waggoner needs five smoothing inputs; the continuous VRP needs three (L, S, μ).
5. Knot count and placement interact with the optimal penalty.
6. Spline models demand more modeller judgement, and are less transparent.
7. Always test out of sample and inspect long maturities visually.

## Connects To
- **ch03**: the alternative (parsimonious) family.
- **ch04**: head-to-head literature comparison.
- **ch06**: out-of-sample design, error statistics and robustness tests.
- **ch07**: empirical performance of Waggoner and VRP.
- **`tuckman-fixed-income` ch21**: curve construction with splines and smoothing.
- **`cfa-fixed-income` ch07**: spot and forward curve concepts.
