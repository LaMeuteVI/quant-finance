# Cheatsheet — Fixed Income & Unconstrained Fixed Income Guides

## Decision rules
| When | Do | Because |
|---|---|---|
| Coupon vs yield | Coupon > yield → premium; < yield → discount | Price adjusts until yields match (ch02, 06) |
| Expecting rising rates | Floaters, short duration, check cap and reset | Coupon resets; cap turns a floater into a fixed bond (ch02) |
| Callable bond | Use yield to worst and OAS; stress extension | Price capped near call; Z-spread overstates credit pay (ch05, 06) |
| Comparing credit bonds | Z-spread for straight, OAS for optioned | Nominal spread ignores curve and options (ch05) |
| Long-dated zeros/bonds, curve move unknown | Use KRDs, not one duration | Parallel shifts are not the norm (ch08) |
| Fixed liability | Match duration with dispersed cash flows, rebalance | Price and reinvestment effects offset (ch08) |
| Surplus over liability | Contingent immunization with floor | Allows active risk to the surplus (ch08) |
| Small portfolio, no credit team | Use funds/ETFs, not single bonds | Diversification and selection capability (ch07) |
| Passive bond fund | Expect sampling and rising index duration | Full replication unaffordable (ch07, 08) |
| Unconstrained manager | Judge on qual analysis plus stress windows | Labels and Sharpe mislead; credit beta hides (ch09) |
| Fund duration reported | Ask by country, curve segment, hedges | A single number aggregates different curves (ch09) |
| Distribution yield > portfolio yield | Treat the gap as return of capital | NAV erodes (ch10) |
| EM exposure | Local-currency if you want FX diversification; hard currency for credit | FX is a main volatility driver locally (ch11, 16) |
| IG credit portfolio | Think spread duration first | Spread is >100% of index yield since 2009 (ch12) |
| Anticipating Fed hikes | Check term premium before shorting duration | 2017: 3 hikes, 10Y yield lower (ch12) |
| HY spreads above +1/+2 sd | Raise spread duration; below −1/−2 sd cut it | Mean reversion of spreads (ch13) |
| Tight spreads, callable HY | Re-test spread duration at original maturity | Duration jumps if spreads widen (ch13) |
| Convertible near conversion price | Take profit or switch to equity | Delta near 100%, convexity gone (ch14) |
| AT1 first call | Compare reset coupon with refinancing cost | Santander 2019 non-call (ch15) |
| Hybrid ratings | Assume 2-3 notches below issuer senior | Subordination and deferral (ch03, 15) |
| Private debt | Hold to maturity, size for illiquidity | Premium compensates limited liquidity (ch17) |

## Decision tree: which instrument?
1. Need capital protection and a dated payout? Senior bonds, covered bonds, immunized portfolio.
2. Need inflation protection? Linkers (check deflation floor) and breakeven.
3. Need income with credit risk? IG corporates (spread-driven), then HY, then hybrids/AT1, private debt.
4. Need equity upside with floor? Convertibles (balanced delta).
5. Need return independent of index? Unconstrained/absolute return with multi-manager and correlation checks.

## Trade-off matrix
| Choice | Gain | Give up |
|---|---|---|
| Single bonds | Control, no product fee | Diversification, selection costs (ch07) |
| ETF | Liquidity, transparency, low cost | Outperformance, full coverage (ch07) |
| Active benchmark | Alpha potential | Tracking error (ch07) |
| Unconstrained | Flexibility, new return sources | Opacity, credit beta (ch09) |
| Distributing class | Cash flow | Possible capital erosion, reinvestment risk (ch10) |
| Local-currency EM | Real yield, FX gains | Currency volatility (ch11, 16) |
| AT1 | Highest bank yield | Coupon cancellation, conversion, extension (ch15) |
| Private debt | Liquidity premium, covenants | Liquidity, long lock-up (ch17) |

## Thresholds and defaults
| Item | Value |
|---|---|
| IG boundary | Baa3 / BBB- |
| Rating mapping check | B1 = B+, B2 = B, B3 = B- (sources misprint) |
| Maturity buckets | Short 1-5y, medium 5-12y, long >12y (ch01) |
| Benchmark corporate size | At least EUR 500m (ch03) |
| AT1 trigger | 5.125% (low) / 7% (high) CET1 (ch15) |
| Tier 2 minimum maturity | 5 years (ch15) |
| TLAC | 18% of RWA from 2022 (ch03) |
| Hybrid step-up | typically 25-75 bp, capped ~100 bp (ch03, 15) |
| CDS standard coupon | 500 bp HY; XOVER 75 names; CDX 100 names (ch13) |
| Convertible balanced delta | around 50% (ch14) |
| Private debt tenors | 3-8 years; senior Italian yields 4-6% (2019) (ch17) |
| Fund life (private debt) | 6-10 years (ch17) |

## Tells and smells
- A "yield" quoted without saying YTM, YTW, current or distribution (ch06, 10).
- Screen quotes in small size for a bond that "has plenty of lines" (ch04).
- Unconstrained fund with high correlation to HY, EM, equities (ch09).
- Duration "negative" from derivatives with a different curve than the holdings (ch09).
- Hybrid priced to first call with no extension stress (ch15).
- Quasi-sovereign spread gap at historic lows or highs without support analysis (ch13).
- Distribution rate above portfolio income (ch10).
- Private debt offered without covenants or monitoring plan (ch17).
