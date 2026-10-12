# Chapter 7: Passive Funds Are More Active Than You Think: Replication, Securities Lending, Tax Efficiency, Voting (Una gestione piu attiva di quanto si pensi)
> **Source**: CFA Society Italy x Advisor Private, "Passive Investments" guide (Advisor Private no. 26, 2020), Chapter 3 | Giovanni Semprini, CFA; the closing insert on ESG myths in index investing is sponsored by Amundi (Laurent Trottier) and is attributed below

## Core Idea
"Passive" describes the objective (follow a benchmark), not the management: every day the ETF manager makes active choices that drive return and tracking error: how to replicate (five methods), whether and how to lend securities, how to handle creation/redemption and taxes, and how to vote and engage. Understanding these choices is the key to selecting between products and to judging ESG claims of index funds.

## Frameworks Introduced
- **Five replication methods and when to use each**:
  1. **Full physical replication**: hold every index constituent in index weights. Pros: simple, return and volatility nearly identical to the index. Cons: loses efficiency as the index gets bigger, with more small caps, or with wide-bid-ask bonds (higher trading fees mean higher tracking error, since the index ignores costs). Best for small-number, liquid indices.
  2. **Physical, stratified sampling**: group constituents into mutually exclusive and exhaustive strata (sector via GICS, style, region, multi-dimensional) and hold the same proportions in each stratum by picking representative (e.g. largest) names. Pros: no statistical inputs, cheap, practical for large illiquid indices. Cons: ignores covariance between the picks, so bigger deviation from the index.
  3. **Physical, optimized sampling**: minimize expected tracking error subject to constraints (max number of names, minimum market cap, style/characteristic matching) using historical returns, volatilities and covariances. Pros: lowest tracking error among sampling methods (correlated names across sectors can be replaced by one). Cons: inputs may not be stationary; sensitive to small input changes, which causes unstable results and trading costs; more expensive to run. Rule: minimize tracking error then choose optimized; minimize TCO (fees plus trading), choose stratified; concentrated liquid index, choose full replication.
  4. **Synthetic unfunded**: the manager holds a substitute (reference) basket that meets UCITS liquidity and diversification rules, and a swap hands the basket's return (plus a fee) to the counterparty in exchange for the index return. Portfolio = securities + derivatives. The basket can be lent out like a physical ETF's holdings (rare in practice, since baskets are often low-demand securities). Considered less risky than funded: on counterparty default the manager already holds the collateral basket.
  5. **Synthetic funded**: subscription cash goes entirely into swaps with one or more counterparties; the fund is fully invested in derivatives; the counterparty posts UCITS-compliant collateral at a custodian bank (higher collateral and haircut than unfunded, because counterparty exposure is larger). Default: seize the collateral, which may take days.
  - **Synthetic ETFs suit** indices with many securities, illiquid names or high turnover, because the swap removes the rebalancing activity and its trading cost. **Counterparty risk** (unrealized mark-to-market gain lost on swap issuer failure) is limited by: UCITS cap of 10% of assets in derivatives of one issuer (hence several counterparties), more frequent swap settlement (daily settlement cuts exposure to one day's index return for funded, or to the index-basket return difference for unfunded), collateral above 100% of NAV with haircuts for volatile collateral, and EMIR margin rules for uncleared OTC derivatives above a 500k mark-to-market. ETFs also publish holdings daily, a transparency advantage.
- **Securities lending (mechanics)**: three phases. (1) Through a lending agent, the fund lends shares or bonds to a borrower for a fee and receives collateral (high-credit financial instruments or cash) worth at least the loan, usually 102-105%. (2) During the loan, cash collateral is reinvested in very short, high-quality instruments; dividends or coupons on the lent security are passed on to the owner. (3) At the end the security returns and collateral is released. Lending income can offset or even exceed the management fee.
  - **Evidence (provider data, fiscal year to 31 Mar 2019)**: lending return vs management fee (bp): Russell 2000 growth ETF 22 vs 24 (92% offset); Russell 2000 ETF 15 vs 19 (about 79%; table shows 77%); Russell 2000 Value 8 vs 24 (34%); S&P SmallCap 600 growth 7 vs 25 (28%); S&P 600 ETF 6 vs 7 (85%); S&P 600 Value 6 vs 25 (23%); Nasdaq Biotech 11 vs 47 (24%). Equity index funds sample: utilization of NAV typically 1-7%, net lending income from about 0.1 to 16 bp (Canada 16.3 bp in 2017 with 5.0% utilization; EMU about 4.6 bp; World funds about 1 bp).
  - **Fee drivers**: scarcity (small caps and corporate bonds earn more than large caps and government bonds), borrower credit quality, collateral flexibility, early-recall rights (lower fee). Fee vs volume chart: US small caps and Far East high margin/low volume; government bonds low margin/high volume.
  - **Risks**: borrower default (mitigated by credit analysis, collateral above loan value, indemnities from some managers); collateral reinvestment risk (market, liquidity, credit; mitigated by diversified, short, high-credit reinvestment). Voting rights follow the share, so lent shares carry no vote. Selection checklist for an ETF: average and maximum percentage lent, borrower credit quality, eligible collateral and reinvestment, indemnities, average lending return, default history, historical sufficiency of collateral. Regulation: EU Securities Financing Transactions Regulation; SEC in the US.
- **Tax efficiency of the ETF structure**: In a mutual fund, redemptions force the manager to sell holdings, realizing gains that burden remaining holders (unfair cross-subsidy). An ETF investor sells on the secondary market, with no portfolio trade; creation/redemption is in kind (units for securities), so no gain is realized. Low turnover in index funds/ETFs also defers capital gains, letting more capital compound. Italian rules: distributions and gains are capital income, losses are "other income" computed on ETF price (before 2014 NAV), so ETF losses cannot offset ETF gains, only "other income" gains (shares, bonds).
- **Voting and engagement**: asset managers vote on behalf of fund holders under a proxy voting policy, via an in-house team or proxy advisers, and may skip a vote if cost exceeds benefit. Typical guideline principles: majority independent non-executive board elected annually; CEO and chair separated; independent audit, remuneration and nomination committees; board diversity; pay linked to medium-long-term results; minimum shareholding for top managers; share bonuses accepted unless excessively dilutive; independent auditor; no dual-class shares; minority rights; few takeover defences; share issuance and buybacks only for stated goals; clear rationale for M&A; support useful shareholder proposals. Case examples of votes shown (Carrefour pay, Vinci related-party agreement, RWE capital authorization, Bayer discharge, EDP Renovaveis board seat, Credit Suisse remuneration) illustrate vote logic and a vote moved from Against to Abstain after dialogue. Amundi's 2018 figures: 2,960 shareholder meetings, 35,285 resolutions, 15% votes against (board structure 39.5%, pay 25.7%, capital transactions 22.3%), 186 companies engaged. Passive-specific limits: synthetic ETFs hold no shares so no votes; sampling ETFs hold not all names so less voting power; lent shares lose the vote. Shareholder Rights Directive (2009), SRD II in force September 2020, raises disclosure of engagement and voting.
- **Amundi insert: myths about ESG indexing (sponsored)**: (1) "an index cannot reflect values": over 1,000 ESG indices exist, from light exclusion to climate-aligned, and data providers and active managers use the same data; Amundi structures a range of "shades of green". (2) "Index investors have no voice": managers vote and engage across active and passive; Amundi voted against at least one resolution at over 55% of 2019 meetings. (3) "Index funds have little impact": best-in-class indices reward leaders; dynamic indices systematically divest laggards under transparent rules. Context: European ESG-considering funds up 56% in 2019 to 668 bn EUR (Morningstar); about 20 bn EUR into European ESG ETFs in the first nine months of 2020, triple the 2019 period; index funds globally about 10 trn. Promotional; treat claims as a vendor's.

## Key Concepts
- **Full replication / stratified sampling / optimized sampling**: three physical methods.
- **Substitute (reference) basket**: collateral securities held by an unfunded synthetic ETF.
- **Swap / total return swap**: contract exchanging basket return for index return.
- **Counterparty risk**: loss of unrealized swap gain if the issuer defaults.
- **Haircut**: discount applied to collateral value.
- **EMIR**: EU rule requiring margin on uncleared OTC derivatives.
- **Lending agent / utilization rate**: intermediary / share of NAV on loan.
- **In-kind creation/redemption**: exchange of units for baskets of securities, avoiding realized gains.
- **Proxy voting guidelines / proxy adviser**: policy and outsourced recommendation.
- **Engagement**: dialogue with management on risk topics.
- **Shareholder Rights Directive (I and II)**: EU voting and disclosure rules.
- **UCITS 10% rule**: cap on exposure to one derivative issuer.

## Formulas & Reference Tables
- `Lending offset = Lending return / Management fee` (e.g. 22 bp / 24 bp = 92%).
- `Collateral ratio = Collateral value / Loaned value` (typically 102-105%).
- `Net lending income = gross lending fees - agent fee - collateral reinvestment loss`; shown as bp of NAV.
- Method choice table:

| Index situation | Best method | Why |
|---|---|---|
| Few liquid names | Full replication | lowest tracking error at low cost |
| Many names, minimize TE | Optimized sampling | uses covariances |
| Many names, minimize TCO | Stratified sampling | cheap, stable |
| Illiquid or high-turnover index | Synthetic (swap) | no rebalancing trades; counterparty risk |
| Counterparty-averse | Unfunded swap over funded | collateral already held |

## Mental Models
- Use "passive" to describe the goal, never the work: ask who decides sampling, lending and collateral.
- Use full replication for small liquid indices; sampling when trading cost beats tracking error.
- Use synthetic only with diversified counterparties and daily swap reset; prefer unfunded.
- Use the lending fee as a partial rebate, but always check the collateral policy; low utilization is conservative.
- Use ETF structure to defer tax; use the Italian rule that ETF losses do not offset ETF gains.
- Use voting records as part of ESG due diligence; a green label without voting is thin.

## Worked Example
Compare lending offset for two ETFs. Inputs: ETF A lending 22 bp, fee 24 bp; ETF B lending 6 bp, fee 25 bp. Steps: offset A = 22/24 = 91.7%, B = 6/25 = 24%. Net cost A = 24 - 22 = 2 bp, B = 25 - 6 = 19 bp. Interpretation: lending income is highest where the underlying is scarce (small-cap growth); but A's income depends on borrower demand and carries borrower and collateral-reinvestment risk, so a 22 bp rebate is not free money. Also note rounding: the source's 77% for the 15/19 case is really 78.9%.

## Anti-patterns
- Judging an ETF only by its stated index.
- Choosing an optimized-sampling ETF without checking turnover caused by changing inputs.
- Accepting funded swaps with one counterparty and weak collateral.
- Counting lending income as certain in the TCO.
- Assuming a synthetic ETF votes like a physical one.
- Treating an ESG index tracker as engaged without checking the manager's voting policy.

## Practitioner Notes
- Ask for: replication method, number of holdings vs index, swap counterparties and collateral level, share of NAV on loan, lending split with the agent, voting policy and record.
- The most useful questions to a provider: what happens on a counterparty default, and how long does collateral seizure take?
- ETF structure tax-efficiency applies at fund level; the Italian investor-level rules still dominate (26% flat; see ch06).
- Voting rights are reduced in sampling and lending; for ESG-labelled products these are relevant.

## Key Takeaways
- Passive means following an index; the manager still actively chooses replication, lending, collateral and voting.
- Full replication for small liquid indices; stratified for low cost; optimized for lowest tracking error; synthetic for illiquid or high-turnover indices.
- Funded swaps carry more counterparty exposure than unfunded; UCITS limits derivatives per issuer to 10%.
- Securities lending can offset up to about 90% of a fee in small-cap ETFs but is small for large-cap funds; risk comes from borrower and collateral reinvestment.
- In-kind creation/redemption and low turnover make ETFs tax efficient at fund level.
- Voting rights are lost on synthetic holdings, partly lost in sampling, and temporarily on lent shares.
- ESG claims in index funds depend on the index design and the manager's engagement record.

## Connects To
- **ch05**: passive vs active overview and ETF liquidity.
- **ch06**: TCO, tracking difference, synthetic vs physical costs and tax.
- **ch08**: smart beta, thematic and ESG alternative indices.
- **ch09-ch14**: ETF selection and due diligence checklists.
- **`cfa-equity-portfolio-management` ch02 and `cfa-portfolio-management` ch11**: passive equity replication and ETF mechanics.
