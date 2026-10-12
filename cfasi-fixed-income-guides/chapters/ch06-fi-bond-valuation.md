# Chapter 6: Introduction to Fixed Income Valuation
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 6 (Introduzione alla valutazione dei titoli a reddito fisso) | Francesco Spadaccia, CFA

## Core Idea
Valuing a bond means choosing the right yield measure for the instrument (current yield, YTM, yield to call/put/worst, real yield, discount margin), moving from a single discount rate to a spot-rate (arbitrage-free) framework, and measuring rate risk with duration and convexity. The chapter then adds credit analysis (ratings, the four Cs), a factor-based risk attribution example, and convertible bond valuation as bond floor plus call. The practical rule: yield measures are ex-ante promises that hold only under stated assumptions; duration and convexity give the price response; embedded options distort both.

## Frameworks Introduced
- **Yield measure selector**
  | Instrument | Measure | Formula idea | Key limitation |
  |---|---|---|---|
  | Any bond (quick screen) | Current yield | `Annual coupon / Price` | Ignores capital gain and reinvestment |
  | Option-free fixed bond | Yield to maturity (YTM / TRES) | IRR: `Price = Σ CF_t/(1+y)^t` | Needs hold to maturity, no default, reinvestment at YTM |
  | Callable / putable | Yield to call, yield to put | YTM with call/put date and price as redemption | Same assumptions as YTM |
  | Callable / putable (conservative) | Yield to worst | Minimum of YTM and all yields to call/put | Pessimistic by construction |
  | Inflation-linked | Real yield, breakeven inflation | Fixed real coupon on index ratio | Deflation clauses vary |
  | Floating rate | Discount margin | Average margin over reference rate that equates price | Assumes constant reference rate |
- **YTM position rule**: coupon = YTM → price par; coupon < YTM → discount; coupon > YTM → premium.
- **Ex-ante vs ex-post rule**: YTM is realized only if (1) held to maturity and redeemed at par, and (2) coupons reinvested at YTM. A shorter holding period replaces YTM with holding-period return (coupon income + price change).
- **Inflation-linked mechanics**: index ratio = CPI today ÷ CPI at issue; coupon and principal scale with it. Most linkers return at least par in deflation; exceptions the guide names are UK, Japanese and some emerging market issues. Breakeven inflation = nominal yield minus real yield at equal maturity; buy the linker if you expect inflation above breakeven.
- **Floater pricing logic**: a floating-rate note resets its coupon to the reference rate plus a margin, so price stays near par absent credit/liquidity change; discount margin equals the quoted margin at par, above it below par, below it above par. Floaters have no YTM comparable to fixed bonds.
- **Bootstrapping spot rates**: use the 1-year zero for `z1`; solve `P2 = C2/(1+z1) + (N2+C2)/(1+z2)^2` for `z2`; then `P3` for `z3`; recurse. Reference: Italian CTZ zero coupon bonds only reach 24 months, so longer spots must be bootstrapped.
- **Spot-forward link**: `(1+S2)^2 = (1+S1)(1+1f2)`. Rising spot curve implies a forward curve above it; falling implies below; flat implies identical.
- **Arbitrage-free valuation**: price a bond as a strip of zeros, each discounted at its own spot rate, instead of one YTM. Violations are arbitraged (buy the Treasury, strip it, sell the strips) as Treasury Strips illustrate.
- **Duration-convexity price approximation**: `ΔP/P ≈ −MD × Δy + ½ × C × (Δy)²`. Duration is the slope of the price-yield curve, convexity its curvature. For option-free bonds the convexity term is positive: duration alone understates gains when yields fall and overstates losses when they rise.
- **Embedded-option distortions**: callable bond, price capped near the call price as yields fall (negative convexity below a threshold yield `y*`); putable bond, price floored near the put price as yields rise.
- **Active risk attribution (BarraOne-style hierarchy)**: total active risk splits into local market risk (common factor: industry, style, term structure, spreads, emerging markets; plus selection), currency risk, and market/currency interaction. Components are volatilities and are not additive; correlations matter.
- **Credit analysis checklist**: (1) agency rating and outlook; (2) the four Cs.
  - **Capacity**: cash-flow generation, balance sheet and income statement, management, sector trend, regulation, competition, liquidity resources, corporate structure and holding arrangements, specific risks.
  - **Collateral**: pledged assets reduce loss given default (secured issues).
  - **Covenants**: protections such as a ceiling on net debt over capitalization.
  - **Character**: management quality and governance (board independence, over-boarding is negative).
