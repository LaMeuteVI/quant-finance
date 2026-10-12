# Chapter 12: Interest Rates and Investment Grade Corporate Bonds
> **Source**: CFA Society Italy × Advisor Private, "Unconstrained Fixed Income" guide (Sept–Oct 2019), Chapter 1 (Tassi di interesse e titoli corporate investment grade) | Francesco Spadaccia, CFA (introduction by Emanuele Gerletti, CFA)

## Core Idea
After 2009 the return of a corporate bond portfolio shifted from rate risk to credit spread risk: the spread of euro IG corporates went from about 10-20% of the index yield before 2008 to more than 100% (180% by 2019, with negative risk-free rates). Rates still matter, but spread moves can more than offset them, in both directions. Understand the curve (level, shape, slope), the two components of rates (expected policy path and term premium), the curve trades (steepener, flattener, duration-neutral), and the credit return decomposition before allocating to IG credit. The introduction frames the whole guide: investors, forced by yields near or below zero ("Japanification"), moved into HY, bank subordinated bonds, hybrids, loans, private debt and securitizations, taking risks they must now understand.

## Frameworks Introduced
- **Rates = expectations + term premium**: yield on a long maturity = expected average short rate (set by central banks) + term premium (compensation for holding longer maturities). Forecasting the central bank is hard (needs the reaction function and the macro inputs), and term premium moves can dominate: in 2017 the market priced two Fed hikes (about 45 bp) and the Fed delivered three (75 bp), yet the 10-year Treasury yield ended slightly lower because the term premium fell. Historical stat quoted: moves in the 12-month T-bill and shorter explained 93% of the variation in 10-year Treasury yields.
- **Curve reading: level, shape, slope**
  - Level: set by policy (QE shifted curves down after 2008).
  - Shape: positive (normal), inverted (recession signal: early 2000 inversion preceded the US recession about a year later), flat (transition; 1990 flat curve then recession).
  - Slope: driven by inflation outlook, growth, central bank, perceived risk.
- **Curve trades (duration-neutral, using government bond futures)**
  | Trade | Position | Pays off when | Example |
  |---|---|---|---|
  | Steepener | Long short-dated, short long-dated, notionals set so net duration is zero | Spread between long and short yields widens (cuts, stronger growth/inflation expectations, less foreign demand for long bonds) | 2y 1.50% and 20y 3.50% (spread 200 bp) move to 1.55% and 3.65% (spread 210 bp) |
  | Flattener | Short 10y, long 30y (or short-end vs long-end) with futures sized to zero duration | Spread narrows; e.g. after the end of QE the maturities the central bank had bought rose more than longer ones | US curve flattening May 2016 to Nov 2018 |
  - Neutralize duration difference, otherwise you are making a directional rate bet.
