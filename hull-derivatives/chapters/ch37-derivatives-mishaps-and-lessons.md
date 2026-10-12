# Chapter 37: Derivatives Mishaps and What We Can Learn from Them

## Core Idea
The big derivatives losses were rarely caused by the instruments themselves. They came from hedgers turning into speculators, weak controls, blind trust in models and ignored liquidity risk. The central lesson is **clear risk policy set by senior management, enforced by independent controls**.

## Frameworks Introduced
- **Lessons for all users**:
  1. **Define risk limits**: set them at board level, translate them to individual desks, and monitor them daily.
  2. **Take the risk limits seriously**: punish breaches even when they produced profits.
  3. **Do not assume you can outguess the market**.
  4. **Do not underestimate the benefits of diversification**.
  5. **Carry out scenario analyses and stress tests**.
- **Lessons for financial institutions**:
  - Monitor traders carefully, including star traders. Separate the front, middle and back office.
  - **Do not blindly trust models**: large profits from simple strategies suggest a model error.
  - Be conservative in recognizing inception profits on exotic trades.
  - **Do not sell clients inappropriate products** (the reputational and legal risk comes back).
  - **Beware of easy profits**.
  - **Do not ignore liquidity risk**: prices of illiquid products drift from model values in stress.
  - **Beware when everyone is following the same trading strategy** (crowded trades: 1987 portfolio insurance, LTCM).
  - **Do not make excessive use of short-term funding for long-term needs** (Northern Rock, 2007).
  - Market transparency matters. Manage incentives. **Never ignore risk management**.
- **Lessons for nonfinancial corporations**:
  - **Make sure you fully understand the trades you are doing**.
  - **Make sure a hedger does not become a speculator**.
  - Be cautious about making the treasury department a profit center.

## Key Concepts
- **Rogue trader**: unauthorized positions concealed by fictitious trades or weak back-office controls.
- **Model risk**: pricing or hedging errors from wrong assumptions, parameters or implementation.
- **Liquidity black hole**: everyone sells at once and there is no counterparty.
- **Crowded trade**: many firms hold the same position, which amplifies unwinds.

## Mental Models
- **If it looks like free money, look for the hidden risk**: model error, liquidity risk or tail risk.
- **Controls > models**: most disasters would have been prevented by position limits and independent checks.
- **Hedging policy must state what is *not* allowed**, not only what is.

## Reference Tables
| Case | Loss | Root cause |
|---|---|---|
| Barings (Leeson, 1995) | ≈ $1bn | Unmonitored Nikkei futures/options; the trader also ran the back office |
| Société Générale (Kerviel, 2008) | > $7bn (€4.9bn) | Unauthorized index futures positions, concealed |
| UBS (Adoboli, 2011) | $2.3bn | Unauthorized index positions |
| Allied Irish Bank (Rusnak) | ≈ $700m | Fictitious FX option trades |
| Amaranth (2006) | $6bn | Concentrated natural gas bets |
| LTCM (1998) | ≈ $4bn | Leverage + flight to quality + illiquidity |
| Kidder Peabody (Jett) | $350m | Systems booked forward accruals as profit |
| Midland Bank | $500m | Wrong interest rate bet |
| Sumitomo | ≈ $2bn | Copper spot/futures/options, single trader |
| Shell (Japan) | $1bn | Unauthorized FX futures |
| Metallgesellschaft | $1.3bn | Rolling short futures vs long supply contracts |
| Orange County (Citron, 1994) | ≈ $2bn | Leveraged bet that rates would not rise |
| Hammersmith & Fulham (1988) | ≈ $600m | Speculative sterling swaps; contracts voided |
| Allied Lyons (1991) | $150m | Selling USD/GBP calls |
| Procter & Gamble (1994) | ≈ $90m | Exotic leveraged swaps with Bankers Trust |
| Gibson Greetings (1994) | ≈ $20m | Exotic rate derivatives with Bankers Trust |

## Anti-patterns
- **Letting one person both trade and settle** (Barings).
- **Rewarding profits that exceeded risk limits**.
- **Treasury as a profit center without limits** (Orange County, Allied Lyons, P&G).
- **Buying products the treasury cannot value independently** (P&G, Gibson).

## Worked Example
**Diagnosing a "too good" P&L (Kidder Peabody pattern).**
- A desk reports steady profits from buying Treasury strips and "reconstituting" bonds forward.
- Question to ask: *what risk earns this return?* Answer: none. The system recognized the forward/spot price difference, which is just the time value of money, as profit.
- Control that would have caught it: an independent P&L attribution that splits carry, market moves and new trades. The "profit" appears only in an unexplained bucket.

## Key Takeaways
1. Define risk limits at board level and enforce them even on profitable breaches.
2. Separate front, middle and back office. Monitor star traders especially closely.
3. Distrust models that show easy profits. Stress-test for liquidity and crowded exits.
4. Corporates: understand every trade, and never let hedgers become speculators.
5. Most mishaps were control failures, not failures of the instruments.

## Connects To
- **Ch 1**: hedgers vs speculators.
- **Ch 2**: LTCM.
- **Ch 3**: Metallgesellschaft.
- **Ch 4**: Orange County.
- **Ch 5**: Kidder Peabody.
- **Ch 7**: Hammersmith & Fulham.
- **Ch 22**: VaR and stress tests.
- **Ch 34**: P&G.