- **Convertible bond valuation**: floor = straight bond value; value = straight bond + call on shares (number of shares = conversion ratio). Minimum value = max(conversion value, bond floor), otherwise arbitrage.

## Key Concepts
- **Current yield** — annual coupon over price; 4/90 = 4.44%.
- **YTM (TRES)** — ex-ante IRR of promised cash flows at the market price.
- **Yield to worst** — lowest of the yields to every possible call/put date and to maturity.
- **Real yield** — fixed yield on an inflation-linked bond before indexation.
- **Index ratio** — CPI today ÷ CPI at issue.
- **Breakeven inflation** — inflation rate that equalizes the nominal and linker returns.
- **Discount margin** — average margin over the reference rate expected over a floater's life.
- **Spot rate** — yield on a zero-coupon bond; discount rate for one cash flow.
- **Forward rate** — rate implied by the spot curve for a future period.
- **Macaulay duration** — present-value-weighted average time of cash flows; equals maturity for a zero-coupon bond.
- **Modified duration** — `D / (1 + y)`; percentage price change per unit yield change.
- **Convexity** — second-order price sensitivity; positive for option-free bonds, negative for callables at low yields.
- **Rating outlook** — positive, negative or stable; 6-12 month signal; "under review" typically resolves within 3 months.
- **Conversion ratio, conversion price, conversion value** — shares per bond; issue price ÷ ratio; ratio × share price.
- **Market conversion (parity) price** — convertible price ÷ conversion ratio.
- **Conversion premium** — market conversion price minus share price (per share), or as % of share price.
- **Premium payback period** — premium per share ÷ favourable income differential per share.
- **Premium over bond floor** — `Convertible price / bond floor − 1`.

## Formulas & Reference Tables
- `Current yield = Annual coupon / Market price`
- `Price = Σ CF_t / (1 + YTM)^t`
- `Index ratio = CPI_t / CPI_issue`
- `Breakeven = Nominal YTM − Real YTM` (approximation)
- `(1 + S_n)^n = (1 + S_{n−1})^{n−1} × (1 + (n−1)f_n)`; `(1+1f2) = (1+S2)^2/(1+S1)`
- `Macaulay D = Σ t × PV(CF_t) / P`; `MD = D/(1+y)`
- `ΔP/P = −MD Δy + ½ C (Δy)²`
- `Conversion value = Ratio × Share price`
- `Market conversion price = Convertible price / Ratio`
- `Conversion premium per share = Market conversion price − Share price`; `Premium ratio = premium per share / share price`
- `Favourable income differential per share = (Coupon − Ratio × Dividend) / Ratio`
- `Payback = Premium per share / Favourable income differential`
- `Convertible = Straight bond + Call`
- Rating scale: same IG/HY thresholds as ch02 (BBB-/Baa3 boundary). **⚠ Correction**: the source table again shows B2 and B3 both as B-; B2 corresponds to B.

## Mental Models
- Use YTM only to rank straight bonds held to maturity; use yield to worst for callables and holding-period return when you will sell early.
- Use spot-rate discounting when comparing bonds with different coupon patterns; one YTM mis-prices both zeros and high-coupon bonds.
- Use `ΔP/P ≈ −MD Δy + ½ C Δy²` for scenario analysis, and add effective duration/convexity from a model when options are present.
- Use the four Cs as a qualitative layer on top of ratings, which lag.
- Use a convertible as "bond floor + call": in falling equity it behaves like the bond, in rising equity it lags the stock by the premium, in flat equity the coupon beats the dividend.
- Use risk attribution before adding a position: total active risk is not the sum of its parts.

