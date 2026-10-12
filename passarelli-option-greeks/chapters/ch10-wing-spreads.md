# Chapter 10: Wing Spreads (Condors and Butterflies)
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Chapter 10 · Part: Spreads

## Core Idea
Wing spreads (condors, iron condors, butterflies, iron butterflies) are **two vertical spreads glued together**, which gives two breakevens and lets a trader profit from something stock trading cannot deliver: a truly neutral market. Treat them first as **break-even analysis trades**: pick strikes whose breakevens bracket the range you believe in, using IV-implied standard deviations. Then manage them with the Greeks: delta and theta for directional butterflies, delta/gamma for adjusting a threatened iron condor, and vega when professionals flip the structure (buy the guts, sell the wings) to trade volatility.

## Frameworks Introduced
- **The wing-spread family** (all legs same underlying and expiry; equal strike distances between the two verticals):

  | Spread | Legs (A < B < C < D) | Cash | Profit when |
  |---|---|---|---|
  | Long condor | +A, −B, −C, +D (all calls or all puts) | debit | underlying between B and C |
  | Short condor | −A, +B, +C, −D (all calls or all puts) | credit | underlying moves away from B–C (max beyond A or D) |
  | Short iron condor | +A put, −B put, −C call, +D call | credit | between B and C |
  | Long iron condor | −A put, +B put, +C call, −D call | debit | underlying moves away from B–C (max beyond A or D) |
  | Long butterfly | +1 A, −2 B, +1 C (all calls or all puts) | debit | at B |
  | Short butterfly | −1 A, +2 B, −1 C | credit | away from B |
  | Short iron butterfly | +A put, −B put, −B call, +C call | credit | at B |
  | Long iron butterfly | −A put, +B put, +B call, −C call | debit | away from B |

  - Long = debit, short = credit. What matters is **which strikes are long and which are short**.
  - Because a call debit spread ≡ put credit spread on the same strikes, **long condor ≡ short iron condor** and **long butterfly ≡ short iron butterfly**.
  - Best case: debit verticals expire with both options ITM, credit verticals with both OTM.
  - "Selling the guts (middle strikes) and buying the wings (outer strikes)" = the neutral, low-realized-vol income stance; the wings only cap the loss on otherwise naked shorts.
- **Butterfly vs condor choice**:
  - Butterfly: higher max profit, but only at one price (B); narrow profit zone.
  - Condor / iron condor: lower max profit, **wider range** where max payout occurs ("wiggle room"). Higher probability ↔ lower payout. Risk and reward are always parallel.
  - Prefer the iron version when its OTM options have tighter bid-ask spreads than the ITM options of the plain version (less edge given up).
- **Keys to success: candidate selection for neutral wing spreads**:
  1. Technicals: has the stock traded inside the intended range for the past few months? Trendlines, support/resistance; ADX or MACD to detect a trend (trend = bad candidate).
  2. Fundamentals: nothing on the agenda (no earnings, FDA decisions, major announcements before expiry).
  3. Numbers: is the payout/risk ratio (e.g., 0.65 vs 4.35) acceptable for this stock, industry and market environment?
  - Many iron-condor traders prefer ETFs and indexes: diversification removes single-name gaps.
