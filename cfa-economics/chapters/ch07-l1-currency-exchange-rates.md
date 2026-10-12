# Chapter 7: Currency Exchange Rates
> **Source**: CFA Program Curriculum 2020, Level I, Reading 18 · Economics | William A. Barker, Paul D. McNelis, Jerry Nickelsburg

## Core Idea
An exchange rate is the price of one currency (the base) in units of another (the price currency); nearly every error in FX arithmetic comes from losing track of which is which. Spot, cross and forward rates are tied together by arbitrage: crosses by triangular arbitrage, forwards by covered interest parity (CIP), so the forward rate carries the interest differential, not a forecast. The higher-yielding currency trades at a forward discount. Regimes trade monetary independence against exchange-rate credibility (no regime delivers fixed rates, free capital flows and independent policy at once), and whether a depreciation fixes a trade deficit depends on elasticities (Marshall-Lerner, J-curve) and on whether national saving rises relative to investment (absorption).

## Learning Outcomes Covered
- Define exchange rate; distinguish nominal vs real and spot vs forward rates
- Describe FX market functions and participants
- Calculate and interpret percentage changes of a currency; calculate cross rates
- Convert forward quotes (points or percent) to outright forwards; explain the spot-forward-interest arbitrage; compute forward premium or discount and the CIP-consistent forward rate
- Describe exchange rate regimes
- Explain the effects of exchange rates on trade and capital flows

## Frameworks Introduced
- **Quote convention `A/B`**: A = price currency, B = base currency; the quote is units of A per 1 unit of B. A rise in `A/B` means the base appreciated (price currency depreciated). Base is always 1 unit.
  - Direct quote: domestic currency is the price currency (`d/f`); indirect quote: domestic is the base (`f/d`). They are reciprocals; "direct" depends on where you sit, so work with base and price currency, not direct and indirect.
  - Professional market codes (Exhibit 6): one code for dollar pairs, e.g. EUR = USD/EUR, GBP = USD/GBP, JPY = JPY/USD, CAD = CAD/USD, CHF = CHF/USD, AUD = USD/AUD, NZD = USD/NZD; six-letter codes list the base first, e.g. EURJPY = JPY/EUR, GBPJPY = JPY/GBP, EURGBP = GBP/EUR. Hierarchy: EUR base against anything, then GBP, then USD (AUD and NZD are base against USD).
  - Quotes are two-sided: bid = price at which the dealer buys the base currency, offer = price at which it sells it; bid < offer; to invert a two-sided quote, `1/offer` becomes the new bid and `1/bid` the new offer. Majors to four decimals (pips), JPY pairs to two.
