# Chapter 17: Alternative Investments - Performance, Risk and Transparency
> **Source**: CFA Society Italy × Advisor Private (AP Advisor Private n. 12, Jul-Aug 2018), *Alternative Investments: L'importanza nel Wealth Management*, Chapter 3 "Performance, rischio e trasparenza" + sponsor insert on long/short equity (J. Clunie, Jupiter AM) | Massimiliano Saccone, CFA

## Core Idea
Private-capital funds are **self-liquidating cash-flow assets**: performance is measured **money-weighted** (IRR, multiples) while listed markets are measured **time-weighted**, so the two are not directly comparable. This chapter gives the toolkit to (1) measure performance (IRR, TVPI/DPI/RVPI, quartiles, PME family, Direct Alpha), (2) decompose financial risk into **funding, liquidity, capital and market risk**, (3) model cash flows (Yale model, probabilistic models, VaR), and (4) understand why regulators (BMR, fair-value accounting) are pushing for time-weighted, replicable, self-financing benchmarks. Operational due diligence is flagged as more critical for closed illiquid funds than for hedge funds.

## Frameworks Introduced
- **Two tools linking track record to the future**: (1) **mark-to-market analysis** - how closely the fund NAV co-moves with listed-market valuations (co-movement, not a statistical beta, because data points are too few); the more it co-moves, the easier it is to build scenarios. (2) **Performance persistence** - whether past success carries over to the next fund. Evidence is mixed and depends on statistical method and sample comparability.
  - Failure mode: "top-quartile" recipes. Qualitative team features (structure, size, institutional standing) support sustainability, but investments are stochastic: portfolio companies are not a predefined universe, entry and exit timing, financing structure and buyer type vary, and successive funds do not share a continuous portfolio.
- **IRR + multiples as a pair**: IRR says how fast capital turns over; multiples say how much the investment returned. Always read them together (the basis of GIPS reporting for closed-end funds).
  - IRR is the rate `r` solving `sum_{t=0..n} CF_t / (1+r)^t = 0`, where CF are contributions (negative), distributions (positive) and residual NAV (as a final positive value).
  - Limits: implicit reinvestment at the same rate; a short holding period inflates it (a 1-month 5% gain annualizes to about 80%, yet the investor earned EUR 5 per EUR 100); multiple IRRs with non-conventional flows; **non-additive**, so it cannot be averaged across funds or used in standard statistics.
- **Quartile ranking within a peer group (vintage and strategy)**: rank funds by IRR into quarters. Obsolete as a sole method because IRR is non-additive and not comparable across funds with different durations. A 78% IRR on a 1-month deployment (TVPI 1.05x) is not better than 76% on 3 months (1.15x) or 74% on 8 months (1.45x); rankings by IRR alone invert the economic ranking.
- **Public Market Equivalent (PME) family**: restate the listed-index return in the same money-weighted logic as the fund.
  - **ICM / Long-Nickels PME**: invest the fund's contributions in the index, deduct distributions, form an index-adjusted NAV; compare the index IRR with the fund IRR. Problem: large distributions can push the index NAV negative.
  - Modified versions: **PME+**, **Rouvinez / Modified PME**, **Cambridge Associates mPME** handle that problem.
  - **Kaplan-Schoar PME (KS-PME)**: ratio of future value of all distributions to future value of all contributions, both compounded at the index return. `KS-PME > 1` means outperformance of the index.
  - **Direct Alpha** (Gredil, Griffiths and Stucke): compound all contributions and distributions to the end date using index returns, then take the IRR of the resulting cash flows. Interpreted as annualized excess return over the index, but it inherits IRR limits and embeds the asset-class risk premium without quantifying it.
- **Financial risk map for a private-capital portfolio**: capital risk (final loss), market risk (value volatility), funding risk (inability to meet calls), liquidity risk (cost of selling). Two are specific to private funds: funding and liquidity.
- **Funding-risk ratios (monitor with scenario analysis and stress tests)**: Current Ratio (liquid resources versus short-term obligations including expected calls), Adjusted Current Ratio (adds paid-in and undrawn capital), **Overcommitment Ratio** (undrawn commitments versus available resources; typically 105-115%, higher is riskier), **Outstanding Commitment Level** (undrawn divided by total commitments; indicates portfolio maturity and latent obligation).
  - Causes of funding risk: (1) over-commitment strategies (committing more than allocated cash, counting on distributions to fill the gap and to approach target exposure efficiently); (2) market phases that distort the expected path of contributions and distributions, breaking the habit of financing recent-vintage calls from mature-vintage distributions. Default can mean losing all rights in the fund including capital already paid.
- **Cash-flow modelling choices**: probabilistic (data-driven, need distributions, produce scenarios, assume independence/stationarity) versus non-probabilistic (few parameters, simple, for scarce data).
  - **Yale Model** (non-probabilistic): projects annual contributions, distributions and NAV from a few parameters: NAV growth rate `g`, contribution rate `RC` (share of undrawn commitment called each year) and distribution rate `RD` (increases with fund age). Works best for a large, diversified, stable portfolio; cannot model cash-flow volatility, so it does not manage funding and liquidity risk directly.
