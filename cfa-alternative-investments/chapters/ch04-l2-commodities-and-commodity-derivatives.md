# Chapter 4: Introduction to Commodities and Commodity Derivatives
> **Source**: CFA Program Curriculum 2022, Level II, Reading 37 · Alternative Investments | David Burkart, CFA, and James Alan Finnegan, CAIA, RMA, CFA

## Core Idea
Commodities are physical goods with no cash flows: they are valued on a forecast of future prices (supply, demand, storage, inventories), and investors get exposure almost entirely through futures, swaps and futures-based indexes. The return of a fully collateralized long futures position decomposes into spot (price) return + roll return + collateral return, and the shape of the curve (contango or backwardation) drives the roll return, which differs sharply by sector and can swamp or add to the spot return over several years.

## Learning Outcomes Covered
- compare characteristics of the six commodity sectors
- compare life cycles from production to consumption
- contrast commodity valuation with equity and bond valuation
- describe futures market participants
- analyze spot vs futures in contango and backwardation
- compare theories of futures returns (insurance, hedging pressure, storage)
- calculate and interpret total return of a fully collateralized futures position
- contrast roll return in contango and backwardation
- describe how commodity swaps obtain or modify exposure
- describe how index construction affects index returns

## Frameworks Introduced
- **Stock-and-flow fundamental analysis (four tools)**: (1) direct announcements (USDA, OPEC, IEA, China NBS inventory and production data), (2) component analysis (stock = capacity, acreage, reserves; flow = utilization, shipments, yields), (3) timing considerations (seasonality, logistics, shocks), (4) money flow (sentiment, interest rates, inflation, subsidies of substitutes).
  - When to use: forming a supply/demand view on any commodity.
  - How: set boundaries with the stock, track the flow against them, overlay the timing, then adjust for macro/monetary conditions.
  - Failure mode: coefficients are non-stationary (genetically modified drought-resistant corn breaks historical weather sensitivities), data are privately held, distributions are non-normal with shifting correlations.
- **Three theories of futures returns / curve shape**:
  - **Insurance theory (Keynes, "normal backwardation")**: producers sell forward for certainty, speculators demand a discount, so futures price < expected spot and the speculator earns a risk premium.
  - **Hedging pressure hypothesis (Cootner; De Roon, Nijman, Veld)**: the curve shape depends on the imbalance between producer hedging (short futures) and consumer hedging (long futures). Producers dominate gives backwardation, consumers dominate gives contango, balance gives a flat curve.
  - **Theory of storage (Kaldor)**: `Futures = Spot + direct storage costs − convenience yield`. Abundant inventories mean low convenience yield and contango; scarce inventories mean high convenience yield and backwardation.
  - When to use: insurance and hedging pressure explain who earns the premium; storage explains the shape from the physical side. Use storage for storable commodities (metals, grains), hedging pressure when positioning data (producer vs consumer) are readable.
  - Failure mode: key inputs are unobservable (storage costs are proprietary, convenience yield jumps with events) and the evidence is weak: Kolb (1992) found "normal backwardation is not normal".
- **Total return decomposition of a fully collateralized futures position**: `Total return = price (spot) return + roll return + collateral return`, plus rebalance return at index level. Collateral equals full notional (no leverage).
- **Index construction levers**: breadth, weighting method, roll rule, rebalancing frequency, governance (rules-based vs selection-based), investability. Each lever changes roll return and rebalance return.