- **Percentage change of a currency**: `%Δ(base) = S_t1/S_t0 − 1` for the base; the price currency's change is the inverse-quote change `S_t0/S_t1 − 1`, never simply the negative (arithmetic asymmetry: base +4.35% means price currency −4.17%).
- **Real exchange rate** (domestic as price currency): `R_(d/f) = S_(d/f) × P_f / P_d`. A higher R means domestic purchasing power over foreign goods fell. `(1 + %ΔR) = (1 + %ΔS)(1 + %ΔP_f)/(1 + %ΔP_d)`, approximately `%ΔS + %ΔP_f − %ΔP_d`. R is an analyst index, never quoted or traded; PPP (law of one price) is a long-run anchor that fails in practice (non-traded goods, differing baskets, trade barriers, capital flows dominate) and real rates are poor predictors of nominal moves; the Big Mac index is the illustration.
- **FX instruments**: spot (T+2, T+1 for USD/CAD); outright forward (OTC, any date and size, settlement counted from the spot date, rate scaled by exact days, liquidity falls with tenor and size); futures (exchange-traded, fixed size and dates, margined and marked to market daily, deep CME IMM liquidity, minimal counterparty risk); FX swap (spot plus an offsetting forward, used to roll or extend forward positions and as swap funding; not the same as a multi-period currency swap); options. Turnover (BIS 2016, USD 5.1 trn/day): swaps 49%, spot 33%, outright forwards 14%, options 5%; interbank 42%, financial clients 51%, non-financial clients 8%; the five top pairs all contain USD (USD/EUR 23.1%, JPY/USD 17.8%, USD/GBP 9.3%).
- **Roll cash flow (FX swap)**: rolling a forward sale settles the old position at the prevailing spot, leaving a cash flow equal to notional × (old forward rate − current spot) in the price currency, with the base-currency amounts netting to zero.
- **Participants**: sell side (tier-one dealers such as Deutsche Bank, Citi, UBS, HSBC dominate and internalize flow; regional banks outsource) and buy side (corporates, real money accounts such as pension funds and ETFs, leveraged accounts such as hedge funds, CTAs and high-frequency traders, retail, governments, central banks, sovereign wealth funds). Most flow is financial (portfolio and speculative), not trade-related; hedging and speculation are often blended (benchmarked corporate treasuries).
- **Cross-rate calculation**: choose the algebra so the common currency cancels; e.g. `CAD/EUR = CAD/USD × USD/EUR`; `JPY/CAD = JPY/USD × (CAD/USD)^(−1)`. If a dealer's cross differs from the implied cross, triangular arbitrage buys the base currency where it is cheaper and sells where dearer. Cross bid/offer follow the same algebra using bids with bids and offers with offers (or inverses crossed), in practitioner convention.
- **Forward quotes**: `forward points = (F − S) × scale` (scale 10,000 for four-decimal quotes, 100 for JPY pairs); `F = S + points/scale`; forward premium or discount in percent: `F/S − 1`. Positive points mean the base trades at a forward premium (and the price currency at a discount); negative points, a forward discount. Quoted points rise with tenor and with the rate gap.
- **Covered interest parity**: hedged foreign investment must earn the domestic risk-free rate. With `f/d` (f per d, d is base): `(1 + i_d) = S_(f/d) × (1 + i_f) × (1/F_(f/d))`, so `F_(f/d) = S_(f/d) × (1 + i_f)/(1 + i_d)`. Generalized: price currency rate over base currency rate: `F = S × (1 + i_price × τ)/(1 + i_base × τ)`, `τ = days/360` for Libor-type deposits (Actual/360).
  - `F − S = S × (i_price − i_base) τ / (1 + i_base τ)`: proportional to spot, to the rate differential and approximately (not exactly) to term.
  - `F/S − 1 = (i_price − i_base) τ / (1 + i_base τ)`.
  - The currency with the higher interest rate trades at a forward discount.
  - Arbitrage if violated: if the forward is too high or low, borrow where hedged cost is lowest, lend where it is highest, lock the forward; the profit is riskless and needs no own capital. Swap funding in foreign currency costs within a few basis points of domestic borrowing because of this.
  - Forwards are not forecasts: reading `F = E[S_(t+1)]` gives `%ΔS = (i_f − i_d)/(1 + i_d)` (counter-intuitive: higher domestic rates imply slower expected domestic appreciation), but empirical forward rates are poor predictors with huge error; use them as arbitrage outputs.
- **Impossible trinity (ideal-regime impossibility)**: credibly fixed rates, full convertibility (capital mobility) and independent monetary policy cannot coexist; with fixed rates and mobile capital, a rate cut triggers outflows, reserve sales and monetary tightening that reverse it; floating restores independence (a rate cut weakens the currency and reinforces stimulus), controls on convertibility also help.
- **Historical regimes**: classical gold standard (price-specie-flow; trade imbalances move gold and money supply and prices), 1930s collapse, Bretton Woods (1944, 44 countries, fixed parities with realignments, collapsed early 1970s), Smithsonian agreements and floating after 1973 (volatility reflected liquid forward-looking asset markets), ERM from 1979 (sterling expelled September 1992 under speculative attack), euro 1999.
- **IMF taxonomy (hardest to softest)**: no separate legal tender (dollarization: inherits currency credibility not creditworthiness, no seigniorage, no lender of last resort; monetary union: shared policy through the ECB); currency board (legislated parity, base 100% backed by foreign assets, works like gold standard, needs flexible wages and a small non-traded sector, earns seigniorage; Hong Kong peg near 7.80 HKD/USD since 1983); fixed parity (no legal commitment, discretionary reserves, band up to ±1%, can still act as lender of last resort; credibility depends on reserves and self-fulfilling attacks); target zone (band up to ±2%); crawling peg (passive: indexed to inflation; active: pre-announced path to steer expectations); fixed parity with crawling bands (gradual exit); managed float ("dirty", no explicit target, invites retaliation); independent float (monetary policy and lender-of-last-resort free). Intervention still occurs under floats (Plaza Accord 1985; concerted 2000 euro support; SNB and BoJ interventions). Major currencies (USD, EUR, JPY, GBP, CHF, CAD, AUD) are considered freely floating.
- **Trade balance and capital flows**: `X − M = (S − I) + (T − G)`; a trade deficit means domestic saving falls short of investment plus fiscal deficit and equals a capital account surplus (foreigners buy domestic assets or lend). Adjustments run mainly through financial prices in the short and intermediate term; trade flows matter more later. Restricting capital flows forces the trade balance to zero.
- **Elasticities approach and Marshall-Lerner**: revenue change `%ΔR = (1 − ε)%ΔP`. For a depreciation with export prices fixed in domestic currency and import prices fixed in foreign currency: `ω_X ε_X + ω_M (ε_M − 1) > 0`, with `ω` the shares of exports and imports in total trade (`ω_X + ω_M = 1`) and `ε` positive price elasticities. A trade deficit means `ω_M > ω_X`; with balanced trade the condition reduces to `ε_X + ε_M > 1`; if `ε_M > 1` the balance definitely improves. Import elasticity matters more as the deficit grows. Elasticities are higher with close substitutes, competitive markets, luxuries, large budget or input-cost shares, and longer horizons.
- **J-curve**: even if Marshall-Lerner holds in the long run, the balance first worsens (contracts already priced in foreign currency, low short-run elasticities) then improves.
- **Absorption approach**: `X − M = Y − absorption` (income minus domestic expenditure, also saving minus investment). Depreciation helps only if it lifts income relative to spending: with slack, it switches demand to domestic goods and raises income; at full employment it needs lower expenditure, mainly via a wealth effect that fades, otherwise prices rise and undo the gain. A lasting fix needs a higher national saving relative to investment (fiscal consolidation, higher real rates) and a matching capital-account shift.

