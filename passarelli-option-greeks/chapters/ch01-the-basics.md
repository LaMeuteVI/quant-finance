# Chapter 1: The Basics
> **Source**: Dan Passarelli, *Trading Option Greeks: How Time, Volatility, and Other Pricing Factors Drive Profits*, 2nd ed. (Bloomberg Press / Wiley, 2012), Part I, Chapter 1

## Core Idea
Every option position, however exotic its name, is a combination of four building blocks: **buy call, sell call, buy put, sell put**. Each block has a fixed at-expiration shape (hockey stick) and a characteristic *motive*. Long options are bought when a trader wants limited risk and expects volatility to rise. Short options are sold when a trader expects a quiet market or wants to be paid to take on an obligation. At-expiration diagrams teach the shapes, but most options are closed before expiry. So a trader needs the greeks (ch02) to forecast what the option will be worth *before* expiry.

## Frameworks Introduced
- **The four basic positions and their true forecasts**:

  | Position | Risk / reward | Forecast it really expresses | Break-even at expiry |
  |---|---|---|---|
  | Long call | Limited risk (premium) / unlimited reward | Bullish, and happy to see volatility rise | `K + C` |
  | Short (naked) call | Limited reward (premium) / unlimited risk | **Not bullish**, which is different from bearish | `K + C` |
  | Long put | Limited risk / substantial reward (down to zero) | Bearish, and happy to see volatility rise | `K − P` |
  | Short put | Limited reward / large risk (down to zero) | **Not bearish**, or "willing to own the stock at K − P" | `K − P` |
  | Covered call (long stock + short call) | Capped upside / stock downside minus premium | Neutral to moderately bullish | `S₀ − C` |
  | Protective put (long stock + long put) | Floor at K / unlimited upside minus premium | Bullish but afraid of a volatility spike | `S₀ + P` |

  - When to use: use this table to map a view (direction plus volatility) onto the simplest structure before you build spreads. A spread is any combination of these legs.
  - Why it matters: the short call and the short put are *not* directional bets in disguise. If the trader expected a collapse, he would short stock or buy puts. Selling calls monetizes "the stock won't rally much" and nothing more.

- **Opening vs. closing orders and open interest accounting**:
  - Buy-to-open or sell-to-open *creates* contracts. Buy-to-close or sell-to-close *extinguishes* them. A trade between one opener and one closer only transfers an existing contract.
  - Volume resets every period. Open interest is a running total of contracts outstanding. Rule: OI rises by the traded quantity only when both sides open, falls when both sides close, and is unchanged when one side opens and the other closes.

- **Stock vs. option choice (the call-vs-stock trade-off)**:
  - Above the strike at expiry, a long call always underperforms the stock by exactly the premium. Below the strike, it loses at most the premium, while the stock can fall to zero.
  - Prefer the call when volatility is expected to rise or a large decline is feared. Park the unused capital in an interest-bearing vehicle (this is the root of the rho and put-call parity carry logic, ch06–ch07).
  - Leverage cuts both ways: the same cash buys many more deltas. The book's example gets about 26 calls for the price of 100 shares, so the trader either takes less risk or gets far more exposure.

- **Assignment risk management for short options**: equity options are American-style, so a short call can be assigned at any time. The trader then holds unintended short stock that does not expire, which extends the risk period and costs extra commissions. Rule of practice: *close short ITM options before expiry* if you never wanted the stock position.