- **Credit risk components**: default risk (immediate loss given default, reduced by collateral and recovery rate) and credit spread risk (downgrade). Marked-to-market positions book downgrades as an immediate loss; accrual positions realize only on default.
- **Credit return decomposition**: (1) spread level (carry), (2) capital gain/loss from spread changes over the cycle, (3) credit events (upgrades, downgrades, defaults).
- **IG vs speculative grade**: IG when characteristics make non-speculative purchase suitable; rating agencies (S&P, Moody's, Fitch) give synthetic credit judgments, monitor continuously, place issuers on watch (with expected review), and the rating change moves tradability and reputation. Multiple agencies increase reliability.
- **Tandem rate-spread rule**: total return of IG credit = −(rate duration × Δrates) − (spread duration × Δspread) + carry. Rate rises can be more than compensated by spread tightening (risk-on, Dec 2012-Dec 2013: Bund yields rose and OAS fell, index TR positive); stress can make TR negative despite lower Bund yields (Sept-Dec 2018).
- **Italy analogy**: after the sovereign debt crisis, Italian government bonds behaved like a corporate IG index: spread (to Bund) became the main driver and its share of the 10-year yield became large. May 2018 (political risk) showed spread widening overwhelming falling risk-free rates; hence "core" (Germany, Netherlands, France: rate-driven) vs "spread" (Italy and peripherals: credit-driven) portfolio components.

## Key Concepts
- **Term premium** — extra yield for bearing duration; can change independently of policy expectations.
- **Yield curve (term structure)** — yields across maturities for one issuer category.
- **Steepener / flattener** — relative value trades on the long-short spread.
- **Credit spread (OAS)** — compensation for lower liquidity and credit quality versus governments.
- **Recovery rate** — share of face recovered after default.
- **Rating watch / outlook** — formal signal of an imminent rating review.
- **Japanification** — persistent low or negative yields and growth.
- **Large-cap IG index (ICE BofAML Global Large Cap Corporate)** — main EUR/USD IG issuers; nominal grew from about USD 4 trillion (2009) to over 9 trillion (2019).
- **Spread/yield ratio** — OAS divided by index yield; above 100% means risk-free yield is negative.
- **Core vs periphery** — sovereign groups behaving as rate vs spread products.

## Formulas & Reference Tables
- `Credit return ≈ Spread level + Δ price from spread changes + event losses/gains`.
- `Spread/Yield = OAS / YTM`; 2019 euro IG index: OAS 115 bp, YTM 64 bp, ratio `115/64 = 180%`.
- Approximate total return: `TR ≈ Yield × t − D_rate × ΔY_risk-free − D_spread × ΔOAS`.
- Rating scale: IG = Aaa/AAA to Baa3/BBB-; speculative (high yield) from Ba1/BB+ down. **⚠ Correction**: the guide's table omits the Baa2/BBB row and prints B2 twice with Fitch listed as "B-" and then "B"; the correct line is B1/B+/B+, B2/B/B, B3/B-/B-.
- Euro IG spread levels: 300-350 bp in the stress peaks of the last decade; averages well above pre-2008.

## Mental Models
- Use "rates = expectations + term premium" before concluding that a central bank's moves will translate into yields.
- Use a steepener when you expect easing or fading foreign demand for long-dated bonds; a flattener when the central bank exits purchases of the segment.
- Use spread/yield ratio to judge whether the portfolio is a rates or a credit product.
- Use IG credit as carry plus spread duration risk: the hedge for rate risk is duration, not spread duration.
- Use mark-to-market vs accrual awareness when reading a downgrade's impact.

## Worked Example
Total return decomposition of a euro IG index over a year.
Inputs (writer's illustration, consistent with the guide's levels): yield 0.64%, OAS 115 bp, rate duration 6.0, spread duration 5.5.
1. Scenario risk-on: Bund yields +30 bp, OAS −40 bp: rate effect `−6.0 × 0.30% = −1.80%`; spread effect `−5.5 × (−0.40%) = +2.20%`; carry `+0.64%` → TR `= +1.04%`.
2. Scenario stress: Bund yields −30 bp, OAS +60 bp: `+1.80% − 3.30% + 0.64% = −0.86%`.
Interpretation: in both cases the sign of total return follows the spread leg, matching the guide's 2013 and late-2018 episodes. Steepener numbers from the guide: `(3.65 − 1.55)% = 2.10% = 210 bp`, up 10 bp.

## Anti-patterns
- Shorting duration on a Fed-hike view without checking the term premium.
- Running a "flattener" or "steepener" without duration-neutral sizing.
- Treating IG credit as a rate product after 2009.
- Reading an index yield of 64 bp as mainly carry from rates.
- Ignoring that mark-to-market losses on downgrade are immediate.
- Assuming a flat curve is a stable regime.

## Practitioner Notes
- The guide cites Fed behavior in 2017 as the classic example that anticipating policy correctly is not enough.
- IG credit nominal growth coincided with falling ratings quality within IG (BBB share), a driver of risk not discussed numerically here.
- Euro IG spreads peaked around 300-350 bp in stress; the 115 bp level in 2019 was near the low end of the post-crisis range.

## Key Takeaways
1. Policy path plus term premium determine yields; term premium can swamp policy surprises.
2. Curve level follows policy; slope signals growth and inflation.
3. Steepeners and flatteners are duration-neutral curve views implemented with futures.
4. Credit return = spread level + spread changes + credit events.
5. Since 2009, spread is the dominant component of IG yield (over 100% by 2019).
6. Rate and spread moves offset each other; total return can be positive in rate selloffs and negative in rate rallies.
7. Italian BTPs after 2011 are a spread product analogous to corporates.

## Connects To
- **ch13**: high yield market, where credit risk dominates fully.
- **ch16**: local currency EM, where rates and FX drive returns.
- **ch05** (`cfasi-fixed-income-guides`): yield curve theory and spread definitions.
- **ch02 / ch06**: credit spread and duration measures.
- **`cfa-fixed-income` ch05-ch07**: duration, credit analysis and spreads.
- **`ilmanen-yield-curve`**: term premium and curve trades empirics.
