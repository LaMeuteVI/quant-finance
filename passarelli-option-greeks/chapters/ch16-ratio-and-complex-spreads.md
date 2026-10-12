# Chapter 16: Ratio Spreads and Complex Spreads
> **Source**: Dan Passarelli, *Trading Option Greeks* (2nd ed., Wiley/Bloomberg 2012), Ch. 16 · Advanced Option Trading

## Core Idea
Ratio spreads (backspreads and ratio verticals) are volatility positions whose gamma, theta and vega change sign as the stock crosses the strikes, so they cannot be judged from an at-expiration diagram or from the net credit/debit. Professional market makers take this to the limit: they run a large multi-strike book and manage it purely through net greeks, delta hedges, quote skewing and skew trades. The skill is tailoring the greeks to a forecast and hedging the unknown, not predicting it.

## Frameworks Introduced
- **Backspread** (more long options than short, same class and expiry; e.g. sell 1 × 70 call, buy 2 × 75 calls, 1:2): net long gamma/vega above the short strike, net short gamma/vega below it.
  - When to use: expect a volatile move (especially in the direction of the long strikes), want long vega at a low IV, and skew lets you buy the cheaper-IV strike and sell the richer one.
  - How: size large enough that gamma scalping is worthwhile; judge by delta, gamma, theta, vega at the current price and at other prices (not by the credit); compare the IV of BOTH legs with RV and IV history; hedge delta but anticipate the sign flip of gamma.
  - Failure mode: delta-hedging too aggressively into the negative-gamma zone (buying stock as the price falls, then being long when it keeps falling), and the IV/price inverse relationship (vega turns negative just where IV tends to rise).
- **Ratio vertical spread** (more short options than long, same class and expiry; e.g. buy 1 × 70 call, sell 2 × 75 calls): mirror image of the backspread.
  - When to use: expect low realized and implied volatility with the stock drifting to the short strike at expiry; accept naked-call tail risk.
  - How: best case is the stock pinned at the short strike (max theta, but also peak negative gamma); hedge delta only when a trend into deep negative-gamma territory looks likely; if volatility is rising, buy back part of the short options (cuts delta, gamma and vega together, but usually locks in a loss).
  - Failure mode: a violent rally through the naked strike; "nothing good can come of looking back", so close on forward-looking logic.
- **Delta lean**: deliberately under- or over-hedge to offset the hidden directional risk that comes from vega changing with the stock price.
  - When to use: experienced vol trader, position greeks flat here but asymmetric on one side.
  - How: simulate the position in a model first; lean short if losses (negative gamma/vega) sit below the market, long if above. Keep the lean only if it reduces risk on both sides.
  - Failure mode: a lean that loses in both directions with no help from other greeks; the fix is closing, not leaning.
- **Risk reversal (delta-neutral skew trade)**: long call, short put at a different strike, stock hedge at the delta ratio; bets that an abnormal skew reverts.
  - When to use: skew between equidistant OTM strikes is far from its "normal" level.
  - How: compare the current call-vs-put IV gap to its usual gap; trade only the excess; hedge delta.
  - Failure mode: short vega on the downside and long vega on the upside is the wrong way round given that IV rises when stocks fall and falls when they rally.
- **Market-maker greek management**: hedge delta at once; then shade bids and offers (lower them when long gamma/vega, raise them when short) to trade out of option-centric risk; never take more than can be spread off.

## Key Concepts
- **Ratio spread**: options bought and sold in a fixed quantity ratio (1:2 is a "one-by-two"; 20:40 is still a one-by-two).
- **Backspread**: long the larger quantity, typically long the farther-OTM strike; a long-volatility play near the long strikes.
- **Ratio vertical spread**: short the larger quantity; a short-volatility play near the short strikes; unlimited risk on the naked side.
- **Dynamic greeks**: gamma, theta and vega of a two-strike position change sign as the stock moves across the strikes.
- **Trading the skew**: a backspread buys the lower-IV strike and sells the higher-IV strike (vertical skew), earning IV "edge" but adding vega-direction risk.
- **Overhedging**: buying/selling stock for delta that later reverses sign because gamma flipped.
- **Underhedging / leaning**: hedging only part of delta on purpose.
- **Paper (order flow)**: customer orders that market makers must react to.
- **Theoretical edge vs actual profit**: buying below and selling above the mid creates theoretical profit; it becomes cash only through sound position management.
- **Risk reversal**: delta-neutral long call/short put (or the reverse) used to trade skew.
- **Synthetic straddles in a book**: at a strike where a delta-neutral trader is net short N options, it is equivalent to N/2 short straddles, since "a put is a call, and a call is a put" when hedged.
- **Trading flat**: minimizing delta, theta, vega and rho exposure while earning the bid-ask spread.
- **Portfolio greeks**: net greeks across all classes, the real measure of diversification.

