# Chapter 2: The Main Risks of Fixed Income Securities
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 2 (I principali rischi dei titoli a reddito fisso) | Denis Manzi, CFA

## Core Idea
A bond is exposed to a dozen distinct risks, and each is driven by a specific contract feature from ch01. Interest rate risk dominates price behavior, but the sensitivity is modulated by maturity, coupon, embedded options and the yield level. Credit, call, reinvestment, liquidity, currency, volatility and inflation risks each need their own diagnostic. Map every position to the risks it carries before judging its yield.

## Frameworks Introduced
- **Coupon vs required yield rule (price anchoring)**
  - When to use: to sign the price move of any fixed-rate bond against new-issue yields.
  - How: coupon = market yield, price = 100; coupon < yield, price < 100; coupon > yield, price > 100. A rational investor will not hold a bond yielding less than an identical new one, so price adjusts until yields match.
  - Why it works: arbitrage across identical-risk bonds. Failure mode: ignores credit and liquidity differences between "identical" bonds.
- **Drivers of interest-rate sensitivity (ceteris paribus)**
  | Feature | Effect on rate sensitivity |
  |---|---|
  | Longer maturity | Higher |
  | Lower coupon | Higher |
  | Lower yield level | Higher |
  | Issuer call option | Lower (price = straight bond price minus call value; call value rises as rates fall, capping upside) |
  | Holder put option | Lower to rate increases (price = straight price plus put value) |
  | Floating coupon | Much lower; residual risk comes from reset lag, margin changes and caps |
- **Floater sensitivity checklist**: (1) reset interval (longer gap between resets = more exposure to a stale coupon); (2) margin (fixed at issue; if the market margin required for the issuer moves, price moves); (3) cap (when the reference rate would push the coupon above the cap, the floater behaves like a fixed bond and its price falls).
- **Parallel vs non-parallel curve shift test**: reprice the portfolio under both. Barbell (5y + 10y zeros, 50/50) versus bullet (7.5y zero): equal loss under a parallel shift, different loss under a twist. This is curve (yield-curve) risk.
- **Credit risk decomposition**: (1) default risk; (2) credit spread risk (spread over a risk-free bond widens); (3) downgrade risk (rating change, especially across the investment grade / high yield boundary, which can force selling by constrained holders).
- **Volatility-option rule**: implied rate volatility up raises option values. Callable bond value = straight bond minus call, so higher vol lowers it. Putable bond value = straight bond plus put, so higher vol raises it.

