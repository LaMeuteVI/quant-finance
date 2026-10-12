# Patterns — Portfolio Construction (Asset Allocation, Passive, Fund Selection, Alternatives, ESG)

## Classify the Investor, Then Set the Policy
**When to use**: first meeting with any institution or client (ch01, ch02, ch04).
**How**: 1) Liabilities contractual? Liability-driven (ALM). 2) Free of liabilities? Asset-only. 3) Personal goals? Goal-based. 4) Write the IPS: objectives, constraints, horizon, benchmark, rebalancing. 5) For individuals take the lower of ability and willingness to bear risk.
**Trade-offs**: a wrong class mis-prices shortfall risk; the questionnaire doubles as bias detector. (ch02, ch04)

## Behaviourally Modified Allocation
**When to use**: client behaviour diverges from the rational portfolio (ch04).
**How**: 1) Classify biases as cognitive or emotional. 2) Moderate cognitive ones, adapt to emotional. 3) Allowed deviation per asset: high wealth/savings +/-5-10% (cognitive), +/-10-15% (emotional); low wealth +/-3-5% and +/-5-10%. 4) Layer by goal buckets and rebalance against goal funding. 5) Report TWRR and MWRR.
**Trade-offs**: bands are guidance only; compromise costs expected return but keeps the plan held. (ch04)

## Rebalancing Rule Selection
**When to use**: writing the rebalancing policy (ch02, ch03).
**How**: calendar (simple, low turnover) when monitoring is thin; tolerance bands (e.g. 18-22% around 20%) when volatility is high. Narrow bands for low costs, volatile holdings; wide for high risk tolerance or high correlation with the rest. CPPI when a floor is mandatory: E = m × (V − F), cap at V.
**Trade-offs**: bands trade more in crashes; CPPI loses in sideways markets and gaps below the floor if the market falls more than 1/m between rebalances. (ch02, ch03)

## Benchmark Validity Check
**When to use**: before mandating or judging a fund (ch03).
**How**: test the seven properties; for multi-asset funds build a composite from investable indices; state the index in all reporting; fix it before the evaluation period.
**Trade-offs**: index choice alone can swing annual returns by several points (Japan 1999: +78% vs +67%). (ch03)

## Risk-Parity Diagnosis
**When to use**: a 60/40 mix is sold as balanced (ch01, ch03).
**How**: compute risk contribution w_i(Σw)_i/σ_p; equity vol 15%, bond 5%, corr 0.2 gives 91.8% equity risk. Equalise contributions; naive weights 1/σ.
**Trade-offs**: needs leverage on low-risk assets and past volatilities. (ch03)

## Passive Instrument Due Diligence (TCO)
**When to use**: choosing between ETFs or index funds on similar exposure (ch06, ch07, ch12).
**How**: 1) Benchmark and weighting rules. 2) Tax and domicile (harmonised UCITS for Italy; Irish for US equity; accumulating for long taxable horizons). 3) TCO = TER + sampling + turnover + swap fee + tax drag − lending income, plus spread, commission, impact. 4) Compare 3-5 year tracking difference on official NAV, then TEV. 5) Replication, lending policy, counterparties, voting. 6) Execute when the underlying market is open, away from open/close.
**Trade-offs**: TD is backward looking; synthetic hides cost in the swap; holding horizon sets whether internal or external costs dominate. (ch06, ch07, ch12)

## Replication Method Choice
**When to use**: understanding what the ETF manager actually does (ch07).
**How**: few liquid names, full replication; many names, minimise TE with optimized sampling or TCO with stratified; illiquid or high-turnover index, synthetic (prefer unfunded, diversified counterparties, daily reset, collateral above 100%).
**Trade-offs**: optimised inputs can be unstable; synthetic adds counterparty risk and no votes. (ch07)

## Securities-Lending Review
**When to use**: lending income is part of the pitch (ch06, ch07).
**How**: check percentage lent, borrower credit, collateral and reinvestment, indemnity, agent split, recall rights; treat income as uncertain.
**Trade-offs**: offset reaches about 90% in small-cap ETFs, little in large caps; voting lost on lent shares. (ch07)

## Factor ETF Selection
**When to use**: buying smart beta or multi-factor exposure (ch08).
**How**: confirm a genuine factor (persistent, broad, grounded, a full cycle, investable); read loadings with a factor profile; mix factors with complementary cycles (value-quality −35%); avoid timing; compare TER with plain cap-weighted.
**Trade-offs**: factors lag 2-3 years; timing gain of 95 bp gross fell to 4 bp net on turnover 4.8. (ch08)

## Add-an-Asset-Class Test
**When to use**: justifying a manager or sleeve for diversification (ch09).
**How**: add if SR_new > ρ × SR_portfolio; with SR_p = 0.50 and ρ = 0.4 hurdle is 0.20. Confirm correlation across market phases and net of fees.
**Trade-offs**: correlation rises in crises; fee layers erode the gain. (ch09)

