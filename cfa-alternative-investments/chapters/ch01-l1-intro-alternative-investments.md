# Chapter 1: Introduction to Alternative Investments
> **Source**: CFA Program Curriculum 2020, Level I, Reading 50 · Alternative Investments | Terri Duhon, George Spentzos, CFA, FSIP, Scott D. Stewart, PhD, CFA

## Core Idea
Alternatives are a heterogeneous set (hedge funds, private equity, real estate, commodities, infrastructure, collectibles) defined by what they are not: long-only, liquid, public stocks, bonds and cash. They are sold on diversification and higher risk-adjusted return, but reported data are smoothed, biased and self-reported, so index statistics flatter them. Fees, leverage, illiquidity and due diligence decide what the investor actually keeps.

## Learning Outcomes Covered
- compare alternatives with traditional investments
- describe hedge funds, PE, real estate, commodities, infrastructure, other: strategies, sub-categories, benefits, risks, fees, due diligence
- describe benefits of alternatives in a portfolio context
- calculate & interpret management fees, incentive fees and net-of-fees returns of hedge funds
- describe valuation and return-calculation issues for each alternative category
- describe risk management of alternatives

## Frameworks Introduced
- **Six-category map of alternatives**: hedge funds, private equity, real estate, commodities, infrastructure, other (collectibles = tangibles; patents, litigation = intangibles).
  - When to use: to place any vehicle and predict its liquidity, data quality and fee basis.
  - How: ask (1) public or private? (2) equity or debt? (3) active or passive? (4) fund (LP) or direct? (5) what drives return: income, price, or manager skill?
- **Hedge fund strategy taxonomy (HFRI)**: equity hedge, event driven, relative value, macro (CAIA equivalents: market directional, corporate restructuring, convergence trading, opportunistic).
  - When to use: to build a portfolio of funds and choose the right benchmark.
  - How: equity hedge = bottom-up long/short equity (market neutral, fundamental growth/value, quantitative directional, short bias, sector specific); event driven = corporate events (merger arbitrage, distressed/restructuring, activist, special situations); relative value = pricing discrepancies (convertible arbitrage, fixed-income ABS / general, volatility, multi-strategy); macro = top-down trades on economic trends across rates, FX, equities, commodities.
  - Failure mode: labels overlap (distressed can sit in HF, PE or high yield) and drift over time; classify by actual exposure.
- **Fee waterfall for a hedge fund (management + incentive, hurdle, high-water mark)**:
  - When to use: to convert gross fund return into the LP's net return.
  - How: (1) management fee = rate x AUM (beginning, average or end-of-period per the PPM); (2) incentive base = gain, optionally net of management fee (net-of-management-fee basis), optionally net of the hurdle (hard hurdle: fee only on excess; soft hurdle: fee on the whole gain once cleared); (3) apply the high-water mark: no incentive unless net-of-fee value exceeds the prior peak, and only on the excess over it; (4) investor return = (ending - fees - beginning capital) / beginning capital.
  - Why it matters: the HWM stops the LP paying twice for the same performance; management fee is paid in losing years.
- **Due diligence grid (Exhibit 18)**: organization; portfolio management; operations and controls; risk management; legal review; fund terms.
  - When to use: before committing and as ongoing monitoring of fund vs prospectus.
  - How: verify track record basis (net/gross, estimated/market values), service providers (independent auditor, prime broker, administrator, custodian), valuation policy, leverage and counterparty limits, key-person and termination clauses, fee and carry terms, alignment (GP capital).
- **Commodity futures return decomposition**: total return = roll yield + collateral yield + change in spot price.
  - When to use: to explain why an index of futures differs from spot.
  - Failure mode: assuming commodity index return equals spot return.

