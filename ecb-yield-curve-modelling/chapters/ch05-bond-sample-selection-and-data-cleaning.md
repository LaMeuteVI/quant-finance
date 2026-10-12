# Chapter 5: Conceptual Framework for Bond Sample Selection and Data Cleaning
> **Source**: ECB Statistics Paper No 27 (2018), §4.1 to §4.3, Table 9 (Conclusions), Table F.1 (Appendix 6) | Nymand-Andersen

## Core Idea
Yield-curve quality is decided before any model is fitted. The paper's "12 golden data recommendations" turn a raw universe of about 720 euro area government bonds into about 318 clean, liquid, homogeneous bonds per day, so that curve changes reflect changes in yields and not changes in the sample. Higher quality always beats larger quantity.

## Frameworks Introduced
- **Conceptual framework for a high-quality bond sample (12 dimensions, Table 9)**:
  1. **Supplier of data**: assess vendors on mandatory fields, definitions and price methodology, stable formats, delivery channels, test files and error correction, price, confidentiality.
  2. **Type of instrument**: keep curves separate by instrument type; do not mix money-market instruments with bonds (different statistical properties); if money-market rates are used, prefer EURIBOR; exclude Brady, convertible, embedded-option, step-up/down, variable-rate, inflation-linked and perpetual bonds unless rules are set.
  3. **Sector**: central government per ESA 2010 (S.1311); state and local government excluded for the euro area.
  4. **Credit risk**: ratings (Fitch) to isolate a near risk-free curve, e.g. AAA sovereigns.
  5. **Liquidity**: turnover or bid-ask thresholds.
  6. **Price type**: same reference time, preferably mid-quote near 17:00 CET close.
  7. **Maturity spectrum**: residual maturity from 3 months to 30 years.
  8. **Removal of outliers**: two-standard-deviation rule per maturity bracket, iterated.
  9. **Special effects and adjustments**: day-count and settlement conventions; no direct coupon or tax adjustment.
  10. **In-sample and out-of-sample population**: hold out 1 bond in 10 (ch06).
  11. **Sample size**: quality first; with small samples use averages or widen outlier bands.
  12. **Time periods**: test across stable, rate-rise, rate-cut and high-volatility regimes (ch06).
- **Outlier removal procedure** (step list in Patterns): per maturity bracket compute mean and standard deviation of yields; drop bonds beyond 2σ; recompute; repeat once more.
- **Benchmark-only alternative**: benchmark bonds (lowest yield in a maturity range, most traded, or price-process based) give stable composition but cut the sample by 50% in the euro area data and force fixed maturity points.

## Key Concepts
- **Raw versus clean sample**: ~720 raw bonds, average 318 selected per day (range 269-354), data from EuroMTS (Fitch ratings), 502 trading days.
- **Turnover threshold**: prices considered reliable above EUR 100,000-200,000 traded per day; ECB chose EUR 1 million (5-10 times higher); testing showed actual turnover of EUR 20-100 million.
- **Bid-ask spread threshold**: maximum 3 bp; mean spread in sample was 4-5 bp (Chart 2) before filtering.
- **Executable (binding) price versus real trade price**: executable quotes are immediately hit-able; real trades near 17:00 differ from quotes by about 1% to 1.8% of price in the sample, and trades are far fewer than quotes.
- **Mid-price**: flat price from the average of the best bid and ask at or before 17:00 with spread at most 3 bp.
- **Traded-days rule**: e.g. trade at least 3 out of 5 sequential days if traded and quoted prices diverge strongly.
- **Time stamp**: prices must share one reference time; intraday volatility is large.
- **Short-maturity distortion**: bonds under 3 months show much higher yield volatility and low information content.
- **Very long bonds**: above 30 years few bonds, prices reflect institutional duration demand.
- **ESA 2010**: sector classification (central government S.1311, other general government S.1312-1314, MFIs S.121-123, other financial intermediaries S.125, non-financial corporations S.11).
- **Target calendar**: curves produced on all TARGET business days.
- **Sample representativeness**: a weighted goodness-of-fit indicator compensates for many short-maturity bonds and few long ones (ch06).

