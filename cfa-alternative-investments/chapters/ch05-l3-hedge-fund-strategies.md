# Chapter 5: Hedge Fund Strategies
> **Source**: CFA Program Curriculum 2023, Level III, Reading 19 · Portfolio Management (Alternative Investments) | Barclay T. Leib, Kathryn M. Kaminski, Mila Getmansky Sherman

## Core Idea
Hedge funds are not one asset class but six strategy families (equity, event-driven, relative value, opportunistic, specialist, multi-manager), each with a distinct payoff shape, leverage level and crisis behaviour. The decision that matters to an allocator is whether a strategy adds alpha and true diversification net of fees, and whether its hidden factor exposures (equity, credit, USD, volatility) switch on in a crisis. A conditional factor model with a crisis dummy is the tool that exposes those hidden exposures.

## Learning Outcomes Covered
- classify hedge fund strategies (instruments, trading philosophy, risk type; six categories)
- describe characteristics, implementation and portfolio role of equity-related, event-driven, relative value, opportunistic, specialist and multi-manager strategies
- describe how conditional factor models reveal hedge fund risk exposures
- evaluate the impact of a 20% hedge fund strategy allocation on a 60/40 portfolio

## Frameworks Introduced
- **Six-category strategy taxonomy**: equity (L/S equity, dedicated short/short-bias, equity market neutral); event-driven (merger arbitrage, distressed); relative value (fixed-income arbitrage, convertible arbitrage); opportunistic (global macro, managed futures); specialist (volatility, reinsurance/life settlements); multi-manager (multi-strategy, fund-of-funds).
  - When to use: map any manager to its dominant risk (equity beta, event risk, credit/liquidity/leverage, trendiness, niche skill, manager-of-managers).
  - How: classify by (1) instruments, (2) trading philosophy (systematic vs discretionary), (3) risk assumed (directional, event, relative value). Vendors (HFR 6 groups; Lipper TASS 10; Morningstar CISDM; Eurekahedge 9; Credit Suisse 9) differ; fewer than 1% of managers report to all of them, so no single index is complete.
- **Conditional linear factor risk model**: `R_i,t = α_i + Σ_k β_i,k·F_k,t + D_t·Σ_k β_i,k^crisis·F_k,t + ε_i,t`
  - When to use: due diligence on a manager or strategy to find exposures that are insignificant in calm markets but appear in stress.
  - How: (1) list candidate factors (SNP500 equity, BOND, USD, CMDTY, CREDIT = Baa-Aaa yield spread, VIX first difference); (2) compute pairwise correlations in each state and flag pairs above 60%; (3) for each flagged pair, regress returns excluding A, then excluding B, keep the factor giving the higher adjusted R²; (4) repeat. BOND and CMDTY were dropped, leaving SNP500, CREDIT, USD, VIX. Crisis dummy D_t = 1 for June 2007-Feb 2009. Total crisis exposure = β + β^crisis.
  - Why it works / failure mode: separates beta from alpha and captures regime shifts; residual = alpha + omitted factors + noise, so "alpha" is only as good as the factor set. Averages hide fund-level heterogeneity, so also count the share of funds with significant loadings (10% level).
- **Strategy-as-option-payoff lens**: merger arbitrage = riskless bond + short binary put; fixed-income arbitrage (on/off-the-run) = short put; long volatility = convex, long put-like; convertible arbitrage = long gamma / long vega with short stock delta hedge.
  - When to use: to anticipate left-tail behaviour and why leverage plus a short-put payoff blows up in a crisis.