## Key Concepts
- **Interest rate risk** — price moves opposite to yield; the dominant risk of fixed-rate bonds.
- **Yield curve risk (rischio di curva)** — risk that rates at different maturities move by different amounts.
- **Parallel shift** — all maturities move by the same number of basis points.
- **Default (insolvency) risk** — issuer cannot or will not pay.
- **Credit spread risk** — widening of the yield gap against a risk-free benchmark (US Treasury, Bund) hurts price even without default.
- **Downgrade risk** — rating cut; can trigger forced selling by investors with rating floors.
- **Investment grade (IG)** — Baa3 (Moody's) / BBB- (S&P, Fitch) and above; below is high yield (HY) or speculative.
- **Call risk / prepayment risk** — early redemption (also in MBS and ABS) forces reinvestment at lower rates, makes cash flows unknowable, and caps price appreciation.
- **Reinvestment risk** — coupons and redemptions reinvested at lower yields; zero-coupon bonds minimize it, high-coupon callable/amortizing paper maximizes it.
- **Liquidity risk** — difficulty selling quickly near the indicative price; proxy is the bid-ask spread (tighter = more liquid).
- **Currency risk** — foreign-currency bond returns are eroded if the currency depreciates against the investor's.
- **Interest-rate volatility risk** — exposure of option-bearing bonds to changes in implied vol.
- **Event risk** — hard-to-predict shocks (natural disaster, takeover) that stop the issuer meeting the indenture.
- **Legal risk** — change of law, e.g. a new tax regime.
- **Inflation risk** — rising prices erode the purchasing power of fixed cash flows.

## Formulas & Reference Tables
- Price of an annual bond: `P = Σ C/(1+y)^t + F/(1+y)^N`, with C = coupon, y = yield, F = face value, N = years.
- Zero-coupon sensitivity (rule of thumb): `ΔP/P ≈ −T × Δy` for a zero with T years to maturity, small Δy.
- Barbell loss under a parallel +1 pp shift: `0.5×5 + 0.5×10 = 7.5` points; bullet at 7.5 years loses 7.5 points as well.
- Foreign-currency annualized return in domestic currency: `(Sale value in EUR / Cost in EUR)^(1/T) − 1`.
- Rating scale (investment grade down to speculative), with indicative default probabilities in the source (Credit Suisse): Aaa/AAA 0.01%, Aa2/AA 0.03%, A2/A 0.07%, Baa2/BBB 0.22%, Baa3/BBB- 0.39%, Ba2/BB 1.17%, B1/B+ 3.51%, Caa1/CCC 18.27%.
- Option decomposition: `P(callable) = P(straight) − V(call)`; `P(putable) = P(straight) + V(put)`.

## Mental Models
- Use "coupon vs yield" to predict whether a bond trades above or below par before pricing it.
- Use the barbell/bullet comparison when a client asks if "same average maturity" means "same risk": it does not unless the curve moves in parallel.
- Use "bid-ask spread" as a free liquidity gauge; widen your required spread for wide-quote bonds.
- Use "a callable is short an option held by the issuer": you give up the upside and keep the downside.
- Use floaters when you fear rising rates, but check cap and reset frequency first.

## Worked Example
Currency risk on a USD zero-coupon bond. Inputs: buy USD 100 face at 90% (cost USD 90), 5 years, redeemed at 100.
1. USD yield: `(100/90)^(1/5) − 1 = 2.13%`.
2. EUR cost at EUR/USD 1.15 (USD per EUR): `90/1.15 = 78.26` EUR.
3. Redemption at EUR/USD = 1.15: 86.96 EUR, so return `(86.96/78.26)^(1/5) − 1 = 2.13%`; at 1.00: 100 EUR, return 5.02% (source rounds to 5.025%); at 1.30: 76.92 EUR, return −0.34%.
Interpretation: a fixed 2.13% USD yield becomes anything from −0.34% to 5.02% in EUR; the bond's own yield is the smaller driver.

Price anchoring check: a 3% annual 10-year bond when new issues yield 4% prices at 91.89 (source writes about 91.86); at 2% it prices at 108.98 (source about 108.97). **⚠ Correction**: minor rounding in the source figures.

## Anti-patterns
- Reading a rating as a default probability that does not move; spread and downgrade risk hit prices long before default.
- Comparing a callable bond's yield to a bullet's without adjusting for call value.
- Assuming a floater has zero rate risk (reset lag, margin and cap remain).
- Hedging only duration and ignoring curve shape.
- Ignoring currency effects on foreign bonds in a "safe" yield-pickup trade.
- Source rating table shows B2 and B3 both as "B-"; the correct S&P/Fitch mapping is B2 = B, B3 = B-. **⚠ Correction**.

## Practitioner Notes
- Rating thresholds matter operationally: many mandates forbid sub-IG paper, so a fall to BB+ produces forced sales and a price gap.
- Rate sensitivity is lower at low yield levels only in the sense of the ceteris-paribus rule; in practice low yields with long maturity are dangerous because convexity works against you (see ch06).
- The guide treats MBS and ABS as call-type risks, because borrowers prepay when rates fall.

## Key Takeaways
1. Price and yield move in opposite directions; coupon-versus-yield decides premium or discount.
2. Longer maturity and lower coupon raise rate sensitivity; embedded calls reduce upside, puts reduce downside.
3. Yield curve risk exists even when duration is matched; test non-parallel shifts.
4. Credit risk has three layers: default, spread widening, downgrade.
5. Call and reinvestment risks hit when rates fall; floaters help when rates rise.
6. Liquidity is measured by bid-ask spread and execution impact.
7. Foreign currency can overwhelm a small bond yield.
8. Implied rate volatility is bad for callables and good for putables.

## Connects To
- **ch01**: contract features (call, put, floater, cap) that create these risks.
- **ch03**: where the risks concentrate by issuer type (sovereign, corporate, bank, securitized).
- **ch06**: quantifies rate and credit risk with duration, convexity and spread measures.
- **ch09**: unconstrained funds as a response to rate risk.
- **`cfa-fixed-income` ch05**: duration, convexity and the CFA treatment of the same risks.
