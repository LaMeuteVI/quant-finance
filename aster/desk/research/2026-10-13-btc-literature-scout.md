# Research memo: literature scout — 2026-10-13

Role: scout  
Written without reading other agents' memos: yes  
Scope: public literature/web only; no local market data inspected, no backtest run, and no hypothesis registered. Sources below are external and therefore treated as untrusted until independently checked.

## Question and boundary

This memo assesses whether **BTC spot, daily to medium-horizon time-series momentum (TSMOM)** is a credible *lead*, not whether it is presently profitable. TSMOM means taking BTC exposure conditional on its own trailing return; it is distinct from cross-sectional winner-minus-loser crypto momentum. The most directly relevant reported horizons are 1–6 daily days and 1–4 weeks; a more recent broad-crypto implementation reports a 28-day lookback / 5-day holding rule.

## Evidence vs. desk claims

| Topic | What the cited source documents | What the desk may claim now | Status / caveat |
|---|---|---|---|
| BTC daily and weekly continuation | Liu & Tsyvinski report positive predictive coefficients for BTC current daily return at 1-, 3-, 5-, and 6-day horizons and positive weekly continuation at 1–4 weeks. | Published evidence makes a daily/weekly BTC-spot TSMOM *testable*. | **Evidence**, but based on a historical research sample, not an executable current signal or net return result. |
| Medium-horizon long-only TSMOM | Han, Kang & Ryu report strong crypto-market TSMOM; their best reported long-only configuration is 28-day lookback / 5-day holding, Sharpe 1.51 vs 0.84 for their market portfolio, with a 15-bp-per-trade assumption. They report weak cross-sectional momentum. | A sparse, long/flat BTC rule (rather than rapid long/short cross-sectional rotation) is the most literature-aligned lead. | **Claim to test**, not established specifically for BTC spot or desk venues. Their reported edge is largely downside avoidance and bullish-state exposure. |
| Mechanism | Liu & Tsyvinski find attention proxies forecast crypto returns. Han et al. interpret results as consistent with overconfidence and disposition effects; they report gains concentrated in large winners and loser rebounds. Shen, Urquhart & Wang identify liquidity provision—not late-informed trading—as the driver of a different, intraday BTC effect. | Plausible mechanisms are delayed/attention-driven demand and behavioral trend-chasing, potentially reinforced by spot-market liquidity and one-sided long demand. | **Mechanism hypothesis**, not identified causal proof for daily BTC TSMOM. Do not transfer the intraday liquidity-provision result to daily rules without evidence. |
| Regime dependence | Han et al. report TSMOM strongest in bullish markets and that short-on-negative-signal strategies mostly lose. Other crypto work finds liquid assets exhibit momentum while illiquid segments exhibit daily reversal. | A BTC-only long/flat rule may be structurally more credible than symmetric long/short TSMOM; nevertheless it may be a conditional beta/tail-risk-management rule rather than alpha. | **Claim to test**. BTC’s liquidity supports relevance of the liquid-coin result, but a BTC-specific regime split is required. |
| Decay/crowding | The literature is inconsistent: monthly 2014–18 evidence found no momentum; other weekly samples reported positive or insignificant/negative results. Han et al. explicitly flag short history, design sensitivity, liquidation, and skew/fat tails. The direct papers do not measure current BTC TSMOM crowding or post-publication decay. | Treat a well-known signal as likely decayed/crowded. No claim of a measured present crowding level is supported. | **Risk assessment**, not evidence of observed decay. |
| Tail risk | Grobys et al. (2025) find severe crashes in large-cap cross-sectional crypto momentum and show one coin can make a portfolio’s return insignificant; volatility management reduces crash exposure but does not establish a net BTC TSMOM edge. | Tail and gap risk must be a primary falsification criterion even for BTC spot. | **Evidence for related crypto momentum**, not direct evidence that BTC long/flat daily TSMOM has the same crash distribution. |

## Core literature