## Key Concepts
- **Liquid alts**: mutual fund/UCITS/ETF wrappers of hedge-like strategies; daily liquidity, lower fees, generally no incentive fee; private hedge funds beat them by roughly 100-200 bps a year (illiquidity premium).
- **Single-manager vs multi-manager**: single-manager runs one strategy; multi-manager = multi-strategy fund (teams under one roof) or fund-of-funds (allocates to external funds).
- **Dedicated short seller vs short-biased**: short only (60%-120% short) versus 30%-60% net short with some long exposure; low leverage, negative correlation to equities.
- **Short squeeze / "losing the borrow"**: lender recalls shares or borrow cost spikes, forcing a buy-back at a bad moment; high short interest and "special" borrow rates (e.g. 20%) are warning signs.
- **Equity market neutral (EMN)**: long/short with beta ≈ 0 and often sector/size/value neutrality; leverage compensates for modest edge; includes pairs, stub and multi-class trading, statistical arbitrage.
- **Stub trading**: buy/sell a parent against its subsidiaries weighted by ownership (short 1 share of parent A, buy 0.90 of B and 0.75 of C if A owns 90% and 75%).
- **Hard vs soft catalyst**: event already announced (less risky) vs anticipated event (riskier).
- **Fulcrum security**: partially in-the-money claim that will own the reorganized company; the target of control-oriented distressed investors.
- **Capital structure arbitrage**: long the cheap security (e.g. junior debt) versus short another security of the same issuer (equity).
- **Duration-neutral**: immunizes small parallel curve moves only; large or non-parallel moves need futures, swaps, swaptions.
- **Haircut**: prime broker's collateral cushion in repo financing; sets leverage available.
- **Conversion ratio / conversion price / conversion value**: shares per bond; bond price ÷ ratio; stock price × ratio.
- **Time-series momentum (TSM) vs cross-sectional momentum (CSM)**: TSM goes long assets with positive own trailing return, short negative (can be net long/short); CSM goes long the best, short the worst within a group (near net zero).
- **Variance / volatility swap**: forward on realized variance / volatility, zero value at inception at the fair strike; pure vol exposure without delta hedging.
- **Netting risk**: FoF investor pays incentive fees to winning funds while losing funds drag returns.
- **Rho (ρ₁)**: first-order serial autocorrelation of returns; high rho signals smoothed, illiquid, mark-to-model pricing.
- **Sortino ratio**: (R − threshold) / downside deviation; preferred for negatively skewed strategies.

## Formulas & Reference Tables
- Conditional model: `R_i,t = α_i + Σ_k β_i,k F_k,t + D_t Σ_k β_i,k F_k,t + ε_i,t`; crisis total β = β_normal + β_crisis.
- Beta-weighted pair hedge: `Short $ = Long $ ÷ (β_short ÷ β_long)` (equal beta-weighted dollars).
- Convertible: `Conversion value = Stock price × Conversion ratio`; `Conversion price = Bond price ÷ Conversion ratio`. Delta-neutral short shares = `delta × conversion ratio` per bond.
- FoF net return (annual, fees at year end): `Fund net = G − mgmt − incentive × (G − mgmt)`; `FoF net = avg(fund nets) − m_FoF − i_FoF × (avg(fund nets) − m_FoF)`.
- Sortino: `(R_p − MAR) / downside deviation`.

| Strategy | Typical leverage | Return/risk shape | Liquidity | Vehicle | Crisis behaviour |
|---|---|---|---|---|---|
| L/S equity | variable (quant higher) | 40%-60% net long; return ≈ long-only at ~50% of its SD | liquid; LP or mutual fund | LP or liquid alt | positive equity beta stays in crisis |
| Dedicated short / short-bias | low | lumpy, disappointing; negative correlation | liquid | LP | gains in sell-offs |
| Equity market neutral | high (up to 300% L vs 300% S) | modest, steady, mean reversion | liquid | LP (exceeds mutual fund leverage limits) | tail risk from forced deleveraging |
| Merger arbitrage | 3-5x | spread 3%-7%; net 7%-12% annualized; left-tail -20% to -40% | liquid | LP | deals fail in stress |
| Distressed | 1.2-1.7x NAV | higher end of event-driven, lumpy, long-biased | illiquid, lock-ups, gates | LP | cyclical; best early in recovery |
| Fixed-income arbitrage | 4-5x (12-15x in multi-strat) | small spreads, short-put payoff | varies, falls with complexity | LP | margin calls (LTCM 1998) |
| Convertible arbitrage | 300% long vs 200% short | cheap implied vol harvest | thin issues, borrow cost | LP | poor in credit stress and illiquidity |
| Global macro | 6-7x notional via 15%-25% margin | lumpy, volatile, anticipatory | highly liquid | LP | positive skew in stress, heterogeneous |
| Managed futures | notional up to 6-7x; 85%-90% in T-bills | trend following, positive skew | highly liquid | LP or liquid alt | strong in prolonged crises (2007-09) |
| Volatility | convex, small premium | long vol convex; short vol steady then blow-up | VIX liquid; OTC less | LP | long vol hedges tail |
| Multi-strategy | high | steady, higher return than FoF, higher variance | gates common | LP | blow-ups (Amaranth, Ritchie) |
| Fund-of-funds | modest | diversified, double fees | lock-up 1y, monthly/quarterly | LP | no crisis hedge from diversification alone |

