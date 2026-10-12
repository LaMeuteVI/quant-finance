# Chapter 21: Curve Construction
> **Source**: Tuckman & Serrat, *Fixed Income Securities* (3rd ed.), Chapter 21

## Core Idea
Fixed-cash-flow securities are priced by interpolating a curve of discount factors or forwards that is calibrated to price liquid benchmarks exactly (bootstrapping), not by arbitrage or full term structure models. The recommended design is flat forwards (piecewise-constant continuously compounded forwards), optionally smoothed by piecewise quadratics. The trade-off is smoothness versus locality: smoothing makes hedges spread across benchmarks that should not matter.

## Frameworks Introduced
- **Three objectives of curve building**: (1) price all chosen benchmarks correctly; (2) economically reasonable forwards (no wild oscillations); (3) local bucket exposures (shifting one benchmark does not ripple through distant securities).
  - Tension: forcing smoothness (objective 2) damages locality (objective 3).
- **Two-step construction**: choose a functional form (discount factors, spot rates, or forwards), then fit it to benchmark prices by **bootstrapping** (fit the first segment to the first benchmark, then the next segment to the next benchmark, and so on).
  - Why forwards: they are monitored/traded, non-overlapping so they can shift independently, and imposing properties on forwards directly is numerically safer than differentiating spot rates (differentiation amplifies errors).
- **Flat forwards**: between t_{i−1} and t_i the continuously compounded forward is constant f_i, so d(t) = d(t_{i−1})·e^(−f_i(t − t_{i−1})).
  - When to use: default for pricing curves, especially LIBOR/OIS swap and futures curves.
  - How: choose segments so that each benchmark determines one segment's forward; solve f_i from d(t_i) = d(t_{i−1})·e^(−f_i·Δ).
  - Property: any forward rate over a period is the duration-weighted average of the flat forwards it spans.
  - Failure mode: forwards jump at knots. In practice, jumps are gradual and harmless at the short end.
- **Smooth forwards by piecewise quadratics**: starting from the flat forwards, find quadratic functions φ_i(t) between successive segment midpoints, such that (a) the function equals f_i at the midpoint of segment i and f_{i+1} at the next midpoint; (b) the integral of the smooth forwards over each flat-forward segment equals (t_i − t_{i−1})·f_i. The first function φ_1 is handled separately (linear).
  - Consequence: all benchmarks remain correctly priced (segment integrals unchanged), forwards are continuous, but the first derivative jumps at midpoints.
  - Failure mode: changing one f_k forces φ_k to change, which through (b) forces φ_{k+1}, φ_{k+2}, … to change. Locality is lost downstream.
- **Partial '01 hedging from a curve**: shift one benchmark rate 1 bp, refit, record the P&L change; hedge notional = P&L sensitivity ÷ benchmark DV01 per unit notional.

## Key Concepts
- **Benchmark (fitting) securities**: deposits/FRAs (very short end), Eurodollar futures (short end), swaps (intermediate and long end), with OIS for fed-funds curves (Chapter 17).
- **Bootstrapping**: sequential fitting, each new benchmark pins the next curve segment.
- **Flat forward segment**: interval with a constant continuously compounded forward.
- **Futures-to-forward (convexity) adjustment**: the forward rate for a futures period equals the futures rate minus a model-specific convexity correction (Chapter 13); also convert act/360 to continuous compounding.
- **Stub**: the period from spot settlement to the first futures start, fitted with a short rate such as 3-month LIBOR.
- **Locality**: moving a benchmark changes only nearby curve segments and therefore nearby hedges.
- **Partial '01 / bucket exposure**: P&L to a 1 bp change in one benchmark with the others fixed.
- **Floating-leg valuation in practice**: project forwards, multiply by actual accrual factors, and discount. The leg is not exactly par because accrual periods and LIBOR terms do not line up exactly.
- **Cubic spline**: smooth through the second derivative but prone to wild oscillation unless well-suited to the data.
- **Central-bank-date segments**: an alternate segmentation where knots sit on policy meeting dates, giving flat forwards an interpretation as targeted short rates (muddied by risk premia and by the lack of a one-to-one benchmark per segment).

