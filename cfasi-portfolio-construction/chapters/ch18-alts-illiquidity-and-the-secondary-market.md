# Chapter 18: Alternative Investments - Illiquidity and the Secondary Market
> **Source**: CFA Society Italy × Advisor Private (AP Advisor Private n. 12, Jul-Aug 2018), *Alternative Investments: L'importanza nel Wealth Management*, Chapter 4 "Illiquidità e mercato secondario" | Massimiliano Saccone, CFA (data cited from Evercore, Cogent Greenhill, Coller Capital, Preqin)

## Core Idea
Closed-end private-capital funds (private equity, real estate, infrastructure, private debt) are **structurally illiquid**: illiquidity is a contractual feature known and accepted **ex ante**, in exchange for a risk premium. It also protects the manager from margin calls and forced liquidations. Yet since the late 1980s a **secondary market** has developed where Limited Partner (LP) stakes trade over the counter, priced as a **percentage of last reported NAV**. Volume reached USD 58bn in 2017; prices recovered from deep discounts in 2008-2009 to about 95% of NAV by 2016. For an advisor the questions are: how liquid is "contractually illiquid" really, who buys and sells, how is price set, and what does a discount tell you.

## Frameworks Introduced
- **Liquidity as a trade-off (speed versus price)**: liquidity is the ability to convert to cash quickly with minimal loss, the loss being transaction costs. Block trades show the trade-off: the lower the explicit price concession a seller accepts, the longer the expected time to find a buyer. There is no sharp liquid/illiquid line; the concept is relative to size and market conditions. Market depth = how much volume a market absorbs without a significant price move.
- **Structural (contractual) illiquidity vs market illiquidity**
  - Structural: stated in the fund contract, known ex ante, accepted to extract the premium. It lets the GP choose investment and exit timing, avoid forced sales, and run operational and financial control of holdings; the cited HBS study (Gompers, Kaplan, Mukharlyamov, 2016) reports that investors expect managers to use this to manage market timing, apply operating levers and arbitrage the financial structure to deliver absolute returns at maturity.
  - Market illiquidity in other asset classes appears ex post, in stress.
  - Use: do not describe a closed-end fund as a failure of liquidity; present it as the price of the premium.