- Fees: hedge funds historically 1%-2% management, 10%-20% incentive. FoF historically adds 1% and 10%; now often 50 bps and 5%.
- Empirical 2000-2016 (TASS/CISDM): L/S equity beta to S&P 500 roughly 0.24-0.58 (Europe 0.24; US and US small cap 0.58); EMN beta about 0.09-0.11; dedicated short -0.28 to -0.46; FoF 0.12-0.33; macro/systematic FoF about 0.
- 48/32/20 portfolio (20% to a strategy, 60/40 base: mean 6.96%, SD 8.66%, Sharpe 0.62, Sortino 1.13, max drawdown 14.42%): systematic futures best Sharpe 0.83 and lowest SD 6.94%; fixed-income arbitrage 7.50% mean, drawdown 12.68%; EMN, global macro, merger arbitrage have the smallest drawdowns (about 5%-11%); L/S equity, distressed, convertible arbitrage have the largest (convertible arbitrage 28%-32%).

## Mental Models
- **Insurance seller**: merger arb, on/off-the-run spreads and short vol collect a steady premium and pay out on the tail. Ask what the strategy looks like on the day the insured event happens, and how much leverage sits on top.
- **Beta you can buy cheaply**: do not pay 1-and-20 for embedded equity beta. Long-biased L/S, event-driven and distressed carry beta; prefer specialist L/S, EMN, macro and managed futures for pure alpha and diversification.
- **Trend vs mean reversion**: opportunistic (macro, CTA) need trends and volatility; relative value and EMN need mean reversion and stable liquidity. Holding both hedges the regime.
- **Diversifier vs return enhancer**: classify each strategy before sizing it. Systematic futures, macro, EMN diversify; L/S equity, distressed, convertible arb mostly enhance return and carry beta or credit tail risk.
- **Average hides the tail**: the average loading of a category masks the share of funds with extreme exposure. Check the cross-section, not only the mean.
- **Illiquidity smooths**: high rho means reported volatility is understated; adjust risk before comparing Sharpe ratios.

## Worked Example
**EMN pair (PEP vs KO).** Allocate $1m to the trade, long KO (β 0.55), short PEP (β 0.65). Beta-neutral short = 1,000,000 ÷ (0.65/0.55) = $846,154. Market moves cancel; profit only if the PEP/KO relative valuation reverts. Weights in the index are irrelevant.

**Stock-for-stock merger arbitrage.** Offer: 1 A share for 2 T shares. After announcement A = $42, T = $19 (pre-deal A $45, T $15). Buy 20,000 T = $380,000; short 10,000 A = $420,000. Success: spread locked = $40,000. Failure: prices revert, A buyback costs $450,000 (loss $30,000 on the short), T falls to $300,000 (loss $80,000 on the long): total loss $110,000. Payoff is a $40,000 riskless bond plus a short binary put paying $110,000 on failure. Risk/reward 2.75:1 against, so deal probability must exceed 110/150 = 73% to break even.

**FoF fee netting.** FoF charges 1% / 10%, funds charge 2% / 20%, two funds equally weighted. Both gross 20%: each net 20 − 2 − 3.6 = 14.4%; FoF net = 14.4 − 1 − 1.34 = 12.06%; fees take 39.7% of gross. One fund +20%, other −5%: nets 14.4% and −7.0%; average 3.7%; FoF net = 3.7 − 1 − 0.27 = 2.43%; fees consume 67.6% of the 7.5% blended gross. That gap is netting risk.

**Convertible arbitrage.** Bond 120% of par (€1,200), conversion ratio 50, conversion price = 1,200/50 = €24 vs stock €30. Stock is rich vs convertible: buy the bond, short stock. Lock-in €6 per share at stock €24, €30 or €36 (convert and deliver). Add €2 borrow + €1 dividend = €3 cost, offset by coupon €50/50 = €1: profit falls to €4 per share.

