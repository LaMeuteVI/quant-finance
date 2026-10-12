# Chapter 6: Overview of Asset Allocation
> **Source**: CFA Program Curriculum 2023, Level III, Reading 5 · Portfolio Management (Asset Allocation) | William W. Jennings, PhD, CFA, and Eugene L. Podkaminer, CFA

## Core Idea
Asset allocation is the first, and by far the most consequential, portfolio construction decision. It must be anchored in good governance and in the client's full economic balance sheet (not just the financial portfolio), then built with one of three approaches that differ in objective and in the definition of risk: asset-only (efficient use of asset risk), liability-relative (fund the liabilities, then seek growth) and goals-based (hit each goal with a required probability). Implementation choices (tactical deviation, passive/active, risk budgets) and rebalancing policy complete the process, with rebalancing being about risk control, not return enhancement.

## Learning Outcomes Covered
- describe effective investment governance and its role in asset allocation
- formulate an economic balance sheet and interpret it for allocation
- compare objectives and risk concepts of asset-only, liability-relative and goals-based approaches
- explain asset classes as exposures to systematic risk and the criteria for specifying them; explain risk factors vs asset classes
- recommend and justify a strategic allocation from objectives and constraints; use the global market portfolio as baseline
- discuss implementation (passive/active, vehicles, risk budgets) and rebalancing strategy

## Frameworks Introduced
- **Six elements of effective investment governance**: (1) articulate long- and short-term objectives, (2) allocate decision rights by knowledge, capacity, time and hierarchy position, (3) process to develop/approve the IPS, (4) process to develop/approve the strategic asset allocation (SAA), (5) reporting framework, (6) periodic independent governance audit.
  - When to use: reviewing any institution's setup (committee, staff, third parties) or advising an individual's delegation to an adviser.
  - How (division of labour): committee crafts mission, approves IPS and SAA, oversees; staff drafts IPS/SAA, selects managers, runs rebalancing within the IPS; third parties (consultants, custodian, actuaries, managers) provide input and execute; an independent party audits.
  - Failure modes: committee drowning in manager selection with little time on asset allocation and risk; political non-economic influence; key-person risk; "decision-reversal risk" (abandoning the plan at the point of maximum loss); blame avoidance; turnover without documented beliefs.
- **Economic balance sheet**: financial assets and liabilities plus extended (off-balance-sheet) assets and liabilities; economic net worth = economic assets − economic liabilities.
  - When to use: before any allocation. It reveals hidden correlations between the client's non-financial exposures and the portfolio.
  - How: individuals: extended assets = human capital (PV of mortality-weighted future earnings), PV of pensions and expected inheritances; extended liability = PV of future consumption and goals (education, gifts, trusts). Institutions: extended assets = PV of expected contributions, royalties, mineral rights; extended liabilities = PV of future support or spending (foundations).
  - Why it matters: human capital is roughly 30% equity-like and 70% bond-like on average (varies by industry), so a young investor's financial portfolio can be equity heavy and should glide toward bonds as human capital converts to financial capital (glide path example: 85/15 equity/bonds at age 25, 82/18 at 35, 77/23 at 45, 63/37 at 55, 49/51 at 65). Failure mode: concentration (employer stock plus employer-paid human capital; endowment real estate correlated with the university's own real estate).
- **Three approaches to asset allocation** (table below): asset-only, liability-relative, goals-based.
- **Asset class specification criteria (five)**: (1) relatively **homogeneous** within; (2) **mutually exclusive** (e.g. domestic equity plus global ex-domestic, not global including domestic); (3) **diversifying** (rule of thumb: pairwise correlation above 0.95 undesirable; test an asset against the combination of all others, not only pairwise); (4) as a group a **preponderance of world investable wealth**; (5) capacity to **absorb a meaningful portion** of the portfolio (liquidity, costs).
  - Greer's three super-classes: capital assets (valued by NPV: equities, bonds, TIPS, timber for harvest), consumable/transformable assets (commodities, petroleum), store-of-value assets (currencies, precious metals, art). Hedge funds and volatility do not fit; they are strategies or characteristics. Asset classes carry a non-skill ex ante risk premium; "strategies/diversifying strategies" do not.
  - Typical lists: global public equity, global private equity, global fixed income (sovereign, IG, HY, EM, optional linkers and cash), real assets (real estate, infrastructure, commodities, optionally linkers). Keep granularity coarse for SAA (equity vs bonds vs others matters far more than sub-classes); refine in implementation.
