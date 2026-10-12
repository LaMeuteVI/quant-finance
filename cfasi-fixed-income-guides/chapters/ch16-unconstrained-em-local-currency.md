# Chapter 16: Emerging Market Local Currency Bonds
> **Source**: CFA Society Italy × Advisor Private, "Unconstrained Fixed Income" guide (Sept–Oct 2019), Chapter 5 (Il mercato emergente in valuta locale) | Giuliano Palumbo, CFA

## Core Idea
EM local-currency bonds (EM Local) form a market almost five times the size of EM external (hard currency) debt, but foreign investors face currency, tax, liquidity and information barriers. Their volatility is closer to local sovereign debt than to EM corporate credit because FX is a major driver. The chapter gives a two-part valuation: a "building-block" fair value of the local yield curve (money market rate, expected policy path over 2 years, and a 2Y10Y term premium estimated from a risk factor) and the currency leg, typically expressed through carry trades (borrow funding currency, invest in high-yield currency) and arbitrage on covered interest parity breakdowns.

## Frameworks Introduced
- **Market structure**: EM Local corporate market is a niche (FX risk, low liquidity). Two types: **local corporate bonds** (over 90% of the EM local corporate universe; issued locally, subject to local tax and rules, need local custody accounts; half of this universe is onshore Chinese debt; mostly held by domestic investors) and **global corporate bonds** (under 10%; local-currency bonds settled via Euroclear, no local account, usually tax-exempt, favoured by foreign investors; includes dual-currency structures with settlement in a hard currency, e.g. masala bonds in India, komodo bonds in Indonesia).
- **Risk and opportunity**: currency risk (unexpected FX moves, regime change such as dropping a peg), transfer risk (capital controls, repatriation limits). Local currency government issuance reduced dependence on foreign currency loans. Post-2008 QE supported flows and compressed volatility; the reversal of accommodative policy (especially the Fed) can let prices diverge from fundamentals.
- **Building-block curve valuation** (two parts: fair value of the local curve; the FX rate vs the investor's base currency)
  1. **Money market (MM)**: considered fair by definition (short-term expected returns near current rates).
  2. **MM2Y**: fair value based on expected overnight policy rate over the next two years (consensus analyst forecasts or the investor's own view); central banks dominate the short end.
  3. **2Y10Y**: term premium compensating duration; harder to model in EM because data are non-stationary and regimes change abruptly (elections, etc.), so econometric term-premium models are unreliable.
- **Risk factor model for 2Y10Y**:
  `Risk factor = (10Y EM Local yield − 10Y benchmark yield) − 5Y CDS premium of the country − (expected 1-year inflation in EM − expected inflation in benchmark country)`
  - Benchmark: US or Germany, chosen by trade links. The CDS removes credit risk, the inflation differential removes inflation risk; the remainder indicates the term premium.
  - The risk factor feeds a quantitative model for fair value 2Y10Y. Dynamics: surprises in credit and inflation shift the risk factor and steepen or flatten the curve; the curve may also steepen/flatten without factor changes, signalling a mean reversion within 1-12 months (lead-lag between risk factor and future 2Y10Y). Gap between fair value and current 2Y10Y = expected term premium (positive or negative).
  - Qualitative inputs plus observable market data complement the model (Figure: policy rate, 2Y, 10Y).
- **Carry trade definition**: borrow low-rate (funding) currencies, invest in high-rate (target) currencies, usually short-term and unhedged. Profitable because **uncovered interest parity (UIP)** fails: UIP says the high-rate currency should depreciate by the rate differential, so no free lunch; empirically it often does not.
  - UIP: `i − i* = E[S_{t+1}]/S_t − 1` where `i` is the target-currency rate, `i*` the funding rate, and `S` the price of the funding currency in units of target currency (expected depreciation of the target currency equals the rate differential). The source writes `i − i* = Ee − E`.
  - CIP (covered interest parity): `i − i* = F/S − 1`, the forward premium equals the rate differential. Breaks (regulation, capital controls, supply-demand imbalances in FX) create arbitrage.
- **Carry trade implementations**
  | Implementation | Mechanics | Typical markets |
  |---|---|---|
  | Local debt | Borrow funding currency, buy target currency spot, invest in local bond; at maturity, buy back funding currency | Brazil (bond), widely |
  | Deliverable forward / FX swap | Buy target spot then swap (buy funding spot, target forward); two transactions with costs | Mexico (liquid peso swap market) |
  | Non-deliverable forward (NDF) / futures | Long target via NDF, cash-settled in a hard currency on the difference vs the contract rate; also short the target for the opposite view | BRL, CLP, COP, PEN |
  - Payoff of the first approach: `Rate differential − expected depreciation of target`.
- **Arbitrage strategies**: when CIP breaks (e.g. implied derivative rates abnormally low), borrow funding currency, invest in local debt or currency, and hedge FX in swap or forward markets. In well integrated markets (Mexico, Turkey, Russia) such opportunities shrink; Peru and South Africa are more fertile. Portfolio carry (multi-currency) vs single pair (use if you know a specific economy).
- **Comparison data** (chart): 3-month NDF implied yield vs 3-month government bond yield for Brazil, Peru, Turkey, Mexico, South Africa and Russia from 2012 to 2018; divergences show where CIP-type deviations opened.
- **Inflation credibility example**: Turkey's central bank targeted 5% since 2012 yet realized inflation ranged 6% to 15%; hence EM curves carry higher term premia and more complex fair-value work.

## Key Concepts
- **EM Local / EM external** — local-currency debt / hard-currency debt.
- **Global corporate bond (EM)** — local currency bond settled internationally (Euroclear).
- **Masala / komodo bond** — offshore rupee / rupiah-linked bonds.
- **Transfer risk** — capital movement restrictions.
- **MM, MM2Y, 2Y10Y** — building blocks of the local curve.
- **Term premium** — extra yield for holding longer maturities.
- **Risk factor** — 10Y spread minus CDS minus inflation differential.
- **CDS 5Y** — most liquid reference for country credit risk.
- **Carry trade** — long high-yield, short low-yield currency.
- **UIP / CIP** — uncovered / covered interest parity.
- **NDF** — non-deliverable forward settled in cash.
- **Funding vs target currency**.

## Formulas & Reference Tables
- `Fair 2Y10Y ≈ f(Risk factor)`, `Risk factor = (y10_EM − y10_bench) − CDS_5Y − (π_EM − π_bench)`.
- `Carry P&L ≈ (i − i*) − (S_T/S_0 − 1)` in the target currency per unit of funding (small-return approximation with S as funding currency in target units).
- `Break-even depreciation = i − i*`.
- `CIP: F/S − 1 ≈ i − i*`; deviation = `(F/S − 1) − (i − i*)`.
- EM Local vs external size ratio: about 5:1 (J.P. Morgan EM Local Markets Guide, 2018).

## Mental Models
- Use the building-block approach to separate policy expectations (MM2Y), term premium (2Y10Y) and FX; each has a different horizon and information set.
- Use CDS and inflation differentials to decompose a long-end EM yield into credit, inflation and residual premium.
- Use carry when volatility is low and funding currencies are stable; remember carry earns "the rate differential minus expected depreciation".
- Use NDFs when onshore access is restricted; use deliverable swaps in liquid markets.
- Use arbitrage versus CIP deviations only where capital is mobile; check why the deviation exists.

## Worked Example
Carry trade, long Brazilian real versus funding in euro (writer's illustration with round numbers).
1. Funding rate `i* = 0.0%`; target short rate `i = 6.5%`; one-year horizon, notional EUR 1,000,000, spot BRL 4.50 per EUR.
2. Gross carry: `6.5% − 0.0% = 6.5%`.
3. Scenario A: BRL depreciates 4% (EURBRL 4.50 → 4.68): return `≈ 6.5% − 4.0% = +2.5%` (more exactly `1.065 / 1.04 − 1 = +2.40%`).
4. Scenario B: BRL depreciates 8%: `1.065/1.08 − 1 = −1.39%`.
5. Break-even: the return is zero when EURBRL rises by `d` with `1.065/(1+d) = 1`, i.e. `d = 6.5%` (BRL depreciation of 6.5% measured as a rise in EURBRL; equal to the rate differential).
Interpretation: carry is a short-volatility payoff, small gains most of the time and sharp losses in risk-off episodes.

Risk factor example: 10Y EM yield 9.0%, benchmark 10Y 2.0%, 5Y CDS 1.8%, inflation differential 3.0% → factor `= 7.0 − 1.8 − 3.0 = 2.2` percentage points (illustrative).

## Anti-patterns
- Applying developed-market term premium models to EM without allowing for regime shifts.
- Treating the local yield as compensation without the FX leg.
- Running carry unhedged with leverage when volatility is low.
- Confusing local corporate bonds (tax, custody) with global corporate bonds (Euroclear).
- Ignoring transfer risk and capital controls.
- Relying on consensus policy forecasts without cross-checks.

## Practitioner Notes
- NDF markets are central for BRL, CLP, COP, PEN; Mexico's liquid FX swap market supports swap-based carry.
- Quant methods add value but must be read against market sentiment; the guide recommends a multi-faceted qualitative and quantitative approach.
- Cited research includes IMF, BIS, NBIM and Federal Reserve working papers on term premia and carry trades.

## Key Takeaways
1. EM Local is about five times the size of EM external debt; FX is a main volatility source.
2. Foreign-friendly access: global corporate bonds via Euroclear; local bonds face taxes and custody.
3. Fair value of the curve: MM (fair by definition), MM2Y (policy path), 2Y10Y (risk factor model).
4. The risk factor strips credit (5Y CDS) and inflation differential from the 10Y spread.
5. Carry trade exploits UIP failure; CIP failure creates arbitrage.
6. Implementation choices: local debt, deliverable swap, NDF/futures.
7. Mean reversion of 2Y10Y within 1-12 months guides curve trades.

## Connects To
- **ch11** (`cfasi-fixed-income-guides`): EM bonds introduction, risk families.
- **ch12**: curve trades and term premium in developed markets.
- **ch13**: hard currency EM credit.
- **`cfa-economics`**: UIP, CIP and exchange rate determination.
- **`cfa-derivatives`** and **`hull-derivatives`**: forwards, NDFs, swaps.
- **`ilmanen-yield-curve`**: term premium and carry.
