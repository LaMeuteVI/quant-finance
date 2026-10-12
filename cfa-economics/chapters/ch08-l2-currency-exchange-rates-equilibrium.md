# Chapter 8: Currency Exchange Rates: Understanding Equilibrium Value
> **Source**: CFA Program Curriculum 2022, Level II, Reading 6 · Economics | Michael R. Rosenberg, William A. Barker, PhD, CFA

## Core Idea
Exchange rates are close to a random walk in the short run, so the toolkit is not for point forecasts but for judging long-run equilibrium value and sizing currency risk. The only parity condition enforced by arbitrage is covered interest rate parity (CIP); uncovered interest rate parity (UIP), forward rate parity, purchasing power parity (PPP) and the international Fisher effect are long-horizon anchors that fail over months and years. That failure is the economic reason the FX carry trade earns a premium, and also why it crashes. Flows (current account, capital account), the monetary-fiscal policy mix, intervention and capital controls drive the short and medium run, and a short list of macro-financial symptoms precedes most currency crises.

## Learning Outcomes Covered
- Calculate and interpret bid-offer spreads (spot, forward) and list what widens them
- Identify triangular arbitrage and compute its profit from bid-offer quotes
- Explain spot and forward rates; compute forward premium or discount
- Mark a forward contract to market
- Explain and relate CIP, UIP, forward rate parity, PPP (absolute, relative, ex ante) and the international Fisher effect
- Evaluate spot, forward, PPP and UIP as forecasters; approaches to long-run fair value
- Describe the carry trade and compute its profit
- Explain how current-account and capital flows, monetary and fiscal policy (Mundell-Fleming, monetary and portfolio balance models), intervention and capital controls affect exchange rates
- Describe warning signs of a currency crisis

## Frameworks Introduced
- **P/B quotation and bid-offer rule**: a quote `P/B` is units of price currency per 1 unit of base. Bid = price at which the dealer buys the base; offer = price at which the dealer sells it. Rule of thumb: every bid or offer refers to the currency in the denominator. When you buy the base you pay the offer (the client "pays the offer"); when you sell the base you hit the bid.
  - Spread drivers: interbank liquidity of the pair, time of day (tightest in the London-New York overlap, roughly 8-11 a.m. New York time), volatility and event risk, transaction size, dealer-client relationship (and, marginally, client credit). For forward points add the tenor (longer means less liquidity, more counterparty and interest-rate risk, wider spread). Interbank dealing size is at least 1 million of base; a pip is 0.0001 (0.01 for JPY).
- **Two arbitrage constraints on dealer quotes**: (1) a dealer bid cannot exceed the interbank offer and a dealer offer cannot be below the interbank bid; (2) a dealer's cross-rate bid must not exceed the implied interbank cross offer, and the dealer's cross offer must not be below the implied interbank cross bid.
  - **Implied cross bid/offer**: choose the algebra so the common currency cancels (`A/C = A/B × B/C`), multiply bids by bids and offers by offers; if a quote must be inverted, `1/offer` becomes the bid and `1/bid` the offer.
  - **Triangular arbitrage**: compare the dealer's cross quote with the implied interbank cross. If the dealer sells the base below the interbank bid, buy base from the dealer (pay the dealer offer) and sell it in the interbank market (hit the interbank bid); if the dealer buys the base above the interbank offer, buy it interbank and sell to the dealer. Profit per unit of base is the gap. Violations vanish within moments; algorithms enforce them.
- **Covered interest rate parity (CIP)**: a currency-hedged foreign deposit earns the domestic risk-free rate.
  - Formulation: `(1 + i_d τ) = S_(f/d) (1 + i_f τ) / F_(f/d)`, so `F_(f/d) = S_(f/d) (1 + i_f τ)/(1 + i_d τ)`, `τ = days/360` for Libor-type deposits (Actual/360; GBP uses 365). In P/B notation: `F = S (1 + i_P τ)/(1 + i_B τ)`, base currency in the denominator.
  - Premium or discount: `F − S = S × (i_P − i_B) τ / (1 + i_B τ)`; approximately `(F − S)/S ≈ i_P − i_B` (annualized, one year). The base is at a forward premium if and only if `i_P > i_B`. The higher-yielding currency is at a forward discount.
  - When to use: pricing forwards, backing out an implied interest rate (given S, F and one rate), checking dealer points. How: put the base-currency rate in the denominator, rate of the price currency in the numerator, use Actual/360. Why it works: if violated, borrow where hedged funding is cheapest, lend where it pays most, lock the exchange rate with a forward; riskless profit, so quotes snap back. Failure mode: stress (balance sheet constraints, cross-currency basis), transaction costs, instruments that are not identical in liquidity or default risk.
