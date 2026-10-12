# Chapter 2: Passive Equity Investing
> **Source**: CFA Program Curriculum 2023, Level III, Reading 16 · Portfolio Management | David M. Smith, PhD, CFA, and Kevin K. Yousif, CFA

## Core Idea
Passive investing is any rules-based, transparent, investable strategy that does not try to identify mispriced stocks; indexing is its purest form. The passive manager's skill is not picking stocks but choosing the right benchmark, building the portfolio at the lowest cost for a given tracking error (replication vs sampling vs optimization vs derivatives), and explaining every basis point of deviation. Fees, trading costs and cash drag are the main sources of tracking error, and securities-lending income is the main offset.

## Learning Outcomes Covered
- discuss considerations in choosing a benchmark for a passively managed equity portfolio
- compare passive factor-based strategies to market-cap-weighted indexing
- compare approaches to passive investing (pooled funds, derivatives, direct/separate account)
- compare full replication, stratified sampling and optimization
- discuss causes of tracking error and ways to control it
- explain sources of return and risk of a passive equity portfolio (attribution, securities lending, engagement)

## Frameworks Introduced
- **Three requirements for an index to be a basis for investment**: rules-based, transparent, investable.
  - When to use: screening any benchmark (or index-linked product) before adopting it.
  - How: (1) rules objective, consistent, predictable (inclusion criteria, rebalance frequency); (2) methodology and constituents fully disclosed, no black box; (3) performance replicable in the market (adequate float, liquidity, tradable constituents).
  - Failure mode: non-investable indexes (hedge-fund-of-funds indexes such as HFRI; Value Line Geometric, a multiplicative index that cannot be replicated) look fine as yardsticks but cannot be held.
- **Benchmark selection checklist (derived from the IPS)**: market segment (broad vs sector; domestic vs international; developed/emerging/frontier), capitalization (mega to micro, smid, all-cap), style (value/growth/blend), other factor exposures (momentum, low vol, quality), then construction method (inclusion, weighting, rebalance/reconstitution, concentration).
- **Index weighting schemes**: market-cap (free-float adjusted is the standard), price, equal, fundamental, dividend, volatility (inverse vol), minimum variance, maximum diversification, multi-factor. See table below.
- **Passive factor-based strategy taxonomy** (return-oriented, risk-oriented, diversification-oriented): active decisions are made up front (choice of factor, rules), then executed passively.
- **Three construction approaches**: full replication, stratified sampling, optimization; plus the **blended approach** (replicate the liquid core, sample/optimize the illiquid tail).
- **Three access routes**: pooled investments (mutual funds, ETFs), derivatives (futures, swaps, options; usually as an overlay), separately managed account built stock by stock.
- **Tracking-error control triad**: minimise trading costs, net investor flows against redemptions, equitize cash with derivatives/ETFs; keep beta at 1.0 and other factor exposures like the index.
- **Return attribution (ex post)**: contribution = weight × sector return; difference portfolio minus benchmark by sector pinpoints the tracking-error source.

## Key Concepts
- **Indexing vs passive investing**: indexing replicates a named index; passive investing is the broader family (including factor strategies chosen by the manager).
- **Free-float adjustment**: counting only shares available to the public (excluding founders, governments, affiliated companies, foreign-ownership caps) to compute weights; improves investability.
- **Buffering**: a band around the size breakpoint between two indexes; a stock migrates only after crossing the outer edge. Example: MSCI USA Large Cap, buffer set at 67% of the cutoff market cap.
- **Packeting**: moving a migrating stock between indexes in several tranches over successive reconstitutions (CRSP), reducing turnover and cost.
- **Reconstitution vs rebalancing**: reconstitution adds/deletes constituents; rebalancing reweights existing ones. Both create turnover and front-running opportunities.
- **Herfindahl-Hirschman Index (HHI)**: sum of squared weights; ranges from 1/n (equal weight) to 1 (single stock).
- **Effective number of stocks**: 1/HHI; the number of equal-weighted stocks with the same concentration.
- **Tracking error (TE)**: standard deviation of (Rp − Rb); always non-negative; a measure of how closely the portfolio behaves like its benchmark.
- **Excess return**: Rp − Rb; signed; distinct from TE.
- **Cash drag**: tracking error from uninvested cash (dividends received, inflows, sale proceeds); hurts in rising markets, helps in falling ones.
- **Equitizing**: using futures, ETFs or swaps to give cash an equity exposure and restore beta.
- **Overlay**: derivatives layer on an existing portfolio: completion (fix beta/exposure gaps), rebalancing (move to policy weights), currency (hedge FX).
- **Authorized participant (AP)**: ETF market maker that creates/redeems shares in kind against baskets of stocks; the reason ETFs are tax efficient.
- **Basis risk**: futures price not moving one-for-one with the index (e.g., futures track price, not dividends).
- **Market-on-close (MOC) order**: executes at the closing price used by the index provider, minimising intraday trading tracking error.
- **Factor tilt / factor rotation**: intentional over/underweighting of risk factors; rotation changes the tilts as conditions change (an active bet via passive vehicles).
- **Fundamental indexation (Arnott, Hsu, Moore)**: weights by sales, cash flow, book value, dividends, employee count instead of price.

