# Chapter 11: Exchange-Traded Funds: Mechanics and Applications
> **Source**: CFA Program Curriculum 2022, Level II, Reading 38 · Portfolio Management | Joanne M. Hill, PhD, and Dave Nadig

## Core Idea
An ETF is a fund whose shares are created and redeemed in kind by a small set of authorized participants (APs) in the primary market, while all other investors trade it intraday on exchanges (secondary market). This arbitrage loop keeps the price close to NAV, shields buy-and-hold holders from other investors' trading costs, and makes ETFs more tax fair and efficient than mutual funds. To use ETFs well you must measure the true all-in cost (fee + tracking difference + spread + premium/discount), match the ETF to the holding period and use (core, tactical, efficiency, factor), and know the structural risks (counterparty in ETNs/swaps, closures, leveraged-reset math).

## Learning Outcomes Covered
- Explain creation/redemption and the role of authorized participants
- Describe how ETFs trade in the secondary market (settlement, US vs Europe)
- Describe sources of ETF tracking error
- Describe factors affecting ETF bid-ask spreads
- Describe sources of premiums and discounts to NAV
- Describe the costs of owning an ETF (explicit and implicit, holding-period effect)
- Describe ETF risks (counterparty, closure, investor-related)
- Identify portfolio uses of ETFs (efficiency, asset class exposure, active/factor)

## Frameworks Introduced
- **Creation/redemption arbitrage loop**: The AP delivers the creation basket (a daily-published list of securities, plus possibly cash) to the issuer and receives a creation unit (typically 50,000 shares; range 10,000 to 600,000) of ETF shares; redemption is the reverse and returns a redemption basket.
  - When to use: to predict whether the ETF will trade at a premium or discount, and who bears costs.
  - How: (1) ETF price > fair value (iNAV): AP buys basket, delivers it for new ETF shares, sells ETF shares; this adds supply of ETF and demand for the stocks, closing the premium. (2) ETF price < fair value: AP buys ETF shares, redeems them for the basket, sells the basket. (3) Action occurs only if the gap exceeds the AP's costs (trading costs, creation fee, settlement/tax, basket risk).
  - Why it works / failure mode: the AP hedges instantly so it has no economic exposure when ETF and basket are fairly priced. It breaks when the basket is hard to trade (high yield, foreign hours closed), when creations are halted (ETNs: a halted UBS ETN traded above 5% premium), or in stress.
- **Arbitrage gap / no-arbitrage band**: ETF trades within a band around fair value whose width = AP's cost of arbitrage + risk premium for volatility/liquidity. Band can be one tick for liquid US equity ETFs and above 1% for high-yield bond ETFs.
  - When to use: to judge expected premium/discount range. Issuers widen or narrow it via basket size, creation fee (US example: US$50 for an inflation-linked Treasury ETF vs US$28,000 for an ex-US small-cap ETF), and cash vs in-kind creation.
- **Tracking difference vs tracking error**: Tracking difference = cumulative (or rolling 12-month) fund return minus index return; tracking error = standard deviation of the daily return differences (reported annualized, typically over 12 months).
  - When to use: tracking difference to see what the investor actually earned vs index and compare with the expense ratio; tracking error to see consistency. Always report a central tendency (mean/median) plus a dispersion (stdev/range).
  - Why it works / failure mode: tracking error alone hides the sign and whether errors are concentrated in a few days. The curriculum summary states tracking difference is more useful than TE.
- **Total cost of ownership (holding-period cost)**: Holding period cost = round-trip trade cost + management fee prorated for the period (see formulas).
  - When to use: choosing an ETF for a given horizon. Short horizon: choose liquidity (tight spread, deep volume), even at a higher fee. Long horizon: choose the lowest fee and tracking difference.
- **ETF use taxonomy**: (1) Portfolio efficiency (cash equitization, rebalancing, completion, transition); (2) Asset class exposure management (core strategic, tactical, thematic); (3) Active and factor investing (smart beta, risk management, alternative weighting, active, dynamic multi-asset).