## Formulas & Reference Tables
Expiry payoffs per 1:2 structure (K₁ = 70 short/long, K₂ = 75, net 1.00):
- Backspread (sell 1×K₁ call, buy 2×K₂ calls, credit c = 1.00): `P&L(S) = 2·max(S−75,0) − max(S−70,0) + 1.00`
  - Lower breakeven `K₁ + c = 71`; max loss `(K₂−K₁) − c = 4.00` at S = 75; upper breakeven `K₂ + 4.00 = 79`; profit above 79 is unlimited; below 70 profit = credit 1.00.
- Ratio vertical (buy 1×K₁ call, sell 2×K₂ calls, debit 1.00): `P&L(S) = −[backspread P&L]`
  - Max loss below 70 = debit 1.00; max profit at S = 75 = `(K₂−K₁) − 1.00 = 4.00`; breakevens 71 and 79; unlimited loss above 79.
- Alternative: buy 2 × 75 calls outright for 1.10 each: `P&L(S) = 2·(S−75) − 2.20`, max risk 2.20, breakeven `75 + 2.20/2 = 76.10`. ⚠ Correction: the book quotes 77.20, which is the breakeven for ONE call bought at 2.20; with two calls it is 76.10. The conclusion (smaller risk than the backspread's 4.00, lower breakeven than 79, twice the delta above it) still holds.
- Skew trade hedge (risk reversal, long call, short put): `shares to short = 100 × N × (Δ_call + |Δ_put|)` where Δ_put is the put's (negative) delta; the short put adds positive delta, so the stock short offsets both.
- Market-maker straddle equivalent: `short straddles = net short options at strike ÷ 2` (1,006 ÷ 2 = 503).

| Position (stock 71, 1 month) | Δ | Γ | Θ | Vega | Reading |
|---|---|---|---|---|---|
| 20:40 call backspread | −0.46 | + | − | + | long vol at 71 |
| 20:40 ratio vertical | +0.46 | − | + | − | short vol at 71 |
| Backspread at 62-66 (well below short strike) | −1.46 to −2.63 | −0.35 to −0.11 | +0.23 to +0.17 | −0.36 to −0.16 | short-vol face: needs calm, low IV |
| Backspread at 68-78 | −2.50 rising to positive (+10 or more at 78) | +0.29 to +1.70 | −0.04 to −1.22 | +0.26 to +2.27 | long-vol face: needs movement, higher IV |

(Exhibit 16.3 lost its minus signs in OCR; signs here are reconstructed from the text: gamma/vega negative and theta positive with the stock below roughly 67, the reverse above. The ratio vertical, Exhibit 16.6, is the exact mirror. Magnitudes are per the book's 20:40 position units.)

## Mental Models
- **Two-faced position**: a ratio spread is a long-vol and a short-vol trade glued together; ask "which face is showing at the current price, and which at my stop price?"
- **Price is not risk**: for ratio spreads the credit or debit is irrelevant; risk is delta/gamma/theta/vega at each spot level.
- **Hedge the unknown, not the forecast**: the talented trader is a disciplined risk manager, not a clairvoyant.
- **Hidden directional risk**: delta-neutral is not direction-indifferent when vega depends on the stock level.
- **Supply and demand for greeks**: market makers move quotes to offload gamma/theta/vega, exactly like ordinary supply and demand but for risk factors.
- **Casino model**: take the other side of flow at a theoretical edge, cap any one series' risk, diversify across classes.

## Worked Example
Backspread 20:40, stock 71, 1 month: sell 20 × 70 calls at 3.20 (IV 32), buy 40 × 75 calls at 1.10 (IV 30), credit 1.00 per spread (recomputed: 3.20 − 2 × 1.10 = 1.00, or $2,000 total).
1. Expiry map: breakevens 71 and 79, max loss 4.00 at 75, credit kept below 70.
2. Skew: buying 30 vol and selling 32 vol = 2 vol points of edge.
3. Greeks at 71: Δ −0.46, Γ +, Θ −, vega + (long IV play).
4. Hedging: at 68 the delta is about −2.50 (250 shares short). Buying 250 shares flattens it, but if the stock falls to 62 the natural delta goes to −1.46 and the shares add +2.50, leaving roughly +1.0 long as gamma has flipped to negative. Underhedge (buy 100-200 shares) to keep a cushion.
5. Risk: if the stock falls through 70, vega turns negative just as IV tends to rise; if it rises into positive-vega territory, IV tends to fall. The 2-point skew edge must be weighed against this.
Ratio vertical (mirror, 1:2): 1 × 70 call bought at 3.20, 2 × 75 calls sold at 1.10, debit 1.00 (20 × 40 lot: $2,000). Max profit 4.00 at 75, breakevens 71 and 79. Going 1:3 turns it into a small credit (source states 0.05; with the rounded prices shown it computes to 0.10) but doubles the naked call exposure.
Market-maker example: Ford position, stock 15.72, delta +1,075, gamma −10,191, theta +1,708/day, vega +7,171, rho 33,137 (OCR signs approximate). Short 1,006 January 15 options is about 503 short straddles, the source of negative gamma; long 1,927 January 2003 20-strike options is the source of positive vega; the book behaves like a time spread plus a ratio between the 15 and 17.5 strikes (1,006:439).

## Anti-patterns
- **Judging a ratio spread by its credit/debit**: the credit is not risk or reward; greeks are.
- **Fully hedging delta mechanically in a backspread**: gamma flips sign and you end up wrong-footed.
- **Ignoring vega vs price correlation**: the wrong-way IV move exactly where vega turns sign.
- **Going 1:3 for a credit without sizing the naked tail**.
- **Holding a loser "to see" (looking back)**: decide on forward greeks and outlook.
- **Leaning delta with no simulation**, or continuing a lean that loses both ways.
- **Quoting unchanged when you are loaded with gamma/vega** (market-maker error): shade your bids/offers.
- **Concentrating in one class**: portfolio greeks, not single-position greeks, define risk.

## Practitioner Notes
- Scalping a 1:2 backspread with one lot is pointless: gamma ≈ 0.05 and delta ≈ 0.02 means under 10 deltas to scalp per point, so size matters; it also requires professional or portfolio margin.
- Market makers hedge nearly every trade's delta immediately with the underlying, especially large-delta trades, then spread off gamma/theta/vega.
- Illiquid options trade "by appointment only", so a position can be stuck until expiry; do not assume scalp exits.
- Skew example: 10% OTM call typically 4 vol points below the 10% OTM put (55 calls at 21, 45 puts at 25 on a $50 stock); when the gap blows out to about 9 points (put 32 vs call 23), sell the put, buy the call, short the right amount of stock.
- Holding positions in several option classes gives psychological detachment; diversification shows up in net portfolio greeks.
- When a put or call "is the same thing" after hedging, net options per strike matter, not call vs put.

## Key Takeaways
1. Read ratio spreads through dynamic greeks at several stock prices, not through the P&L diagram or credit.
2. A backspread is long vol near its long strikes and short vol below the short strike; the ratio vertical is the reverse.
3. Check the IV of both legs; backspreads trade vertical skew, but vega sign flips in the same region that IV moves against you.
4. Do not reflexively hedge to flat delta in a backspread; anticipate the gamma sign flip and underhedge if needed.
5. Buy back part of the short leg of a ratio vertical when volatility may rise; it reduces delta, gamma and vega together.
6. Use delta leans only when simulation shows lower risk on both sides; otherwise close.
7. Manage the book as net greeks: move quotes to shed gamma/theta/vega, diversify classes, know up-and-down risk.
8. Trade skew (risk reversal) only for excess deviation from the stock's normal skew, and respect its vega-vs-price trap.

## Connects To
- **ch03**: volatility skew and term structure underlying backspread edge.
- **ch09**: vertical spreads the ratio variants are built on.
- **ch10**: wing spreads as capped-risk alternatives to naked tails.
- **ch12**: delta-neutral trading of implied volatility.
- **ch13**: gamma scalping and realized vol.
- **ch15**: straddle/strangle equivalence for book analysis.
- **ch17**: using greeks to choose strategies and adjust.
- **`hull-derivatives`**: Greek hedging and portfolio greeks management.
