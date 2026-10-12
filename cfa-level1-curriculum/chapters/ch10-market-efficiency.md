# Chapter 10: Market Efficiency (Equity)

## Core Idea
In an informationally efficient market, prices reflect new information quickly and rationally. Abnormal risk-adjusted returns are then impossible once information costs and trading costs are counted. Efficiency comes in weak, semi-strong and strong forms. Documented anomalies and behavioral biases challenge it, but many of them disappear after costs or after risk adjustment.

## Frameworks Introduced
- **Market value vs intrinsic value**:
  - Market value is the transaction price. Intrinsic value is what a fully informed investor would pay.
  - Active management bets that the two differ.
- **What makes a market efficient**:
  - Many active participants and analysts (large caps are more efficient than small caps).
  - Information availability; **Reg FD** requires fair disclosure.
  - Few **limits to trading** (arbitrage is possible, short selling is allowed).
  - Low transaction and information-acquisition costs.
  - In equilibrium, prices only need to be efficient *within* those costs.
- **Three forms (Fama)**:

| Form | Prices reflect | What cannot earn abnormal returns |
|---|---|---|
| Weak | All past market data (prices, volume) | Technical analysis |
| Semi-strong | All public information | Fundamental analysis of public data |
| Strong | Public + private information | Even insiders |

- **Evidence**: developed markets are broadly weak- and semi-strong-form efficient. They are **not strong-form efficient**: insiders earn abnormal returns, which is why insider trading is illegal.
- **Implications**:
  - Fundamental analysis earns only a normal return for its cost, but it is what *makes* markets semi-strong efficient.
  - Technical analysis should not work.
  - Portfolio management: favor passive, low-cost strategies. The manager's role becomes diversification, risk tolerance and tax management.
- **Anomalies**:
  - **Time-series**:
    - Calendar: the January effect (tax-loss selling, window dressing), turn-of-the-month, day-of-the-week, weekend, holiday effects.
    - Momentum (short-term continuation).
    - Overreaction (long-term reversal).
  - **Cross-sectional**: the **size effect** (small caps outperform) and the **value effect** (value beats growth). These may be risk factors, not inefficiencies (Fama–French).
  - **Other**:
    - Closed-end fund discounts to NAV (fees, liquidity, tax).
    - Post-earnings-announcement drift after earnings surprises.
    - IPO first-day underpricing followed by long-run underperformance.
- **Behavioral finance**: markets can be rational even when individuals are not.
  - **Loss aversion**: losses hurt more than equal gains please.
  - **Herding**.
  - **Overconfidence**.
  - **Information cascades**.
  - **Representativeness**.
  - **Mental accounting**.
  - **Conservatism**: slow updating.
  - **Narrow framing**.

## Key Concepts
- **Abnormal return**: actual − expected (risk-adjusted) return.
- **Joint hypothesis problem**: a test of efficiency is also a test of the asset-pricing model used to define "expected".
- **Data mining / snooping**: anomalies found by searching many strategies.

## Mental Models
- **Ask "after costs and risk?"** before calling anything an anomaly.
- **Efficiency is a spectrum, not binary**: large-cap developed markets are more efficient than small caps or frontier markets.
- **Fundamental analysts are paid to make the market efficient.** Their competition removes the edge.

## Anti-patterns
- **Chasing published anomalies**: they often decay once widely known.
- **Mistaking a risk premium (size, value) for mispricing**.
- **Assuming efficiency means prices are always "right"**: it means mispricings are not *exploitable* after costs.
- ⚠ **Correction vs the notes**: the January effect is attributed to December **tax-loss selling** (realizing capital *losses* to offset gains), not to "creating tax liabilities".

## Worked Example
**Abnormal return test.** A stock returns 12% in a year when the market returns 8%. r_f = 2% and β = 1.5.
- CAPM expected return = 2% + 1.5 × (8% − 2%) = **11%**.
- Abnormal return = 12% − 11% = **+1%**. It is statistically meaningful only if it persists across many stocks or periods, beyond costs, and is not due to model error (the joint hypothesis problem).

## Key Takeaways
1. Efficiency is about prices reflecting information fast enough that abnormal profits vanish after costs.
2. Weak form defeats technical analysis. Semi-strong defeats public-information analysis. Markets are not strong-form efficient.
3. Anomalies (calendar, momentum, size, value, IPOs, closed-end discounts) often reflect risk, costs or data mining.
4. Behavioral biases explain some mispricing, but markets can still be efficient in aggregate.
5. Implication: low-cost passive investing is a strong default.

## Connects To
- **Ch 8**: arbitrage and short selling.
- **Ch 9**: indexes as passive vehicles.
- **Ch 13**: intrinsic value estimation.
- **`pairs-trading-partial-cointegration` skill**: statistical arbitrage as a test of weak-form efficiency.