## Formulas & Reference Tables
`Market-cap weight_i = (Price_i × free-float shares_i) / Σ(Price_j × free-float shares_j)`
`Price-weighted weight_i = Price_i / Σ Price_j` (equals holding one share of each)
`Equal weight_i = 1/n`
`HHI = Σ wᵢ²`  (range 1/n to 1)
`Effective number of stocks = 1/HHI = 1 / Σ wᵢ²`
`Tracking error = σ(Rp − Rb) = √Variance(Rp − Rb)`
`Excess return = Rp − Rb`
`Futures contract unit value = multiplier × futures price`; `P&L = multiplier × Δ futures price`
`Equity swap net settlement (receiver of index) = N × index return − N × (Libor + spread) × days/360`
`Diversification ratio (Choueifaty-Coignard) = Σ wᵢσᵢ / σp`
`Sector contribution = wᵢ × rᵢ`; `Difference = Σ (wᵢ,p − wᵢ,b) × rᵢ` when sector returns are common

| Weighting | Philosophy | Strengths | Weaknesses |
|---|---|---|---|
| Market-cap (float-adj.) | Market portfolio is mean-variance efficient (CAPM); weights self-adjust | Low turnover and cost, capacity (liquidity-weighted), transparent | Concentrated (NASDAQ 100: 100 stocks, ~25 effective), overweights overpriced stocks per fundamental advocates |
| Price | One share of each | Simple; visible (DJIA, Nikkei 225) | Splits distort weights, arbitrary, rarely used for investing |
| Equal | Naive diversification, no preference | Lowest concentration, slow-changing sector exposure | Small-cap bias, higher vol, needs rebalancing (index is equal-weighted only ~1 day per quarter), limited capacity (S&P 100 EW ~USD 176bn; S&P 600 EW ~USD 2bn) |
| Fundamental | Prices drift from value; fundamentals do not | Cheap, rules-based, value/size tilt (~200 bp/yr over 43 yrs, but not pure alpha) | Embedded value and size tilts; crowding |
| Inverse-vol / min-variance | Lower risk | Lower absolute vol and drawdowns | Backward-looking inputs; sector/country constraints needed |
| Dividend / yield | Income | Income stream; defensive | Sector bias (utilities, telecom), rate-sensitive |
| Max diversification | Maximise diversification ratio | Diversification-oriented | Depends on historical vol/correlation |

| Construction method | Best when | Tracking error | Cost / complexity | Main weakness |
|---|---|---|---|---|
| Full replication | Liquid index, few/homogeneous names (S&P 500 workable from ~USD 10m), large mandate | Lowest (before costs) | High trading costs if tail names are illiquid | Costs rise at the illiquid end |
| Stratified sampling | Many constituents (global, multi-cap), small mandate | Higher than replication | Low trading cost, simple | Stratum choice; ignores covariances inside strata |
| Optimization | Need min TE with N-stock cap, technical team | Lower than sampling | Needs software and expertise; frequent re-runs | Uses past data; may be mean-variance inefficient versus benchmark (Roll, Jorion), fix by constraining total volatility to match the index |
| Blended | Cap-spanning indexes (Russell 3000, S&P 1500, Wilshire 5000) | Balanced | Moderate | Judgment on the cutoff |
| Synthetic (swaps/OTC derivatives) | Few liquid exchange futures; customised | Low | Counterparty and tax risks | Counterparty, liquidity, rate, tax-policy risk |

