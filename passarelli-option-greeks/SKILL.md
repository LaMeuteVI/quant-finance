---
name: passarelli-option-greeks
description: "Dan Passarelli, Trading Option Greeks (2nd ed., Bloomberg Press/Wiley 2012), 17 chapters on trading options through delta, gamma, theta, vega, rho and dividends: volatility selling, put-call parity, spreads, delta-neutral trading, vol charts, straddles, ratio spreads. Use when choosing an option strategy from a view, managing a short option, reading implied vs realized volatility, gamma scalping, or adjusting a spread. Topics: delta, gamma, theta, vega, rho, implied volatility, skew, iron condor, butterfly, calendar spread, straddle, strangle, backspread, covered call, put-call parity, conversion, box, dividends, early exercise, rush and crush."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Trading Option Greeks (Passarelli)
**Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012) | **Domain**: Finance de marché | **Chapters**: 17 | **Generated**: 2026-09-29

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch07`
- **Browse** — "what chapters do you have?"

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

### The greek frame
- **Theo is a mirror, not an oracle** (ch02): calibrate IV so the theo sits in the bid-ask, then trust the greeks. A theo outside the market means a bad input (rate, dividend, days), not a free trade.
- **Daily P&L attribution** (ch02, ch12): `ΔV ≈ Δ·ΔS + ½Γ·ΔS² + θ·days + vega·ΔIV + ρ·Δr`. Reprice moves with the average delta, not the starting delta.
- **Greek signs**: long option = +Γ, +vega, −θ; short option the reverse. Every option trade is a choice between gamma/vega and theta (ch02, ch04). Theta is the rent on gamma.
- **Strike choice is greek choice** (ch04): ITM is stock-like delta; ATM maximizes Γ, θ, vega; OTM is a magnitude bet with low odds. Rank greeks by thesis (long directional: delta, theta, vega, gamma, rho) and budget average daily theta over the holding period.
- **Short call is not bullish, short put is not bearish** (ch01): they say "not above" and "not below" only.

### Volatility
- **Three vols** (ch03): historical (what happened), implied (what is priced), expected (your forecast). Buying options buys both realized (gamma) and implied (vega) vol.
- **Rule of 16** (ch03, ch10): 1-day σ = IV/16; n-day σ = (IV/16)·√n. Use it as a sanity check on every trade.
- **IV mean reverts in a 6–12 month range, until a regime change** (ch03, ch12). IV usually falls when stocks rise; equity put skew is steeper than call skew.
- **Read RV and IV together** (ch14): nine patterns. Buy vol when IV is below RV and low in its range; sell when IV exceeds RV by 5+ points with no news; 1–3 point gaps persist, 7–10 converge.
- **Rush and crush** (ch12): IV rises into a known event and drops 10–20 points after. Sell delta-neutral just before and exit next morning; or buy days early and exit before the news, needing `ΔIV ≥ |θ|·days/vega`.

### Short premium and parity
- **Pain-point stop** (ch05): `ΔS = ΔV / (|Δ| + Γ/2)`, priced at the offer. Short puts get the double whammy (delta and vega hurt together).
- **Would I Do It Now?** (ch05, ch17): if flat, would I open this at today's prices? If not, close. Roll when the short is worth a nickel to a dime.
- **Put-call parity** (ch06): `Call + K − Interest + Dividend = Put + Stock`. A call is a put plus stock; only delta differs. Conversion (rho negative), reversal (rho positive), box (riskless loan worth width minus interest), jelly roll.
- **Rho ≈ strike × time** (ch07): ignore on short-dated, 5–8% of value on two-year ATM. Back out implied rates when the call/put gap grows with maturity.
- **Dividends** (ch08): the ex-date is what counts. Exercise a long ITM call the day before if `Dividend − Interest > Put bid`. A wrong date or amount shows up as false IV.

### Spreads
- **Verticals** (ch09): the ATM strike dominates the greeks: long vol near the long strike, pure delta in between, short vol near the short strike. The short strike is the target. Slow move: vertical; fast move: outright.
- **Wing spreads** (ch10): two verticals; long condor = short iron condor. Butterfly for precision, condor for tolerance. Short strikes at ±1σ only when you expect realized below implied (payout:risk is usually below 1:3). Tested condor: buy back the cheap safe side, then close or lift the tested short.
- **Calendars and diagonals** (ch11): long calendar = −Γ, +θ, +vega: short realized, long implied. Buy back-month IV in the lower third of its range with no event. Back vega is about 2× front. Prefer OTM. Double diagonal = rollable iron condor with positive vega.
- **Ratio spreads** (ch16): two-faced greeks that flip with the stock price. Judge by greeks at several prices, not the credit. Underhedge a backspread; buy back part of a ratio vertical's shorts if vol rises.

### Delta-neutral trading
- **Delta neutral is a construction, not a strategy** (ch12): once direction is stripped, you hold gamma/theta (realized) and vega (implied).
- **Gamma scalping** (ch13): long gamma sells strength and buys weakness; revenue is scalps, expense is theta, weekends are pure cost. Break-even daily move `≈ √(2Θ$/(Γ·100))`, close to the IV-implied daily σ. Short gamma hedges partially. Go home flat.
- **Straddles and strangles** (ch15): long needs movement and cheap IV; short needs IV above RV and a hedge plan. Add wings to cap the tail; never sell dime strangles.
- **Greeks-driven selection** (ch17): derive the greek profile from the view, holding period and vol regime, then choose the structure. Know net portfolio greeks and up/down risk including 3σ gaps. Start with 1–2 lots.

---

## Chapter Index
| # | Title | Part | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-the-basics.md) | The Basics | I · Foundations | four positions, assignment, stock vs call |
| [ch02](chapters/ch02-greek-philosophy.md) | Greek Philosophy | I · Foundations | five greeks, average delta, P&L attribution |
| [ch03](chapters/ch03-understanding-volatility.md) | Understanding Volatility | I · Foundations | HV/IV, rule of 16, skew, mean reversion |
| [ch04](chapters/ch04-option-specific-risk-and-opportunity.md) | Option-Specific Risk and Opportunity | I · Foundations | strike-greek matrix, gamma/theta, vol buyers vs sellers |
| [ch05](chapters/ch05-volatility-selling-strategies.md) | Volatility-Selling Strategies | I · Foundations | pain-point stop, Would I Do It Now?, covered call |
| [ch06](chapters/ch06-put-call-parity-and-synthetics.md) | Put-Call Parity and Synthetics | I · Foundations | parity, conversion, box, jelly roll |
| [ch07](chapters/ch07-rho.md) | Rho | I · Foundations | rho scaling, LEAPS, implied rates |
| [ch08](chapters/ch08-dividends-and-option-pricing.md) | Dividends and Option Pricing | I · Foundations | ex-date exercise rule, dividend inputs |
| [ch09](chapters/ch09-vertical-spreads.md) | Vertical Spreads | II · Spreads | four verticals, greek migration, box |
| [ch10](chapters/ch10-wing-spreads.md) | Wing Spreads | II · Spreads | condor, butterfly, 1σ strikes, adjustments |
| [ch11](chapters/ch11-calendar-and-diagonal-spreads.md) | Calendar and Diagonal Spreads | II · Spreads | term structure, double diagonal, free call |
| [ch12](chapters/ch12-delta-neutral-trading-implied-volatility.md) | Delta-Neutral: Implied Volatility | III · Volatility | rush and crush, P&L attribution |
| [ch13](chapters/ch13-delta-neutral-trading-realized-volatility.md) | Delta-Neutral: Realized Volatility | III · Volatility | gamma scalping, negative scalping |
| [ch14](chapters/ch14-studying-volatility-charts.md) | Studying Volatility Charts | III · Volatility | nine RV/IV patterns, mesa |
| [ch15](chapters/ch15-straddles-and-strangles.md) | Straddles and Strangles | IV · Advanced | long/short straddle, legging out, synthetics |
| [ch16](chapters/ch16-ratio-and-complex-spreads.md) | Ratio and Complex Spreads | IV · Advanced | backspread, ratio vertical, risk reversal |
| [ch17](chapters/ch17-putting-the-greeks-into-action.md) | Putting the Greeks into Action | IV · Advanced | greeks-driven selection, HAPI, adjusting |

## Topic Index
- **Assignment / American exercise** → ch01, ch06, ch08
- **Average delta** → ch02, ch05, ch13
- **Backspread** → ch16
- **Box** → ch06, ch09
- **Butterfly** → ch10
- **Calendar spread** → ch11
- **Cash-secured put** → ch01, ch05
- **Conversion / reversal** → ch06, ch07, ch08
- **Covered call** → ch01, ch05
- **Covered put** → ch05, ch06
- **Delta** → ch02, ch04
- **Delta hedging / delta neutral** → ch12, ch13
- **Diagonal / double diagonal** → ch11
- **Dividends** → ch08
- **Early exercise** → ch06, ch08
- **Earnings rush and crush** → ch03, ch12, ch14
- **Gamma** → ch02, ch04
- **Gamma scalping** → ch13, ch15
- **HAPI / discipline** → ch17
- **Historical volatility** → ch03, ch14
- **Implied volatility** → ch02, ch03, ch14
- **Iron condor** → ch10, ch17
- **Jelly roll** → ch06
- **LEAPS** → ch01, ch07
- **Margin (Reg T, portfolio)** → ch09, ch12, ch15
- **Mean reversion of IV** → ch03, ch12
- **Moneyness** → ch02, ch04
- **Naked call / put** → ch01, ch05
- **Open interest, volume** → ch01
- **P&L attribution** → ch02, ch12
- **Pin risk** → ch06, ch15
- **Put-call parity** → ch02, ch06
- **Ratio spread** → ch16
- **Realized volatility** → ch03, ch13, ch14
- **Rho** → ch02, ch07
- **Risk reversal** → ch16
- **Rule of 16** → ch03, ch10
- **Skew** → ch03, ch11, ch16
- **Straddle / strangle** → ch15
- **Strategy selection** → ch04, ch17
- **Synthetics** → ch06, ch15
- **Term structure** → ch03, ch11
- **Theta** → ch02, ch04
- **Vega** → ch02, ch03
- **Vertical spread** → ch09
- **Vol chart** → ch03, ch14
- **Volatility selling** → ch04, ch05
- **Would I Do It Now?** → ch05, ch17

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules and thresholds for the desk

---

## Related Skills
- `hull-derivatives` — BSM derivation, greek formulas (ch15, ch19), smiles (ch20), strategy payoffs (ch12)
- `cfa-derivatives` — options strategies in a portfolio context (ch05), contingent-claim valuation (ch04)
- `tuckman-fixed-income` — fixed-income options if you need rate-linked option pricing
- `cfa-fixed-income` — embedded options in bonds

## Scope & Limits
Covers US listed equity, ETF and index options as traded in 2012: conventions, margin rules and product examples (HOLDRs, AM settlement, Reg T, 2011 vol regimes) predate later changes; expiry moved to the third Friday in 2015 and weekly products have expanded. Prices in examples are the author's and were checked against Black-Scholes where flagged. Charts and exhibits were reconstructed from extracted text, so some signs of position greeks (ch09, ch10, ch16, ch17) are inferred. Not covered: exotic options, binomial pricing, interest-rate or commodity options. Several ⚠ corrections to the book's arithmetic are flagged inside the chapters (ch03, ch05, ch11, ch16).