## Key Concepts
- **Authorized participant (AP)**: large broker/dealer, often a market maker, authorized by the issuer to create/redeem shares in kind; the only entity that can do so.
- **Primary market**: OTC in-kind exchange between AP and issuer; **secondary market**: exchange trading among all other investors, with settlement through the normal cash-market process.
- **Creation basket / redemption basket**: the published securities list used for creation; the redemption basket can differ (e.g., to hand out low-cost-basis lots).
- **Creation unit**: the block size of an AP transaction, usually 50,000 shares.
- **iNAV (indicative NAV)**: intraday fair value per share based on the day's creation basket, disseminated by the exchange; NAV is the end-of-day value.
- **Premium/discount**: end-of-day = (price - NAV)/NAV; intraday = (price - iNAV)/iNAV.
- **Tax fair**: selling by other investors does not force portfolio sales or gains onto remaining holders. **Tax efficient**: the issuer redeems out low-basis lots, raising basis and reducing distributed gains.
- **Representative sampling / optimization**: holding a subset of the index; cheaper for illiquid indexes but widens tracking range (one sampled Asia ETF held 763 of 2,342 index names, with a 12-month tracking range of 1.95% vs 0.57% for the full-ish EM ETF).
- **Exchange-traded note (ETN)**: unsecured, unsubordinated debt of the issuing bank promising index return minus fees; holds no assets, so counterparty risk can be 100%.
- **Synthetic (swap-based) ETF**: gets exposure through OTC total return swaps; carries settlement/counterparty risk (mitigated by frequent settlement and T-bill collateral).
- **Security lending**: lending holdings to short sellers for fees; a negative cost (income); collateral typically 102% domestic, 105% international.
- **Cash equitization / cash drag**: investing idle cash in ETFs to stay at benchmark exposure; cash drag is mis-tracking from uninvested cash.
- **Smart beta ETF**: rules-based index weighted or screened on factors (value, dividend, quality, low vol, momentum), holdings transparent; about 20% of ETF assets (2018).
- **Soft closure**: creation halt or change of the tracked index/strategy, without liquidating the fund.

## Formulas & Reference Tables
- End-of-day premium/discount (%) = `(ETF price − NAV per share) / NAV per share`
- Intraday premium/discount (%) = `(ETF price − iNAV per share) / iNAV per share`
- Tracking difference (period) = `R_ETF − R_index` (rolling 12-month; expect ≈ −expense ratio before securities lending income)
- Tracking error = `σ(R_ETF,t − R_index,t)` (daily); annualized TE = `σ_daily × √252` (monthly: `σ_m × √12`)
- Round-trip trading cost (%) = `2 × one-way commission % + 2 × (½ × bid-ask spread %)` = `2c + s`
- Holding period cost (%) = `round-trip trading cost + (months/12) × annual management fee` (no compounding)
- Quoted ETF spread ≲ `± creation/redemption fees and direct costs + underlying bid-ask spreads + compensation for carry/hedge risk + market maker target profit − discount for chance of offsetting order flow`
- Leveraged/inverse ETF: daily return = `k × R_index,t` (k = 3, 2, −2 ...), NAV_t = NAV_{t−1}(1 + k·R_t); swap exposure reset = `k × NAV_t − existing exposure`.

| Cost factor | Depends on holding period? | Explicit/Implicit | Dominates for |
|---|---|---|---|
| Management fee | Yes | Explicit | Long-term holders |
| Tracking error/difference | Yes | Implicit | Long-term holders |
| Commission | No (one-time) | Explicit | Short-term traders |
| Bid-ask spread | No | Implicit | Short-term traders |
| Premium/discount | No | Implicit | Short-term traders |
| Portfolio turnover | Yes | Implicit | Long-term |
| Taxable gains | Yes | Explicit | Taxable investors |
| Security lending | Yes | Implicit (negative cost) | n/a |

