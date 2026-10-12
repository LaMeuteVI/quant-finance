# Chapter 3: Does Duration Extension Enhance Long-Term Expected Returns?
> **Source**: Antti Ilmanen, *Understanding the Yield Curve, Part 3: Does Duration Extension Enhance Long-Term Expected Returns?*, Salomon Brothers U.S. Fixed-Income Research (July 1995). Text from OCR; tables reconstructed and cross-checked.

## Core Idea
Use this chapter to set a **strategic (benchmark) duration**. In the U.S. Treasury market from 1970 to 1994, a period chosen because start and end yields were similar, duration extension paid well at the **front end**. The 1-year bill beat the 1-month bill by about 150bp per year, with almost 200bp from 1-month to 2-year duration. The **average return curve is essentially flat beyond about 2 years' duration**, while volatility keeps rising. Expected returns are therefore **concave** in duration and even in volatility, which contradicts theories that make premia linear in duration or beta. For a short-horizon, volatility-averse investor there is little long-run reason to hold a benchmark duration above about 2 years. Long bonds belong to long-liability holders and to *tactical* bets, for example when the curve is unusually steep beyond 2 years.

## Frameworks Introduced
- **Six theories of the bond risk premium (BRP)**. Each predicts a sign, a shape and a stability, but none predicts the magnitude:
  1. **Pure expectations**: BRP = 0.
  2. **Liquidity (risk) premium**: BRP > 0 and rising with duration, because investors are averse to short-horizon price risk. Subtler form: when horizons are vague, public accountability makes price risk more feared than reinvestment risk, which biases portfolios short.
  3. **Preferred habitat**: BRP can rise or fall with duration. Pension funds and life insurers see long bonds as the safe asset. Long-horizon investors are a *minority*, so the market premium still rises with duration, but less than short-horizon investors would require.
  4. **One-factor models**: BRP ∝ return volatility (partial equilibrium).
  5. **CAPM**: BRP = β × market premium. Bond betas and volatilities are roughly ∝ duration, which implies a BRP linear in duration.
  6. **General equilibrium / "bad times"**: assets that do badly when marginal utility is high earn premia. Bonds hedged the 1930s deflation but lost heavily in the 1973–75 and 1980–82 inflationary recessions, so post-war the BRP should be positive.
  - Plus practitioner (non-risk) sources: illiquidity (bills vs short coupons, off-the-run vs on-the-run, the illiquid 20y vs the 10y/30y), career risk in unpopular assets, and supply/demand. "BRP" covers all of them.
  - ⚠ Linearity in duration follows only if yield volatility is equal across the curve. Short rates are more volatile (mean reversion), so return volatility, and hence the premium, should be **concave** in duration.
- **Two ways to estimate the long-run BRP, and their traps**:
  - **Average term spread**: valid only if expected yield changes average zero. Persistent expectations of rising rates inflate it.
  - **Average realized excess return**: valid only if unexpected returns wash out, i.e. the sample has no yield trend.
    - The 1980s–90s disinflation *overstates* the premium, and many databases start near the 1981 yield peak.
    - The 1950s–70s inflation surprises *understate* it.
  - How: pick a **neutral window** (similar start and end yields), use long samples (300 months), and check subperiods and other markets. No econometric technique fixes period specificity.
- **Arithmetic vs geometric mean**:
  - Geometric (compound) is correct for describing history and approximates the median outcome.
  - Arithmetic is the correct expected value.
  - `GM ≈ AM − σ²/2`, so the gap grows with volatility: 64bp for the 20y at 11% vol.
- **Strategic duration decision rule**:
  - Short-horizon, volatility-averse investor → benchmark duration ≤ about 2 years.
  - Long-duration liabilities or a long horizon → long bonds are the low-risk asset.
  - Tactical extension beyond 2 years only when you can predict rate declines or the curve beyond 2 years is abnormally steep.
