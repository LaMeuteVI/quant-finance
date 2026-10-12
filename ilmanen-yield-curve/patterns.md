# Patterns — Forward-Rate and Yield-Curve Trade Recipes (Ilmanen)

## Bootstrap Spot and Forward Rates from Par Yields
**When to use**: turning a par curve into spots, one-year forwards and implied next-year curve.
**How**: 1) s₁ = par₁. 2) For each n solve `100 = C/(1+s₁) + … + (C+100)/(1+sₙ)ⁿ` with C = parₙ. 3) `1+fₙ₋₁,ₙ = (1+sₙ)ⁿ/(1+sₙ₋₁)ⁿ⁻¹`. 4) Implied curve: `(1+f₁,ₙ)ⁿ⁻¹ = (1+sₙ)ⁿ/(1+s₁)`.
**Trade-offs**: 2-decimal par inputs give up to ~10bp noise beyond 6y. Upward curve: forward > spot > par (ch01).

## Break-Even Test of a Directional View
**When to use**: before shorting or extending duration.
**How**: 1) Compute `Δfₙ₋₁ = f₁,ₙ − sₙ₋₁` (or the carry rule `(sₙ − s₁)/Dur_h + (sₙ − sₙ₋₁)`). 2) Compare your expected move in the constant-maturity rate. 3) Go short only if you expect a rise larger than the break-even; be long if smaller.
**Trade-offs**: break-evens are model-free but the unchanged curve has been the better base case than forwards realized (ch01, ch02).

## Cheap-Sector Butterfly from the Forward Curve
**When to use**: the one-year forward curve has a local bump (par curve looks smooth).
**How**: 1) Plot the forward curve. 2) Buy the bond whose forward is abnormally high and sell the neighbor on the low side. 3) Add a third leg (e.g. a longer short) with weights that make level and slope exposures zero. 4) Judge cheapness versus the bond's own history.
**Trade-offs**: market-value-weighted pairs leave level and slope risk. Cheapness can persist for months (ch01).

## Barbell-Bullet Break-Even (Curve Trade vs Convexity Trade)
**When to use**: sizing any duration-neutral flattener/steepener or barbell vs bullet.
**How**: 1) `w_long = Dur_bullet,h/Dur_long,h`, rest in cash. 2) Rolling-yield give-up = `w·RY_long + (1−w)·RY_cash − RY_bullet`. 3) Flattening break-even ≈ give-up ÷ (w_long·Dur_long,h) = bp of bullet-to-long spread narrowing with no parallel shift (0.71% ÷ 6.7 ≈ 11bp in the 10s–30s example). 4) Parallel break-even = shift at which `½·ΔCx·Δy²` covers the give-up. 5) Compare both with historical frequency (10s–30s Sep 1995: 11bp flattening vs 138bp parallel).
**Trade-offs**: concave curve means forwards imply flattening; most of that is convexity value, not a flattening forecast (ch02, ch05).

## Convexity-Adjusted Expected Return
**When to use**: ranking bonds or barbells by near-term expected return with an unchanged-curve base case.
**How**: 1) Rolling yield = yield + rolldown. 2) σ = bp yield volatility (`σ_bp = relative vol × y`). 3) Add `½·Cx·σ²` (scale by horizon). 4) Rank sums. 5) For a view, add `−Dur_h·E(Δy)`.
**Trade-offs**: value is only as good as σ (hundreds of bp in early 1980s, rarely above 100bp in 1990s). Zero convexity: `Cx ≈ Dur²/100` (ch05).

## Convexity Bias Curve Thought Experiment
**When to use**: isolating how much of long-end curve sag is convexity.
**How**: 1) Give every zero the same expected return. 2) Rolling yield = expected return − `½·Cx·σ²`. 3) That equals the one-year forward for (n−1, n). 4) Chain forwards into spots.
**Trade-offs**: pure result inverts; real curves hump because positive BRP offsets the bias at the front end (ch05).

