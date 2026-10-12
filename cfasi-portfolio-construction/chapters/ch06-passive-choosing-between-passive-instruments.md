# Chapter 6: Choosing Between Passive Instruments: Benchmark, Tax, Total Cost of Ownership, Tracking and Core-Satellite (Come scegliere tra diversi strumenti)
> **Source**: CFA Society Italy x Advisor Private, "Passive Investments" guide (Advisor Private no. 26, 2020), Chapter 2 | Andrea Semino, CFA; the closing insert on index investing and the climate crisis is sponsored by Amundi (Ilaria Pisani) and is attributed below

## Core Idea
Among index funds and ETFs tracking similar benchmarks, the winner is the one that minimizes **Total Cost of Ownership (TCO)** over the investor's horizon and replicates the benchmark most faithfully: look beyond the TER to benchmark rules, domicile and tax, replication method, turnover, securities lending, swap fees, bid-ask spread, market impact and tracking difference. The chapter ends with core-satellite as the structure that frees cost and risk budget for high-alpha satellites.

## Frameworks Introduced
- **Passive market picture (mid-2020, Morningstar)**: global fund and ETF assets about 41 trn USD with a little over one quarter passive; passive about 11 trn USD of which index funds 6.65 trn and ETFs 4.48 trn (active about 30 trn). Passive share above 40% of collective funds in the US vs below 20% of European portfolios; but passive took the bulk of net sales for 8 years (nearly all in 2014, 2016, 2018); in Europe about 50 cents of each net-sales dollar goes to passive. Drivers: low rates, fee pressure (MiFID II), ESG. ESG-passive products tripled in number and assets in five years. In the US about 2/3 of passive assets are funds; Europe about half. Tax quirks affect adoption (UK, Switzerland stamp duty on ETFs).
- **Due-diligence sequence for a passive instrument**: (1) benchmark, (2) tax profile and domicile, (3) TCO over the horizon, (4) tracking quality (difference and error), (5) operational specifics (currency/share class, accumulating vs distributing, hedged).
  1. **Benchmark first**: there are 148 index funds/ETFs registered for sale in Italy in "US equity" alone (Morningstar, Aug 2020); weighting scheme (cap-weighted MSCI USA, S&P 500, Nasdaq; price-weighted Dow; ESG; smart beta) drives cost and performance. TER range: a few bp for the plainest exposures to 0.60-0.80% for sophisticated smart beta; best-worst product gap was 15.6% in 2018 and 52.9% in 2019. Inclusion rules matter: S&P 500 and MSCI USA differ by over 100 names (e.g. profitability rule at S&P vs MSCI's methodology that admitted Tesla from September 2013). Bond benchmarks differ by legal form and issue-size cutoffs. Tilts (ESG, SRI, low carbon) change the index again.
  2. **Italian tax profile (as of 2020)**: UCITS "harmonized" funds/ETFs in administered regime are taxed 26% (12.5% on the share derived from Italian government bonds, white-list countries, supranationals); non-harmonized instruments (e.g. US ETFs) are declared separately at marginal rates. Prefer the harmonized wrapper. Gains from funds/ETFs are "capital income" while losses are "other income" (cannot offset gains within the same fund category in administered regime; losses still offset securities gains); tax is computed on purchase vs sale price, not NAV. ETCs (commodity-linked) are not funds and offset normally. Accumulating share classes defer the 26% on dividends and keep compounding; a distributing class reinvests only 74% of gross dividend after tax plus trading costs.
  3. **TCO = recurring costs (annual) + transaction costs (one-off)**; relative weight depends on horizon: tactical investors prioritize liquidity and low trading costs, long-term investors prioritize low recurring costs.
- **Recurring cost components (tracking difference)**: TER (management fee + admin including custody; EM custody can add 0.10-0.20% a year; share classes vary retail/institutional/hedged); sampling (replicating with a subset can drag); turnover/rebalancing costs; swap fee (synthetic); securities-lending income (positive); tax drag (positive or negative); the benchmark itself is gross of costs.
  - **Sampling case study**: iShares MSCI EM ETF (EEM) held only about half of index names before 2010; in 2009 its net return lagged the MSCI EM index by close to 7 points (NAV total return about 71.8% vs index 78.5%, table shows 6.72% difference), whereas Vanguard VWO (full replication, then tracking MSCI EM) lagged by 4.5 points in the table (76.3%); the text says roughly 2 points on NAV basis for the latter. Sampling is cheap to trade but creates tracking error; full replication has low ex-ante error but higher rebalancing costs.
  - **Synthetic replication via swaps**: gives near-perfect tracking (net of swap cost), at the price of counterparty credit risk. Funded swap (ETF holds cash, collateral posted externally, ETF swaps cash performance for index return; greater counterparty exposure) vs unfunded swap (ETF holds a collateral basket directly and swaps its basket return for index return via total return swap; less exposure). Mitigants: daily swap reset, over-collateralization, multiple counterparties. Swap fee is not in TER, so a synthetic ETF with TER 0.15% and swap fee 0.20% can show ex-ante tracking error near zero but tracking difference of 0.35% (verified 0.15 + 0.20 = 0.35).
  - **Turnover**: benchmark turnover drives cost: developed equity about 2.5% a year, EM about 11.5% (MSCI World factsheet); MSCI World 3.06% vs MSCI World Minimum Volatility 20.16% (about 6x); bond indices vary by maturity segment (1-5 year about 25% a year). Customized or concentrated indices (ESG, sector, smart beta) turn over more.
  - **Dividends, cash equitization and withholding tax**: cash between ex-date and payment can be equitized with futures for tight tracking, but some vehicles (notably SPY, structured as a US trust) cannot, hence systematic lag (-0.19% in 2019), despite scale (over 300 bn USD). Three layers of dividend tax: country of the stock (level 1), country of the vehicle (level 2), investor level (level 3, e.g. Italy). Gross-dividend benchmarks assume no tax; net-return benchmarks deduct standard withholding; physical funds usually sit between gross and net. Domicile choice: Luxembourg for many European equities, Ireland for US equity (US-Ireland treaty cuts US withholding from 30% to 15%; a Luxembourg fund bears the full withholding, an Irish ETF about half, a synthetic can replicate gross); for Brazilian bonds Irish structures face 15-22.5% withholding vs exemption for Luxembourg funds. Prefer relief at source to treaty reclaims (delays can distort returns).
  - **Securities lending**: global market about 2.3 trn EUR (ISLA, Sept 2020); index funds are good candidates because of low turnover and wide portfolios; Vanguard research estimated an average +0.03% a year (2007-2014), around 10 bp or more for small caps or special situations; policy types "value lending" (lend scarce, well-paid names, low utilization) vs "volume lending" (high utilization); low utilization/high margin is the conservative setting; some pension investors require no lending at all (common in Switzerland and Northern Europe). Treat lending income as a negative item in the TCO.
  - **Swap fee**: depends on contract size and asset class complexity; liquid equity markets can show zero or negative swap fees; often disclosed only by some issuers, otherwise inferred from tracking difference.
- **Transaction costs**: funds trade once a day at the closing NAV. Pricing methods: clean NAV (NAV excludes dealing costs; fixed anti-dilution levies charged on orders; preferred by institutions for performance attribution) or single swing pricing (NAV adjusted by net flow; widely available on platforms like AllFunds). ETFs: brokerage commission (may be embedded in spread or zero at US retail brokers), bid-ask spread (liquid ETFs generally under 10 bp but wider in stress; in March 2020 high yield and EM bond ETFs traded at discounts of about 6% to NAV), and market impact (size the order against the ETF's implied liquidity, i.e. liquidity of the underlying names; sector ETFs are most exposed).
- **Tracking quality**: **tracking difference** = realized return gap vs benchmark (what the client actually lives with); **tracking error** = volatility of that gap, ex-ante (model-based) or ex-post (actual, affected by stale prices or NAV accounting). Low tracking error does not mean low tracking difference (synthetic). Compare ETFs using official NAV data (not exchange prices) and benchmark in the right currency with WM/Reuters FX.
- **Illustrative comparison (MSCI Emerging Markets, Bloomberg 2019, ten UCITS products)**: five-year tracking differences ranged from -1.01% (UBS, LU) to -4.14% (Lyxor swap), i.e. -0.20% to -0.83% a year; ex-ante recurring cost estimates 0.26% to 0.90% a year. Best performer low-cost physical funds (Vanguard fund, CS Lux, UBS Lux), worst the expensive synthetic. Illustrative only; products and fees change.
- **Core-satellite**: passive core (60-80% of the liquid portfolio typically) for cost and tracking risk; active satellites for diversification, alpha, illiquid/thematic assets. Core-satellite also reallocates the risk budget (passive tracking error is negligible) and the cost budget (to high active-share managers). Driven by low rates, MiFID II, industry concentration and the need to contain tracking error (US DB pension deficits above 350 bn USD cited). Illustrative table (zero correlation between sleeves):

| Profile | Traditional: avg fund TER / total cost incl. 0.90% overlay | Core-satellite: avg TER / total cost | 
|---|---|---|
| Conservative | 0.87% / 1.77% | 0.42% / 1.32% |
| Balanced | 1.00% / 2.10% | 0.50% / 1.60% |
| Aggressive | 1.16% / 2.66% | 0.66% / 2.16% |

  Weights/fees used: traditional funds with equity 1.27%, bond 0.74%, alternatives 1.25%; core equity 0.18%, bond 0.17%, active satellite 1.80%. Fee totals verify (conservative traditional 20/75/5: 0.871%; core-satellite 15/70/15: 0.416%).
  **⚠ Correction**: the printed total tracking errors (3.45%, 3.70%, 4.20% vs 1.62%, 2.10%, 3.08%) do not follow from the stated inputs with zero correlation: recomputing the root-sum-of-squares gives traditional 2.42%, 2.38%, 2.97% and core-satellite 1.50%, 2.00%, 3.00%. The conclusion (lower fee, lower tracking error for conservative/balanced) holds; in the aggressive profile the two have similar tracking error (about 3%). Use your own recomputation.
- **Climate-index insert (Amundi, sponsored)**: ESG-integrated assets above 40 trn USD, about 45% of AUM; MSCI climate-change index variants outperformed parent indices in the periods shown (to July 2020, by the provider's presentation). EU Climate Transition Benchmark (CTB) and Paris-Aligned Benchmark (PAB) labels (delegated regulation, July 2020) require annual self-decarbonization and carbon-intensity cuts vs the parent index; PAB adds exclusions. Method: negative screens, reweighting by index-specific scores, optimization to hit the carbon-reduction path; uses Scope 1 (direct), Scope 2 (purchased energy), Scope 3 (other indirect) emissions plus forward-looking transition data. Issuer choice matters: engagement and voting policy should align with the index objective (Amundi reports voting against management at 55% of 2019 meetings). Vendor view; see also ch08 and the ESG chapters.

## Key Concepts
- **TER (Ongoing Charge)**: annual fee ratio accrued in NAV.
- **Share class**: fund variant (retail/institutional, hedged, accumulating/distributing) with its own TER.
- **Tracking difference / tracking error**: realized return gap / its volatility.
- **Physical full replication, sampling, synthetic**: ways to track an index (detailed in ch07).
- **Funded vs unfunded swap**: how collateral is held in synthetic ETFs.
- **Cash equitization**: using futures on cash awaiting distribution to stay fully exposed.
- **Withholding tax (WHT) / double tax treaty**: tax levied at source on dividends, recoverable or reduced by treaty.
- **Gross vs net total return index**: dividends reinvested before or after withholding.
- **Utilization rate**: share of the portfolio on loan.
- **Anti-dilution levy / swing pricing**: mechanisms charging transaction costs to the trading investors.
- **Bid-ask spread / market impact**: explicit and implicit trading costs.
- **Core-satellite**: passive core plus active satellites.
- **Active share**: degree to which holdings differ from the benchmark.

## Formulas & Reference Tables
- `Tracking difference (TD) = R_instrument - R_benchmark`; annualized from n years: `(1 + TD_total)^(1/n) - 1` or simply TD_total / n for small numbers (the source uses TD_total / 5).
- `Tracking error = std(R_instrument,t - R_benchmark,t)` (ex-ante from model, ex-post from data).
- `Expected TD (synthetic) = -(TER + swap fee) + other items`; `Expected TD (physical) = -(TER + sampling + turnover cost + tax drag) + lending income`.
- `Net reinvested dividend (distributing, Italy) = gross dividend x (1 - 0.26)`.
- `Portfolio TER = sum(w_i x TER_i)`; `Portfolio TE (uncorrelated) = sqrt(sum((w_i x TE_i)^2))`.
- Tax-drag intuition: accumulating share class defers the dividend tax, so compounding works on 100% of the dividend until sale.

## Mental Models
- Use TCO over your horizon: tactical flows favor liquidity and tight spreads; buy-and-hold favors lowest recurring costs and lowest tracking difference.
- Use tracking difference (not TER, not tracking error) as the realized-cost measure.
- Use domicile as a tax tool: Irish ETFs for US equity, Luxembourg funds for many EM bonds, always harmonized UCITS for Italian clients.
- Use synthetic only if you accept counterparty risk and read the swap fee.
- Use core-satellite to fund active risk from the cost saved on the core.
- Use official NAV data for comparisons, never intraday exchange prices alone.

## Worked Example
Compare two EM ETFs over 5 years from the source's table. Inputs: Product A (physical, lending, TER 0.23%, 5-year TD -1.01%, ex-ante cost 0.27%); Product B (synthetic, TER 0.55%, swap 0.40%, 5-year TD -4.14%, ex-ante cost 0.90%). Steps: annualized TD A = -1.01/5 = -0.20% a year; B = -4.14/5 = -0.83% a year; difference = 0.63% a year; on 100,000 EUR over 5 years, extra drag about 0.63% x 5 x 100,000 = 3,150 EUR (simple, ignoring compounding; about 3,200 compounded at 6%). Interpretation: the 0.32% TER gap understates the real gap because of swap fees; compare tracking difference.

## Anti-patterns
- Ranking ETFs by TER alone.
- Comparing an ETF's exchange price returns with a fund's NAV returns.
- Assuming a low tracking error synthetic ETF has low cost.
- Choosing a non-harmonized (US-domiciled) ETF for an Italian taxable client.
- Distributing share class for a long-horizon taxable investor who reinvests.
- Ignoring order size versus ETF liquidity.
- Using backward-looking TD to predict cost without checking whether the TER has been cut.

## Practitioner Notes
- Always list: benchmark (and its weighting rules), TER and share class, domicile, replication, lending policy, swap fee, spread, AuM, tracking difference over 3 and 5 years.
- Recompute the 'tax drag' if your client's tax regime differs; Italian figures are 2020.
- Loss-offset rules for ETFs in administered regime make harvesting hard; check before switching.
- ETFs show 6% discounts to NAV in HY and EM bonds at the March 2020 peak; avoid market orders in stress.
- The Amundi insert is promotional on climate indices; the CTB/PAB regulation facts are the useful part.

## Key Takeaways
- Choose the benchmark first: similar-looking indices can differ by 100+ constituents and large returns.
- TCO = recurring costs (TER, sampling, turnover, swap fee, tax drag minus lending income) + one-off costs (commission, spread, market impact).
- Tracking difference is what you earn; tracking error is how erratic it is.
- Domicile and wrapper decide tax drag: Irish for US equity, Luxembourg for some EM bonds, harmonized UCITS in Italy.
- Synthetic replication trades counterparty risk for lower tracking error but hides swap costs.
- Accumulating share classes avoid the 26% tax haircut on reinvested dividends.
- Core-satellite typically holds 60-80% in passive, lowering fee and tracking error.

## Connects To
- **ch05**: why passive and the risks of passive vehicles.
- **ch07**: replication choices and what passive managers do daily.
- **ch08**: smart beta, thematic and ESG alternative indices.
- **ch02-ch03**: core-satellite, benchmarks and tracking error in allocation.
- **ch09-ch14**: ETF and fund selection (scoring, due diligence).
- **`cfa-portfolio-management` ch02, ch11**: index construction, ETF structure and tracking.