- **Why secondary pricing is hard (valuation difficulty)**: information asymmetry between buyer and seller and between each and the GP; uncertainty about investments not yet made (capital-call funds); result: a bid-ask gap that may drive the probability of closing to zero. Behavioural factors widen it: **status quo bias** (own asset valued above its purchase price), **loss aversion** (reluctance to realize a loss), **relationship concerns** (fear of damaging trust with the GP). Differences in liquidity premium and horizon also matter.
- **Secondary transaction mechanics**: the buyer pays a price and, with GP consent, takes over all rights and obligations, including **unfunded commitments**. Price is quoted as % of the latest NAV (usually the quarter-end). Settlement adjusts for cash flows between the NAV reference date and the closing date: add capital calls paid after the NAV date and deduct distributions received.
- **Sellers' motives (Evercore 2016 survey, share of volume)**: portfolio reshaping about 65%; GP-led restructuring about 23%; regulatory pressure (Basel III, Solvency II, Volcker; see ch16) about 9%; financial distress about 1%; other about 2%. Seller types spread across pension funds, asset managers, family offices, endowments/foundations, financial institutions and sovereign funds (the extracted figure is garbled; treat the type split as approximate).
- **Buyers' benefits**: a shorter-duration, lower-risk exposure than a primary commitment: the portfolio is largely formed, so the investor escapes the blind pool and the early J-curve, receives distributions sooner and gets faster capital turnover, which lifts IRR while multiples may be lower. Structures are flexible: seller financing, leverage from intermediaries, and **preferred equity** funds that provide liquidity against a coupon plus a share of upside.
- **Market growth drivers**: pre-crisis fundraising boom, regulatory change, crisis liquidity needs, narrower discounts, credit availability, structuring flexibility, GP-led deals (managers originating secondaries to manage investor relationships and fund restructurings). The market moved from a few pioneers buying leveraged buyout and venture stakes (late 1980s) with few buyers, forced sellers and steep discounts to a deep, multi-player market.
- **Market sizing figures (as reported)**: annual volume USD 58bn in 2017 (reported growth over 21% per year; the chart series is garbled, see Issues); secondary fundraising USD 43bn+ in 2017 (Preqin), over USD 30bn in the market in early 2018 with one fund targeting USD 12bn (a record); dry powder about USD 90bn, roughly 1.6x 2017 volume (checks: 90 / 58 = 1.55).
- **Execution process via an intermediary (managed auction)**: Phase 1 - idea generation: targets, motives, market conditions, valuation parameters. Phase 2 - structuring: legal, tax, regulatory aspects and the exit strategy; short-list of counterparties. Phase 3 - execution: due diligence, offering memorandum, two bid rounds (non-binding from all invited, then binding subject to due diligence), GP consent, then the sale and purchase agreement for legal and financial settlement. Digital platforms help counterparty discovery but the process remains traditional.
- **"Modified bottom-up" valuation (Cogent Greenhill)**: combine fundamental inputs with statistics and macro data. Steps: (1) collect financial reports, the limited partnership agreement and placement memorandum; (2) model the **unfunded multiple** (expected future calls) from statistics; (3) forecast exit values and timing from GP guidance, market analysis, comparable data and industry statistics; (4) combine into gross cash flows; (5) apply the **waterfall** (distribution priority per the fund's legal terms) to get net distributions to the investor; (6) discount at the investor's required return.
  - Failure mode: prices published as averages refer to plain-vanilla deals; asset type, portfolio size, seller urgency and complexity move the actual price.
- **Price trend (Coller Capital)**: secondary prices as % of NAV fell sharply after 2007 (roughly 109% in 2007, down to the high 50s-70s in 2008-2009) and climbed back toward the mid-90s by 2014-2016. Drivers beyond better NAV quality: equity market recovery, easy exit environment, abundant credit and buyers (figure values read from a garbled chart; see Issues).

## Key Concepts
- **Illiquidity premium**: extra expected return for accepting the inability to sell quickly.
- **Structural illiquidity**: contractual lock-up of capital; known ex ante.
- **Secondary transaction**: sale of an existing LP stake in a fund to another investor.
- **LP / GP**: Limited Partner (investor) and General Partner (manager, AIFM).
- **Unfunded commitment**: capital promised but not yet called; transfers to the buyer.
- **NAV-based pricing**: quoting price as a percentage of reported NAV; discount means price below 100%.
- **Bid-ask spread**: divergence between asking price and bid that can eliminate the deal.
- **GP-led secondary / restructuring**: transaction originated by the manager, such as extending a fund's life or moving assets to a new vehicle.
- **Preferred equity secondary**: liquidity provided as a fixed coupon plus a share of upside.
- **Dry powder**: capital raised but not yet invested; here it signals buyer capacity.
- **Waterfall**: legal priority of cash distribution among investors and the GP.
- **Block**: a large trade needing special handling to limit market impact.
- **Blind pool**: exposure to a portfolio not yet assembled; secondaries avoid most of it.

## Formulas & Reference Tables
- Secondary price (% of NAV) `= bid price / last reported NAV`.
- Cash settled `= %NAV x NAV + capital calls after NAV date - distributions after NAV date`.
- Intrinsic value (modified bottom-up): `V = sum_t E[net distribution_t - calls_t] / (1 + k)^t`, with `k` the buyer's required return; discount to NAV `= 1 - V / NAV`.
- Dry-powder coverage `= dry powder / annual volume` (about 1.6x in 2017).

| Seller reason (2016) | Share of volume |
|---|---|
| Portfolio reshaping | ~65% |
| GP-led restructuring | ~23% |
| Regulatory pressure | ~9% |
| Financial distress | ~1% |
| Other | ~2% |

## Mental Models
- Use "illiquidity is the fee for the premium" when explaining lock-ups to clients; use the secondary market as a contingency exit, not a plan.
- Use secondary price as % of NAV as a sentiment gauge for private markets: below 85% signals stress, mid-90s a healthy market.
- Use the buyer-side lens (shorter duration, no blind pool, faster IRR) when judging secondary funds.
- Use the bid-ask gap plus behavioural biases to predict why deals fail even when value exists.
- Use reporting-date adjustments every time: a quoted % of NAV is not the cash price.

## Worked Example
**Secondary price settlement.** A fund interest has quarter-end NAV 100. Bid is 95% of NAV. Between quarter-end and closing the fund called 5 and distributed 8.
- Price on NAV = 95.
- Adjust: `95 + 5 - 8 = 92` cash paid by the buyer. (Buyer also assumes any unfunded commitment.)
- Interpretation: the headline "95% of NAV" hides about 8 points of difference versus a naive NAV-based expectation once cash flows are settled.

**Modified bottom-up value (toy).** NAV 40; unfunded 10 called in year 1; net cash flows after waterfall: year 1 -10, year 2 0, year 3 +25, year 4 +30, year 5 +15; buyer's required return 12%.
- PV `= -10/1.12 + 0 + 25/1.12^3 + 30/1.12^4 + 15/1.12^5 = -8.93 + 17.79 + 19.07 + 8.51 = 36.44`.
- Price as % of NAV `= 36.44 / 40 = 91.1%`, i.e. a 8.9% discount.
- Interpretation: a seller refusing anything below 100% of NAV will see no deal at a 12% target return; either the cash-flow forecast or the required return must move.

## Anti-patterns
- Selling "liquidity via the secondary market" as a guarantee; depth and discount vary with the cycle.
- Treating discounts of 2008-2009 as a permanent feature or 2016 pricing as permanent.
- Comparing deal prices without adjusting for asset type, size, urgency and complexity.
- Forgetting that unfunded commitments follow the stake.
- Ignoring GP consent and information rights when planning an exit.

## Practitioner Notes
- When a client needs liquidity, expect a multi-stage intermediated auction (two bid rounds, GP consent) and prepare due-diligence materials early.
- Understand your seller category: portfolio reshaping sellers accept fair prices; distressed sellers are rare in recent data (about 1%), so a "distressed bargain" is unlikely.
- Sentiment: with abundant dry powder and credit, prices rose; reverse conditions (scarce credit, high calls, low distributions) reverse them.
- Use the secondary market for diversification and J-curve mitigation as a buyer as well, via specialist funds.

## Key Takeaways
1. Closed-end illiquidity is contractual, known ex ante, and compensated by a premium.
2. Illiquidity also protects GPs from forced selling and gives timing control.
3. Secondary prices are quoted as % of NAV and settled with call and distribution adjustments.
4. Information asymmetry and behavioural biases create bid-ask gaps that can block trades.
5. Volume reached USD 58bn in 2017; dry powder around USD 90bn.
6. About two-thirds of volume is portfolio reshaping, not distress.
7. Buyers gain shorter duration, no blind pool and faster IRR.
8. Prices of the best plain-vanilla assets improved from the high 50s-70s % of NAV (2008-09) to the mid-90s.

## Connects To
- **ch15**: the illiquidity premium as a reason to hold alternatives.
- **ch16**: regulatory drivers (Basel III, Solvency II, Volcker) behind seller pressure.
- **ch17**: liquidity and funding risk, IRR, multiples and NAV lag; denominator effect.
- **ch19**: product innovation attempting to solve structural illiquidity (listed vehicles, co-investment, feeders, auctions).
- **`cfa-alternative-investments`**: CFA treatment of private equity valuation and exits.
