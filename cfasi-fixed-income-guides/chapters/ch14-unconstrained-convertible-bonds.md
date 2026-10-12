# Chapter 14: Convertible Bonds
> **Source**: CFA Society Italy × Advisor Private, "Unconstrained Fixed Income" guide (Sept–Oct 2019), Chapter 3 (I bond convertibili) | Luca Pellini, CFA (with a sponsored insert on a flexible fixed income fund)

## Core Idea
A convertible bond is a creditor claim (coupon, maturity, redemption, bond floor) plus an equity call option held by the investor. Its behaviour changes with the share price: bond-like when the stock is low, balanced around 70% to 100% of the conversion price, equity-like when deep in the money, and distressed ("busted") when credit fears take over. Long-only investors take profit around the conversion price to keep convexity; hedge funds delta-hedge to harvest volatility (gamma trading). Features of the prospectus (coupon deferral, M&A and change-of-control clauses, anti-dilution) matter as much as pricing.

## Frameworks Introduced
- **Convertible anatomy**: bond floor (PV of bond cash flows, credit-risk weighted) + conversion option. Terms: conversion ratio (shares per minimum lot, e.g. 1,000 shares per EUR 100,000 nominal), conversion price (= nominal ÷ ratio, here EUR 100 per share), parity (market value of the shares received on conversion), premium (convertible price ÷ parity, always above 1 and decreasing as parity rises).
- **Variants**: plain convertible; exchangeable (underlying shares from a different issuer); mandatory (repaid only in shares at maturity); cash-settled / delta-neutral (pays the cash equivalent of the shares on conversion).
- **Price regimes versus share price (typical illustrative axis: stock 40-130 vs conversion price 100)**
  | Zone | Share vs conversion price | Delta | Behaviour |
  |---|---|---|---|
  | Busted / distressed | Far below | Near 0 | Price converges to bond floor; if solvency fear, falls to recovery value of equal-seniority bonds; equity also falls with high volatility |
  | Bond-like | Well below | Low | Mostly credit and rates |
  | Balanced | About 70% of conversion price up to par | Around 50% | Participates in upside with a "parachute" on downside; favoured by long-only |
  | Quasi-equity | At or above conversion price | Toward 100% | Moves one-for-one with the stock, premium shrinks, less incentive to hold an illiquid bond |
- **Delta**: ratio of convertible price change to share price change; "50% delta" means ±1% in the stock moves the convertible about ±0.5 points. Other Greeks also apply as for calls (gamma, vega).
- **Why the investor rarely converts**: even deep in the money, converting forgoes the option's time value; also the investor gives up accrued coupon, may receive shares ex-dividend, conversion windows close before dividend dates and shareholder meetings, and the process takes days.
- **Pricing models**: combine interest rates, credit spread, share price and volatility; advanced models include an equity-credit correlation adjustment (equity falls widen credit spreads, especially for sub-IG or unrated issuers when lower market capitalization pushes financial ratios to alert levels).
- **Long-only playbook**: buy balanced convertibles, set profit targets when the stock passes the conversion price (waiting longer gives up convexity); to speculate on more upside, switch to the equity at the same risk profile with better liquidity.
- **Hedge fund/arbitrage strategies**
  - **Long/short delta-neutral (gamma trade)**: long convertible, short `delta × ratio` shares. Stock up: delta rises, net long equity; sell more shares to rebalance at higher prices. Stock back down: net short; buy shares back at lower prices. Profit from oscillation grows with volatility inside a trading range; the position is largely immune to direction.
  - **Volatility arbitrage**: convertibles vs listed options on the same stock (long-dated convertible volatility, up to 8-10 years, cannot be replicated with single-stock options that rarely exceed 18 months).
  - **Synthetic put**: short-dated, high-delta convertibles of highly rated issuers held by bearish investors; a quick drop in the stock leaves the bond out of the money and redeemed at par in cash, so the short equity hedge can be closed at a profit.
- **Prospectus protections to check**:
  - Dividend policy: convertible coupons cannot be deferred; extra dividends may pass through to bondholders fully or in part.
  - M&A: conversion ratio adjustment, extra cash, or put at a price equivalent to the offer terms when a takeover cannot be converted into in time.
  - Change of control: if a merger lowers the rating, the holder can put at par.
  - Anti-dilution: rights issues extend equivalent terms to convertible holders.
- **Evidence**: 2010-2019 total return of the Bloomberg-Barclays EMEA Convertibles index (long-only and delta-hedged versions) against Euro Stoxx 50 total return, base 100 in January 2010: convertibles delivered smoother performance through volatility spikes; the hedged version was market-neutral by design.

