# Chapter 4: Value Shareholders: Buffett's Owner Earnings and Value in Banks
> **Source**: CFA Society Italy × Advisor Private, *Value Investing* guide (2020), Ch. 4 "Azionisti di valore" | Antonio Amendola; plus insert "Banche e Value Investing: opportunità o trappola?" (Francesco Castelli, CFA, Banor Capital; sponsor content, attributed where used)

## Core Idea
Value investors judge a business by the cash it really produces for its owners and by what management does with that cash. Buffett's measure of this is **owner earnings**, a cash-based, hard-to-manipulate alternative to reported net income. The chapter tests it in a simple long/short experiment on the Stoxx 600 ex-financials, and the Castelli insert shows the limits of a single balance-sheet ratio (P/B below 1 in European banks was a decade of false buy signals) and how Buffett used a structured, bond-like deal in Goldman Sachs to obtain a margin of safety.

## Frameworks Introduced
- **Buffett's two-block process**
  - Qualitative principles: type of business, durability of the business over time, reliability and transparency of management.
  - Quantitative principles: focus on return on capital rather than earnings per share; ability to create at least one dollar of market value for each dollar retained; value of the underlying assets.
  - Use: screen qualitatively first (can this business last, is management honest), then quantify with owner earnings.
- **Owner earnings**
  - What: the cash earnings available to owners after keeping the business running.
  - Formula: `Owner earnings = reported net income + D&A +/- other non-cash charges - average annual maintenance capex +/- change in working capital`.
  - How: take net income from the income statement; add depreciation and amortisation and other non-cash items such as stock-based compensation (from the cash-flow statement); subtract only the capex needed to maintain the status quo (growth capex excluded); adjust for working capital (an increase consumes cash).
  - Why it works: it shows both how cash is produced and how it is used (dividend, maintenance, growth). It is harder for management to manipulate than net income, and it focuses on long-run prospects instead of quarterly consensus beats.
  - Failure mode: maintenance capex must be estimated (it is not reported), and averaging over years is a judgement.
- **Where retained cash goes**
  - After paying dividends, the remainder either maintains facilities (book value stays flat) or buys new assets (book value grows and adds income). Growth in book from the second use plus dividends are both owner earnings.
- **Price-to-owner-earnings screen (practical test)**
  - What: rank stocks on P/E vs P/owner earnings and build sector long/short portfolios (long cheapest, short most expensive) in the Stoxx 600 excluding financials (financial statements are unsuited to these cash metrics).
  - Period: 31/12/2003-31/12/2019, with two sub-periods starting 31/12/2007 (global financial crisis) and 31/12/2009 (sovereign debt crisis).
  - Outcome reported: the owner-earnings portfolio outperformed both the index and the P/E portfolio in all three windows (charts only, no numbers given); the experiment is described by the author as simplistic.
  - Sector tilt: the owner-earnings portfolio concentrated in sectors usually labelled growth.

## Key Concepts
- **Owner earnings**: reported earnings adjusted to cash available after maintenance investment.
- **Maintenance capex**: spending required to keep current capacity; distinct from growth capex.
- **Working capital**: current assets minus current liabilities; changes absorb or release cash.
- **Non-cash charges**: items such as employee stock compensation added back when computing cash earnings.
- **Retained earnings test**: a company should create at least one dollar of market value for every dollar retained.
- **Return on capital vs EPS**: value investors prefer capital efficiency to per-share earnings, which can be inflated by buybacks or leverage.
- **Value is a life-cycle phase**: a sector is not inherently value or growth; value stocks appear in tech and healthcare at certain times.
- **Book value as convention**: bank book value reflects historical accounting; assets carried at 100 may no longer be worth 100.
- **Structured margin of safety**: protection obtained through instrument terms (coupon, seniority, redemption premium, warrants) rather than through price alone.
- **Subordinated debt as value instrument**: when equity is trapped by regulation, bond investors may collect the cash flow instead.

## Formulas & Reference Tables
- `Owner earnings = NI + D&A +/- other non-cash - maintenance capex +/- change in working capital`.
- `P/OE = market capitalisation / owner earnings` (or price per share / OE per share).
- Sector weights in the two long/short portfolios (entire period, % of portfolio):

| Sector | P/E portfolio | P/OE portfolio |
|---|---|---|
| Travel & Leisure | 10 | 2 |
| Oil & Gas | 15 | 9 |
| Telecom | 15 | 6 |
| Auto & Parts | 17 | 2 |
| Utilities | 2 | 16 |
| Construction & Materials | 7 | 8 |
| Technology | 1 | 20 |
| Healthcare | 5 | 18 |
| Industrial & Consumer Goods | 10 | 14 |
| Basic Resources | 18 | 5 |