- **Private-equity VaR**: the maximum loss at a confidence level over a horizon, adapted without price histories by using the volatility of NAV series or of cash-flow series. Imperfect but puts private capital on the same information footing as other asset classes and links to capital risk.
- **The denominator effect (Harvard / Duke, 2008)**: allocation caps are ratios, so when listed assets fall the portfolio total (the denominator) falls and the private-equity weight breaches its cap. Harvard's cap was 13% and the weight rose to about 15%; the forced sale of USD 1.5bn of private-equity stakes (the "Great Unwinding") locked in losses at steep discounts in a dried-up market, before funds and markets recovered.
  - Use: size private allocations and liquidity buffers against a stressed denominator, not the current one.
- **Valuation lag**: private-fund valuations arrive 1 to 6 months late (about 4 on average) because portfolios are valued bottom-up. Tools now give near-real-time statistical indications; the BMR push is for indices that are representative of the underlying and allow relative valuation using listed-market information.
- **Benchmark Regulation (EU 2016/1011, BMR, in force 3 January 2018)**: benchmark administrators must be authorized; conflicts of interest and discretion controlled; methodologies robust and based on actual transaction data where possible. Supervised entities (banks, investment firms, UCITS, AIFMs) may use only benchmarks from authorized administrators. Industry data providers say a suitable private-capital index must be (1) **time-weighted**, (2) **replicable** (an investable portfolio exists that earns exactly the index return), (3) **self-financing** (no extra capital flows). Money-weighted measures fail all three by construction. The guide mentions the author's DaRC (Duration adjusted Return on Capital), a bond-style index under development.
- **Operational risk in due diligence**: governance and process safeguards matter most where the investor cannot exit; AIFMD provides a minimum common protection (except for funds below the thresholds, see ch16).

## Key Concepts
- **Track record**: past performance of a manager, used with team quality in due diligence; a backward-looking input for a forward-looking decision.
- **Blind pool**: a new fund with no portfolio yet; analysis rests on strategy documents and the manager.
- **Money-weighted return**: return that depends on the size and timing of the investor's cash flows (IRR).
- **Time-weighted return**: compound growth rate independent of cash-flow timing, used for listed funds.
- **TVPI** (Total Value to Paid-In): `(NAV + cumulative distributions) / cumulative contributions`.
- **DPI** (Distributions to Paid-In): `cumulative distributions / cumulative contributions`; realized return.
- **RVPI** (Residual Value to Paid-In): `NAV / cumulative contributions`; unrealized return. `TVPI = DPI + RVPI`.
- **Vintage**: the year a fund starts investing; peers must be compared within vintage.
- **FAS 157 / ASC Topic 820**: US fair-value framework (exit price) since 2006; **IPEV** guidelines allow comparable transactions, multiples, listed references, DCF, NAV.
- **Undrawn / unfunded commitment**: capital promised but not yet called.
- **Funding risk**: risk of being unable to honour capital calls; the "default risk" of private capital.
- **Capital risk**: probability and size of ending below the capital invested, i.e. `DPI = TVPI < 1` (the source writes this as `< 0`, meaning a negative return); rarer than assumed because of internal diversification.
- **Smoothing**: pre-crisis non-fair-value accounting gave artificially smooth returns and hid exposure to secondary-market shocks.
- **Self-liquidating fund**: closed-end fund that returns capital through exits and winds down.

## Formulas & Reference Tables
- `TVPI = (NAV + Distr) / Contr`; `DPI = Distr / Contr`; `RVPI = NAV / Contr`; `TVPI = DPI + RVPI`, where Contr = cumulative paid-in capital, Distr = cumulative distributions.
- IRR: solve `0 = sum CF_t / (1+IRR)^t`.
- `KS-PME = [sum D_t * (I_T / I_t)] / [sum C_t * (I_T / I_t)]`, where `D_t`, `C_t` are distributions and contributions at time t and `I` is the index level; `T` is the final date (equivalently future values at index returns).
- Direct Alpha: IRR of cash flows `CF_t * (I_T / I_t)` (including terminal NAV), after annualizing.
- Yale model (standard formulation, reconstructed because the source formulas were graphical): `Contribution_t = RC_t * (Commitment - PaidIn_{t-1})`; `Distribution_t = RD_t * NAV_{t-1} * (1+g)`; `NAV_t = NAV_{t-1}*(1+g) + Contribution_t - Distribution_t`; `RD_t = max(yield, (t/L)^B)` with `L` fund life and `B` a bow factor. **Note**: the guide describes the parameters but not the exact equations; this is the Takahashi-Alexander form.
- Overcommitment ratio (reconstructed, definitions vary): `(NAV + Undrawn) / Total capital allocated to the program`; outstanding commitment level = `Undrawn / Total commitments`. **Flag**: source formulas were images; use the plan's own definitions consistently.

