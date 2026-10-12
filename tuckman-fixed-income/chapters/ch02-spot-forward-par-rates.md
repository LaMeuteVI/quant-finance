# Chapter 2: Spot, Forward, and Par Rates
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 2 (Part One) · Examples from USD/EUR/GBP/JPY swap curves, 28-May-2010

## Core Idea
Discount factors d(t) contain all the information, but rates are more intuitive: they normalize for amount and horizon. The same curve can be quoted three ways:
- **spot rates** r(t), the rate on a loan from today to t;
- **forward rates** f(t), the rate on a six-month loan from t − .5 to t;
- **par rates** C(T), the coupon that prices a bond or swap fixed leg at par. Swap rates *are* par rates.

Their relationships drive everything a curve trader does:
- spot ≈ the average of forwards;
- forwards sit above spot when spot rises, and below when it falls;
- par sits below spot on an upward-sloping curve;
- an asset rolling down an unchanged curve gains or loses according to *coupon vs the expiring forward*.

The chapter ends with a live trade: receiving EUR 10y6m against paying 25y6m or 30y6m forwards in Q2-2010, sized on roll-down.

## Frameworks Introduced
- **Swap-as-bond extraction of discount factors**
  - When to use: to build a benchmark discount curve from quoted par swap rates.
  - How:
    1. Add a fictional exchange of notional at maturity. The fixed leg then becomes a **coupon bond** and the floating leg a **floating-rate bond worth par** on reset dates (justified in ch16, with qualifications in ch17).
    2. A receiver "buys" a fixed-coupon bond for par. A payer "sells" one.
    3. Each par swap gives one equation, `(C(T)/2)·Σ d(t/2) + d(T) = 1`. Bootstrap them sequentially as in ch01.
  - Failure mode: post-2008, when LIBOR embeds bank credit and liquidity risk and OIS discounting applies, treating the floating leg as worth par on a LIBOR curve is only an approximation (ch17, two-curve discounting).
- **Spot–forward averaging**
  - `(1 + r(t)/2)^{2t} = Π (1 + f(s)/2)` over s = .5, 1, …, t. So r(t) is a geometric average of forwards, and the simple average is a first-order approximation.
  - Slope rule (Appendix E): `r(t) > r(t−.5) ⇔ f(t) > r(t−.5)`. A rising spot curve means forwards above spot, a falling one means forwards below spot. Continuous time: `f_c(t) = r_c(t) + t·dr_c/dt`.
  - Why it matters: forwards amplify curve shape. A gently falling long-end spot curve implies a steeply falling forward curve.
- **Par–spot ordering (Appendix F)**: if spot rates rise strictly, `C(T) < r(T)`. If they fall strictly, `C(T) > r(T)`. If the curve is flat at r, spot = forward = par = r (Appendix C).
  - Intuition: a par bond's early coupons are discounted at lower spot rates than r(T), so paying r(T) would price above par. The par rate must be lower.
- **Roll-down of a fixed-rate asset along an unchanged curve (Appendix G)**
  - `sign[P(T) − P(T−.5)] = sign[c − f(T)]`. As a bond or swap ages six months with the curve unchanged, its PV **rises if its coupon < the forward rate of the expiring period** and **falls if its coupon > that forward**.
  - When to use: to predict the P&L of "nothing happens", before sizing any trade.
- **Forward-curve RV trade construction (trading case study)**
  1. Identify an abnormal forward-curve shape. Here, EUR 10s-30s forwards sloped steeply *down*: 10y6m ≈ 4.25% vs 30y6m ≈ 2.29%.
  2. Explain it with **technicals and macro**. Pensions and insurers, pushed by Solvency II, were receiving fixed at the long end with no matching payers. Sovereign stress (Greece) added macro uncertainty.
  3. State the thesis and both "outs". If Europe deteriorates, EUR converges to the JPY curve. If it improves, EUR converges to the USD and GBP curves. **Either way 10s-30s steepens.**
  4. Implement: **receive the high forward (10y6m), pay the low long-end forward**, DV01-neutral so that a parallel 1bp move has zero P&L (Part Two, ch04).
  5. Check **roll-down**: a trade that bleeds while nothing happens may be stopped out by stop-losses or collateral calls before the thesis plays out.
  6. Optimize the legs on roll-down. Paying 25y6m instead of 30y6m raised roll-down from +7.1bp to +30.1bp a year.
  7. Hedge the global-flattening risk with the **opposite trade in a slow-moving currency** (JPY: pay 10y6m, receive 25y6m). Check that the hedge has no idiosyncratic risk of its own and that its roll-down (−13.8bp) does not kill the trade. Net roll-down = +16.3bp.
  8. Admit the residual bet: EUR 10s-30s flattening further *while* JPY steepens loses on both legs.

