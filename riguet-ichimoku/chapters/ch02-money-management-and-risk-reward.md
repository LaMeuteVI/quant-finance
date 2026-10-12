# Chapter 2: Money Management and Risk/Reward
> **Source**: Patrick Riguet, *Ichimoku Kinko Hyo — La formation totale* (French), Part 1 "Le money management" and "Le ratio risque rendement" | retail FX/CFD trader-educator

## Core Idea
Survival comes from two rules: risk a fixed small percentage of capital per trade by adapting position size to the stop distance, and only enter when the take profit is at least twice the stop distance. Together they let a trader lose more often than he wins and still make money, and they make wide swing-trading stops affordable. This chapter gives the exact numbers.

## Frameworks Introduced
- **Fixed-fractional risk rule (1% per trade, 2% per day)**
  - When to use: before every entry, any horizon (scalping, intraday, swing).
  - How: (1) maximum loss per trade = 1% of capital; (2) maximum total loss per trading day = 2%; (3) compute size from the stop distance (next framework).
  - Why it works / failure mode: constant percentage risk keeps every loss small relative to the account; the author cites that 69 consecutive losers at 1% are needed to lose half the capital (0.99⁶⁹ ≈ 0.50). Failure: it assumes losses are taken at the stop; gaps, slippage, widened stops or correlated open positions (several trades in the same currency) break the 1% ceiling.
- **Position-size formula (lot sizing from the stop)**
  - When to use: after the stop is fixed, before sending the order.
  - How: `size (value per pip) = capital × risk% ÷ stop distance in pips`. Then loss at stop = stop pips × size = capital × risk%.
  - Why it works: the rule is identical for a 25-pip or a 200-pip stop, so wide stops are not scary, only smaller in size.
- **Minimum 2:1 reward-to-risk filter**
  - When to use: as the final gate of every trade (after signal, filter and target are identified).
  - How: (1) set the stop from structure; (2) set the take profit from structure (next flat, channel bound, range bound: ch04, ch06, ch07); (3) compute `R:R = (TP − entry) ÷ (entry − stop)` for a long; (4) if R:R ≥ ~2 enter; if clearly below, abstain or wait for a pullback that improves the ratio; a slightly lower ratio (about 1.9) may be tolerated, not a dogma.
  - Why it works / failure mode: with R:R = 2 the break-even win rate is 1/(1+2) ≈ 33%. Failure: stretching the target to hit 2:1 when no structure supports it.
- **Range-trading ratio advantage**: stop just beyond the rejection wick and target just short of the opposite bound give ratios far above 2:1 (ch07); the author says no other method gives comparable ratios.