| Access route | Pros | Cons |
|---|---|---|
| Open-end index mutual fund | Convenience, record keeping, low fee | Slightly higher expense ratio than ETFs; taxable events on redemptions; trades at NAV |
| ETF | Intraday trading, margin/short possible, in-kind redemption (tax efficient), 1,354 US-tracked indexes vs 184 for funds | Bid-ask spread, commissions (can offset fee edge for frequent traders), fewer ETFs than indexes |
| Futures | Cheap, liquid, leverage, short easily, one trade changes whole exposure | Roll cost, margin/daily cash flows, basis risk, position limits, expiry |
| Swaps | Any index, customised, no stock trading costs, tax deferral | Counterparty, non-marketable, interest-rate (Libor leg) and tax-policy risk |
| Separate account (DIY) | Customisation, tax-lot control, no pooled fees | Needs index data licence, OMS/accounting, broker relationships, compliance |

Typical tracking-error drivers (ranked in the source): fees, number of securities held (sampling), intraday execution vs closing price, commissions and market impact, cash drag, dividend drag, index changes.

## Mental Models
- **TE is a U-shape in holdings**: adding more index names cuts TE until the illiquid tail's trading costs outweigh the benefit; the optimal sample stops before the least liquid names.
- **Passive is "active up front"**: smart beta, factor and fundamental indexes embed active choices (which factor, when) in the rules; judge them like active strategies for factor crowding and cyclicality, but they keep the fee advantage.
- **Futures for tactics, cash for strategy**: use derivatives to move exposure fast and cheaply (overlays, equitizing); use physical holdings for permanent exposure because derivatives expire, roll and face position limits.
- **Lend freely if you hold the index anyway**: lending income can make an index fund's net expense negative, but collateral reinvestment and borrower credit are the real risks.
- **Concentration check before you buy a cap-weighted index**: compute 1/HHI; a 100-stock index with 25 effective names is not 100 stocks of diversification.

## Worked Example
**1. Effective number of stocks (verified).** 50-stock index: top five weights 0.089, 0.080, 0.065, 0.059, 0.053 (sum 0.346); remaining 45 stocks hold 0.654 with Σw² = 0.01405.
Σw² of top five = 0.00792 + 0.00640 + 0.00423 + 0.00348 + 0.00281 = 0.02484. HHI = 0.02484 + 0.01405 = 0.03889. Effective N = 1/0.03889 = 25.7 (about 26), versus 50 for equal weight, so concentration is about half what the name count suggests.

**2. Futures margin call (verified).** ASX 200 futures at AUD 5,700, multiplier 25: unit value AUD 142,500. Initial margin 6,700, maintenance 5,300: a margin call comes after a AUD 1,400 loss, i.e. unit value 141,100, futures price 5,644, a 0.98% fall in the index. The margin account falls 1,400/6,700 = 20.9% (source rounds to 20%). Leverage works both ways.
S&P 500 futures: settlement 2,159.30 vs 2,157 = +2.30 × USD 250 = USD 575 per contract.

**3. Equity swap settlement (verified).** EUR 20m notional receives Euro STOXX 50 return (6-month +2.3%) and pays Libor 0.18% + 0.20% = 0.38% annualised for 180/360. Receive 460,000, pay 20m × 0.0038 × 0.5 = 38,000, net receipt EUR 422,000.

**4. Tracking error reading.** Australian funds (293-296 stocks held of 300, 0-20 bp fee): TE 0.02-0.11%. Korean funds (178-204 of 200): TE 1.3-1.5%. Negative excess returns of -0.17% and -0.18% roughly match the 18-20 bp fees, so fees explain excess return while sampling and index-change timing explain TE.