- **Near-term vs long-run BRP**: the historical average is the best forecast of the *long-run* premium, and of the near-term premium only if the premium is constant. It is not constant, so use the curve (rolling yield, better than the term spread) and other predictors for tactical forecasts (ch04).

## Key Concepts
- **Bond risk premium (BRP)**: the expected holding-period return of a long bond in excess of the riskless one-period bond, whatever its cause. Synonyms: term premium, interest rate risk premium, liquidity premium, expected excess return. "Required return" is a better word than "expected return", because premia are highest in bad times.
- **Riskless return**: the return of the bill maturing at the horizon (nominally riskless, but it carries inflation risk).
- **Realized vs expected excess return**: realized = expected + unexpected. Monthly returns are dominated by the unexpected part.
- **Neutral sample period**: one whose start and end yield levels are close. 1970–94 had small net changes (short rates down, long rates up) and an inverse-V yield path.
- **Maturity-subsector portfolio**: a monthly rebalanced portfolio with stable characteristics (CRSP bill and bond buckets, Ibbotson 20y).
- **Inverted term structure of yield volatility**: short rates are more volatile (1970–94: 1m 3.04%, 20y 1.31% per year). In 1985–94 it was flatter, at 1.1–1.3% and peaking at intermediate maturities.
- **Sharpe ratio (bonds)**: annualized mean excess return / volatility. It falls monotonically with maturity. The t-stat of the excess return ≈ 5 × Sharpe for 300 months (√25 years).
- **Money-market credit-spread inversion**: private-issuer spreads over bills are *wider* at 1 month than at 6 months. The 1m bill is "overpriced" because of safe-asset demand.
- **Reassessment of bond riskiness**: bond volatility, beta and inflation rose from the mid-1960s to about 1980. The resulting re-pricing, with higher required premia, depressed realized returns in that era.

## Formulas & Reference Tables
- `AM = (h₁ + … + h_N)/N`; `GM = [(1+h₁)(1+h₂)…(1+h_N)]^(1/N) − 1`; `GM ≈ AM − σ²/2`
- Excess return decomposition: `hₙ − s₁ = BRPₙ + unexpected part`
- Bond return volatility ≈ duration × yield volatility, which is concave because yield volatility falls with maturity.

**U.S. Treasury maturity subsectors, 1970–94 (annual; OCR-corrected, GM ≈ AM − σ²/2 checked)**

| Sector | 1m | 3m | 6m | 9m | 1–2y | 2–3y | 3–4y | 4–5y | 5–10y | 20y |
|---|---|---|---|---|---|---|---|---|---|---|
| Arithmetic mean | 6.87 | 7.71 | 7.98 | 8.28 | 8.56 | 8.91 | 9.10 | 9.01 | 9.28 | 9.51 |
| Geometric mean | 6.87 | 7.71 | 7.97 | 8.27 | 8.52 | 8.81 | 8.95 | 8.82 | 8.98 | 8.87 |
| Geom. premium over 1m | 0.00 | 0.84 | 1.11 | 1.40 | 1.65 | 1.94 | 2.09 | 1.95 | 2.12 | 2.00 |
| Volatility | 0.81 | 1.00 | 1.34 | 1.79 | 3.02 | 4.36 | 5.26 | 6.03 | 7.43 | 10.98 |
| Avg duration | 0.08 | 0.24 | 0.48 | 0.71 | 1.3 | 2.4 | 2.9 | 3.7 | 5.1 | 9.8 |
| Sharpe ratio | — | 1.92 | 1.10 | 0.87 | 0.55 | 0.45 | 0.40 | 0.34 | 0.31 | 0.22 |

**Average yields 1970–94**: 1m 6.75, 3m 7.21, 6m 7.56, 12m 7.73, 2y 8.04, 5y 8.44, 10y 8.63, 20y 8.85. The curve is upward-sloping and concave.

**Hit rates, annual horizon, 1970–94** (frequency of beating the previous maturity / the 1m bill):

