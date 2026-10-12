# Chapter 25: A Fund-Selection Example in Emerging-Market Equities
> **Source**: CFA Society Italy × Advisor Private, *Emerging Markets* guide (2021), Ch. 4 "Un esempio di fund selection sui mercati azionari emergenti" | Giovanni Semprini, CFA; plus Capital Group insert "Cina, da fabbrica del mondo a innovatore" (Robert Lovelace, Christopher Thomsen; sponsor content, attributed)

## Core Idea
A worked, replicable fund-selection process: define the investable universe, screen quantitatively to a short list, then run documentary, geographic, sector, factor, correlation and qualitative due diligence, and finish with a **complementary combination** of funds rather than a single winner. The key lesson is that **quantitative screens are necessary but not sufficient**: a fund can pass every filter and still have a changed mandate, a hidden developed-market allocation or an unstable team. The process is one of many; it must be structured, repeatable and look at risk from several angles.

## Frameworks Introduced
- **Fund-selection funnel (EM equity)**
  1. **Universe**: use a data provider (Bloomberg, Morningstar Direct, Refinitiv Lipper); global EM equity funds, excluding single-country (e.g. India) and single-region (e.g. Latin America) funds and frontier-only funds; target funds with geographic, sector and factor profile similar to MSCI Emerging Markets. Result: about 700 funds.
  2. **Quantitative screen**: share-class currency USD; no funds of funds; registered in Italy; UCITS with daily liquidity; inception before 31/12/2017; AUM over USD 100m. Result: about 100 funds.
  3. **Short list (the "brutal and naive" filter)**: keep only funds beating the benchmark (MSCI EM) in each of 2018, 2019 and 2020. Result: 6 funds. (Alternative considered and rejected for brevity: weighted quantitative scoring on absolute metrics such as return, volatility, Sharpe, maximum drawdown, Sortino, downside deviation, Calmar and relative metrics such as excess return, tracking error, information ratio, correlation, beta, upside and downside capture, Jensen's alpha, on calendar-year or rolling windows.)
  4. **Quantitative profile of the short list (Table 1; weekly data, 3 years, as of 15/07/2021)**
     | Fund | Excess 2021 | 2020 | 2019 | 2018 | Max drawdown 3Y | Sharpe 3Y | Tracking error | Information ratio |
     |---|---|---|---|---|---|---|---|---|
     | 1 | 2.12% | 4.88% | 6.18% | 4.02% | -29% | 0.68 | 4.89% | 0.93 |
     | 2 | 3.44% | 6.73% | 9.44% | 2.10% | -30% | 0.73 | 6.78% | 0.65 |
     | 3 | 1.15% | 4.91% | 11.12% | 1.24% | -32% | 0.70 | 6.39% | 0.73 |
     | 4 | -2.99% | 0.18% | 4.56% | 0.38% | -29% | 0.47 | 4.23% | 0.09 |
     | 5 | 1.89% | 38.61% | 6.17% | 0.71% | -26% | 1.05 | 11.10% | 1.11 |
     | 6 ("Enhanced Index") | 1.36% | 0.47% | 4.53% | 5.93% | -30% | 0.71 | 11.22% | 0.43 |
     Reading: Funds 1 and 2 most balanced; Fund 3 has the deepest drawdown (March 2020); Fund 4 has the lowest tracking error but the worst Sharpe and information ratio; Fund 5 has high tracking error yet the best information ratio due to an extreme 2020 (+38.6% excess); Fund 6 name says enhanced index but tracking error is 11.2%, inconsistent.
  5. **Eliminate with documents and data checks**
     - **Fund 6 out**: asking the investment house showed a **mandate change in June 2019** (previously an active Latin America fund). The pre-June 2019 history is invalid, so inception date and all Table 1 stats except 2020-21 excess return no longer hold.
     - **Fund 2 out**: the factsheet shows geographic allocation by area: Emerging Markets 42.6%, North America 25.3%, Europe 16.5%, Pacific ex-Japan 5%, Japan 2.5%, other 1.7%, cash 6.3%; too far from the MSCI EM benchmark (likely mis-classified by the data provider). Its KIID also makes no reference to the MSCI EM index so large deviations are possible.
     - KIID checks: Fund 1 at least 70% of assets in EM equities, active with discretion, MSCI EM used as reference; Fund 3 explicit ESG approach (climate, water, waste, biodiversity, product safety, supply chain, health and safety, human rights; firm-wide exclusion list including cluster munitions and anti-personnel mines) and a 30% cap on Chinese onshore A and B shares. China weight in MSCI EM is 37.5% at 30 June 2021, so the cap creates differentiation.
  6. **Geographic allocation relative to the benchmark (Table 2, percentage points)**: Fund 1 close to benchmark (China -3.4, Taiwan -4.5, Korea -3.3, India +1.7, Brazil +2.0, Russia +4.7, other +6.1); Fund 3 China -8.0, Korea -7.6, India +4.1, South Africa +4.3, other +9.8; Fund 4 China +3.7, small deviations elsewhere; Fund 5 India +11.4, Korea -13.2, China -4.7, other +16.1 (the "other" bucket is about 30% outside EM: US 12.1%, Singapore 7.9%, Germany 7.1%, cash 2.8%). All managers underweight Korea (unanimous view); no other country shows a consensus.
  7. **Sector allocation relative to benchmark (Table 3)**: Fund 1 no large tilts (financials +5.2, industrials +3.0, staples -4.1); Fund 3 IT +6.4, communication -7.1, health -5.0, energy -5.0, and no exposure at all to health care, energy, real estate and utilities (most concentrated); Fund 4 financials +10.4; Fund 5 consumer discretionary +13.0, communication +6.9, financials -5.5, no energy or utilities. All underweight real estate and utilities, suggesting a growth-oriented bias to verify with factors.
  8. **Factor analysis (Table 4; bottom-up from underlying holdings, Anima SGR method, relative to the benchmark; = similar, + / ++ / +++ higher, - / -- / --- lower)**: Fund 1: momentum =, quality -, size =, growth =, low volatility -, yield -. Fund 3: momentum +, quality +, size =, growth +, low volatility =, yield -. Fund 4: all = except low volatility +. Fund 5: momentum ++, quality -, size =, growth +++, low volatility ---, yield ---. Only Fund 5 differs strongly (growth and momentum, less yield and low-vol; more volatile). Alternative methods exist (top-down regression or style analysis with MSCI factor indices).
  9. **Performance review (Figures 4-7)**: Since January 2018 Fund 5 cumulated about +180% vs Funds 2-3 at 147% and Fund 4 and benchmark at 126-128%. Returns were similar in 2018-19; the gap came in 2020 when growth was rewarded, but MSCI EM Growth beat MSCI EM by only about 10.5% between January 2020 and mid-July 2021, so style alone does not explain it: Fund 5 also had "alpha" from stock selection, country allocation or factor timing. In 2021 growth underperformed value, and Fund 5 suffered a drawdown of about 21% between mid-February and mid-March 2021, much deeper than peers, yet it still beat the benchmark year-to-date (+1.86%). Use performance attribution (sector, country and factor allocation, then stock selection) to confirm the source of excess return.
  10. **Correlations (Table 5; weekly, 3Y)**: Fund 1 vs benchmark 0.96, Fund 4 vs benchmark 0.97, Fund 1 vs Fund 4 0.97, Fund 3 vs benchmark 0.94, Fund 5 vs benchmark 0.84 (lowest, vs other funds 0.82-0.83). Within one asset class, about 0.8 is an excellent diversification result.
  11. **Qualitative due diligence**: team, process and firm via direct interviews and questionnaires. Past performance does not persist: S&P US Persistence Scorecard shows of the funds in the top half in 2016 only 21.4% stayed top half in 2017, falling to 4.8% in 2020 (vs random expectations of 25%, 12.1%, 12.5%, 6.5%, 6.25% shown on the chart; reading is that persistence is no better than chance). Morningstar finds Gold, Silver and Bronze rated funds outperform Neutral and Negative on average (five pillars: People, Parent, Process, Performance, Price). EM-specific checks: team experience in EM and physical presence of analysts in main EM economies (language and culture barriers).
- **Conclusion: complementary combination**: exclude Fund 4 (same exposure as Fund 1, lower return, correlated with the index) and construct with: **Fund 1** = enhanced index (low tracking error, close allocations, consistent excess return); **Fund 5** = most active (large sector and country differences, growth bias, but decorrelated); **Fund 3** = intermediate (more active than Fund 1 with sector gaps and China cap, but factor profile near the benchmark).

## Key Concepts
- **Investable universe / short list**: initial pool and narrowed set for deep due diligence.
- **Apples-to-apples**: compare funds with similar exposures so that results do not reflect structural differences.
- **Excess return** (vs MSCI EM, in USD): fund minus benchmark.
- **Tracking error / information ratio / Sharpe ratio / maximum drawdown**: relative and absolute quality measures.
- **KIID**: key investor document with objectives and constraints.
- **Mandate change**: breaks the validity of the track record.
- **Active share / relative allocation**: weight differences vs benchmark by country and sector.
- **Factor tilts**: momentum, quality, size, growth, low volatility, yield.
- **Performance attribution**: split of excess return into allocation and selection.
- **Persistence**: whether top performers stay top performers (little evidence).
- **Enhanced index**: low tracking error with modest alpha target.
- **Complementary portfolio of funds**: mix of core and satellite managers.

## Formulas & Reference Tables
- `Excess return = R_fund - R_MSCI EM` (USD).
- `Tracking error = std(R_fund - R_benchmark)`; `Information ratio = annualised excess return / tracking error`. Example check, Fund 1: if IR 0.93 and TE 4.89%, the annualised excess return implied is **4.55%** (consistent with the 2018-2021 excess returns 2.1-6.2%).
- Implied annualised excess returns: Fund 5: 1.11 x 11.10% = **12.3%**; Fund 2: 0.65 x 6.78% = **4.4%**; Fund 3: 0.73 x 6.39% = **4.7%**; Fund 4: 0.09 x 4.23% = **0.4%**; Fund 6: 0.43 x 11.22% = **4.8%**.
- Relative weight: `w_fund,i - w_bench,i` by country/sector.
- Persistence expectation if random: ratios in the S&P chart (25%, 12.1%, 12.5%, 6.5%, 6.25%).

## Mental Models
- Use a **funnel**: broad data screen, then a simple rule, then documents, then holdings, then people.
- Use **document verification** before any quantitative ranking (KIID, factsheet, provider call).
- Use **relative allocation tables** to identify unanimous views (Korea underweight) vs idiosyncratic bets.
- Use **factor look-through** to tell style beta from alpha; ask for attribution.
- Use **core-satellite mix of funds**: enhanced index + intermediate + high-active decorrelated manager.
- Use **0.8 rule**: inside one asset class, fund-to-fund correlation near 0.8 is already good diversification.

## Worked Example
Check what Fund 5's 2020 excess return means for the information ratio.
- Information ratio 3Y = 1.11; tracking error 11.10%; implied annualised excess return = 1.11 x 11.10 = **12.3%** a year.
- Excess returns by year: 2018 0.71%, 2019 6.17%, 2020 38.61%, 2021 YTD 1.89%. Without 2020, the average of the other three periods is ((0.71 + 6.17 + 1.89)/3) = **2.9%**.
- Averaging the four printed periods gives (0.71 + 6.17 + 38.61 + 1.89)/4 = 11.8%; replacing 2020 with the 2018-19 average (about 3.4%) gives about 3.0%, roughly a quarter of the headline figure.
- Interpretation: the headline IR depends on a single outlier year (growth rally); this is why the author asks for attribution and keeps the fund only as a decorrelated satellite.

## Anti-patterns
- Choosing the highest information ratio without checking the source of the excess return.
- Ignoring mandate changes, manager changes or reclassification (Fund 6, Fund 2).
- Using a short list built by "beat the benchmark three years in a row" as a skill test (author admits it is naive; persistence is weak).
- Combining funds that duplicate each other (Funds 1 and 4 correlation 0.97).
- Forgetting that a fund's non-EM allocation (Fund 5: about 30% outside EM) can clash with other holdings.
- Comparing funds with different share-class currencies or domiciles.

## Practitioner Notes
- Sponsor insert (Capital Group) on China: R&D spending growth, patent filings (China about 1.4m filings in 2019 vs US 621k, Japan 308k, Korea 219k, EPO 181k), shift from manufacturing to services and innovation, internet platforms (Tencent, Alibaba), healthcare, clean energy such as city gas networks, with accounting and trade-tension risks and a need for on-the-ground research. Advocacy for active management; use as a theme note.
- Fund names are anonymised; the framework, not the product list, is the takeaway.
- For the full method of fund diligence see the sister guides on ETF & fund selection in `cfasi-portfolio-construction`.

## Key Takeaways
1. Start from an investable universe of comparable funds (700 → 100 → 6).
2. A simple screen ("beat benchmark each year 2018-2020") works as a first cut but is naive.
3. Always verify mandate, KIID, factsheet and provider data: two funds out for qualitative reasons.
4. Compare country, sector and factor tilts relative to the benchmark.
5. Excess return needs attribution; the strongest fund's IR rested on one growth-driven year.
6. Past performance rarely persists; qualitative review of team, process and firm is decisive.
7. Final design combines complementary funds: enhanced index, intermediate, high-active.

## Connects To
- **ch22-ch23**: EM index composition and the equity case for EM.
- **ch21**: the thematic product due diligence analogue.
- **`cfasi-portfolio-construction` ch09-ch14 (ETF & Fund Selection)**: general fund-selection methods; `ch05-ch08` passive investing.
- **ch06-ch08**: factor definitions used in the factor analysis.
