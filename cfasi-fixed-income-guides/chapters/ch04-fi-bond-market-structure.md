# Chapter 4: The Fixed Income Market: Introduction and Peculiarities
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 4 (Il mercato dei titoli a reddito fisso: un'introduzione ed alcune peculiarità) | Emanuele Gerletti, CFA

## Core Idea
The bond market is far larger than the equity market but is mostly over-the-counter (OTC), institutional and fragmented: one issuer can have hundreds of lines, so liquidity is concentrated in a few large issues and screen prices are often indicative, not executable. New issues reach investors via auctions (governments) or bookbuilding (corporates). The 2015-2018 regime of central bank quantitative easing and negative rates compressed yields across the asset class, creating an exit risk because the secondary market's door is narrow.

## Frameworks Introduced
- **Primary market channels**
  | Channel | Used by | Mechanism |
  |---|---|---|
  | Competitive (yield) auction | Italian BOT (short bills) | Bids in yield; each allocated bid gets its own yield, lowest yields first until quantity is filled; pro-rata at the last yield |
  | Marginal (price) auction | Medium/long Italian BTP | All winners pay the same marginal price (lowest accepted price); quantity set discretionally between announced min and max |
  | Bookbuilding | Corporates | Syndicate of banks builds an order book; priced by price talk |
- **Auction safeguards**: an exclusion yield (maximum acceptable) and a safeguard yield (minimum acceptable) are computed to ignore opportunistic bids far from market; specialists/primary dealers are obliged to bid and quote, and in return get exclusive access to supplementary placements.
- **Bid-to-cover ratio** = demand ÷ supply. Well above 1 signals strong demand, read as good news for the issuer.
- **Bookbuilding sequence**: (1) issuer picks a global coordinator (lead manager) and bookrunners; (2) feasibility discussion (size, collateral, covenants, single or multi-tranche); (3) announcement; (4) roadshow; investors give yield indications; (5) initial price talk (IPT); (6) book open 1-2 days, orders can be limit orders on yield or size; (7) book closed, bond "launched" hours later; (8) secondary trading starts. A grey market (pre-market) runs from announcement to issue, quoted as discount/premium to re-offer price, and does price discovery.
- **Liquidity read-through from a dealer screen (ALLQ-type view)**: check (1) outstanding size, (2) number of contributing dealers, (3) bid-offer width, (4) quoted size, (5) issuer rating, (6) currency versus issuer's home market. Firm versus indicative quotes: screen prices are requests, not guaranteed fills.
- **Negative-yield regime diagnosis**: low inflation (HICP) + 5y5y inflation-swap breakeven falling to 1.25% (July 2016) → ECB negative deposit rate, QE (government, covered, ABS, IG corporates) → yields collapse, even in segments not bought.

## Key Concepts
- **OTC market** — private bilateral trading, not on a regulated exchange; most bond trading.
- **Market maker vs broker** — a market maker holds inventory and quotes two ways; a broker matches clients and generally closes both sides the same day.
- **Primary dealers / specialists** — government securities dealers with quoting and bidding obligations.
- **Global coordinator / lead manager** — bank that structures and steers the issue; **bookrunners** gather investor orders.
- **Initial price talk (IPT)** — first indicated yield level; usually tightens as demand builds.
- **Re-offer price** — issue price to investors.
- **Joint Lead Managers' interest** — banks' own orders in the book (akin to underwriting).
- **Grey market (when-issued)** — pre-issue forward trading, quoted as spread to re-offer price.
- **Clearing (Euroclear, Clearstream)** — delivery versus payment settlement.
- **Benchmark size** — large outstanding amount; drives the number of dealers and thus liquidity.
- **Liquidity risk** — inability to trade size at a fair price, quickly, at low cost.
- **Negative interest rate policy (NIRP)** — central bank charging banks on reserves; used by ECB and also Sweden, Switzerland, Denmark, Japan.
- **Quantitative easing (QE)** — central bank asset purchases to lower yields and lift inflation.
- **5y5y breakeven inflation** — expected average inflation over five years starting in five years, from inflation swaps; watched by the ECB.
- **Exit strategy risk** — disorderly yield rise when central banks reduce support.

## Formulas & Reference Tables
- `Bid-to-cover = Total demand / Amount offered`.
- `Bid-offer spread = Offer price − Bid price`, in price points (cents).
- Observed liquidity ladder (guide, 2 March 2018 screen, indicative):
  | Bond | Size | Rating | Min / typical bid-offer (cents) |
  |---|---|---|---|
  | BTP 2.05% 2027 | EUR 19.19bn | BBB | below 5 / 5-10; about 10 dealers for EUR 5-10m |
  | Enel EUR 2026 | EUR 1.25bn | BBB | 15 / 30 |
  | Fiat Chrysler EUR 2024 | EUR 1.25bn | BB- | 36 / 50 |
  | Moby 7.75% 2023 | EUR 300m | B+ | 95 / about 150; quoted size mostly EUR 1m |
  | Enel USD 2027 / Fiat Chrysler USD 2023 | USD 2bn / USD 1.5bn | BBB / BB- | about 75 / about 90 (versus about 25 / 50 for EUR lines) |
- Market data cited: negative-yield government debt about USD 7.4 trillion (September 2017); EUR 5y5y breakeven 1.71% (2 March 2018); 10-year BTP yield about 1.5% versus about 7% at the 2011 peak; Bund 10-year negative mid-2016; European HY yield-to-worst below 3%.

## Mental Models
- Use "size, dealers, rating, currency" as a four-line liquidity checklist before buying a bond for a portfolio that may need exits.
- Use the bid-to-cover ratio as a quick sentiment signal on a sovereign auction, not as a valuation signal.
- Use "central bank as price-insensitive buyer": yields can detach from fundamentals, and the exit can be abrupt.
- Use EUR-denominated lines for a European issuer when liquidity matters; foreign-currency lines carry a liquidity discount.

## Worked Example
Liquidity cost on EUR 1m of Fiat Chrysler EUR 2024 at mid-price 108.70, bid-offer 0.50 points (50 cents).
1. Round-trip cost = full spread = 0.50 points = `0.50/108.70 = 0.46%` of notional, i.e. EUR 4,600 per EUR 1m round trip (half-spread 0.23%, EUR 2,300 each way).
2. Same trade in the BTP at 7 cents spread on 101.30 price: `0.07/101.30 = 0.07%`, EUR 700 round trip.
3. For a bond with 3.75% coupon and about 5.5 years left, EUR 4,600 equals roughly 0.5% of price, or about 1 year of the BB- spread premium over BTP carry if the position is held only a year.
Interpretation: for a one-year hold the transaction cost for the BB- bond is about 6.6x that of the BTP; for a five-year hold, it amortizes to about 0.09% a year.

## Anti-patterns
- Taking a screen quote as a guaranteed price for size.
- Judging liquidity by the number of lines of an issuer rather than by the size of the specific bond.
- Buying small foreign-currency tranches of an issuer for a pick-up without discounting the poorer liquidity.
- Assuming that low yields are permanent because the central bank said "for a long time".
- Treating a high bid-to-cover alone as proof of fair pricing.

## Practitioner Notes
- Post-2008 regulation shrank dealers' balance sheets, so market making capacity fell; brokers partly replaced them but with smaller size.
- Stress periods (summer 2011, 2015-16 spread correction) saw screen bids 25-50 cents above real execution levels on peripheral corporates.
- In the guide's view, the exit from QE should be gradual because crowded exits through an OTC market could trigger gapping.
- Bank and insurer margins suffered under low rates, which is the commonly cited argument for eventual rate normalization.

## Key Takeaways
1. Bonds trade OTC; institutional investors are the main counterparties, retail is marginal.
2. Governments auction (competitive on yield for bills, marginal on price for BTPs); corporates bookbuild.
3. Bid-to-cover above 1 signals demand; the exclusion and safeguard yields protect the issuer from outliers.
4. The grey market does price discovery before issue and quotes the bond as discount/premium to re-offer.
5. Liquidity depends on size, dealer count, rating, currency; bid-offer spreads rise as each worsens.
6. Screen prices are indicative; firm size is often a small fraction of what the screen suggests.
7. QE and negative rates compressed yields across the asset class; exit risk is liquidity risk.

## Connects To
- **ch02**: liquidity risk definition and bid-ask measure.
- **ch03**: issuer types referenced in the liquidity comparison.
- **ch05**: curves and spreads that auction and bookbuilding price off.
- **ch07**: access routes (funds, ETFs) that transform bond illiquidity into daily liquidity.
- **ch08**: active versus passive implementation and liquidity management.
- **`cfa-fixed-income` ch02**: primary and secondary market mechanics in the CFA curriculum.
