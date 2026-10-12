# Chapter 6: Factor Investing: A New Concept of Asset Allocation (Theory, Factor Zoo, Smart Beta, Bond Factors)
> **Source**: CFA Society Italy × Advisor Private, *Factor Investing* guide (2018), Ch. 1 "Un nuovo concetto di asset allocation" | Elia Palesa and Giancarlo Sandrin, CFA; plus Invesco-sponsored insert on multi-factor fixed-income and multi-asset offerings (attributed where used)

## Core Idea
Asset classes are bundles of **risk factors**. A portfolio's return decomposes into exposure to macro factors (which set the level of returns), style factors (which set the dispersion) and alpha. Because factor correlations are low and, unlike asset-class correlations, do not spike in crises, allocating by factor can diversify better than allocating by asset class. The chapter gives the theory (EMH, CAPM, APT, Fama-French and extensions), catalogues the "factor zoo" and the criteria a real factor must meet, explains how smart-beta indices are built, and shows how the same logic applies to bonds.

## Learning Outcomes Covered
Not a CFA curriculum chapter; practitioner outcomes: decompose a portfolio into factors; state the market-efficiency forms and the CAPM, APT and Fama-French models; judge whether an anomaly is a real factor; compare smart-beta weighting schemes; apply factor thinking to bonds.

## Frameworks Introduced
- **Factor view of asset allocation (Ang 2014 metaphor)**
  - What: factors are to assets what nutrients are to food. `Return = macro-factor exposure + style-factor exposure + alpha`.
  - How: map each holding to macro factors (growth, real rates, inflation, volatility, liquidity, emerging markets, currency) and style factors (value, size, momentum, quality, low volatility, credit spread, duration, convexity); sum exposures across assets; adjust the total.
  - Why it works: cross-asset exposures hidden in labels become visible (US high yield is driven by the same growth factor as equities). Evidence in the guide (PIMCO study, 1994-2009): average factor cross-correlation about 2% in every regime, versus asset-class correlation of 39% overall, 30% in calm markets and 51% in turbulent markets.
- **Five tests of a genuine risk factor (Berkin and Swedroe 2016)**
  - Persistent over time; pervasive across countries; robust to alternative definitions; economically sensible (rational or behavioural); investable at reasonable cost. A factor must also be reasonably independent of other factors to diversify.
  - Warning evidence: Linnainmaa and Roberts (2016) find returns of 36 anomalies fall on average 58% after publication; McLean and Pontiff (2016, 97 strategies) agree. Harvey et al. (2015) count hundreds of factors in over 300 papers and show that the usual t-ratio above 2 threshold is too lenient after data mining.
- **Market efficiency forms and factor investing**
  - Weak (prices reflect past prices and volumes), semi-strong (all public information), strong (private information too). Under EMH, no persistent outperformance; factors challenge it through anomalies, either as compensation for risk or as behavioural mispricing.
  - Formal statement: `P(t+1) = E[P(t+1) | Omega(t)] + e(t+1)` with `E[e] = 0`.
- **CAPM → APT → multifactor models**
  - CAPM: `E[Ri] = Rf + beta_i,M x (E[RM] - Rf)`, `beta = Cov(Ri,RM)/Var(RM)`; a single factor, the market portfolio.
  - APT (Ross 1976): `Rit = a_i + sum_j b_ij x F_jt + e_it`; several systematic factors not identified a priori; idiosyncratic risk diversifiable.
  - Chen, Roll and Ross (1986) macro factors: industrial production, unexpected inflation, change in expected inflation, risk premium, term structure; what is priced is the shock, not the level.
