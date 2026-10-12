# Chapter 2: Real Estate Investments
> **Source**: CFA Program Curriculum 2022, Level II, Reading 35 · Alternative Investments | Steven G. Bloom, Jeffrey D. Fisher, David Kruth, Bryan D. MacGregor, Ian Rossa O'Reilly, Anthony Paolone

## Core Idea
Real estate is a bond-like (lease income) and stock-like (rollover, supply/demand, leverage) asset that cannot be priced from a screen. Private property is valued by **appraisal**: income approach (direct capitalization or DCF), cost approach, sales comparison. Listed vehicles (REITs, REOCs) are valued with **NAVPS**, **P/FFO and P/AFFO**, and dividend discount models. The recurring discipline: value comes from **NOI, the cap rate and growth** (`cap rate = discount rate - growth`); financing changes the equity return and risk, not the property's value; and appraisal-based data smooth volatility and understate correlation, which inflates the allocation to private real estate.

## Learning Outcomes Covered
- Compare characteristics, classifications, principal risks and basic forms (four quadrants) of public and private real estate.
- Explain portfolio roles and economic value drivers; discuss commercial property types and lease structures.
- Explain due diligence for private and public equity real estate.
- Discuss real estate indexes (appraisal-based, repeat-sales, hedonic, securities) and their biases.
- Compare income, cost and sales comparison approaches; compare direct capitalization and DCF.
- Estimate inputs (NOI, cap rate, discount rate, terminal cap rate) and compute property value.
- Calculate and interpret LTV, DSCR, equity dividend rate, leveraged and unleveraged IRR.
- Discuss REIT types; estimate NAVPS; use FFO/AFFO, P/FFO, P/AFFO and DCF to value a REIT share.
- Compare public vs. private real estate.

## Frameworks Introduced
- **Four-quadrant map of real estate investment**: crosses market (public/private) with capital position (equity/debt).
  | | Public | Private |
  |---|---|---|
  | **Equity** | REIT/REOC shares, listed trusts, ETFs | Direct ownership, joint ventures, LPs/commingled funds, private REITs |
  | **Debt** | Mortgage REITs, CMBS/RMBS, unsecured REIT debt | Mortgages, private debt, bank debt |
  - When to use: pick the form that matches liquidity, control, expertise and risk needs. Equity = income + appreciation (residual claim). Debt = contractual cash flows, priority claim on the collateral, no share of appreciation, bond-like and rate-sensitive.

- **Core vs. non-core strategy**: **core** = high-quality, well-leased office, retail, industrial/warehouse, multi-family in large diversified markets, leverage at most 30% of asset value (avoids leasing, development and speculation risk). Hotels, senior housing, self-storage, data centers, towers and other specialty uses are non-core (less substitutable space, more operating risk). Development is the riskiest.

- **Return profile by risk (expected)**: bonds < core private real estate < stocks, because leases are bond-like but renewal, vacancy, and re-leasing are stock-like. More leverage, development or management intensity pushes expected return and volatility up.

