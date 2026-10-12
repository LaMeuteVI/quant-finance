# Chapter 8: Trend Trading (Le trading d'une tendance)
> **Source**: Patrick Riguet, *Ichimoku Kinko Hyo — La formation totale* (French), Part 3 "Le trading d'une tendance sans obligation de naviguer sur les UT supérieures" (charts 98–114, reconstructed as rule lists) | retail FX/CFD trader-educator

## Core Idea
When the cloud (Kumo) is clearly oriented, you trade only in its direction, using one of two entries: a pullback to a flat Kijun-sen that has already held, or a close beyond the previous swing high/low. Stop and target come from structure (flat Kijun and trend line for the stop, upper channel bound for the target) and the trade is taken only if risk/reward is at least about 2:1 and Chikou is free. In rare, perfectly identified trends this can be done without climbing time frames, but the author still recommends checking that the trend is not about to hit the bound of a higher-TF range.

## Frameworks Introduced
- **Pullback on a flat Kijun (throwback / pullback)**
  - When to use: oriented cloud, price in trend, a flat Kijun-sen that has acted as support (long) or resistance (short).
  - How: (1) confirm cloud orientation and no twist; (2) wait for at least two prior contacts that show the flat Kijun holding; (3) check that Chikou is free; (4) enter at the candle close at the next pullback to the flat; (5) place the stop where the signal is invalidated: below the flat Kijun and the trend line together (long); (6) put the target on the upper channel bound immediately above price (the author notes Chikou often "surfs" this oblique); (7) enter only if R:R ≥ ~2 (slightly under is tolerable, not a dogma).
  - Why it works / failure mode: the flat Kijun is the 50% level of the last 26 bars (ch03). Failure: a late flat after several wins can fail; the author shows a loss after consecutive gains. Many books omit that Kijun is not always respected.
- **Sloped Kijun is not a break**
  - How: price crossing a sloped Kijun is a momentum signal, not a break; only the flat portion (extended to the right) counts as support. The trade stays valid while the flat holds.
- **Breakout of a new high (or low) in trend**
  - When to use: oriented cloud, horizontal resistance in the trend.
  - How: (1) a candle closes beyond the resistance; (2) stop below the latest lows and below the body of the last reversal candle (or under Tenkan flat and under the oblique); (3) target the upper channel bound; (4) check R:R ≥ 2 and Chikou free; (5) enter at the close, never in anticipation on a lower TF here (anticipated breakouts are exposed to false wicks); (6) if R:R < 2 even though the signal is perfect (e.g. a marubozu breaking resistance), abstain.