| Source of tracking difference | Direction / note |
|---|---|
| Fees and expenses | Negative, about equal to expense ratio; the largest and most predictable |
| Representative sampling | Either sign; widens range, regime dependent |
| ADRs/GDRs or other ETFs held | Timing and pricing mismatches |
| Index changes | Trade timing; fixed via market-on-close with APs; small, infrequent |
| Fund accounting (FX strike time, bond pricing time) | Noise in daily differences |
| Tax and regulation (withholding, transaction taxes) | Usually negative |
| Security lending, dividend recapture | Positive (negative cost) |

| Settlement | US | Europe |
|---|---|---|
| Cycle | T+2 via NSCC/DTC; market makers get up to 6 days | Fragmented across about 29 CSDs; large OTC negotiated trades |

Spread benchmarks (asset-weighted average, Dec 2018): US equity 0.03%, US fixed income 0.02%, intl equity 0.05%, leveraged 0.29%, alternatives 0.18%. Median spreads are much wider (0.14% to 0.38%): small ETFs are costlier than the weighted figure suggests.

## Mental Models
- **The AP is a free option on the gap, not a charity**: expect premium/discount to stay inside the AP's cost band; widen the band when the underlying is illiquid, foreign, or closed.
- **Sell the ETF, buy the basket**: the secondary market spread already contains the AP's costs; transacting holders pay, long-term holders are shielded.
- **Short horizon: pay for liquidity; long horizon: pay for low fee.** A 0.25% round trip exceeds most annual fees.
- **ETF as price discovery vehicle**: when bonds or foreign stocks are stale or closed, a premium/discount can be the ETF being right and the NAV stale, not mispricing.
- **Daily-reset products are path dependent**: leveraged/inverse ETFs are one-day tools (about a month at most); beyond that they must be rebalanced by the investor.
- **Credit risk lens for ETNs and deposit-based funds**: monitor the issuing bank's 1-year CDS; a spread above about 5% signals serious default concern.

## Worked Example
**1. Holding-period cost (curriculum numbers, recomputed).** Commission 0.05% each way, bid-ask spread 0.15%, fee 0.15%/yr.
Round trip = 2(0.05%) + 0.15% = 0.25%.
3 months: 0.25% + (3/12)(0.15%) = 0.2875% ≈ 0.29%. 12 months: 0.40%. 3 years: 0.25% + 0.45% = 0.70%.
Trading share of total: 0.25/0.2875 = 87% (the curriculum shows 86% using the rounded 0.29%) (3m), 62.5% (12m), 36% (3y). Interpretation: for a tactical 3-month trade the fee is nearly irrelevant; for a 3-year hold it is 64% of cost.

**2. Tracking difference and error.** 12 monthly index returns with an ETF that has a 0.20%/yr fee and tiny noise: mean monthly difference × 12 = −0.19%; cumulative tracking difference = −0.196%; annualized tracking error = stdev of monthly differences × √12 = 0.043%. Interpretation: TD ≈ −fee (as expected for a fully replicating fund); TE is tiny, so the fund is consistent. A 0.50% TE with the same TD would signal sampling/regime risk.

**3. −2× inverse ETF over two days (curriculum Exhibit 15).** Index 100 → 110 (+10%) → 99 (−10%). ETF NAV: 100 → 80 (−20%) → 96 (+20%). Index two-day return −1%, naive −2×(−1%) = +2%, actual fund −4%. Volatility drag, not a mistake.

**4. 3× fund reset.** NAV £100, exposure £300; index +5% → NAV £115, exposure £315; needed £345, so increase swap exposure by £30 (buy more on up days, sell on down days, reinforcing the trend).

