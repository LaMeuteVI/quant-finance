# Chapter 7: Currency Exchange Rates (Economics)

## Core Idea
Exchange rates are quoted as price currency per unit of base currency. Nominal rates adjusted for price levels give real rates. **Covered interest parity** ties forward rates to interest differentials, so the currency with the higher interest rate trades at a forward discount. Regimes range from no separate legal tender to free floating. Devaluation improves the trade balance only if the **Marshall–Lerner** condition holds, and usually only after a **J-curve**.

## Frameworks Introduced
- **Quote conventions**:
  - `A/B` = units of A (the **price** currency) per 1 unit of B (the **base** currency).
  - Market code **"BBBAAA"** lists the base first: GBPJPY means JPY/GBP.
  - **Direct quote**: domestic currency is the price currency. **Indirect quote**: its inverse.
  - Quotes are two-sided (bid/offer); the spread is quoted in pips.
- **Appreciation of the base currency**: A/B rises.
  - % change of the *inverse* rate: (1/(1 + x) − 1), which is not simply −x.
- **Nominal vs real exchange rate**:
  - `Real_{d/f} = S_{d/f} × (P_f / P_d)`.
  - The real rate rises when foreign prices rise relative to domestic prices, or when the foreign currency appreciates. Domestic goods become relatively cheaper.
- **Law of one price / PPP**: identical goods should cost the same once converted (e.g., the Big Mac index). It holds loosely and over the long run, because of non-traded goods, barriers and transport costs.
- **FX instruments**:
  - **Spot**: settles T+2.
  - **Forward**: an OTC agreement to exchange at a future date, at a rate fixed today.
  - **Futures**: exchange-traded (CME IMM), standardized, margined.
  - **FX swap**: a spot trade + an offsetting forward, used to roll forward positions.
  - **Options**.
- **Market participants**:
  - Buy side: corporates, real money (asset managers, insurers, pension funds), leveraged accounts (hedge funds, HFT), retail, governments, central banks, sovereign wealth funds.
  - Sell side: tier-1 dealer banks, and regional banks that outsource to them.
- **Cross rates**: `(CAD/EUR) = (CAD/USD) × (USD/EUR)`. Misaligned cross rates are removed by **triangular arbitrage**.
- **Covered interest parity (forward rate)**:
  - `F_{f/d} = S_{f/d} × (1 + i_f)/(1 + i_d)` (for a 1-period horizon; scale the rates by actual/360 for shorter periods).
  - Forward points = F − S, quoted in pips (scaled by 10⁴). F > S means the base currency trades at a **forward premium**.
  - The **higher-yielding currency trades at a forward discount**.
- **Ideal regime (impossible trinity)**: a country cannot have fixed exchange rates, full capital mobility (convertibility) and independent monetary policy all at once.
- **History**: gold standard (price-specie-flow) → Bretton Woods (1944, adjustable pegs) → Smithsonian (1971) and generalized floating → European ERM (1979) → the euro (1999).
- **Taxonomy of regimes (IMF), from hardest to softest**:
  1. No separate legal tender: dollarization, monetary union.
  2. **Currency board**: a legislated fixed parity, with the monetary base 100% backed by foreign reserves (Hong Kong).
  3. **Fixed parity**: discretionary, no legal commitment, ±1% band.
  4. **Target zone**: wider band (±2%).
  5. **Crawling peg**: passive (indexed to inflation) or active (pre-announced).
  6. Crawling bands.
  7. **Managed ("dirty") float**.
  8. **Independent float**.
- **Trade balance and exchange rates**: a current-account deficit is mirrored by a capital/financial-account surplus.
- **Marshall–Lerner condition**: `ω_X·ε_X + ω_M·(ε_M − 1) > 0`.
  - ω are the shares of exports/imports in total trade, and ε the price elasticities.
  - With balanced trade this reduces to **ε_X + ε_M > 1**.
  - Import elasticity matters more when imports exceed exports.
- **J-curve**: after a depreciation, the trade balance first worsens (contracts are already signed, and demand adjusts slowly), then improves.
- **Absorption approach**: `CA = Y − absorption`. A depreciation improves the CA only if income rises relative to expenditure. Otherwise, at full employment, prices rise and offset it (partly via the wealth effect).

## Key Concepts
- **Base vs price currency**, **pips**, **forward premium/discount**, **swap points**.
- **Seigniorage**: profit from issuing money. A currency board earns interest on its reserves.
- **De facto vs de jure currency substitution**.

## Mental Models
- Always ask **"which currency is the base?"** before interpreting any move.
- **Forwards are not forecasts**: they reflect interest differentials (arbitrage), not expected spot rates.
- **Harder pegs import credibility but give up monetary independence.**

## Anti-patterns
- ⚠ **Correction vs the notes**: it is *futures* (not forwards) that are exchange-traded, standardized and margined.
- ⚠ **Correction**: in the Marshall–Lerner discussion, a trade **deficit** means ω_M > ω_X (imports exceed exports), not the reverse.
- **Inverting a percentage change naively**: if GBP/EUR rises 5%, EUR/GBP falls 1/1.05 − 1 = 4.76%, not 5%.

## Worked Example
**Forward rate from interest parity.**
- Spot USD/EUR = 1.1000 (USD per EUR). 1-year i_USD = 5%, i_EUR = 3%.
- F = 1.1000 × 1.05/1.03 = **1.1214**. Forward points = +214 pips.
- The EUR (base, lower rate) trades at a **forward premium**. The USD (higher rate) trades at a forward discount.

**Cross rate.** CAD/USD = 1.35 and USD/EUR = 1.10 → CAD/EUR = 1.35 × 1.10 = **1.485**.

## Key Takeaways
1. Read A/B as the price of 1 B in A. The market code lists the base currency first.
2. Real exchange rate = S × P_f/P_d. PPP holds only loosely and over the long run.
3. Covered interest parity: F = S(1 + i_price)/(1 + i_base). The high-yield currency trades at a forward discount.
4. Regimes run from dollarization and currency boards to free floats. The impossible trinity constrains them all.
5. A devaluation helps the trade balance only if ε_X + ε_M > 1, and only after a J-curve.

## Connects To
- **Ch 5**: monetary policy and interest differentials.
- **Ch 6**: the BOP and trade balance.
- **Hull Ch 5 / Ch 17** (`hull-derivatives` skill): currency forwards and options.
