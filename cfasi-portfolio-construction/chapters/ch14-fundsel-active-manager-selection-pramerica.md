# Chapter 14: Selecting an Active Manager: The Pramerica SGR Framework (La selezione di un gestore attivo: il framework utilizzato da Pramerica SGR)
> **Source**: CFA Society Italy x Advisor Private, "ETF & Fund Selection" guide (Advisor Private no. 16, 2019), Chapter 6 | Anna Silvia Bruschi, Camilla Silvani and Teodor Naumov, CFA (Pramerica SGR multimanager team); illustrations use Pramerica internal data for teaching purposes

## Core Idea
A practitioner's fund-of-funds workflow: collect daily data, screen a peer group quantitatively (quartiles, share of negative periods), build a one-page Quantsheet of statistics per fund (beta, R-squared, tracking error, information ratio, drawdown, up/down capture, factor betas), run a qualitative due diligence (people, organization, process, risk, costs, ESG), combine into a Quant Ranking Score and build portfolios by combining scores (score-weighted, risk parity, Z-score maximization, "plateau optimization"). The team never recommends funds in the abstract; the analysis always ends in a portfolio and tolerates marginal use of some strategies because they diversify.

## Frameworks Introduced
- **Four-step process**: (1) data collection and analysis; (2) evaluation and selection of UCITS funds; (3) portfolio construction; (4) monitoring risk and performance. New funds enter the database through a standard questionnaire (administrative data plus preliminary classification).
- **Data hygiene**: use daily time series, but correct for missing observations caused by different market closures and administrative issues: daily-corrected official NAV creates an intraday-like proxy so fund and benchmark are comparable. For multi-time-zone universes (global equity) weekly data may be better than daily.
- **Peer-group screening**: build the universe per asset class and sub-peer-groups (passive and semi-passive separate from flexible, very active strategies); metrics: quartile ranking, percentage of negative observations, percentage of observations below the peer group average; evaluate on YTD, 3y, 5y and since inception plus event windows (example August 2015 to February 2016). Reduce to a short list. Case: 16 euro-equity funds vs a Euro Stoxx benchmark, 2016-2019 (annual relative performance, three yearly observations each): quartile incidence table, e.g. Fund 3 and Fund 13 spent 67% of years in the top quartile while Fund 14 spent 67% in the bottom quartile and was negative in every year (-11.1% cumulative). The analyst also asks how often a fund underperforms in market downturns; rejected strategies are sometimes revisited with a contrarian lens for mean reversion.
- **Quantsheet** (per fund):
  - Beta (systematic risk; for global area use lower-frequency data).
  - R-squared and tracking error, 60-day and 20-day rolling (specific risk).
  - Information ratio (consistency).
  - Standard deviation and Sharpe ratio (absolute risk).
  - Maximum drawdown (the largest loss from a prior peak; read against volatility and return, also to see recovery capacity).
  - Volatility ratio (fund vs benchmark).
  - Coincidence of overperformance with rising markets and underperformance with falling ones (aggressiveness; clients react differently depending on the market context).
  - Graphics: daily fund, benchmark, ratio and differential across horizons; rolling relative drawdown; quarterly performance vs benchmark.
  - Effective exposure to asset classes over time, to allow tilting the portfolio by increasing or decreasing those exposures; factor exposure via beta to individual factors (momentum, value, low vol, quality, growth, size) which is more stable than multi-factor regressions across horizons.
  - Example output (Fund 1 Euro Equity, 30 Dec 2015 to 8 Feb 2019, benchmark DJ Euro Stoxx TR): cumulative 144.84% vs 103.91% (+40.93 pts); annualized period figure 12.71% vs 7.01% (+5.70); volatility 15.14% vs 15.57%; correlation to benchmark 0.98; rolling beta 0.93-0.98; volatility ratio 94-99%. (The Information Ratio values 0.58 and 0.42 and tracking error entries in the source table do not reconcile with a simple excess/TE ratio; treat as illustrative.)