## Key Concepts
- **Alternative investments**: non-traditional vehicles/assets (private, leveraged, short, illiquid, derivative-based), usually actively managed, with lower regulation and transparency.
- **Absolute vs relative return objective**: positive returns through the cycle versus return relative to an equity or bond benchmark.
- **Survivorship bias**: database holds only surviving funds, so liquidated (poor) funds vanish and index returns are overstated.
- **Backfill bias**: a fund enters a database with its prior (usually good) history added, overstating returns.
- **Smoothing / appraisal bias**: appraised or model values lag markets, so volatility and correlation with traditional assets are underestimated.
- **General partner (GP) / limited partner (LP)**: GP manages with unlimited liability; LPs own fractional interests with liability limited to capital.
- **Hurdle rate (hard/soft)**: minimum return before an incentive fee; hard = fee on excess only, soft = fee on entire return once cleared.
- **High-water mark**: highest net-of-fee value per investor that must be recovered before a new incentive fee.
- **Lockup / notice period / gate**: restrictions on redemptions to let managers unwind in an orderly way.
- **Drawdown**: fall in NAV below the high-water mark (worst drawdown = largest peak-to-trough cumulative loss).
- **Committed capital**: LP promise to fund, drawn over about 3-5 years; PE management fees (1%-3%) are charged on it.
- **Clawback**: GP returns incentive fees already paid until LPs have their capital back plus 80% of total profit.
- **Fund of funds (FoF)**: pool of hedge funds giving access, diversification, due diligence and better redemption terms at the cost of a second fee layer.
- **NOI / cap rate**: net operating income (before depreciation, financing, tax) divided by the capitalization rate (discount rate minus growth) gives property value.
- **FFO / AFFO**: REIT cash-flow proxies; FFO = net income + real estate depreciation - gains on property sales (+ losses); AFFO = FFO less recurring capex.
- **Contango / backwardation**: futures above spot (little convenience yield) versus below spot (high convenience yield).
- **Brownfield / greenfield**: existing infrastructure assets with operating history versus assets to be built.
- **Sortino ratio**: (mean return - target) / downside deviation.

## Formulas & Reference Tables
- `Sharpe = (R − R_f) / σ`; `Sortino = (R − target) / σ_downside` (downside deviation uses only returns below target). Exhibit 3 used target 0% for Sortino.
- `Management fee = m × AUM_basis`; `Incentive fee = i × max(0, gain − management fee [if net] − hurdle [if hard] − HWM shortfall)`.
- `Net return to LP = (V_end − fees − V_begin_LP_capital) / V_begin_LP_capital`.
- `Geometric mean = (Ending/Beginning)^(1/n) − 1`.
- `Minimum fund size = investor ticket / ownership limit` (e.g., 10 / 10% = 100; if the limit applies to the post-investment fund, pre-investment size = 90).
- `Direct capitalization: V₀ = NOI₁ / cap rate`; `cap rate = r − g`; multiple = 1 / cap rate.
- `FFO = NI + depreciation (real estate) − gains on sales + losses on sales`; `AFFO = FFO − recurring capex`.
- `Futures price ≈ Spot × (1 + r) + Storage − Convenience yield`; cost of carry = interest + storage.
- PE portfolio company valuation: market/comparables (EBITDA multiple x EBITDA), DCF (FCFF at WACC, FCFE at cost of equity), asset based (fair vs liquidation value).

| Category | Typical fee basis | Liquidity | Return data problem |
|---|---|---|---|
| Hedge fund | 1.6%/17.75% avg (2-and-20 historic) on AUM; FoF adds ~1%/10% | Lockups, 30-90 day notice | Self-reporting, survivorship, backfill |
| Private equity | 1%-3% of committed capital + 20% carry (net of hurdle) | Very low; 5-10 yr | Cost-based marks pre-2009, smoothing; quarterly vol 12.8% vs annual 21.1% |
| Real estate funds | 1%-2% of committed/invested capital + performance fee | Low (direct), high (REIT) | Appraisal lag; repeat-sales selection bias; REIT index looks like equities |
| Commodities | Futures: none; managed futures 2-and-20; energy partnerships 1%-3% | High (futures) | Index choice (S&P GSCI ~79% energy in 2008) |
| Infrastructure | PE-like funds; listed/MLP: public-equity fees | Low (direct), high (listed) | Few indices; clustering of listed assets |