## Formulas & Reference Tables
- `d(t) = d(t_{i−1})·exp(−f_i·(t − t_{i−1}))` — flat forward discount factor (t_{i−1} ≤ t ≤ t_i).
- `f_{i} = ln[d(t_{i−1})/d(t_i)] / (t_i − t_{i−1})` — bootstrapped forward.
- `f(T₁,T₂) = Σ f_i·Δ_i / (T₂ − T₁)` — any forward as a time-weighted average of overlapping flat forwards.
- Midpoint: `t_{i−1}^m = (t_{i−1} + t_i)/2`.
- Quadratic piece: `φ_i(t) = a_i + b_i(t − t_{i−1}^m) + c_i(t − t_{i−1}^m)²` on [t_{i−1}^m, t_i^m].
- Continuity: `φ_i(t_{i−1}^m) = f_i`, `φ_i(t_i^m) = f_{i+1}`.
- Segment integral: `∫φ_{i−1} over [t_{i−1}^m, t_{i−1}] + ∫φ_i over [t_{i−1}, t_i^m]`-type pieces sum to `(t_i − t_{i−1})·f_i`, i.e. the smooth curve reproduces each flat segment's average forward.
- First piece (linear): `φ_1(t) = f_1 + (f_2 − f_1)/(t_1^m − t_0^m)·(t − t_0^m)`.
- Par swap pricing: fixed leg PV = c·Σ(accrual_fixed·d) + d(T) (the last term is the fictional notional) must equal 1 at the par rate; floating leg = Σ(fwd_act/360 · accrual_float · d).
- Hedge notional = `P&L per 1bp / (DV01 per 100 / 100)`.

| Design choice | Flat forwards | Piecewise quadratic | Cubic spline |
|---|---|---|---|
| Forward continuity | jumps | continuous, derivative jumps | C² smooth |
| Locality | high | degraded downstream | poor |
| Stability/ease | easy, stable | harder | oscillation risk |
| Benchmarks priced exactly | yes | yes | yes (if fitted) |

## Mental Models
- **A curve is an interpolation device, not a theory.** It prices a 13.4-year swap from 12- and 15-year benchmarks; arbitrage is only used to extract the benchmark-implied forwards.
- **Forwards are the natural coordinates.** Non-overlapping forwards can be bumped independently; discount factors and spot rates are cumulative and overlap.
- **Smoother is not better.** Extra smoothness buys pretty pictures and pays with hedge ratios that contaminate unrelated buckets.
- **Hedge test of a curve.** If a 5.5-year and a 17-year swap need 4-, 7-, 12- and 25-year hedges, the curve is propagating artefacts, not information.
- **Match granularity to liquidity.** Segment length must match benchmark availability; if only the 10- and 12-year swaps exist, extract the 2-year rate 10 years forward, not a 6-month rate.

