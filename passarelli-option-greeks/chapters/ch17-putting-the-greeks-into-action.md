# Chapter 17: Putting the Greeks into Action
> **Source**: Dan Passarelli, *Trading Option Greeks* (2nd ed., Wiley/Bloomberg 2012), Ch. 17 · Advanced Option Trading

## Core Idea
The greeks are a decision tool at every stage of a trade: choosing the strategy, sizing and monitoring risk, deciding to hold or exit, and adjusting when the market moves. The right option position is the one whose greeks match the forecast, the holding period and the volatility environment, and it must be re-matched whenever the market changes the position's greeks. Discipline (learning path, small size, probability thinking, taking losses) matters as much as the mathematics.

## Frameworks Introduced
- **Three-step learning process**: Study, Paper Trade, Showtime.
  - When to use: anyone building option skills.
  - How: (1) learn the greeks thoroughly; (2) simulate real markets with fake money to see how strategies differ from theory; (3) go live starting with one or two lots per trade until decisions are rational and emotions are controlled.
  - Failure mode: skipping to live size; wealth as the motive.
- **Greeks-driven strategy selection** ("trading is situational"): derive the desired greek profile from forecast (direction, size, timing), holding period (theta importance), and volatility level/catalysts (vega and gamma desire), then pick the structure and strikes/expiry.
  - When to use: before any entry.
  - How: for a bullish view ask (a) how long will I hold (theta), (b) is IV cheap, fair or rich versus RV and its own history, is an IV catalyst approaching (vega), (c) do I want convexity (gamma). Then choose outright vs spread, and strike/expiry.
  - Failure mode: picking a strategy by name ("bullish, so a bull put spread") without checking its vega/theta.
- **Know Thy Risk**: know every trade's greeks, the net-portfolio greeks at all times, and the "up and down risk" (P&L for benchmark moves in both directions, including 3-standard-deviation gaps).
  - Failure mode: relying on at-expiration diagrams alone or on hope.
