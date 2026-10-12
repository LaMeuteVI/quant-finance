# Chapter 5: Passive Investing: Allocation Role, Active-vs-Passive Evidence and Market Risks (Passive Investments)
> **Source**: CFA Society Italy x Advisor Private, "Passive Investments" guide (Advisor Private no. 26, 2020), Chapter 1 | Giancarlo Sandrin, CFA; the closing insert on ETF liquidity in stressed markets is sponsored by Amundi (Matthieu Guignard) and is attributed below

## Core Idea
Index funds and ETFs are not "no-thinking, static" tools: they are the building blocks ("mattoncini") of strategic and tactical asset allocation. Once the allocation is the main performance driver, choosing passive for each block removes manager-selection and alpha-selection risk, at low cost and with transparency. The chapter backs this with SPIVA scorecards (most active funds trail benchmarks over long horizons), discusses industry effects, and tests the common worries about passive (bubble, crowded rebalancing, closing-auction concentration, ETF liquidity in stress, using the March 2020 episode).

## Frameworks Introduced
- **Three asset-allocation modes (Jennings and Podkaminer, CFA Institute overview)**: asset-only (optimize for a risk level using class return, volatility, correlation expectations; typical for sovereign funds and standard individual mandates), liability-relative / LDI (institutional; invest to meet liability flows, manage excess assets separately), goal-based (individuals; start upstream by defining, ranking and testing the feasibility of goals). In all three, an index vehicle per sleeve is the natural implementation, and active vs passive becomes a marginal, per-sleeve choice.
- **Passive as an efficiency decision, not only a cost decision**: cost is one reason but not the only one. Test per asset class: how efficient is it (SPIVA hit rate), how persistent is outperformance, how costly is constant manager due diligence. Passive removes fund/manager selection and the alpha-mistake risk; active remains useful for selecting managers with a reliable edge or specific risk/factor exposures, or strategies tapping non-market risk factors that decorrelate from traditional classes.
- **Zero-sum argument (Sharpe 1991; Malkiel 2003)**: before costs the average active dollar earns the market return; after costs active must trail. As industry costs and models standardize, the theory fits better, so the practical result is passive as default and active as a justified exception.
- **SPIVA evidence read-through**: percentages of funds underperforming a benchmark (Europe, mid-2019): European equity vs S&P Europe 350: 1y 90.2%, 3y 82.6%, 5y 77.5%, 10y 88.2%; Global equity vs S&P Global 1200: 87.2, 90.6, 94.9, 98.6; US equity vs S&P 500: 84.3, 86.2, 91.9, 97.7; Emerging markets: 58.3, 82.6, 91.3, 95.1; Italy: 81.0, 82.4, 54.0, 69.9. US (SPIVA, June 2020) large caps: 5y 77.97%, 3y 71.24%, 1y 63.17%; mid caps 59.34 / 49.66 / 43.69; small caps 66.67 / 56.70 / 46.79; multi-cap 78.02 / 65.61 / 65.02. Pattern: failure rates rise with horizon; in the US over 1 and 3 years mid and small caps flip to a minority underperforming. Active selection is a continuous process because yesterday's winners do not persist.
- **Risk checklist for passive vehicles** (test each claim with data):
  1. Bubble in large caps from passive flows? Question: is it index flows or monetary policy? Facts quoted: US fund assets end 2019: passive 13.9 trn USD vs active 8.4 (Lipper), US equity passive 5.4 vs active 5.2 trn; S&P 500 cap about 24 trn, MSCI USA about 28 trn; BIS (2018 review) estimates passive about 5% of market cap in most markets, ETF turnover about 15% of US equity volume (2017); S&P 500 futures notional about 2 trn USD vs about 0.8 trn in ETFs on the same benchmark.
  2. Rebalancing crowds: quarterly index changes force buying/selling (stocks entering/leaving; bonds moving between investment grade and high yield). Effect should mean-revert and creates opportunities for active managers; it has also pushed "alternative" indices.
  3. Closing-auction concentration: a rising share of volume trades at the close (author's Bloomberg data, five European markets, 15 Dec to 15 Jan windows 2014-2020) for index alignment, mostly around the rebalancing season; attribution to passive vs active funds cannot be isolated, since active managers also seek liquidity windows.
  4. ETF liquidity in stress (Covid-19, spring 2020): author analysis on four euro corporate-bond ETFs (iShares IEAC, Xtrackers XBLC, Amundi CC4, Lyxor CRPE) against the Bloomberg Barclays Euro Corporate Bond index and some constituent bonds on Frankfurt: ETF prices tracked the index; ETFs traded at a slight discount at the peak of stress, read as a liquidity premium the ETF gives over its underlying basket; trading volumes held up. Jane Street (April 2020) found US credit ETF spreads widened but ETFs let investors transfer risk efficiently at transparent prices. Limitation: off-exchange (OTC/MTF) trading in Europe is reported but not centrally gathered (unlike US TRACE), so analyses see only the on-exchange part.
- **Industry impact (Oliver Wyman / Morgan Stanley 2019)**: global asset-management profit pool about 326 to 345 bn USD (2018 to 2023f, +1% CAGR). Growth shares by 2023f: EM clients +60%, private markets +51%, solutions +26%, passive +8%, hedge funds -2%, core active -36%. Margins squeezed by low rates and fee pressure, not only passive; solutions and mass personalization (technology) are the growth, and low-cost liquid passive blocks are the enabler of mass-market customization.
- **Amundi insert on ETF liquidity (sponsored)**: ETF liquidity has three layers: exchange-visible liquidity, secondary-market liquidity (natural investor-to-investor trades plus market makers, can function even if the basket is illiquid or closed) and underlying (primary-market) liquidity, reached by creating or redeeming units. Spring 2020: spreads widened (reflecting weak underlying liquidity) but execution was immediate, ETF volumes were two to three times 2019 averages, and credit ETF prices provided executable price discovery when cash bond quotes were stale (BIS Bulletin no. 6, April 2020). Provider checklist: assess underlying liquidity before launch, use UCITS rules, apply index liquidity filters (issue size, minimum rating), standardized disclosure, broad network of authorized participants and market makers (Amundi cites 70+ counterparties incl. 17 electronic market makers). Treat as vendor commentary.

## Key Concepts
- **Index fund / ETF**: vehicle replicating a market index at low cost and with holdings transparency.
- **SPIVA (S&P Indices Versus Active)**: scorecard of the share of active funds beating their benchmark.
- **Asset-only / LDI / goal-based allocation**: three allocation modes.
- **Zero-sum game**: market return is average active return before costs.
- **MiFID II cost transparency**: aimed to expose costs; the author sees little retail pushback in Italy so far.
- **Crowded trading**: concentrated flows at index changes affecting small caps and bonds changing credit bucket.
- **Closing auction share**: percentage of daily volume executed at the close.
- **Premium / discount to NAV**: ETF price versus the net asset value of the basket.
- **Price discovery**: ETF prices revealing the value of an illiquid underlying when bonds are not tradable.
- **Authorized participant / market maker**: counterparty that creates/redeems units and quotes spreads.
- **TRACE**: US public database of OTC bond trades.
- **Futures notional**: size of derivatives replicating indices, historically larger than ETF assets.

## Formulas & Reference Tables
- `Active return = Rp - Rb` (before costs, market-weighted average over all investors = 0; after costs < 0).
- `Premium/discount = (Price - NAV) / NAV`.
- SPIVA figures: see the framework above (all in percent of funds underperforming).
- Note: the source's Figure 1 shows the 2018 profit pool as 326 bn and 2023f as 345 bn; (345/326)^(1/5)-1 = 1.1%, consistent with the stated +1% CAGR (verified).

## Mental Models
- Use passive for the blocks you cannot expect to beat (efficient large-cap, global, US equity); use active where selection has a plausible edge and you can afford continuous due diligence.
- Use SPIVA persistence tables, not one-year hit rates, to judge manager-selection odds.
- Use ETF price as a price-discovery gauge when the bond market is frozen, but expect wider spreads.
- Use a compare-to-futures sanity check before claiming that passive causes a bubble.
- Use the allocation first: if the sleeve choice drives results, passive vs active is second-order.

## Worked Example
Check the SPIVA cohort arithmetic. Inputs: US large caps over 5 years, 77.97% of active equity funds underperform S&P 500. Steps: share outperforming = 100 - 77.97 = 22.03%; for a selector who picks one fund at random, P(beating) = 22%; adding a typical cost drag, the odds do not improve with hindsight because winners rarely persist. Also compute the passive share of US equity assets: 5.4 / (5.4 + 5.2) = 50.9%. Interpretation: passive crossed half of fund assets, but fund assets are tiny relative to market cap: 10.6 trn of funds against about 24-28 trn of index market cap, so most shares are still held directly or by active funds.

## Anti-patterns
- Equating "passive" with "static" or "no allocation decision".
- Justifying passive only by fee level.
- Judging active managers from 1-year hit rates.
- Assuming an ETF always trades exactly at NAV in stress; ignoring widened spreads.
- Using on-exchange volume alone to measure European ETF liquidity.
- Blaming passive for index-rebalancing effects that active flows also create.

## Practitioner Notes
- When rates are near zero, a 1-2% fee consumes the whole expected return of a low-risk portfolio; that is when passive blocks win commercially.
- Active manager selection is continuous: re-run due diligence, do not "select and forget".
- Quarterly index events are tradeable by active managers (supply of liquidity at the rebalance).
- Large-cap ETFs for mass-market customization: low cost, liquid, accessible.
- Provider-supplied liquidity evidence (Amundi) and independent evidence (BIS, Jane Street) point the same way; weigh both.

## Key Takeaways
- Asset allocation drives results; index products are its implementation blocks.
- SPIVA data show a large majority of active funds trail over 5 to 10 years, with shorter-horizon exceptions in US mid and small caps.
- Cost is one reason to go passive; manager-selection and alpha risk are others.
- Passive is a modest share of market cap (about 5% in many markets per BIS), so bubble claims need caution.
- Index events and closing-auction trading are real frictions but also opportunities for active managers.
- In March 2020 credit ETFs traded at wider spreads, at slight discounts, and served as price discovery.
- Industry growth lies in solutions, private markets and EM clients; core active shrinks.

## Connects To
- **ch02**: active vs passive at AA level and core-satellite.
- **ch03**: benchmarks, tracking error and performance measures.
- **ch06**: how to choose among passive instruments (ETF vs index fund, replication).
- **ch07**: management of passive funds ("more active than it seems").
- **ch09-ch14**: ETF and fund selection.
- **`cfa-portfolio-management` ch02-ch03, ch11**: indexes, market efficiency, ETFs.