- **Fama-French three-factor model (1993)**: `Ri - Rf = a + b_M (RM - Rf) + b_SMB SMB + b_HML HML + e`.
- **Carhart four-factor model (1997)**: adds `b_PR1YR x PR1YR` (prior 12-month winners minus losers, i.e. momentum, after Jegadeesh and Titman 1993).
- **Fama-French five-factor model (2015)**: adds RMW (robust minus weak profitability) and CMA (conservative minus aggressive investment): `Ri - Rf = a + b_M (RM-Rf) + b_SMB SMB + b_HML HML + b_RMW RMW + b_CMA CMA + e`.
  - Derivation via the dividend discount model: market value equals discounted expected dividends; dividends equal earnings minus change in book. Dividing by book gives three predictions: lower price-to-book implies higher expected return; higher profitability implies higher expected return; higher book growth (investment) implies lower expected return.
  - Criticisms: omits momentum; offers a reworking of the DDM rather than a rational risk story for the added factors.
- **Pastor-Stambaugh liquidity model**: `Ri - Rf = a + b_M(RM-Rf) + b_SMB SMB + b_HML HML + b_WML WML + b_LIQ LIQ + e` (adds winners-minus-losers and liquidity).
- **Smart-beta index construction (three design choices)**
  - Universe selection (a stock-picking step with possible factor tilt), rebalancing frequency (cost vs unintended exposure drift), weighting scheme.
  - Weighting menu: equal weight (maximum deconcentration; no estimation risk); Equal Risk Contribution (risk parity); Diversified Risk Weighted; Maximum Decorrelation; Efficient Minimum Volatility; Efficient Maximum Sharpe Ratio. Trade-off: parameter-estimation risk vs optimality risk (the more optimisation inputs, the larger the estimation error; maximum Sharpe needs expected returns and is the most fragile).
- **Factor diversification**: diversify across factors with different cycles; value and momentum are naturally offsetting since a price rise lowers cheapness but raises momentum.
- **Bond factor decomposition**
  - Rates (duration) explain 60-80% of price variation of investment-grade bonds (Litterman-Scheinkman 1991); credit spread plus duration explain over 90% of return differences across bonds. Add slope, curvature, credit spread, liquidity, volatility, growth.
  - Style factors for bonds: value (yield to maturity, OAS, Z-spread), size (issue amount), momentum (price changes), low volatility (return or OAS volatility, duration times spread), quality (leverage, debt service, free cash flow, rating, default probability).
  - Value in bonds example: fallen angels (downgraded from investment grade to high yield) are forced-sold by constrained holders and can be cheap.

## Key Concepts
- **Factor**: a systematic source of return and risk shared by many securities.
- **Macro factors**: economic growth, real rates, inflation, volatility, liquidity, emerging-market risk, currency; they set the level of returns.
- **Style factors**: value, size, momentum, quality, low volatility, credit spread, convexity, duration; they set dispersion.
- **Smart beta**: index with systematic, rules-based weighting aimed at factor exposure; between passive and active.
- **Factor zoo** (Cochrane 2011): the proliferation of reported factors, many of them spurious.
- **Data mining**: finding patterns that exist only in the sample; Black (1993) argued the size effect could be one.
- **Size effect**: small caps outperform large (Banz, Reinganum 1981); linked to distress risk and illiquidity; the premium fades once discovered (Schwert 2002).
- **Value effect**: high book-to-market or earnings-to-price stocks outperform (Basu 1977; Fama-French 1993); risk story (distress) vs behavioural story (extrapolating past growth, Lakonishok-Shleifer-Vishny 1994).
- **Momentum**: winners continue to win over 12 months; explanations: herding, return chasing, disposition effect.
- **Profitability / Investment**: RMW and CMA; Novy-Marx (2013) used gross profits over assets.
- **Quality**: Piotroski (2000) found separating strong from weak fundamentals lifts a value strategy's annual return by 7.5%; Asness-Frazzini-Pedersen define quality as safe, profitable, growing and well managed (QMJ factor).
- **Low volatility / low beta**: Haugen-Baker (1991) minimum variance beats market on a risk-adjusted basis; Frazzini-Pedersen (2014) betting against beta; Ang et al. find high idiosyncratic volatility earns low returns, while Bali-Cakici (2008) find the result unstable.
- **Liquidity premium**: Amihud-Mendelson (1986): returns rise as liquidity falls; the guide's table (Financial Analysts Journal 2013) shows small-cap annual averages of 17.07% in the least liquid quartile versus 9.89% in the most liquid.
- **Volatility has a negative risk price**: to harvest the premium you must sell volatility, a position that pays in calm markets and loses in crises.
- **Concentration risk of cap-weighted indices**: top 10 S&P 500 names are about 19% of the index, the same weight as the bottom 308.