## Key Concepts
- **Bond floor** — PV of coupons and redemption at straight-bond yield; lower bound barring distress.
- **Parity** — conversion ratio × share price (market value of shares if converted).
- **Conversion premium** — price of convertible ÷ parity − 1 (or ratio form); falls as parity rises.
- **Delta / gamma** — sensitivities of convertible price to share price.
- **Busted convertible** — option worthless, trades as a bond (or distressed bond).
- **Quasi-equity** — convertible with delta near 100%.
- **Balanced convertible** — delta around 50%, asymmetric risk profile.
- **Mandatory / exchangeable / cash-settled** — structural variants.
- **Gamma trading** — rebalancing the hedge to monetize volatility.
- **Convexity** — payoff curvature that convertibles share with long options.

## Formulas & Reference Tables
- `Conversion price = Nominal / Conversion ratio`.
- `Parity = Conversion ratio × Share price`.
- `Premium = Convertible price / Parity − 1`.
- `Convertible value ≈ Bond floor + Option value`.
- `Hedge shares = Delta × Conversion ratio` (per bond lot).
- Greek rule of thumb: `ΔPrice ≈ Delta × ΔS + ½ Gamma × (ΔS)²`.

## Mental Models
- Use convertibles for equity upside with a floor when your equity view is positive but your risk budget is tight.
- Use the balanced zone (delta about 50%) for asymmetry; reduce when delta approaches 100% because the liquidity cost no longer pays.
- Use delta-neutral convertible baskets when you expect volatility and range-bound stocks.
- Use "equity falls, spread widens" as the main risk: the floor is not static.
- Read the prospectus: protections for M&A, dividends, change of control can matter more than the headline premium.

## Worked Example
Delta-hedged position (writer's illustration, consistent with the guide's mechanics): convertible with conversion ratio 1,000 per EUR 100,000 nominal (conversion price EUR 100), share price EUR 100, delta 50%, price 100.0.
1. Short `0.50 × 1,000 = 500` shares to be delta-neutral.
2. Share rises to EUR 110; delta moves to 70%. To re-hedge, short `0.70 × 1,000 = 700`, i.e. sell 200 more shares at EUR 110 (EUR 22,000 proceeds).
3. Share falls back to EUR 100; delta back to 50%: buy back 200 shares at EUR 100 (EUR 20,000).
4. Gain on the rebalancing round trip `= 22,000 − 20,000 = EUR 2,000`, ignoring option price changes and funding. 
Interpretation: the trade profits from the oscillation, not the direction; the more volatile the range, the greater the profit. The delta numbers 50% and 70% are assumptions, not market quotes.

## Anti-patterns
- Treating the bond floor as fixed when the issuer is weak or unrated.
- Holding a convertible far above the conversion price for the equity move: the instrument is less liquid than the stock.
- Converting early and losing the option's time value and accrued coupon.
- Ignoring that mandatory convertibles have no floor protection at maturity.
- Delta-hedging without watching borrow costs, dividends and gamma.
- Forgetting prospectus clauses on extra dividends and M&A.

## Practitioner Notes
- Convertibles offer maturities up to 8-10 years, a sector spread (cyclical/defensive, value/growth) and rating range hard to match with listed options.
- The sponsored insert (Nordea Flexible Fixed Income Fund, launched May 2013, a multi-asset team "risk balancing" approach) promotes a liquid unconstrained strategy: global universe, tactical risk reduction rather than return chasing, defensive currencies and alternative strategies, 100% of assets liquidable within a week. Treat as sponsor material and verify independently; its 2018 claim is about drawdown resilience versus portfolios concentrated in EM and HY.
- Correlation between risky and safe bonds rising makes alternative return sources more valuable, per the sponsor.

## Key Takeaways
1. A convertible is a bond floor plus an equity call; the investor decides conversion.
2. Premium falls as parity rises; delta rises from near 0 to 100%.
3. Balanced convertibles offer the best asymmetry; quasi-equity zone has lost it.
4. Early conversion wastes the option's time value; take profits on the convertible or switch to equity.
5. Delta-neutral hedging monetizes volatility (gamma trade).
6. Credit and equity are correlated: falling stock widens spreads and erodes the floor.
7. Prospectus clauses on dividends, M&A, change of control and anti-dilution protect holders.

## Connects To
- **ch06** (`cfasi-fixed-income-guides`): convertible valuation basics (conversion premium, payback period).
- **ch13**: HY credit risk behind busted convertibles.
- **ch15**: other hybrid/equity-like instruments.
- **`hull-derivatives`**: option Greeks and hedging.
- **`passarelli-option-greeks`**: delta, gamma and volatility trading.
- **`cfa-derivatives`**: option replication and arbitrage.