- **Factor-based vs asset-class-based allocation**: factors (GDP growth, inflation, real rates, duration, credit/default risk, volatility, liquidity, value, size, momentum, currency, capital structure, convexity) are the building blocks that overlap across asset classes (the reason equity and credit correlate).
  - How: specify desired factor exposures, describe asset classes by their factor sensitivities, build investable factor portfolios (long/short: nominal Treasuries minus linkers isolates inflation; long high-quality credit minus Treasuries isolates credit spread; long 10y+ minus short 1-3y Treasuries isolates duration; VIX futures proxy volatility), then map back to asset-class weights.
  - Caveat: with the same constraints, factor-based allocation cannot enlarge the achievable set of outcomes; it is no automatic improvement, but it controls overlapping risks (e.g. equity risk dominating a "diversified" portfolio) and helps express liability-related exposures.
- **Strategic asset allocation as utility maximization**: `max E[U(W_T)]` over weights `w_i` with `Σw_i = 1` and other constraints; power utility is approximated by mean-variance utility. Single risky + risk-free asset: `w* = (μ − r_f) / (λ·σ²)` where λ = risk aversion, μ expected risky return, σ² variance (reading's wording: inversely proportional to risk aversion, proportional to expected return per unit of variance).
- **Nine-step SAA process**: (1) objectives, (2) risk tolerance and risk measures, (3) horizon(s), (4) other constraints (tax, ESG, legal, political), (5) choose approach, (6) specify asset classes and capital market expectations, (7) generate candidate allocations (optimization), (8) robustness tests (simulation, sensitivity to CMEs), (9) iterate to agreement.
- **Global market portfolio (GMP) as baseline**: market-value-weighted portfolio of all investable assets; theory (two-fund separation) says it is the efficient risky portfolio and minimises uncompensated diversifiable risk. Phase 1: weights across stocks, bonds, real assets; phase 2: regional/country/security weights.
  - How: start at GMP and justify every deviation (home bias, value, size, EM tilts). MSCI ACWI weights at end 2015: North America 55.9%, developed Europe/Middle East 22.8%, developed Pacific 11.7%, EM 9.6%.
  - Hurdles: estimating private and residential real estate sizes, investability of private assets; proxies usually use traded assets and ETFs; GDP weighting and equal weighting are active alternatives.
- **Liability glide path (for underfunded plans)**: pre-specify the share of liability-hedging vs return-seeking assets and the hedge duration as funded status improves; reduce surplus risk over time.
- **Goals-based sub-portfolios**: one sub-portfolio per goal with time horizon, cash-flow pattern and required probability of success; the sum is the SAA. Goal typologies: Brunel (personal, dynastic, philanthropic); Chhabra (personal risk bucket = downside protection, market risk bucket = maintain lifestyle, aspirational risk bucket = grow wealth).
- **Implementation dimensions**: (a) passive/active management of asset class weights: tactical asset allocation (TAA, short-term tilts), dynamic asset allocation (DAA, longer-term valuation/economic views), global TAA; (b) passive/active within each asset class along a continuum (indexing the global market portfolio → non-cap-weighted/smart-beta → diversified active → aggressive or unconstrained); measures: tracking risk and active share (not in lockstep).
- **Risk budgeting**: decide which risks and how much. Absolute budgets (e.g. 20% volatility) vs relative (tracking error to the SAA benchmark, or to an asset class benchmark); risk-budgeting allocation ignoring expected returns, e.g. risk parity / equal risk contribution; active risk budgets at SAA level (for TAA) and asset class level (alpha vs tracking error).
- **Rebalancing framework**: calendar rebalancing (simple, arbitrary); percent-range/corridor rebalancing (no-trade region, trigger when weight breaches band). Four questions: valuation frequency (monthly or quarterly typical), trigger size (fixed ±x%, proportional to target, volatility-based, or cost-benefit), full vs partial correction (to target, to range edge, or halfway between edge and target), and tools (cash flows, trades, derivatives overlay).

## Key Concepts
- **Investment governance**: organisation of decision rights and oversight to align investing with objectives, risk tolerance, constraints and law.
- **Investment policy statement (IPS)**: the foundation document: objectives, constraints, responsibilities, review frequency, rebalancing policy; asset allocation and manager guidelines sit in a more easily revised appendix.
- **Strategic asset allocation (policy portfolio)**: long-run target mix expected to meet objectives given constraints; fixes the return level of passive and aggregate investors, whatever the degree of active management.
- **Extended portfolio assets/liabilities**: items such as human capital, PV of contributions and PV of consumption absent from accounting balance sheets.
- **Human capital**: mortality-weighted NPV of future labour income; non-tradable and unhedgeable; longevity matters because individuals can outlive a portfolio but not a lifetime annuity.
- **Funded ratio / surplus**: assets divided by liabilities, or assets minus PV of liabilities; surplus optimisation applies mean-variance to the surplus.
- **Liability-hedging portfolio vs return-seeking portfolio**: the first is matched to liability interest-rate, inflation and credit sensitivities; the second is riskier relative to liabilities and seeks growth (LDI structure).
- **Mental accounting**: treating money as non-fungible by purpose; goals-based investing systematises it so riskier assets can live in long-term, aspirational buckets.
- **Longevity risk**: living beyond the median life expectancy; handle with longer planning horizon (e.g. 35 vs 20 years) or deferred (longevity) annuities.
- **Home-country bias**: overweighting the domestic market relative to global weights; implicitly a market view, sometimes justified by home-currency liabilities.
- **Tactical vs dynamic asset allocation**: TAA = short-term tilts on short-term views; DAA = deviations on longer-term valuation or economic views.
- **Active share**: share of portfolio weights differing from the benchmark; complements tracking risk.
- **Risk parity / equal risk contribution**: weights set so each asset class contributes equally to portfolio volatility.
- **Rebalancing range (corridor)**: no-trade band around target weights.
- **Decision-reversal risk**: abandoning a chosen course at the worst time; governance should pre-empt it.

## Formulas & Reference Tables
- Expected utility: `max E[U(W_T)]`, `Σw_i = 1`; power utility `U = W^(1−λ)/(1−λ)`-type with constant relative risk aversion (reading: `W_T^{1−λ}/(1−λ)`, λ > 0; λ → 0 is risk neutral). Mean-variance utility: `U = E[R] − ½λσ²`.
- One risky asset: `w* = (μ − r_f)/(λσ²)`.
- Sharpe ratio: `SR = (E[R_p] − r_f)/σ_p`.
- Economic net worth: `(financial + extended assets) − (financial + extended liabilities)`.
- Funded ratio `= A/L`; surplus `= A − PV(L)`; surplus volatility = volatility of `A − L`.
- Range rebalancing sizes (fixed vs proportional): target 60% with ±10% proportional band = ±6 points; target 5% = ±0.5 points; fixed ±5 points applied to both a 40% and a 15% target is the traditional alternative. Asymmetric taxable band example: target 25%, allowed 24%–28% (−1 / +3).

| | Asset-only | Liability-relative | Goals-based |
|---|---|---|---|
| Balance-sheet focus | Assets only; liabilities not modelled | Legal and quasi-liabilities | Goals (sub-portfolios) |
| Typical objective | Maximise Sharpe ratio for acceptable volatility | Fund liabilities, invest surplus for growth | Achieve each goal with a required probability |
| Risk concept | Volatility, tracking error, VaR, drawdown, semivariance; Monte Carlo for tails | Shortfall risk: assets insufficient vs liabilities; surplus or funded-ratio volatility; contribution volatility | Probability of failing each goal; portfolio risk = weighted sum of goal risks |
| Typical users | Some foundations/endowments, sovereign wealth funds, individuals (simplicity or undefined liabilities) | Banks, DB pensions, insurers | Individuals and families (asset segmentation by life insurers is analogous) |
| Core tool | Mean-variance optimisation, efficient frontier | Surplus optimisation, LDI, liability glide path | Sub-portfolios per goal, time-based buckets |

- Institutional liabilities versus individual goals: legal debts vs soft goals; uniform vs many and varied; forecastable by pooling (law of large numbers) vs not.
- Rebalancing strategic considerations (all else equal): higher transaction costs mean wider ranges; more risk-averse investor, tighter; less correlated asset, tighter; asset highly correlated with the rest of the portfolio, wider; momentum belief, wider; mean-reversion belief, tighter; illiquid asset, wide range; taxes, wider and asymmetric; derivatives allow synthetic rebalancing.
- Passive/active drivers: investable representative index available, scalability of active strategies, client-specific constraints (e.g. ESG) vs index products, belief in efficiency, expected benefit net of costs and risk, tax status (taxable investors face higher hurdles; hold active in tax-advantaged accounts).
- Goals-based discounting: higher required probability means a lower discount rate (more assets) for that sub-portfolio; longevity handled with longer horizon.

## Mental Models
- **Governance first**: a good allocation that the committee will abandon in a drawdown is worse than a slightly inferior one it will keep. Design for survivability and decision-reversal risk.
- **Net worth lens**: the investor's whole balance sheet is the portfolio; treat human capital as a bond-heavy (about 70%) asset and look for exposures that correlate with the employer or sponsor.
- **Three questions pick the approach**: Is there a legal liability with a penalty for failing? Use liability-relative. Are there many distinct goals with different priority? Goals-based. Neither, or simplicity matters? Asset-only.
- **Asset class = non-skill premium; strategy = skill**: only the former belongs as an asset class in the SAA; hedge funds are "diversifying strategies" or are mapped to factor exposures.
- **Start at the market portfolio and justify departures**: GMP is the default; every tilt (home bias, value, EM) is an explicit view.
- **Rebalancing is a short-volatility contrarian discipline** (selling outperformers, buying laggards): uncomfortable behaviourally, but it holds risk steady and does not reliably add return.
- **Look-through before diversification**: asset class labels hide overlapping factors (inflation, volatility, credit); test diversification against all other assets together.

## Worked Example
**Asset-only SAA choice (GPFC sovereign wealth fund, risk-free 3%, volatility cap 17%, 5% VaR tolerance −22%).**

| | Current | Mix A | Mix B | Mix C |
|---|---|---|---|---|
| Expected arithmetic return | 8.50% | 8.25% | 8.88% | 8.20% |
| Volatility | 15.57% | 14.24% | 16.63% | 14.06% |
| Sharpe (recomputed) | 0.353 | 0.369 | 0.354 | 0.370 |
| 1-yr 5% VaR | −17.11% | −15.18% | −18.48% | −14.93% |

All four meet the volatility and VaR limits. Mix B takes more risk for no Sharpe gain, so reject. Mix A and C are modest improvements; C wins on qualitative grounds: more equity-like GDP-growth/population exposure (spending grows with population and inflation), 10% inflation-linked bonds hedging the inflation-linked spending, and 25% non-domestic equity cutting home bias (Caflandia is 0.5% of world equity). Limits: Sharpe ignores VaR and funded ratio constraints; and a higher Sharpe for one asset (diversifying strategies) does not mean it should replace another, because correlations drive the portfolio effect.

**Liability-relative vs asset-only (GPLE frozen DB plan, assets $1.25bn, liabilities 1.25/1.15 = $1.087bn, buffer $0.163bn).** Recommendation A (65% equity, 35% bonds) holds $0.8125bn in equity; a 20.06% equity fall exhausts the buffer, creating contribution risk with no benefit to anyone since the buffer is already adequate. Recommendation B puts $1.125bn (90%) into a duration-matched liability-hedging bond portfolio and $0.125bn (10%) in equities: lower expected return, below the asset-only frontier, but pension liabilities are effectively defeased. Interpretation: when the penalty for missing liabilities is high and surplus is adequate, risk is shortfall risk, not volatility of assets.

**Economic balance sheet (Lee family, US$ m).** Assets 25 (portfolio) + 3 (house) + 16 (human capital) = 44; liabilities 1 + 1 + 0.25 + 0.75 + 3 + 20 = 26; economic net worth = 18. Goals total 24 (lifestyle 20, education 0.25, charity 0.75, trust 3). Human capital (16) is less than lifestyle needs (20), so the portfolio must fund the gap; most of the 18 net worth is human capital, not liquid. Implication: short-term goals (education: very high probability, short horizon) go in a cash-heavy sub-portfolio; the long-dated trust (high probability, long horizon) can hold 45% global equities and 15% diversifying strategies; an illiquid, risky venture investment belongs only in the aspirational/long sub-portfolio, funded from excess capital.

## Anti-patterns
- **Optimising on the financial portfolio alone**: ignores correlated human capital (employer stock plus salary), sponsor risk or related real estate, and so mis-sizes equity and real estate.
- **Defining asset classes that overlap or lump heterogeneous assets** (global equity plus domestic equity; real estate inside debt; both US equity and highly correlated "derivatives"): breaks diversification control and CMEs.
- **Excess granularity** (many small sub-classes with overlapping risk factors): spurious optimiser precision; decide broad classes first.
- **Reading diversification from pairwise correlations only**: an asset can be an exact blend of two others with correlation just 0.5 to each; check stress-period correlations too.
- **Choosing allocation by highest Sharpe ratio alone**: ignores absolute risk limits (VaR, funded ratio), liquidity and liability factor exposures.
- **Committee micro-managing manager selection** and neglecting asset allocation and risk: governance inversion.
- **Never rebalancing**: high-return, higher-risk assets take over, concentrating risk (60/40 mix drifted heavily to equities in the 1995-2001 bubble with much higher VaR at a similar ending value).
- **Treating factor-based allocation as free alpha**: same constraints give the same attainable set; the benefit is risk transparency.
- **Using the same band for all assets**: ignoring cost, volatility and correlation; ignoring the tax cost in taxable accounts.

## Exam Focus & Traps
- Distinguish **approach by objective and risk**: asset-only = Sharpe/volatility; liability-relative = shortfall/funded ratio/surplus volatility; goals-based = probability of failing goals. All three can use standard deviation, but of different things (portfolio, surplus, funded ratio).
- Economic net worth is a **plug** (assets minus liabilities); remember to **exclude** assets owned by a different entity (the university's real estate is not on the endowment's balance sheet but affects its risk).
- Identify **which asset-class criterion** is violated: non-homogeneous (real estate in debt), non-exclusive (global plus domestic), non-diversifying (correlated equity and foreign equity "derivatives").
- Goals-based: more important goals have a **higher required probability** and lower-risk, shorter, more liquid sub-portfolios; high-probability, long-horizon goals can still hold growth assets (trust example); aspirational goals take most risk.
- Rebalancing direction rules (cost-benefit): higher costs wider; higher correlation with the rest of the portfolio wider; risk-averse tighter; momentum belief wider; taxes wider/asymmetric.
- TAA vs DAA vs strategic: TAA is short-term and uses momentum, valuation or cycle signals; always weigh tracking error and trading costs/taxes.
- Hedge funds are not a Greer asset class and not a factor; equity volatility is a characteristic.
- ⚠ Source slip: in the reading's Example 6 solution the Sharpe ratios of Exhibit 9 are printed as "3.70, 3.69, 3.53" (scale error); the correct values are 0.370, 0.369 and 0.353 (current and Mix B differ by 0.001 only). Also in that example the quoted Sharpe ratios for diversifying strategies (0.55) and real estate (0.50) are not consistent with the footnote inputs (7.0% return, 9% volatility gives 0.44; 7.5% and 16% gives 0.28 at a 3% risk-free rate); the qualitative point (do not rank asset classes by Sharpe alone) stands.
- Human capital rule of thumb is about 30% equity-like and 70% bond-like; glide path falls out of that.
- Reading note: the formula for the one-risky-asset allocation `w* = (μ − r_f)/(λσ²)` is printed with symbols garbled in extraction; use mean-variance utility `E[R] − ½λσ²`. Check with example: λ = 3, μ = 8%, r_f = 3%, σ = 15% gives w* = 0.0500/0.0675 = 74.1%.

## Key Takeaways
1. Build governance first: six elements, clear division of rights, an IPS with rebalancing rules, a governance audit, and defences against decision-reversal and key-person risk.
2. Always draw the economic balance sheet; look for correlation between human capital or sponsor exposures and portfolio holdings; allow bond-like human capital to justify early-life equity.
3. Pick the approach by the nature of the obligation: asset-only for undefined liabilities or simplicity; liability-relative for legal liabilities (hedging portfolio plus return-seeking portfolio, glide path if underfunded); goals-based for individuals (sub-portfolios by goal, horizon and required probability).
4. Specify a small set of homogeneous, mutually exclusive, diversifying asset classes covering world investable wealth and able to absorb meaningful capital; use factors to see overlap and to match liability exposures.
5. Use the global market portfolio as the default baseline and document every deviation (home bias, tilts).
6. Rank candidate mixes by Sharpe ratio but test them against hard limits (volatility, VaR, funded status, liquidity) and by simulation and CME sensitivity.
7. Treat TAA as a cost-benefit decision (tracking error, trading costs, taxes) and place each asset class on the passive-active spectrum according to efficiency beliefs, scalability, costs, taxes and constraints.
8. Set rebalancing bands by cost, risk aversion, correlation, volatility, beliefs and taxes; use derivatives overlays where cheaper, and remember rebalancing is for risk control.

## Connects To
- **ch03**: the capital market expectations framework that supplies the inputs to every SAA step.
- **ch04**: Singer-Terhaar, Grinold-Kroner, building blocks and shrinkage covariance produce the return, volatility and correlation inputs for optimisation.
- **ch05**: cycle-phase view of real rate, inflation, credit and equity premia that informs TAA/DAA tilts.
- **ch07**: the "how": mean-variance, Black-Litterman, resampling, risk parity, liability-relative and goals-based models in detail.
- **ch08**: real-world constraints (taxes, liquidity, ESG, behavioural) layered onto this SAA process.
- **`cfa-wealth-institutional-management` ch01–ch04**: IPS construction and investor-specific constraints for individuals and institutions.
- **`cfa-portfolio-management` ch04 and ch07**: portfolio management process and planning basics reviewed at Level I.
- **`cfa-fixed-income` ch13**: LDI and liability-matching techniques used in the liability-hedging portfolio.