Exhibit 2 highlights (1990-2014, annual mean / st. dev.): global stocks 6.9% / 16.5%; bonds 6.3% / 5.8%; hedge funds 7.2% / 6.0%; commodities 2.2% / 21.8%; real estate 10.4% / 18.1%; PE 15.4% / 20.3%; VC 15.0% / 47.2%. Sharpe (Libor): HF 0.63, PE 0.59, bonds 0.49, RE 0.38, VC 0.25, stocks 0.21, commodities −0.06. Sortino (target 0%): PE 1.19, bonds 1.09, RE 0.79, HF 0.74. Crisis Q4 2007-Q4 2009: stocks −10.8%, HF −4.9%, real estate −17.6%, commodities −15.9%. Correlations (1990-2014): commodities vs stocks 0.247, vs bonds 0.183, vs CPI 0.315; global REITs vs stocks 0.62, vs bonds 0.35.

## Mental Models
- **Read every alternative statistic through the data filter**: appraised or self-reported returns imply understated volatility and correlation and overstated return. Haircut the Sharpe ratio before you believe it.
- **Fees are the strategy's first hurdle**: a fund must out-earn its fee stack. On 2-and-20 a 0% gross year costs the LP 2%; a 10% gross year nets 6%.
- **Illiquidity plus leverage equals procyclical fragility**: drawdown, margin call, forced liquidation, redemptions, further drawdown. Notice and lockup periods exist to break this loop.
- **Correlation is regime dependent**: diversification is an average; in a crisis correlations among risky assets approach 1.
- **Manager dispersion dominates asset-class beta** in PE and hedge funds (Kaplan-Schoar: top-quartile IRR 22% vs bottom 3%); picking the manager is the allocation decision.
- **Match structure to liability**: infrastructure and real estate income fit long-dated liabilities; PE needs a long horizon and tolerance of capital calls.

## Worked Example
Hedge fund with 100 initial, 2% management fee on year-end value, 20% incentive fee (recomputed):
- Year 1, gross value 130. Independent fees: mgmt 2.6, incentive 6.0, total 8.6. LP net = (130 − 100 − 8.6)/100 = **21.40%**. Incentive on gain net of mgmt fee: 0.2 × (30 − 2.6) = 5.48, total 8.08, net **21.92%**. With a 5% hard hurdle and net-of-mgmt basis: 0.2 × (30 − 5 − 2.6) = 4.48, total 7.08, net **22.92%**.
- Year 2 (independent-fee structure plus HWM), value falls to 110: mgmt 2.2, incentive 0. LP capital goes from 121.4 to 107.8 = **−11.20%**.
- Year 3, value 128: mgmt 2.56; incentive only above the HWM of 121.4: 0.2 × (128 − 121.4) = 1.32. LP capital 124.12, return **15.14%**.
- Three years: arithmetic mean 8.45%, geometric mean (124.12/100)^(1/3) − 1 = **7.47%**, LP gain 24.12, total fees 14.68. Interpretation: the arithmetic average overstates the compounded LP experience, and GP fees of 14.68 were paid against an LP gain of 24.12.
- Fund of funds: underlying 2-and-20, 20% gross gives 14% net; FoF "1 and 10" then takes 1 + 1.4, so the LP nets **11.6%** versus 14% direct. The extra layer cost 2.4 points; buy it only for access, diversification or diligence.

## Anti-patterns
- **Quoting the index Sharpe ratio as the investment case**: smoothing and survivorship inflate it; the ratio also ignores skew and kurtosis.
- **Treating "uncorrelated" as a fact**: hedge funds were uncorrelated only in 2000-2001; correlation rose in 2008.
- **Comparing gross and net returns across funds** (Example 6): with 2-and-20 versus 1.5-and-15, fees can explain the whole return gap.
- **Sizing a fund check without an ownership cap**: one LP at 50% of AUM is a fund-closure risk.
- **Assuming a short notice period equals liquidity** when positions are a large share of each issue.
- **Chasing consistently smooth returns**: unusually good, steady performance is a fraud flag; insist on third-party custody and independent audit.
- **Equating a commodity index with spot prices**: futures indexes embed roll yield and collateral yield.

