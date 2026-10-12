# Chapter 2: Asset Allocation for Institutional Investors (Asset Allocation per gli Investitori Istituzionali)
> **Source**: CFA Society Italy x Advisor Private, "Asset Allocation" guide (Advisor Private no. 25, 2020), Chapter 2 | Riccardo Rasi, CFA, and Danilo Giuliani; the Vanguard-sponsored insert on active vs passive and the VAAM model is attributed below

## Core Idea
For an institution, asset allocation (AA) is the master decision: Ibbotson and Kaplan (2001) report that policy explains roughly 50-90% of ex-post return variation depending on how the question is posed, while security selection, market timing and fees explain the rest. The chapter builds a top-down chain: investor type decides the mandate (liability-driven vs asset-only), the IPS fixes objectives and constraints, then SAA sets long-run weights, TAA allows bounded deviations, and a rebalancing rule keeps risk in check. Alternatives and factor/passive tools are the post-2010 evolution when low rates stop paying for traditional risk.

## Frameworks Introduced
- **Three management approaches**: liability-driven (target return set by liabilities), asset-only (maximize return for a risk budget), goal-based (private investors with personal goals). When to use: first classify the investor, because it fixes risk appetite. How: (1) are liabilities contractual and binding? then liability-driven, ALM first; (2) are returns free of liabilities (defined-contribution funds, foundations)? then asset-only, higher risk appetite since missing a target breaks no promise; (3) personal spending goals? then goal-based. Why it works: the cost of failure differs. Failure mode: a liability-driven investor running an asset-only SAA (or the reverse) mis-prices shortfall risk.
- **Asset-class design tests**: a class should be (a) internally homogeneous and highly correlated (shared systematic risk factor), (b) different from the other classes (low or negative correlation, different factors), (c) non-overlapping (a security sits in one class only), (d) investable and reasonably liquid (a secondary market exists). The text adds exhaustiveness (the set covers the investable universe). Granularity falls as investor size and sophistication fall. Caveat: high yield behaves like equity in stress, and "alternatives" (defined in the 1980s as everything non-traditional) is now too generic a bucket.
- **Global market portfolio as starting point**: market-value-weighted portfolio of all investable classes. Theoretically the most diversified, minimizing diversifiable risk, but not fully investable, so it is a reference, not a recommendation. Deviations (ESG constraints, regulation, taxes, views) must be explicit choices.
- **Top-down (macro to micro) vs bottom-up**: top-down starts from asset classes, then selects within them. Why institutions prefer it: forecasting expected return for a homogeneous class is easier than for single securities because idiosyncratic risks net out, leaving market-wide risk drivers; common risk factors across classes give better correlation estimates and thus real diversification. Phases: SAA, then TAA.
- **SAA (strategic asset allocation)**: identify classes and long-run average weights over a medium-long horizon, set a benchmark per class, then weights from past benchmark performance, market-variable forecasts and macro scenario. Standard engine: Markowitz mean-variance optimization (lowest standard deviation for each target return). Weaknesses noted: unstable outputs, concentration, and large losses when inputs are wrong. Fixes: extra constraints and Bayesian estimation of expected returns (the Black-Litterman family) to get stable, diversified, view-aware weights.
- **Active vs passive at two levels**: (i) at AA level, active = TAA (changing weights), passive = holding weights as set; (ii) per asset class, passive = market-cap weights, active = security weights changed. Choose by: efficiency of the class (more efficient, weaker case for active), investability and liquidity (harder access favors active), ESG or other constraints that push away from market weights (force active choices), regulation and tax treatment.
- **Core-satellite**: passive core to minimize cost and tracking risk, active satellites for excess return. Born from low risk-free yields: invest passively where active rarely produces positive alpha, actively where excess return is plausible (alternatives).
- **Long-only vs long-short**: long-only cannot hedge a negative view on a segment; long-short can.
- **Risk budgeting**: decide which risks to take, how much, and the metric (volatility, tail risk, drawdown).
- **TAA mechanics**: bounded deviations from SAA (upper/lower bounds on each weight), usually built with Black-Litterman plus constrained optimization: absolute and relative views, each with a confidence level (higher confidence means larger departure from SAA). Add a risk cap: maximize return subject to portfolio sigma not above the investor's profile, plus a **relative VaR** limit versus the strategic portfolio (example: 8% relative VaR at 95% means a 5% probability of underperforming SAA by more than 8%). TAA costs money and risk, so compare expected excess return with cost, and portfolio risk with client tolerance.
- **Rebalancing policy**: (1) calendar (simple, low turnover, ignores interim drift, can trade needlessly); (2) tolerance bands (needs monitoring, trades only when needed). On trigger, restore either exactly to SAA or just inside the band. Justification: mean reversion, since classes cannot stay at extreme returns forever.
- **Constant priority (CPPI-type) strategy**: `risky exposure = m x (portfolio value - floor)`. When to use: investors with guarantees who want dynamic protection. How: (1) set floor = present value of the capital to secure; (2) set multiple m from risk appetite; (3) risky exposure = m x cushion, remainder in risk-free assets; (4) re-compute at each rebalancing. With m = 0 it collapses to buy-and-hold (floor strategy fully in safe assets); with m above 1 it buys risky assets in rallies and sells in falls (convex, option-like payoff, synthetic put with no explicit hedge cost). Failure mode: a gap move below the floor between rebalances, and whipsaw (buying high, selling low) in range markets.
- **ALM techniques for liability-driven investors**: cash-flow matching (outflows covered by inflows from the portfolio); interest-rate and price risk management by **duration gap analysis**; hedging with derivatives or **portfolio insurance** replicating put payoffs. Actuarial valuation can be semi-deterministic (immunization: assets and liabilities equally sensitive to rate moves, per the general immunization theorem) or stochastic (yield curves from stochastic models, assets and liabilities projected jointly). Mature schemes with steady outflows mix duration matching (immunize rate moves) and cash-flow matching (cash for near-term payments).
- **Vanguard VAAM (sponsored insert; Vanguard Asset Allocation Model, 2017)**: utility-based optimizer that adds **alpha-risk aversion** to ordinary risk aversion. Inputs: return distributions for asset classes, active strategies and long-only factors (via Vanguard Capital Markets Model, VCMM), investor attitude to systematic risk, alpha risk and factor-premium risk, constraints. Output: allocation among passive, active and factor sleeves maximizing expected utility. Core ideas: expected alpha is an ex-ante belief, not a certainty; manager outcomes are a probability distribution around the passive benchmark, so even a manager with positive expected alpha can lag it, and the lagging area depends on tracking error (alpha risk). Traditional MVO is the special case of infinite alpha-risk aversion, one slice of a three-dimensional "efficient surface". Sequential tree approaches (passive first, then factors, then active) use information inefficiently. Treat it as one provider's method, not a standard.