## Key Concepts
- **Simple interest**: interest = rate × term. One payment of principal plus interest.
- **Semiannual compounding**: simple interest each half-year, with proceeds reinvested. `F(1 + r/2)^{2T}`. The gap versus simple interest is **interest on interest**.
- **Continuous compounding**: `e^{r_c T}` growth, `d(t) = e^{−r_c(t)t}`.
- **Interest rate swap**: exchange of fixed (semiannual in USD) against floating (3m LIBOR, quarterly) on a **notional** that is never exchanged.
- **Payer / receiver**: the payer pays fixed (short the "bond") and the receiver receives fixed (long the "bond").
- **Spot rate r(t)**: the rate on a loan from today to t. `d(t) = (1 + r(t)/2)^{−2t}`.
- **Forward rate f(t)**: the rate agreed today on a six-month loan from t − .5 to t. `1 + f(t)/2 = d(t−.5)/d(t)`.
- **"XyYm" notation**: 10y6m is the six-month rate starting 10 years forward.
- **Par rate C(T)**: the coupon making a T-year bond's PV = par. Swap rates are par rates.
- **Annuity factor A(T)**: `Σ d(t/2)` for t = 1…2T, the PV of 1 per period. It converts a rate difference into a price difference. A(2) ≈ 3.948 in the USD example.
- **Flattening**: long rates fall more than short, *or* short rates rise more than long. **Steepening** is the reverse. The terms are defined by relative moves, even when "flatten" doesn't match everyday usage (e.g., an inverted curve becoming more inverted is a "flattening").
- **Roll-down** (some desks say **carry-roll-down**): P&L from the passage of time with the curve unchanged.
- **Stop-loss**: a loss threshold forcing closure. Together with collateral calls it creates **impatience**, which is why negative roll-down can kill a correct trade.

## Formulas & Reference Tables
- Growth at compounding frequency n: `(1 + r/n)^{nT}`. Continuous: `e^{rT}`. Equivalent rates: `(1 + r_sa/2)² = (1 + r_m/12)^{12} = (1 + r_a)`, etc.
- Spot: `d(t) = 1/(1 + r(t)/2)^{2t}` ⇔ `r(t) = 2[d(t)^{−1/(2t)} − 1]`.
- Forward: `(1 + r(t)/2)^{2t} = (1 + r(t−.5)/2)^{2t−1}(1 + f(t)/2)` ⇔ `f(t) = 2[d(t−.5)/d(t) − 1]`.
- Spot as product of forwards: `(1 + r(t)/2)^{2t} = Πₛ₌.₅ᵗ (1 + f(s)/2)`.
- Continuous forward: `f_c(t) = −d′(t)/d(t)`. `f_c(t) = r_c(t) + t·r_c′(t)`. Discrete: `f_c(t−Δ,t) = −[ln d(t) − ln d(t−Δ)]/Δ`.
- Par rate: `(C(T)/2)·A(T) + d(T) = 1` ⇒ `C(T) = 2[1 − d(T)]/A(T)`, with `A(T) = Σₜ₌₁^{2T} d(t/2)`.
- Bond price (coupon c, unit face):
  - `P = (c/2)A(T) + d(T)` (discount factors);
  - `P = Σ (c/2)/(1 + r(t)/2)^{2t} + 1/(1 + r(T)/2)^{2T}` (spot rates);
  - `P = Σ (c/2)/Π(1 + f/2) + 1/Π(1 + f/2)` (forwards);
  - **`P = 1 + ((c − C(T))/2)·A(T)`** (par rate). The premium or discount is the annuity-weighted coupon gap versus par.
- Geometric sum: `Σₜ₌ₐᵇ zᵗ = (zᵃ − z^{b+1})/(1 − z)`. With z = 1/(1 + r/2): `Σₜ₌₁^{2T} (1 + r/2)^{−t} = (2/r)[1 − (1 + r/2)^{−2T}]`.
- Roll-down sign: `P(T) − P(T−.5) = ½(c − f(T)) / Πₛ₌.₅ᵀ(1 + f(s)/2)`.