- **Sub-peer-groups**: separate passive/semi-passive from flexible strategies for fair comparison.
- **Qualitative due diligence**: investment management team (lead PM, co-managers, expertise, roles, research process, key events); strategy and portfolio (philosophy, objectives, style/strategy changes, composition, diversification, trading, quantitative models, derivatives, collateral); administrative/legal (UCITS status, settlement, dealing and valuation periods, share class, platform availability, AUM, subscription limits); costs (management fee, TER with administrative costs, performance fee, other costs such as financing for leveraged products); organization (staff, structure, incentives, risk management, audit, depositary). Sources: questionnaire answers, prospectus/KIID, meetings with portfolio managers and phone interviews.
- **ESG overlay**: no universally accepted taxonomy yet; Pramerica uses (a) quantitative ESG scoring from external databases for homogeneity, (b) a review of the manager's declared ESG process; results feed the qualitative due diligence.
- **Quant Ranking Score**: output of all analyses, set by conviction in the fund and its risk. Applicable to long-only and alternative (total return/UCITS alternatives) classes; correct classification into homogeneous risk-driver categories is essential; the more complex the risk drivers, the harder the analysis (multi-asset blends allocation, timing, sector/style, stock picking; global bonds where open currency risk is itself an alpha source, so separate currency contribution from asset alpha).
- **Alternative-fund extras**: Z-score, Sharpe, and `max drawdown / standard deviation` (flag when it exceeds a threshold of 2-2.5 standard deviations of drawdown, over at least 3 years); beta to credit, high yield, Treasuries, US equity, euro equity, measured overall, in up markets (beta up), in down markets (beta down) and in tails (tail beta). Classification blends HFRI categories with total return bond strategies; each category tied to underlying risk premia: Long/Short Equity and Market Neutral use equity premia (quality, momentum, value, size, low volatility); Event Driven draws on a liquidity premium; Global Macro/CTA on cross-asset momentum; Long/Short Credit on quality, momentum, value, carry from credit; Multistrategy and Macro/Systematic use combinations of premia. Control the correlation between categories (heat map: Fixed Income Absolute vs L/S Equity 0.54; L/S Equity vs Market Neutral 0.65; Global Macro/Systematic near zero with all, -0.07 to 0.16).
- **Portfolio construction**: the team does not publish a list of "buy" funds; analysis exists to build portfolios, and may use marginally some strategies despite higher volatility because they decorrelate genuinely. Method: (1) a score-weighted portfolio (Quant Ranking Scores combined with qualitative results); (2) compare with a risk parity portfolio and with a Z-score-maximizing optimization (historical correlations) and "risk-adjusted" solutions with EWMA correlations; (3) **Plateau Optimization**: combine solutions to obtain a sufficiently diversified portfolio near the information-ratio efficient frontier, aiming for consistent performance over medium/long horizons. Example "Model" portfolio vs Euro Stoxx (31 Jul 2013 to 27 Feb 2019): 58.19% vs 46.05% (+12.13 pts as printed; arithmetic difference 12.14), rolling 20-day volatility 12.62 vs 12.51 (ratio 100.9%), correlation 0.99; monthly alpha table total +0.17% (2013 partial), +0.64%, +3.90%, +1.25%, +2.33%, -1.22% (2018); maximum drawdown of relative performance -2.32% on 16 Oct 2014.

## Key Concepts
- **Peer group / sub-peer group**: homogeneous set of funds for comparison.
- **Quartile incidence**: share of periods in each quartile.
- **Quantsheet**: single-page statistical dossier of a fund.
- **Rolling R-squared / tracking error (20d, 60d)**: short-window estimates of specific risk.
- **Beta up / beta down / tail beta**: market sensitivity in rising, falling and extreme markets.
- **Z-score**: standardized deviation of a statistic vs the peer group.
- **Max drawdown / standard deviation ratio**: tail-risk indicator.
- **Risk premia**: systematic return sources behind each strategy category.
- **EWMA correlation**: exponentially weighted correlation estimate.
- **Plateau optimization**: combining several optimization solutions to avoid fragile single-point optima.
- **Quant Ranking Score**: composite fund score.
- **KIID**: key investor information document.