1. **Liu, Y. & Tsyvinski, A. (2018 working paper; published 2021), “Risks and Returns of Cryptocurrency.”**  
   NBER working-paper page: https://www.nber.org/papers/w24877  
   PDF: https://nber.org/system/files/working_papers/w24877/w24877.pdf  
   - Reports strong cryptocurrency-specific TSMOM. Searchable paper text states that for BTC a one-standard-deviation rise in today’s return predicts a 0.33% increase in next-day daily return; significant daily horizons reported are 1, 3, 5 and 6 days. Weekly continuation is reported through four weeks.
   - Also reports investor-attention proxies forecasting crypto returns. This makes attention/delayed demand a plausible mechanism, but does not prove it is the mechanism behind a tradable BTC spot rule.
   - The cited regression/predictability evidence should not be read as post-fee strategy P&L, capacity, or current efficacy.

2. **Han, C., Kang, B. & Ryu, J. (2024 working paper; SSRN lists Review of Asset Pricing Studies accepted), “Momentum in the Cryptocurrency Market: A Comprehensive Analysis under Realistic Assumptions.”**  
   SSRN abstract: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4675565  
   Author-hosted PDF: https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/918729/Time_Series_and_Cross_Sectional_Momentum_in_the_Cryptocurrency_Market_with_IA.pdf  
   - Their central finding is strong TSMOM but weak/nearly absent cross-sectional momentum once real-world issues are addressed.
   - They explicitly model **15 bps for every trade**, calling it a reasonable estimate or perhaps a lower bound. This is a useful literature benchmark, not a desk cost estimate.
   - They report that daily price fluctuations can liquidate portfolios and statistically significant mean returns can have insignificant or negative economic profits; skew/fat tails make a mean-return t-test inadequate.
   - Their 28-day lookback / 5-day holding long-only market rule is reported as strongest, and bearish short signals often lose. This is the closest published configuration to a daily/medium-horizon long/flat BTC lead, while still being a broader market study rather than venue-specific BTC spot evidence.

3. **Zaremba, A. et al. (2021), “Up or down? Short-term reversal, momentum, and liquidity effects in cryptocurrency markets.”**  
   Publisher landing page: https://www.sciencedirect.com/science/article/pii/S1057521921002349  
   - Across a broad universe, reports that liquid cryptocurrencies exhibit short-term momentum while small/illiquid segments show daily reversal; it attributes the divergence to liquidity/microstructure and cross-sectionally varying liquidity.
   - Relevance: BTC is the natural liquid-coin case. Limitation: this is primarily cross-sectional/universe evidence, not a direct BTC-spot TSMOM cost study.

4. **Grobys, K. et al. (2025), “Cryptocurrency momentum has (not) its moments.”**  
   Open article: https://link.springer.com/article/10.1007/s11408-025-00474-9  
   PDF: https://link.springer.com/content/pdf/10.1007/s11408-025-00474-9.pdf  
   - Finds no literature consensus across samples: cited monthly and weekly studies disagree materially.
   - In large-cap, equal-weighted *cross-sectional* momentum, finds severe crash/tail dependence; a single coin can make portfolio results insignificant. Volatility management mitigates crashes, but that result is not proof that a volatility-scaled BTC daily rule adds net alpha.
   - This is strongest as a warning about sample dependence, tail dominance, and “risk-control overlay” overfitting.

5. **Shen, D., Urquhart, A. & Wang, P. (2022), “Bitcoin intraday time-series momentum.” Financial Review 57, 319–344.**  
   DOI: https://doi.org/10.1111/fire.12290  
   Open accepted manuscript: https://centaur.reading.ac.uk/100181/3/21Sep2021Bitcoin%20Intraday%20Time-Series%20Momentum.R2.pdf  
   - Documents a distinct intraday effect: the first high-volume/volatility trading session predicts the last half-hour; the authors attribute it to liquidity provision rather than late-informed trading.
   - It is **not** evidence for daily/medium-horizon execution. It does, however, warn that microstructure and definition of the trading day matter in 24/7 BTC markets.