- **Forward points to all-in rate**: `F = S + points/10,000` (JPY pairs `/100`); points are already scaled to maturity, not annualized. Use the bid points with the spot bid (sell base) and the offer points with the spot offer (buy base). Broken dates are interpolated.
- **Mark-to-market of a forward** (4 steps): (1) write the offsetting position (same size, opposite direction in the original base); (2) find today's all-in forward rate for the remaining tenor, using the bid if you sell the base and the offer if you buy it; (3) settlement cash flow = notional (in base) × (original forward − new rate) with sign by whether you were long or short the base; it is in the price currency; (4) discount it at the price-currency rate over the remaining days. At initiation MTM is zero.
- **Uncovered interest rate parity (UIP)**: the expected return on an unhedged foreign deposit equals the domestic return. The text writes the return as `(1 + i_f)(1 − %ΔS_(f/d)) − 1 ≈ i_f − %ΔS_(f/d)`; the exact form is `(1 + i_f)/(1 + %ΔS_(f/d)) − 1`, because the foreign proceeds are divided by the new spot (f per d). Parity: `%ΔS^e_(f/d) = i_f − i_d` (high-rate currency expected to depreciate). Requires risk-neutral speculators; not enforced by arbitrage, since no trade locks a riskless profit. It cannot hold simultaneously for `S_(f/d)` and `1/S_(f/d)` (approximation).
- **Forward rate parity**: CIP and UIP together give `F_(f/d) = S^e_(f/d)`: the forward is an unbiased (not perfect) predictor of the future spot. It holds only if UIP holds, so it is a poor short-run forecaster. Forecast ladder: current spot as forecast = random-walk view (needs no UIP); forward as forecast = CIP + UIP; PPP = long-run only.
- **Purchasing power parity (PPP)**, three versions built on the law of one price `P^x_f = S_(f/d) P^x_d`:
  - Absolute: `S_(f/d) = P_f/P_d`; requires all goods tradable, identical baskets and weights, no frictions; rarely true (persistent departures).
  - Relative: `%ΔS_(f/d) ≈ π_f − π_d` if frictions are constant; the high-inflation currency depreciates.
  - Ex ante: `%ΔS^e_(f/d) = π^e_f − π^e_d` (expected, forward-looking). Evidence: no relation at 1 year, strong at 6+ years; a PPP gap closes about half in 3 to 5 years.
