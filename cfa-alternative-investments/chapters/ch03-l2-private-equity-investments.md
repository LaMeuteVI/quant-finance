# Chapter 3: Private Equity Investments
> **Source**: CFA Program Curriculum 2022, Level II, Reading 36 · Alternative Investments | Yves Courtois, CMT, MRICS, CFA, and Tim Jenkinson, PhD (VC-method section authored by Victoria Ivashina, PhD)

## Core Idea
Private equity (PE) is an alternative governance model: ownership and control are concentrated in one owner who re-engineers the company, levers it with cheap debt, and pays managers through equity, then sells ("buy-to-sell") within a fund life of about 10 years. There is no market price, so value is inferred backwards (LBO model, VC method) and the investor in a fund must judge performance with cash-flow-weighted metrics (IRR, DPI, RVPI, TVPI) that are distorted by fees, J-curve, GP valuation policy and IRR timing games.

## Learning Outcomes Covered
- explain sources of value creation in PE (re-engineering, leverage, alignment)
- explain how PE firms align interests with portfolio-company managers
- compare buyout vs venture capital characteristics
- interpret LBO model and VC method output
- explain exit routes (IPO, secondary sale, MBO, liquidation) and their impact on value
- explain risks and costs of investing in PE
- explain fund structures, terms, due diligence and valuation
- interpret and compare fund performance as an investor
- calculate management fees, carried interest, NAV, DPI, RVPI, TVPI

## Frameworks Introduced
- **Three sources of value creation in PE**: (1) re-engineering the business, (2) financial leverage and access to credit on favorable terms, (3) alignment of interests between owners and managers.
  - When to use: to decompose or challenge a PE return claim.
  - How: value bridge from entry cost to exit value = earnings growth + multiple expansion + debt reduction (Exhibit "value-creation chart"). Each bar must be backed by due diligence (commercial, tax, financial) and a strategic review.
  - Why it works / failure mode: leverage alone is not proof of skill. Modigliani-Miller says financing does not change firm value without taxes, distress costs and asymmetric information, but the interest tax shield does create value in an LBO, and Jensen's free cash flow hypothesis says debt service removes management's discretion to waste cash in low-growth, cash-rich firms. Public firms can also re-engineer (Apple, Toyota, Unilever), so operational edge is only part of the story.
- **LBO model**: a tool that takes (a) target free cash flow forecasts, (b) required returns of each financing provider (equity, senior, high-yield, mezzanine) and (c) available financing, then solves for the **maximum price payable to the seller** that still meets target returns.
  - When to use: buyouts of mature firms with steady cash flow; also as a negotiation tool to bound the bid range.
  - How: forecast FCF over the expected holding period; set exit year and exit multiple (EV/EBITDA from peers); amortize senior debt with cash flow; waterfall the exit EV through debt, preference shares, then common equity (PE fund vs management); compute multiple and IRR per stakeholder; run scenarios on exit multiple, growth and leverage.
  - Why it works / failure mode: initial high and declining leverage is the main technical valuation issue; falls apart if cash flows disappoint or no exit is available. It is not a valuation methodology per se, it is a price-ceiling and returns tool.
- **VC method**: work backwards from expected exit value and required ROI to post-money, pre-money and ownership fraction.
  - When to use: early-stage ventures where DCF, multiples and LBO are impractical.
  - How: (1) forecast exit metric (revenue, users, EBITDA) times industry multiple = exit equity value; (2) choose required ROI (10x-30x for VC vs 2.0x-2.5x for buyouts); (3) post-money = exit value / ROI; (4) pre-money = post-money - new investment; (5) fractional ownership = investment / post-money; (6) convert to IRR if needed.
  - Why it works / failure mode: very sensitive to the revenue forecast and the required ROI; the high hurdle is a haircut for a high failure rate.
- **Stage financing**: VC is funded in rounds (Series A, B, ...) to buy information; later-round pre-money valuations mark up earlier stakes, and each new round dilutes earlier holders pro rata.
- **Distribution waterfall choice**: deal-by-deal (American) vs total return (European, prevalent in large institutional funds), with clawback and hurdle as LP protections.
- **PME (Public Market Equivalent, Long-Nickels / Index Comparison Method)**: compare fund IRR with an index by investing fund cash flows in the index at the same amounts and dates. Breaks down when the fund strongly outperforms (negative NAV); fixes: PME+ (Rouvinez 2003), modified PME (Cambridge Associates 2013).

