# Chapter 35: Energy and Commodity Derivatives

## Core Idea
Commodity prices mean-revert, are seasonal and can jump, especially electricity. Model them with risk-neutral processes fitted to the futures curve, and value options on trees or by Monte Carlo. Weather and catastrophe risks have no systematic risk, so expected payoffs from historical data are discounted at r.

## Frameworks Introduced
- **Commodity classes**:
  - Agricultural: grains, softs, livestock.
  - Metals: investment metals like gold and silver vs industrial metals.
  - Energy: crude oil, natural gas, electricity.
  - Each class has its own storage, seasonality and convenience-yield dynamics.
- **Energy specifics**:
  - **Crude oil**: futures, forwards and swaps. Benchmarks are WTI and Brent. Swaps and options often reference **average** prices (Asian).
  - **Natural gas**: seasonal, with storage constraints.
  - **Electricity**: non-storable, with extreme spikes and strong mean reversion. Contracts are on-peak or off-peak. **Swing options** allow flexible take quantities.
- **Risk-neutral commodity process**: `d ln S = [θ(t) − a ln S]dt + σdz`.
  - θ(t) is chosen to fit the futures curve, so seasonality is captured through the futures prices.
  - Build trinomial trees like the Hull–White tree, with a shift to match futures.
  - Add jumps for electricity (jump-diffusion).
- **Weather derivatives**:
  - **HDD** = max(0, 65°F − average daily temperature).
  - **CDD** = max(0, average daily temperature − 65°F).
  - Contracts are on the cumulative HDD or CDD for a month or season.
- **Insurance derivatives**: catastrophe (CAT) bonds, industry loss warranties. They are alternatives to reinsurance, and investors lose principal if a catastrophe happens.
- **Pricing without systematic risk**: estimate the expected payoff from historical data and discount at r (the market price of risk λ = 0).
- **Producer hedging**: hedge price and volume risks together (e.g., weather derivatives + energy futures), because demand correlates with temperature.

## Key Concepts
- **Convenience yield / backwardation / contango** (Ch 5).
- **Mean reversion speed a**: high for electricity, lower for oil.
- **Spark spread**: the power price − heat rate × gas price. A power plant is a strip of spark-spread options.
- **Load-serving risk**: volume uncertainty correlated with price.

## Mental Models
- **Use the futures curve as the risk-neutral expectation**: you do not need to estimate λ for commodities if futures exist.
- **Electricity = a mean-reverting, jumpy, non-storable asset**, so spot/forward relations break down.
- **Weather risk is diversifiable**: its price is roughly actuarial.

## Anti-patterns
- **Applying cost-of-carry to electricity**: it cannot be stored.
- **Using GBM for commodities**: it ignores mean reversion and overprices long-dated options.
- **Hedging price but not volume**: a utility's revenue depends on both, and they are correlated.

## Worked Example
**HDD call (Example 35.4).** February, Chicago O'Hare. Strike 700 HDD, $10,000 per degree-day.
- From historical data: the HDD is lognormal with mean 710 and a standard deviation of ln HDD of 0.07.
- d₁ = [ln(710/700) + 0.07²/2]/0.07 = 0.2376 and d₂ = 0.1676.
- Expected payoff = 10,000 × [710N(d₁) − 700N(d₂)] = **$250,900**.
- Valued one year before maturity at r = 3%: 250,900e^{−0.03} = **$243,400**. There is no risk adjustment, since weather has no systematic risk.

## Key Takeaways
1. Commodity models need mean reversion, seasonality and sometimes jumps. Calibrate the drift to futures.
2. Electricity is non-storable, spiky and strongly mean-reverting. Swing and spark-spread options are common.
3. Average-price (Asian) structures are standard for oil swaps and options.
4. Weather and CAT products are priced actuarially: historical expected payoff × e^{−rT}.
5. Producers should hedge price and volume jointly.

## Connects To
- **Ch 5**: convenience yield.
- **Ch 18**: futures options.
- **Ch 26**: Asian options.
- **Ch 32**: trinomial trees with mean reversion.
- **Ch 36**: real options on commodity projects.
- **`tian-commodity-price-jumps` skill**: jumps and discontinuities in commodity prices.
