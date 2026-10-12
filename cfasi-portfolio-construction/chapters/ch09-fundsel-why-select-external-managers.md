# Chapter 9: Why Select External Investment Managers? (Quali sono le ragioni per le quali si seleziona un investment manager esterno?)
> **Source**: CFA Society Italy x Advisor Private, "ETF & Fund Selection" guide (Advisor Private no. 16, 2019), Chapter 1 | Nicola Tommasini, CFA

## Core Idea
After setting the strategic asset allocation (SAA), an investor decides which asset classes to run in-house, which to implement with passive vehicles and which to delegate to external managers (active or passive). Delegation is justified by two things: (1) diversification, because adding weakly correlated asset classes or strategies improves the portfolio Sharpe ratio, and many of them are reachable only through specialist managers; (2) alpha, because investors still want security selection and skilled managers, especially when low yields compress the returns of every major asset class. The case for outsourcing must also be weighed against cost and transparency risks.

## Frameworks Introduced
- **Investment process funnel**: (1) objectives, risk profile, constraints; (2) SAA: top-down view, expected return, volatility and correlation per asset class; (3) implementation: choose between self-selected securities, passive vehicles, or external active managers; (4) monitor. SAA drives most long-run return, but implementation (security selection) still decides consistency.
- **Add-an-asset-class test**: a new asset class improves the portfolio if `SR_new > rho x SR_p`, where `SR_new` = expected Sharpe ratio of the candidate, `SR_p` = Sharpe ratio of the existing portfolio, `rho` = correlation between candidate and portfolio. How: (1) estimate the three inputs; (2) compare; (3) if satisfied, allocate. Why it works: the diversification benefit rises as correlation falls, so a low-correlation asset with even a modest Sharpe ratio helps; at `rho = 0` any positive Sharpe helps. Failure mode: unreliable estimates, or correlation rising in crises. (Formula restated from the source, whose equation image was lost; verified numerically.)
- **Which manager types serve which allocation goal**:
  - Passive funds/ETFs: low-cost access to more asset classes, geographies (low-correlation countries), and recently factors and themes; flexible for tactical allocation.
  - Active directional funds: niches where passive options are thin or absent: frontier-market bonds, asset-backed securities, hybrid and subordinated bonds, convertibles, catastrophe bonds, Chinese bonds; ESG-specialists; multi-asset funds (delegates both tactical and strategic allocation plus selection, so requires very high trust and due diligence).
  - Liquid alternatives (UCITS alternatives, daily/weekly liquidity): aim for manager alpha plus low correlation with traditional assets. Focus on strategies with truly low correlation across market phases: market neutral, merger arbitrage, CTA, macro; for long-short equity check the return profile is actually uncorrelated with equity. No benchmark and broad mandates make structured selection decisive.
  - Alternatives (hedge funds, private equity, venture capital, real estate): require specialist skill, are not replicable by passive vehicles, suit long-horizon investors with stable base (pension funds, foundations) who can earn an illiquidity premium. Reasons: diversification; and, with negative real rates, higher expected return to reach targets (private equity, private real estate, venture capital, long-biased hedge funds). Strategies limited to few hedge-fund managers: tail-risk protection (put-like volatility reduction without option costs) and data-intensive quantitative strategies (AI, machine learning) that need heavy data investment.
- **Alpha-seeking rationale**: even where dispersion of excess returns among active managers has narrowed (e.g. US equities), alpha is a larger share of total return when all beta returns are compressed, so investors stay focused on finding managers who beat benchmarks consistently. Evaluate managers on risk-adjusted excess return over traditional beta, then check style bias and factor-index returns, since part of "alpha" is factor exposure that can be bought cheaply.
- **Regime-driven reasons** (post-2008): central banks held nominal rates low with positive inflation, so risk-free real returns are persistently negative; plain "self-managed vanilla securities" portfolios are rare; investors raise risky assets and use external managers (passive and active) while still capping total cost. Some adopt core-satellite: low-cost passive core plus "high-conviction" active satellites.
- **Qualitative benefit**: long-term relationships with external managers give idea exchange and access to research, improving the in-house team's reading of the market and allocation decisions.
- **Costs and risks of delegation**: excessive fees that prevent adequate net performance; insufficient transparency. Mitigation: thorough pre-selection and a disciplined due diligence and selection process (see ch11-ch14).