## Key Concepts
- **Commodity**: tradable physical good from a natural resource supplied without substantial differentiation; value comes from consumption or use as an input, not from cash flows.
- **Six sectors (Bloomberg Commodity Index segmentation)**: energy, grains, industrial (base) metals, livestock, precious metals, softs (cash crops: cotton, cocoa, sugar, coffee).
- **Spot price**: price to buy or deliver the physical good at a specific location now; highly localized by grade and logistics.
- **Basis**: spot price − futures price (the reading's general definition); also used for physical-vs-futures differences (e.g., soybeans at the Mississippi River vs the contract).
- **Backwardation**: spot above near futures, and near futures above deferred futures; downward-sloping curve; positive calendar spread.
- **Contango**: spot below futures, and near futures below deferred futures; upward-sloping curve; negative calendar spread.
- **Calendar spread**: near-term futures price − farther-term futures price for the same commodity; positive in backwardation, negative in contango; tradeable as its own instrument.
- **Convenience yield**: benefit of holding physical stock as a buffer against supply disruption; high when inventories are low, low when stock is abundant.
- **Price (spot) return**: `(current front price − previous front price)/previous front price`.
- **Roll return (roll yield)**: percentage gap between near and far contract prices times the share of the position rolled; an accounting component, not independently capturable.
- **Collateral return**: interest on the T-bills or cash backing the futures position (initial margin plus unlevered balance).
- **Rebalance return**: extra return from resetting index weights, positive when components mean-revert and are imperfectly correlated.
- **Commodity swap**: OTC contract exchanging payments on multiple dates tied to commodity reference prices or indexes (excess return, total return, basis, variance, volatility swaps).
- **Cash vs physical settlement**: cash-settled contracts have no value after maturity and may converge imperfectly; physical delivery forces spot-futures convergence at specific delivery points (WTI at Cushing, Brent in the North Sea).
- **Rules-based vs selection-based index**: quantitative rules vs a committee choosing constituents.

## Formulas & Reference Tables
- `Price return = (P_t − P_{t−1}) / P_{t−1}` (front-month futures, not physical)
- `Roll return = [(Near price − Far price) / Near price] × % of position rolled`
- `Contracts after roll = exposure ÷ far-contract exposure per contract` (backwardation: buy more than you sell; contango: buy fewer)
- `Total return (fully collateralized) = price return + roll return + collateral return`; collateral return = risk-free rate × fraction collateralized (100% for index math). Components add approximately; geometric compounding gives a small cross term.
- `Futures price (theory of storage) = Spot + direct storage costs − convenience yield`
- `Calendar spread = Near − Far` (positive: backwardation; negative: contango)
- `Excess return swap payment = notional × excess return of index futures`; `Total return swap payment (long) = notional × index return` (spot + roll + collateral, net of fee)
- Keynes check: speculator profit if front price is stable = deferred price converges up to front price (cotton: 76.75 − 74.50 = 2.25 cents × 50,000 lb = $1,125 per contract).

Curve shape and drivers:

| | Backwardation | Contango |
|---|---|---|
| Spot vs futures | Spot > near > far | Spot < near < far |
| Calendar spread | positive | negative |
| Roll return (long) | positive | negative |
| Contracts to roll | buy more | buy fewer |
| Insurance theory | producers sell forward, speculators paid | not predicted |
| Hedging pressure | producers' hedging dominates | consumers' hedging dominates |
| Storage theory | low inventories, high convenience yield | ample inventories, storage costs dominate |

Sector roll returns, S&P GSCI sectors (mean annual, rolling 12-month, to March 2019):

| Sector | Mean roll return |
|---|---|
| S&P GSCI total | −1.3% |
| Energy | −1.5% (only sector with credible positive potential; fading after 2010) |
| Industrial metals | −1.3% |
| Agriculture | −4.5% |
| Livestock | −1.1% |
| Precious metals | −5.1% |
| Softs | −5.5% |

S&P GSCI return components, Jan 1970 to Mar 2019: total 6.8% (risk 19.8%), spot 3.0% (corr to total 0.97), roll −1.3% (risk 4.2%, corr −0.11), collateral 5.0% (risk 1.1%, corr −0.14). Roll return correlation with price return is only about 3%.

Major indexes (as of April 2019):

| Element | S&P GSCI | BCOM | DBLCI | TR/CC CRB | RICI |
|---|---|---|---|---|---|
| Adoption | 1991 | 1998 | 2003 | 2005 | 1998 |
| Commodities | 24 | 23 | 14 | 19 | 38 |
| Weighting | World production | Production + liquidity | Fixed | Fixed (tiers) | Fixed (tiers) |
| Roll | Nearby, monthly | Front to next/second | Optimized on roll return (next 12 months) | Front to next | Front to next |
| Rebalance | Annual | Annual | Annual | Monthly | Monthly |
| Notes | Energy up to about 80% | Sector cap 33%, floor 2% per commodity; selection-based | No livestock | Committee weights | Exotic/illiquid constituents, some non-USD |

Swap types:

| Swap | Pays on | Typical user |
|---|---|---|
| Excess return | Price change of the futures in the index vs fixed level | Hedgers (refiner), speculators |
| Total return | Index level change including collateral interest, net of fee | Pension funds, institutions wanting passive exposure |
| Basis | Spread between two related reference prices (Brent vs heavy Gulf crude) | Refiners with grade-specific costs |
| Variance | Realized minus fixed variance, often capped | Volatility views |
| Volatility | Realized minus expected volatility | Volatility views (seller wins if realized is lower) |

## Mental Models
- **Commodity = a price forecast, not a cash-flow stream**: there is no DCF; compare with an option on logistics, storage and inventories. A commodity "return" is earned from price change, from the curve and from the collateral.
- **Roll return is an accounting, not an alpha**: it is the cost or gain of staying in the front of the curve; you cannot hold "roll only". It matters over years, not months.
- **The curve is a balance sheet in disguise**: contango is the market paying the holder of stock (storage cost), backwardation is the market paying whoever releases stock (convenience yield). Track inventories and the curve together.
- **Stored vs just-in-time**: metals, grains, softs, livestock feed and gold are stored, so they tend toward contango and negative roll; energy was consumed in real time and showed a better roll record until shale changed the picture after 2010.
- **Insurance view**: a long futures investor is selling insurance to a hedger; whether it pays depends on who needs the insurance more.
- **Index choice = roll and weight choice**: all five indexes correlate above 70% with each other and about 0% with equities and bonds, but their roll rules and sector weights decide relative performance in any period.

## Worked Example
**1. Total-return decomposition of a long soybean futures trade (collateralized, rolled once).** Long nearby soybeans at 865.0; three months later the near price is 877.0 and the far price is 883.0, collateral earns 0.60% annualized, the whole position is rolled.
- Price return = (877 − 865)/865 = 1.387%
- Roll return = (877 − 883)/877 = −0.684% (contango, 100% rolled)
- Collateral return = 0.60% × 3/12 = 0.150%
- Total = 1.387 − 0.684 + 0.150 = 0.853%, about 0.85%
Interpretation: contango removed roughly half of the price gain, which is why a positive spot move is not a positive total return.

**2. Annualized total return on a lean hog position.** Price return −12%, roll return −24%, risk-free 1.2% on 100% collateral: −12 − 24 + 1.2 = −34.8%. Backwardation or contango matters: here a persistent contango cost twice the price decline.

**3. S&P GSCI rolling over five days.** March 52.64, April 53.00: gross roll = (52.64 − 53.00)/52.64 = −0.684%. Rolling 20% per day: −0.684% × 20% = −0.137% (the source prints −0.13%, rounding down; rounded correctly it is −0.14%).

**4. Maintaining exposure.** £110 of exposure with near contract worth £10 (11 contracts); far contract £9 (backwardation): 110/9 = 12.2, buy about 12 contracts, i.e., roll 11 and add 1. In contango (£108 exposure, near £9 = 12 contracts; far £10): 108/10 = 10.8, hold about 11 and sell the extra one.

**5. Total return swap.** Long GSCI total return swap, $25m notional, monthly reset, index 2,542.35 (April), 2,582.23 (May), 2,525.21 (June). May: +1.569% so the dealer pays $392,157; June: −2.208% so the long owes $552,042 (the 25m × index change, not a swap premium).

## Anti-patterns
- **Treating spot price as the futures-based return**: the long-only futures investor earns spot + roll + collateral, so a flat spot with persistent contango loses money.
- **Assuming backwardation always earns a risk premium**: 40% of commodities in Ilmanen's sample had negative roll but positive total return; Kolb found "normal backwardation is not normal".
- **Equating hedging with being short and speculating with being long**: both sides appear in each category (gold miner short = hedge; oil major long = speculation); regulators separate commercial from non-commercial participants regardless.
- **Valuing commodities with DCF**: no cash flows; use a forecast of price and the curve.
- **Reading an index as diversified because it spans many exchanges**: exchange-level commodity prices are highly correlated, so exchange diversity adds little (CFA Example 24).
- **Concentration without noticing**: production-weighted indexes can be about 80% energy (S&P GSCI) vs about 30% for BCOM; natural gas weight (3% vs 9%) with roll costs near 19% a year changes the index drag.
- **Using hedging as risk-free**: poorly designed hedges become speculation (Metallgesellschaft AG, 1993).

## Exam Focus & Traps
- **Backwardation/contango definitions**: backwardation = spot above futures (near above far); contango = futures above spot. Calendar spread = near − far, so positive spread = backwardation. ⚠ Source text note: Example 11's solution says "current spot minus futures"; the numeric spread definition used elsewhere in the reading (and in Exhibits 6-7) is near minus far. Both give the same sign convention.
- **⚠ Errata (L2 2022 R37, Solution to 10)**: the basis for the near-term Brent contract is spot minus near futures = 77.56 − 73.64 = **$3.92**; the calendar spread (near − far) is 73.64 − 73.59 = $0.05, so neither $3.97 (calendar spread) nor $0.05 (basis) is correct. Brent curve: spot > near > far, so backwardation.
- **Storage costs are positively related to futures prices** (contango), not negatively. Statement "commodities generate future cash flows" is false; they incur storage cost. Statement "most commodity investments are via derivatives" is true.
- **Which theory fits**: balanced producer/consumer hedging and a large crop with a contango curve points to the theory of storage (inventories); energy consumed in real time with minimal storage and spot above futures points to storage too, since convenience yield is high. Consumers more concerned about price than producers means hedging pressure and contango; producers more concerned means insurance theory and backwardation.
- **Which roll sign**: contango negative, backwardation positive; in backwardation you buy more contracts than you sell.
- **Total return**: add price, roll and collateral; collateral = risk-free rate × collateralization. Annualize the three components consistently (a 3-month trade uses 0.60% × 3/12).
- **Gold in the exhibit**: flat curve across months gives zero roll; coffee in contango gives negative roll; gasoline in backwardation gives positive roll.
- **Swap choice**: expect Brent to outperform heavy crude: long basis swap (long Brent, short heavy); expect realized volatility below expectations: short volatility swap; expect index to rise: long (not short) excess return swap.
- **Index trends**: in an upward-trending market, an index of contango commodities (A) underperforms one of backwardated commodities (B) with the same weights and rebalancing. Annual rebalance favors trending markets; monthly rebalance favors mean-reverting markets; production-weighted indexes (GSCI, BCOM) have lower rebalancing turnover.
- **Participants**: liquidity providers provide insurance to hedgers; informed investors are hedgers and speculators; arbitrageurs with storage exploit spot-futures mispricing. Commodity futures net positions sum to zero; short futures need the same margin as long.
- **Commodity returns diversification**: low correlation with stocks and bonds, some inflation hedging via price return; roll return has statistically strong negative mean in all sectors but energy.

## Key Takeaways
1. Value commodities by price forecast and inventory/storage economics, not cash flows; use stock, flow, timing and money-flow tools.
2. Decompose any futures-based return into spot, roll and collateral: since 1970 the S&P GSCI returned 6.8% with about 3.0% spot, −1.3% roll, 5.0% collateral.
3. Roll return follows the curve: contango negative, backwardation positive; storable and stored sectors (precious metals, softs, agriculture) have the most negative historical roll.
4. Do not assume backwardation pays: the insurance theory has weak evidence; combine hedging pressure (who needs insurance) with storage (inventory level).
5. Use swaps when you need customization, cash settlement or one contract for a long period; use total return swaps for passive institutional exposure, basis swaps for grade spreads, variance/volatility swaps for pure volatility views.
6. Choose indexes by roll rule, weights, rebalance frequency and governance: GSCI is energy-heavy and production-weighted, BCOM is capped and liquidity-weighted, DBLCI optimizes the roll, CRB and RICI use fixed weights and rebalance monthly.
7. A diversified commodity basket has roughly 0% correlation to traditional assets and above 70% among commodity indexes; sector mix decides roll return.
8. Hedge purposefully: the airline, refiner and farmer examples show hedging fixes cash flow rather than profit; flawed hedging becomes speculation.

## Connects To
- **ch01**: alternative investment characteristics, indexes and return measurement issues for real assets and commodities (same skill).
- **ch06**: how commodities fit in strategic allocation to alternatives, inflation hedging and diversification (same skill).
- **`tian-commodity-price-jumps`**: stochastic models of commodity prices with jumps, the quantitative side of spot price dynamics and convenience yield.
- **`hull-derivatives` ch35**: commodity derivatives, storage costs, convenience yield and futures pricing models (cost-of-carry with convenience yield).
- **`cfa-equity-valuation` ch11**: contrast of income-based valuation (equities) with commodity price-forecast valuation; commodity prices as inputs to resource-company valuation.
- **`cfa-derivatives` ch03**: futures and forward pricing, cost-of-carry and no-arbitrage bounds behind the contango and backwardation relationships.
