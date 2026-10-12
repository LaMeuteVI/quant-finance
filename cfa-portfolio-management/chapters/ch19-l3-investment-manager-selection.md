# Chapter 19: Investment Manager Selection
> **Source**: CFA Program Curriculum 2023, Level III, Reading 27 · Portfolio Management | Jeffrey C. Heisler, PhD, CFA, and Donald W. Lindsey, CFA

## Core Idea
Manager selection is due diligence, not return-chasing. The question is not "who did well?" but "will this process keep producing this return distribution, from identifiable sources, at an acceptable net cost, inside a firm that will survive and tell the truth?" A sound selection process has three layers: a defined universe, a quantitative read of the track record (attribution, appraisal, capture ratios, drawdowns, style), and qualitative due diligence split into investment and operational. Hiring and firing are hypothesis tests with asymmetric, psychologically distorted errors.

## Learning Outcomes Covered
- Describe the components of a manager selection process, including due diligence
- Contrast Type I and Type II errors in hiring and continuation (retain/fire) decisions
- Describe uses of returns-based (RBSA) and holdings-based (HBSA) style analysis
- Describe uses of upside/downside capture, maximum drawdown, drawdown duration in evaluating managers
- Evaluate a manager's investment philosophy and decision-making process
- Evaluate costs and benefits of pooled vehicles vs separate accounts
- Compare manager contract types (liquidity, fee provisions), describe the three forms of performance-based fee, interpret a fee schedule

## Frameworks Introduced
- **Manager search and selection process (three components)**: universe, quantitative analysis, qualitative analysis (investment DD + operational DD).
  - When to use: any hire, add, replace or retain decision after the IPS and asset allocation are set. The IPS and the reason for the search define the role.
  - How: (1) Define the feasible universe. A new strategic or tactical exposure means a broad universe and "best in class". Adding capacity or diversification means a complement to current holdings. Replacing a manager means "best within the strategy". (2) Quantitative: return distribution, attribution and appraisal (skill?), capture ratios (up vs down markets), drawdowns (tail behavior), style analysis (exposures). (3) Qualitative: philosophy, process, people, portfolio construction (investment DD), then process/procedures, firm, vehicle, terms, monitoring (operational DD).
  - Why it works / failure mode: the unstated assumption is that a consistent, robust process yields a similar return distribution relative to risk factors across time. Qualitative DD tests whether that assumption holds. Failure mode: letting backtested numbers substitute for understanding how the returns were produced.
