# Chapter 12: Selecting a Passive Manager: Practical Insights (La selezione di un gestore passivo: alcuni spunti)
> **Source**: CFA Society Italy x Advisor Private, "ETF & Fund Selection" guide (Advisor Private no. 16, 2019), Chapter 4 | Giancarlo Sandrin, CFA; the closing insert on alternative risk premia ETFs is sponsored by J.P. Morgan Asset Management (Roberta Gastaldello) and is attributed below

## Core Idea
ETF choice is not trivial: out of about 1,500 ETFs listed in Europe (and a European ETF/ETP universe growing exponentially), many offer the same exposure but differ in six decision factors: **benchmark** (most important), fund structure, total cost of ownership, tracking error volatility, liquidity, transparency, plus domicile. Weights on these depend on the investor: a tactical investor prefers low TEV and high liquidity; a buy-and-hold investor focuses on TCO.

## Frameworks Introduced
- **ETF evolution map**: 1.0 (2000): replicate main equity indices; 1.1: fixed-income ETFs; 2.0: smart beta (components chosen on fundamental/technical criteria such as volatility, momentum, profitability); 3.0: ESG and fundamental screening; the author expects 4.0 to resemble self-indexing (manager's proprietary, transparent rules with an active flavor).
- **Six-factor ETF selection checklist** (benchmark, fund structure, TCO, tracking error volatility, liquidity, transparency and simplicity, plus domicile):
  1. **Benchmark first**. Same market, different indices: Japan: Nikkei 225 (price-weighted, like the Dow Jones, so weights depend on share price); Nikkei 400 (market-cap weighted after screening on ROE and operating profit / market value to select the most profitable names); TOPIX (cap-weighted, about 2,000 stocks including small caps); MSCI Japan (cap-weighted, about 320 stocks). Four indices, potentially materially different returns because of construction. Know what you own.
  2. **Fund structure**: physical full replication (nearly identical holdings; common for liquid, small indices, e.g. EuroStoxx 50: buy the 50 stocks in index weights), physical optimized/sampled (representative sample when fund size or low liquidity of small constituents makes full replication hard: MSCI World has about 1,650 names; buying the 100 smallest increases trading cost without improving tracking much), or synthetic (swap). Illustrative curve: more of the benchmark replicated lowers tracking error but raises costs.
  3. **Total cost of ownership**, two components. Internal cost = **tracking difference** (ETF return minus benchmark over the horizon) driven by TER, replication skill, extra income (securities lending, tax treatment of dividends vs the benchmark's assumption). External costs = trading costs, mainly bid-ask spread. Longer holding: internal costs dominate; short tactical: external ones.
  4. **Liquidity**: look at the exchange order book (first level spread and quantities, plus deeper levels), not at ETF liquidity relative to the underlying. Market makers hedge in the underlying markets, so ETFs on US underlying are priced best when US markets are open (afternoon in Europe); avoid trading near open/close or without a price reference (volatility widens quotes). Example on Borsa Italiana, 1 March 2019, buying and selling 50,000 EUR of a heavily traded ETF: at 9:00, average buy about 39.32, average sell about 39.218, round-trip cost 0.26% (39.32/39.218 - 1); at 9:08 buy 39.229-ish and sell 39.27 (as printed) with a spread of only 0.07%; a 0.19% difference within 10 minutes. (Source printed prices contain inconsistencies, e.g. a buy price of 39.229 below the sell price; the quoted spreads 0.26% and 0.07% match the first-level quotes: 39.30/39.225 and 39.295/39.270.)
  5. **Domicile**: Irish-domiciled ETFs benefit from 15% US withholding on US dividends instead of 30% for other domiciles.
  6. **Tracking error volatility (TEV)**: standard deviation of daily gaps between ETF and benchmark; useful for short horizons, misleading over long ones. Example: ETF A loses 0.005% vs benchmark every day: TEV below 0.01%, yet over 45 days returns 2.97% vs benchmark 3.2% (gap about 0.23%); ETF B fluctuates around the benchmark (TEV about 0.2%) and returns 3.19%. A constant underperformance keeps TEV low but costs money, so tie TEV with tracking difference and TCO.
  7. **Transparency**: portfolio, structure, index construction. Never underestimate it.
- **Physical vs synthetic**: formerly "the mantra" of the European market, less central now as issuers improved transparency and counterparty-risk coverage. Historical swap structure: the fund bought a basket unrelated to the index (possibly lent out) and swapped its return for the index; swap value could be positive (credit exposure to the investment bank) or negative; problem: counterparty risk and opacity of the basket. Today: swap collateralized (funded structure per the source's definition, with collateral usually above the swap value, swap reset regularly, sometimes daily, or when the swap value passes thresholds, so the bank pays the fund the swap value and counterparty risk is practically eliminated). Remaining issue: opaque implicit swap cost, not in TER but inferable from the fund-index return gap. Swaps are justified for lower TEV (compare with TCO) and for commodities, leverage and similar where swap is the only or best option. Focus now shifts to securities lending: collateral and split of revenue between fund and manager. (Note: the source's labeling of funded/unfunded differs from ch07; ch07 uses the standard market convention where a funded swap holds cash and posts collateral externally. Check each product's prospectus.)
- **Leveraged and inverse ETFs**: resets daily, so the exposure is as if a futures position were closed and reopened each day with the notional updated by yesterday's P&L; compounding makes multi-day returns differ from the multiple of the index. Example (-2x daily short): index +2.10%, +1.50%, +3.10%, +2.20%, -2.00%, -3.10%, -1.60% over seven days = +2.03% cumulative; the ETF finishes -5.02% instead of -4.06% (verified: 94.98 from 100), i.e. the investor loses on both sides. Mathematical reminder: after a 50% loss you need +100%. Use only for very short, tactical positions and understand the benchmark.
- **Alternative risk premia ETFs (sponsored insert, J.P. Morgan AM)**: evolution from alpha to beta: first all fund returns were attributed to stock-selection skill (1896 Dow Jones; 1957 S&P 500; 1975 Bogle's first index fund treated equity beta as an investable risk premium; then Fama-French and factor indices; in hedge funds, "alternative beta" after 2008 funds). Alternative risk premia are rule-based long-short strategies across equities, fixed income, FX and commodities (value, quality, momentum, carry), with positive risk-adjusted returns and low correlation to traditional assets (correlation matrix, Jan 1998-Dec 2017: e.g. equity value vs developed equity 0.11, equity quality -0.27, equity momentum -0.18; FX carry 0.37; FX momentum -0.04; commodity momentum 0.02; versus emerging equity 0.83 and high yield 0.67 with developed equity). Packaged as UCITS ETFs: Managed Futures (systematic CTA beta via momentum and carry in futures across four asset classes) and Equity Long-Short (value, quality, momentum long-short, to lower beta to equity). Promotional: test net returns, capacity and persistence of premia.

## Key Concepts
- **Price-weighted vs cap-weighted index**: weights by share price vs by market value.
- **Replication**: full, optimized (sampled), synthetic.
- **Tracking difference / TEV**: realized gap / volatility of the gap.
- **Spread, order book depth**: first and further levels of bids and offers.
- **Market maker**: provider of ETF quotes who hedges in the underlying.
- **Domicile**: legal location of the fund, determining withholding tax.
- **Leveraged / inverse ETF**: daily-reset multiple of index return.
- **Compounding (path dependence)**: multi-day return differs from the multiple of index return.
- **Swap collateral reset**: periodic settlement of swap value.
- **Alternative risk premia**: systematic long-short premia: value, quality, momentum, carry.

## Formulas & Reference Tables
- `TCO = tracking difference + trading costs` (spread, commission, impact).
- `Round-trip spread cost = (Ask - Bid) / Bid`; e.g. buy 39.32, sell 39.218 gives 0.26%.
- Daily-reset leveraged ETF: `V_t = V_(t-1) x (1 + L x r_t)`; `L = -2` for 2x short. Seven-day example: index +2.03% (cumulative), ETF -5.02%.
- `TEV = std(R_ETF,t - R_bench,t)`; `TD = R_ETF - R_bench` (cumulative).
- Factor importance by investor:

| Investor | Priority |
|---|---|
| Tactical, short horizon | TEV, liquidity, spreads, execution timing |
| Buy and hold | TCO, tracking difference, domicile/tax |
| Any | Benchmark, transparency |

## Mental Models
- Use the benchmark as the first filter; two ETFs with different indices are different products.
- Use tracking difference over your holding period alongside TEV: low TEV can hide a steady drag.
- Use execution timing: trade ETFs when the underlying market is open and away from the open/close.
- Use sampling when the incremental small stocks cost more than the tracking they improve.
- Use daily-reset ETFs only for hours or days.
- Use domicile as a tax lever (Irish for US equity).

## Worked Example
TEV trap. Inputs: benchmark +3.2% over 45 days; ETF A loses a constant 0.005% per day; ETF B wanders +/-0.2% around the benchmark and ends +3.19%. Steps: A's cumulative drag = 1 - (1 - 0.00005)^45 = 0.22%, so A returns about 2.97%; A's TEV is under 0.01% because the gap is steady; B's TEV about 0.2% but its tracking difference is only -0.01%. Result: lower TEV (A) but worse outcome by 0.22%, which compounds with time. Interpretation: for horizons beyond a few days, rank ETFs on tracking difference net of costs; use TEV only to judge short-horizon precision.

## Anti-patterns
- Choosing an ETF on TER and a past chart without reading the index methodology.
- Taking TEV as a universal quality measure.
- Trading in the first and last minutes of the session or without a price reference.
- Holding leveraged inverse ETFs for weeks.
- Ignoring the swap's implicit cost because it is not in the TER.
- Ignoring domicile when buying US equity exposure.

## Practitioner Notes
- Check the order book depth to size, not just the best bid-ask, especially for orders above first-level quantity.
- Write down the benchmark, replication, TD (1, 3, 5 years), TER, spread, domicile, securities-lending policy in one comparison table for each shortlist.
- For commodities and leverage, the swap structure may be unavoidable; demand collateral transparency.
- Revisit securities-lending revenue split: it is part of the internal cost.
- Treat alternative-risk-premia ETFs as satellite diversifiers; validate correlations out of sample.

## Key Takeaways
- Benchmark selection decides most of the final performance; same market does not mean same index.
- Total cost of ownership = tracking difference (internal) + trading costs (external); weights depend on holding horizon.
- Tracking error volatility misleads over long horizons; always read tracking difference.
- Optimized sampling avoids paying for illiquid small constituents.
- Trade ETFs when the underlying market is open, away from open and close, with attention to depth.
- Leveraged daily-reset ETFs lose to compounding in volatile markets (+2.03% index, -5.02% for -2x).
- Irish domicile cuts US dividend withholding to 15% from 30%.

## Connects To
- **ch05-ch08**: passive investing, costs, replication details, smart beta.
- **ch06**: TCO and tax; **ch07**: replication, lending.
- **ch09-ch11**: manager selection framework.
- **ch13-ch14**: multimanager and active selection.
- **ch15-ch19**: alternatives and risk premia.
- **`cfa-portfolio-management` ch02, ch11**: index construction, weighting and ETFs.