| USD swaps 28-May-2010 (verified) | Swap (par) rate | d(t) | Spot r(t) | Forward f(t) |
|---|---|---|---|---|
| 0.5y | 0.705% | 0.996489 | 0.705% | 0.705% |
| 1.0y | 0.875% | 0.991306 | 0.875% | 1.046% |
| 1.5y | 1.043% | 0.984494 | 1.045% | 1.384% |
| 2.0y | 1.235% | 0.975616 | 1.238% | 1.820% |
| 2.5y | 1.445% | 0.964519 | 1.450% | 2.301% |

| Curve shape | Forward vs spot | Par vs spot |
|---|---|---|
| Spot rising (upward sloping) | f > r | C < r |
| Spot falling | f < r | C > r |
| Flat at r | f = r | C = r |

## Mental Models
- **Spot = average of forwards, forward = marginal rate.** Like marginal vs average cost: the average rises only if the marginal exceeds it. Forwards show the curve's shape at maximum magnification, so read abnormalities in forwards.
- **Think of a fixed-rate asset as a strip of forward loans at coupon c.** Each period where c > f is a "gift" to the holder (value above par), and each period where c < f is a "cost". Rolling off a period removes that gift or cost, which gives the roll-down sign.
- **Par rates are the curve the market trades, spot rates the curve you price with, forward rates the curve you trade views on.**
- **Every trade needs a "what if nothing happens" answer.** Roll-down funds your patience. A great thesis with negative roll-down can die of stop-losses.
- **Hedge macro beta with a slow-moving twin.** If the risk is a global move, take the opposite position in a market whose idiosyncratic factor won't move over your horizon, and pay for it with part of your roll-down.

## Worked Example
**1. From swap rates to spot, forward and par (verified).**
- Inputs: 0.5- to 2.5-year USD par swap rates 0.705%, 0.875%, 1.043%, 1.235%, 1.445%.
- Step 1, bootstrap:
  - `(100 + 0.705/2)·d(.5) = 100` ⇒ d(.5) = 0.996489.
  - `(0.875/2)d(.5) + (100 + 0.875/2)d(1) = 100` ⇒ d(1) = 0.991306, and so on to d(2.5) = 0.964519.
- Step 2, spot: r(2) = 2[0.975616^{−1/4} − 1] = **1.238%**. So $100 grows to 100(1.00619)⁴ = **$102.499** in 2 years.
- Step 3, forward: f(2.5) = 2[0.975616/0.964519 − 1] = **2.301%**. So $100 invested at year 2 is worth **$101.151** at 2.5.
- Step 4, averaging check: (0.705 + 1.046 + 1.384 + 1.820 + 2.301)/5 = **1.451%** ≈ r(2.5) = 1.450%.
- Step 5, par check: A(2) = 3.948, and (1.235/2)(3.948) + 100(0.975616) = 100 ✓. Par 1.445% < spot 1.450% (upward-sloping curve).

**2. Roll-down of a 1.445% fixed leg on an unchanged curve (Table 2.2, verified).**

| Remaining maturity | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 |
|---|---|---|---|---|---|
| PV per 100 | 100.37 | 100.57 | 100.60 | 100.41 | 100.00 |
| Forward of that period | 0.705% | 1.046% | 1.384% | 1.820% | 2.301% |

- From 2.5 to 2.0 years the PV **rises** (+0.41), because the expiring 2.5-year period had a forward of 2.301% > the 1.445% coupon. Dropping a below-market period adds value.
- From 1.5 to 1.0 the PV **falls** (100.60 → 100.57), because the expiring forward 1.384% < 1.445%.

**3. Case study roll-down (Tables 2.3–2.5, verified; bp over one year, DV01-matched legs).**

| Leg | Today | 1y later (same curve) | Roll-down |
|---|---|---|---|
| Receive EUR 10y6m | 4.254% | 9y6m 4.127% | +12.7 |
| Pay EUR 30y6m | 2.293% | 29y6m 2.237% | −5.6 → **total +7.1** |
| Pay EUR 25y6m instead | 2.550% | 24y6m 2.724% | +17.4 → **total +30.1** |
| JPY hedge: pay 10y6m | 2.712% | 9y6m 2.594% | −11.8 |
| JPY hedge: receive 25y6m | 2.433% | 24y6m 2.452% | −1.9 (book: −2) |
| **Net with hedge** | | | **≈ +16.3** |