## Worked Example
Bond: 2 years, 5% annual coupon, face 100, price 101.
1. YTM solves `5/(1+y) + 105/(1+y)^2 = 101`: `y = 4.466%` (source rounds to 4.47%).
2. PVs: `4.786` and `96.214`.
3. Macaulay duration `D = (1×4.786 + 2×96.214)/101 = 1.953` years (source 1.95; its formula shows a typo sign on the first term).
4. Modified duration `MD = 1.953/1.04466 = 1.869`.
5. Estimated price change for +100 bp: `−1.869%` (convexity adds a small positive term).
Forward rate correction: with spots 1%, 2%, 3% for 1, 2, 3 years, the 1-year rate starting in two years is `1.03^3/1.02^2 − 1 = 5.03%`. **⚠ Correction**: the source writes the square root of that ratio, getting 2.48%, which is the geometric average of 1f2 and 2f3 rather than 2f3.

Convertible (company ABC, 7% coupon, EUR 1,000 nominal, ratio 25, price EUR 985, bond floor EUR 950, share EUR 35, dividend EUR 1):
- Conversion value `25 × 35 = 875`; floor 950 exceeds it, so minimum value is 950.
- Market conversion price `985/25 = 39.40`; premium per share `4.40`; premium ratio `4.40/35 = 12.57%`.
- Income differential `(70 − 25)/25 = 1.80`; payback `4.40/1.80 = 2.44` years.
- Premium over floor `985/950 − 1 = 3.68%`: the downside buffer is thin relative to the upside premium.

## Anti-patterns
- Using current yield to compare bonds of different maturities.
- Treating YTM as a forecast of realized return when you will sell early (the guide's 10-year 10% bond bought at 100, sold at 120 after one year, returns 30%, not 10%).
- Applying modified duration to a callable bond near its call price.
- Reading discount margin like a YTM spread.
- Adding up risk contributions from an attribution table.
- Buying a convertible for yield without checking the conversion premium and payback.

## Practitioner Notes
- Market practice computes YTM, YTC and YTP for every date and reports yield to worst.
- Floating coupons reset to money-market rates (Libor, Euribor, usually 3 or 6 month), which is why prices stay near par except between reset dates.
- The guide's attribution example (BarraOne via Credit Suisse): total risk 2.09, local market 1.96 (term structure 1.95, spread 0.83, emerging markets 0.12, selection 0.18), currency 0.64. The sum exceeds the total, which is the diversification effect between currency and market.

## Key Takeaways
1. Pick the yield measure by instrument: YTM, yield to worst, real yield, discount margin.
2. YTM holds only to maturity with reinvestment at YTM.
3. Spot rates discount single cash flows; forwards follow from spots; bootstrapping builds the spot curve.
4. Arbitrage-free pricing uses a spot rate per cash flow.
5. Duration gives the slope, convexity the curvature; both are distorted by embedded options.
6. Callable bonds have negative convexity at low yields; putable bonds have a price floor.
7. Credit analysis = rating + outlook + capacity, collateral, covenants, character.
8. Convertible = straight bond + call; minimum value is the greater of bond floor and conversion value.

## Connects To
- **ch02**: the risks quantified here.
- **ch05**: spreads (Z, OAS) built on the spot curve.
- **ch08**: duration management in active/passive portfolios.
- **ch09**: unconstrained funds' duration range.
- **`cfa-fixed-income` ch05, ch06**: duration, convexity and credit analysis in the CFA curriculum.
- **`tuckman-fixed-income`**: spot/forward theory and arbitrage-free pricing.