## Key Concepts
- **Asset class**: group of assets sharing a systematic risk factor and partly decorrelated from other groups.
- **IPS (Investment Policy Statement)**: document with return objective, risk tolerance, constraints, horizon, AA model, allowed instruments, benchmark and rebalancing policy.
- **ALM (Asset Liability Management)**: integrated analysis of assets and liabilities, mandatory for pension, insurers, professional funds.
- **Asset-only approach**: liabilities in the background; the objective is maximum return for a given risk budget.
- **Inverted production cycle**: premiums or contributions are collected before the benefits are paid.
- **Fully funded / over-funded**: assets equal / exceed liabilities; the surplus can be run asset-only.
- **Defined-benefit (DB) vs defined-contribution (DC) fund**: DB bears the promise; in DC the member bears the market risk.
- **Life-cycle mechanism**: financial risk falls as the member ages (DB-style pension schemes with compartments).
- **Duration gap**: difference between asset and liability duration, the measure of rate-risk mismatch.
- **Tracking error volatility**: standard deviation of active return, the risk limit for passive mandates.
- **Smart beta**: rules-based indices replicating active-style factor tilts at lower cost with transparent holdings.
- **Risk factors**: macro or style drivers (size, value, etc.) whose correlations tend to fall in crises, unlike asset-class correlations (which rise).
- **Illiquidity premium**: extra return from private markets and funds that cannot be sold quickly.
- **Event-driven / arbitrage hedge funds**: merger arbitrage, convertible arbitrage and fixed-income arbitrage harvest market inefficiencies or corporate events.

## Formulas & Reference Tables
- `Constant priority: E = m x (V - F)`; E = risky exposure, V = portfolio value, F = floor (present value of the capital to guarantee), m = multiple; bond exposure = V - E (long-only: E capped at V).
- `Relative VaR (95%, 8%)`: P(portfolio return < SAA return - 8%) = 5%.
- `Mean-variance`: minimize `sigma_p^2 = w'Sw` subject to `w'mu = target`, weights sum to 1.
- `Immunization (duration matching)`: asset duration = liability duration and PV(assets) >= PV(liabilities).