## Key Concepts
- **Price currency / base currency; pip; bid and offer; spread**.
- **Appreciation / depreciation (market) vs revaluation / devaluation (fixed regime)**.
- **Spot settlement T+2; forward maturity measured from spot date**.
- **Forward (swap) points; forward premium and discount**.
- **Triangular arbitrage; covered interest arbitrage**.
- **Libor deposit day count Actual/360**.
- **Real exchange rate; PPP; law of one price**.
- **Currency board; dollarization; monetary union; seigniorage**.
- **Fixed parity; target zone; crawling peg; crawling band; managed float; independent float**.
- **Capital controls; convertibility**.
- **Marshall-Lerner condition; J-curve; absorption**.
- **Real money vs leveraged accounts; tier-one dealers**.
- **FX swap vs currency swap**.

## Formulas & Reference Tables
- Cross: `A/C = (A/B) × (B/C)`; invert as needed so the common currency cancels
- Percentage change of base `= S₁/S₀ − 1`; of price currency `= S₀/S₁ − 1`
- Real: `R_(d/f) = S_(d/f) × P_f/P_d`; `%ΔR ≈ %ΔS + %ΔP_f − %ΔP_d`
- Forward from points: `F = S + points/10,000` (JPY pairs `/100`); from percent: `F = S(1 + %)`
- CIP: `F = S × (1 + i_price τ)/(1 + i_base τ)`; `F − S = S (i_price − i_base) τ/(1 + i_base τ)`
- Higher-rate currency trades at forward discount; `F > S` means `i_price > i_base`
- Unhedged-by-forward expected change if `F = E(S)`: `%ΔS = (i_price − i_base)/(1 + i_base)`
- Hedged return of a domestic investor lending abroad (f/d quotes): `S_(f/d) (1 + i_f)/F_(f/d) − 1`; CIP holds when this equals `i_d`
- Marshall-Lerner: `ω_X ε_X + ω_M (ε_M − 1) > 0`; balanced trade `ε_X + ε_M > 1`
- Trade identity: `X − M = (S − I) + (T − G)`

| Regime (hard to soft) | Policy independence | Main feature |
|---|---|---|
| Dollarization / monetary union | None | no own currency; credibility imported |
| Currency board | None | 100% foreign backing, legal commitment |
| Fixed parity ±1% | Very low | discretionary, peg can be abandoned |
| Target zone ±2% | Low | wider band |
| Crawling peg / band | Moderate | pre-set or inflation-indexed drift |
| Managed float | High | undeclared intervention |
| Independent float | Full | market-set rate |

## Mental Models
- **Write the quote as "price per base" before every calculation**; then cancel units.
- **Forward = spot adjusted for interest differential** (carry); forward points tell you the rate gap, not the market's forecast.
- **High interest rate, forward discount**: the currency that pays more is priced to lose that advantage in the forward.
- **Pegs import credibility and export autonomy**; the harder the peg, the less central-bank discretion.
- **Trade deficit equals capital inflow**: ask who is financing it and on what terms.
- **Elasticities need time and slack**: expect a J-curve, and expect depreciation to fail at full employment without lower absorption.