## Anti-patterns
- **Paying hedge fund fees for beta**: long-biased L/S, event-driven and distressed funds embed equity beta available cheaply elsewhere.
- **Reading "market neutral" as "risk-free"**: beta-neutral EMN and arbitrage books are levered; margin calls and forced downsizing, not market direction, drive losses.
- **Judging a strategy by calm-period factor loadings**: credit and volatility exposure appear only in crisis; use the conditional model.
- **Assuming FoF or multi-manager diversification protects in a crisis**: 2007-09 exposure tests showed no hedging benefit, only more fee layers (FoF) or higher leverage (multi-strategy).
- **Using HFRX as a replicable benchmark**: it includes closed funds (superior managers) so it overstates what an investor could earn; HFRI shows funds open to investment. Also beware survivorship bias (80%+ of database funds are defunct).
- **Chasing a short on a crowded name**: very high short interest and special borrow cost invite a squeeze; use puts, put calendars or risk reversals instead.
- **Ignoring operational and liquidity mismatch**: monthly-liquidity FoF holding gated, locked-up funds needs staggered positions and a credit line.

## Exam Focus & Traps
- Merger arbitrage in a stock deal: buy target, **short acquirer** in the offer ratio; in a cash deal, buy target only. Failure reverses the initial price move; failure is the short put.
- Distressed absolute priority: senior secured, junior secured, unsecured, convertible, preferred, common. In reorganization existing equity is cancelled; fulcrum securities become the new equity.
- Fixed-income arbitrage: duration-neutral hedges only small parallel shifts; main risk in on/off-the-run trade is liquidity, not rate or credit.
- Global macro vs managed futures: macro is discretionary, top-down, anticipatory, heterogeneous; managed futures is systematic, trend-following, positive skew, with crowding and slippage. Both highly liquid, high embedded leverage.
- TSM can be net long or net short; CSM is roughly market neutral, so it has lower volatility.
- Convertible arbitrage: long convertible = long call + bond; delta-hedge with short stock; short stock gamma is zero so long gamma earns when realized vol exceeds implied vol net of costs. Best with high issuance, moderate vol, ample liquidity.
- Liquid alts: no incentive fee, daily liquidity, underperform private funds by 100-200 bps.
- FoF vs multi-strategy: multi-strategy has faster allocation, transparency, GP absorbs netting risk, but higher leverage and operational concentration; FoF has double fees and slower reaction.
- Conditional model reading: crisis total exposure = normal + incremental; use t-statistics (1.96 at 5%, 1.67 at 10%); a negative VIX loading means short volatility.
- Sortino beats Sharpe for negatively skewed strategies; high rho flags smoothing.
- Short-seller rules: US uptick-type rule applies after a 10% decline; bans on shorting can appear in crises.

## Key Takeaways
1. Classify by dominant risk, then by payoff shape; most arbitrage-type strategies are levered short-put payoffs.
2. Fees make embedded beta the most expensive beta; insist on idiosyncratic alpha (stock selection first, timing second).
3. EMN, global macro, managed futures and merger arbitrage gave the best drawdown and Sharpe improvement when added at 20% to a 60/40 portfolio; L/S equity, distressed and convertible arbitrage raised drawdown.
4. Run a conditional factor model; scan for crisis-state equity, credit, USD and volatility loadings, and check the fraction of funds with significant loadings.
5. Strategy diversification alone did not shield FoFs and multi-strategy funds in 2007-09; leverage, liquidity and credit are the true crisis drivers.
6. Choose FoF for access, small tickets and due diligence help; choose multi-strategy for speed and fee netting borne by the GP; weigh leverage and operational concentration.
7. Check smoothing (rho), survivorship, index choice and vehicle (LP vs liquid alt) before trusting reported statistics.
8. Size positions so that margin-call and gating scenarios are survivable, especially for fixed-income arbitrage, convertibles and multi-strategy funds.

## Connects To
- **ch06**: how to size and combine hedge funds with other alternatives in an asset allocation.
- **ch01**: introduction to alternatives, fees and structures (LP, lock-ups, 2 and 20).
- **ch04**: commodities and futures markets used by managed futures and macro.
- **`pairs-trading-partial-cointegration`**: quantitative basis for EMN pairs and relative value mean reversion.
- **`cfa-derivatives` ch05**: option strategies for volatility trading and short-bias implementation.
- **`cfa-fixed-income` ch15**: credit strategies behind fixed-income and distressed arbitrage.
- **`cfa-asset-allocation-cme` ch06**: policy placement of hedge funds in the portfolio.
