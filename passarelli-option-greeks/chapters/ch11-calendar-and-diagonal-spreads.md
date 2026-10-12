# Chapter 11: Calendar and Diagonal Spreads
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Chapter 11 · Part: Spreads

## Core Idea
Time spreads (calendars, double calendars, diagonals, double diagonals) combine options of **two expirations**, so at-expiration diagrams fail: at the front-month expiry you still own an option with time value, which must be valued with a model and the Greeks. A long calendar is a **gamma/theta trade with long vega**, the one structure where gamma and vega carry opposite signs: the trader wants low *realized* volatility but benefits from higher *implied* volatility. Because two months are involved, calendar-family spreads are true **volatility spreads**: they let you trade the term structure of IV, not just direction, realized vol and overall IV level.

## Frameworks Introduced
- **Calendar (time, horizontal) spread**: long one option, short another of the same type and strike, different expiries.
  - **Buying the calendar** = sell the short-term ATM option, buy the long-term ATM option (net debit).
  - Greeks of a long ATM calendar: delta ≈ 0, **gamma −, theta +, vega +**, rho small (+ for calls, − for puts).
  - Best case: the underlying sits at the shared strike when the front month expires. The short leg expires worthless, the long leg has its maximum value.
  - Max loss (downside) = the debit. Upside loss ≈ debit − interest carried by the deep-ITM long call (an estimate that ignores residual time value).
  - Max profit = model value of the back-month option at the strike on front expiry minus the debit; estimate it with a pricing model at unchanged IV.