## Formulas & Reference Tables
- `E[Ri] = Rf + beta_i,M x (E[RM] - Rf)`; `beta = Cov(Ri, RM) / Var(RM)`.
- `Ri - Rf = a + b_M (RM - Rf) + b_SMB SMB + b_HML HML (+ b_PR1YR PR1YR) (+ b_RMW RMW + b_CMA CMA)`.
- Weighting schemes (symbols: w = weights, Sigma = covariance matrix, Omega = correlation matrix, mu = expected returns, sigma_i = volatility):
  - Equal weight: `w_i = 1/N`.
  - Equal Risk Contribution: choose `w` so that `w_i (Sigma w)_i` is the same for every i.
  - Diversified Risk Weighted (assumes identical correlations): `w_i = (1/sigma_i) / sum_j (1/sigma_j)`.
  - Maximum Decorrelation (assumes identical volatilities): minimise `w' Omega w`.
  - Efficient Minimum Volatility: minimise `w' Sigma w`.
  - Efficient Maximum Sharpe: maximise `(w' mu - Rf) / sqrt(w' Sigma w)`.
- Selected factor premia from the Kenneth French database (annual, %): value, North America: 2016 +21, 2015 -9; momentum Global: 2009 -57, 2013 +21; market Global 2008 -42, 2009 +32; size Global 2008 -1 to 2016 +4. Premia change sign across years and regions.
- Market share data: smart beta reached about 12% of US ETF assets in 13 years; end 2016 over 6,000 ETFs/ETPs with about USD 3.5tn, over 1,000 smart-beta indices from 145 providers in 32 countries; ETFGI reports USD 644bn in smart-beta products in September 2017; a FTSE Russell 2016 survey found three quarters of investors using or planning smart beta.
- Bond data (ICE BofA Global Corporate by rating, Jan 2000-Dec 2017): annual return / volatility / Sharpe (risk-free taken as 0): AA 1.76% / 5.93% / 0.30; A 2.15% / 5.91% / 0.36; BBB 4.30% / 5.58% / 0.77; BB 6.40% / 6.46% / 0.99; B 4.33% / 8.26% / 0.52; CCC 6.87% / 11.72% / 0.59; Global Government 1.58% / 4.50%. **⚠ Correction**: the source prints 0.031 for AA; 1.76/5.93 = 0.297.
- Average cumulative credit loss by rating (Moody's 1983-2016, mean / max): Aa 0.0/0.3%; A 0.0/0.3%; Baa 0.1/0.7%; Ba 0.6/2.4%; B 2.5/8.5%; Caa-C 8.3/27.2%.
- Variance explained by real rates (bond indices): about 70% or more for government and aggregate indices, under 6% for US high yield, EM hard currency (4.3%) and EM local currency (0.3%); growth and volatility explain far more for high yield and EM than for Treasuries.

## Mental Models
- **Use factors, not labels, when asset-class correlations jump in crises**: factor correlations stay near 2% while asset-class correlations rise to 51%.
- **Use the five-test checklist before adding a factor**: persistent, pervasive, robust, sensible, investable.
- **Use equal weight when you distrust inputs; use optimisation only when you trust the estimates**: more inputs, more estimation risk.
- **Use factor diversification across cycles**: value with momentum, quality with low volatility.
- **Use credit spread and duration separately in bonds**: a high-yield bond with shorter duration is not less risky if default risk rises; hedge duration to isolate credit.

## Worked Example
Fama-French three-factor expected excess return (illustrative inputs).
- Inputs: b_M = 1.1, market premium 5.0%, b_SMB = 0.3 with SMB premium 2.0%, b_HML = 0.5 with HML premium 4.0%.
- Steps: 1.1 x 5.0 = 5.5; 0.3 x 2.0 = 0.6; 0.5 x 4.0 = 2.0; sum = 8.1% over Rf.
- Result: required excess return 8.1% against 5.5% under CAPM.
- Interpretation: tilts to small and value stocks raise the hurdle; only returns above 8.1% over cash count as alpha.

Diversified Risk Weighted (illustrative).
- Inputs: three stocks with volatilities 10%, 20%, 20%.
- Steps: 1/sigma = 10, 5, 5; sum = 20; weights = 50%, 25%, 25%.
- Result: the low-volatility stock gets double weight, equalising stand-alone risk when correlations are equal.
- Interpretation: the same inputs under equal weighting give 33% each, a 20% vs 25% volatility split; ERC would adjust for actual correlations.

## Anti-patterns
- Treating labels (equity, high yield) as diversifying when they share the growth factor.
- Adding every published factor ("factor zoo") without an economic rationale.
- Assuming premia are constant: factor returns vary by year, region and cycle (e.g. momentum -57% globally in 2009).
- Relying on a t-ratio above 2 after extensive data mining.
- Using maximum-Sharpe optimisation with noisy expected returns.
- Reducing high-yield or EM risk simply by shortening duration.
- Rebalancing a smart-beta index too rarely (drift into unwanted factors) or too often (cost).

## Practitioner Notes
- Asset allocation still matters: the guide cites Ibbotson-Kaplan (2000) that policy benchmark explains about 90% of return variability over time; factor thinking refines, not replaces, it.
- Factor investing sits between active and passive: factor rules formalised into indices let investors buy active managers' traditional sources of return at lower cost.
- Fixed-income factor products are scarcer than equity ones; the Invesco 2017 study cites only about one third of respondents able to implement their preferred factor strategies, and one third using factors in bonds; barriers are limited research, short track records, and concerns over derivatives and leverage in multi-asset products.
- Larger institutions (sovereign funds, pensions) often use risk parity on macro factors (inflation, rates, equity) to free risk budget for uncorrelated alpha.
- Alternative bond indexation by GDP rather than issuance is not a factor approach: high GDP does not imply low debt-to-GDP (Japan).

## Key Takeaways
1. Return = macro-factor exposure + style-factor exposure + alpha; macro sets the level, style the dispersion.
2. Factor correlations (about 2%) are far lower than asset-class correlations (39% overall, 51% in turbulent markets).
3. A factor needs persistence, pervasiveness, robustness, economic sense and investability; many published anomalies shrink by about 58% after publication.
4. CAPM is a one-factor special case of APT; Fama-French adds size and value, Carhart momentum, Fama-French 2015 profitability and investment.
5. Size and value are time-varying; value has both risk and behavioural explanations; quality (Piotroski, QMJ) improves value strategies.
6. Smart-beta design = universe, rebalancing, weighting; the more optimisation inputs, the more estimation risk.
7. In bonds, duration and credit spread dominate; high yield and EM behave like equities (growth, volatility).
8. Volatility carries a negative price of risk; low-volatility and low-beta strategies exploit investor preference for high-risk stocks.

## Connects To
- **ch07**: how each factor behaves over the economic cycle.
- **ch08**: active vs passive factor implementation and manager evaluation.
- **ch03**: value premium and HML in the value-investing guide.
- **ch05**: multifactor construction used by active managers.
- **`cfa-equity-portfolio-management`**: factor models and smart beta in the CFA treatment.
- **`cfa-asset-allocation-cme`**: strategic allocation and risk-factor approaches.
- **`cfa-fixed-income`**: duration, curve and credit-spread decomposition.