| Investor | Approach | Horizon / risk | Management freedom |
|---|---|---|---|
| Insurer, non-life | ALM | short, low risk | regulated |
| Insurer, life | ALM | long, higher financial risk | regulated |
| DB pension fund | ALM | long, risk depends on funding ratio | little direct management; mostly outsourced, tight mandates (turnover, absolute-risk or tracking-error limits) |
| Professional pension scheme (cassa) | ALM | long, low risk appetite, bonds and alternatives for prudential diversification | freer, direct or indirect |
| DC pension fund | asset-only (guaranteed lines hybrid, portfolio insurance) | long, life-cycle compartments | same regulatory constraints as DB |
| Banking foundation | asset-only | medium-long, sustainable spending rate with capital preservation | full freedom to outsource or insource |

## Mental Models
- Use top-down when you want robust return forecasts and correlations: forecast classes, not securities.
- Use the global market portfolio as the null hypothesis and require a reason for every deviation.
- Use bands rather than calendars when volatility is high and monitoring is available; use calendars when simplicity and low turnover matter.
- Use CPPI when a floor is mandatory; expect to lose to buy-and-hold in sideways markets as the price of insurance.
- Use alternatives only if the horizon is long and liquidity needs low; the premium is for illiquidity.
- Use factors as a second lens on diversification: classes can look different but share the same factor in a crisis.

## Worked Example
CPPI with floor. Inputs: V = 100, floor F = 80, multiple m = 4. Steps: cushion = 20, risky exposure = 4 x 20 = 80, safe asset 20. Risky assets fall 10%: loss 8, V = 92, cushion 12, new exposure 48 (sell 24 of risky). Alternatively risky rise 10%: V = 108, cushion 28, formula gives 112 > 108, so the long-only cap sets exposure to 108 (fully invested, no leverage). Result: exposure shrinks mechanically by 40% after a 10% loss, so the floor is protected unless a gap drop above 25% (1/m) occurs between rebalances. Interpretation: m sets how much market fall can be absorbed (a fall of 1/m of the risky position takes V to the floor) and also the cost of whipsaw.

## Anti-patterns
- Starting from security picks without an agreed allocation and IPS.
- Treating "alternatives" as one diversifier without checking its liquidity and factor exposure.
- Rebalancing calendar-only through a crash (or ignoring costs with tight bands).
- Plain unconstrained Markowitz run on point estimates.
- Cutting TAA views without confidence levels or relative VaR limit.
- Running a guaranteed-return fund with asset-only risk logic.

## Practitioner Notes
- The Ibbotson-Kaplan "40, 90, 100 percent" question has three different answers depending on whether you ask about time-series variation, cross-section across funds or level of return; quote the right one.
- Low-rate policy pushed institutions to raise risk deliberately; the text frames this as seeking risk that is paid (illiquid alternatives) and exposure to specific factors, not blind reach for yield.
- In stress, class correlations rise while factor correlations tend to fall: check the factor map before trusting asset-class diversification.
- Smart beta and automated factor indices are a middle path between active and passive, but their rules must be understood (transparent does not mean riskless).
- Treat VAAM-style models as inputs to a discussion with a professional adviser; the insert itself says answers come with adviser guidance.

## Key Takeaways
- Asset allocation drives most of the variability of portfolio results; fix it first and fix it explicitly in the IPS.
- Classify the investor (liability-driven, asset-only, goal-based) before choosing return and risk targets.
- Good asset classes are homogeneous inside, distinct outside, non-overlapping and investable.
- Run SAA as top-down, with constrained or Bayesian optimization; use TAA in bounded bands with confidence levels and relative VaR.
- Choose rebalancing rules (calendar vs bands vs constant priority) for the objective: simplicity, risk control or protection.
- Liability-driven investors manage the funding gap through cash-flow matching, duration gap and hedging or portfolio insurance.
- Alternatives and factor exposures add diversification and a paid illiquidity or factor premium, but need long horizons.
- Active vs passive is a per-class decision based on efficiency, liquidity, constraints and cost; core-satellite combines both.

## Connects To
- **ch01**: life-insurer ALM, the most developed liability-driven case; solvency and RAF.
- **ch03**: AA inside funds (fund-level SAA/TAA implementation).
- **ch04**: AA for private investors (goal-based approach).
- **ch05-ch08**: passive investing as the building block for core portfolios.
- **ch15**: alternatives case and diversification.
- **`cfa-asset-allocation-cme` ch03-ch04, ch06-ch07**: capital market expectations, asset allocation principles, mean-variance inputs.
- **`cfa-wealth-institutional-management`**: IPS for institutional investors.