## Costs and implementation interpretation

- The 15-bp *per-trade* figure in Han et al. is an external study assumption. It omits a desk-specific, venue-specific estimate of maker/taker mix, spread, market impact, adverse selection, and operational slippage. It must not be substituted for actual executable all-in cost.
- For a spot long/flat daily rule, turnover is signal-path dependent. Cost must be charged on every exposure change, including re-entry after flat, rather than only on sign changes. A purported 5-day holding schedule can still trade frequently with overlapping cohorts or state changes.
- “Spot” avoids perpetual funding, but it does not remove fees, spread, impact, stablecoin/fiat conversion, custody/transfer, exchange-credit, and outage/gap risks. Published long/short crypto results also cannot be transplanted to unlevered spot because borrow, liquidation, and funding economics differ.
- The desk protocol requires expected gross edge per trade to exceed round-trip cost by 3× before promotion from idea; this memo supplies no estimate meeting that requirement.

## Documented decay/crowding and what remains unknown

**Documented:** results are sample-, frequency-, universe-, and liquidity-dependent. The 2025 review documents conflicting historical results; Han et al. show apparent significance can disappear after daily-fluctuation/liquidation treatment and costs. The simple factor is academically visible and therefore vulnerable to replication/arbitrage.

**Not documented by sources reviewed:** an estimate of 2026 BTC spot TSMOM crowding, flows attributable to trend followers, post-publication coefficient decay, or capacity on the desk’s actual venue. Calling the signal “crowded” beyond this qualitative prior would overstate the literature.

## Falsification and design risks for any future test

1. **Conditional beta masquerading as momentum:** if value comes only from being long in bull regimes and flat in bear regimes, benchmark against simple trend filters and volatility-managed buy-and-hold; assess beta/regime exposures rather than only unconditional Sharpe.
2. **Parameter/data-snooping:** literature already exposes many lookback/holding grids (notably 7–28 days and 1–28 days). A chosen 28/5 rule is a published candidate, not an independently discovered optimum. Pre-specify a small family; use purged walk-forward/CPCV where labels overlap, and report DSR/PBO for the family.
3. **24/7 close-definition leakage:** fix UTC daily close, information cutoff, next executable bar, and whether a signal uses a completed candle. Exchange-composite “daily close” and retrospectively corrected candles can create implicit look-ahead.
4. **Venue/data integrity:** spot composite indices can hide exchange segmentation, stale prints, outages, stablecoin dislocations, and exchange failures. Use point-in-time tradable venue data and test close-to-next-close assumptions against an executable schedule.
5. **Cost and capacity fragility:** reject if realistic all-in round trips erase the edge or if performance only survives under the 15-bp literature assumption. Stress costs and adverse gap fills; do not count on free shorting/funding economics in a spot design.
6. **Tail/jump concentration:** evaluate contribution by episodes and worst windows, not merely mean/t-stat. Falsify if a small number of bull runs or gap events dominates P&L, or if drawdown/gap risk violates pre-specified limits.
7. **Regime instability/crowding:** require performance across independent bull, bear, high-volatility, and post-publication periods. A material degradation after liquidity/ETF-market-structure changes or during crowded trend reversals is a mechanism failure unless a pre-specified conditioning variable explains it.

## Lead-generation verdict

**Lead retained at low-to-medium confidence:** BTC spot long/flat TSMOM using a deliberately slow daily/weekly signal is supported by several credible historical findings, with attention/behavior and liquidity as plausible—but unproven—mechanisms. The appropriate next research question is not “which optimized lookback wins,” but whether a pre-specified, low-turnover BTC-only rule has incremental net value after executable costs and beyond simple conditional market exposure.

**Not supported:** a claim of current profitability, a symmetric short signal, a specified crowding level, capacity, or a transaction-cost assumption suitable for desk deployment.