- **Fisher effect and international Fisher effect**: `i = r + π^e` (add a risk premium for risky currencies). If `%ΔS^e = i_f − i_d` (UIP) and `%ΔS^e = π^e_f − π^e_d` (ex ante PPP) then `r_f − r_d = 0`: real interest rate parity. International Fisher effect: `i_f − i_d = π^e_f − π^e_d` (needs ex ante PPP and real rate parity; not absolute PPP). Some authors call UIP the "international Fisher effect"; this reading reserves the name for the nominal-rate/inflation link. Emerging currencies carry a risk premium so their real rates exceed those in developed markets.
- **Parity chain**: CIP: nominal spread = forward premium or discount. UIP: nominal spread = expected `%ΔS`. CIP + UIP: forward unbiased. Ex ante PPP: expected `%ΔS` = expected inflation differential. Fisher + real rate parity: nominal spread = inflation differential. If all held, expected `%ΔS` = forward discount = nominal spread = inflation differential and no consistent currency profit exists.
- **FX carry trade**: go long the high-yield currency, finance in a low-yield funding currency, hold unhedged. Profit if UIP fails. Steps: borrow funding currency at t0, convert at spot, invest, liquidate at t1, convert back, repay the loan. Return = yield spread + currency change (+ asset change). Risk profile: steady accrual of the spread, sudden capital loss when volatility spikes (flight to quality, stop-losses, leverage, crowded unwinds). Returns are negatively skewed and fat-tailed (more peaked than normal). Persistence argued as compensation for a risk premium in high-yield economies; examples: yen carry 1995-2007 and its 1998 unwind, Turkish lira 2002-10 (profit came mostly from carry because the central bank resisted appreciation).
- **Current account and exchange rate channels**: (1) flow supply/demand (surplus raises demand for the currency; pass-through is often incomplete, about 0.5% rise in import prices per 1% depreciation, and demand responses lag by years, so a large depreciation may be needed); (2) portfolio balance (surplus countries accumulate claims, which they may later trim); (3) debt sustainability (persistent deficits raise net external debt/GDP, shifting the market's view of long-run fair value down). Short and intermediate run: capital and financing flows dominate because goods prices adjust slowly, financial markets reallocate stocks of wealth instantly, and expected currency moves trigger large flows; the US dollar rose in the early 1980s and late 1990s despite widening deficits because capital flowed in.
- **Real yield spread and capital flows**: exchange rates tracked US-foreign real yield spreads (1977-90, 1993-98). Policy of higher rates, lower expected inflation, lower deficits, reforms and a lower risk premium raises a currency gradually and can sustain carry profits for years. Equity-currency correlation is unstable (long-run near zero; negative since the global financial crisis because the dollar acts as a safe haven in risk-off phases).
- **Mundell-Fleming (short run, demand only, slack in output)**: with floating rates and high capital mobility, restrictive monetary policy and expansionary fiscal policy appreciate the currency (higher rates attract capital); expansionary monetary with restrictive fiscal depreciates it; both loose or both tight is indeterminate. With low capital mobility, the effect runs through trade: both expansionary depreciates; both restrictive appreciates; mixed is indeterminate. High mobility fits developed markets; low mobility fits restricted emerging markets. Germany 1990-92 (loose fiscal, tight Bundesbank) is the classic case.
- **Monetary approach and Dornbusch overshooting**: pure monetary model: money up X% means prices up X%, and with PPP the currency falls proportionally (output fixed, interest rates ignored). Dornbusch (1976): prices sticky in the short run but flexible in the long run; a money increase cuts the interest rate, capital flows out, and the currency overshoots below its new long-run PPP level, then appreciates back along the long-run path.
- **Portfolio balance approach (long run fiscal)**: growing deficits expand the bond supply; investors hold it only for a higher expected return: higher rates or risk premium, or an immediate depreciation that promises later appreciation. Integrated view: expansionary fiscal policy under high mobility is positive for the currency short run (higher real rates) and negative long run once debt looks unsustainable (monetization or later consolidation).
- **Intervention and capital controls**: inflows driven by pull factors (better inflation, fiscal position, liberalization, privatization, reforms) and push factors (low rates in developed markets, portfolio allocation trends). Surges preceded the 1992-93 ERM crisis, the 1994 Mexican peso crisis and the 1997-98 Asian crisis. Tools: sterilized or unsterilized intervention, taxes (Brazil), unremunerated reserve requirements (Thailand 2006, 30% deposit), ownership caps, repatriation limits (Ukraine 2015), multiple rates (Venezuela, creating a black market). Effectiveness: developed markets' reserves are small relative to daily turnover, so effect is limited (a central bank can weaken its own currency without limit, but this undermines domestic monetary policy); emerging markets' reserves are large relative to local turnover, so intervention lowers volatility and may move levels; capital controls leak (trade finance, black markets, circumvention) and can divert flows to other countries. The IMF accepts controls as a legitimate tool in some circumstances.
- **Currency crisis early-warning list** (nine factors): liberalized capital markets; large capital inflows relative to GDP, especially short-term foreign-currency funding; banking crisis before or alongside; fixed or partially fixed regime; sharp fall in FX reserves; currency strongly above its historical mean; deteriorating terms of trade (exports relative to imports); rising broad money growth and M2/bank reserves; higher inflation. Two schools: fundamentals-driven versus self-fulfilling sentiment and contagion. A good system: strong hit rate with few false alarms, timely data, broad indicator set, early signals. Iceland 2008 (bank assets more than 14 times GDP, foreign-currency deposits, maturity mismatch, krona down more than 40% in H1 2008, rates to 18%, capital controls, IMF aid) is the template.

## Key Concepts
- **Base and price currency**: in `P/B`, B is the unit being priced and P is the currency it is priced in.
- **Pip and interbank market**: smallest standard quote increment (0.0001; 0.01 for yen) and the wholesale dealer network (1 million+ units).
- **Implied cross rate**: the A/C rate inferred from A/B and C/B; any dealer quote outside it creates a triangular arbitrage.
- **Forward points**: scaled difference between forward and spot; positive means the base is at a premium.
- **All-in forward rate**: spot plus scaled forward points.
- **Covered interest arbitrage**: borrowing, lending and forward cover that locks a riskless profit when CIP is violated.
- **Uncovered position**: foreign exposure left unhedged, earning the yield plus whatever the spot does.
- **Risk-neutral investor**: ranks investments by expected return alone; UIP assumes enough of them.
- **Real interest rate parity**: equal real rates across countries, the product of UIP and ex ante PPP.
- **Funding currency**: the low-yield currency a carry trader borrows.
- **Crash risk**: carry's negatively skewed, fat-tailed return distribution caused by crowded, leveraged unwinds.
- **Pass-through**: share of an exchange-rate change that shows up in traded-goods prices; often partial, often lagged.
- **Debt sustainability channel**: rising net external debt lowers the market's estimate of long-run fair value.
- **Overshooting**: short-run move of the exchange rate beyond its long-run level when goods prices are sticky.
- **Capital controls**: legal or tax limits on cross-border flows to blunt surges or protect the currency.
- **Safe-haven currency**: one that appreciates in risk-off episodes (US dollar, yen, Swiss franc), driving negative correlation with equities.

## Formulas & Reference Tables
- Cross: `A/C = (A/B)(B/C)`; inverted quote: bid' = `1/offer`, offer' = `1/bid`
- CIP: `F_(P/B) = S_(P/B) (1 + i_P τ)/(1 + i_B τ)`; `F − S = S (i_P − i_B) τ/(1 + i_B τ)`; `τ = days/360`
- Implied rate: `1 + i_P τ = (F/S)(1 + i_B τ)` (solve for the unknown deposit rate)
- Forward from points: `F = S + points/10,000` (JPY pairs `/100`)
- MTM of a forward: long base `PV = N (F_new − F_orig)/(1 + i_P × days_remaining/360)`; short base `PV = N (F_orig − F_new)/(1 + i_P × days_remaining/360)`; `F_new` is the all-in rate for the offsetting trade (bid to sell base, offer to buy base); discount at the price-currency rate
- Unhedged foreign deposit (f/d quote): `(1 + i_f)/(1 + %ΔS_(f/d)) − 1 ≈ i_f − %ΔS_(f/d)`
- UIP: `%ΔS^e_(f/d) = i_f − i_d`; forward rate parity: `F_(f/d) = S^e_(f/d)`
- PPP: absolute `S_(f/d) = P_f/P_d`; relative `%ΔS ≈ π_f − π_d`; ex ante `%ΔS^e = π^e_f − π^e_d`
- Fisher: `i = r + π^e`; `r_f − r_d = (i_f − i_d) − (π^e_f − π^e_d)`; international Fisher: `i_f − i_d = π^e_f − π^e_d`
- Product to growth: `X = YZ ⇒ %ΔX ≈ %ΔY + %ΔZ`; `X = Y/Z ⇒ %ΔX ≈ %ΔY − %ΔZ`
- Carry return (investor currency d, f per d quotes): `(1 + i_f) S_(f/d,0)/S_(f/d,1) − (1 + i_d)`, approximately `i_f − i_d − %ΔS_(f/d)`

| Parity condition | Enforced by arbitrage? | Holds short run? | Needed for |
|---|---|---|---|
| CIP | Yes | Yes (except stress) | Forward pricing |
| UIP | No | Rarely | Carry-trade logic, forward as forecast |
| Forward rate parity | No (CIP + UIP) | Rarely | Unbiased forward forecast |
| Absolute PPP | No | No | Level of fair value |
| Relative / ex ante PPP | No | Only at 6+ years | Long-run drift |
| Real rate parity | No | Rarely | International Fisher effect |

| Policy mix (floating rates) | High capital mobility | Low capital mobility |
|---|---|---|
| Expansionary monetary + expansionary fiscal | Indeterminate | Depreciates |
| Expansionary monetary + restrictive fiscal | Depreciates | Indeterminate |
| Restrictive monetary + expansionary fiscal | Appreciates | Indeterminate |
| Restrictive monetary + restrictive fiscal | Indeterminate | Appreciates |

## Mental Models
- **Use CIP to price and to arbitrage, never to forecast**: the forward carries the rate gap; a hedged deposit earns the home rate.
- **Use PPP and ex ante inflation gaps for a 5-year-plus fair-value anchor, not for next quarter**: the gap closes about half in 3 to 5 years.
- **Use UIP failure as the carry thesis, and size carry for the crash**: small steady income, rare large loss; leverage and low-vol complacency are the tells.
- **In the short run follow capital, not trade**: real-rate spreads, risk appetite and flows move FX before the current account does; trade imbalances matter when debt sustainability is questioned.
- **Ask two questions before reading a policy mix**: floating or pegged, and how mobile is capital? High mobility means rates dominate (tight money, loose fiscal is bullish); low mobility means trade dominates (loose both is bearish).
- **Treat crises as leveraged-positioning events**: look for short-term foreign-currency debt, falling reserves, an overvalued fixed rate, and a banking sector already weak.

## Worked Example
All numbers recomputed.

**1. Implied cross and triangular arbitrage.** Interbank USD/EUR 1.1649/1.1651, JPY/USD 105.39/105.41. JPY/EUR offer `= 105.41 × 1.1651 = 122.813`, bid `= 105.39 × 1.1649 = 122.769` (so about 122.77/122.81). JPY/CAD from CAD/USD 1.3199/1.3201: invert to USD/CAD `1/1.3201 = 0.75752` (bid), `1/1.3199 = 0.75763` (offer); JPY/CAD bid `105.39 × 0.75752 = 79.84`, offer `105.41 × 0.75763 = 79.86`. A dealer quoting JPY/CAD 79.81/79.83 offers CAD below the interbank bid: buy CAD from the dealer at 79.83, sell interbank at 79.84, gain JPY 0.01 per CAD. A dealer quote of 79.82/79.87 breaches nothing (bid not above 79.86, offer not below 79.84).

**2. CIP forward and why the quote is arbitrageable.** USD/EUR spot 1.1650 (EUR base), 1-year `i_USD = 4%`, `i_EUR = 1%`: `F = 1.1650 × 1.04/1.01 = 1.1996` (EUR at a forward premium, USD at a discount). If a dealer quotes 1.1900, the euro is too cheap forward: borrow EUR 1,000,000 at 1%, convert to USD 1,165,000, invest at 4% to USD 1,211,600, sell USD forward at 1.1900 to receive EUR 1,018,151 versus a loan payoff of EUR 1,010,000: riskless gain EUR 8,151. Forward premium on the Libor example (CAD/AUD 0.9000, 270 days, `i_AUD = 1.47%`, `i_CAD = 0.41%`, AUD base): `0.9000 × 0.75 × (0.0041 − 0.0147)/(1 + 0.0147 × 0.75) = −0.0071` (AUD at a discount because AUD rates are higher). Practice case: INR/GBP 79.5093, `i_INR = 7.52%`, `i_GBP = 5.43%`: `F − S = 79.5093 × (0.0752 − 0.0543)/1.0543 = +1.576` (GBP at a premium).

**3. Points to all-in rate and forward MTM.** Selling EUR 3 months forward uses the spot bid and bid points: `1.1649 − 15.9/10,000 = 1.16331`. Mark-to-market: long GBP 10m at 1.8100 AUD/GBP, three months from settlement, spot 1.8210/1.8215, points +130/+140. To offset you sell GBP, so use the bid: `1.8210 + 0.0130 = 1.8340`. Settlement cash flow `10,000,000 × (1.8340 − 1.8100) = +AUD 240,000`; discount at 3-month AUD rate 2.40%: `240,000/(1 + 0.024 × 90/360) = AUD 238,569`. Short NZD 10m forward at 0.7900 USD/NZD, spot 0.7825/0.7830, points −12.1/−10.0, USD rate 0.31%: you buy NZD, so use the offer: `0.7830 − 0.0010 = 0.7820`; cash flow `10,000,000 × (0.7900 − 0.7820) = +USD 80,000`; PV `= 80,000/(1 + 0.0031 × 0.25) = USD 79,938`. A different trade: short USD 10m forward at 0.7900 (a long-USD hedge) closed three months early. You buy USD, which means selling the NZD base, so use the bid: `0.7825 − 0.00121 = 0.78129`. In NZD, contracted receipt `10m/0.7900 = 12,658,228`, offsetting payment `10m/0.78129 = 12,799,345`, difference `−NZD 141,117`, PV at NZD 3.31% `= −NZD 139,959` (a loss because USD strengthened). Note the cash flow currency changes with which currency you hold the exposure in.

**4. UIP, forward as forecast, PPP.** JPY/AUD 71.78, `i_AUD = 3%`, `i_JPY = 1%`: UIP expects AUD to fall about 2% (to roughly 70.34 by the approximation; exactly `71.78 × 1.01/1.03 = 70.39`, which is also the CIP forward since `71.78 − 1.394 = 70.386`). Forward rate parity then says `S^e = F`. Unhedged return check: foreign deposit at 10%, home 4%, `S_(f/d)` rising 6% (domestic currency appreciates): exact `1.10/1.06 − 1 = 3.77%` versus approximation `10% − 6% = 4%` (UIP holds approximately); the error grows with the product `i × %ΔS`. PPP: foreign inflation 9%, domestic 5%: `%ΔS_(f/d) ≈ +4%` (exact `1.09/1.05 − 1 = 3.81%`), the foreign currency weakens. A currency 10% overvalued by PPP needs the quote to fall 10% (or relative inflation to adjust) to return to parity.

**5. Carry trade (recomputed, and a source inconsistency).** Yen investor funds at JPY 0.10%, buys one-year AUD at 1.70%. JPY/USD 105.40 to 104.60; USD/AUD 0.6810 to 0.6850. Cross JPY/AUD `105.40 × 0.6810 = 71.78`, one year later `104.60 × 0.6850 = 71.65`. Unhedged AUD deposit in JPY: `1.017 × 71.65/71.78 − 1 = 1.52%`; net of funding `1.52% − 0.10% = 1.42%` (exact 1.4209%). **⚠ Correction**: the source lists answer B as "+1.53%" while its own solution derives 1.42%; the correct number is 1.42%. Second trade: borrow USD at 0.80%, invest EUR at 2.20%; `S(EUR/USD) = 1.3200 × 0.6506 = 0.8588`, projected `1.3151 × 0.6567 = 0.8636`; gross `0.8588 × 1.022/0.8636 − 1 = 1.628%` (the text rounds to 1.632%), net `1.628% − 0.80% = 0.83%`.

**6. Forecast with CIP and implied rate.** JPY/GBP spot 129.67, `i_JPY = 0.10%`, `i_GBP = 3.00%` (one year): the one-year forward is `129.67 × 1.001/1.03 = 126.02`; under UIP the expected spot equals 126.02, i.e. sterling expected to fall about 2.8% against the yen (`126.02/129.67 − 1`). Three-month USD/GBP with Libors 0.33% (USD) and 0.58% (GBP): `F = 1.2303 × (1 + 0.0033/4)/(1 + 0.0058/4) = 1.2295`, a forward discount of 0.0008; the implied EUR Libor from positive GBP/EUR points is below GBP Libor.

## Anti-patterns
- Using a forward premium or discount as a forecast of where spot will go; it is an interest differential.
- Putting the price-currency rate in the denominator of CIP (the base-currency rate belongs there).
- Quoting the cross bid as the product of the "wrong sides" (bid times offer) or forgetting to swap bid and offer on inversion.
- Treating UIP, forward rate parity or absolute PPP as reliable over months; only CIP is arbitrage-enforced.
- Running carry with leverage and no tail hedge because realized volatility has been low.
- Reading a trade deficit as an immediate sell signal; capital inflows can lift the currency for years.
- Applying the Mundell-Fleming policy-mix table without checking capital mobility and regime.
- Assuming central bank intervention in a major pair has lasting effect, or that capital controls stop all flows.

## Exam Focus & Traps
- Offer when you buy the base, bid when you sell it; dealers cover the client trade interbank and earn the spread (one pip on EUR 1 million is USD 100).
- Triangular arbitrage questions: compute implied bid and offer (inversion swaps bid and offer) and compare with the dealer's quote.
- Forward points for the premium sign: positive points mean base at a premium and `i_P > i_B`; the high-yield currency is at a forward discount.
- MTM: pick the correct side (bid to sell base, offer to buy base), identify the currency of the cash flow, discount with that currency's rate over the remaining period only.
- Forward is an unbiased predictor only if CIP and UIP hold; current spot as forecast means random walk; do not choose "inflation differential" for a one-year forecast.
- UIP vs CIP: only CIP is a no-arbitrage condition; the carry trade is profitable when UIP fails; real interest rate parity is not required for forward rate parity.
- International Fisher effect needs ex ante PPP and real rate parity; absolute PPP is not required.
- Persistent deficit currencies do not weaken immediately (long lags, financing flows); an exam statement that exchange rates "immediately correct the trade imbalance" is wrong.
- Monetary models cite inflation and price levels; risk premiums belong to the portfolio balance approach.
- Early-warning signals: reserves decline (not rise), money growth rises, currency overvalued; a rising reserve balance lowers crisis risk.
- Emerging market intervention succeeds more often than developed market intervention because reserves are large relative to local FX turnover.
- **⚠ Correction (source Example 7 Q4)**: the keyed result in the text is 1.42% (answer option printed as 1.53%); recompute and expect 1.42%.
- **Note (source Example 4 approximation)**: the source states `%ΔS = i_f − i_d` for both `S_(f/d)` and its inverse; it cannot hold for both. Use the exact form when the question gives precise percentages.

## Key Takeaways
1. All quotes are `price/base`; bid and offer refer to the base; implied crosses multiply bids with bids and offers with offers after unit cancellation.
2. CIP is arbitrage-enforced: `F = S(1 + i_P τ)/(1 + i_B τ)`; the high-yield currency is at a forward discount.
3. Forward points are scaled to maturity; MTM discounts the settlement cash flow with the price-currency rate.
4. UIP, forward rate parity and PPP are long-run anchors that fail short run; the international Fisher effect adds real rate parity.
5. Carry trades monetize UIP failure and carry negatively skewed, fat-tailed crash risk.
6. Capital flows dominate the short run; current-account imbalances act through flow, portfolio balance and debt-sustainability channels with long lags.
7. Policy mix works through capital mobility: tight money plus loose fiscal strengthens a currency when capital is mobile; Dornbusch adds overshooting; portfolio balance flips fiscal's long-run sign.
8. Intervention is weak in developed markets, stronger in emerging ones; capital controls leak; watch the nine crisis indicators, especially short-term foreign debt and falling reserves.

## Connects To
- **ch07**: Level I quote conventions, CIP derivation, regimes, Marshall-Lerner; this chapter adds parity, carry and policy-driven equilibrium.
- **ch06**: trade and capital flows underlying the balance of payments channels.
- **ch05**: central bank and fiscal policy transmission behind the Mundell-Fleming table.
- **ch10**: regulatory competition and arbitrage, prudential regulation and the cost-benefit logic behind capital controls and intervention.
- **`cfa-fixed-income`**: sovereign yield spreads and real rates drive currency carry.
- **`cfa-derivatives`**: forward pricing, CIP-based FX forwards and swaps.
- **`cfa-asset-allocation-cme`**: currency return forecasting and hedging decisions.