Typical level: overcommitment 105-115%; valuation lag 1-6 months (avg ~4).

## Mental Models
- Use IRR for speed of capital turnover and multiples for size of gain, never IRR alone.
- Use PME/KS-PME when asked "did private equity beat the index?"; use a plain IRR comparison only as a rough check.
- Use stress scenarios on the **denominator** (public-asset drawdown) before setting a private-equity limit.
- Use over-commitment only if you hold a liquidity plan for late or delayed distributions.
- Use time-weighted, replicable, self-financing indices when a benchmark must satisfy BMR.

## Worked Example
**1. Why IRR rankings mislead (recomputed).** Three one-year-window deals on EUR 100 invested: 1 month earning EUR 5; 3 months earning EUR 15; 8 months earning EUR 45.
- Annualized compounded IRR: `1.05^12 - 1 = 79.6%`; `1.15^4 - 1 = 74.9%`; `1.45^1.5 - 1 = 74.6%`. (The source quotes 78%, 76%, 74%; its exact figures depend on its compounding convention, but the ranking and message are the same.)
- TVPI: 1.05x, 1.15x, 1.45x.
- Interpretation: the 1-month deal tops the IRR table yet creates the least value. The three IRRs cannot be averaged.

**2. Yale model sketch (recomputed).** Commitment 100, `g = 10%`, `RC = 25%` of the undrawn amount, years 1-4 only, `L = 12`, `B = 3`, yield 0.
- Contributions: 25.0, 18.8, 14.1, 10.5.
- NAV end of year: 25.0, 46.1, 64.0, 78.3.
- Distributions begin small (0.1 in year 2, 0.8, 2.6, then 6.2, 11.0, 16.8 in years 5-7 with no further calls); NAV peaks at about 79.9 in year 5 and then declines.
- Interpretation: the J-curve - negative net cash flow early, positive only after year ~5; commitments must be funded from other assets until then.

**3. Denominator effect.** Total portfolio 100, private equity 13 (13%); public assets 87, of which equities 50. Equities fall 40% (-20). Portfolio 80; private equity unchanged (lagged valuation) 13/80 = **16.25%**, above a 13% cap, forcing sales or a cap breach.

## Anti-patterns
- Averaging IRRs across funds or using quartile rank as the only filter.
- Comparing a private-fund IRR directly with an index's annual return.
- Treating a lagged, smoothed NAV as proof of low volatility.
- Over-committing without stress-testing distribution delays.
- Assuming past top-quartile status carries to the next fund.
- Ignoring operational due diligence because performance is strong.

## Practitioner Notes
- Ask a manager for contributions and distributions by date, not just the headline IRR: you need them for DPI/RVPI, PME and the Yale-style projection.
- Evidence of NAV quality: check the ratio of exit prices to carried values over several vintages (secondary-market prices in 2017 were consistent with improved NAV quality absent shocks, see ch18).
- Insert (Jupiter AM, long/short equity): rising volatility can help market-neutral long/short managers, since short books concentrate in highly market-sensitive stocks and bought options gain value; the manager builds short exposure gradually, couples bottom-up pair ideas with top-down sector and country risk control, and aims to profit from dispersion rather than market direction. A long/short UCITS fund can replace part of the equity sleeve with a better risk-return, letting the equity target be raised if volatility falls. Sponsor opinion; treat as illustration, not evidence.
- Alternatives help when both equity (end-cycle valuations) and bonds (rising-rate risk) are exposed; the 2018 Mercer survey footnote is the cited source for allocation trends.

## Key Takeaways
1. Private-fund returns are money-weighted; do not mix them with time-weighted listed returns without a PME-type bridge.
2. Read IRR together with TVPI, DPI and RVPI; IRR is non-additive and favors short, quick deals.
3. KS-PME above 1 and positive Direct Alpha signal outperformance versus the chosen index.
4. Four risks matter: capital, market, funding and liquidity; funding and liquidity are specific to commitment-based funds.
5. Monitor overcommitment (typically 105-115%) and outstanding commitment level with stress tests.
6. The denominator effect can force sales of illiquid assets at the worst moment (Harvard 2008).
7. BMR pushes private-market benchmarks toward time-weighted, replicable, self-financing indices.
8. Operational due diligence is more critical for closed funds because the investor cannot exit.

## Connects To
- **ch15**: why investors allocate to alternatives and why transparency limits adoption.
- **ch16**: AIFMD, MiFID II and the regulatory frame behind BMR and operational safeguards.
- **ch18**: liquidity risk resolved through the secondary market and its pricing as a percentage of NAV.
- **ch19**: structures (evergreen, listed vehicles, platforms) that change the cash-flow and benchmark problem.
- **`cfa-alternative-investments`**: CFA treatment of private equity performance and J-curve.
- **`cfa-ethics-gips`**: GIPS rules for closed-end funds (IRR and multiples).