## Exam Focus & Traps
- Management fee base: hedge fund = AUM; private equity = committed capital (then invested capital). Quick discriminator in multiple-choice.
- Hurdle: hard hurdle = fee on excess over hurdle; soft = fee on whole return. Order of operations in the vignette: management fee first if incentive is "net of management fee".
- HWM is computed net of fees and is per investor; LPs entering at different dates have different HWMs.
- Sortino uses downside deviation, not standard deviation; target return 0% in Exhibit 3. Hedge funds win on Sharpe, PE and bonds on Sortino.
- Bias direction: survivorship and backfill inflate returns; appraisal smoothing deflates volatility/correlation.
- Valuation of liquid listed positions: mid quote is common; the conservative rule is bid for longs and ask for shorts (closing prices). Trading NAV may include a liquidity haircut; reporting NAV uses quotes.
- Repeat-sales index drawback = sample selection bias; appraisal index drawback = stale, subjective values; REIT index = behaves like equities.
- Contango = little convenience yield; backwardation = high convenience yield and positive roll yield.
- Brownfield = predictable cash flows; greenfield = growth and higher risk. Publicly traded infrastructure = liquidity, transparent governance, less control.
- As LTV rises, risk rises for both debt and equity investors.
- Angel investing is formative stage, before seed; seed is the first stage at which VC funds usually invest; mezzanine VC is pre-IPO bridge.
- ⚠ Correction/clarification: the source's due diligence example states a $90 million minimum fund size for a $10 million ticket at a 10% ownership cap. That holds only if the cap applies to the fund after the investment (90 + 10 = 100). If the ticket is 10% of current AUM, the minimum is 100; state the assumption.
- ⚠ Clarification: in the Year 3 fee calculation the source compares gross fund value (128) with a net-of-fee HWM (121.4), so it mixes bases. Follow the curriculum arithmetic on the exam; in practice apply the HWM consistently (per-investor net asset value).

## Key Takeaways
1. Classify by exposure: public vs private, equity vs debt, passive vs active, fund vs direct; then read the risks off the structure.
2. Expect lower liquidity, transparency and regulation, higher fees and leverage, and poor data; discount reported Sharpe ratios accordingly.
3. Diversification benefit is real on average but fails in stress; size the allocation with downside frequency, worst month and liquidity, not just mean and sigma.
4. Net return = gross return minus a fee waterfall: always recompute with hurdle, HWM and fee basis, and compare on a net basis.
5. Use downside measures (Sortino, VaR with non-normal inputs, shortfall risk) plus stress tests for skewed, fat-tailed payoffs.
6. PE and VC returns depend on manager selection (22% vs 3% top/bottom quartile) and on long commitments; demand a liquidity premium.
7. Commodity exposure comes through futures; return = roll + collateral + spot change; real return is about zero over time, inflation hedge is partial.
8. Due diligence must cover organization, process, operations, risk, legal and fund terms, and continue after investing.

## Connects To
- **ch02**: real estate valuation (NOI, cap rate, FFO/AFFO, NAV) in depth.
- **ch03**: private equity structure, fees, valuation, J-curve in depth.
- **ch04**: commodity futures pricing, roll yield, contango/backwardation in depth.
- **ch05**: hedge fund strategies and performance issues in depth.
- **ch06**: how much to allocate to alternatives in a portfolio.
- **`cfasi-portfolio-construction` ch15**: practitioner case for alternative investments in portfolio construction.
- **`cfa-equity-valuation` ch11**: private company valuation (comparables, DCF, asset based) used for PE targets.
- **`cfa-derivatives` ch01**: futures, forwards, swaps and options used to express commodity and hedge fund exposures.
- **`cfa-portfolio-management` ch04**: portfolio management overview and diversification.
