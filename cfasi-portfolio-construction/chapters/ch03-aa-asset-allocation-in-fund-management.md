# Chapter 3: Asset Allocation in Fund Management (Asset Allocation nella gestione dei fondi)
> **Source**: CFA Society Italy x Advisor Private, "Asset Allocation" guide (Advisor Private no. 25, 2020), Chapter 3 | Daniel Squindo, CFA; the closing insert "Creating clear and appropriate investment objectives" on VAAM applications is Vanguard-sponsored (attributed below)

## Core Idea
A practitioner's view of how allocation theory meets fund operations: (1) choose a valid benchmark, because it effectively is the strategic allocation; (2) know the three classic allocation engines (Markowitz, Black-Litterman, Risk Parity); (3) run tactical allocation top-down, bottom-up or mixed; (4) judge the result with risk-adjusted ratios and Brinson-style attribution; (5) set a rebalancing corridor. Brinson, Hood and Beebower (1986) found policy explained about 93.6% of the variation of returns of a large plan, so benchmark choice sits at the top of the decision list.

## Frameworks Introduced
- **Seven properties of a valid benchmark** (as listed in the chapter): unambiguous (weights clearly defined), investable (you can hold it instead of paying for active), measurable (public, transparent rules, computable return), appropriate (matches the manager's style or area), reflective of current views (manager knows current opinion on constituents), specified in advance (before the evaluation period, methodology known), accepted (manager takes responsibility and explains deviations). How to use: check a candidate benchmark against all seven before mandating it; for multi-asset funds build a composite from market indices. Failure mode: index choice itself moves results (example in text: 1999 Japan, FTSE index +78% vs MSCI +67%).
- **Markowitz mean-variance optimization (1952)**: inputs are expected return, variance of each asset and covariance across assets; output is the efficient set (max return for given risk, or min risk for given return). Diversification means holding assets with low correlation, not simply many assets. Failure mode: estimating expected returns is hard, so outputs are often extreme and unintuitive; practitioners think in weights, and optimizer weights often look implausible.
- **Black-Litterman (BL)** (Goldman Sachs, early 1990s): when to use: you have views of varying confidence but do not trust raw historical means. How: (1) reverse optimization (Sharpe 1974): assume the market portfolio is optimal, back out the implied equilibrium expected returns from CAPM; (2) add investor views (absolute or relative) with confidence levels; (3) blend equilibrium and views into posterior expected returns (and covariance); (4) feed into a standard mean-variance optimizer. Why it works: with no views you hold the market portfolio; the stronger the views and confidence, the further weights move from it. Gives stable, reasonable weights. Failure mode: garbage views or overconfidence still pull the portfolio away from neutral.
- **Risk Parity**: when to use: when a 60/40 portfolio hides concentrated risk. How: (1) estimate each asset class's risk contribution; (2) set weights so contributions are equal, ignoring expected returns (simplest form); (3) typically this overweights bonds and may need leverage to reach a return target; (4) include equities, real estate, credit spreads, commodities and inflation-linked bonds to avoid dependence on bonds alone. Why: limits the damage from any one asset class. Criticisms: relies on leverage on low-risk assets (bonds) and on past volatility estimates.
- **Tactical allocation approaches**: bottom-up (pick classes or securities with best prospects regardless of macro; the final allocation is the sum of independent bets) vs top-down (start from the global economic view, forecast classes and sectors, then regions, then single securities, then timing); most managers mix both. SAA models (Markowitz, Risk Parity) define the policy; BL is the tool that links views to deviations.
- **Performance ratio toolkit**: no perfect measure; pick by what the investor cares about.
  - Sharpe: excess return per unit of total standard deviation; unreliable for asymmetric payoffs.
  - Sortino: excess return over a minimum acceptable return (MAR) per unit of downside deviation.
  - Information ratio: active return over tracking error volatility (TEV); measures consistency of outperformance.
  - Calmar: return over maximum drawdown, i.e. gain relative to worst peak-to-trough loss.
- **Performance attribution (Brinson-Fachler style)**: three methods named: factor analysis (P/E, duration; heavy data), return decomposition (allocation, selection, interaction), and (implicitly) the sector approach. Active effect = portfolio return - benchmark return = allocation + selection + interaction. See formulas and the corrected example. Use it for manager self-assessment, whereas ratios serve clients.
- **Rebalancing corridors**: set a tolerance band around each target weight (example: target 20%, rebalance only outside 18-22%). No universally right width. Narrower when transaction costs are low, own-asset volatility is high, or other assets are highly volatile; wider when risk tolerance is higher, or when the asset's returns are highly correlated with the rest of the portfolio (less drift danger). Drift is natural: winners grow in weight.
- **Vanguard VAAM applications (sponsored insert)**: (i) passive/ETF model portfolios: optimize inside a chosen opportunity set and a risk-aversion level; ad hoc tilts (to emerging-market equity or cash) ignore correlations and fall below the efficient frontier; (ii) factor model portfolios using index factor funds; (iii) **manager substitution analysis**: hold factor-risk aversion fixed and raise alpha-risk aversion, and the model swaps explicit active allocation for index factor exposure (replace costly active funds with cheap factor funds); (iv) time-varying frontiers from the Vanguard Capital Markets Model, whose forecasts depend on starting valuations and short rates; (v) scenario portfolios (neutral, recession, strong growth) from the 10,000 simulations. Conceptual point: every allocation, with or without a model, embeds assumptions on alpha, equity premium and risk tolerance; the model only makes them explicit. Treat results as one vendor's illustrations (2018 data), not evidence.

## Key Concepts
- **Benchmark**: performance standard and, for passive investors, the portfolio held.
- **Composite benchmark**: weighted blend of indices for a multi-asset mandate.
- **Reverse optimization**: derive implied expected returns from market weights.
- **Efficient frontier**: set of portfolios with the highest return per unit of risk.
- **Risk contribution**: weight times marginal contribution to portfolio volatility; sums to 100%.
- **Downside deviation (DSR)**: deviation of returns below the MAR.
- **MAR (minimum acceptable return)**: the threshold used by Sortino.
- **TEV (tracking error volatility)**: standard deviation of portfolio minus benchmark returns.
- **Maximum drawdown**: worst peak-to-trough loss.
- **Allocation, selection, interaction effects**: the three components of active return.
- **Tolerance band / corridor**: permitted drift range before rebalancing.
- **Alpha risk**: risk that an active manager lags its passive counterpart (see ch02).
- **Tilt**: deliberate overweight to an asset funded from another.

## Formulas & Reference Tables
- `Sharpe = (Rp - Rf) / sigma_p`
- `Sortino = (Rp - MAR) / DSR`, `DSR = sqrt( mean( min(0, R_t - MAR)^2 ) )`
- `IR = (Rp - Rb) / TEV`, `TEV = std(Rp,t - Rb,t)`
- `Calmar = annualized return / |maximum drawdown|`
- Segment `i` with portfolio weight `wp_i`, benchmark weight `wb_i`, segment returns `Rp_i`, `Rb_i`, total benchmark return `R_B`:
  - `Allocation = (wp_i - wb_i) x (Rb_i - R_B)`
  - `Selection = wb_i x (Rp_i - Rb_i)`
  - `Interaction = (wp_i - wb_i) x (Rp_i - Rb_i)`
  - `Active effect = Allocation + Selection + Interaction`
- `Risk contribution_i = w_i x (S w)_i / sigma_p`; naive risk parity (uncorrelated assets): `w_i proportional to 1/sigma_i`.
- **⚠ Correction**: the source's selection and interaction examples contain errors. Selection must use the benchmark weight (7%), not the portfolio weight, giving 7% x (8% - 9%) = -7 bps (the text shows -15 bps). Interaction is (15% - 7%) x (8% - 9%) = -8 bps (the text shows +8 bps, a sign error). Source also states allocation as "0.0016%"; the figure is 0.16% = 16 bps. Check: 16 - 7 - 8 = +1 bp, which equals the active contribution.

## Mental Models
- Use the benchmark as the contract: decide it before the evaluation period and make it investable.
- Use Black-Litterman when you have a few views to express and want the market portfolio as the default.
- Use risk parity to test whether your allocation is really diversified: look at risk shares, not weights.
- Use Sortino or Calmar when return distributions are skewed or the investor fears drawdowns; Sharpe for roughly symmetric returns; IR for active mandates.
- Use attribution to separate "right sector" from "right stocks" before judging a manager.
- Use wider corridors for low-cost-sensitivity, high-tolerance investors, narrower for volatile holdings.

## Worked Example
Brinson-Fachler decomposition. Inputs: benchmark (S&P 500) return 7%; Technology segment benchmark return 9%, portfolio segment return 8%; benchmark weight 7%, portfolio weight 15%. Steps: allocation = (15% - 7%) x (9% - 7%) = +16 bps; selection = 7% x (8% - 9%) = -7 bps; interaction = 8% x (-1%) = -8 bps. Result: Technology adds +1 bp in total (checks against 15% x 8% - 7% x 9% - 8% x 7% = 1 bp). Interpretation: the manager was right to overweight the sector but picked stocks worse than the sector index, and the overweight amplified that miss; overweighting a segment where you select poorly costs money.

Risk parity illustration (recomputed): 60/40 portfolio, equity vol 15%, bond vol 5%, correlation 0.2 gives portfolio volatility 9.6% and an equity risk share of 91.8% (the source quotes about 90%). Naive equal-risk weights with zero correlation would be 25% equities, 75% bonds, which needs leverage to match a 60/40 return.

## Anti-patterns
- Choosing a benchmark after seeing results, or one the fund cannot replicate.
- Judging with Sharpe alone for option-like or highly skewed strategies.
- Letting interaction effects disappear into "selection" without understanding the source.
- Running raw Markowitz on historical mean returns.
- Rebalancing on a fixed calendar when volatility is spiking, or setting identical bands for volatile and stable assets.
- Adding ad hoc tilts without checking correlations (frontier test).

## Practitioner Notes
- Day-to-day deviations from the model portfolio also come from flows (redemptions, subscriptions), not just views; keep the policy and track actual versus model weights.
- A 60/40 portfolio is an equity-risk portfolio; if the client expects balance, show risk contribution.
- Index choice can swing annual returns by several points; state the index in all reporting.
- The Squindo article is practitioner commentary with few formulas; cite the original papers (Markowitz 1952, Sharpe 1966/1974, Brinson et al. 1986) for rigor.
- Attribution formulas vary (Brinson-Hood-Beebower vs Brinson-Fachler); confirm which your platform uses before comparing results.

## Key Takeaways
- Benchmark selection equals SAA selection: apply the seven validity criteria.
- Markowitz needs good inputs; Black-Litterman anchors on market equilibrium and moves with confident views; Risk Parity equalizes risk shares.
- Tactical decisions come from top-down, bottom-up or both; SAA models are not a tactical tool except BL.
- Choose performance metrics to match what the investor fears: Sharpe (volatility), Sortino (shortfall), IR (consistency vs benchmark), Calmar (drawdown).
- Attribution splits active return into allocation, selection and interaction; always reconcile the sum.
- Rebalancing bands widen with risk tolerance and correlation to the portfolio, and narrow with volatility and low costs.
- A model does not remove assumptions; it makes them visible.

## Connects To
- **ch01**: performance decomposition SAA + TA + SS + IR (same idea as the attribution here).
- **ch02**: SAA/TAA, Black-Litterman as the TAA tool, rebalancing and VAAM.
- **ch04**: allocation for private investors.
- **ch05-ch08**: passive vehicles used to implement benchmark-based allocation.
- **`cfa-portfolio-management` ch02, ch04, ch18**: indexes, portfolio management process, performance evaluation.
- **`cfa-asset-allocation-cme` ch06-ch07**: asset allocation approaches in the CFA curriculum.
