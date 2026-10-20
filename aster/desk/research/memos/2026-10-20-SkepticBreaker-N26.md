# F3 v1.1 — Skeptic & Breaker (N26)

**Authors**: Aster (desk agent) · **Date**: 2026-10-20
**Companion to**: `2026-10-20-V0V7-N25.md` (technical audit).
**Purpose**: Independent review of the F3 v1.1 dev verdict before the holdout is read.

---

## Section 10 — Skeptic memo

### Mechanism (where does the edge come from?)
F3 v1.1 is a cross-sectional trend signal: 20/60/120-day EMA of price averaged, then sized to a 10 % annualised vol target per asset. The intuition is **trend persistence in liquid crypto**: bull markets carry for ~60-90 days, bear markets decay, and the 5 majors we use are correlated enough that an aggregate trend + rebalance-band reduces drawdowns. The weekly rebalance (V1 finding) adds: in a 24/7 market with daily volatility, weekly batching of the signal trades roughly the same amount but at lower cost because it stops churning the book.

The mechanism is **not** new — trend-following has been documented since the 1980s (Hurst, Ooi, Pedersen 2017) and crypto trend papers exist (e.g. Han, Li, Sun 2022). The **specific** question is: does it survive costs + capacity on crypto perps? The dev sample says yes.

**Risk**: in a regime shift (e.g. 2022-23 defi summer and rotation), the 120-day lookback may hold losers too long. We saw this in 2022: max DD -22.6 % vs EW5 b&h -65 %. The trend book got out faster than naive holding, but it still had a 22 % drawdown.

### Crowding
Trend signals on crypto perps are well-known. Wintermute, Jump, Tower, all run cross-sectional trend books. The retail signal of moving averages is universal. **The edge, if any, comes from (i) faster reaction in 24/7 markets, (ii) vol targeting reduces drawdowns, (iii) the weekly batching reduces churn.** None of these is exclusive — they are all available to anyone with a 5y backtest. The question is whether they survive realistic costs at scale.

Our dev sample shows Sharpe 1.046 with **the wrong cost model** (constant 15 bps RT). With the **real grid** (V5), Sharpe at 1M is +0.765, at 10M +0.198. **The capacity is real but bounded.** At 10M per side the book is roughly breakeven on Sharpe; above that the strategy dies.

### Survivorship (5 majors)
The 5 majors (BTC, ETH, BNB, SOL, XRP) are survivors from a list of ~10,000 coins. They were chosen because they were liquid when we built the dataset (2024-06 cutoff). This is a **classic survivorship bias**:
- We never traded the coins that died (LUNA, FTT, dozens of failed perps).
- We never saw the coins that became majors after the cutoff.
- The dev sample includes only the future winners.

The 12-symbol R5 panel adds some names that had rough periods (XMR dropped from Binance spot listings in some jurisdictions, SUI/NEAR/FET/AAVE had crash years), but they are still survivors from the same 2024-06 lens.

**Defence**: the strategy is **cross-sectional** not stock-picking — it goes long AND short of the trend signal. Survivorship is less severe than for a long-only basket, but it is not zero (we never traded the dead perps, so we never tested whether a trend signal would have caught their crashes).

### Cost assumption risk (the big one)
The dev Sharpe 1.046 is at constant 15 bps RT. With the grid:
- 1M: Sharpe 0.765
- 10M: Sharpe 0.198

**A 100k USD book is a different trade from a 10M book.** The dev report's `aum_sweep` is misleading because of the constant cost bug (V5). We need to either fix the pipeline default to `GridCostModel` before the holdout, OR pin the holdout allocation to a specific AUM with the grid applied.

### Data snooping risk
- Family `btc-daily-tsmom` has 8 dev trials (1 v1.0, 1 v1.1, 4 V1 diagnostics, 1 V2 re-run, 1 R5).
- DSR at n=8 was 0.984 in v1.1 — Deflated Sharpe adjusts for multiple testing.
- At n=8 trials with 1 win and 7 diagnostics, the DSR penalty is small but not negligible.
- If we add more trials in the family (V4 PBO, more V1 micro-decompositions), DSR may fall below 0.95.

**Recommendation**: do NOT add more trials in this family before the holdout read. The holdout decision is for the **5-major panel v1.1** as already configured.

---

## Section 11 — Breaker memo

### Stress tests (already in report.json)
From `H-20261020-004/.../report.json`:
- **Stress costs ×2** (30 bps RT instead of 15): Sharpe 0.674 — still passes the 0.3 stress floor.
- **Stress costs ×3** (45 bps RT): Sharpe drops further; not stored in the trimmed report, but the engine would produce it.
- **Stress lag 2** (signal computed 2 days ago): Sharpe stays positive (PASS).
- **Stress haircut** (deflated): Sharpe 0.900.