| | 3m | 6m | 9m | 1–2y | 2–3y | 3–4y | 4–5y | 5–10y | 20y |
|---|---|---|---|---|---|---|---|---|---|
| vs previous maturity | 0.99 | 0.67 | 0.67 | 0.56 | 0.55 | 0.53 | **0.44** | 0.53 | 0.51 |
| vs 1m bill | 0.99 | 0.88 | 0.82 | 0.69 | 0.64 | 0.61 | 0.59 | 0.57 | 0.56 |

The bill curve sloped upward about 94–98% of the time. Longer spreads over the previous maturity were positive 72–81% of the time.

**Curve steepness and subsequent 20y returns, 1970–94**

| 20y − 1m spread at month start | Months | Annualized 20y return |
|---|---|---|
| < 0bp (inverted) | 45 | −2.57% |
| 0–300bp | 148 | 9.44% |
| > 300bp | 107 | 12.46% |

**Other markets, 1985–94 (1–3y vs 7–10y sectors)**

| Market | Yield spread | Return premium |
|---|---|---|
| U.S. Treasury | 1.11 | 2.52 |
| Agency / AAA–AA / A / BBB | 1.33 / 0.96 / 0.95 / 1.15 | 2.28 / 1.77 / 1.67 / 1.81 |
| Canada / Japan / Australia | 0.41 / 0.55 / 0.37 | 1.36 / 1.63 / 1.65 |
| Britain / France | 0.24 / 0.24 | 1.45 / 1.67 |
| Netherlands / Germany | 0.21 / 0.56 | −0.05 / 0.06 |

Money-market curves 1970–94 (6m − 1m): bills 81bp against CDs 29bp, CP 27bp and Eurodeposits 34bp. The 1m Euro–bill spread averaged above 160bp in the 1970s and 1980s but only 73bp in the 1990s. The 1985–94 Euro–Treasury spread was **V-shaped**: 1.06 (1m), about 0.50 (6–12m), 0.68 (5y).

## Mental Models
- **Front-end premium is structural, long-end premium is regime-dependent.** 1m → 9m returns rose monotonically in all five 5-year subperiods. The ranking of intermediates against the long bond flips with bull or bear inflation trends.
- **Think of the return curve as the risk-premium curve bent by preferred habitat.** Long-horizon liability holders pull long-bond expected returns down, but they are a minority, so the curve still slopes up, only concavely.
- **Prefer volatility, not duration, on the x-axis.** Short rates are more volatile, so duration overstates the risk of the front end relative to the back.
- **Popularity lowers a strategy's return.** Long-horizon investors are lucky to be a minority, because they collect a premium on the asset they find safest (Perold–Sharpe).
- **An average is only as good as its sample's trend.** Before quoting a premium, ask where yields started and ended.

## Worked Example
**Where does duration pay? (from the 1970–94 table, recomputed)**
- Premium per year of duration, front end (1m → 1–2y): (8.52 − 6.87)/(1.3 − 0.08) = **1.35% per duration-year**.
- Back end (1–2y → 20y): (8.87 − 8.52)/(9.8 − 1.3) = **0.04% per duration-year**.
- Volatility over the same back-end move rises from 3.0% to 11.0%. For a Sharpe-maximizer, the marginal duration beyond about 2 years buys volatility, not return.
- Consistency check on the OCR table: GM ≈ AM − σ²/2. For the 20y, 9.51 − 10.98²/200 = 8.91 against 8.87 reported. For the 3m, 7.71 against 7.71, which confirms the 3-month figures read 7.71.

