# Chapter 3: Parsimonious Functional Forms (Nelson-Siegel and Svensson)
> **Source**: ECB Statistics Paper No 27 (2018), §3.2, §6.1 (Table 6), Appendix 2 (B.1), Appendix 3 and Appendix 6 | Nymand-Andersen

## Core Idea
Nelson-Siegel (N&S, 1987) and Svensson (1994) describe the whole forward curve with 4 or 6 parameters that have direct economic readings: long-run level, short-to-long slope, and one or two humps. The forward rate converges horizontally to a constant, which gives smooth, stable, communicable curves. Flexibility is limited by the parameter count, and estimation is sensitive to starting values.

## Frameworks Introduced
- **Nelson-Siegel model** (4 parameters β₀, β₁, β₂, τ): instantaneous forward rate
  `f(t) = β₀ + β₁·exp(−t/τ) + β₂·(t/τ)·exp(−t/τ)`
  - When to use: smooth policy or communication curves; thin data; need of stable parameters.
  - How: fit the parameters by minimising squared yield (or duration-weighted price) errors across bonds, with constraints β₀ > 0, β₀+β₁ > 0, τ > 0.
  - Failure mode: one hump only; flexibility at short and long ends is limited.
- **Svensson extension** (6 parameters β₀…β₃, τ₁, τ₂): adds a second hump/U-shape
  `f(t) = β₀ + β₁·exp(−t/τ₁) + β₂·(t/τ₁)·exp(−t/τ₁) + β₃·(t/τ₂)·exp(−t/τ₂)`
  - When to use: curves with two bends, better out-of-sample fit; the ECB's published model.
  - Failure mode: parameters highly correlated (near-identical curves from different parameter sets, "over-parameterised"); more sensitive to input changes.
- **Parameter interpretation** (paper): β₀ = long-term asymptote of f (must be positive); β₁ = spread long minus short, so β₀+β₁ = short rate (t → 0); τ₁ = position of the first hump or U; β₂ = size and sign of the hump; β₃ and τ₂ do the same for the second hump.
- **Banque de France hybrid**: estimate Svensson; if β₃ lies inside its confidence interval use Svensson, else Nelson-Siegel. Svensson was selected in 405 of 502 days (above 80%).
- **N&S / Svensson as constrained McCulloch**: the forward curve is constrained away from undesirable shapes.

## Key Concepts
- **Asymptote β₀**: long-end forward and zero rate; parsimonious models assume 20-25 year forwards are indistinguishable.
- **Short rate**: y(0) = β₀ + β₁.
- **Hump / U-shape**: local extremum produced by the β₂ (β₃) term; sign of β decides hump or trough.
- **Decay factor τ**: scale (years) at which the exponential terms fade; hump sits near 1.8τ for the spot-curve hump factor (recomputed).
- **Spot curve from forward**: s(T) = (1/T)∫₀ᵀ f(u) du.
- **Par curve**: derived from discount factors of the fitted spot curve.
- **Objective function**: yield deviations (ECB, Bundesbank, Greece) versus price deviations weighted by 1/D² (Banque de France).
- **Starting values**: initial parameters for the optimiser; results are sensitive to them.
- **Local optimum**: non-linear least squares can stall; starting from the previous day's solution stabilises the series.
- **Over-parameterisation**: several parameter sets yield nearly the same curve.
- **Hybrid model**: rule switching between N&S and Svensson.

## Formulas & Reference Tables
Closed forms (derived by integrating f; numerically checked):
- **Nelson-Siegel spot**: `s(T) = β₀ + β₁·(1−e^(−T/τ))/(T/τ) + β₂·[(1−e^(−T/τ))/(T/τ) − e^(−T/τ)]`
- **Svensson spot**: N&S terms with (β₂, τ₁) plus `β₃·[(1−e^(−T/τ₂))/(T/τ₂) − e^(−T/τ₂)]`
- **Discount factor** (continuous compounding): `P(T) = exp(−s(T)·T)`; **forward between T₁ and T₂**: `f(T₁,T₂) = (s(T₂)T₂ − s(T₁)T₁)/(T₂ − T₁)`.
- **Par yield** (annual coupon, maturity N): `c = (1 − P(N)) / Σₙ₌₁..N P(n)`.
- Limits: `s(0) = f(0) = β₀+β₁`; `s(∞) = f(∞) = β₀`.

| Parameter | Level | Slope | Curvature/hump | Constraint |
|---|---|---|---|---|
| β₀ | Long-run asymptote | | | > 0 |
| β₁ | | Short minus long (negative = upward curve) | | β₀+β₁ > 0 |
| β₂, τ₁ | | | First hump, position τ₁ | τ₁ > 0 |
| β₃, τ₂ | | | Second hump | τ₂ > 0 |

