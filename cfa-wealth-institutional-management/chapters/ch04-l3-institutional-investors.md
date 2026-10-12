# Chapter 4: Portfolio Management for Institutional Investors
> **Source**: CFA Program Curriculum 2023, Level III, Reading 24 · Portfolio Management | Arjan Berkelaar, PhD, CFA; Kate Misic, CFA; Peter C. Stimes, CFA

## Core Idea
Every institution gets its IPS from the same checklist: who the stakeholders are, what the liabilities are, how long the horizon is, how much liquidity is needed, and which legal, tax and accounting rules bind. The answers differ by type. DB pensions run asset-liability (surplus) risk against a PV of benefits. DC plans push investment risk onto members, so the sponsor designs menus and defaults. Endowments and foundations fund a spending rule forever, so they target about 5% real. Sovereign wealth funds (SWFs) have no sharp liabilities, so the type of fund (stabilization, savings, reserve, pension reserve, development) drives everything. Banks and insurers are leveraged intermediaries whose job is to protect equity capital, so risk is measured on the equity of the balance sheet, not on the portfolio alone. Four operating models sit on top: Norway, Endowment, Canada, LDI.

## Learning Outcomes Covered
- discuss the common characteristics of institutional investors (scale, horizon, regulation, governance, principal-agent issues)
- discuss investment policy (IPS) of institutional investors
- discuss stakeholders, liabilities, horizon and liquidity needs of each type
- describe the focus of legal, regulatory, tax and accounting constraints by type
- evaluate risk considerations of private DB plans (funded status, sponsor strength, sponsor-fund interaction, plan design, workforce)
- prepare the investment objectives section of an IPS and evaluate an IPS
- evaluate the portfolio of a private DB plan, SWF, university endowment, private foundation
- describe balance sheet management considerations of banks and insurers

## Frameworks Introduced
- **Five common characteristics of institutional investors**: scale, long horizon, regulatory frameworks, governance framework, principal-agent issues.
  - Scale cuts both ways: small funds (<US$25m) cannot access private equity or real estate minimums and outsource; large funds (>US$10bn) get access and can internalize, but suffer capacity limits, market impact and diseconomies (a 1% venture capital slot is too small to matter).
  - Governance: board sets policy, risk appetite and strategic asset allocation (SAA); investment committee oversees; investment office (CIO plus specialists) implements. Best practice is to delegate manager hiring and firing to staff so the board focuses on policy.
  - Principal-agent: internal agents (committee, staff) and external agents (managers, brokers, consultants, board). A high base fee payable regardless of performance is the standard conflict. Remedy: governance, accountability, fee transparency.
- **IPS content**: mission, return objective, risk tolerance, constraints, asset allocation policy with ranges and benchmarks, rebalancing, implementation guidelines, reporting. Review annually, revise rarely; allocation and guidelines go in an appendix so they are easy to change.
  - Risk tolerance is stated differently by type: DB = surplus volatility; SWF = probability of loss or of not preserving purchasing power; endowment/foundation = total return volatility; bank/insurer = VaR/CVaR plus scenario stress tests.
  - Real return targets need a defined inflation index (GIC: G3 inflation; US endowments: HEPI; Wellcome: average of US and UK CPI).
- **Four investment approaches (Exhibit 1)**:

| Model | Features | Pros | Cons |
|---|---|---|---|
| Norway (GPFG; 60/40 falls here) | Public stocks and bonds, mostly passive, tight tracking error, benchmark as starting point | Cheap, transparent, low manager risk, easy for the board | Little alpha potential |
| Endowment (Yale) | High alternatives, active, externally managed | High value-add potential | Expensive; needs manager access and skill; hard for small funds (no access) and for very large ones (footprint) |
| Canada (CPPIB, NZ Super Fund) | High alternatives, active, mostly internal; reference portfolio plus total portfolio approach | High value-add, builds internal capability | Costly, complex to run |
| LDI | Hedge the liabilities (duration-matched fixed income), plus a return-generating portfolio (growth) | Liabilities explicit in the process | Longevity and inflation risk not hedged |

  - **Canada model details**: *reference portfolio* = passive public equity/bond/cash mix that meets the return objective at the right risk; it is a cheap, risk-equivalent benchmark the board understands (can differ from the SAA). *Total portfolio approach* = keep total risk exposures intact as investments enter or leave. Example: private equity is leveraged equity, so cut public equity by more than the PE allocation and add fixed income to offset the leverage.
  - **LDI split**: hedging portfolio (long-duration bonds, interest rate swaps to extend duration) plus return-generating portfolio (equities, alternatives).
