# Chapter 3: Settings, Tenkan-sen and Kijun-sen
> **Source**: Patrick Riguet, *Ichimoku Kinko Hyo — La formation totale* (French), Part 2 "Les réglages", "Vue d'ensemble", "Tenkan-sen", "Kijun-sen" | author's charts: FXCM Trading Station 2

## Core Idea
Ichimoku Kinko Hyo ("equilibrium of the market at a glance") is a price-action indicator built from five lines, each a midpoint of a high-low range over a fixed window. Keep the original 9-26-52 settings. Tenkan-sen (9) and Kijun-sen (26) are equilibrium lines: they stay close to price, go flat when no new extreme is made, and then act as support/resistance, but only in a trending market.

## Frameworks Introduced
- **Midpoint computation of the five lines** (exact)
  - When to use: to verify any platform output or build the indicator in code.
  - How: for bar t, `Tenkan-sen = (highest high + lowest low) ÷ 2` over the last 9 bars; `Kijun-sen` same over 26 bars; `Senkou span A (SSA) = (Tenkan + Kijun) ÷ 2`, plotted 26 bars ahead; `Senkou span B (SSB) = (highest high + lowest low of the last 52 bars) ÷ 2`, plotted 26 bars ahead; `Chikou span = close of bar t`, plotted 26 bars back. The Kumo (cloud) is the band between SSA and SSB.
  - Why it works / failure mode: each line is a mean-reversion anchor at a different horizon; failure: on flat markets the lines bunch together and lose S/R power.
- **Flats ("plats Tenkan / Kijun")**
  - When to use: to draw support/resistance levels.
  - How: a line is flat when the window has made no new high or low, so the midpoint does not move. Mark each flat; extend it to the right as a horizontal level ("en extension"). Longer flat = stronger level. A Kijun flat is stronger than a Tenkan flat.
  - Why it works: a flat marks a zone where price could not make new extremes, i.e. the market memory of a balance point. Failure mode: flats work as S/R only in trends, never inside a range.
- **Flat versus sloped line**
  - When to use: to read momentum.
  - How: a sloped Tenkan (or Kijun) shows trend strength over 9 (or 26) periods; a flat one shows no trend over that window. Only the flat portion is a level. Price crossing a sloped Kijun is not a Kijun break (see Worked Example).
- **Tenkan overbought/oversold reading**
  - When to use: before entering a breakout or accelerating move.
  - How: Tenkan hugs price. When price is far from Tenkan (Tenkan can no longer follow), the market is overbought/oversold and the stretch cannot last. Do not buy or sell the acceleration; wait for price to return to Tenkan or Tenkan to catch up (via a pullback or a pause).
- **Kijun elastic band (effet élastique)**
  - When to use: to time pullback entries in trends and to accept missing a move.
  - How: when Kijun is flat it equals the 50% retracement of the 26-bar range; price far beyond a flat Kijun will tend to return to it. In a trend (only), the return to the flat Kijun is often a good entry. If you missed a strong move, wait for price to come back.

## Key Concepts
- **Ichimoku Kinko Hyo**: "see the market's equilibrium at a glance"; credited to Japanese journalist Goichi Hosoda (the book spells "Goishi Hosada"), first published early 1960s.
- **Tenkan-sen (転換線, conversion line)**: 9-period midpoint; short-term equilibrium.
- **Kijun-sen (基準線, base line)**: 26-period midpoint; medium-term equilibrium.
- **Senkou span A / B (先行スパン)**: leading spans forming the cloud; plotted 26 bars ahead.
- **Kumo (雲, cloud)**: area between SSA and SSB (ch04).
- **Chikou span (遅行スパン, lagging span)**: close plotted 26 bars back (ch05).
- **Plat (flat)**: horizontal stretch of a line, a support/resistance level; "plat en extension" = its horizontal projection to the right.
- **Settings 9-26-52**: 9 ≈ one and a half trading weeks, 26 ≈ one month (six-day week, Sundays removed), 52 ≈ two months, from the historical Japanese calendar.
- **Overbought / oversold (surachat / survente)**: price too far from Tenkan; unsustainable.
- **Elastic effect**: magnet effect of a flat Kijun on distant price.
- **Fibonacci 50% link**: a flat Kijun equals the midpoint of the 26-bar high-low, hence the 50% retracement of that range (true by construction, stated by the author).
- **Timeframe (UT, unité de temps; TF)**: chart period; lines are identical in logic on every TF, from 1-minute to monthly.

## Formulas & Reference Tables
- `Tenkan_t = (max(H_{t−8..t}) + min(L_{t−8..t})) ÷ 2`
- `Kijun_t = (max(H_{t−25..t}) + min(L_{t−25..t})) ÷ 2`
- `SSA (plotted at t+26) = (Tenkan_t + Kijun_t) ÷ 2`
- `SSB (plotted at t+26) = (max(H_{t−51..t}) + min(L_{t−51..t})) ÷ 2`
- `Chikou (plotted at t−26) = Close_t`
- The cloud under bar t therefore uses data computed at bar t−26.