## Key Concepts
- **Option**: a contract giving the owner the right to buy (call) or sell (put) a fixed quantity of an underlying at the strike price, until or at expiration.
- **Holder / writer**: the long party owns the right. The short party (writer) carries the obligation and gets **assigned** when the holder **exercises**.
- **OCC (Options Clearing Corporation)**: the central counterparty that guarantees every listed US option. After the trade, it is the counterparty to every exercise and assignment. Clearing members assign customers randomly or FIFO. When the deliverable is ambiguous (for example after corporate actions), the OCC is the authority.
- **Option series vs. class**: a *series* is one strike, one expiry and one type within a *class*. A *class* is all options on the same underlying deliverable. Corporate actions (splits, spin-offs, special dividends) can create several classes with non-standard deliverables. The book's example is Ford in 2000, where F, XFO and FOD each delivered a different package.
- **Contract size / multiplier**: usually 100 shares, so a premium of 5.00 costs $500.
- **Moneyness**: a call is ITM if S > K, ATM if S ≈ K and OTM if S < K. For puts it is the reverse.
- **Intrinsic value**: the ITM amount. `max(S − K, 0)` for a call and `max(K − S, 0)` for a put.
- **Time value (premium over parity)**: premium minus intrinsic value. An option with no time value trades **at parity**.
- **American vs. European exercise**: American options can be exercised or assigned any time up to expiry. European options only at expiry. The label has nothing to do with geography. US single-stock and ETF options are American. Many index options are European.
- **Cash settlement**: index options (for example SPX) deliver `(ITM amount) × $100` in cash, not shares.
- **AM settlement**: the final settlement value is computed from the constituents' *opening* prices on expiration-Friday morning, so the last trading day is Thursday.
- **ETF options (SPY, QQQ)**: physically settled in 100 ETF shares, American-style. Know the scale ratio to the index: SPY is about 1/10 of the S&P 500 and QQQ about 1/40 of the Nasdaq-100.
- **LEAPS**: long-dated listed options, with about 1 to 2.5 years to expiry. **Weeklys** are one-week options.
- **Cash-secured put**: a short put backed by cash equal to `K × 100 − premium`, so an assignment can be paid for without margin.
- **Married put**: stock and put bought together as one spread. A protective put added to stock already held is economically the same.

## Formulas & Reference Tables
- `Time value = Premium − Intrinsic value`
- Long call at expiry: `P&L = max(S_T − K, 0) − C`. Break-even `K + C`. Max loss `C`.
- Short call at expiry: `P&L = C − max(S_T − K, 0)`. Break-even `K + C`. Max gain `C`.
- Long put: `P&L = max(K − S_T, 0) − P`. Break-even `K − P`. Max gain `K − P`.
- Short put: `P&L = P − max(K − S_T, 0)`. Break-even `K − P`. Max loss `K − P`.
- Covered call: max profit `(K − S₀) + C`. Break-even `S₀ − C`.
- Protective put: max loss `(S₀ − K) + P`. Break-even `S₀ + P`.
- Index option cash settlement: `(S_settle − K) × 100` for a call.

**Contract conventions (as of the 2012 edition)**

| Item | Convention in the book |
|---|---|
| Expiry | Saturday after the 3rd Friday, with Friday the last trading day. ⚠ Since 2015 the OCC uses the 3rd **Friday** as the expiration date. The economic substance is unchanged. |
| Strike spacing | $1, $2.50, $5 or $10 depending on price level and liquidity |
| Listed months | At least 4, and up to 6 with LEAPS |
| HOLDRs | Baskets whose holders keep voting and dividend rights. ⚠ These products were wound down in 2011–2012, so treat them as historical. |

## Mental Models
- **"Options are created, stock is borrowed."** A short option needs no borrow, so every long option contract has a short counterpart and shorting options is as common as buying them. Shorting stock is much rarer than buying it.
- **Think of a short option as selling insurance.** The premium is the most you can earn. The loss is the tail you insured.
- **Buy options when you expect volatility to rise, sell them when you expect it to fall.** This is the book's recurring thesis. Directional views only decide *which* option to use.
- **The at-expiration diagram is the final exam, not the daily quiz.** It shows the destination. Greeks (ch02) show the path, which is what you actually trade.
- **A covered call and a short put are cousins.** Both are "not bearish, capped upside, stock-like downside" (this is formalized by synthetics in ch06).

## Worked Example
**Four blocks, one set of numbers** (per share, 1 contract = 100 shares):