- **DB plan risk-tolerance factors (Exhibit 5)**: higher funded ratio, lower sponsor debt, higher profitability, plan small relative to sponsor, lower correlation of sponsor earnings with plan assets, younger workforce with more active than retired lives = more risk tolerance. Early retirement or lump-sum options shorten liability duration = less risk tolerance.
- **Three funded-status strategies**: (a) match assets to liabilities (LDI, duration gap or cash-flow matching) when near fully funded; (b) grow assets faster than liabilities (more risk) when underfunded or when lowering contributions; (c) go defensive and accept higher contributions for a stable funded ratio. Adequately funded sponsors may transfer risk (lump-sum offers, buyout with an insurer).
- **Endowment spending rule (one formula, three cases)**: `Spend(t+1) = w × Spend(t) × (1 + inflation) + (1 − w) × spending rate × average AUM`. w = 1 constant growth (inflation-indexed amount, usually with 4%-6% caps and floors; ignores asset value); w = 0 market value rule (4%-6% of a 3- to 5-year average AUM; pro-cyclical); 0 < w < 1 hybrid, the Yale rule (w typically 30%-70%).
- **Liquidity risk band** (endowments): `(NAV of illiquids + uncalled commitments) / total AUM`. A breach triggers reduced or stopped commitments, or secondary sales.
- **Balance sheet leverage model for banks and insurers** (equity E, assets A, liabilities L, all at market values): `A = L + E`, so `ΔE/E = (A/E)(ΔA/A) − ((A/E) − 1)(ΔL/L)`. Formulas for equity duration and volatility are below.
  - Three accounting systems apply: financial (GAAP/IFRS, smoothest), statutory (regulator; subtracts intangibles, accelerates costs, so lower earnings and capital; capital rules are built on it), economic/mark-to-market (most volatile, truest).