- **Income-calendar checklist (Richard's rules)**:
  1. Forecast a range around the strike through the front expiry.
  2. Buy back-month IV in the **lower third of its 12-month range** ("buy low, stay low").
  3. Check that no event is pending that could move IV or the stock.
  4. A rise in IV is not really wanted: front-month IV usually rises more (you lose more on the short than you gain on the long), and rising IV signals anxiety and future movement.
- **Delta-hedging a calendar**: size the tolerable move with gamma; when gamma plus time create unwanted deltas, **sell stock to flatten long deltas, buy stock to flatten short deltas**. Accept the new price level and keep collecting theta.
  - Time passing makes a calendar's delta drift positive when the stock falls, because the short-dated call's delta decays toward zero faster than the long-dated call's.
- **Rolling for a "free" call**: buy a 6–12-month option, sell one-month options against it, rolling each month (sell the next month after expiry, or buy the expiring short at 0.05–0.10 and sell the next as a spread). Once aggregate short premium exceeds the long option's cost, the long option is "paid for" (earned, with risk). Then:
  - Bearish view → sell the long option (residual value is profit).
  - Bullish view → hold it (delta gains).
  - Neutral view → keep writing against it.
  - Risk: the stock staying pinned for months is unlikely ("Russian roulette"); it is still a negative-gamma trade each month.
- **Trading volatility term structure**:
  - **Sell the front, buy the back** (long calendar) when front IV is rich (e.g., Feb 50 vol vs May 35). Risks: (a) IVs diverge further; (b) back-month IV falls with front-month IV. Back-month vega is larger, so a smaller drop in back IV can wipe out the front gain.
  - Market-maker mechanics behind (b): dealers who sold front-month options to customers buy back-month options to hedge gamma, lifting back IV; when customers sell front vol back, dealers dump the back months and back IV falls too.
  - **Buy the front, sell the back** (short calendar: gamma +, theta −, vega −) when front IV is cheap (e.g., 17 front vs 25 back). Two causes: (1) short-term complacency (premium sellers prefer front months for theta and shorter risk) → bet on front IV recovering; (2) an anticipated event after front expiry (lawsuit, product) → bet on back IV normalising, which is more speculative. Main danger: back IV keeps rising into the event while realized vol stays low. You then lose on theta and vega.
  - Filter the IV history: remove one-off spikes (read the news of the time) before judging "cheap vs expensive".
- **Directional calendars (the outfielder model)**: a calendar at a strike away from the market is directional. **Strike = where** the stock must be, **front expiry = when**.
  - Strike above the market → bullish (calls: long OTM back delta > short OTM front delta; puts: short ITM front delta dominates).
  - Strike below the market → bearish.
  - Movement is needed, but not too much (negative gamma). Theta collapses and can turn negative away from the strike.
- **ITM vs OTM calendar choice ("the in-or-out crowd")**: call and put calendars at the same strike behave alike; prefer the **OTM** one because ITM options have wider bid-ask (more edge conceded, twice per spread, compounded by monthly rolls) and early-assignment risk (calls before dividends, deep ITM puts because of interest). An assigned deep-ITM short put leaves long stock + deep-ITM long put, which is roughly the same delta-flat position.
- **Double calendar**: two calendars, same months, two strikes. Long double calendar = negative gamma/positive theta with **two target prices**. Short double calendar = positive gamma/negative theta that can be gamma-scalped. As an IV play, often a put calendar at the lower strike + a call calendar at the upper strike (**strangle swap**).
- **Diagonal**: different strikes and different expiries (horizontal + vertical), more delta-focused. Long back-month lower-strike call + short front-month higher-strike call = bullish diagonal.
  - Judge the IV difference net of **vertical skew** (the higher strike should trade at lower IV) and of **bid-ask width in vol points** (`width / vega`).
  - Diagonal vs straight calendar at the target strike: more delta and more debit, versus less delta and less at risk.
- **Double diagonal**: a call diagonal + a put diagonal = an iron condor with front-month guts and back-month wings (= long back strangle + short front strangle). Advantages: higher theta, can be rolled, can exploit term-structure discrepancies. Unlike a same-month iron condor, vega is **positive**.

## Key Concepts
- **Calendar / time / horizontal spread**: same strike, different expiries.
- **Buying (selling) the calendar**: long the back month and short the front month (and the reverse).
- **Term structure of volatility**: IV by expiry month; its "skew" is what calendars trade.
- **Volatility spread**: a position in the difference between two IVs (months or strikes).
- **Rolling the spread**: closing the expiring short and selling the next month.
- **"Free" call**: a long back-month option whose cost has been recovered by cumulative short-premium sales.
- **Strangle swap**: long back-month strangle vs short front-month strangle (put calendar low + call calendar high).
- **Diagonal spread**: different strikes and different expiries.
- **Double diagonal**: iron condor with front-month short strikes and back-month long wings.
- **Vertical skew**: IV difference across strikes within one month.
- **Bid-ask width in vol points**: `(ask − bid) / vega`.
- **Negative scalping**: buying stock to maintain delta in a negative-gamma trade, then selling it lower on a retracement.

## Formulas & Reference Tables
- Calendar value at front expiry (S = K): `Spread = V_back(S=K, T_back − T_front, σ_back)`; `Profit = Spread − Debit`.
- Upside loss estimate (calls): `Loss ≈ Debit − K × r × τ`, where τ = time remaining on the back month at front expiry.
- Position Greek in $ = Greek × 100 × contracts (the author's tables show position Greeks "per contract" × lots, so theta 0.18 on 20 lots = $18/day).
- Delta after a move: `Δ_new ≈ Δ_old + Γ × ΔS` (plus a time-drift term for calendars).
- Vega P&L when months move independently: `P&L = Σ_i vega_i × ΔIV_i × 100`. A convergence trade needs `|vega_front| × ΔIV_front > |vega_back| × ΔIV_back`.
- Roll break-even: the long option is "free" when `Σ short credits ≥ cost of the long option`.

| Structure | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|
| Long ATM calendar | ≈ 0 | − | + | + |
| Short ATM calendar | ≈ 0 | + | − | − |
| Long calendar, strike above spot | + | − | + | + |
| Long double calendar | ≈ 0 | − | + | + |
| Bullish call diagonal (long low-strike back, short high-strike front) | + | − (small) | + | + |
| Double diagonal (short front strangle, long back wings) | ≈ 0 | − | + | + |

## Mental Models
- **A long calendar is short realized vol and long implied vol.** You want the stock still and IV firm, especially in the back month.
- **Think of the calendar as a rubber band**: negative gamma keeps stretching delta away from zero, and the strike keeps pulling the P&L back to the peak.
- **The outfielder**: distance = strike, timing = front expiry. Catch the ball at both.
- **The back month has the bigger vega.** Any calendar is mostly a bet on back-month IV, whatever you believe about the front.
- **Prefer OTM calendars over ITM ones**: same Greeks, less edge given up, no early-assignment headaches.

## Worked Example
**1. BBBY Jan/Feb 57.50 call calendar** (BBBY $57.50; Jan 25 days, Feb 53 days; IV 23%, r 2%): sell Jan 57.50C 1.30, buy Feb 57.50C 2.10 → debit 0.80.

| | At entry (spread 0.80) | At Jan expiry, S = 57.50 (spread = Feb call 1.53) |
|---|---|---|
| Delta | +0.009 | +0.523 |
| Gamma | −0.036 | +0.107 |
| Theta | +0.009 | −0.027 |
| Vega | +0.027 | +0.065 |

Best case: 0.80 → 1.53 = **+91%**. The put calendar (1.95 − 1.20 = 0.75 → 1.45) gives +93% with negative rho. 20-lot version: Δ +0.18 (18 shares), Γ −0.72, Θ +$18/day. A week later BBBY −$1: theta earned ≈ 7 × $19 ≈ $133, roughly offsetting the delta loss; delta ≈ +0.90 (+ time drift) → sell ~100 shares to flatten.

**⚠ Correction**: the author estimates the upside max loss as 0.80 − 0.17 = 0.63, using interest on 57.50 over 53 days. At January expiry only 28 days remain on the February call, so the carry is ≈ 57.50 × 2% × 28/365 ≈ 0.09 and the loss ≈ 0.71 (the text's "plus 0.28" is also inconsistent).

**2. Rolling to a "free" December call** (XYZ $60): sell July 60C 1.45, buy Dec 60C 4.00 → debit 2.55. At July expiry with XYZ at $60, the Dec call is worth 3.60 → +1.05 (+41%).

| Roll | July (29d) | Aug (29d) | Sep (36d) | Oct (29d) | Nov (29d) |
|---|---|---|---|---|---|
| Credit | 1.45 | 1.45 | 1.60 | 1.45 | 1.45 |
| Cumulative | 1.45 | 2.90 | 4.50 | **5.95** | 7.40 |
| Dec call value | 4.00 | 3.60 | 3.20 | 2.70 | 2.20 |

After three rolls, 4.50 > 4.00: the call is "free" (**⚠ Correction**: the book's exhibit prints 6.95 for October; 4.50 + 1.45 = 5.95).

**3. Term-structure calendar** (stock $164.15, 10 lots): sell 22-day July 165C at 7.10 (45% IV), buy 85-day Sep 165C at 12.60 (38% IV) → debit 5.50. Net Δ +0.369, Γ −0.089, Θ +0.945, vega +1.522 (+$152 per parallel vol point). By leg: July vega −1.604, Sep +3.127.
- July IV −8 pts, Sep unchanged: +1.604 × 100 × 8 = **+$1,283**.
- July IV +1 pt: −$160.
- July −8 and Sep −4: +1,283 − 1,251 ≈ **+$32**, i.e. the trade is flat. Back-month vega ≈ 2× front.

**4. Diagonal vs calendar** (AAPL $405.10; Jan 22 days, Feb 50 days): sell Jan 420C 5.35 (29% IV), buy Feb 400C 21.80 (32% IV) → debit 16.45; Δ +0.255, Γ −0.005, Θ +0.037, vega +0.239. The IV gap is explained by bid-ask (0.10 wide ≈ 0.29 vol pts on the Jan, vega 0.34; ≈ 0.18 on the Feb, vega 0.57) plus normal vertical skew. The straight Jan/Feb 420 calendar costs 12.15 − 5.35 = 6.80 with Δ ≈ 0.07 (Feb 420 Δ 0.39 vs Feb 400 Δ 0.57): less delta, less at risk.

**5. Double diagonal** (JPM $49.85, 10 lots; Aug 33 days): buy Sep 55C 0.30 (19%), sell Aug 52.50C 0.40 (20.5%), sell Aug 47.50P 0.50 (24.4%), buy Sep 45P 0.45 (26%) → **credit 0.15**; Δ −0.032, Γ −0.842, Θ +0.146, vega +0.183. ATM IV 22.9% ≈ 20-day HV 23%, and the term-structure differences are explained by skew, so this is a pure theta trade. After August: sell the Septembers, hold them, or sell Sep 47.50/52.50 to convert into a standard iron condor.

## Anti-patterns
- **Drawing an at-expiration diagram for a calendar**: only the downside max loss is certain. Use model values at the front expiry.
- **Buying calendars when back-month IV is historically high**: you are long vega where it matters most.
- **Assuming a calendar is neutral**: negative gamma means the delta keeps moving; hedge with stock or accept the drift.
- **Trading a vol-convergence calendar looking only at net vega**: the months move independently. Look at each leg's vega.
- **Using ITM calendars when an OTM one gives the same exposure**: more edge conceded twice (and monthly on rolls), plus early-assignment risk.
- **Buying stock to chase delta in a negative-gamma diagonal**: invites negative scalping on a retracement.
- **Selling a calendar to fade rich back-month IV ahead of a known event**: IV can keep rising into the event while the stock stays still, so you lose on both theta and vega.

## Practitioner Notes
- Conservative time-spread traders buy the 2-month option and sell the 1-month one (fewer earnings months, shorter risk window). Market makers and savvy retail traders often buy 6–12 months and roll the short monthly.
- Roll mechanics: either sell the next month on the Monday after expiry, or buy the expiring short at 0.05–0.10 and sell the next month as a spread.
- Vol-history hygiene: exclude one-off spikes (e.g., a 55 vol print in a 20–30 range) after checking the news of the time.
- Due-diligence template (MMM Aug/Oct 85/90 double calendar, 10 lots, debit 3.20 = max loss $3,200; Θ +$19/day, Γ −0.468, vega +$147/pt): stock in a range ($85–$97), no news or earnings, front IV only 1 point over the back month, back IV in line with 30-day HV. "Trading is both cerebral and statistical."
- A long calendar with the strike above the market (WMT $48.50, Aug/Sep 50C, debit 0.50, Δ +0.563, Γ −0.323, Θ +0.030): theta peaks and delta goes flat at $50; below ~$47 theta can turn negative; above $50 delta turns negative.
- In the double diagonal, positive vega is incidental; if IV is fairly priced, aim for the smallest vega possible.

## Key Takeaways
1. Value calendars at the front expiry with a model; only the debit (max loss) is known for sure.
2. Long calendar = short gamma, long theta, long vega: short realized vol, long implied vol.
3. Buy back-month IV cheap (lower third of 12-month range) and avoid pending events.
4. Hedge negative-gamma drift with stock; remember time pushes a falling calendar's delta positive.
5. Roll a long-dated back month to finance it, but respect the monthly negative-gamma risk.
6. Term-structure trades hinge on leg-by-leg vega. Back-month vega dominates, and back IV often follows front IV for dealer-hedging reasons.
7. Choose OTM over ITM calendars, and diagonals over calendars when you want more delta.
8. The double diagonal is a rollable, higher-theta iron condor with positive vega.

## Connects To
- **ch03**: term structure of volatility and IV behavior across months.
- **ch09**: verticals; a diagonal is a vertical plus a calendar.
- **ch10**: iron condors, which the double diagonal generalizes.
- **ch12**: delta-neutral trading of IV, including calendars as term-structure trades.
- **ch13**: gamma scalping of positive-gamma (short) calendars and delta hedging.
- **ch15**: strangles and the strangle swap.
- **`hull-derivatives` ch12**: calendar and diagonal spreads, payoff profiles.
- **`hull-derivatives` ch20**: volatility term structure and surfaces.
- **`cfa-derivatives` ch05**: L3 calendar spreads and volatility-based strategies.
