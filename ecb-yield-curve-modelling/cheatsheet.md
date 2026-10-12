# Cheatsheet — ECB Yield Curve Modelling

## Decision rules
- Public policy curve, daily release → **Svensson** (transparent, converges long end). Rich/cheap bonds or cross-area comparison → **Waggoner/VRP**.
- Fit gap within about 1 bp → decide on transparency, long-end behaviour, stability, not on RMSE.
- Parsimonious optimiser unstable → start from **previous day's parameters**; hybrid N&S/Svensson if β₃ insignificant.
- Spline long end erratic → raise long-end penalty, check max maturity, drop sparse bonds; do not trust 30y spreads.
- Any model comparison → same sample, same tests, in- and out-of-sample, several regimes, plus plots.
- Data first: quality over quantity; changes in the curve must be changes in yields.

## Thresholds and defaults
| Item | Value |
|---|---|
| Maturity range | 3 months to 30 years |
| Turnover filter | at least EUR 1m a day (actual 20-100m) |
| Bid-ask filter | at most 3 bp |
| Price time | mid-quote near 17:00 CET |
| Outliers | 2σ per maturity bracket, twice |
| Out-of-sample | 1 bond in 10 (ranked by maturity) |
| Sample (ECB) | about 720 raw, about 318 used (286 + 32), 502 days |
| Knots | equal bonds between knots, about every 6th bond (not 3-4) |
| VRP test values | L = 100,000, S = 0.1, μ = 1 |
| Waggoner steps | a=0.1, b=100, c=100,000 at 1y and 10y |
| Hit-rate band | 1.5 bp (11-16%), 3 bp (72%), 5 bp (98%) for Svensson |
| Typical error | WMAE 2-5 bp; RMSE 5-9 bp |
| Parameter rules | β₀ > 0, β₀+β₁ > 0 (short rate), τ > 0 |

## Trade-off matrix
| | Spline (Waggoner, VRP) | Parsimonious (N&S, Svensson) |
|---|---|---|
| Fit | Slightly better | Slightly worse |
| Long end | Erratic, volatile | Flat, stable |
| Interpretation | None | Level, slope, humps |
| Settings | Algorithm, penalty, knots | Starting values, algorithm |
| Communication | Hard | Easy |

## Tells and smells
- Hit rate low at long maturities but RMSE fine → look at the plot; hit rate ignores distance.
- Different parameter sets giving the same curve → over-parameterisation; compare curves, not betas.
- Yield spread series jumps with no market event → model artefact.
- Sample composition changes (new issues, holiday dips) → curve shifts that are not yield moves.
- Spreads that include 3m or 30y noisier → edge effects.
- Results great in a calm window → untested in stress or near zero rates.
- Spline curves showing 30y yield flipping 5%-6% without data support → over-flexible penalty.