- **Universe definition (hybrid approach)**: assign managers to a benchmark and strategy bucket by combining four methods.
  - How: third-party categorization (fast, but check the provider's criteria against the portfolio role), returns-based style analysis (objective, extra computation), holdings-based style analysis (current exposures, depends on transparency), manager experience/judgment. Start with third-party data, refine with quant and experience.
  - Why it works / failure mode: do not screen on performance at this stage; screen on risk profile and role. Too narrow a search misses candidates, too broad gains nothing. The universe is dynamic (strategies drift, managers enter and exit).
- **Type I / Type II error framework**: null hypothesis = manager has no skill.
  - Type I = hire or retain a manager who then underperforms expectations (reject a true null). Type II = do not hire or fire a manager who then performs in line or better (fail to reject a false null).
  - When to use: every hire, retain and fire decision. Decide which error is cheaper given the benefits and costs of changing managers.
  - Why it works / failure mode: decision makers over-weight Type I (error of commission, explicit cost, measurable, linked to pay, visible to the client) and under-weight Type II (omission, opportunity cost, unmeasured). Fix: track not only managers held but managers evaluated-and-rejected and managers fired, and test whether the hire/fire factors are consistent with your own philosophy and whether retaining or firing added value.
- **Investment philosophy test**: five questions. (1) Can the manager articulate the philosophy clearly and consistently? (2) Are the assumptions credible, and consistent with the process (and with the allocator's own beliefs about market efficiency)? (3) How has it evolved (reasonable response to markets vs ad hoc reaction to performance or flows)? (4) Are return sources tied to a credible inefficiency? (5) Capacity: does the inefficiency pay enough, often enough, to cover costs and fees (without leverage?), is it repeatable, is it sustainable at the manager's AUM?
- **Inefficiency taxonomy**: behavioral (created by other participants' biases, e.g., trend following, loss aversion; temporary, ends on convergence) vs structural (created by rules and regulations; long-lived, assumes the rules continue rather than prices converging). Passive strategies instead assume efficiency and harvest risk premia (equity, duration, credit, plus alternative premia: liquidity, volatility, catastrophe risk).
- **Four-element decision process**: signal creation (is information unique, timely, or interpreted differently?), signal capture (how ideas become positions, who approves), portfolio construction (allocation method, conviction weighting, stop-losses hard/soft, instruments, hedge sizing, long/short pairing, liquidity), monitoring (feedback loop on external environment and internal drift).
- **Style analysis (RBSA and HBSA)**:
  - RBSA = top-down regression of portfolio returns on factor/index returns. HBSA = bottom-up exposures computed from the securities held at a date.
  - Must be meaningful, accurate, consistent, timely. Both should agree with the stated philosophy; if not, the process may not be repeatable or consistently implemented. Track over time to detect style drift.
  - Most useful for liquid, frequently priced strategies. For hedge funds, PE and VC, use it to design further DD questions, not to confirm the process.
- **Active share vs tracking risk grid** (Exhibit 7): low AS/low TR = closet indexer; low AS/high TR = sector rotation; high AS/low TR = diversified stock picker; high AS/high TR = concentrated stock picker. "Low/high" are relative to the universe and category definitions.
- **Operational due diligence checklist**: trading policy, soft dollars, unauthorized-trading controls, fee calculation, allocation across accounts (objective, e.g., by invested capital), strategy proliferation vs infrastructure, backup and cybersecurity, service providers (prime broker, administrator, auditor, counsel; auditor changes are a red flag), risk function independence (risk manual, hard/soft guidelines, breach cure process, independent risk officer), firm business risk (ownership, AUM, breakeven AUM, closed strategies), compliance and legal history, alignment (employee co-investment, deferred stock).
- **Performance-based fee structures (three basic forms)**:
  1. Symmetrical: `Fee = Base + Sharing × (performance)`; manager fully exposed to downside and upside.
  2. Bonus, upside uncapped: `Fee = max(Base, Base + Sharing × positive performance)`; floor at base, no cap.
  3. Bonus, capped: `Fee = max(Base, Base + Sharing × performance) subject to a maximum fee`.
  - Provisions: high-water mark (HWM), clawback, maximum fee, hurdle. Bonus fees are economically a call option on active return struck at the base fee, minus a call struck at the max fee.

## Key Concepts
- **Due diligence**: investigation and analysis supporting an investment action or recommendation; for managers it covers both how past results were achieved and whether the process, firm and people will repeat them.
- **Investment due diligence**: qualitative review of philosophy, process, people and portfolio construction.
- **Operational due diligence**: review of infrastructure, procedures, firm sustainability, vehicle and terms to find risks not visible in historical returns.
- **Style drift**: movement of exposures away from the stated style; signalled by tracked RBSA/HBSA deviating from expectation.
- **Upside capture (UC)**: portfolio return as a share of benchmark return in benchmark-up periods; >100% suggests outperformance in up markets.
- **Downside capture (DC)**: same ratio in benchmark-down periods; <100% suggests outperformance in down markets.
- **Capture ratio (CR)**: `UC / DC`; measures return asymmetry; >1 means more participation in up than down markets.
- **Drawdown / drawdown duration**: cumulative peak-to-trough loss over a continuous decline; total time from the start of the drawdown until the cumulative loss recovers to zero. Drawdowns act as a stress test of process, risk control and people.
- **Active share**: `½ Σ |w_strategy,i − w_benchmark,i|`; 0 = replicates the benchmark, 1 = no overlap.
- **Key person risk**: strategy depends on a single person or small team whose departure would hurt performance.
- **Capacity**: level, repeatability and sustainability of returns an inefficiency can support, including opportunity count, liquidity, and AUM absorbed without dilution.
- **Breakeven AUM**: asset base needed for fee revenue to cover total firm expenses.
- **Separately managed account (SMA)**: segregated account in the investor's name, customizable, direct ownership. **Pooled (commingled) vehicle**: assets of many investors in one portfolio without customization (open-end, closed-end, ETF, ETN, hedge fund).
- **Lockup (hard/soft)**: initial period with no redemptions; soft lock allows redemption for a fee paid into the fund (equivalent to a mutual fund redemption fee). **Gate**: cap on assets redeemable at one redemption date.
- **High-water mark (HWM)**: no performance fee until prior losses are recouped; protects investors from paying for recovery of earlier losses.
- **Ad valorem fee**: percentage of AUM; "sticky" assets mean it rewards retention more than performance.
- **Principal-agent problem**: agent controls effort and risk, principal controls assets; skills and actions are not fully visible.

## Formulas & Reference Tables
- `Upside capture = (portfolio annualized return in benchmark-up periods) / (benchmark return in those periods)`; `Downside capture` analogous for benchmark-down periods; `Capture ratio = UC / DC`.
- `Active share = ½ Σᵢ |wᵢ,strategy − wᵢ,benchmark|` over all N securities, range 0 to 1.
- `Symmetrical fee = Base + s × (R_net of base)`; `Bonus fee = Base + s × max(R_net of base, 0)`; `Capped bonus = min(Bonus fee, Max fee)`. Check each fund's text: sharing may be on active return, on return net of base, or on total return.
- `Net active return = Active return − Billed fee`.
- Fee effects: a management fee shifts the mean down and leaves σ unchanged; a performance fee lowers the mean and also lowers measured σ (accruals pull returns toward zero), understating downside risk, and the larger the fee the stronger the effect.

**Return profile capture ratios (CFA Exhibit 4)** and what they imply:

| Profile | UC | DC | CR | Reading |
|---|---|---|---|---|
| Long only | 100% | 100% | 1.0 | Beta 1 |
| Positive asymmetry | 75% | 25% | 3.0 | Convex payoff; skill or inherent strategy shape? |
| Low beta | 50% | 50% | 1.0 | Same asymmetry as index, half the volatility |
| Negative asymmetry | 25% | 75% | 0.33 | Participates in losses, not gains |

**Stylized profile statistics, Jan 2000-Dec 2013 (S&P 500 + T-bills, CFA Exhibit 6)**: long only: annualized 3.60%, σ 15.64%, Sharpe 0.10, max DD −50.9%. Low beta: 3.14%, 7.79%, 0.14, −28.3%. Positive asymmetry: 8.86%, 9.61%, 0.71, −26.9%. Negative asymmetry: −1.98%, 10.01%, −0.40, −48.9%. Lesson: limiting drawdown can improve both absolute and risk-adjusted return.

**RBSA vs HBSA**

| | RBSA (top-down) | HBSA (bottom-up) |
|---|---|---|
| Input | Return series vs factor indexes | Position-level holdings |
| Data burden | Low, easy to obtain | High; needs transparency, may lag |
| Window dressing | Resistant (uses actual returns) | Exposed (snapshot) |
| Precision | Imprecise: attributes to an unchanging average portfolio, hides dynamic decisions | Accurate current exposures |
| Illiquid / stale prices | Understates risk | Understates risk |
| Complex strategies | Estimable | Hard; needs understanding of the strategy; easier for equities |
| High turnover | Average portfolio | Snapshot may not reflect future |

**Liquidity ladder (most to least liquid)**: ETFs and closed-end funds (intraday, price depends on depth) > open-end funds (daily at NAV) > hedge funds (redemption frequency, notice period, lockup, gates) > private equity / VC (capital calls over about 5 years, life about 10 years plus two 1-year extensions) . SMA liquidity = liquidity of the securities held.

**SMA vs pooled vehicle**

| Factor | SMA | Pooled |
|---|---|---|
| Ownership/legal recovery | Direct, segregated | Shared; exposed to other investors' redemptions |
| Customization | Yes | No |
| Tax efficiency | Higher (own realized gains, tax-loss harvesting) | Lower |
| Transparency | Real-time position level | Delayed |
| Cost | Higher, does not scale, trades not aggregated | Lower, scales |
| Attribution | Confounded by investor constraints (tracking risk) | Clean manager decisions |
| Behavioral risk | Micromanagement, performance chasing, familiarity bias, loss aversion | Low |

**Exhibit 8 sample fee schedule (verified)**: standard fee 0.50%, base 0.25%, sharing 20% of active return beyond the base, max 0.75%, so the cap binds at active return 2.75%.

| Active return | ≤0.25% | 1.00% | 1.50% | 2.00% | ≥2.75% |
|---|---|---|---|---|---|
| Billed fee | 0.25% | 0.40% | 0.50% | 0.60% | 0.75% |
| Net active return | ≤0.00% | 0.60% | 1.00% | 1.40% | ≥2.00% |

Breakeven active return = 1.50% (billed fee equals the 0.50% standard fee).

## Mental Models
- **Process first, performance second**: past performance only informs if the process that produced it is repeatable. Reconcile the track record with the claimed process (the Madoff test: unnaturally smooth returns, a strategy "too complex to explain", broker-dealer fee model, a three-person auditor).
- **Skilled-vs-unskilled distribution overlap**: the more the two return distributions overlap (efficient markets, short samples), the cheaper both errors are and the weaker the case for churning managers; the more distinct, the bigger the opportunity cost of Type II. Mean-reverting strategies make performance-chasing a Type I factory.
- **Drawdown as a stress test of people**: how a manager behaves in a loss (stop-losses triggered at the bottom, as in August 2007 quant equity; deviation from the process; business risk crowding out investment risk) is more informative than the loss itself. A disciplined response vs panic vs misaligned interest are different diagnoses.
- **Horizon and risk capacity decide the tolerable drawdown**: investors near the end of the horizon need shallower, shorter drawdowns (lower DC, small max DD). Absent a change in policy or suitability, resist exiting at the bottom.
- **Bonus fee = call option on active return**: higher active volatility increases option value, so the manager is paid to take risk; the cap gives a short call, flattening incentives at the top. Prefer linear compensation (fewer inflection points) and set benchmarks and risk monitoring accordingly.
- **Fee certainty vs alpha uncertainty**: fees are paid for sure, alpha is not. If expected gross alpha equals the extra cost, a risk-averse investor should pick the passive option. Only net (after-fee, ideally after-tax) positive significant excess return is evidence the skill benefits the investor.

## Worked Example
**1. Fee payoffs, three structures (CFA fund set, recomputed).** Base fee b, sharing s = 20%.
- Symmetric (Yellow Wood: b = 1.50%, sharing on return net of base). 2016 gross 15%: `1.5 + 0.2 × (15 − 1.5) = 4.20%`. 2017 gross −5%: `1.5 + 0.2 × (−5 − 1.5) = 0.20%`. 2018 gross 7%: `1.5 + 0.2 × 5.5 = 2.60%`. The fee falls below base after a loss (manager shares downside).
- Bonus, no cap (Red Grass: b = 1.00%, sharing on return net of base). 2016 gross 8%: `1 + 0.2 × 7 = 2.40%`. 2017 gross −2%: net of base negative, so fee = floor `1.00%`. 2018 gross 5%: `1 + 0.2 × 4 = 1.80%`.
- Capped bonus (Blue Water: b = 0.50%, sharing on active return, cap 2.50%). 2018 active 14 − 2 = 12%: `0.5 + 0.2 × 12 = 2.90%`, capped at 2.50%.
- High-water-mark recalculation for Red Grass: after 2017's −3% (net of base), 2018's 4% net-of-base gain first recoups 3%, so only 1% is shared: fee `1 + 0.2 × (4 − 3) = 1.20%` instead of 1.80%. Only 2018 changes (2016 sets the mark, 2017 pays floor).
- Interpretation: the Yellow Wood symmetric structure aligns risk and effort best but is the least popular with managers; the bonus structures (Red Grass: uncapped option, highest incentive to gamble) give the strongest incentive to increase risk; the cap at Blue Water reduces that incentive once the cap binds.

**2. Choosing between funds on capture and drawdown (retiring in 3 years, loss averse).** Funds: Alpha UC 80 / DC 20 (CR 4.0), last drawdown −57% over 21 months; Beta 55 / 45 (CR 1.22), −38% over 15 months; Gamma 50 / 50 (CR 1.0), −28% over 12 months. Alpha has the best asymmetry but a 57% drawdown that took 21 months to recover is incompatible with a 3-year horizon and strong loss aversion. Gamma has the shallowest and shortest drawdown and the lowest risk, with UC = DC, so it is the suitable choice despite the weaker ratio. Also check whether Alpha's asymmetry is inherent (e.g., option strategy) or skill, and why its drawdown was so deep despite 20% downside capture (a deviation from process, or a one-off event?).

**3. Active share.** Strategy weights (30, 30, 20, 20, 0)% vs benchmark equal-weight (20 each): `½ × (10+10+0+0+20) = 20%`. Low active share: with low tracking risk this is closet-indexer territory.

## Anti-patterns
- **Screening the universe on historical returns**: bakes in performance chasing; screen on role, risk profile and strategy, then evaluate performance.
- **Hiring after a hot year, firing after a bad one**: trend following with mean-reverting strategies; the cited sponsor study found products receiving contributions later underperformed those with withdrawals (over $170 billion lost).
- **Avoiding Type II errors out of regret aversion only**: never tracking fired or rejected managers means the selection process is never audited.
- **Accepting a manager who cannot articulate specific inefficiencies per position**: "we exploit inefficiencies" is not a thesis; credible managers state how their information or view differs from price and track whether the market comes round.
- **Relying on self-reported or inconsistent risk reports**: missing, selective, late or inaccurate reporting signals either poor controls or concealment.
- **Taking an SMA for control and then micromanaging**: negates the point of hiring; also brings attribution noise from the investor's own constraints.
- **Computing risk on net-of-performance-fee returns**: the fee structure converts symmetric gross active returns into asymmetric net returns and understates downside risk; analyze gross and net separately.
- **Ignoring side effects of fee mixes at the manager**: performance-fee accounts can be favored in trade or IPO allocation (an ethics issue); check the allocation policy.
- **Treating style analysis on illiquid or hedge strategies as confirmation**: stale pricing understates volatility; use it only to generate DD questions.

## Exam Focus & Traps
- **Type I vs II labels**: Type I = hire/retain someone who underperforms (error of commission). Type II = fail to hire/fire someone who outperforms or performs in line (omission). Questions give two decisions on different skill levels; match each to the table (hire an unskilled = Type I; not hire a skilled = Type II).
- **Investment DD vs operational DD**: philosophy, process, people, portfolio construction are investment DD. Procedures/back office, firm, vehicle, terms, monitoring and compensation/compliance arrangements are operational. "Key person risk" and expertise depth are investment DD; "employee compensation arrangements" is operational (legal/compliance). Uniqueness of information belongs to assumptions of the process, not to capacity.
- **Capture-ratio direction**: UC < 100% and DC > 100% (e.g., 75% / 125%) means underperforming the benchmark in both up and down markets. Worse relative performance in downturns shows up as DC above 100%; the ratio CR = UC/DC mixes both sides, so always read UC and DC separately before inferring a CR below or above 1.
- **RBSA vs HBSA**: RBSA needs less/easier data, resistant to window dressing, but imprecise; HBSA is subject to window dressing and snapshot problems, harder for complex strategies. Both mislead with illiquid securities. Style inconsistent with stated philosophy = process may not be repeatable (not "absence of style drift").
- **Style drift for a fixed benchmark mandate**: moving into small caps or out of the benchmark's bond sector is drift; raising cash tactically is a manager decision within mandate and not necessarily drift.
- **Universe defining**: avoid excluding managers on historical risk-adjusted returns at this stage; identifying the benchmark and using third-party categories are appropriate.
- **Efficiency link**: more efficient markets means smaller skilled/unskilled difference, lower opportunity cost. A highly distinct skilled distribution means high opportunity cost of not hiring a skilled manager.
- **Liquidity ranking**: ETFs/closed-end funds > open-end > hedge funds > PE. Pooled vehicles: cheaper, but SMAs win on tax, customization, transparency, legal ownership.
- **Fee volatility effect**: performance (incentive) fees reduce the measured volatility of net returns; management fees do not change it.
- **Fee computations**: read the "sharing is based on ..." clause (active vs net-of-base), apply the floor (base) for bonus fees and the cap (max fee). For the HWM variant, only gains in excess of prior unrecouped losses are shared.
- **Capacity questions**: a repeatable structural inefficiency is one where affected assets exceed the AUM of the manager and competitors; a one-off event or gross return equal to costs is not repeatable.

## Key Takeaways
1. Run a three-layer process: define the universe by role and risk (not performance), analyze the quantitative record, then do investment and operational due diligence; none of the layers substitutes for another.
2. Frame every hire/retain/fire as a hypothesis test, state which error costs more, and audit your own process by tracking managers rejected and fired.
3. Beware performance chasing, especially for mean-reverting strategies; short-term results are a weak basis for dismissal when the process and suitability are unchanged.
4. Use style analysis (RBSA top-down, HBSA bottom-up) together and over time; mismatch with the stated philosophy or drift signals unrepeatable or inconsistently executed process.
5. Use capture ratios and drawdown depth/duration to match the manager to the investor's horizon and risk capacity; check whether positive asymmetry is skill or a built-in convex strategy.
6. Demand a clear philosophy tied to a specific behavioral or structural inefficiency with adequate capacity; test the decision process through signal creation, capture, construction (hedges, liquidity) and monitoring.
7. Operational DD is not optional: back office, auditor and service-provider stability, independent risk function, consistent risk reporting, firm economics (breakeven AUM) and compliance culture catch the failures that returns hide.
8. Choose the vehicle on cost vs control, tax, transparency and legal ownership; read liquidity terms (lockups, gates, notice) against the investor's liquidity needs.
9. Prefer fee structures that are close to linear and aligned: understand bonus fees as options on active return that reward added risk, use HWM and caps, and evaluate skill on returns net of fees (and taxes).

## Connects To
- **ch18**: attribution and appraisal outputs (Brinson attribution, information ratio, Sharpe, Sortino, capture ratios, drawdown, benchmark quality) are the quantitative layer of selection.
- **ch15**: active share, tracking risk, information ratio and the fundamental law of active management frame what skill looks like and its capacity limits.
- **ch04**: the IPS and portfolio management process define the role, benchmark and constraints before the search.
- **ch03**: market efficiency determines how large the skilled vs unskilled gap should be and what inefficiency a manager can credibly claim.
- **ch17**: trade strategy and execution (liquidity, market impact, soft dollars) feeds portfolio-construction and operational DD.
- **ch16**: trading costs and electronic markets, relevant to capacity and the cost of liquidity in portfolio construction.
- **`cfasi-portfolio-construction`**: ETF and fund selection (the practical screening of funds and pooled vehicles).
- **`cfa-ethics-gips`**: GIPS (composite and fee-adjusted return presentation, which manager track records rely on) and the Asset Manager Code (fair allocation across fee-paying and non-fee accounts).
- **`cfa-alternative-investments` ch05**: hedge fund strategies, lockups, gates and fee structures (HWM, hurdles).
- **`cfa-wealth-institutional-management` ch04**: institutional investors who run manager searches and monitor managers.