**Stripping the premium out of forwards (hypothetical, using ch02's relation).**
- s₁ = 5.50%, s₂ = 6.20%, so f₁,₂ = 1.062²/1.055 − 1 = **6.90%**. The "forward-implied" 1y rate rise is 140bp.
- Take the long-run premium of a 2y zero over the 1y bill at about 50bp (the 9m → 2–3y geometric gap in the table is roughly 50bp).
- `Δf₁ ≈ E(Δs₁) + BRP₂/1`, so E(Δs₁) ≈ 1.40 − 0.50 = **+0.90%**. The market-expected 1y rate next year is about 6.40%, not 6.90%. This is valid only if the premium is at its long-run average (see ch04).

## Anti-patterns
- **Using a post-1981 database to estimate the long-run premium**: disinflation makes long bonds look far better than their expected return.
- **Using 1926–94 or 1952–94 as "long therefore unbiased"**: decades of inflation surprises make long bonds look too poor. Fama (1984) found average returns peaking at 12–18 months in 1953–82.
- **Assuming the premium is linear in duration or volatility**: the data show a concave curve.
- **Using the historical average as a near-term forecast**: this is only valid if the premium is constant. It is not (see the steepness table).
- **Holding 1-month bills as the "cash" asset**: they have been systematically about 100bp too expensive against 3m bills and other one-month paper.
- **Reading cross-country premia from ten years of data**: Germany went from top (Bisignano 1987) to near bottom after reunification.
- **Assuming a leveraged 2-year note trade captures the front-end premium**: you borrow at private-issuer rates, not bill rates, and the credit spread eats most of it. Only bill holders or the Treasury can arbitrage it away.

## Practitioner Notes
- **Cash management**: replacing 1-month bills with longer bills or other high-grade money-market paper "may be the best reward-to-risk ratio in all capital markets", in Ilmanen's view. The 3-month bill beat the 1-month bill in 99% of years.
- **Credit placement**: the Euro–Treasury spread curve is V-shaped and money-market credit spreads are inverted, so take a large share of desired credit exposure at *short* maturities.
- The duration reward in corporates (1985–94) looks a bit lower than in Treasuries. The comparison is flawed, though: the duration gap between sectors is smaller, negative convexity from calls is ignored, and industry mix differs (utilities issue long, financials short).
- Non-U.S. government yield spreads were smaller than in the U.S. Return premia exceeded yield spreads because long yields fell in 1985–94, except in Germany and the Netherlands. In four of eight countries the 1–3y sector *underperformed* 1-month Eurodeposits.
- Structural forces that could lower the future long-run premium: more long-horizon investors, stronger anti-inflation institutions (central bank independence, market discipline), international diversification, and better liquidity. Opposite forces raised required premia from 1965 to 1980.
- Return volatility peaked in the early 1980s *despite* the shortest durations (high yields), because yield volatility more than offset it.
- Use the steepness table as the bridge to tactical duration: an inverted curve was followed by negative 20y returns, and a steep curve (>300bp) by 12.5% per year.

## Key Takeaways
1. Set strategic duration from long-run premia measured over a neutral sample. In U.S. Treasuries the premium is about 200bp from 1m to 2y and roughly zero beyond.
2. Expected returns are concave in duration and in volatility. Sharpe ratios fall monotonically with maturity.
3. Beyond 2 years, a marginal duration step is close to a coin toss on an annual horizon (hit rates 44–56%).
4. Long bonds are for long-liability investors or for tactical views, not for boosting a short-horizon benchmark.
5. Never quote a historical bond premium without checking the sample's yield trend.
6. Short bills are structurally rich. Extend within the money market and take credit risk at the front.
7. The premium varies with regime and cycle. Use it as the long-run anchor and forecast the near term with the curve and other predictors (ch04).

## Connects To
- **ch01**: the definition of BRP and the concave empirical premium curve.
- **ch02**: the break-even relation used to back out expectations net of BRP.
- **ch04**: time-varying premia (steepness, real yield, inverse wealth, momentum) and dynamic duration.
- **ch05**: the convexity bias, which is the other reason long yields are low.
- **`cfa-asset-allocation-cme` ch04**: building capital-market expectations for bonds (term premium component).
- **`tuckman-fixed-income` ch08**: risk premium in the short-rate process and the effect of mean reversion on the volatility term structure.
- **`cfa-fixed-income` ch07**: liquidity, preferred habitat and segmented-markets theories.