| Line | Window | Role | Flat means |
|---|---|---|---|
| Tenkan-sen | 9 | short equilibrium, overbought/oversold gauge | no 9-bar trend; weak S/R |
| Kijun-sen | 26 | medium equilibrium, 50% level, magnet | no 26-bar trend; stronger S/R |
| SSA | (T+K)/2, +26 | cloud edge | S/R in trends |
| SSB | 52, +26 | cloud edge, strongest flats | strong S/R in trends |
| Chikou | close, −26 | filter (ch05) | not applicable |

## Mental Models
- **Keep the default settings because everyone else does**: the levels work because the crowd watches them; changing to 7-22-44 makes you the only one acting on your levels (author's view; empirical evidence not given).
- **Tenkan is the dog on a leash, Kijun the owner**: Tenkan sticks to price; extended stretches mean a snap back.
- **Flats are scars**: each flat records where the market could not extend; old flats become future S/R for both price and Chikou.
- **A level is only as good as the regime**: confirm trend via the cloud (ch04) before trusting any flat.

## Worked Example
**Hand check (author's figures)**: CAC 40, 5-minute, last 9 bars: high 5088, low 5072 → Tenkan = (5088+5072)/2 = 5080. USDCAD H4, last 26 bars: high 1.3053, low 1.2917 → Kijun = (1.3053+1.2917)/2 = 1.2985.

**Python-verified computation** on a seeded synthetic series of 100 bars (random.seed(7), drift +0.25 for 60 bars then −0.15, start 100.0):
```python
import random
random.seed(7); p=100.0; H=[];L=[];C=[]
for i in range(100):
    o=p; c=o+(0.25 if i<60 else -0.15)+random.uniform(-0.8,0.8)
    H.append(max(o,c)+random.uniform(0.1,0.6)); L.append(min(o,c)-random.uniform(0.1,0.6)); C.append(c); p=c
mid=lambda n,t:(max(H[t-n+1:t+1])+min(L[t-n+1:t+1]))/2
t=99
tenkan,kijun=mid(9,t),mid(26,t)
ssa_future,ssb_future=(tenkan+kijun)/2,mid(52,t)       # plotted at bar t+26
ssa_now,ssb_now=(mid(9,t-26)+mid(26,t-26))/2,mid(52,t-26)  # cloud sitting under bar t
chikou_value=C[t]                                      # drawn at bar t-26
```
Results: last-9-bar high 115.11 / low 112.37 → Tenkan = 113.74; last-26 high 115.50 / low 112.37 → Kijun = 113.94 (113.937); last-52 high 115.50 / low 106.37 → SSB plotted ahead = 110.93; SSA plotted ahead = (113.74+113.937)/2 = 113.84; the cloud currently under bar 99 (computed at bar 73) is SSA 111.26, SSB 108.44; Chikou = 113.04, drawn at bar 73 where price closed 113.09 (high 113.27, low 112.24), so Chikou sits inside that candle. Reading: price is above the cloud, Tenkan is slightly below Kijun (113.74 < 113.94, short-term weakness after the turn).

**Sloped versus flat Kijun** (author's case): in an uptrend price crosses a sloped Kijun yet the trend holds; the later flat Kijun, extended to the right, still supports price. The sloped crossing is a momentum signal, not a break; only the flat level counts.

## Anti-patterns
- **Changing 9-26-52 to 7-22-44** (or other "adapted" values): you lose the crowd's shared levels.
- **Trading a sloped line as if it were a level**: only flats act as S/R.
- **Using flats as S/R inside a range**: they are crossed easily (ch07).
- **Buying/selling accelerations away from Tenkan**: overbought/oversold traps.
- **Assuming "Kijun always holds in a trend"**: the author says many books omit that Kijun is often overrun; check past reactions (two prior contacts, ch08) and cloud integrity.
- **Reading Chikou or cloud as if unshifted**: the cloud under price was computed 26 bars ago.

## Practitioner Notes
- Author's flat-strength ranking: longer flat > shorter; Kijun flat > Tenkan flat; alignments of several flats at the same price (Tenkan + Kijun + SSA + SSB) are stronger still (ch04, ch06).
- Colours used in the book (free choice): Tenkan red, Kijun blue, Chikou black, SSB light blue, SSA orange.
- Practise on all timeframes; the lines behave the same on 1-minute and monthly charts.
- How far to zoom out for flats? As long as flats are clearly visible; when details get too small, switch to the next higher TF (ch06).
- Tenkan flats on higher TFs are obstacles: if a signal faces a flat Tenkan or old Tenkan flat on the higher TF, wait for price to clear it before entering.

## Key Takeaways
1. Use 9-26-52; midpoint of highest high and lowest low for Tenkan, Kijun, SSB.
2. SSA = (Tenkan + Kijun)/2; both spans plotted 26 bars ahead; Chikou = close, 26 bars back.
3. Only flat portions of lines are support/resistance; sloped lines measure momentum.
4. Flats work only when the market trends; they fail in ranges.
5. Distance from Tenkan signals overbought/oversold; wait rather than chase.
6. A flat Kijun is the 50% retracement and pulls price back (elastic effect).
7. Extend every old flat to the right; it becomes a future level.

## Connects To
- **ch04**: SSA/SSB form the cloud, where flats are strongest.
- **ch05**: Chikou uses the same flats as obstacles.
- **ch06**: higher-TF flats give validation and targets.
- **ch08**: pullbacks on flat Kijun as trade setups.
- **`cfa-portfolio-management` ch09**: generic technical analysis (moving averages, support/resistance, oscillators).