## Anti-patterns
- **Judging an ETF by expense ratio alone**: tracking difference, spread, and premium/discount are all real costs; compare rolling 12-month tracking difference with the fee.
- **Judging tracking quality by tracking error alone**: it ignores sign and concentration; pair with mean/median tracking difference.
- **Using the strict last-trade price to compute premium/discount for thinly traded ETFs**: stale price vs fresh NAV creates false premiums; use closing midpoint.
- **Calling a closing premium/discount "mispricing" for ETFs on foreign or bond holdings**: the NAV is stale/early; the ETF may be the better price.
- **Holding leveraged/inverse ETFs long term**: compounding breaks the multiple.
- **Treating ETNs as funds**: they are unsecured bank debt; no assets back them.
- **Quoted spread = cost for large orders**: quoted spreads are for small sizes; above about 10% of ADV, negotiate with the issuer's capital markets desk or broker ETF desk.
- **Choosing a thin ETF with a low fee for tactical trades**: choose the highest dollar volume (dollar volume / assets is a screen).

## Exam Focus & Traps
- Premium: AP buys basket, creates, sells ETF shares. Discount: AP buys ETF, redeems, sells basket. Retail investors never create/redeem. Direction mix-ups are the classic trap.
- **Who pays creation/redemption costs**: the AP (passed on in the bid-ask spread), not remaining shareholders and not the sponsor.
- Reported tracking error is the **annualized** standard deviation of daily return differences. The tracking difference (rolling return gap) shows the real investor outcome.
- Smallest source of tracking error: index changes (infrequent, can be done market-on-close). Largest: fees and sampling. Lowest-TE profile: full replication + local shares + securities lending.
- Holding cost formula: fee is prorated, commissions/spreads are not. Check "round-trip commission" wording: if the question gives round-trip commission already, do not double it (e.g., 9 months, 0.40% fee, 0.55% round-trip commission, 0.20% spread: 0.30 + 0.55 + 0.20 = 1.05%; fee 0.32%, 0.20%, 0.10%: 0.24 + 0.20 + 0.10 = 0.54%).
- Spread determinants: negative with order flow and with competition, positive with market maker costs/risks. For very liquid ETFs creation/redemption fees matter least.
- ETFs have higher premium/discount risk when low trading frequency + large foreign share.
- Expectation (investor-related) risk = not understanding complex ETFs (leveraged/inverse). Fund-closure risk drivers: regulation, competition, corporate actions.
- Return-of-capital distributions are generally not taxable and reduce basis.
- Tax fairness (no forced selling) is distinct from tax efficiency (basis management) and from tax on sale.

## Key Takeaways
1. All ETF value flows from the in-kind creation/redemption arbitrage: it anchors price, lowers cost and taxes, and moves transaction costs onto the traders who cause them.
2. Compare ETFs on all-in cost for your horizon: tactical = spread, volume and premium/discount; strategic = fee and tracking difference.
3. Measure tracking with both rolling tracking difference (central tendency) and tracking error (dispersion); expect difference ≈ -fee ± securities lending income.
4. Premiums/discounts are largest when the underlying is foreign, illiquid or stale, or the ETF trades infrequently; use iNAV intraday.
5. Fixed-income and international ETFs have wider spreads and wider arbitrage bands; in stress, they may be the true price discovery vehicle.
6. ETNs, swap-based and deposit-based ETFs carry counterparty risk; track issuer CDS; securities lending is over-collateralized (102%/105%).
7. Leveraged/inverse ETFs reset daily and are not buy-and-hold instruments.
8. Use ETFs for cash equitization, rebalancing, completion, transitions, core exposure, tactical tilts and factor tilts; very large asset owners may prefer SMAs (lower fees, customization, disclosure of large holdings).

## Connects To
- **ch12**: multifactor models explain the factor exposures that smart beta/factor ETFs package.
- **ch13**: VaR and risk measurement for ETF positions; leveraged ETF path dependence matters for risk limits.
- **ch15**: active risk, tracking risk and information ratio; tracking error of a replicating fund is the active risk of a passive strategy.
- **ch16**: trading costs, spreads and electronic markets behind ETF liquidity.
- **`cfasi-portfolio-construction`**: ETF and fund selection process and screening criteria.
- **`cfasi-equity-investment-styles`**: factor investing that factor ETFs implement.
- **`cfa-derivatives` ch04**: swap/option structures behind synthetic and leveraged ETFs.