## Key Concepts
- **SAA**: long-run weights set by objectives, return/risk expectations, correlations.
- **Securities selection**: choice of instruments within each class.
- **External manager / third-party fund**: asset manager hired to run a mandate.
- **Liquid alternatives**: UCITS-compliant alternative strategies with daily/weekly liquidity.
- **Multi-asset fund**: fund where the manager decides tactical and strategic allocation.
- **Illiquidity premium**: extra return for locking capital.
- **Tail-risk protection**: strategies that pay off in sell-offs and high-volatility regimes.
- **CTA / macro / market neutral / merger arbitrage**: low-correlation liquid alternative strategies.
- **Core-satellite**: passive core plus active satellites.
- **Style bias**: persistent tilt (e.g. value, small cap) of a manager.
- **Negative real rates**: nominal yield below inflation.

## Formulas & Reference Tables
- `Add asset class if: SR_new > rho(new, portfolio) x SR_portfolio`.
- Example thresholds with `SR_p = 0.50`:

| Correlation rho | Minimum SR of new asset to improve portfolio |
|---|---|
| 0.0 | above 0 |
| 0.4 | above 0.20 |
| 0.8 | above 0.40 |
| 1.0 | above 0.50 (equal to portfolio) |

- Mapping of vehicle to goal:

| Goal | Typical vehicle | Selection effort |
|---|---|---|
| Beta, new geography/factor | Passive/ETF | low (ch12) |
| Niche directional exposure | Active directional | high (ch11, ch14) |
| Uncorrelated alpha | Liquid alternatives / hedge funds | very high |
| Illiquidity premium | Private markets | very high, long horizon |

## Mental Models
- Use the SR-vs-correlation test before hiring a manager for diversification: does the fund add something the portfolio does not already have?
- Use passive for any class where a cheap index vehicle exists; reserve manager selection for niches and strategies passive cannot reach.
- Use multi-asset managers only when you accept delegating allocation as well as selection.
- Use liquid alternatives to diversify only if the observed correlation is low in several market phases.
- Use core-satellite to cap total cost while keeping a budget for conviction managers.

## Worked Example
Add-an-asset test. Inputs: existing portfolio expected Sharpe 0.50; candidate liquid-alternative fund expected Sharpe 0.25, correlation to portfolio 0.40; alternative B has Sharpe 0.20 and correlation 0.40. Steps: threshold = 0.40 x 0.50 = 0.20; fund A: 0.25 > 0.20 so adding improves the portfolio (numerically, the best mix Sharpe rises from 0.500 to about 0.503 with a modest weight); fund B: 0.20 = threshold, no improvement. Interpretation: a small edge only; the gain is small unless correlation is lower, so confirm correlation in drawdown periods and cost net of fees before hiring.

## Anti-patterns
- Hiring managers only for the story, without checking incremental diversification.
- Treating multi-asset funds as plain diversification while ignoring the delegation of allocation.
- Buying liquid alternatives that behave like equity beta.
- Paying active fees for factor exposure available in cheap factor ETFs.
- Letting total fee layers (fund-of-fund plus manager plus platform) consume the diversification benefit.

## Practitioner Notes
- Define in the IPS why each external mandate exists: diversification, alpha, access, or capacity.
- Alternatives belong with investors who can bear lock-ups; short-horizon clients get liquid versions.
- Long relationships with managers pay off in research access; formalize the exchange.
- Revisit the case each year: what the manager was hired for vs what they deliver.

## Key Takeaways
- Delegate because of diversification (access to uncorrelated sources) or alpha, not by default.
- A new asset class helps if its Sharpe exceeds correlation times the portfolio's Sharpe.
- Passive tools open geography, factor and theme exposures cheaply; active managers still dominate niches.
- Liquid and private alternatives require specialist selection, long horizons and attention to correlation.
- Negative real rates push investors to riskier allocations and more managers, while cost discipline remains.
- Costs and transparency are the main risks of external management and call for formal due diligence.

## Connects To
- **ch10**: how to combine active and passive and the cost math (FAR).
- **ch11**: common selection framework (qualitative/quantitative).
- **ch12**: selecting a passive manager.
- **ch13**: building a multimanager portfolio.
- **ch14**: active selection framework (Pramerica).
- **ch01-ch04**: asset allocation context (SAA, IPS).
- **ch15-ch19**: alternatives guide.
- **`cfa-wealth-institutional-management`**: manager selection in institutional context.
