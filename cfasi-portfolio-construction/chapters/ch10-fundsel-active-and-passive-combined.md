# Chapter 10: Active or Passive? Why Not Both (Gestione attiva o gestione passiva. Perche non utilizzare entrambe?)
> **Source**: CFA Society Italy x Advisor Private, "ETF & Fund Selection" guide (Advisor Private no. 16, 2019), Chapter 2 | Davide Montaldo and Federico Reggianini, CFA; the closing insert on Research Enhanced Indexing is sponsored by J.P. Morgan Asset Management (Piera Elisa Grassi) and is attributed below

## Core Idea
No universal verdict exists on active vs passive; the authors argue they coexist: passive where alpha is hard to extract (efficient, liquid markets), active where markets are inefficient, illiquid, or index-granular. The decision rests on portfolio objectives, horizon, asset class and cost, not on cost alone. Because Sharpe's arithmetic makes the average active manager lose by costs, the test for any active fund is whether its expected alpha, at a fair price, justifies its fee for active risk, and how much manager diversification the portfolio can absorb before paying for risk that cancels out.

## Frameworks Introduced
- **Vehicle map**: ETFs (exchange-traded, intraday), index funds (dealt at NAV, mid-1970s Bogle origin; ETFs date to late 1980s/early 1990s), smart-beta/factor ETFs, actively managed ETFs (ETF wrapper with active management), ETC/ETN (different underlying and replication, not the same as ETFs). Passive means accepting the whole market without choice among constituents.
- **Match the asset class to the style**:
  - Efficient developed equity markets: replicable well passively; many benchmarks, so choose carefully.
  - Fixed income: more benchmarks and more granularity; passive providers follow different indices; liquidity of the cash bonds underlying matters. A bond index fund holds a constant duration set by the benchmark and does not behave like a held-to-maturity bond (no roll-down, never reaching maturity); active managers manage duration (mixed results). Know what index is replicated (physically or synthetically): (1) is it the market you want, (2) is the cross-product comparison coherent.
  - Niches better served actively: multi-asset (allocation delegated), hybrids, financial subordinated, catastrophe bonds, small caps, specific sectors, niche EM, less covered or illiquid segments; liquid alternative strategies (passive replications exist; decide case by case).
  - Leveraged/short ETFs: check leverage reset (daily?) and the implicit costs of the short position; long-run outcomes can differ widely from naive expectation.
- **Sharpe's arithmetic of active management (1991)**: (1) sum of all active and passive = market; (2) sum of passive = market; (3) therefore sum of active = market; (4) net of costs (higher for active), the average active manager loses to the market and to a passive peer. Independent of market efficiency. Evidence: Fama and French (2010), US active funds: gross alpha near 0 over 1984-2006; net alpha between -0.84% and -1.13% a year.
- **Three consequences for selection**: (1) the average active manager loses, but evidence shows some managers beat the market for a long time; (2) in peer-group scoring passive funds usually sit in the second quartile, so picking an above-median active manager can add significantly more; (3) find the right price for expected alpha.
- **FAR (fees for active risk)** (McKay, Shapiro, Thomas, "What Free Lunch? The Costs of Overdiversification"): `FAR = management fees / active risk (tracking error volatility)`. Lower is better: you pay little per unit of active risk. Use at fund level; at portfolio level the correlation between active strategies can lower the combined active risk while fees stay the same, raising portfolio FAR. Overdiversifying across managers can neutralize the positive expected information ratio and the fee still gets paid.
- **Over-diversification evidence**: US pension plans, 30 Sep 2015: average number of strategies by plan size: under 1 bn USD, 6; 1-10 bn, 40; 10-25 bn, 56; 25-50 bn, 82; over 50 bn, 163; all plans: 75 (maximum 297). More strategies as assets grow, with no proof of usefulness.
- **Cost reality check**: lowest-cost US ETFs (SCHB, SCHX, ITOT, SPLG, SPTM, VTI) charge 0.03% a year (ETFdb, 24 Feb 2019); European ETFs cost more. Passive grew to over one third of total assets (Morningstar chart, US). Institutional active funds at 50-70 bp must beat the market by about 5-7% cumulatively over a 10-year cycle just to cover fees (verified: 10 x 0.50-0.70%).
- **Core-satellite implementation**: core in passive for allocation fidelity and cost; satellites active. Pros/cons table (BMO ETFs): passive: market return minus fees, low cost, efficient access, smart beta lowers emotional effect, but no excess return, inefficient in illiquid classes, possible concentration; active: potential excess return, downside control, flexible mandates, but possible negative excess returns, higher costs, long bad stretches for good managers, need for rigorous due diligence (see ch13 for building multimanager portfolios).
- **Research Enhanced Index (sponsored, J.P. Morgan AM)**: hybrid ETF: index-like risk and cost, but position sizes are set by fundamental analyst conviction, cutting the price-weight link. Region, sector and style neutral, so alpha comes from stock selection (many small active positions overweighting attractive names, underweighting expensive ones). Claims: low costs and turnover, high diversification, steady modest excess return, suited to a portfolio core. Provider view; test its net-of-fee information ratio and tracking error independently.