### Regimes
Already covered in V4 — 5 active years, 2022 was the worst at +0.55 Sharpe, no year negative. 2022 is the canonical stress (BTC -64 %, ETH -68 %); the book went to flat quickly because the 120-day trend broke.

### The realistic capacity problem
**The headline dev Sharpe 1.046 is at constant 15 bps RT.** With the realistic grid at 10M USD per side, Sharpe falls to +0.198. **This is below the dev stress floor (0.3)**. The strategy is **NOT viable at 10M+** with current costs. The honest capacity is ~1M USD per side.

### Cost ×3 sanity check
At 100k with constant cost, Sharpe is +1.183 (per V5 test, with constant cost). At 100k with the realistic grid (1k-10k bracket, ~16 bps RT), Sharpe is +0.946. The dev report's 0.674 stress is roughly **50 bps RT**, which is plausible for 1M-10M notional. The **stress ×3 (45 bps RT)** would put the book below 0.3 Sharpe at 10M.

### Lag 2 sanity check
A 2-day lag on the signal — simulating a 2-day execution delay — keeps the book in positive Sharpe territory. Trend signals are robust to small lags by construction (20/60/120 EMAs smooth out daily noise).

### What kills the strategy (ranked)
1. **Cost underestimation** (V5 finding). If the grid replaces the constant, the headline Sharpe is revised down. This is the dominant risk.
2. **Capacity ceiling**. At 10M+ the strategy dies from impact. Capacity must be quoted at 1M, not 50M.
3. **Regime flip from bull to bear**. The 120-day trend is slow; a sharp bear (March 2020, May 2021 China ban) can produce a >10 % drawdown in a month. We saw this with -13.1 % in March 2020.
4. **Survivorship of the universe**. The 5 majors were the right call in 2024-06; if the universe had been chosen in 2020 it would have been different (no SOL until 2020, no SHIB, etc.). The strategy is not stable across universe redefinitions.
5. **Multiple-testing inflation**. At n=8 trials the DSR still passes, but the family is approaching its budget. Future additions would erode DSR.

### What does NOT break the strategy
- Lag 2 (PASS).
- Cost ×2 (PASS stress floor 0.3, Sharpe 0.674).
- Haircut (Sharpe 0.900).
- Look-ahead on rebalance (V2 PASS, 0 violations).
- 2022 bear (Sharpe +0.55).
- BNB/SOL/XRP individual drawdowns (correlated enough that the cross-sectional doesn't rescue them but also doesn't amplify them).

---

## What result would REJECT the holdout

- Sharpe on the 7-month holdout (2024-07-01 → 2025-XX-XX) ≤ 0.3 (deflated by costs ×2).
- Drawdown on holdout < -25 % (worse than dev).
- Time in market on holdout outside [0.30, 0.80] (extended flat OR extended fully-invested are both red flags).
- Trade count on holdout ≈ 0 (signal didn't trigger — universe is dead).

A holdout Sharpe in the range [+0.3, +0.7] would be **marginal** — within the noise of 2509 dev bars vs ~250 holdout bars (1/10 the sample, 95 % CI of Sharpe is approximately ±0.4).

A holdout Sharpe ≥ 0.8 (matching dev) would be a **strong confirm** but would not fully reflect the cost-grid revision (V5); we should also pin the cost model before live.

---

## Recommendation to Samuel

The candidate F3 v1.1 has:
- Sharpe 1.046 dev (constant cost) / ~0.95 dev (grid 1M USD).
- All 6 dev gates PASS at constant cost; **DD and DSR FAIL on the 12-symbol R5 extension**.
- Honest capacity ≈ 1M USD per side with the realistic grid.
- One structural finding from this audit: the AUM sweep in the pipeline is wrong and needs to be fixed before any live allocation is decided.

**Ask**: read the holdout with the dev-granular same pipeline (`H-20261020-004` re-run on 2024-07-01+ bars, same 5 majors, same v1.1 params, with the **grid cost model** to avoid the V5 bug). If the holdout Sharpe (grid) is above 0.5, the dev gate is confirmed; if below 0.3, the dev was over-fit and we go back to diagnosis.

**Do NOT**:
- Read the holdout for R5 (12-symbol panel) — the panel is already falsified on dev.
- Promote to live before the cost grid is fixed in the pipeline default.
- Change the universe definition (5 majors → 12 or anything else) without re-running dev from scratch.