## Key Concepts
- **Capital at risk per trade**: the loss booked if the stop is hit; 1% of capital, fixed regardless of stop size.
- **Daily loss cap**: 2% of capital per trading day (author's rule; implies stopping after two full stops at 1%).
- **Pip value / lot size**: the money per pip; the adjustable variable in the sizing formula.
- **Risk/reward ratio (R:R)**: take-profit distance divided by stop distance.
- **Average trader**: someone who loses more often than he wins yet is not losing money thanks to ratios.
- **Risk of ruin**: theoretical ruin avoided because the risk percentage is identical on all positions.
- **Break-even stop (BE)**: stop moved to entry price so the trade can no longer lose (used in ch07, ch08).
- **Pyramiding**: adding positions on pullbacks while raising earlier stops (ch08); total risk must still respect the cap.
- **Wide-stop instruments**: CAD pairs, EURNZD, GBPNZD, gold and oil produce "killer wicks"; use wider stops and correspondingly smaller size.

## Formulas & Reference Tables
- `size = capital × r ÷ stop_pips` (r = risk fraction, e.g. 0.01).
- `loss_at_stop = stop_pips × size = capital × r`.
- `R:R = reward_pips ÷ risk_pips`.
- `break-even win rate = 1 ÷ (1 + R:R)`; expectancy per trade in R units = `p × R:R − (1 − p)`.
- `capital after n straight losers = capital × (1 − r)ⁿ`; losers to halve the account = `ln(0.5) ÷ ln(1 − r)`.

| Capital | Risk | Stop (pips) | Size (€/pip) | Loss at stop |
|---|---|---|---|---|
| 10,000 | 1% | 50 | 2 | 100 |
| 10,000 | 1% | 25 | 4 | 100 |
| 10,000 | 1% | 200 | 0.5 | 100 |

| R:R | Break-even win rate |
|---|---|
| 1:1 | 50% |
| 2:1 | 33.3% |
| 3:1 | 25% |
| 4:1 | 20% |

## Mental Models
- **Size is the dependent variable**: the stop is set by the chart, the size by the stop. Never choose a stop to fit a desired size.
- **Ratio as peace of mind**: a high ratio lets you lose several trades in a row without doubting the method.
- **Aggressive is not reckless**: aggressive entries (anticipating on lower time frames, ch07) exist to raise the ratio, but they never waive entry rules.
- **Pips are vanity, money is sanity**: a series with fewer pips won can still be profitable.

## Worked Example
Author's 5-trade sequence, capital 10,000, risk 1% (100), all at 2:1:

| Trade | Stop (pips) | TP (pips) | Result |
|---|---|---|---|
| 1 | 25 | 50 | loss, −100 |
| 2 | 135 | 270 | loss, −100 |
| 3 | 15 | 30 | win, +200 |
| 4 | 45 | 90 | loss, −100 |
| 5 | 35 | 70 | win, +200 |

Losers: 25+135+45 = 205 pips, −300. Winners: 30+70 = 100 pips, +400. Net = +100 despite −105 pips net. (All figures recomputed.)

Author's entry check (EURAUD trend trade, ch08): entry 1.3145, stop 1.3080 (65 pips), target 1.3285 (140 pips). R:R = 140 ÷ 65 = 2.15 → validated. Size at 1% on 10,000 = 10,000 × 0.01 ÷ 65 ≈ 1.54 €/pip.

## Anti-patterns
- **Fixed lot size regardless of stop**: makes wide stops impossible and kills swing trading.
- **Entering below 2:1 "because the signal is perfect"**: the author skipped a perfect SP500 weekly breakout for this reason.
- **Moving the stop after entry**: breaks the ratio; only tiny exceptional adjustments (5–6 points).
- **Evaluating by pips or win rate alone**.
- **Ignoring correlation**: several 1% positions on the same currency exceed the intended risk (inference, not in the book).

## Practitioner Notes
- ⚠ Correction (nuance): the author states that losing three range trades and winning the fourth still yields a profit. At exactly 2:1 that sequence is −3R + 2R = −1R, a net loss. It holds only if R:R > 3:1, which range trades (stop beyond the wick, target at the opposite bound) can provide, so it is correct for range setups, not for the generic 2:1 rule.
- The 69-loser claim: ln(0.5)/ln(0.99) = 68.97 losers, i.e. 69. At 2% it would take 34.
- Discipline on entry: "if the target is not at least twice the stop, stay out" also thins out signals, which tests patience (author's own remark).
- The daily 2% cap implies at most two full-risk losers per day.

## Key Takeaways
1. Risk 1% of capital per trade, 2% per day maximum.
2. Size = capital × risk% ÷ stop distance; wide stops mean small size, not no trade.
3. Fix stop and target from structure before sizing.
4. Enter only with R:R ≥ ~2:1; otherwise abstain or wait for a pullback.
5. R:R of 2 needs only a 33% win rate to break even.
6. Range setups give the best ratios; trend breakouts close to the target often fail the filter.
7. Do not evaluate in pips.

## Connects To
- **ch01**: the emotional rules that keep these numbers respected.
- **ch07**: range trading delivers the highest R:R.
- **ch08**: pyramiding and break-even management under the same risk cap.
- **`passarelli-option-greeks` ch17**: disciplined position sizing and scenario risk in an options book.
- **`cfa-portfolio-management` ch08**: generic risk management (risk budgeting, limits).