- **Exit variant: ride until the opposite Kijun break**
  - How: instead of the channel target, hold until price breaks Kijun in the opposite direction (the author's example: entry 1.3145, exit near 1.34 on the opposite Kijun break).
- **Pyramiding (pyramidage)**
  - How: open a new position at each pullback on the next flat Kijun; raise the previous position's stop to the new position's stop; exit all on the opposite Kijun break. Total risk must respect the cap of ch02.
  - Failure mode: not possible when the Kijun is repeatedly overrun (see below).
- **Weakened trend case (DAX M5 downtrend)**: if Kijun is slightly exceeded several times but the cloud stays oriented with no twist, new entries remain possible when Kijun breaks again in the trend direction; but no pyramiding and no riding to the opposite Kijun break.
- **Higher-TF caution**: check that the trend is not a sub-trend inside a higher-TF range; entering a trend just below/above a range bound is wrong because the bound is a probable end of the trend (ch06, ch07).

## Key Concepts
- **Orientation du nuage**: slope of the cloud; defines allowed trade direction.
- **Throwback / pullback**: return to broken level / to the line.
- **Repli sur plat Kijun**: pullback to a flat Kijun.
- **Channel (canal)**: upper bound drawn parallel to the trend line; target.
- **Marubozu**: long body candle with almost no wicks.
- **Hammer-doji / reversal candle**: its body is a stop reference.
- **Stop at invalidation**: a level whose break invalidates the signal, no more risk than that.
- **Break even (BE)**: stop at entry.
- **Pyramiding**: adding positions with raised stops.
- **Kijun overrun**: price repeatedly pierces Kijun, reducing its reliability.

## Formulas & Reference Tables
- `R:R = (target − entry) ÷ (entry − stop)` for a long.
- Position size: `size = (capital × risk%) ÷ stop distance` (ch02).

| Item | Rule |
|---|---|
| Direction | only with cloud orientation |
| Entry trigger | candle close at flat Kijun pullback or beyond the swing extreme |
| Stop | under flat Kijun + trend line (pullback) or under last lows/reversal body (breakout) |
| Target | upper channel bound above price; or opposite Kijun break |
| Filter | Chikou free; R:R ≥ ~2 |
| Skip when | cloud twist/flat, Chikou blocked, ratio < 2, near a higher-TF range bound |

## Mental Models
- **Trend gives direction, flat gives price, trend line gives target**.
- **Two touches before trust**: a flat becomes tradable only after it has held twice.
- **A perfect signal with a bad ratio is not a signal**.
- **Pyramid with the stop ratchet**: each add moves prior stops up so total risk does not grow.

## Worked Example
**EURAUD H4 long (author's levels, python-checked)**: entry 1.3145 at the candle close on a Kijun flat pullback; stop 1.3080 below flat Kijun and trend line = 65 pips; target 1.3285 on the upper channel bound = 140 pips. R:R = 140 ÷ 65 = 2.15, validated. Sizing at 1% of 10,000: 100 ÷ 65 = 1.54 per pip.
Alternative exit on the opposite Kijun break at about 1.34: 255 pips, i.e. 3.9R on the original stop.
**Breakout rejection (SP500 weekly)**: a marubozu breaks resistance, stop under Tenkan flat and the hammer body, but the trend-line target is too close: R:R < 2, so no trade. A second breakout with the stop under Tenkan flat and just under the oblique, target at the channel top, R:R clearly > 2: take it (target hit only just).
**Repeating the setup**: at each later pullback on the flat Kijun the same logic applies, stop either under the trend line or under the previous flat; one of the entries ends in a loss after several wins.

## Anti-patterns
- **Buying a sloped Kijun crossing as a break**.
- **Entering on the first pullback without two prior holds**.
- **Anticipating a breakout on a lower TF** (false wicks).
- **Taking trades with R:R below ~2 because the pattern looks perfect**.
- **Trend following into a higher-TF range bound**.
- **Pyramiding when Kijun is frequently overrun**.
- **Moving the stop away** (ch01).

## Practitioner Notes
- Only enter at the close; the anticipation techniques of ch07 are acceptable for pullback-type entries but the author warns against them for breakouts.
- Tenkan flat stop for breakouts, Kijun flat + oblique stop for pullbacks.
- Perfect trends (oriented cloud, trend line, channel) are the exception allowing no higher-TF check; otherwise ch06 applies first.

## Key Takeaways
1. Trade only with the cloud's direction.
2. Pullback entry on a flat Kijun after two proven holds, at the close.
3. Stop at signal invalidation, target at channel top, R:R ≥ ~2.
4. Breakouts: close beyond swing extreme, stop under last lows/reversal body.
5. Pyramid at each new Kijun pullback with the stop ratchet; exit on the opposite Kijun break.
6. A sloped Kijun cross is momentum, not a break.
7. Verify that no higher-TF range bound sits just ahead.

## Connects To
- **ch02**: R:R, sizing, break even and pyramiding limits.
- **ch03**: flat Kijun, elastic effect.
- **ch04**: cloud orientation, twist.
- **ch05**: Chikou filter.
- **ch06**: higher-TF validation.
- **ch07**: range logic and anticipation.
- **ch09**: plans.
- **`cfa-portfolio-management` ch09**: trend following, moving averages, channels.