## Worked Example
**1. Percentage changes (recomputed).** USD/EUR 1.1500 to 1.2000: EUR +4.35%; USD against EUR: `1.15/1.20 − 1 = −4.17%`. CHF down 12% against GBP means GBP up `1/0.88 − 1 = 13.64%`. Base up 8% to 1.4500 implies a starting 1.4500/1.08 = 1.3426.

**2. Real exchange rate.** GBP/EUR rises 10%, euro-area prices +5%, UK prices +2%: `1.10 × 1.05/1.02 − 1 = 13.2%` (approximation 13%): UK buyers' purchasing power over euro goods fell. India 2018: INR/USD +6.7%, US inflation 2.5%, India 4.7%: `1.067 × 1.025/1.047 − 1 = 4.5%`.

**3. Cross rates and triangular arbitrage.** CAD/USD 1.3020, JPY/USD 111.94: `JPY/CAD = 111.94/1.3020 = 85.975`. A dealer quoting 86.20 offers a riskless gain of 0.2246 JPY per CAD (buy CAD at 85.975, sell at 86.20). USD/EUR 1.1701 and CAD/USD 1.3020: `CAD/EUR = 1.5235`. GBP/EUR `= 1.1701/1.3118 = 0.8920`. Second dealer ZAR/SEK 1.1210 vs implied `1.0218/0.9149 = 1.1168`: buy SEK at 1.1168, sell at 1.1210: about ZAR 4,200 per million SEK (exact 4,157 using the unrounded cross).

**4. Two-sided inversion.** MXN/USD 18.8580 ~ 18.8600 becomes USD/MXN `1/18.8600 = 0.053022` bid ~ `1/18.8580 = 0.053028` offer.

**5. Forward from points and percentage.** USD/EUR 1.15885 with +80.9 points (3 months): `1.15885 + 0.00809 = 1.16694`, i.e. +0.698%. Twelve-month +364.7 points: forward 1.19532, +3.147%, implies USD rates above euro rates. GBP/EUR 0.8752 with −1.4 points: forward 0.87506 (EUR base at a forward discount, so euro rates exceed sterling rates). Twelve-month forward 0.87295 against spot 0.8752 is −22.5 points; a rival dealer at a −0.30% discount offers 0.87257, so buying EUR forward there and selling at 0.87295 earns GBP 0.00038 per EUR.

**6. CIP forward and arbitrage.** `S = 1.6535` (f/d), `i_d = 3.50%`, `i_f = 5.00%`, 12 months: `F = 1.6535 × 1.05/1.035 = 1.6775` (foreign per domestic, premium). If the quote is 1.6900, hedged foreign investment returns `1.6535 × 1.05/1.69 − 1 = 2.73%` against 3.50% at home: borrow foreign (at 5%), convert, invest domestic, buy foreign currency forward at 1.6900: riskless gain about 0.78% on the foreign amount borrowed (1,000 foreign borrowed repays 1,050 and the domestic proceeds deliver 1,057.85 foreign at the forward).

**7. Points scale with rates and term (Actual/360).** S = 1.6555, `i_d = 2%`, `i_f = 3%`: 30-day forward 1.65688 (14 points); 180-day 1.66370 (82 points, not 6 × 14 = 84); with `i_f = 4%` the 30-day points double to about 28 (27.5 exactly). JPY/AUD 82.42, `i_JPY = 0.15%`, `i_AUD = 4.95%`, 90 days: `F = 82.42 × (1.000375/1.012375) = 81.443`, points `(81.443 − 82.42) × 100 = −97.7` (AUD, the higher-rate base currency, at a forward discount). A 270-day GBP/EUR with `i_GBP = 1.325%`, `i_EUR = 1.370%`, S = 0.8489 gives `F = 0.84862`, −2.8 points.

**8. Covered investment and swap roll.** AUD/HKD spot 0.1714, 1-year HKD rate 2.20%, forward 0.1724: 1 AUD becomes 5.834 HKD, grows to 5.962, converts to 1.0280 AUD: +2.8% hedged. Rolling a forward sale of EUR 100 million at 1.2000 when spot is 1.1900 yields a cash flow of USD 1,000,000, then a new forward is struck.

**9. Marshall-Lerner (domestic EUR depreciates 10%).** Exports 400m, imports 600m, `ε_X = 0.75`, `ε_M = 0.65`: export value +7.5% = +30m; import expenditure `+10% × (1 − 0.65) = +3.5%` = +21m; balance improves 9m. Check `0.4 × 0.75 + 0.6 × (0.65 − 1) = +0.09 > 0`. Australia example: exports 200 (ε 0.3), imports 180 (ε 0.6), `ω_X = 0.526`, condition = −0.03 (fails, balance moves the wrong way) and holds only if `ω_X > 4/7 = 0.571`.

