# Chapter 4: Portfolio Management: An Overview
> **Source**: CFA Program Curriculum 2020, Level I, Reading 51 · Portfolio Management | Owen M. Concannon, Robert M. Conroy, Alistair Byrne, Vahan Janjigian

## Core Idea
Evaluate every security by what it adds to the whole portfolio, not in isolation: diversification cuts risk (standard deviation) far more than it changes expected return, but it is not downside protection in a systemic crisis. The portfolio management process is a loop (plan → execute → feedback) anchored by the investment policy statement (IPS), and the investor type (individual, DB plan, endowment, bank, insurer, SWF) dictates horizon, risk tolerance, income and liquidity needs. The reading also maps the asset management industry and the pooled products (mutual funds, ETFs, SMAs, hedge funds, PE/VC) used to implement portfolios.

## Learning Outcomes Covered
- describe the portfolio approach to investing
- describe the steps in the portfolio management process
- describe types of investors and their distinctive characteristics and needs
- describe DC and DB pension plans
- describe aspects of the asset management industry
- describe mutual funds and compare them with other pooled investment products

## Frameworks Introduced
- **Portfolio approach to investing**: judge each security by its contribution to the risk and return of the total portfolio.
  - When to use: any selection or sizing decision; any time a client concentrates in one name (employer stock, one sector, one country).
  - How: (1) measure each holding's stand-alone return/risk; (2) measure co-movement (correlation) between holdings; (3) choose weights on the portfolio's risk-return trade-off, not on stand-alone Sharpe ratios; (4) re-test under stress correlations.
  - Why it works / failure mode: combining imperfectly correlated assets lowers volatility with no loss of expected return (portfolio mean return = weighted average, portfolio σ < weighted-average σ). It fails when correlations converge to ~1 in crises (2007-09: diversification ratio 99.4%).