## Formulas & Reference Tables
- **Outlier rule**: drop bond i in bracket b if `|yᵢ − ȳ_b| > 2·σ_b`; recompute ȳ_b, σ_b on survivors and repeat once (two layers).
- Share of bonds by residual maturity (daily average, 1 April 2003 to 31 March 2005): 0-3m 7%, 3-6m 8%, 6-9m 6%, 10-12m 6%, over 1 year 74%; bonds under 1 year are 20-30% of the sample (26% average).
- Yield spread bond minus EURIBOR at 3 months averaged about −4.9 bp, with 1 and 2 months showing abnormal dispersion.

| Design choice | Recommended | Reason |
|---|---|---|
| Sector | Euro area central government only | Comparable issuers |
| Coupon type | Zero and fixed coupon, strips | Removes option/indexation effects |
| Maturity | 3 months to 30 years | Noise below 3m, sparse above 30y |
| Money-market mix | No | Different properties |
| Price | Mid-quote near 17:00 CET (or last trade) | Homogeneous information set |
| Liquidity | Turnover at least EUR 1m/day, bid-ask at most 3 bp | Informative prices |
| Outliers | 2σ per maturity bracket, twice | Noise control |
| Yields | Pre-tax, convention-adjusted | No reliable direct coupon/tax adjustment |
| Out-of-sample | 1 in 10 bonds | Full maturity coverage |

## Mental Models
- **Garbage-in rule**: the paper's line is that data quality is king; differences between models are smaller than differences caused by sample changes.
- **Liquidity is information**: the more trades, the more prices reflect views, so filter on turnover and spreads, not on issue size (size removes small but liquid issues in small markets and keeps big illiquid ones).
- **One clock**: a curve is a snapshot; all inputs need one time stamp.
- **Segment your instruments**: money-market and bond curves react differently; do not splice without evidence.

## Worked Example
Outlier filter on one maturity bracket (illustrative, recomputed): ten bonds with yields (%) 3.10, 3.12, 3.11, 3.13, 3.09, 3.12, 3.10, 3.11, 3.45, 3.12.
Round 1: mean 3.145, σ ≈ 0.105 (population). Band = 3.145 ± 0.21 = [2.935, 3.355]. The 3.45 bond is outside → removed.
Round 2: mean of remaining nine = 3.111, σ ≈ 0.012; band [3.087, 3.135]. All remaining are inside (3.09 to 3.13), none removed.
Interpretation: iteration matters, since the outlier inflated σ in round 1; without iteration a milder outlier could survive.

## Anti-patterns
- **Screening by amount outstanding**: removes small liquid issues, keeps big illiquid ones.
- **Mixing price definitions or times** (traded, reference, open, close).
- **Keeping under-3-month bills** in a coupon-bond curve.
- **Skipping descriptive statistics** and going straight to model fitting.
- **Comparing models on different samples**: results reflect data, not models.

## Practitioner Notes
- Number of bonds per maturity class is stable; lowest count (about 16) at 5-10 years, highest (about 66) at 3m-1y. Samples dip around 24, 29, 31 December, and jumped by 65 bonds on 1 July 2004 from new zero-coupon issues (Belgium +17, France +13, Italy +14).
- Sample stable over time for highest-rated or all-rated bonds: benchmark-only filtering is not needed in the euro area.
- Coupon differences affect yields' comparability but no suitable direct adjustment exists; outlier removal catches the rest.
- General government is 48% of euro area securities outstanding (EUR 7,950 billion, October 2017).
- After the 2007 crisis spread widening increased error terms; convergence 1999-2007.

## Key Takeaways
1. Do descriptive statistics first; clean data before fitting.
2. Central-government, plain-vanilla, AAA or credit-homogeneous bonds.
3. Liquidity by turnover and bid-ask, not by issue size.
4. One reference time; mid-quote at 17:00 CET.
5. 3 months to 30 years; do not splice money-market rates.
6. Two-layer 2σ outlier removal per maturity bracket.
7. Keep a stable composition across time; log sample changes.
8. Quality over quantity, but check each maturity bracket remains populated.

## Connects To
- **ch06**: test design (in-sample / out-of-sample split, evaluation).
- **ch07**: clean-sample effects on results.
- **ch08**: ECB operational settings.
- **`tuckman-fixed-income` ch21**: input choice for curves.
- **`cfa-fixed-income` ch01**: bond features to screen out (options, floaters).
