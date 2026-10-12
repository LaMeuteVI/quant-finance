# Chapter 4: Interest Rates

## Core Idea
Every derivative valuation needs a correctly measured, correctly compounded risk-free zero curve. Build it by bootstrapping, extract forward rates from it, and summarize bond price sensitivity with duration and convexity.

## Frameworks Introduced
- **Compounding conversions**:
  - `R_c = m·ln(1 + R_m/m)` and `R_m = m(e^{R_c/m} − 1)`.
  - Continuous compounding is the default for derivatives.
- **Reference rates after LIBOR**: overnight rates (SOFR in the US, SONIA in the UK, €STR in the euro area) are the risk-free benchmarks. Term rates are compounded overnight rates. LIBOR is discontinued.
- **Bootstrap method**: price the short zero-coupon instruments first, then solve maturity by maturity for the zero rate that reprices each coupon bond. Interpolate linearly and hold the curve flat beyond the ends.
- **Forward rates**: `R_F = (R₂T₂ − R₁T₁)/(T₂ − T₁)`, which equals `R₂ + (R₂ − R₁)·T₁/(T₂ − T₁)`. An upward-sloping zero curve implies forwards above zeros.
- **FRA valuation**: value = `L·(R_K − R_F)·τ·e^{−R·T₂}`. Assume the forward rate is realized and discount at the risk-free rate.
- **Duration**:
  - `D = Σ t_i·(c_i e^{−y t_i})/B`, and `ΔB ≈ −B·D·Δy` (continuous y).
  - **Modified duration** `D* = D/(1 + y/m)` applies for compounding frequency m.
  - **Dollar duration** = `B·D*`.
- **Convexity**: `C = Σ t_i²·c_i e^{−y t_i}/B`, and `ΔB/B ≈ −D·Δy + ½·C·(Δy)²`.
- **Term-structure theories**:
  - Expectations theory: forwards equal expected spot rates.
  - Market segmentation.
  - **Liquidity preference**: forwards are *above* expected spot rates. This is the theory that fits observed data.

## Key Concepts
- **Zero (spot) rate**: the rate on an investment with a single payoff at maturity.
- **Par yield**: the coupon that makes the bond price equal to par. `c = (100 − 100d)·m/A`, where d is the discount factor to maturity and A the annuity factor.
- **Bond yield (YTM)**: the single discount rate that reprices all cash flows.
- **Basis point**: 0.01%.
- **Repo rate**: a collateralized borrowing rate (sell and repurchase). It is slightly above the overnight risk-free rate.
- **Instantaneous forward rate**: `R + T·∂R/∂T`.
- **Net interest income / ALM mismatch**: the risk of funding long assets with short liabilities.

## Mental Models
- Think of compounding frequency as **units** (miles vs km). Convert before comparing.
- Use **duration for small parallel shifts** only. Add **convexity** for large moves, and use key-rate / principal-component analysis for non-parallel moves (Ch 22).
- **Forward rates are break-even rates**: if you think future rates will be below today's forwards, borrow short and lend long. This is the Orange County trade (it worked until rates rose in 1994).

## Anti-patterns
- **Leveraged yield-curve bets without stress tests**: Orange County (Bob Citron) lost $1.5bn in 1994 when rates rose.
- **Mixing compounding conventions** in a single discounting formula.
- **Treating duration as exact for big shifts**: this ignores convexity.

## Reference Tables
| Maturity (y) | Price | Coupon | Zero rate (cont.) |
|---|---|---|---|
| 0.25 | 99.6 | 0 | 1.603% |
| 0.50 | 99.0 | 0 | 2.010% |
| 1.00 | 97.8 | 0 | 2.225% |
| 1.50 | 102.5 | 4 | 2.284% |
| 2.00 | 105.0 | 5 | 2.416% |

## Worked Example
**Bootstrap the 1.5-year zero rate.** The bond has a 4% coupon (semiannual) and a price of 102.5.
- Solve `2e^{−0.02010·0.5} + 2e^{−0.02225·1} + 102e^{−R·1.5} = 102.5`.
- This gives `e^{−1.5R} = 0.96631`, so R = 2.284%.

**FRA value.** The company receives 5.8% (s.a.) and pays SOFR on $100m for years 1.5–2. The forward rate is 5% and the 2-year rate is 4% (continuous).
- Value = 100m × (0.058 − 0.050) × 0.5 × e^{−0.08} = **+$369,200**.

**Duration check.** B = 94.213, D = 2.653, and the yield rises 10bp.
- The duration estimate is ΔB = −94.213 × 2.653 × 0.001 = −0.250, so B = 93.963.
- Full revaluation gives 93.963.

## Key Takeaways
1. Always state and convert compounding frequencies. Use continuous compounding for derivatives.
2. Bootstrap zero curves from liquid instruments. Linear interpolation is the default.
3. FRAs are valued by assuming the forward rate is realized, then discounting.
4. Duration = first-order parallel sensitivity. Convexity = second order.
5. Liquidity preference explains why forward rates usually exceed expected future rates.

## Connects To
- **Ch 5**: forward pricing uses these zero rates.
- **Ch 6**: duration-based hedging and Treasury bond futures.
- **Ch 7**: swaps are portfolios of FRAs.
- **Ch 22**: PCA of yield curve moves.
- **Ch 29–33**: term-structure models.