## Key Concepts
- **Passive replication**: owning the market per the benchmark with no constituent choice.
- **Actively managed ETF**: ETF wrapper with discretionary management.
- **Tracking error volatility**: standard deviation of active return = active risk.
- **FAR**: fee paid per unit of tracking error.
- **Information ratio**: expected excess return per unit of tracking error.
- **Overdiversification**: more managers than the active-risk budget justifies.
- **Duration exposure**: constant in a bond index fund, set by the index.
- **Alpha**: return in excess of risk-adjusted benchmark.
- **Peer-group quartile**: ranking of a fund within its category.
- **Research Enhanced Index**: fundamental-research-sized index tilt.
- **Leveraged/inverse ETF**: daily-reset exposure; compounding effects over time.

## Formulas & Reference Tables
- `FAR = Management fee / TEV`.
- `Required cumulative outperformance for fee recovery (simple) = fee x years`; e.g. 0.60% x 10 = 6.0% (about 6.9% compounded at ~6% growth, source rounds to 5-7%).
- Sharpe identity: `R_active,avg (before costs) = R_market`; `R_active,avg (net) = R_market - (cost_active - cost_passive) < R_passive`.
- Choice grid:

| Situation | Lean toward |
|---|---|
| Large, liquid, efficient equity | Passive |
| Illiquid, niche, complex (hybrids, cat bonds, small cap, EM niche) | Active |
| Need exact allocation fidelity | Passive core |
| Seeking alpha with controlled risk | Active satellites, check FAR |
| Cost sensitivity, long horizon | Passive |

## Mental Models
- Use passive by default for efficient classes and active by exception where an identifiable edge exists.
- Use FAR to compare active funds: lower fee per unit of active risk wins.
- Use portfolio-level FAR, not fund-level only, once you hold several active funds.
- Use second-quartile logic: an average passive fund beats the median active; hire active only when you can plausibly select the top half.
- Use the bond-fund caveat: an index fund is not a bond; its duration never rolls down.

## Worked Example
Fee break-even and FAR. Inputs: active fund fee 0.60%, tracking error 4%, expected alpha 1.0%; passive fee 0.05%. Steps: FAR = 0.60 / 4.0 = 0.15 (15 bp of fee per point of active risk); expected IR = 1.0 / 4.0 = 0.25 gross of fee; net expected alpha = 1.0 - (0.60 - 0.05) = 0.45% a year; over 10 years, cumulative required outperformance to cover the extra fee = 0.55 x 10 = 5.5%. Interpretation: the fund adds value only if its alpha forecast is credible; if four such funds are held with correlated active bets, portfolio tracking error might be 2.5% while the weighted fee stays 0.60%, so FAR rises to 0.24.

## Anti-patterns
- Picking "all active" or "all passive" for ideology.
- Buying duration-constant bond ETFs as if they were hold-to-maturity bonds.
- Using leveraged or short ETFs as long-term positions.
- Holding dozens of correlated active funds (paying for active risk that nets out).
- Comparing index trackers without checking the underlying benchmark's definition.

## Practitioner Notes
- Fund the core with passive; require a written alpha thesis for each satellite.
- Compute FAR yourself with realized (ex-post) and expected tracking error.
- In peer group tools, remember that the passive fund's quartile rank hides that its realized gap to its benchmark is small.
- ETF and index-fund differences: dealing, liquidity, replication. Review both (see ch12).
- US ETFs are cheaper than European ones; adjust cost assumptions to the domicile.

## Key Takeaways
- Use passive for efficient, liquid classes and active where inefficiency or complexity creates room for alpha.
- Sharpe's arithmetic shows the average active manager trails after costs; Fama-French found -0.84% to -1.13% net alpha a year.
- Passive funds usually rank in the second quartile of peer groups; selecting an above-median active manager can add more.
- Judge active funds by FAR and information ratio; avoid overdiversification across managers.
- Bond index funds have constant duration; active managers manage it deliberately.
- Core-satellite lets both styles coexist with explicit roles and budgets.
- Hybrids (smart beta, actively managed ETFs, research-enhanced indices) blur the line; judge them on rules, costs and evidence.

## Connects To
- **ch09**: why hire managers (diversification, alpha).
- **ch11**: due diligence framework for both styles.
- **ch12**: passive manager selection.
- **ch13**: multimanager portfolio construction.
- **ch05**: SPIVA evidence and passive risks; **ch06**: TCO; **ch08**: smart beta.
- **ch02-ch03**: core-satellite and benchmarks.
- **`cfa-portfolio-management` ch03, ch15**: market efficiency and active management analysis.