- **Three valuation approaches (triangulate, then reconcile)**
  1. **Income**: PV of expected cash flows at a risk-appropriate rate. Direct capitalization and DCF.
  2. **Cost**: land + replacement cost of building (incl. developer's profit) - depreciation/deterioration - obsolescence (functional, locational, economic). Best for new or special-purpose property with few comparables. Ceiling logic: nobody pays more than land plus new-build cost.
  3. **Sales comparison**: price per sq m/ft (or per unit) of comparables, adjusted for size, age, quality, location, condition, market timing; recent sales weigh more. Ceiling logic: nobody pays more than for a similar property.
  - Usually differing results. Re-examine assumptions, weight by data quality, reconcile to one estimate.
  - **Highest and best use**: land value = what the best developer could pay for the vacant site = value on completion - all-in development cost (incl. required profit). It is the use with the highest residual, not the highest completed value. If existing use value < land value at best use, expect demolition.

- **Direct capitalization (value = NOI1 / cap rate)**: use for stable, typical income. How: (1) forecast first-year (or **stabilized**) NOI, (2) derive cap rate from several comparable sales (`NOI_comp / price_comp`), (3) divide. Growth is **implicit** in the cap rate. UK variant: `value = rent / all-risks yield (ARY)` on fully-let property where tenants pay costs; reciprocal of the cap rate = years' purchase (YP). Gross income multiplier is weaker (ignores vacancy and expense differences). Failure mode: applying a cap rate to temporarily depressed NOI undervalues a property that will stabilize; or using it when income steps up (Property B, ch02 Example 20).

- **DCF / yield capitalization**: explicit NOI (less capex and leasing costs) for a holding period + **terminal (reversion) value** `= NOI(year N+1) / terminal cap rate`, discounted at the discount rate. Use when income is non-level (lease rollover, renovation, step-ups). Terminal cap rate is usually **>= going-in** (older asset, more uncertainty, possibly higher rates); a lower terminal cap is justified only by falling discount rates or stronger growth. The forecast must run one year past exit.

- **Layer method** (concept): split income into the contractual (level) layer and the market-rent/growth layer, discounting each at its own risk. Mentioned as an alternative to direct cap when income has several growth regimes.

- **Leverage analysis**: max loan = **min(LTV x value, NOI / DSCR / loan constant)**. Equity dividend rate (cash-on-cash) = (NOI - debt service) / equity. Leveraged IRR > unleveraged IRR when the property return exceeds the loan rate (positive leverage); downside is symmetric and larger. Financing does not change the property's value, only equity return and risk.

- **NAVPS approach for REITs/REOCs**: market value of operating real estate (forward cash NOI / cap rate) + other tangible assets - debt and other liabilities, / shares. Exclude goodwill, deferred financing costs, deferred tax assets and liabilities ("soft" items); use market value of debt if materially different. Use as the primary benchmark (Europe, Asia) and as a relative tool (implied cap rate from the share price). Premiums/discounts of +-25% to NAV occur.

- **Relative value with FFO/AFFO**: P/FFO is the REIT "P/E", P/AFFO the "cash" multiple; EV/EBITDA is unlevered and is the reciprocal of a cap rate proxy. Multiples rise with growth, fall with risk and leverage. Compare with sector peers and history; adjust for leverage and for non-income assets (land, development) that earn no FFO.

- **Dividend discount (two- or three-step)**: REITs pay out 90-100% of taxable income, so DDM/DCF is valid with explicit near-term growth and a terminal Gordon value.

- **Choosing among valuation methods**: single best method, midpoint, or reliability-weighted average. NAV becomes unreliable when property transactions dry up; multiples when earnings are distorted by one-offs.

## Key Concepts
- **NOI**: rental revenue (incl. recoveries) less operating expenses (taxes, insurance, maintenance, utilities, vacancy and collection loss), before financing, income taxes, depreciation and capex; the property analog of EBITDA.
- **Cap rate**: `NOI / value`, a snapshot yield on first-year income; inverse of the price/NOI multiple; **going-in** (year 1) vs. **terminal/residual** (year after sale).
- **Discount rate**: required total return (risk-free + property risk premium); applies to all NOI, so it exceeds the cap rate when growth is positive.
- **Net lease vs. gross lease**: net = tenant pays operating expenses (NNN: CAM, taxes, insurance); gross = owner pays. Base rent of a net lease is lower; the party that pays bears expense risk. Long single-tenant net lease (often sale-leaseback) is the most bond-like.
- **Percentage lease**: base rent + share of tenant sales above a breakpoint; the natural breakpoint = base rent / percentage rate.
- **Rent bumps / step-ups, CPI-linked rent, expense caps and pass-throughs**: contractual inflation protection with gaps (caps, regional cost inflation).
- **Straight-line (non-cash) rent**: average contractual rent booked as revenue; differs from cash rent; deducted from FFO to reach AFFO and from NOI to reach cash NOI.
- **Appraisal lag / smoothing**: appraised values trail transactions, dampening volatility and correlation; Sharpe ratios and allocations to private real estate are overstated.
- **Repeat-sales vs. hedonic index**: both transaction-based; repeat sales controls for property by using the same asset twice; hedonic regresses price on characteristics and needs only one sale. Transaction indexes lead appraisal indexes but are noisy.
- **REIT / REOC / TRS**: REIT = tax-transparent, must distribute 90-100% and hold at least 75% assets and income in real estate; REOC = taxable operating company, free to develop and retain earnings; TRS = taxable subsidiary of a REIT for non-qualifying activity.
- **LTV, DSCR, equity dividend rate**: debt/value; NOI/debt service (lenders require about 1.25-1.5x); first-year levered cash yield on equity (not an IRR).
- **FFO**: net income + real estate depreciation and amortization + losses (- gains) on property sales + real estate impairments. **AFFO (FAD)**: FFO - non-cash straight-line rent - recurring maintenance capex and leasing costs (commissions, tenant improvements); best proxy for dividend capacity, but no standard definition.
- **Real estate cycle**: about 17-18 years on average; supply lags demand because of long development lead times, which is why oversupply continues to complete two to three years after a recession starts.

## Formulas & Reference Tables
Symbols: r discount rate, g constant growth of income and value, NOI1 first-year NOI, c cap rate.
- `Cap rate = NOI1 / Value`; `Value = NOI1 / c`
- `c = r - g`, i.e. `r = c + g` (constant growth; approximate when rents reset only periodically)
- `Value = NOI1 / (r - g)` (Gordon growth analog); level NOI: `Value = NOI / r`
- `ARY = Rent / Sale price of comparable`; `Value = Rent / ARY`
- `Terminal value_N = NOI_(N+1) / terminal cap rate`
- `DCF value = SUM(t=1..N) CF_t/(1+r)^t + TV_N/(1+r)^N`, with CF = NOI - capex and leasing costs
- `Stabilized value (renovation case) = NOI_stab/(r - g) - PV of lost income during renovation`
- `Cost approach value = Land + Replacement cost (incl. developer profit) - Deterioration - Obsolescence`
- `Implied land value = Value on completion - all-in development cost (incl. profit)`
- `Net rent (net lease) ~ Gross rent - operating expenses` (equivalent rents)
- `Percentage rent = Base rent + p x (Sales - Breakpoint)`
- `NCREIF-style holding period return = (NOI - Capex + End MV - Begin MV) / Begin MV` (MVs are appraisals; unleveraged)
- `DSCR = NOI1 / Debt service`; `Max loan (interest-only) = min(LTV x V, (NOI1/DSCR)/i)`
- `Equity dividend rate = (NOI - Debt service) / Equity`
- `FFO = NI + D&A (real estate) + losses - gains on sales (+ impairments)`; `AFFO = FFO - straight-line rent - recurring capex and leasing costs`
- `Payout ratio = Dividend / FFO (or AFFO)`
- `NAVPS = (Forward cash NOI / c + cash + receivables + land + prepaids - debt - other liabilities) / shares`
- `Forward cash NOI = (LTM NOI - non-cash rent + full-year effect of acquisitions) x (1 + g)`
- `Price/NAV` discount = potential undervaluation; premium needs justification (management, growth, development pipeline).

**Property type drivers and lease norms**
| Type | Primary demand driver | Typical lease | Risk notes |
|---|---|---|---|
| Office | Job creation (finance, insurance), space per employee | 3-5y small, 5-10y large; UK FRI, 5-year upward-only reviews | Supply dislocation, remote work, obsolescence |
| Industrial/warehouse | GDP, trade, e-commerce, logistics routes | Long net; build-to-suit | Trade-route shifts; most sensitive to import/export |
| Retail | Consumer spending, retail sales, confidence | 3-5y small, long for anchors; percentage rent | E-commerce, anchor quality; management intensive |
| Multi-family | Household formation, demographics, rent vs. buy | 6m-2y (1y common), gross-ish | Short leases reprice fast; rates move rent vs. own |
| Hotel | GDP, business confidence | None (nightly) | Highest cash-flow volatility, operating business, excluded from core |

**Index families**
| Index type | Examples | Bias |
|---|---|---|
| Appraisal-based (property, funds) | NCREIF NPI, MSCI (ex-IPD), INREV, ANREV, GREFI | Smooth, lagged, low correlation |
| Transaction-based | RCA CPPI (repeat sales), hedonic indexes | Noisy, data-hungry, lead appraisals |
| Listed | FTSE EPRA Nareit, S&P, MSCI, CMBX (debt) | Equity-like short-run behavior |

## Mental Models
- **Cap rate is a yield with growth baked in**: use `c = r - g` to read a quoted cap rate. A 5% cap in a market with 7% required return means the buyer expects 2% growth; a rising rate without growth means falling price.
- **Value does not care how you finance it**: use unleveraged NOI/cap rate or DCF for value; use LTV, DSCR and IRR spread only to judge equity return and risk.
- **Bond with an equity tail**: lease term = bond maturity, tenant credit = credit spread, rollover = reinvestment and equity risk. Longer leases give stability but forfeit upside when market rents rise; shorter leases reprice fast but expose income in a downturn.
- **Appraisal index = moving average of reality**: when a private real estate series looks suspiciously diversifying, unsmooth it or use a transaction index before sizing the allocation.
- **Listed = private repriced daily**: shares lead private values and overshoot; a deep discount to NAV is the signal for take-privates and asset sales (the arbitrage closing the gap).
- **Use the multiple that matches the question**: NAVPS for asset value and takeover logic, P/FFO for quick peer comparison, P/AFFO for dividend capacity, DDM for income investors.

## Worked Example
All numbers recomputed in Python.

**1. Terminal value and going-in cap (CFA Example 20).** NOI is 100,000 for 5 years, then 120,000 in year 6 growing 2%; r = 12%, hold 5 years.
- Terminal cap = 12% - 2% = 10%; `TV = 120,000/0.10 = 1,200,000`.
- `V = 100,000 x annuity(12%,5) + 1,200,000/1.12^5 = 360,478 + 680,912 = 1,041,390`.
- Going-in cap = 100,000/1,041,390 = **9.60%** < terminal 10%: buyers accept a lower initial yield because income steps up at rollover. Direct cap on year-1 NOI with a 10% cap would give 1,000,000 and undervalue.

**2. Warehouse DCF (Perth, CFA Example 22).** Year-1 NOI = AUD 145 x 20,000 m2 = AUD 2.9m; initial cap 6.0%, so price = **AUD 48.33m**. Exit end of year 7 at 7.0% on year-8 NOI of AUD 3.788m gives TV = **AUD 54.11m**. Cash flows (AUD m, after capex and leasing): 2.799, 2.882, 3.002, 1.681 (renovation year), 3.388, 3.446, and 3.549 + 54.114 in year 7. At 7.0%: PV = **49.49m**, NPV = **+1.15m**, IRR = **7.42%**.
- Sensitivity: exit cap 8.0%/7.5%/6.5%/6.0% gives NPV -3.06m / -1.09m / +3.75m / +6.77m. A 100 bp exit-cap move swings NPV by far more than the entry spread.
- **Breakeven price = PV of inflows = AUD 49.49m (entry cap 5.86%)**.
- **⚠ Correction**: the printed entry-cap sensitivity (NPV 3,847 / 2,626 / ... (647) / (2,896)) and the "AUD 51.1m, 5.67%" breakeven do not tie to the printed DCF. Holding cash flows and exit fixed, NPV = 49,488 - price: 7.0% cap +8,059; 6.5% +4,872; 5.5% -3,240; 5.0% -8,512.

**3. Leverage (CFA Examples 23-26).** Value $5m, NOI $400k, interest-only 8%, LTV cap 80%, DSCR 1.25.
- LTV loan = $4.0m; DSCR loan = (400k/1.25)/0.08 = $4.0m (both bind). Debt service $320k, equity $1.0m, equity dividend rate = 80k/1.0m = **8.0%**.
- Sell after 5 years at $6m: equity IRR = **21.14%** (cash flows -1.0m, 80k x 4, 80k + 2.0m). Unleveraged IRR = **11.20%** (-5m, 400k, ..., 400k + 6m). Positive leverage: 11.2% property return vs. 8% loan cost. Check: with no appreciation (sale at $5m) both IRRs fall to 8.0% (leveraged: -1.0m, 80k, ..., 80k + 1.0m), so the leverage benefit comes entirely from the property earning more than the loan rate.

**4. NAVPS (CFA Exhibit 10).** LTM NOI 270,432 - non-cash rent 7,667 + acquisition effect 4,534 = cash NOI 267,299; x 1.015 = 271,308 (next 12 months). At 7.0% cap: 3,875,829. Add cash 65,554, land 34,566, receivables 45,667, prepaids 23,456 = gross asset value 4,045,072. Less debt 1,010,988 and other liabilities 119,886 = NAV 2,914,198 / 55,689 sh = **NAVPS 52.33**. A +100 bp cap move to 8.0% cuts operating real estate by 12.5% to 3,391,350 and NAVPS to about **$43.63** (-16.6%): the debt is fixed, so the equity value falls proportionally more than the property.

**5. FFO and AFFO (CFA Exhibit 12).** NI 160,638 + D&A 76,100 + losses on sales 25,000 = FFO 261,738 (4.70/share). Less straight-line rent 21,103 and recurring capex/leasing 55,765 = AFFO 184,870 (3.32/share). AFFO is 70.6% of FFO: the gap is the maintenance burden.

**6. Capitol Shopping Center REIT multiples (CFA Exhibits 16-17).** Price 69.85: P/FFO 2021E 69.85/4.23 = **16.5x**, 2022E 15.2x; P/AFFO 18.6x and 17.1x. Premium to shopping center REIT peers (14.5x P/FFO 2021E) = **13.8%**. Required return by CAPM = 4.0% + 0.80 x 5.0% = **8.0%**. 2020 dividends 2.80 vs. FFO 3.95 = 70.9% payout; vs. AFFO 3.54 = 79.1%, close to the board's 80% target.

## Anti-patterns
- **Applying a cap rate to non-stabilized or non-level NOI**: use stabilized NOI minus PV of the shortfall, or DCF with a terminal value.
- **Using the going-in cap rate as the exit cap**: assumes the building does not age and rates do not rise; set terminal cap at or above going-in unless justified.
- **Quoting cap rate as expected return**: it equals the return only with zero growth. Return ~ cap + growth.
- **Letting leverage change the property valuation**: financing affects equity IRR, not value. Compare all-cash vs. levered cases only for return.
- **Sizing private real estate on raw appraisal-based volatility and correlation**: overstates Sharpe and allocation; unsmooth or use transaction indexes.
- **Treating FFO as cash flow or dividend capacity**: it ignores maintenance capex, leasing costs and straight-line rent; use AFFO (and check definitions).
- **Pricing REITs on P/FFO alone**: ignores land, development pipeline, leverage and below-market leases; cross-check with NAV.
- **Using a NAV from stale appraisals in a frozen market**: when transactions are thin NAV is subjective; rely more on multiples and DDM.
- **Skipping due diligence on cash flows**: seller statements may hide underspending, free rent and incentives that inflate NOI and occupancy.

## Exam Focus & Traps
- **Cap rate = discount rate - growth**. If growth is negative, cap > discount. Q3-style: g = 7.25% - 5.25% = **2.00%**.
- **Direct cap vs. DCF**: with constant growth they agree. Here direct cap gives $52.87m vs. DCF $49.75m for Property 1: direct cap is **higher** here because the 5.25% cap implies 2% perpetual growth from year 1, whereas the DCF exits at 6.0% (implied growth 1.25%, older building) and so assumes less future growth.
- **Terminal value** uses **year N+1 NOI** (e.g. $3,217,959/0.06 = $53,632,650), not year N.
- **Loan sizing**: take the **lower** of the LTV loan and DSCR loan ($48m value, 75% LTV = $36.0m vs. DSCR 1.5x loan = $32.18m; answer about $32m).
- **Net vs. gross lease**: gross lease puts expense risk on the **owner**; net lease on the **tenant**; net rent about = gross - expenses.
- **Percentage rent**: min rent + % of sales above the breakpoint; natural breakpoint = min rent / %.
- **Highest and best use** = highest **residual land value**, not highest completed value (office 4m beats apartment 3m although the apartment completes higher).
- **FFO adds back depreciation and removes gains; AFFO subtracts straight-line rent, recurring capex and leasing costs**. Going from AFFO to FFO: add straight-line rent and capex, **not** depreciation. Baldwin: FFO/share = (142,187 + 90,409 - 2,162)/121,944 = 1.89 (gains subtracted); price = 1.89 x 11.5 = **$21.73**.
- **NAV excludes deferred tax liabilities and goodwill**; NAVPS falls when the cap rate rises; it ignores book value. Mistaken answers: book value per share (ignores market value), or real estate value per share (ignores debt).
- **Appraisal-based index**: smoothing, lag, lower volatility, lower correlation, higher Sharpe, over-allocation. Transaction-based indexes lead and are noisier.
- **REIT vs. REOC**: REIT = tax-exempt at entity level (no double taxation), high yield, limited flexibility and growth retention; REOC = flexible, can develop and retain. Liquidity both; maximum growth/development flexibility = REOC or direct.
- **Private equity real estate**: lower correlation to stocks than listed REITs; control; illiquidity premium; high fees; leverage drives returns.
- **Property survey** finds encroachment and easements; environmental inspection finds contamination; engineering inspection finds structure.
- **Two-step DDM**: Baldwin D1 = 1.00, D2 = 1.06, g = 5%, r = 8.5%: D3 = 1.113, TV2 = 1.113/0.035 = 31.80, value = **$28.83**. **⚠ Errata**: the 2022 errata fixes answer C to $28.83 (the printed $28.76 used a rounded D3 of 1.11).
- **⚠ Errata (Example 15)**: valuation metrics in the London office table are updated: price/sq ft 1,450 / 1,600 / 875; price/revenue 22.7x / 21.1x / 16.8x; price/operating income 25.3x / 23.4x / 19.8x. The comparable Class B range becomes **GBP 87.5m** (875 x 100,000 sq ft) to about **GBP 90.9m** (16.8x revenue), before an age discount.
- **⚠ Errata (Section 10.2)**: the revised net worth per share is **NAVPS** (not NAV).
- **⚠ Correction (CRE case, Exhibit 15)**: "debt / total market capitalization" of 40.5% is actually debt / **equity** market cap (1,792,629 / 4,421,196). On true total capitalization it is 28.8%; also the text says year-end "2018" where 2020 is meant. Compare only like-for-like with the peer figures.

## Key Takeaways
1. Real estate returns = income + appreciation; core private real estate sits between bonds and stocks in risk and return, with imperfect (but overstated) diversification.
2. Four quadrants (public/private x equity/debt) define the investable universe; pick by liquidity, control and expertise.
3. Value private property three ways (income, cost, comparables) and reconcile; DCF or layer method when income is not level.
4. `Cap rate = r - g`; value = NOI1/cap; terminal value uses next-year NOI at a cap rate at or above going-in.
5. Financing never changes property value; LTV and DSCR cap the loan (take the lower); positive leverage raises equity IRR and risk.
6. Appraisal indexes smooth volatility and understate correlation; unsmooth or use transaction indexes before allocating.
7. REITs: NAVPS (cap NOI, add other assets, subtract liabilities), P/FFO and P/AFFO, DDM; AFFO best reflects dividend capacity but is non-standard.
8. Public vs. private: listed = liquidity, transparency, diversification, low entry; private = control, illiquidity premium, lower reported volatility, leverage-driven returns.

## Connects To
- **ch01**: alternative investment overview, fee structures, index biases (this chapter develops real estate valuation in depth).
- **ch03**: private equity funds use the same J-curve, appraisal and fee logic as private real estate funds.
- **ch06**: unsmoothing appraisal returns and sizing private real estate in a multi-asset allocation.
- **`cfa-equity-valuation`**: Gordon growth and multi-stage DDM (the REIT DDM and `c = r - g`) and P/E-type multiples.
- **`cfa-fixed-income`**: MBS/CMBS, mortgage debt and prepayment (real estate debt quadrant).
- **`cfa-financial-statement-analysis`**: investment property fair value vs. cost model (IFRS/US GAAP), straight-line rent.
- **`cfa-portfolio-management`**: diversification, illiquidity premium and strategic asset allocation using real estate.
