# Patterns — ECB Yield Curve Modelling

## Nelson-Siegel / Svensson Spot, Forward and Par Computation
**When to use**: turning fitted parameters into curves or discount factors. (ch03)
**How**: 1) Forward `f(t) = β₀ + β₁e^(−t/τ₁) + β₂(t/τ₁)e^(−t/τ₁) [+ β₃(t/τ₂)e^(−t/τ₂)]`. 2) Spot `s(T) = β₀ + β₁g₁ + β₂(g₁ − e^(−T/τ₁)) [+ β₃(g₂ − e^(−T/τ₂))]` with `g = (1−e^(−T/τ))/(T/τ)`. 3) `P(T) = e^(−s(T)T)`. 4) Forward between T₁, T₂: `(s₂T₂ − s₁T₁)/(T₂−T₁)`. 5) Par yield `c = (1−P(N))/Σₙ P(n)`.
**Trade-offs**: closed forms are cheap; limits s(0)=f(0)=β₀+β₁, s(∞)=f(∞)=β₀. Example N&S T=5 gives spot 3.1375%, forward 4.4776%.

## Daily Svensson Fit (ECB Recipe)
**When to use**: producing a published curve. (ch03, ch08)
**How**: 1) Clean sample (ch05). 2) Start from yesterday's six parameters. 3) Minimise yield deviations with β₀ > 0 and positivity constraints. 4) Output spot, forward, par curves. 5) Inspect the plot, publish on TARGET days.
**Trade-offs**: stable series, but sensitive to starting values and algorithm; fall back to N&S start if non-convergent.

## Hybrid N&S / Svensson Switch
**When to use**: avoid a spurious second hump. (ch03, ch07)
**How**: fit Svensson; test β₃ against its confidence interval; keep Svensson if inside, else use N&S.
**Trade-offs**: best fit statistics, extra rule to explain.

## Variable Roughness Penalty Spline Fit
**When to use**: flexible curves for cross-area comparison or anomaly detection. (ch02)
**How**: 1) Choose knots (equal bond counts per interval). 2) Build B-spline basis (De Boor). 3) Minimise `Σ((P−Π)/D)² + ∫λ(m)[f″(m)]²dm`. 4) Penalty `λ(m) = 10^[log₁₀L − (log₁₀L − log₁₀S)e^(−m/μ)]`, test L=100,000, S=0.1, μ=1; or Waggoner steps a=0.1, b=100, c=100,000 at 1y, 10y.
**Trade-offs**: best local fit, erratic 10-30y, sensitive to algorithm, penalty, knots.

## Bond Sample Cleaning
**When to use**: before any fit. (ch05)
**How**: 1) Descriptive statistics by instrument, maturity, country. 2) Keep central government (S.1311), zero and fixed coupon, no options or indexation. 3) Credit filter (AAA or homogeneous). 4) Turnover ≥ EUR 1m, bid-ask ≤ 3 bp. 5) One time stamp: mid-quote near 17:00 CET. 6) Maturity 3m-30y. 7) Two-layer 2σ outlier removal per bracket. 8) Log composition changes.
**Trade-offs**: smaller but cleaner sample; check sparse brackets.

## Two-Layer Outlier Filter
**When to use**: after liquidity filters. (ch05)
**How**: per maturity bracket compute mean ȳ and σ; drop |y−ȳ| > 2σ; recompute on survivors; repeat once.
**Trade-offs**: iteration catches masked outliers; with few bonds widen the band.

## In-Sample / Out-of-Sample Evaluation
**When to use**: model selection or validation. (ch06)
**How**: sort bonds by residual maturity; every 10th bond is out-of-sample; fit on the rest; compute RMSE, MAE, WMAE (`Σ|y−ŷ|/√D / N`), hit rate for both sets; repeat over five regimes.
**Trade-offs**: weight in-sample for flexibility, out-of-sample for robustness.

## Robustness Shock Test
**When to use**: check that local data noise stays local. (ch06)
**How**: bump all prices 15 bp (global); bump one bond by 3σ (local); bump short bonds 30 bp, long 20 bp (regional); compare curves.
**Trade-offs**: shows sensitivity only to those shocks; needs repeated days.

## Smoothness Spread Test
**When to use**: spotting model artefacts. (ch06)
**How**: build daily series of 2y-3m, 10y-3m, 10y-2y, 10y-5y, 30y-10y for spot and forward; look for jumps without market cause.
**Trade-offs**: spreads with the 3m point are noisy for all models.

## Purpose-Driven Model Choice
**When to use**: selecting a production curve. (ch04, ch08)
**How**: 1) State the use. 2) Same sample and tests. 3) If fit gaps are within about 1 bp, rank on transparency, long-end behaviour and stability. 4) Document assumptions.
**Trade-offs**: public policy curve → Svensson; relative value across areas → splines.

## Break-Even Inflation from Two Curves
**When to use**: read inflation expectations. (ch01)
**How**: estimate nominal and inflation-linked curves with the same method; subtract at each maturity.
**Trade-offs**: includes inflation risk and liquidity premia.