## Anti-patterns
- **Treating tracking error and excess return as interchangeable**: a fund can lag then lead and net to zero excess return while TE is large.
- **Optimising TE alone**: the optimised portfolio can be riskier than the index; add a total-volatility constraint.
- **Using equal weight or fundamental weight as "free alpha"**: much of the premium is size and value factor exposure, and it shrinks after rebalancing costs and taxes (Qin-Singal) for taxable investors.
- **Leaving cash idle**: any uninvested balance is a beta below 1; equitize with futures or ETFs.
- **Trading at random times in the day**: the index prices at the close; use market-on-close orders to avoid intraday tracking error.
- **Pre-announced reconstitution trades**: predictable index changes let arbitrageurs front-run passive funds (price effects at breakpoints per Petajisto); objective, announced rules make this worse, committee-based methods are harder to predict.
- **Ignoring collateral quality in securities lending**: reinvesting cash collateral in long or risky paper (Sigma Finance in 2008) turns fee income into losses.
- **Assuming a passive investor cannot or need not engage**: passive holders are permanent shareholders with fiduciary voting duties, though management may take them less seriously because they cannot sell.

## Exam Focus & Traps
- Free-float adjustment **improves** investability (it excludes untradable shares); it does not lower liquidity. Buffering also improves investability (less turnover).
- Price-weighted = one share of each (stock splits distort); equal-weighted = 1/n, small-cap bias, higher volatility, rebalancing needed; cap-weighted rests on efficient markets, fundamental weighting on market inefficiency.
- HHI ranges from 1/n to 1; effective N = 1/HHI; HHI 0.0286 means about 35 effective stocks. If the stated index is price-weighted the HHI still applies to its weights.
- Tracking error is a standard deviation (>= 0); excess return is signed. Higher fees lower excess return; sampling raises TE.
- Full replication: needs liquid, available constituents and large enough assets; stratified sampling: many constituents or small AUM, simple and technically unsophisticated; optimization: needs sophistication, covariances, past data, frequent reruns.
- Cash drag: negative in rising markets, positive in falling. Futures equitize cash; to hedge anticipated inflow (e.g. a USD bonus), buy futures sized to the exposure: contracts = (cash × policy weight of that market) / (multiplier × futures price), rounded to whole contracts. Example: USD 5.75m bonus × 15% US policy weight = USD 862,500; E-mini (50 × 2,464.29 = USD 123,214) gives 7.0, so buy 7 E-minis (a full-size contract, multiplier 250, would be 1.4).
- Futures basis risk arises because the contract tracks index price, not dividends; futures are cash-settled; swaps carry counterparty risk, exchange futures effectively do not.
- Securities lending: borrower gets voting rights and manufactured dividends go to the lender; cash collateral (typically 102-105%) reinvestment is the biggest risk; index funds and pension funds are preferred lenders.
- Factor-based passive strategies concentrate risk and cost more than broad indexing; multi-factor approaches mitigate factor cycles.
- ETF vs mutual fund: ETF lower expense and tax-efficient (in-kind) but bid-ask and brokerage; mutual funds have more passive-fund conveniences for small recurring contributions.
- Source clarifications: the margin example's "20%" is really 20.9% (1,400 of 6,700); treat as rounding.

## Key Takeaways
1. A usable benchmark is rules-based, transparent and investable; derive market, size, style and factor exposure from the IPS.
2. Float-adjusted cap weighting is the default because it self-rebalances, is cheap and has capacity; check concentration with 1/HHI.
3. Non-cap weights (equal, fundamental, min-variance, multi-factor) are factor bets with their own costs and crowding, not free lunches.
4. Choose construction by index size, liquidity and mandate size: replicate liquid cores, sample or optimise the tail, use futures/ETFs for cash and tactical moves.
5. Tracking error comes from fees, trading costs (use MOC), cash/dividend drag and sampling; control with netting of flows, equitization and beta near 1.0.
6. Securities-lending income can fund the whole fee; manage collateral and borrower risk, and recall shares only when votes matter.
7. Attribute returns by sector/country/currency/security to explain TE and the sources of return.
8. Passive does not mean passive owners: vote, engage and watch for conflicts of interest.

## Connects To
- **ch 01**: roles, segmentation, costs and securities-lending economics that this chapter operationalises.
- **ch 03**: active strategies as the alternative to passive and factor tilts.
- **ch 04**: tracking error, active share and the risk budget of an active portfolio built around a passive core.
- **`cfa-portfolio-management` ch 02**: index construction basics; **ch 11**: ETF creation/redemption detail; **ch 12**: multifactor models behind smart beta.
- **`cfa-derivatives` ch 06**: equity swaps and futures strategies.
- **`cfasi-equity-investment-styles` ch 06-08**: factor investing guides.
