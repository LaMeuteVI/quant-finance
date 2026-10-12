# Chapter 9: Security Market Indexes (Equity)

## Core Idea
An index represents a market, segment or asset class. Five decisions define it:
1. Target market.
2. Security selection.
3. Weighting scheme.
4. Rebalancing policy.
5. Reconstitution policy.

The weighting scheme drives the index's biases. Price-return and total-return versions differ by the income reinvested.

## Frameworks Introduced
- **Price return vs total return**:
  - `PR = (V₁ − V₀)/V₀ = Σwᵢ·PRᵢ`.
  - `TR = (V₁ − V₀ + Income)/V₀ = Σwᵢ·TRᵢ`.
  - Over several periods returns **compound**: `V_T = V₀·Π(1 + Rₜ)`.
- **Weighting schemes**:

| Scheme | Weight | Pros | Cons |
|---|---|---|---|
| Price-weighted (DJIA, Nikkei) | Pᵢ/ΣP | Simple | High-price stocks dominate; splits require divisor changes |
| Equal-weighted | 1/N | Simple, no concentration | Small caps overweighted; frequent rebalancing |
| Market-cap weighted (value) | MVᵢ/ΣMV | Reflects the investable market; self-rebalancing | Overweights stocks that have risen (momentum/overvaluation) |
| Float-adjusted cap weighted | Free-float MV | Investable shares only | Needs float estimates |
| Fundamental weighted | Revenue, earnings, book, dividends | Contrarian, value tilt | Deviates from the market portfolio |

- **Index management**:
  - **Rebalancing**: restore the target weights, often quarterly. Needed for equal-weighted and fundamental indexes.
  - **Reconstitution**: change the constituents after IPOs, bankruptcies, M&A or delisting.
- **Uses of indexes**: gauge sentiment, proxy the market for CAPM beta, proxy asset classes in allocation, benchmark active managers, serve as model portfolios (index funds, ETFs).
- **Equity index families**:
  - **Broad market** (Russell 3000 ≈ 98% of US equity).
  - **Multi-market** (MSCI: developed, emerging, frontier).
  - **Sector**.
  - **Style**: size, value/growth.
- **Fixed-income indexes**: the universe is huge and trades mostly through dealers and illiquidly, so prices are often estimated with matrix pricing. Turnover is high as bonds mature. Classified by issuer, collateral, currency, maturity, credit quality and inflation linkage.
- **Alternative indexes**:
  - **Commodities**: futures-based, so roll returns matter. Weights are equal or based on production/liquidity, which can bias toward energy.
  - **Real estate**: appraisal, repeat-sales and REIT indexes (FTSE EPRA/NAREIT).
  - **Hedge funds**: self-reported data, which creates **survivorship** and **backfill** biases. The constituents choose the index, not the reverse.

## Key Concepts
- **Constituent securities**; **divisor** in price-weighted indexes.
- **Free float**: shares available to the public, excluding strategic holdings.
- **Survivorship bias**: failed funds drop out of the index, which inflates its returns.

## Mental Models
- **Weighting = embedded strategy**: cap weighting follows momentum; equal and fundamental weighting tilt toward small caps and value.
- **Benchmark must match the mandate**: judge a small-cap manager against a small-cap index.
- **Distrust hedge fund index returns**: they are biased upward.

## Anti-patterns
- **Comparing a total-return fund with a price-return index**: this overstates the manager's alpha.
- **Assuming price-weighted indexes are neutral**: a stock split changes the weights.
- **Treating bond index prices as transaction prices**: many are estimates.

## Worked Example
**Three stocks.** A: price 10 → 12, 1,000 shares. B: 50 → 45, 200 shares. C: 100 → 110, 100 shares.
- **Price-weighted**: (12 + 45 + 110)/(10 + 50 + 100) − 1 = 167/160 − 1 = **+4.38%**. C dominates.
- **Equal-weighted**: average of (+20%, −10%, +10%) = **+6.67%**.
- **Cap-weighted**: MV₀ = 10k + 10k + 10k = 30k; MV₁ = 12k + 9k + 11k = 32k → **+6.67%**. The cap weights happened to be equal here.

## Key Takeaways
1. Price return excludes income; total return includes it. Multi-period returns compound.
2. Price weighting favors high-priced stocks. Equal weighting favors small caps. Cap weighting favors stocks that have risen.
3. Rebalancing changes weights; reconstitution changes constituents.
4. Fixed-income indexes face liquidity, pricing and turnover problems.
5. Hedge fund indexes suffer from survivorship and backfill bias.

## Connects To
- **Ch 8**: market structure.
- **Ch 10**: passive investing and efficient markets.
- **Ch 12**: equity classes.
- **Ch 14–18**: fixed-income characteristics.