| Trade | Inputs | Break-even | Max gain | Max loss |
|---|---|---|---|---|
| Long INTC 22.50 call | S = 22.25, C = 0.85 | 23.35 | Unlimited | 0.85 |
| Naked short TGT 50 call | S = 49.42, C = 1.45 | 51.45 | 1.45 | Unlimited |
| Covered call TGT | Long stock at 49.42, short 50 call at 1.45 | 47.97 | (50 − 49.42) + 1.45 = **2.03** | 47.97 (stock to 0) |
| Short BA 65 put | S = 69.77, P = 1.20 | 63.80 | 1.20 | 63.80 |
| Long SPY 139 put | S = 140.35, P = 2.30 | 136.70 | 136.70 | 2.30 |
| Protective put SPY | Long ETF at 140.35 + 139 put at 2.30 | 142.65 | Unlimited | (140.35 − 139) + 2.30 = **3.65** |

- **Leverage check (long call)**: if INTC ends at 27, the profit is `(27 − 23.35)/0.85 ≈ 429%` on the premium. The stock returns `(27 − 22.25)/22.25 ≈ 21%`. Below 22.50 the call loses 100%. For the same $2,225 as 100 shares, the trader can buy ≈ 26 calls (2,225/85 = 26.2), which is the rights on about 2,600 shares.
- **Cost of insurance (protective put)**: 2.30/140.35 ≈ **1.6%** of the position, paid up front to defer the sale until the risk window passes.
- **Cash-secured put sizing**: to be ready for assignment on 1 BA 65 put, hold $6,500 − $120 premium = $6,380 in cash.

## Anti-patterns
- **Reading a naked call as a bearish trade**: its payoff is capped at the premium. If you expect a crash, a naked call is the wrong tool.
- **Planning with at-expiration diagrams only**: most options are closed before expiry, and the P&L along the way is driven by delta, gamma, theta and vega, not by the hockey stick.
- **Ignoring early assignment on American shorts**: this leaves you with an unwanted stock position over a weekend or event.
- **Selling puts without funding the assignment**: decide up front whether the put is cash-secured or margined (about 50% of the stock value).
- **Assuming the deliverable is 100 shares after a corporate action**: check the class with the OCC.
- **Confusing volume with open interest**: high volume with flat OI can simply be the same contracts changing hands.

## Practitioner Notes
- Choose between a call and the stock by your *volatility* expectation as much as your direction. If you fear a large drop but are bullish, buy the call and keep the cash in T-bills.
- The covered-call writer must be happy both to own the stock at the current price *and* to sell it at the strike. If either is false, use a different structure.
- A short put used as a "paid limit order" gives an effective purchase price of `K − P`, even if the stock ends only slightly below K. If the put is not assigned, the premium is kept. That is its edge over a plain limit order.
- For SPX-style European, AM-settled index options, the settlement print is Friday's opening value. Positions held into Thursday's close carry overnight gap risk that you cannot trade out of.
- Retail brokers tier their approvals. Naked calls require the highest level and the highest margin because the risk is unlimited.

## Key Takeaways
1. Every strategy is built from four legs, so learn each leg's shape, break-even and motive.
2. A short call is *not bullish* and a short put is *not bearish*. Neither is a directional conviction trade.
3. Buy options when you expect volatility to rise, and sell them when you expect it to fall.
4. A long call trades a fixed underperformance equal to the premium for a floor on losses. It also frees up capital that earns interest.
5. American-style shorts carry assignment risk at any time. Close them if you do not want the stock.
6. The OCC is the counterparty to every listed trade and the final word on deliverables.
7. Most options are closed early, so value them with greeks, not only with expiry payoffs.

## Connects To
- **ch02**: greeks, the tool for pricing options before expiry.
- **ch04**: why long options suffer theta and short options suffer gamma.
- **ch06**: synthetics, which explain why a covered call ≈ short put and a protective put ≈ long call.
- **ch08**: dividends and early exercise of American options.
- **`hull-derivatives` ch10–ch11**: option mechanics, bounds and early exercise properties.
- **`hull-derivatives` ch12**: payoff diagrams of spreads built from the four blocks.
- **`cfa-derivatives` ch05**: covered calls and protective puts in a portfolio context.