## Key Concepts
- **Institutional investor**: legal entity investing for groups or individuals across generations: DB/DC pensions (~US$35tn, about half of institutional assets), SWFs (~US$7tn), endowments and foundations (~US$1.6tn), banks and insurers (~US$9tn net financial assets). Pensions went from ~33% to 49% DC in 20 years across the P7 markets.
- **DB plan**: sponsor promises a formula benefit (e.g. final salary x 1.5% x years of service). Sponsor bears investment risk; mortality risk is pooled. **DC plan**: contributions defined, benefit not; member bears investment and longevity risk. Hybrids (Switzerland) blur the line.
- **DB liability drivers (Exhibit 4)**: service/tenure up, salary growth up, matching contributions up, longevity up, lower turnover (more vesting) up, **discount rate up means liabilities down**. Liabilities are the PV of benefits earned to date (IFRS and US GAAP).
- **Funded ratio**: `fair value of plan assets / PV of defined benefit obligations` (called vested benefit index in some countries). Below 100% some regulators force higher contributions.
- **Discount-rate games**: sponsors prefer high rates (lower liabilities, lower contributions); beneficiaries the reverse. US corporates may use 25-year-average high-grade yields (MAP-21 amendment of the PPA); US public plans (GASB) use the expected return on assets, far above bond yields, which pushes them into equities and alternatives. Too aggressive a rate makes contributions inadequate.
- **Accounting hooks**: ASC 715 (US corporate) puts an overfunded plan on the balance sheet as an asset, an underfunded plan as a liability, and runs gains, losses and service cost through net income. It pushed corporates into LDI. GASB (US public) blends: funded part at expected return, unfunded part at the muni bond yield.
- **Pension risk factors**: sponsor stock in the plan is dangerous (the stock falls when the sponsor weakens and contributions are needed), also industry peers; poor plan design (optimism on contributions; used as a retention or labor-peace tool); workforce (younger = longer asset duration; older = liquidity; long tenure = more vested liabilities).
- **DC specifics**: sponsor fiduciary duty (menu, administrators, education, default option, QDIA in the US, MySuper in Australia, mandated lifecycle default in Hong Kong). Life-cycle options: participant-switching (de-risk as age rises) and cohort/target-date (glide path, e.g. 90/10 equity/bonds at 25 years out). DC pooled into alternatives creates sponsor liquidity risk if many members exit.
- **Pension liquidity needs** rise with: share of retirees, workforce age, a well-funded plan (sponsor cuts contributions), ability of members to switch or withdraw. Frozen plans (negative cash flow) need the most.
- **Taxes on pensions**: contributions and earnings deferred, benefits taxed (US 401(k): 10% extra tax before 59.5; UK: first 25% tax free). Taxed plans must watch derivative income vs capital gains, long-term gains incentives, double taxation (use treaty-eligible structures; foreign tax credit).
- **SWF types (IMF)**: budget stabilization (Chile, Russia oil fund), development (Mubadala, Khazanah), savings (ADIA, KIA, QIA, Alaska Permanent Fund), reserve (CIC, KIC, GIC), pension reserve (NZ Super, Future Fund of Australia, China NSSF). Norway GPFG is a mix. Liabilities are not clearly defined, unlike other institutions.
- **Santiago Principles (GAPP)**: self-regulation by IFSWF members: legal framework, mission, independence, accountability, transparency, risk management, regular review. SWFs are usually tax free at home but may not claim withholding credits abroad.
- **Reserve fund logic**: central banks buy FX with local currency and sterilize via monetary stabilization bonds that cost more than the low-yield FX reserves earn (negative carry). The reserve fund invests the excess for a higher return than the bond cost.
- **Endowment**: perpetual, intergenerational equity (Tobin: "guardians of the future against the claims of the present"). Gifts may be restricted or unrestricted. Headline spending 4%-6%, net spending 2%-4% after gifts. **Private foundation**: grant maker; four types (community, operating, corporate, private grant-making; the latter is the largest group). US private foundations must pay out 5% of assets (trailing 12 months) plus investment expenses is the model; failing the 5% means a 30% tax on undistributed income; typically 2% excise tax on net investment income; donations must be spent in the year received (flow-through).
- **Limited-life foundation** (Gates: spend down within 30 years of the founders' deaths; Atlantic Philanthropies closed about 2020): as the horizon shortens, liquidity needs rise and risk tolerance falls.
- **Mission-related (impact) investing**: lower-yielding investments reduce portfolio return and the grants that can be funded (Ford: up to US$1bn, 8%+ of assets over ten years).
- **Outsourced CIO**: used by small foundations (investment office is a cost center inside the 5%); tends to mean more public markets, more passive, more beta.
- **Bank balance sheet**: loans up to 50% or more of assets, debt securities 25%+; deposits more than half of liabilities; long-term debt 10%-15%; repo and trading payables 10%-20%. Time deposits: amount and timing known. Demand deposits: amount known, timing uncertain (treated as short). Perpetual horizon but short-maturity instruments.
- **Liquidity regulation for banks**: LCR (liquid assets over 100% of highly probable near-term outflows), NSFR (stable funding vs assets). Retail banks have cheaper, more stable funding than commercial (wholesale-funded) banks.
- **Insurers**: life (long liabilities, 20-40 year objectives; term life predictable, annuities carry longevity risk and shorter duration) vs P&C (short, uncertain liabilities; catastrophe risk; large cash and short fixed income). Stock vs mutual (policyholder-owned, less access to capital markets). General account (company bears risk: whole, term, universal life, fixed annuity) vs separate account (policyholder bears risk: variable life, variable annuity).
- **Insurer portfolio split**: reserve portfolio (statutory size, liquid, low risk) vs surplus portfolio (higher return; may hold private equity, hedge funds, non-security assets). Liquidity plan: internal (cash, investment income, maturities) and external (bond issuance, credit lines, repo). Rising rates cause surrenders and cash outflows.
- **SIFIs and regulation**: economies of scale via the law of large numbers concentrate the industry in a few large institutions. Post-2008 rules: higher capital, limits on payouts, tighter derivative and proprietary trading rules, stress tests, more disclosure. Basel III/CRD IV (banks), Solvency II (EU insurers), NAIC and state regulators (US insurers), Dodd-Frank/Volcker, FATCA, UCITS V, AIFMD, MiFID II, EMIR. Pensions: ERISA/PPA/PBGC (US), IORP II (EU), SIS Act (Australia), UPMIFA/UPIA (endowments, US), Trustee Act 2000 (UK).
- **Tax status**: pensions tax-favored, SWFs tax free (home), endowments and foundations tax exempt (gifts deductible, income and gains exempt, payouts exempt if to an exempt recipient), banks and insurers taxable entities (manage after-tax, gain/loss timing).

## Formulas & Reference Tables
Funded ratio: `FR = fair value of plan assets / PV of DB obligations`. Surplus = assets − PV(liabilities); surplus volatility is the DB risk measure.

Endowment spending: `S(t+1) = w · S(t)(1 + π) + (1 − w) · s · AUM_avg`. With w = 0.8, prior spend 10.0, π = 2%, s = 5%, average AUM 250: 0.8 × 10.0 × 1.02 + 0.2 × 0.05 × 250 = 8.16 + 2.50 = **10.66**.

Real return needed: `r_real ≈ r_nominal − inflation ≥ spending rate (+ expenses)`. Rule of thumb: 5%-5.5% real for endowments, 5% real plus expenses for foundations, volatility target 10%-15%. MIT: 3% inflation + 5% spending means about 8% nominal.

Bank/insurer equity impact (market values):
- `ΔE/E = (A/E)(ΔA/A) − ((A/E) − 1)(ΔL/L)`
- Asset shock: ΔE/E = (A/E) × ΔA/A. E/A 10% and assets −1% gives −10%; E/A 5% and −1% gives −20%.
- Liability shock: ΔE/E = −((A/E) − 1) × ΔL/L. E/A 10% and liabilities +1% gives −9%.
- **Equity duration**: `D*_E = (A/E) D*_A − ((A/E) − 1) D*_L (Δi/Δy)`. Equity value change ≈ −D*_E × Δy.
- **Equity volatility**: `σ²_E/E = (A/E)² σ²_A + ((A/E) − 1)² σ²_L − 2 (A/E)((A/E) − 1) ρ σ_A σ_L` (the extraction drops the minus sign on the correlation term; it is minus, which is why higher ρ lowers equity volatility).
  - Leverage 5x with σ_A = σ_L = 1.5%: ρ = 0.5 gives 6.9%, ρ = 0.9 gives about 3.4% (source text says 3.5%). E/A 5%: ρ = 0.5 gives 29.3%; ρ = 0.9 gives 13.2%.
  - Duration facts: zero-coupon modified duration = maturity / (1 + y); a 10-year zero is about 9.75 (±100 bp is ±10%). With E/A 10%, liability duration about 0 and asset duration only 2.5, equity duration reaches 25 (±100 bp is ±25%): borrowing short and lending long is dangerous.

Comparison of institutional investor types:

| Type | Objective | Risk measure / tolerance | Horizon | Liquidity need | Legal, tax | Typical allocation |
|---|---|---|---|---|---|---|
| DB pension | Return above liability discount rate (funded ratio at least 100%); secondary: minimize PV of contributions | Surplus volatility; higher when overfunded, sponsor strong, young workforce | Depends on maturity (retiree share) | Medium; high if mature or frozen | ERISA/PPA, ASC 715, PBGC; tax-deferred plan | Equities (about 46% for P7 in 2017, from 57% in 1997), bonds for hedging, "other" alternatives 25% (from 4%); more LDI as funding improves |
| DC pension | Grow member assets for retirement; sensible default | Member-level (age, balance, risk appetite) | Per member: now to death of last spouse | Lifecycle; rises as members near retirement; exits | Fiduciary duty, default option rules | Menu plus default; balanced or target-date; Australia and US the highest equity shares |
| University endowment | Real return at least 5% (spend plus inflation), perpetuity | Volatility 10%-15%; higher if endowment funds a small share of the budget, can issue debt, gift inflows | Perpetual | Low (net spend 2%-4%); capital calls | UPMIFA/UPIA (total return, prudence); tax exempt | Large endowments (>US$1bn): alternatives 57% in FY2017 (32% in FY2002), public equity 32% (45%), fixed income 7% (21%); small ones: US equity heavy, home bias |
| Private foundation | Real return at least 5% plus expenses | Similar to endowment but a single revenue source: more conservative and liquid on average | Perpetual (limited-life exceptions) | Low but higher than endowment (5% payout, grants committed) | 5% payout, 30% penalty tax, 2% excise tax; tax exempt | Largest private foundations (>US$500m) about half in alternatives; smaller ones more US equity; more outsourced CIO and beta |
| SWF: budget stabilization | Capital preservation, real return with low chance of annual loss | Very low | Short | Highest | National legislation; tax free at home | Mostly bonds and cash; avoids assets correlated with budget revenue (commodities) |
| SWF: savings | Preserve purchasing power in perpetuity; fund spending (GPFG 3%) | High | Very long | Low (changes when resources deplete) | Santiago Principles | Growth tilt: equities plus real assets, private equity and debt, hedge funds |
| SWF: reserve | Earn more than the cost of monetary stabilization bonds (negative carry) | Medium-high | Long, no interim payout | Between stabilization and savings | Same | 50%-70% equity or equity-like, rest liquid fixed income; fewer alternatives than savings funds |
| SWF: pension reserve | CPI plus 4%-5% (Future Fund); meet contingent pension and health costs | High in accumulation | Long; phases: accumulate, then decumulate | Low then rising, e.g. about 5% of assets a year from 2030 | Same | Heavy equities plus alternatives (infrastructure, property, private markets, hedge funds); shift to liquid high-quality bonds in decumulation |
| SWF: development | Raise real GDP growth, diversify the economy | Mandate driven | Project dependent | Low (infrastructure, R&D) | Mandate may force 100% local or offshore | No typical allocation (limited universe) |
| Bank | Maximize NPV of shareholder capital; protect capital and liquidity | VaR/CVaR, stress tests, regulatory capital; equity duration | Perpetual institution, short instruments | Core: LCR/NSFR; high-quality liquid securities | Basel III, statutory accounting, taxable | Loans 50%+, debt securities 25%+, cash, central bank deposits; short or floating |
| Insurer | Fund claims, grow surplus; maximize NPV of capital | VaR/CVaR, risk-based capital, rating agencies | Life 20-40 yrs; P&C shorter | P&C high; life depends on surrender risk | Solvency II, NAIC, statutory; taxable (after-tax decisions) | Reserve: liquid high-quality fixed income (statutory). Surplus: credit, private placements, real estate, private equity. P&C: cash and short bonds |

Rule: shorter horizon, higher liquidity need and tighter regulation push to bonds and cash; long horizon, low liquidity need and high risk tolerance push to equities, private markets and real assets.

Pension approximations by country (2017 split DB/hybrid vs DC): Australia nearly all DC, Canada mostly DB; P7 hold more than 80% of world pension assets.

## Mental Models
- Ask in order: **who bears the risk?** (sponsor, member, taxpayer, citizen, shareholder), **what is owed and when?** (liabilities and horizon), **how fast can cash be needed?** (liquidity), **what do the rules forbid or reward?** (constraints). Objectives follow.
- For DB plans, think surplus not assets: assets can rise and the plan still gets worse if the discount rate falls. Hedge the rate risk (LDI) when funded; take growth risk only if the sponsor can fund the downside.
- For endowments, the spending rate is the liability. Check expected real return vs spending rate before debating asset mix: Ivy at 20/80 earns 3% nominal, 1% real, against 5% spending, a slow loss of purchasing power.
- Prefer the model your organization can run: the endowment model needs skill, access, staff and fee budget. A copycat allocation (peer benchmarking, herding) ignores your own liability traits.
- For banks and insurers, leverage amplifies everything: a 1% asset move equals a 10% equity move at 10% capital. Capital, correlation of assets and liabilities, and duration matching work together; high correlation breaks in stress, so it never replaces capital.
- Regulation and accounting shape behavior: high discount-rate rules push public pensions into risk; mark-to-market ASC 715 pushed corporates to LDI; risk-based capital charges push insurers toward sovereigns.
- Time is a state variable: frozen DB plans, limited-life foundations, and pension reserve funds entering decumulation all move toward liquid, lower-risk assets as the horizon shortens.

## Worked Example
**1. DB vs DC (Geoff, Example 1).** DB (1.5% x years x final 3-year average salary): payout set by formula; employer contributes and bears shortfall; longevity pooled. DC (15% of salary): benefit unknown, Geoff bears investment and longevity risk, can top up contributions. Vested DB benefits may be transferred into the DC plan.

**2. DB risk tolerance (Andes, Example 2).** Young firm with no retirees, EUR100m assets, EUR8m surplus (8% of assets), low debt, profitable but cyclical, workforce age 39, liability duration 20 years. Above average risk tolerance. Risk objective: shortfall risk on funded status (e.g. P(FR below 100%) at most 10%) or minimize PV of expected contributions. Contrast Antiliaro (Q14): EUR100m deficit on EUR1bn, more debt, no growth, average age 50, many retirees, high correlation of sponsor and plan: below average on at least two grounds (underfunded plus weak sponsor; liquidity from age; high correlation).

**3. Public plan alternatives (Example 3).** LSPP 30/30/30/10 with expected real returns of 4.0, 5.0, 1.0, −0.5 shifts 25% to alternative debt, infrastructure, hedge funds (10% each). Expected returns rise, so the actuarial discount rate can go up, lowering liability PV; funded status improves. Cost: illiquidity, manager dispersion, higher fees and staff cost. A higher discount rate is a cosmetic gain: the assets must really earn it.

**4. SWF phases (People's Fund, Example 4).** Payouts of about 5% of assets from 2030. Before: very low liquidity needs, so heavy alternatives are fine. After: liquidity, horizon and risk tolerance change. 2030 is not an end date, but the policy must be reviewed for the two phases.

**5. Ivy Endowment (Examples 5 and 6; recomputed).** US$250m, supports 40% of the budget, spends 5% of a 3-year average, inflation 2%. Objective: real total return of at least 5% over HEPI (net of fees), volatility at most 15%. Current 20% US equities/80% Treasuries: 0.2 x 7% + 0.8 x 2% = 3.0% nominal, 1.0% real: far below the 5%. Two feasible mixes: (I) 40% US active equity (7.5%), 40% non-US active (8.5%), 10% Treasuries, 10% hedge funds: 7.1% nominal, 5.1% real. (II) 50% US passive (7%), 30% non-US active (8.5%), 10% Treasuries (2%), 10% private equity (10%): 7.25% nominal, 5.25% real. The new CIO's 30% PE/30% hedge funds/30% public equity/10% bonds gives 7.1% nominal, 5.1% real, but 60% in alternatives with a four-person team and limited manager access: **reject**. The same return is available with far less complexity.

**6. Wolf Endowment (Q6-7).** US$200m, 4% of 3-year average, supports 10% of the budget, debt access, strong gifts: above-average risk tolerance. Expected nominal returns (4.1, 6.3, 7.5, 5.0, 9.1%): Allocation 1 (45/40/10/0/5) = 5.57%, real 3.07% (below 4%: fails). Allocation 2 (10/15/15/30/30) = 6.71%, real 4.21%, but 60% alternatives. Allocation 3 (13/32/40/5/10) = 6.71%, real 4.21%, 15% alternatives: **choose Allocation 3** for a small staff and limited access. Prometheo (Q16): 0.6 x 7.4% + 0.4 x 4.0% = 6.04% nominal, 3.54% real vs a 6% spending policy: unsustainable; the 60% alternatives (20% PE plus 40% hedge funds) proposal with four staff is also rejected.

**7. MegaWorld Bancorp (Example 7; verified).** E/A = 9%, D*_A = 2.0, D*_L = 1.5, Δi/Δy = 0.85. A/E = 11.11: D*_E = 11.11 x 2.0 − 10.11 x 1.5 x 0.85 = **9.33**; +50 bp gives −4.67% in equity. At E/A = 10%: 10 x 2.0 − 9 x 1.5 x 0.85 = **8.53**. Then with D*_A = 1.75: **6.03**. Q18 (Meura): E/A 10%, D*_A 2.10, D*_L 1.90, 0.65: 21.0 − 11.115 = **9.89**.

**8. Foresight International Assurance (Example 8; verified).** σ_A = 5%, σ_L = 2.5%, ρ = 0.25, E/A 20% (A/E = 5): variance = 25 x 0.0025 + 16 x 0.000625 − 2 x 5 x 4 x 0.25 x 0.05 x 0.025 = 0.0625 + 0.01 − 0.0125 = 0.06, σ_E = **24.5%**. Raise E/A to 25% (A/E = 4): variance 0.038125, **19.5%**. Then σ_A = 4%: variance 0.025225, **15.9%**. EPS falls (more shares, lower asset yield), but risk and the cost of capital fall too, so the share price effect is not determinable from earnings alone.

**9. Mini-cases (Example 9).** (A) Sell floating small-business loans, buy fully hedged fixed-rate governments: duration profile roughly unchanged, equity volatility lower (liquidity, less credit spread risk), earnings lower; justified by liquidity needs, a higher regulatory capital ratio, or a plan to reverse after a recession widens loan spreads. (B) Insurer swaps IG securities for an auto-loan trust: liquidity lower, regulatory capital charge higher (so it must have excess capital), earnings higher, equity volatility higher, needs actuarial prepayment and default projections. (C) Sell financial-sector floaters (MRR + 0.1%) for diversified fixed-rate bonds (T + 1.0%) plus pay-fixed swap (pay T + 0.4%, receive MRR): net MRR + 0.6%, duration neutral, better diversification away from systemic financial risk, little capital impact. (D) Life insurer buys corporate and ABS, expecting rates to rise: shorter duration, less liquidity and a higher capital charge (only if capital is ample), more earnings; hedge the surrender risk with out-of-the-money puts or payer swaptions.

**10. Funded-ratio sensitivity (illustrative).** Assets 100, liabilities 92: FR 108.7%. Falling discount rate raises the PV of long liabilities; with liability duration 20 a 100 bp fall raises liabilities about 20%, to roughly 110, taking FR to about 91%. This is why DB plans extend asset duration.

## Anti-patterns
- **Copying a peer or the Yale mix without the staff, access or liquidity**: Ivy with 60% alternatives and four people. Check against own liabilities, not peer rankings (herding).
- **Setting a return target off a government-yield discount rate**: too low; hedge the liabilities with LDI instead.
- **Using a high discount rate to look funded** (public plans on expected return): cosmetic funded status, too-low contributions, extra risk to defend the assumption.
- **Holding sponsor stock or same-industry stocks in a corporate DB plan**: plan assets and sponsor strength fall together.
- **Treating illiquid alternatives as free of liquidity cost**: capital calls, derivative margin and a 2008-style drawdown forced endowments to sell secondaries, cut payouts, or issue bonds. Use cash flow models, a liquidity band and stress tests.
- **Ignoring liability differences inside a peer group**: an endowment funding 40%-50% of the budget cannot take the risk of one funding 5%.
- **Setting the objective in nominal terms without naming the inflation index** (HEPI, CPI, G3).
- **Letting a limited-life foundation or maturing DB plan keep a perpetual-horizon portfolio**: horizon shrinks, liquidity needs rise.
- **Banks "borrowing short, lending long" with thin capital**: E/A 10%, liability duration about 0, asset duration 2.5 gives equity duration 25.
- **Relying on asset-liability correlation instead of capital**: correlation breaks in stress and equity volatility spikes, especially at high leverage.
- **Judging a bank or insurer on earnings alone**: capital raises lower EPS but can raise value by cutting risk and the cost of capital.
- **Board micromanaging manager hiring and firing**: delegate to staff and keep board time for policy.
- **High base fees with weak performance incentives** (principal-agent): negotiate transparency and alignment.

## Exam Focus & Traps
- Lower employee turnover means more vesting, higher liabilities, lower funded ratio (Q1). Overfunded corporate plan is an asset on the sponsor's balance sheet (ASC 715) and benefits shareholders.
- Small plan size (US$25m) means outsourcing (scale), but outsourcing does not remove regulation or eliminate principal-agent conflict; it only brings access (Q2).
- Model identification: high alternatives plus active plus outsourced is the Endowment model; same but insourced is Canada; mostly public passive and tight tracking error is Norway; liabilities-first is LDI.
- Risk tolerance is above average for the plan with: overfunded status, small plan relative to sponsor, low correlation of sponsor and plan, younger workforce (Q4). Below average for underfunded plans with weak sponsors, older workers, high correlation, early retirement or lump-sum options.
- Endowment risk tolerance rises with debt market access, a small share of the university budget, significant gifts (Q6). Gifts lower net spending below the headline spending rate.
- Compare **real** expected return with the spending rate: nominal return minus inflation, versus spending (Q7, Q16). Then check feasibility (staff, access, size) before picking the highest return.
- Liquidity ranking for SWFs: stabilization (highest) > reserve > pension reserve (rising in decumulation) > savings (lowest). Development funds depend on projects.
- Foundations: 5% payout is **in addition to** investment expenses in the model; US donations are flow-through; endowments are not legally forced to pay 5%. Foundations have higher liquidity needs than endowments.
- Equity duration formula: **(A/E) D_A minus ((A/E) − 1) D_L x (Δi/Δy)**. A/E = 1 / (equity ratio). Do not use E/A directly. Lower leverage lowers D_E; shortening asset duration lowers it more.
- Equity volatility: the correlation term is **subtracted**. Raising capital ratio and cutting σ_A both lower equity volatility; ρ near +1 minimizes it.
- Mini-case logic: more illiquid or higher-credit-risk assets mean a higher regulatory capital charge and require ample capital; sovereign and plain-vanilla swaps are capital friendly; hedging fully gives a synthetic floater.
- Exposure to equity or common stock gets 100%+ risk weights, so it rarely backs liabilities at banks and insurers.
- Surrender penalties and prepayment penalties raise correlation of assets and liabilities (reduce liability or asset shocks). Variable annuities move risk to the policyholder: correlation approaches 1.0 in the separate account.
- ⚠ **Correction**: the source's discussion of Exhibit 26 states equity volatility of 3.5% for 20% equity ratio and ρ = 0.9; recomputing the formula gives 3.35% (about 3.4%). The 6.9%, 29.3% and 13.2% figures check out. The extracted text of Equation 9 loses the minus sign before the covariance term; Examples 8 and Q18 confirm the minus sign. The source also states pension equity share 57% to 46% (1997-2017) and "Other" 4% to 25%; these are chart readings and approximate.

## Key Takeaways
1. Build every institutional IPS from stakeholders, liabilities, horizon, liquidity, constraints; then state the return objective against the liability (discount rate, spending rate, or funding cost) and the risk measure that fits the type.
2. DB plans: manage surplus, not assets. Funded status, sponsor strength, sponsor-fund correlation, plan design and workforce set risk tolerance; LDI hedges rate risk once funded.
3. DC plans: members bear risk, sponsor owns the menu and default; lifecycle and target-date options handle horizon.
4. Endowments and foundations fund spending in perpetuity: target about 5% real, test expected real return against spending, use a smoothed spending rule (w x inflated prior spend plus (1 − w) x rate x average AUM), and manage illiquidity with a liquidity band.
5. SWF type dictates policy: stabilization (liquid, bonds), reserve (50%-70% equities, liquid remainder), savings and pension reserve (growth and alternatives), development (mandate). Governance follows the Santiago Principles.
6. Banks and insurers run balance sheet LDI: leverage magnifies asset and liability moves; control equity duration, asset-liability correlation, liquidity, and capital; regulation (Basel III, Solvency II, LCR/NSFR, statutory accounting) sets the frame.
7. Choose the investment model by capability: Norway (cheap, passive), Endowment (outsourced alternatives), Canada (reference and total portfolio, internal), LDI (liability hedging). Scale, staff and access decide feasibility.
8. Horizon shifts (maturing plans, limited-life foundations, decumulating funds) require shifting toward liquid, lower-risk assets.

## Connects To
- **ch01-ch02**: private wealth IPS and tax treatment; institutions are mostly tax exempt or tax deferred, unlike taxable individuals (ch02).
- **ch03**: risk management for individuals: human capital and longevity risk pooled in DB plans and annuities, borne by the member in DC plans.
- **ch05**: endowment case applying the spending rule, liquidity band and endowment model; **ch07**: SWF (savings fund) risk case with direct investments.
- **`cfa-fixed-income` ch13**: liability-driven investing (duration matching, cash flow matching, immunization), the hedging portfolio of the LDI model and of bank/insurer balance sheet management.
- **`cfa-asset-allocation-cme` ch07**: asset allocation with liabilities and surplus optimization (ALM), plus the real-world constraints (liquidity, regulation, time horizon) that shape institutional policy portfolios.
- **`cfa-asset-allocation-cme` ch01-02**: behavioral issues, such as herding on peer-group benchmarks.
- **`cfa-alternative-investments`**: illiquidity, fees, manager selection and capital-call risk behind the endowment and Canada models.