## Active-or-Passive Per Sleeve
**When to use**: setting where to spend research budget (ch10, ch11).
**How**: read the barometer success rate by category (below 25% over 10 years, default passive); active only where inefficiency or a niche exists; compute FAR = fee / TEV at fund and portfolio level; use cost as first screen.
**Trade-offs**: passive tends to sit in the second quartile; hybrids (smart beta, research-enhanced) need net-of-fee evidence. (ch10, ch11)

## Four-Phase Manager Selection
**When to use**: any fund hire, active or passive (ch11, ch14).
**How**: I plan from the IPS (role, constraints, odds); II screen on operational, performance, portfolio data with cost first; III due diligence on five Ps; IV manage outcome with a written thesis and kill criteria, review on events.
**Trade-offs**: screening data are weakly predictive except fees; investor timing destroys more value than selection. (ch11)

## Pramerica Quant-to-Portfolio Workflow
**When to use**: running a fund-of-funds shortlist (ch14).
**How**: clean daily NAV; peer-group quartile incidence and share of negative periods; Quantsheet (beta up/down, rolling R² and TE, IR, drawdown); qualitative DD; Quant Ranking Score; combine score-weighted, risk parity and Z-score solutions into a plateau portfolio.
**Trade-offs**: three annual observations are thin; alternatives need premia classification and correlation heat maps. (ch14)

## Multimanager Optimisation in Active-Risk Space
**When to use**: combining several active managers and index funds (ch13).
**How**: regress to the natural benchmark; pure alpha and pure active risk; PIR; optimise weights by alpha per unit risk with index at origin; risk aversion picks the point. Example: 51% ETF/26% enhanced/23% active gives alpha 1.44 at risk 0.43.
**Trade-offs**: alpha forecast decisive; if you cannot defend it hold the index. (ch13)

## Alternatives Perimeter and Vehicle Match
**When to use**: proposing an alternative to a client (ch15, ch16, ch19).
**How**: UCITS or AIF; marketing route (professional notification, retail Consob authorisation, EUR 500,000 ticket); target-market check; match vehicle liquidity to the underlying (daily liquidity UCITS; closed funds with secondary exit; listed vehicle accepting NAV discount; feeder with extra fee layer).
**Trade-offs**: regulatory perimeter often decides before suitability. (ch16, ch19)

## Private Fund Performance and Funding Review
**When to use**: evaluating a private-capital track record or programme (ch17).
**How**: IRR with TVPI/DPI/RVPI by vintage; KS-PME and Direct Alpha vs index; Yale projection with RC, RD, g; monitor overcommitment 105-115% and outstanding commitment level; stress the denominator.
**Trade-offs**: IRR inflated by short deals; valuation lag 1-6 months. (ch17)

## Secondary Pricing
**When to use**: exiting or buying an LP stake (ch18).
**How**: price = % of NAV; cash = %NAV × NAV + calls − distributions after the NAV date; intrinsic value by modified bottom-up discounting at required return; managed auction with two bid rounds and GP consent.
**Trade-offs**: bid-ask gaps from information asymmetry and loss aversion; prices cycle (high 50s-70s % in 2008-09, mid 90s by 2016). (ch18)

## ESG Fund Selection
**When to use**: choosing or auditing an ESG fund (ch23, ch24).
**How**: objectives; GSIA strategy label; fund DD (exclusions, voting, factors, compensation); benchmark (exclusion, inclusion or over/underweight; more ESG content means more tracking error); two rating agencies; ESG momentum; overlay for few conflicting names.
**Trade-offs**: index mandates are semi-passive; ratings reward disclosure volume. (ch23, ch24)

## Impact Report Build
**When to use**: showing what a portfolio contributes (ch27).
**How**: reference market proxy; indicators distinct from selection ones; map to E/S/G and SDG; keep at least 70% coverage; delta = (a − b)/b; add WACI, attributable emissions and footprint.
**Trade-offs**: absolute emissions reflect size; sector tilts distort. (ch27)

## ESG Engagement Cycle
**When to use**: running stewardship (ch30).
**How**: public policy; annual plan by E, S, G linked to SDGs and science-based asks; select targets; dialogue and voting, collaborative where possible; scored evaluation; public report; escalation thresholds.
**Trade-offs**: evidence is observational with modest significance. (ch30)

## Materiality-Led ESG Valuation
**When to use**: combining ESG with value or small-company disclosure (ch25, ch26).
**How**: SASB material variables per sector; weight pillars by relevance; combine value rank and ESG rank; adjust intrinsic value for governance findings; SMEs report on one recognised standard.
**Trade-offs**: one-pillar strength does not offset weakness elsewhere; sample short. (ch25, ch26)