## Key Concepts
- **Private equity**: equity not quoted on stock markets; spans venture capital (VC), growth equity and buyouts (LBO, MBO), plus special situations (mezzanine, distressed, secondaries, fund of funds).
- **Leveraged buyout (LBO)**: acquisition of control financed with a large share of debt (typically about 70% debt / 30% equity; 6-8x EBITDA borrowing common for large deals). Leverage is quoted as a multiple of EBITDA, not of equity.
- **Mezzanine financing**: subordinated debt or preferred shares with an equity kicker (warrants, conversion), paying a higher coupon than senior or high-yield debt.
- **Leveraged loans vs high-yield bonds**: loans are senior secured with maintenance covenants; bonds are unsecured, lower rated, high coupon; both are repackaged into CLOs/CDOs.
- **Pre-money / post-money valuation**: value before / after new financing; pre-money + new equity = post-money.
- **Option pool (fully diluted basis)**: VC share price is computed on fully diluted shares so founders, not the VC, absorb dilution from future option exercise.
- **Ratchet**: clause letting management raise its equity share if performance (or the PE firm's return) beats targets.
- **Liquidation preference / preferred dividend**: PE gets paid first, often a guaranteed minimum multiple; cumulative preferred dividends act like junior debt and come at earlier investors' expense.
- **Earnout**: deferred price contingent on post-deal performance (mostly VC).
- **Tag-along / drag-along rights**: minority can join a majority sale on equal terms / majority can force minority to sell on the same terms.
- **Capital call (drawdown) and commitment**: LPs commit money, GP draws it as deals are done; undrawn commitments are unfunded liabilities, not in NAV.
- **J-curve**: negative or low reported early returns (fees, cost-based valuation) followed by improvement as companies mature and exit.
- **Hurdle rate / preferred return**: IRR (typically 7%-10%) the fund must exceed before the GP earns carry.
- **Carried interest**: GP's share of fund profits, typically 20% after management fees.
- **Clawback**: GP returns excess carry to LPs (true-up, typically at termination or annually, often with escrow).
- **Key man clause**: investment freeze if named key executives leave or under-commit time.
- **Vintage year**: year the fund launched; performance is benchmarked to peers of the same vintage and strategy.
- **Gross IRR vs net IRR**: gross = cash flows between portfolio companies and fund (GP track record); net = cash flows between fund and LPs after fees and carry.
- **PIC, DPI, RVPI, TVPI**: paid-in capital ratio, realized cash-on-cash, unrealized value, and their sum, all net of fees and carry.
- **Crossover co-investment**: a later fund of the same GP invests in a company funded by an earlier fund (conflict of interest).

## Formulas & Reference Tables
Exit-stakeholder payoffs (LBO, exit at year T):
- `Senior debt at exit = D₀ − cumulative repayments`
- `Preference shares at exit = P₀ × (1 + r_pref)ᵀ` (dividend capitalized, paid at exit)
- `Residual equity = Exit EV − debt − preference shares`
- `PE equity proceeds = PE share × Residual equity`; `Management equity proceeds = (1 − PE share) × Residual equity`
- `Multiple = Proceeds / Invested`; `IRR = Multiple^(1/T) − 1` (single in, single out)

VC method:
- `Post-money = Exit equity value / ROI`, with `Exit equity value = exit metric × industry multiple`
- `Pre-money = Post-money − New equity investment`
- `VC fractional ownership = Investment / Post-money`
- `ROI = (1 + IRR)ᵗ`, so `IRR = ROI^(1/t) − 1`
- New shares: `N_new = f × N_old / (1 − f)` where f is the required ownership fraction and N_old is fully diluted (founders + option pool); `Price per share = Investment / N_new`
- Dilution by a later round with fraction f_B: `Old holder stake = previous stake × (1 − f_B)`
- Implied ROI of an earlier round at a later round = `(Later exit value × diluted ownership) / Original investment`
- Cumulative preferred dividend = `Investment × [(1 + d)ᵗ − 1]`

Fund economics:
- `Management fee = fee % × committed capital` (investment period), then often on invested capital/NAV
- `NAV before distributions_t = NAV after distributions_{t−1} + capital called_t − management fee_t + operating results_t` (realized + unrealized)
- `NAV after distributions = NAV before − carried interest − distributions`
- `DPI = cumulative distributions / paid-in capital`
- `RVPI = residual NAV (LP share) / paid-in capital`
- `TVPI = DPI + RVPI`
- `PIC = paid-in capital / committed capital`

Buyout vs VC:

| Feature | Buyout | Venture capital |
|---|---|---|
| Cash flows | Steady, predictable | Unpredictable, cash burn |
| Leverage | Extensive (senior + junior/mezzanine) | Rare, equity funded |
| Asset base | Significant, collateralizable | Weak |
| Target return | about 2.0x-2.5x | 10x-30x |
| Return dispersion | Low, bankruptcies rare | A few winners, many write-offs |
| Due diligence | Full (financial, strategic, commercial, legal, tax, environmental) | Technology and commercial; financial limited |
| Main value driver | EBITDA growth, deleveraging, multiple | Revenue growth, milestones |
| Deal flow | Auctions | Often proprietary |
| GP income | Carry + transaction + monitoring fees | Mostly carry |
| Typical exit | Secondary buyout, strategic sale, IPO | Strategic sale, secondary venture, IPO |

Valuation approach by stage: DCF (expansion to maturity), earnings multiples (established, predictable; rare for start-ups), real options (seed/start-up flexibility), replacement cost (early stage, asset-rich). Adjustments for control premium and illiquidity discount are applied to the preliminary value, not inside the cost of capital.

Waterfall alternatives:

| Waterfall | Carry paid | Favors |
|---|---|---|
| Deal-by-deal (American) | After each exit | GP (earlier carry), needs clawback |
| Total return, alt. 1 | Only after all committed capital returned | LPs |
| Total return, alt. 2 | On distributions while portfolio value exceeds invested capital by a threshold (about 20%) | Middle |

## Mental Models
- **The LBO as a price ceiling**: start from what financiers require and solve for the highest price; never read it as "fair value".
- **Value bridge**: decompose exit value into earnings growth, multiple expansion and debt paydown; prefer deals where the first and third carry the return, because multiple expansion is luck.
- **Call-option view of VC**: target ROI of 10x-30x is the price of a high failure rate; the expected multiple of the whole VC book is far lower than the required multiple per deal.
- **Fund-life lens**: DPI answers "how much cash have I banked", RVPI "how much of the rest is GP opinion", TVPI "total, but only as honest as the valuations". Weigh DPI more heavily the older the fund.
- **Net of fees is the only return an LP owns**: gross IRR measures the GP's skill, net IRR the LP's outcome.
- **IRR is a fragile number**: anything that shortens the time capital is outstanding (credit-line funded deals, dividend recaps) raises IRR without adding value; pair IRR with multiples.

## Worked Example
**1. LBO exit (recomputed from the source example).** Buy at EV = €5,000m, financed with debt €2,500m and equity €2,500m, split into €2,400m preference shares (12% annual, rolled up, PE-owned), €95m PE common and €5m management common. Residual common equity is split 95/5. Exit after 5 years at EV = 1.6 × 5,000 = €8,000m; debt paid down to €1,600m.
- Preference shares = 2,400 × 1.12⁵ = 4,229.6 (about 4,230)
- Residual equity = 8,000 − 4,229.6 − 1,600 = 2,170.4
- PE common = 0.95 × 2,170.4 = 2,061.9; management common = 0.05 × 2,170.4 = 108.5
- PE fund total proceeds = 4,229.6 + 2,061.9 = 6,291.5 on invested 2,495 → multiple 2.52x, IRR = 2.52^(1/5) − 1 = 20.3%
- Management: 108.5 / 5 = 21.7x (source rounds to 21.8x), IRR about 85%
Interpretation: a 60% EV gain (earnings growth + multiple) plus deleveraging from 2,500 to 1,600 produces a 20% fund IRR and a huge management payoff from a tiny sweet equity slice. ⚠ Errata: the 12% per annum IRR belongs to the preference-share component; the 20% is the PE fund's blended IRR on pref plus common.

**2. VC method with option pool and two rounds.** Seed: raise $0.5m, exit sales $80m, revenue multiple 2x, required ROI 20x, no debt.
- Exit value = 160; post-money = 160/20 = $8.0m; pre-money = $7.5m; ownership = 0.5/8 = 6.25%; 5-year IRR = 20^(1/5) − 1 = 82.0%.
- Series B one year later: $2m at 10x on a $300m exit → post = 30, pre = 28, ownership = 2/30 = 6.67%. Series A is diluted to 6.25% × (1 − 0.0667) = 5.83%; founders 93.75% × 0.9333 = 87.5%. Series A implied ROI = 300 × 5.83% / 0.5 = 35x (vs 20x at entry) although no exit has happened.
- Option pool: $4m for 20% with 10m founder shares and a 2m pool. Fully diluted = 12m; new shares = 0.2 × 12/0.8 = 3.0m; price = 4/3 = $1.33; VC starts at 3/13 = 23.08% and is diluted to 20% when options are exercised. With no pool: 2.5m shares at $1.60.

## Anti-patterns
- **Reading the LBO model as a valuation**: it yields the maximum affordable price given financier hurdles, not intrinsic value.
- **Attributing all PE returns to operational skill**: part is leverage, tax shield and favorable credit cycles (low spreads, covenant-lite loans).
- **Applying peer multiples blindly to a private target**: comparables differ in size, risk, capital structure, accounting (trailing vs forward earnings); unlever and relever beta.
- **Folding control premium and illiquidity discount into the discount rate**: they are judgmental adjustments to the preliminary value.
- **Using DCF or multiples for seed-stage companies**: use the VC method, real options or replacement cost.
- **Quoting IRR alone**: ignores size, can be gamed with credit lines, and is cash-flow weighted so it is not comparable to time-weighted returns of other asset classes.
- **Treating RVPI as a guaranteed future return**: it is the GP's mark; all ratios are per dollar paid in, not per dollar committed.
- **Ignoring undrawn commitments**: they are legal obligations excluded from NAV.

## Exam Focus & Traps
- **Pre- vs post-money**: ownership = investment / **post**-money, not pre-money. Pre-money = post-money − investment.
- **Fully diluted trap**: the VC's ownership is quoted at 20% post-dilution; the share-count approach shows a higher starting percentage (23.08%) because the pool is not yet exercised.
- **ROI vs IRR**: ROI is a multiple (20x); convert with the holding period. ROI does not depend on the holding period, IRR does.
- **Waterfall direction**: deal-by-deal (American) benefits GP; total return (European) benefits LP and is prevalent for large institutional funds. Clawback and hurdle are LP protections; a fund with clawback + total return + higher hurdle is better aligned (practice problem Fund B).
- **Carry and hurdle with deal-by-deal**: check the IRR of each deal against the hurdle before applying 20% (example: $5m profit on $40m over 2 years = 6.1% IRR < 8% → zero carry).
- **Clawback true-up**: cumulative carry is 20% of cumulative profit across deals (example: gains 10, loss 5 → GP keeps 20% × 5 = 1, pays back 1 of 2).
- **Carried interest on NAV excess over committed capital** (EVP case): in the first year NAV exceeds commitments, carry = 20% × (NAV − commitments); later years, 20% × increase in NAV before distributions.
- **DPI/RVPI/TVPI misreads**: they are scaled to paid-in capital; a low PIC with RVPI 0.65 does not imply RVPI will double when the rest is called. TVPI = DPI + RVPI, net of fees and carry.
- **Fund management fee base**: committed capital during the investment period, paid-in/invested capital afterward (the EVP example uses 2% of paid-in capital).
- **Exit least likely for VC**: management buyout, because leverage is not available to firms with short history.
- **Valuation statement least valid**: DCF emphasis for early-stage VC (false); buyouts use income approaches as primary (true).
- **Fee/cost list**: management 2%, performance 20%, placement about 2% upfront or trailer fee, transaction and audit costs, dilution.
- **NAV staleness**: GPs mark at cost, lower of cost/market, last-round, or peer multiples with discounts; NAV is stale in down markets with long gaps between rounds.

## Key Takeaways
1. PE value = earnings growth + multiple expansion + deleveraging; favor deals whose return comes from the first and last components.
2. Use the LBO model to set a maximum bid, stress exit multiple, exit year and leverage, and check covenant and cash-flow headroom.
3. In the VC method, pre-money = exit value / ROI − investment; ownership = investment / post-money; always compute on a fully diluted basis.
4. Later-round valuations mark up earlier rounds (implied ROI) but dilute them pro rata; preferred terms shift value from earlier to later investors.
5. Exit route drives value: IPO gives top multiples but is market-timed; secondary sale is the workhorse for buyouts; MBO aligns interests but adds leverage; liquidation sets a floor.
6. Fund terms to negotiate: fee base, hurdle, waterfall type, clawback with escrow, key-man, fee sharing, co-investment rights, GP removal thresholds (above 75% supermajority).
7. Evaluate a fund on net IRR vs same-vintage peer median, plus DPI/RVPI/TVPI; expect a J-curve; scrutinize valuation policy and IRR-boosting credit lines.
8. Compare PE with public markets using PME, not raw IRR vs time-weighted index returns.

## Connects To
- **ch01**: alternative investment characteristics, fee structures and return-measurement issues for illiquid assets (same skill).
- **ch05**: hedge fund fee/liquidity terms contrast with PE closed-end terms (same skill).
- **ch06**: how PE fits into strategic allocation to alternatives, illiquidity and liquidity budgeting (same skill).
- **`cfa-equity-valuation` ch11**: private company valuation, control and marketability discounts, and comparables for private targets.
- **`cfa-corporate-finance` ch06**: capital structure, Modigliani-Miller, interest tax shield and leverage trade-offs behind LBOs.
- **`cfa-corporate-finance` ch09**: M&A and LBO takeover mechanics.
- **`cfa-ethics-gips` ch12**: GIPS treatment of IRR as the appropriate PE performance measure.