## Worked Example
1. **Flat-forward averaging (book)**: flat forwards 4% (year 10-12) and 4.25% (12-15). The 3-year forward from year 11 to 14 = (1×4% + 2×4.25%)/3 = 4.167%.
2. **Pricing Eurodollar futures from flat forwards (book data, recomputed)**: EDU0 covers 9/15-12/15/2010: 1 day at 0.5945% plus 90 days at 0.8480%, so forward = (1×0.5945 + 90×0.8480)/91 = 0.8452% (market column: 0.8453%). EDM1: (1×1.1138 + 91×1.2856)/92 = 1.2837% (market 1.2838%). Both match, so the segment rates price the futures.
3. **Three-year swap check (Table 21.3, recomputed)**: par rate 1.6695%; fixed-leg coupons (6 periods, 30/360 accruals 0.5000, 0.5000, 0.5000, 0.5111, 0.4917, 0.5000) discounted give PV 0.04899 per unit; adding d(6/3/2013) = 0.951018 gives 1.0000. The floating leg (projected act/360 forwards × accrual × discount factors) also gives 0.04899. Equal legs at the par rate confirm the curve prices the swap. Discount factors come from continuous forwards on act/360 (e.g. exp(−0.005945 × 92/360) = 0.99848).
4. **Toy bootstrap (computed)**: annual par swaps 2%, 2.5%, 3%. d(1) = 1/1.02 = 0.98039; d(2) = (1 − 0.025×0.98039)/1.025 = 0.95170; d(3) = (1 − 0.03×(0.98039+0.95170))/1.03 = 0.91460. Flat forwards: 1.980%, 2.970%, 3.976% (continuous). Each new swap pins exactly one new segment.
5. **Hedge ratio (book)**: 5-year partial '01 = $23,517 with 5-year DV01 of 0.04748 per 100, so notional = 23,517/0.0004748 = about $49.5mm. Flat forwards: hedge only with 5-, 6-, 15-, 20-year swaps (e.g. 49.5, 50.6, 56.9, 43.1 $mm). Smooth forwards: also large offsetting hedges of about −5.9mm (4y), −6.8mm (7y), −12.0mm (12y), −6.6mm (25y), which are artefacts of the quadratic linkage.

## Anti-patterns
- **Fitting a curve by differentiating a smoothed spot curve**: noise in spot rates explodes in forwards.
- **Using a cubic spline without checking forwards**: oscillating forwards and unstable hedges.
- **Segment lengths finer than the benchmark set**: unidentified forwards.
- **Ignoring the futures convexity adjustment and day counts**: systematic errors at the short end.
- **Pricing the floating leg as exactly par in precision-critical settings**: accrual periods and LIBOR terms differ (holidays, business-day rolls). Project forwards and discount.
- **Treating hedge ratios from a smooth curve as market-optimal**: they depend on the interpolation assumption.
- **Forcing exact fit of noisy benchmarks**: if prices carry observation error (on-the-run effects in Treasuries), minimize errors instead; for LIBOR swaps and futures, exact fit is standard.

## Practitioner Notes
- Typical benchmark set in the book's USD LIBOR curve (28 May 2010): first 10 ED futures, swaps 3-10y annually, then 12, 15, 20, 25, 30 and 40y.
- Take a snapshot of swap and futures rates when both markets are liquid; it need not be the futures close.
- Segments are sized so each futures rate pins one flat forward (about 3 months at the short end), which gives noticeable jumps only at longer terms, gradually changing in size.
- The two-curve (OIS discounting) method of Chapter 17 uses the same machinery: build projection and discount curves jointly so that swaps price at par.
- For a rough desk rule, use flat forwards for risk and hedging (locality) and smooth forwards only where jumps are operationally unacceptable, such as pricing exotics, and accept the dependency.
- Partial '01s are computed by bump-and-refit, with benchmark DV01s used to express hedges in benchmark notional.

## Key Takeaways
1. Price by interpolating benchmark-calibrated curves; bootstrap so every benchmark prices exactly.
2. Work in forward rates; flat forwards are the robust default.
3. Choose segments to match benchmark liquidity and overlaps (ED futures overlap, so non-overlapping segments cannot match deposits exactly).
4. Futures need convexity adjustment and conversion to continuous compounding before fitting.
5. Verify the curve by repricing benchmarks, including swap legs with actual accrual factors.
6. Piecewise quadratics smooth flat forwards while still repricing benchmarks, at the price of downstream dependence.
7. Judge a curve by its hedges: local hedges signal a healthy curve.

## Connects To
- **ch01**: bootstrapping discount factors from bond prices.
- **ch02**: spot, forward, par rates and bootstrapping from par swaps.
- **ch05**: partial '01s and key-rate exposures.
- **ch13**: futures-forward convexity adjustment.
- **ch15**: Eurodollar futures, FRAs and Fed policy extraction.
- **ch16**: swap valuation, day counts, fictional notional.
- **ch17**: two-curve OIS discounting, whose curves are built with these methods.
- **`hull-derivatives`**: curve building and bootstrapping of zero rates.