At €10,000 per bp of DV01 per leg, the +7.1bp version earns €71,000 a year if nothing moves.

## Anti-patterns
- **Comparing rates with different compounding conventions**: 2% annual equals 1.9901% semiannual, 1.9819% monthly and 1.9803% daily. Always convert.
- **Treating a par bond as permanently par**: it is par only at the instant of pricing. Any curve move or passage of time changes it.
- **Reading curve shape from par or spot rates alone**: abnormalities (like a steeply inverted EUR 10s-30s) are visible mainly in forwards.
- **Assuming the everyday meaning of "flattening/steepening"**: desk usage is about *relative* moves of long vs short rates.
- **Ignoring roll-down when choosing legs**: the 30y leg is more liquid, but the 25y leg carried +23bp a year more roll-down.
- **Hedging with a market that has its own idiosyncratic catalyst**: the hedge then *adds* variance.
- **Trading long-dated six-month forwards literally**: they are illiquid. Real implementation uses portfolios of par swaps with equivalent forward exposures (the book's footnote).

## Practitioner Notes
- Swap desks quote par rates, bootstrap d(t), and look at forward curves (6m forwards across tenors) to spot anomalies. Bloomberg-style charts plot par, spot and forward together (Figures 2.2–2.5). Typical patterns:
  - EUR in 2010: forwards above spot out to about 10–15 years, then far below, so the par curve crosses *above* spot at the long end.
  - USD: spot falls only gently after about 2041, so par stays below spot throughout.
- The EUR long-end inversion of 2010 was a **supply/demand technical**: pension and insurer receiving under Solvency II. The desk view was that it would eventually be absorbed, but the book is explicit that incremental receiving could flatten 10s-30s even more. The thesis had two ways to win (EUR converges to JPY or to USD/GBP) and one clear way to lose.
- Use roll-down as the tie-breaker between otherwise similar expressions of a view, and to justify buying insurance (the JPY hedge cost 13.8bp of the 30.1bp).
- **End-of-book Exercise 2.5 check (verified)**: with d = 0.998752, 0.996758, 0.993529, a 1.5-year 0.5% bond is worth 100.100. After six months on an unchanged curve it is worth 100.175, a rise, because c = 0.5% < f(1.5) = 0.650%.

## Key Takeaways
1. `d(t) = (1 + r(t)/2)^{−2t}`, `1 + f(t)/2 = d(t−.5)/d(t)`, `(C/2)A(T) + d(T) = 1`. Memorize these three links.
2. Swap rates are par rates. Bootstrap them like bonds, treating the floating leg as par.
3. Spot is the (geometric) average of forwards. Forwards sit above spot when spot rises and below when it falls. Par sits below spot on a rising curve.
4. `P = 1 + ((c − C)/2)·A(T)`: a premium or discount is the coupon gap times the annuity.
5. On an unchanged curve, a fixed-rate asset's price rises as it ages if its coupon is below the expiring forward, and falls if above.
6. Build RV trades in forwards: explain the anomaly (technicals plus macro), make them DV01-neutral, check roll-down and hedge the common factor with a slow-moving market.

## Connects To
- **ch00**: the pension and insurer technicals (Solvency II, LDI receiving) behind the EUR curve case.
- **ch01**: bootstrapping and the law of one price.
- **ch03**: returns decomposition (carry-roll-down, realized forwards), yields and spreads.
- **ch04**: DV01-neutral sizing of the two legs.
- **ch05**: forward-bucket '01s, the natural risk measure for forward-rate trades.
- **ch16 / ch17**: swap valuation; LIBOR vs OIS two-curve discounting.
- **ch21**: smooth curve construction.
- **`cfa-fixed-income` ch03**: spot, forward and par rates at L1.
- **`cfa-fixed-income` ch07**: term structure dynamics and rolling down the curve.
- **`hull-derivatives` ch04**: interest rates, compounding and FRAs.
- **`ilmanen-yield-curve` ch01**: forward-rate analysis.
- **`ilmanen-yield-curve` ch06**: frameworks for yield-curve trades, carry and roll-down.