Reading: P/E favours cyclical, capital-intensive sectors with depressed earnings (Basic Resources, Auto, Oil & Gas, Telecom); P/OE favours cash-generative sectors, including Technology and Healthcare.

## Mental Models
- **Use owner earnings when comparing companies with different capex needs**: a low P/E on a capital-hungry business may hide that most earnings must be reinvested just to stand still.
- **Use "cash in, cash out" analysis when evaluating management**: ask what they do with retained cash and whether each dollar creates a dollar of value.
- **Use sector-neutral thinking**: look for the value phase of a business, not a value sector.
- **Use balance-sheet reclassification before trusting P/B**, especially in banks: compare earning power under market conditions with peers and add credit analysis.
- **Use structure when equity is uncertain**: if you like the franchise but not the timing, a senior or preferred claim with a high coupon can deliver the margin of safety that the common stock cannot.

## Worked Example
Owner earnings (illustrative inputs, recomputed).
- Inputs: net income 100; D&A 40; stock compensation 10; average maintenance capex 55; increase in working capital 5.
- Steps: 100 + 40 + 10 - 55 - 5 = 90.
- Result: owner earnings 90 (10% below net income). At market cap 900, P/E = 9.0 but P/OE = 10.0.
- Interpretation: net income overstated distributable cash by 10%; a screen on P/E alone would rank this company cheaper than it is.

Goldman Sachs 2008 deal (figures as given by Castelli, partial recompute).
- Terms: USD 5bn perpetual preferred paying 10%, redeemable in 2011 at a 10% premium; warrants on 43.5m shares at 115 versus a market price of 126.
- Steps: three years of coupons = 3 x 10% x 5bn = 1.5bn; redemption premium = 0.5bn; strike discount 115/126 - 1 = -8.7% (the source calls it 10%); the source reports about 3.1bn total profit including the 2013 warrant exercise, a return of 3.1/5 = 62% over five years, versus +35% for the stock.
- Interpretation: the contractual cash flows alone gave 2.0bn (40%); the warrant added equity upside; the coupon structure meant the huge price swings (stock halved again within weeks) did not matter.

## Anti-patterns
- Using trailing or quarterly reported earnings as the sole measure of value.
- Treating "low P/B" as a buy signal for banks without reclassifying the balance sheet and analysing credit quality; European banks traded below book for over a decade.
- Assuming value investing means avoiding tech, healthcare or other "growth" sectors.
- Counting growth capex as maintenance capex (understates owner earnings) or ignoring it altogether (overstates it).
- Confusing a good company at a fair price with a fair company at a great price (Castelli, citing Buffett).
- Arriving at a panic without cash; being unable to buy when prices collapse.
- Reading the experiment as proof: it was short, simple, with no costs and no portfolio construction constraints.

## Practitioner Notes
- Owner earnings is a long-run lens: investors should care how much value the company creates and how it returns to them in cash.
- Buffett's Goldman investment shows courage under panic, quality focus (a franchise he called unrivalled), tolerance of macro mistakes (he expected the bail-out plan to pass immediately; it was rejected and then approved a month later), and use of a bond-like instrument for protection. Position was largely closed in 2020.
- Banks after 2008: US banks cleaned up through state intervention and became dominant again; in Europe aid was staggered, the sovereign debt crisis (2011) depressed growth and profitability, and equity holders received little (few dividends, no buybacks) while regulators forced capital to roughly double. Subordinated and perpetual debt offered attractive spreads with improving credit quality; the ECB froze dividends in 2020 but expected coupons on perpetuals to be paid.
- Looking forward from April 2020: bank balance sheets far stronger than in 2008, systemic role supports state backing; dividend resumption could make bank shares a legitimate value holding.

## Key Takeaways
1. Owner earnings equals net income plus non-cash charges minus maintenance capex, adjusted for working capital.
2. Buffett cares about what management does with retained cash, not just what the company earns.
3. A P/owner earnings screen in the Stoxx 600 ex-financials outperformed both P/E and the index in the guide's (simple) test.
4. Value is a phase in a company's life; sectors labelled growth appear in value portfolios.
5. P/B below one is not enough for banks: check accounting conventions, credit risk and the ability to distribute cash.
6. An instrument-structured margin of safety (coupon, seniority, warrants) can substitute for a low equity price.
7. Panic buying requires liquidity prepared in advance.

## Connects To
- **ch01**: margin of safety and quality of management.
- **ch03**: value traps (energy, banks) and the role of profitability.
- **ch05**: combining value with other factors to avoid single-metric traps.
- **`cfa-financial-statement-analysis`**: cash-flow adjustments and quality of earnings.
- **`cfa-equity-portfolio-management`**: valuation inputs and style screens.