- **HAPI, the Hope and Pray Index**: a contra-indicator; the more you are hoping and praying, the worse the trade, and the nearer the time to take the loss and move on.
  - When to use: as a self-diagnostic whenever an adverse gap or move makes you rationalize.
  - How: if you notice hope/prayer/bargaining, apply the **Would I Do It Now?** rule (if I had no position, would I open this one at today's prices?); if no, close or adjust.
  - Why it works: entry and exit prices are the only two things you control; thinking in probabilities pre-commits the response to adverse moves.
- **Adjusting by re-matching greeks to outlook**: if after a market move the position's greeks no longer express your (possibly unchanged) outlook, adjust the position so delta, theta, gamma and vega represent the view again.
  - Example: roll the threatened credit-spread leg of an iron condor.

## Key Concepts
- **Situational trading**: the best strategy differs for each combination of forecast, time horizon and volatility regime.
- **Optimal greeks position**: the position whose net greeks best exploit the opportunity with minimal unwanted exposures.
- **Up and down risk**: P&L for moves of benchmark size up and down, used alongside greeks.
- **Net portfolio greeks**: aggregate delta, gamma, theta, vega, rho across all positions.
- **HAPI (Hope and Pray Index)**: contraindicator that rises with hoping rather than managing; higher means worse trade.
- **Would I Do It Now? Rule**: re-decide each open position as if flat (from ch05).
- **Adjusting**: modifying a position (rolling legs, adding hedges) so its greeks reflect the current outlook.
- **Rolling a spread**: closing a spread and opening one at different strikes or expiry, e.g. moving an iron condor's call spread up.
- **Paper trading**: simulated trading of real markets with fake money.
- **Three-standard-deviation move**: rare but real; the 2010 flash crash is the cited example.
- **Probability thinking**: assess likelihood, payout, loss and own risk tolerance before entry.

## Formulas & Reference Tables
No new formulas. Decision matrix from the chapter's cases:

| Situation | Greeks wanted | Structure | Why |
|---|---|---|---|
| Bullish, uptrend, earnings in 1 week, IV cheap vs RV and past IV, short hold (Arlo) | big +delta, +gamma, +vega; theta irrelevant | Long front-month call (3 weeks) | Spreads give up vega and gamma; front month gains most from pre-earnings IV rise |
| Bullish to about $34 from about $31, steady uptrend, no catalysts, IV midpriced, hold weeks (Luke) | delta, near-zero vega, near-zero theta at start | Debit call spread, long call somewhat ITM, short call at 34 | Keeps a delta play without theta/vega noise; positive theta builds near short strike |
| Neutral, short iron condor after stock rises toward short strike | delta back to about 0, theta restored | Roll call spread up (35/36/38/39 to 35/36/39/40) | Gamma gave short delta and theta is fading as stock nears long strike |

Iron condor roll, Halliburton (stock 36.85): sold 10 February 35/36/38/39 condors at 0.45; buy 10 × 38 calls and sell 10 × 39 calls to close the call spread, then buy 10 × 39 calls and sell 10 × 40 calls to open it; net position is the 35/36/39/40 condor.

## Mental Models
- **Greeks are the job description of a position**: if the position's greeks do not match the stated outlook, change the position.
- **Two numbers you control**: entry price and exit price; everything else on screen is outside your control.
- **Good traders are good at losing**: cut losses fast, let winners run, accept the statistical nature of trading.
- **Start small until you are rational**: one or two lots; emotions should not override judgment.
- **Plan for the tail**: anything can happen; size by up and down risk, not by comfort.
- **Look forward, never back**: use the Would I Do It Now? rule to strip sunk cost.

## Worked Example
Choosing the structure (Arlo vs Luke), same bullish view, different greeks:
1. Arlo: uptrend, intraday volatility rising, IV cheap, earnings in one week, exit before earnings. Theta is small for a short hold; vega is an asset; gamma is an asset. Rule out short-vega trades (naked/cash-secured put, put credit spread) and verticals (they spread off vega, gamma, and profits need time). Choose a long call, front month (about three weeks).
2. Luke: same direction, target about 34 from about 31, weeks-long hold, mid-priced IV, no events. Theta and vega both matter; he wants neither. Choose a debit call spread, long strike slightly ITM, short at 34. Versus a long call it has less theta/vega; versus an OTM bull put spread it has better vega and a bigger delta.
Condor adjustment (HAL): 10 lots, stock 36.85, credit 0.45 per condor is 0.45 × 100 × 10 = $450 total credit. If the stock rallies and the trader is still neutral, roll the call credit spread up by one strike pair (net effect: the short call moves from 38 to 39 and long from 39 to 40), restoring delta toward zero and theta away from zero. If bullish, close; if bearish, accept the short delta.

## Anti-patterns
- **Choosing a strategy by directional label** without checking its vega, theta and gamma against the situation.
- **Hoping and praying** (high HAPI): holding a loser without re-deciding.
- **Relying on at-expiration diagrams** as the only risk view.
- **Not knowing net portfolio greeks or up/down risk**; "I couldn't plan for it" is not acceptable.
- **Going live at full size** before paper trading and small-lot experience.
- **Letting positions drift** until the greeks contradict the outlook, instead of adjusting.
- **Trading for quick riches**: the book names it a poor motivation.

## Practitioner Notes
- Questions to ask before every entry: view and horizon? theta tolerance? IV versus RV and its own history? catalyst ahead? want or fear convexity? This produces the greek profile.
- Short-dated options give more gamma and less vega; if IV may rise into an event, the front month gains most.
- An iron condor is neutral by delta near flat, but gamma turns that into an exponentially growing short delta as the stock rallies; theta also decays in value when the stock nears a long strike.
- Keep positions in several classes for detachment and diversification; read the portfolio as one position with moving parts.
- Exits, not entries, separate good from bad traders; trade losers with the same rules as winners.
- Source caveat: HAL condor greeks in the source lost their signs in OCR (delta near flat, gamma and vega negative, theta positive); use qualitative reading.

## Key Takeaways
1. Match the position's greeks to forecast, holding period and volatility regime before entry.
2. For a short hold into cheap IV, a long front-month option beats a spread; for a multi-week delta play at fair IV, a debit spread removes theta/vega noise.
3. Know trade and portfolio greeks and up/down risk at all times, including 3-sigma gaps.
4. Treat HAPI as a warning: hope is a signal to apply the Would I Do It Now? rule and likely exit.
5. Adjust when the greeks stop representing the outlook (e.g., roll the threatened side of the condor).
6. Learn via study, paper trading, then one or two lots.
7. Take losses quickly and trade in terms of probabilities.

## Connects To
- **ch02**: greek philosophy underpinning position profiles.
- **ch05**: Would I Do It Now? rule and short-vol strategies.
- **ch09**: vertical spreads' greek profile (time to profit).
- **ch10**: iron condors and their adjustments.
- **ch12-ch15**: volatility trading, charts and straddles feeding the vega decision.
- **ch16**: complex spread greeks and market-maker management.
- **`hull-derivatives`**: greek-based hedging and risk limits.