**Table 6 parameters (ECB paper, dated "9 May 2005"; yields as decimals)**:

| | β₀ | β₁ | β₂ | β₃ | τ₁ | τ₂ |
|---|---|---|---|---|---|---|
| N&S | 0.05572142 | −0.03154683 | −0.04809111 | n/a | 1.86079661 | n/a |
| Svensson | 0.05570325 | −0.03151222 | 0.02464373 | −0.07449321 | 1.75867062 | 1.8224406 |

## Mental Models
- **Level, slope, hump**: β₀ anchors the long end, β₁ tilts, β₂/β₃ bend the middle.
- **Forward curve converges to a flat line**: bakes in the belief that far-forward expectations are indistinguishable; fine for policy reading, wrong if a true long-end slope is the object.
- **Use yesterday as today's prior**: optimisation is path-dependent; the previous day's parameters are the best start (ECB practice).
- **Two very different parameter sets can give the same curve**: compare curves, not parameters, when judging fit.

## Worked Example
Using Table 6 parameters (recomputed in Python; closed form equals numerical integration of f to 4 decimals). Yields in %:

| T (years) | N&S spot | Svensson spot | N&S forward f(T) | Svensson forward f(T) |
|---|---|---|---|---|
| 0.25 | 2.3247 | 2.3257 | 2.2492 | 2.2497 |
| 1 | 2.2211 | 2.2210 | 2.2190 | 2.2180 |
| 2 | 2.3336 | 2.3331 | 2.7308 | 2.7302 |
| 5 | 3.1375 | 3.1381 | 4.4776 | 4.4799 |
| 10 | 4.1194 | 4.1204 | 5.4377 | 5.4380 |
| 30 | 5.0782 | 5.0775 | 5.5721 | 5.5703 |

Steps for N&S at T = 5: x = 5/1.8608 = 2.687; g = (1−e^(−x))/x = 0.3468 and e^(−x) = 0.0681; s = 0.05572 − 0.03155·0.3468 − 0.04809·(0.3468 − 0.0681) = 3.1375%. Short rate = β₀+β₁ = 2.417%; long = 5.572%. Discount factor P(5) = exp(−0.031375·5) = 0.8548. Forward 2y-into-5y (continuous) = (5·3.1375 − 2·2.3336)/3 = 3.673%. Five-year annual-coupon par yield: N&S 3.153%, Svensson 3.154%.
Interpretation: the curves agree to about 1 bp; the two parameter sets look different (β₂ flips sign) yet describe the same curve, the over-parameterisation the paper warns about. The curve is an upward slope with a forward trough near 1 year.

## Anti-patterns
- **Reading β₂ or β₃ signs across days as economic signals** when τ and β₃ are poorly identified.
- **Cold-starting the optimiser every day**: results change with starting values and algorithm.
- **Forcing Svensson when β₃ is insignificant**: the hybrid rule avoids spurious second humps.
- **Fitting with 3-month and 30-year bonds unfiltered**: spreads incl. the shortest or longest maturity become volatile.

## Practitioner Notes
- ECB implementation (Table F.1): Svensson, six parameters, starting values = previous day's parameters, constraint long-term asymptote β₀ positive, minimise **yield** deviations, three curves released (spot, instantaneous forward, par).
- Bundesbank starting values: β₀ = mean yield of the three longest papers, β₁ = y₁ − β₀, β₂ = β₃ = −1, τ₁ = τ₂ = 1; fall back to the previous day if non-convergent.
- Banque de France starts Svensson from N&S estimates, β₃ = 1, τ₂ = 0, and searches starting sets to find a global minimum.
- Yield-minimisation gave average absolute yield errors of about 4 bp (MAE 0.037-0.044 in % points); price minimisation gave much larger yield errors at long maturities (ch07).
- Parsimonious models fit better in the belly than at the extremes.

## Key Takeaways
1. N&S: 4 parameters; Svensson: 6, adding a second hump.
2. β₀+β₁ is the short rate; β₀ the long asymptote; both must be positive.
3. Closed-form spot and discount formulas make par and forward curves straightforward.
4. Stability needs good starting values: use previous parameters.
5. Parameters are interpretable, hence transparent for public release.
6. Flexibility is limited; check ends and long maturities visually.
7. Hybrid N&S/Svensson switching on β₃ significance is an option.

## Connects To
- **ch02**: spline alternative.
- **ch04**: why parsimonious versus spline.
- **ch07**: empirical errors of N&S versus Svensson.
- **ch08**: ECB implementation details.
- **`tuckman-fixed-income` ch21**: curve construction; **ch02**: spot, forward, par relationships.
- **`cfa-fixed-income` ch07**: spot, forward and par curves, level/slope/curvature.
- **`hull-derivatives` ch4**: zero and forward rates.