## Implied Volatility of a Barbell-Bullet Trade
**When to use**: asking whether the curve prices more or less volatility than you expect.
**How**: solve σ such that rolling-yield spread = convexity pick-up; compare with option-implied or historical σ. Better: subtract convexity value at implied σ from the rolling-yield spread to isolate flattening expectations.
**Trade-offs**: very noisy; dished curves give negative σ (ch05).

## Decompose a Forward into Expectations, Premium and Convexity
**When to use**: interpreting a forward curve or backing out market expectations.
**How**: 1) `f(n−1,n) = s₁ + Dur·E(Δs) + BRP + CB`. 2) Proxy BRP by long-run average (ch03) or expectations by surveys. 3) CB = `−½·Cx·σ²`. 4) Solve for the remaining term.
**Trade-offs**: residual is multiplied by duration; unreliable beyond ~7y duration (ch03, ch06).

## Survey-Based Risk Premium Estimate
**When to use**: measuring the premium embedded in bills or long bonds.
**How**: (forward-implied Δ − survey Δ) × duration at horizon, annualized (Δ3m gap 106bp × 0.25 → ≈53bp/yr; 30y 24bp × ~10 → ≈480bp/yr).
**Trade-offs**: surveys are poor forecasts themselves (ch02).

## Horizon-Shifted Curve Trade
**When to use**: a view on a spread one year ahead (e.g. 2s4s in a year).
**How**: trade the 3y and 5y zeros plus 1y cash today; for an immediate view use 2s vs 4s plus cash.
**Trade-offs**: maturities shorten over the horizon (ch02).

## Estimate the Long-Run Bond Risk Premium
**When to use**: setting strategic (benchmark) duration.
**How**: 1) Choose a neutral window (similar start/end yields, ~300 months). 2) Use maturity-subsector portfolios. 3) Compare average term spread and average realized excess return. 4) Check five-year subperiods, hit rates and other markets. 5) Use geometric for history, arithmetic for expectation (`GM ≈ AM − σ²/2`).
**Trade-offs**: no econometric fix for period-specific trends (ch03).

## Four-Predictor Forecast and Dynamic Duration
**When to use**: tactical duration timing versus a benchmark.
**How**: 1) Each month compute term spread (5y−3m), real yield, inverse wealth, momentum. 2) `E = −10.15 + 0.37·TS + 0.20·RY + 9.85·IW + 0.34·Mom` (% per month, refit on an expanding window). 3) Scaled: hold forecast% units of the 20y; 1/0: 1 unit if forecast > 0 else cash. 4) Map to target duration (aggressive −2…10, moderate 0…8, conservative 3…5 on a 4y benchmark). 5) Judge over 3–5 years.
**Trade-offs**: ~61% hit rate, R² ≈ 10%; fails in trend reversals (1994) (ch04).

## Five-Term Expected-Return Table
**When to use**: one scale for duration, sector, barbell and issue choices.
**How**: yield income + rolldown + `½·Cx_h·σ²·(1+RY/100)` + `−Dur_h·E(Δy)·(1+RY/100)` + local rich/cheap (repo advantage + spread to curve + expected cheapening). Weight portfolios by market value; rank on total, not yield spread.
**Trade-offs**: noisy inputs can make it worse than yield spreads; backtest first (ch06).

## Scenario Analysis with Implied Statistics
**When to use**: stress-testing a curve position.
**How**: 1) 3–5 curve scenarios (bear/bull parallel, unchanged, bear-flattener, bull-steepener). 2) Horizon returns. 3) Assign probabilities. 4) Weighted return. 5) Back out implied mean yield change, volatility, correlations.
**Trade-offs**: one scenario means zero volatility and undervalues convexity (ch06).

## Cash Enhancement Along the Money-Market Curve
**When to use**: managing cash benchmarked to 1-month bills.
**How**: move from 1m bills to 3m bills or high-grade money-market paper; take credit exposure at short maturities (V-shaped Euro–UST spread).
**Trade-offs**: the 1m bill is ~100bp rich; leveraged 2y-note trades lose the edge to private-issuer funding rates (ch03).