- **Diversification ratio (this reading's definition)**: `DR = σ(equally weighted portfolio) / σ(randomly selected single asset)`; lower = more risk reduction.
  - When to use: quick read on the value of naive diversification when mean returns are equal.
  - How: compute the average stand-alone σ across assets and divide the portfolio σ by it. HKSE five-stock example: 17.9% vs 24.9%, DR ≈ 71-72%. Global equity indexes: 75.1% (1993-2000), 95.8% (2006-09), 99.4% (Q4 2007-Q1 2009).
  - Why it works / failure mode: DR close to 100% signals a correlation spike; diversification "is a false promise" under worldwide contagion.
- **Modern portfolio theory (MPT, Markowitz 1952)**: hold portfolios, and focus on how securities relate to each other. Sharpe, Lintner and Treynor then showed that only the systematic (non-diversifiable) part of risk earns a premium (CAPM).
- **Portfolio management process (three steps)**:
  1. **Planning**: understand client objectives and constraints; write the IPS (may specify the benchmark; review about every 3 years or on a major change in client circumstances).
  2. **Execution**: asset allocation (asset classes, sub-classes, geography, alternatives) → security analysis (top-down macro view combined with bottom-up company work) → portfolio construction (weights, risk management, trading via a buy-side trader).
  3. **Feedback**: monitoring and rebalancing (weights drift with prices; client needs change), performance evaluation and reporting versus the IPS benchmark. Feedback can trigger an IPS revision.
- **Top-down vs bottom-up**: top-down starts with macro conditions, then industries, then companies; bottom-up starts with company specifics (management quality, business prospects) and is less concerned with the cycle.
- **Investor-needs grid** (time horizon, risk tolerance, income, liquidity): use to sanity-check any proposed allocation against the client type (table below).
- **Fund structure decision tree**: open-end vs closed-end; load vs no-load; by asset type (money market, bond, stock, hybrid/target-date); versus ETF, SMA, hedge fund, PE/VC.

## Key Concepts
- **Portfolio approach**: evaluating securities by their contribution to the characteristics of the whole portfolio.
- **Investment policy statement (IPS)**: written document of the client's objectives, constraints and (optionally) benchmark; the anchor for all later decisions.
- **Asset allocation**: target weights across asset classes; commonly viewed as the decision with the greatest effect on portfolio performance.
- **Defined contribution (DC) plan**: retirement plan in the employee's name; the employee bears investment and inflation risk (401(k), UK group personal pension, Australian superannuation).
- **Defined benefit (DB) plan**: company-sponsored plan promising a defined retirement benefit; the employer bears funding risk; assets are there to fund liabilities (LDI-style matching possible).
- **Endowment / foundation**: endowments are funds of non-profits; foundations are grant-making entities; typically perpetual, real-capital preservation plus a spending rule, heavy alternatives allocation (Swensen/Takahashi "Yale model").
- **Insurance general account vs surplus account**: general account backs claims (conservative, high-quality fixed income; life insurers hold longer duration than P&C); surplus account = assets minus liabilities, can take more risk (equity, real estate, infrastructure, hedge funds).
- **Sovereign wealth fund (SWF)**: state-owned investment fund with no specific pension-type liabilities, horizons varying with government goals (stabilisation, development).
- **Buy-side vs sell-side**: asset managers buy research and execution; broker/dealers sell securities and research.
- **Smart beta**: simple, transparent, rules-based factor strategies (size, value, momentum, dividend) with somewhat higher fees and turnover than cap-weighted passive.
- **Liquid alternatives**: retail-wrapped versions of alternative strategies: less leverage, no performance fee, more liquid holdings.
- **Net asset value (NAV)**: fund assets minus liabilities, computed daily at closing prices; per-share NAV = NAV / shares outstanding.
- **Open-end fund**: issues and redeems shares at NAV; shares outstanding change. **Closed-end fund**: fixed share count; trades on the market at a premium or discount to NAV.
- **Load / no-load**: a load is a sales charge on purchase, holding or redemption; no-load funds charge only the annual fee.
- **Separately managed account (SMA)**: assets owned directly by a single client, customised (ESG exclusions, tax), higher minimums than a fund.
- **Hedge fund**: private vehicle using leverage, derivatives, long/short; typical "2 and 20" fees, periodic redemptions.
- **Carried interest / GP-LP**: the GP's profit share (typically 20%) in a private equity limited partnership, usually paid only after LPs recover contributed capital.

## Formulas & Reference Tables
| Formula | Meaning |
|---|---|
| `Diversification ratio = σ_EW portfolio / σ_random asset` | lower = more benefit |
| `Annualised mean = quarterly mean × 4`; `annualised σ = quarterly σ × 2` | quarterly to annual (√4 = 2) |
| `NAV per share = (Assets − Liabilities) / Shares outstanding` | fund pricing |
| `New shares issued = Investment / NAV per share` | open-end subscription |
| `Shares redeemed = Redemption / NAV per share` | open-end redemption |
| `Spending_t = 0.8 × Spending_{t−1} + 0.2 × 5.25% × MV_{t−2}` | Yale smoothing rule (illustrative) |

**Investment needs by client type**

| Client | Time horizon | Risk tolerance | Income needs | Liquidity needs |
|---|---|---|---|---|
| Individual | Varies | Varies | Varies | Varies |
| DB pension | Long | Typically high | High for mature funds, low for growing | Depends on plan maturity |
| Endowment / foundation | Very long | Typically high | To meet spending commitments | Typically low |
| Bank | Short | Quite low | To pay interest on deposits and expenses | High |
| Insurance company | Short (P&C); long (life) | Typically quite low | Typically low | High (claims) |
| Investment company (fund) | Varies by fund | Varies | Varies | High (redemptions) |
| Sovereign wealth fund | Varies | Varies | Varies | Varies |

**Pooled products compared**

| Product | Pricing / trading | Key features |
|---|---|---|
| Mutual fund (open-end) | Once a day at NAV, bought from the fund; no shorting or margin | Low minimums, diversified, daily liquidity; dividends usually reinvested |
| Closed-end fund | Exchange-traded at premium or discount to NAV | Fixed shares; ~1% of US mutual fund assets; no redemption pressure |
| ETF | Intraday on exchange; short and margin allowed; price close to NAV | Usually open-end; dividends paid out; small minimums |
| SMA | Custom account | Direct ownership, tailored, high minimum |
| Hedge fund | Periodic redemption | Leverage, shorts, absolute return, 2% + up to 20% |
| PE / VC | Limited partnership, 7-10 year life | Mgmt fee 1-3% of committed capital, carry ~20%, exit by merger, sale or IPO |

**Industry facts (2017)**: global AUM about $79 trillion (North America 47%, Europe 28%); active = 80% of assets but 94% of revenue; passive = 20% of assets but 6% of revenue; alternatives = 15% of assets but ~43% of revenue; global pension assets about $41 trillion (US, UK, Japan > 76%); SWF assets > $7.6 trillion; robo-advisers about $180 billion (fees ~0.20% vs ~1% for a typical adviser). US/Australia are DC-heavy; Canada, Japan, Netherlands, UK remain DB-weighted.

## Mental Models
- **"Portfolios affect risk more than return"**: expected return is a weighted average, so the free lunch is entirely on the σ side.
- **Diversification is fair-weather protection**: it lowers volatility in normal markets; in global crises correlations rise and all assets fall together. Stress-test with crisis correlations, and use hedges/option-like exposures for real downside protection.
- **Liabilities define risk**: a bank or insurer with short, hard liabilities holds safe liquid fixed income; an endowment with perpetual horizon can own illiquid equity-like assets. Start from the liability, not the asset.
- **Human capital plus financial capital**: an Enron employee's wages and savings were both tied to one firm. Count correlated non-portfolio exposures before sizing company stock.
- **Fee economics drive industry behaviour**: alternatives earn disproportionate revenue (performance fees), passive earns little per dollar, so traditional managers push into alternatives and alternative managers into liquid, long-only products.

## Worked Example
**Open-end fund flows.** Fund launched at $10.0m and 100,000 shares, so NAV/share = $100. Later NAV = $12.0m, so NAV/share = $120. Investor F invests $0.96m and buys 960,000/120 = 8,000 shares (NAV becomes $12.96m, shares 108,000). Same day Investor E redeems 5,000 shares: 5,000 × 120 = $600,000. Net: +$360,000 cash to invest and +3,000 net new shares (108,000 − 5,000 = 103,000 shares outstanding, NAV $12.36m). Check: 12.96m − 0.6m = 12.36m; 12.36m / 103,000 = $120 per share, unchanged. Interpretation: entries and exits at NAV never dilute the other holders, but the manager must raise cash for redemptions (hence cash drag).

**Yale spending rule.** Suppose last year's spending was $1.20m and endowment value two years ago was $25m. Spending = 0.8 × 1.20 + 0.2 × 5.25% × 25 = 0.96 + 0.2625 = **$1.2225m**. The smoothing gives stable budgets while converging to 5.25% of (lagged) value.

**Diversification ratio.** σ_EW = 17.9%, average single-asset σ = 24.9%: DR = 0.719 (source prints 71.0%). Diversification removed about 28% of the risk at no cost in expected return (15.1% both).

## Anti-patterns
- **Concentrating retirement savings in employer stock** (Enron: 62% of plan assets in company shares; price $90 to zero in a year): income and wealth then share one risk.
- **Choosing the best historical risk/return stock and assuming it persists**: absent a forecast, expect a random pick's risk-return.
- **Equal-weighting as "optimal"**: the same 15.1% return was obtained with σ = 15.6% via optimised weights (vs 17.9% equal-weighted). Composition matters.
- **Treating diversification as crisis insurance**: it reduces risk, does not eliminate it, and does not guarantee downside protection.
- **Skipping the IPS or never updating it**: no objective benchmark, no trigger for rebalancing.
- **Ignoring fees and tax in fund selection**: active funds combine higher fees, turnover and more capital-gain distributions than index funds.

## Exam Focus & Traps
- "Portfolios are most likely to provide": **risk reduction** (not risk elimination, not downside protection).
- IPS review: regularly (about every 3 years) and on a major life or circumstance change.
- Asset allocation is the decision usually viewed as having the **greatest impact** on performance.
- DC: the **employee** bears investment risk; DB: the **employer** bears funding risk. Do not swap.
- Insurers: life = longer-term, P&C = shorter-term liabilities; surplus account can be riskier than the general account.
- Bank: liquidity is paramount; risk tolerance low; horizon short.
- ETF vs mutual fund: ETFs trade intraday, can be shorted/bought on margin, pay out dividends, and have smaller minimums; mutual funds trade at NAV once a day.
- Closed-end funds can trade at a premium or discount; open-end funds never do (transact at NAV).
- Hedge funds: "2 and 20", high-water mark; PE: fees on committed capital, carry after LPs recover capital.
- Smart beta = rules-based factor tilts, not cap-weighted, higher fees than plain passive.
- **⚠ Correction (minor)**: the source prints the HKSE diversification ratio as 71.0%, but 17.9/24.9 = 71.9%. Use the formula, expect the printed 71% on the exam.

## Key Takeaways
1. Evaluate securities by contribution to total-portfolio risk and return; co-movement (correlation) is the key input.
2. Diversification lowers σ at constant expected return, but correlation spikes in crises erase most of the benefit (DR 99.4% in 2008-09).
3. Run the loop: IPS → asset allocation → security analysis → construction → monitoring/rebalancing → performance review, and feed results back into the IPS.
4. Map client type to horizon, risk tolerance, income and liquidity needs before choosing assets (banks/insurers conservative; endowments/SWFs long and illiquid-tolerant).
5. Know who bears the risk: DC = participant, DB = sponsor.
6. Active vs passive is a fee and revenue story: passive has 20% of assets but 6% of revenue; alternatives 15% of assets but about 43% of revenue.
7. Pick the vehicle by need: mutual fund (simple, daily NAV), ETF (intraday, cheap), SMA (custom), hedge fund/PE (illiquid, leveraged or long-lock, high fees).

## Connects To
- **ch05**: turns the diversification intuition into the math (covariance, correlation, two-asset variance).
- **ch06**: CAPM and performance ratios, the measurement layer of the feedback step.
- **ch07**: IPS construction (objectives, constraints) in full detail, and the planning/construction steps.
- **ch03**: market efficiency determines whether active management can add alpha after fees.
- **ch15**: active portfolio management analysis (fundamental law, information ratio).
- **ch18**: performance evaluation, the feedback step in depth.
- **`cfa-asset-allocation-cme` ch07**: mean-variance optimisation and asset allocation implementation.