- **Strike selection by standard deviation (the trader's shortcut)**:
  - Deannualize IV with the √256 convention (16² = 256 trading days) to get a 1σ move to expiry.
  - Sell the short strikes near ±1σ for ≈ 68% (two-thirds) chance that the underlying stays inside.
  - **Strikes too close** (QQQ 54/55/57/58 at $55.95): good payout/risk ratio, but a $3.26 profit range (−2.8%/+3.0%) is too tight for a month; long-run loser.
  - **Strikes too far** (DJX 120/123/142/145 in 2007 low vol): the put spread sells for zero, the call spread for 0.10. No payoff, and a year later DJX was ~50% lower. Always price in unexpected volatility.
- **The "being selective" edge argument**:
  - If IV is an unbiased forecast of realized vol and you trade at fair value, you break even in the long run.
  - Non-market-makers sell the bid and buy the offer ("giving up the edge"), and iron condor losers are 3–5× the winners (max profit/max loss usually < 1:3). The 1σ iron condor is therefore a statistical loser unless you have a view.
  - Rule: **sell the 1σ iron condor only when you believe there is more than a two-thirds chance of neutrality**, i.e., realized vol will be lower than implied.
- **Directional butterfly**: buy the fly centered on your price target (all OTM calls for bullish, all OTM puts or ITM calls for bearish). Cheaper than the vertical, higher nominal max profit, but loses if the move overshoots the upper wing. The P&L comes from delta and theta jointly; Greeks are tiny at entry. Works best in **trending, low-volatility stocks**.
- **Managing a threatened iron condor (the "safe landing")**:
  1. Inaction: accept that some trades lose (only for traders with a proven edge).
  2. Close the whole spread: "if you don't have an opinion, you shouldn't have a position".
  3. Dismantle piecemeal: buy back the nearly worthless short on the safe side (cheap, removes a delta that would hurt on a retrace); leave the worthless long wing (free optionality); close or adjust the tested side.
  4. If you now believe in the move, **buy back the tested short strike** so the position becomes a long strangle/long call with delta in the direction of your forecast.
- **Condor as a long-volatility (vega) trade (the pro's use)**: buy the guts, sell the wings (short condor). Center the underlying between the long strikes: delta/gamma ≈ flat, vega positive, theta negative. Put it on **before** the catalyst ("buy the rumor, sell the news") and keep it short-term because theta is large relative to vega.

## Key Concepts
- **Wing spread**: a 3- or 4-strike structure made of two verticals sharing a direction of risk.
- **Guts**: the middle strike(s) of a wing spread.
- **Wings**: the outer strikes, bought (neutral stance) or sold (vol-buying stance).
- **Condor**: four strikes, same option type; equal-width outer verticals.
- **Iron condor**: condor built from a put vertical below and a call vertical above.
- **Butterfly**: 1 × 2 × 1 at three equidistant strikes, same option type.
- **Iron butterfly**: short (long) straddle at B with long (short) wings at A and C.
- **Break-even analysis trade**: a trade judged mainly by where the underlying ends relative to its breakevens.
- **Wiggle room**: the extra distance between breakevens a condor provides versus a butterfly.
- **Double dip**: an iron condor collects two credits, and only one side can lose at expiry.
- **Standard deviation (σ) move to expiry**: IV scaled to the trading days remaining times the price.
- **Giving up the edge**: the expected-value cost of trading at the bid/offer instead of theoretical value.
- **Directional butterfly**: an OTM fly centered on a price target, used as a cheap directional bet.
- **Buy the rumor, sell the news**: IV rises into uncertainty and falls once the news is out.

## Formulas & Reference Tables
- Butterfly (width w = B − A = C − B), debit D: `Max profit = w − D` at S_T = B; `Max loss = D`; `BE = A + D` and `C − D`.
- Short iron condor, credit C, vertical width w: `Max profit = C` for B ≤ S_T ≤ C_strike; `Max loss = w − C`; `BE_low = B − C`, `BE_high = C_strike + C`.
- Trader's σ-to-expiry shortcut (author's convention):
  `σ_$ = (IV / √256) × √(trading days to expiry) × S`, and strikes at `S ± σ_$` bracket ≈ 68% of outcomes.
  - √256 = 16 assumes 256 trading days; the exact count is ~252 (gives slightly wider bands). Use **trading** days, not calendar days.
  - This is a normal (not lognormal) approximation that ignores drift and interest.
- Payout-to-risk ratio of an iron condor = `C / (w − C)`; typically < 1:3.
- Position Greeks = Σ (contracts × per-contract Greek); in the author's tables deltas are in "contracts", so −2.54 delta = short 254 shares.
- Vega-vs-theta break-even time for a long-vol structure: `days = (vega × ΔIV) / |theta|`.

## Mental Models
- **Think of every wing spread as two verticals.** One of them is guaranteed to win at expiry (the stock can't be above and below); only one side can lose, but you must defend both sides independently.
- **Butterfly = precision, condor = tolerance.** Choose by how confident you are in the pin.
- **The short strike is a price you are willing to be wrong at; place it at ±1σ only if you think realized < implied.**
- **Use a fly, not a vertical, when your target is specific and the stock trends slowly; use the vertical when an overshoot is plausible.**
- **When the market moves against a neutral position, it is no longer neutral.** Read the new delta and re-underwrite the view.

## Worked Example
**1. UPS July 65/70/75 long call butterfly vs 60/65/75/80 iron condor** (UPS $70.65).

| | Legs | Net | Max profit | Max loss | Breakevens |
|---|---|---|---|---|---|
| Butterfly | +65C 6.60, −2×70C 2.50, +75C 0.40 | debit 2.00 | 3.00 at $70 | 2.00 (< 65 or > 75) | 67 / 73 |
| Iron condor | +60P 0.20, −65P 0.50, −75C 0.40, +80C 0.05 | credit 0.65 (0.30 put + 0.35 call spread) | 0.65 between 65–75 | 4.35 (< 60 or > 80) | 64.35 / 75.65 |

The condor widens each breakeven by 2.65 but risks 4.35 to make 0.65.

**2. SPX 1σ strikes**: SPX 1241, IV 23.2%, 50 calendar days = 35 trading days.
`σ = 0.232/16 × √35 × 1241 = 106.45` → band 1134.55 – 1347.45 → sell the 1135 puts and 1350 calls for ≈ 2/3 odds. (With √252: 107.3.)

**3. Iron condor adjustment** (10 lots; stock $90, IV 16.5%, 41 days ≈ 29 trading days → σ ≈ 0.165/16 × √29 × 90 ≈ 5.0): buy 80P 0.05, sell 85P 0.35, sell 95C 0.55, buy 100C 0.05 → credit 0.80 ($800); max loss (5 − 0.80) × 1,000 = $4,200. One week later the stock is $93 and the spread is worth 1.10 (−$300).

| Leg (10 lots) | Value | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|---|
| +80 put | 0.00 | 0.000 | +0.010 | 0.000 | +0.020 |
| −85 put | 0.07 | +0.340 | −0.150 | +0.050 | −0.220 |
| −95 call | 1.24 | −3.840 | −0.810 | +0.310 | −1.090 |
| +100 call | 0.21 | +0.960 | +0.360 | −0.130 | +0.550 |
| **Net** | **1.10** | **−2.54** | **−0.590** | **+0.230** | **−0.740** |

(Signs reconstructed; the extraction lost the minus signs.) Delta −2.54 ≈ short 254 shares into a rally the trader fears. Adjustment: buy back the 85 puts (0.07, no-brainer) and the 95 calls. What remains is a long 80/100 strangle, effectively **long ten 100 calls**: Δ +0.96, Γ +0.37, Θ −0.13, vega +0.57. The trader has turned a short-delta position into a long-delta one consistent with the new forecast.

**4. CRM short condor as a vol play** (CRM $104.32, 59 days, 100 lots): sell 90C 17.40, buy 95C 13.75, buy 115C 3.80, sell 120C 2.55 → credit 2.40. Net Greeks (sum of legs): Δ +0.70, Γ +0.51, Θ −1.50 (−$150/day), vega +4.0 (+$400 per IV point). A +5-point IV rise earns $2,000, which theta consumes in 13 days ($1,950). The trade must be short-term and needs the catalyst soon.

## Anti-patterns
- **Choosing condor strikes by feel on the payout ratio**: a 0.63/0.37 QQQ condor looks attractive but its breakevens sit ±3% away over a month. The probability, not the ratio, is the problem.
- **Wings so far OTM that the credit is zero**: all risk, no reward; and "unlikely" tails do happen (DJX −50% within a year of 2007).
- **Selling 1σ iron condors mechanically**: with bid-ask edge and 1:4 payoffs, the strategy loses in the long run unless you forecast realized < implied.
- **Trading neutral wing spreads through earnings, FDA rulings or other catalysts**.
- **Directional flies without accepting the overshoot risk**: a fly can lose if you are "too right".
- **Expecting a directional fly to pay on an early move**: Greeks at entry are tiny (WAG Δ +0.008); the profit needs theta near the center strike.
- **Freezing when an iron condor is tested**: the position has a real delta now; close, dismantle or re-position.
- **Buying condor vega after the news**: IV is already priced in; buy the rumor, sell the news.

## Practitioner Notes
- Retail loves iron condors for limited risk and high win rates ("nobody tells stories about their losing condors"). Pros with low commissions and margin more often use wing spreads to trade **volatility**, including buying the guts/selling the wings.
- Four-leg commissions and margin make vega trading with wing spreads impractical for most non-professionals; portfolio-margined accounts are better equipped.
- Author's numbers: iron condor max profit/max loss usually < 1:3; for every $1 of potential profit, $4–5 are at risk.
- Cheap way to lock in: after a move, the far-OTM short on the untested side often costs pennies (0.07). Buy it back rather than carry a delta that bites on a retracement; keep worthless long wings as free lottery tickets.
- IV-to-probability conversion (±1σ ≈ 68%) is only as good as your belief that the market's IV is right; the edge comes from disagreeing with it for identifiable reasons.
- A bearish fly = all OTM puts (or all ITM calls) centered on the downside target.
- Catalysts suitable for a long-vol condor: rumored product launch, product recall, management change, any shake-up raising uncertainty.

## Key Takeaways
1. Wing spreads = two verticals; long condor ≡ short iron condor, long fly ≡ short iron fly on the same strikes.
2. Butterfly for a precise pin (bigger payout, narrow zone); condor for a range (smaller payout, wide zone).
3. Select strikes with the σ-to-expiry shortcut, `IV/16 × √(trading days) × S`, and sell ±1σ only when you expect realized vol below implied.
4. Screen candidates: range-bound chart, no trend (ADX/MACD), no scheduled events; prefer indexes/ETFs.
5. A tested iron condor has real delta; buy back cheap shorts, and if you believe the move, lift the tested short to flip the delta.
6. Directional flies are cheap target trades whose payoff depends on theta as much as delta.
7. Reverse the structure (buy guts, sell wings) to trade rising IV, before the catalyst and for a short holding period.

## Connects To
- **ch09**: verticals, the building blocks of every wing spread; box/synthetic equivalence.
- **ch12**: trading implied volatility; the condor as an IV position.
- **ch13**: realized volatility and gamma, the risk that "kicks in" when an iron condor is tested.
- **ch15**: strangles and straddles, what an adjusted iron condor becomes.
- **ch16**: ratio and complex spreads (broken-wing variants).
- **`hull-derivatives` ch12**: butterfly and condor payoff diagrams.
- **`hull-derivatives` ch19**: gamma/theta trade-off behind the neutral wing spread.
- **`cfa-derivatives` ch05**: L3 volatility-based option strategies (straddles, collars, spreads) and their use for a given market view.