## Anti-patterns
- Reading `A/B` backwards or calling a quote direct or indirect without checking whose currency is domestic.
- Treating the percentage move of the price currency as the negative of the base's move.
- Calling the forward rate a forecast, or expecting the high-rate currency to be at a forward premium.
- Forgetting the day-count and the ×100 versus ×10,000 point scaling for yen pairs.
- Cross-rate algebra that does not cancel units (multiplying two rates that share the wrong currency).
- Assuming PPP or the real rate predicts the spot rate.
- Expecting any depreciation to fix a deficit regardless of elasticities, capacity and saving behavior.
- Treating a fixed parity as a currency board (no legal commitment) or dollarization as importing creditworthiness.

## Exam Focus & Traps
- Base appreciates when `A/B` rises; direct quote for a domestic currency appreciating falls (e.g., GBP/EUR 0.8650 to 0.8590 for UK sterling appreciation).
- Real exchange rate falls (domestic purchasing power rises) when the domestic price level rises, all else equal.
- Forward premium or discount refers to the base currency; positive points or percent means premium; the premium base has the lower interest rate than the price currency (`i_price > i_base`).
- Convert percentage points with `S(1 + %)`, points with `/10,000` (or `/100` for yen); use `(i_a − i_b)/(1 + i_b τ)` with Actual/360.
- Spot settlement T+2 and forward maturity from spot date; a company expecting a foreign-currency receivable sells it forward; a long foreign bond holding is hedged by selling the foreign currency forward.
- Swap points are approximately but not exactly proportional to maturity.
- Marshall-Lerner generalization uses trade shares; a deficit means imports exceed exports; import elasticity dominates when the deficit is large; luxury, competitive goods benefit from devaluation.
- Currency board = legal commitment plus 100% backing of the monetary base; fixed parity bands ±1%, target zone ±2%; crawling pegs adjust the parity itself.
- Dollarized or board economies cannot offset US monetary policy; a floating currency can.
- A trade surplus cannot fall unless the matching capital outflow also falls (foreigners must buy more domestic assets or sell fewer to the country).
- Most FX turnover is swaps and financial-client flow, not trade settlement.
- **⚠ Correction (source Example 4 solution)**: the explanation of the two-sided inversion contains stray figures (an "offer of USD 0.08063" and a "bid of 0.08061"); the correct bid and offer in USD/MXN are 0.053022 and 0.053028.
- **⚠ Correction (source Practice Problem 15 notation)**: the "JPY/AUD" forward points are `(F − S) × 100 = −97.7`; one answer option shows +98.9, which has the wrong sign because the AUD (base) has the higher rate.
- **Note (source Example 8)**: the Marshall-Lerner value computed with unrounded weights is −0.032 (the text rounds to −0.03).

## Key Takeaways
1. `A/B` is price of one B in A; the base appreciates when the quote rises; inverse moves are not symmetric in percent.
2. The real exchange rate `S × P_f/P_d` measures relative purchasing power; PPP is a loose long-run anchor.
3. Cross rates follow from unit cancellation; mismatches are removed by triangular arbitrage.
4. Forward points translate the interest differential; CIP gives `F = S(1 + i_price τ)/(1 + i_base τ)`, so the higher-yielding currency is at a forward discount and forwards are poor forecasts.
5. Spot is a minority of FX turnover; swaps and financial flows dominate.
6. Regimes run from dollarization to independent float; fixed rates plus capital mobility rule out independent monetary policy.
7. Trade deficit equals capital inflow equals saving shortfall (`X − M = (S − I) + (T − G)`).
8. Depreciation improves the trade balance only if Marshall-Lerner holds and absorption falls relative to income; expect a J-curve.

## Connects To
- **ch 01**: elasticity concepts reused in Marshall-Lerner.
- **ch 03**: the `S = I + (G − T) + (X − M)` identity and exchange-rate shifters of AD and SRAS.
- **ch 05**: policy rates, exchange-rate targeting, capital flows and intervention.
- **ch 06**: balance of payments, capital account, trade policy and the FX regimes of trading blocs.
- **`cfa-derivatives`**: forwards, futures and swaps pricing under CIP.
- **`cfa-fixed-income`**: yield differentials and hedged foreign bond returns.