## Formulas & Reference Tables
- `Max drawdown = min over t of (V_t / max_(s<=t) V_s - 1)`.
- `Relative drawdown = same measure applied to the ratio fund/benchmark`.
- `Volatility ratio = sigma_fund / sigma_benchmark`.
- `Information ratio = annualized active return / annualized tracking error`.
- `Drawdown test = Max drawdown / standard deviation` (>2-2.5 flags excessive risk; window at least 3 years).
- `Cumulative difference` check: 144.84 - 103.91 = 40.93; 12.71 - 7.01 = 5.70 (verified).
- Process checklist:

| Stage | Output |
|---|---|
| Data collection | questionnaire, daily NAV series corrected |
| Quantitative screen | short list from peer-group quartiles and negative-observation share |
| Quantsheet | statistics and graphs per fund |
| Qualitative DD | people, process, costs, legal, ESG, risk |
| Score | Quant Ranking Score |
| Portfolio | score weighted vs risk parity vs Z-score; plateau optimization |
| Monitor | risk and performance, tilting by exposure |

## Mental Models
- Use quartile incidence (share of years in each quartile), not one-year rank, to judge consistency.
- Use rolling 20d/60d R-squared and tracking error to spot style drift early.
- Use up-capture/down-capture style statistics (beta up/down) to learn whether alpha is skill or just market exposure.
- Use factor betas one factor at a time for stability.
- Use a risk-premia map to classify alternative funds before comparing them.
- Use portfolio-level thinking: a volatile fund with truly low correlation can earn a place.

## Worked Example
Peer-group screening. Inputs: the 16-fund euro-equity case. Fund 14: quartiles over three annual observations: 0% I, 0% II, 33% III, 67% IV; cumulative relative performance -11.1%; negative in 100% of years. Fund 15: 67% I, 33% III; cumulative +10.3%; negative in 33% of years. Steps: apply illustrative filters (my thresholds, not the source's): "at most one of three years below the peer-group average" and "top two quartiles in a majority of years"; Fund 14 fails both, Fund 15 passes; Fund 7 (0% I, 33% II, 67% III, cumulative -3.4%) and Fund 9 (-3.3%) fail on quartile. Result: a short list of the funds passing (for example Funds 13, 15, 16, 3, 10, 11) goes on to Quantsheets. Interpretation: three annual observations are a thin sample; quartiles reduce workload, but the Quantsheet and due diligence decide.

## Anti-patterns
- Using one return series frequency across all time zones.
- Ranking on cumulative return alone.
- Treating alternative strategies as one asset class with one benchmark.
- Reading historical beta as stable across market regimes (use beta up/down/tail).
- Recommending funds in a vacuum rather than in portfolios.
- Dropping a strategy after one bad year without a contrarian/mean-reversion check.
- Ignoring currency effect as a source of alpha in global bond funds.

## Practitioner Notes
- Always request the manager's questionnaire and verify with KIID and a live meeting.
- Keep a correlation heat map across categories of alternatives; look for categories with near zero correlation (macro/systematic).
- A fund that adds diversification may be worth holding with small weight even with higher volatility.
- Define event windows (crisis and recovery) as part of every screen.
- Combine optimization outputs (plateau) to reduce fragility of a single optimized weight set.

## Key Takeaways
- Build the process as data, quantitative screen, Quantsheet, qualitative DD, score, portfolio, monitoring.
- Peer-group quartile frequency and share of negative periods filter quickly but need follow-up.
- Rolling R-squared, tracking error, beta up/down, drawdown ratios catch what averages hide.
- Alternative funds require risk-premia classification, correlation heat maps and tail-aware ratios.
- Selection ends in portfolio construction, combining scores with risk parity and Z-score optimization into a plateau solution.
- Qualitative due diligence (team, process, incentives, risk, costs, ESG) confirms or overrides the numbers.

## Connects To
- **ch11**: the general four-phase framework this chapter implements.
- **ch13**: manager-level optimization and pure alpha.
- **ch09-ch10**: purpose and cost logic (FAR).
- **ch03**: performance measures (Sharpe, information ratio, drawdown).
- **ch15-ch19**: alternatives guide: risk premia and hedge-fund strategies.
- **`cfa-portfolio-management` ch19 / `cfa-wealth-institutional-management` ch04**: manager due diligence.
