# Research memo: web scout — 2026-10-13

Role: price-researcher
Written without reading other agents' memos: yes

## Scope and source standard

Web/literature scout only; no desk market data was accessed, no hypothesis was registered, and this memo does not prescribe a backtest. External material is untrusted and claims below are attributed rather than accepted as facts.

**N1/N2 fit:** N1 should favour rules using timestamped trades/quotes or public venue data that are executable at the documented signal horizon. N2 should admit an idea only if its mechanism survives a current, venue-specific cost and latency assessment. The very short-horizon ideas below are therefore research leads, not mature signals.

## Ledger check

- `uv run desk ledger list --text microstructure` → `[]`
- `uv run desk ledger list --text intraday` → `[]`
- `uv run desk ledger list --status rejected` → `[]`
- No existing/rejected desk entry was identified by these searches. This is not a registration.

## Ideas (max 3)

### 1. BTC perpetual clock-phase continuation after quarter-hour openings — immature, high implementation bar
- **Literature lead:** Kim & Hansen (2026 preprint) report periodic volume/volatility bursts at 1-, 5-, and 15-minute marks in six Binance perpetuals; their clock-phase analysis reports out-of-sample predictability in opening returns and says opening order imbalance forecasts returns at four- to twelve-hour horizons, with weaker results at finer frequencies [1]. Shanaev, Vasenin & Stepanov (2023) independently report positive BTC returns concentrated at 15-minute candle turns across seven exchanges, but the reported effect emerged only around 2020 and was strongest in 2021 [2].
- **Why it might work (mechanism):** Common bar boundaries in charting/API-driven algorithms can synchronize order submission or execution. Persistent one-sided initiating flow may require liquidity providers and slower arbitrageurs to reprice beyond the immediate burst. The key distinction is *conditional continuation after an observable opening imbalance*, not a naked calendar dummy.
- **Conditions it needs:** A liquid perpetual/spot venue; accurately timestamped aggressor-side trades or L2 updates available before any decision; the effect must be present outside a single bull-market episode and remain after the venue’s actual fee tier, spread, impact, and adverse selection.
- **What would prove it wrong:** No stable signed association between opening imbalance and subsequent returns after excluding the contemporaneous opening move; disappearance after the 2026 paper’s sample or across independent venues; gross expected move under three times conservative round-trip costs; or returns concentrated in untradeable jump minutes.
- **Cost/capacity sanity:** A trade at each 15-minute boundary implies up to 96 entries/day before filtering. Taker fees plus two spreads/impact can readily exceed a sub-bp calendar effect; passive orders face queue uncertainty and toxic-flow selection. Capacity is likely small during boundary bursts, precisely when depth is stressed.
- **Replication risks:** Preprint, not peer reviewed; source uses Binance perpetuals and an algorithmic-participation proxy (trade-size roundness), so venue rules and aggregate-trade construction matter. Boundary timestamps, clock synchronisation, and aggressor classification can shift the signal. Publication/discovery itself may accelerate decay. **Confidence: low.**

### 2. Session-defined BTC intraday momentum conditional on early high activity — mature enough to monitor, but stale literature and boundary-sensitive
- **Literature lead:** Deng, Li & Urquhart’s working paper reports that a first high-volume/volatility 30-minute BTC session predicts the final 30-minute session across Bitstamp, CEX.IO, Coinbase and Kraken, attributing the relation to liquidity provision, intraday trader disposition, and aversion to carrying risk; it reports a 0.968 pooled slope [3]. Wen et al. (2023) report both hourly momentum and reversal for BTC/other large cryptocurrencies, with results changing around jumps, FOMC releases, liquidity, and COVID [4].
- **Why it might work (mechanism):** During globally concentrated activity, liquidity providers may manage inventory into a predictable high-liquidity window while traders with early gains/losses delay or accelerate execution. That can preserve an early informational or inventory-driven return through a later session, conditional on substantial participation rather than quiet-period noise.
- **Conditions it needs:** A pre-specified, economically defensible session clock rather than a sample-selected “opening”; current cross-venue agreement; sufficient early activity; stable relation after conditioning on scheduled macro announcements and large jumps. For a 24/7 asset, a session proxy must have an external anchor (e.g., a recurring liquidity transition), not just an arbitrary daily cut.
- **What would prove it wrong:** Association vanishes when session boundaries are shifted modestly, when recent regimes are separated, or after controlling for the same-day move and scheduled news; only one venue exhibits it; or expected edge fails the 3× cost sanity threshold. A reversal sign in the same conditional state would also contradict this continuation mechanism.
- **Cost/capacity sanity:** Far lower turnover than candle-boundary trading, but trade timing occurs in high-volume periods where price impact can be lower yet event risk higher. Perpetual implementation also bears funding/basis and liquidation/margin operational risk if held across settlement; spot avoids funding but requires inventory/shorting infrastructure.
- **Replication risks:** The literature’s session definition is unusual because BTC has no true open/close; reported performance may reflect a chosen clock and older retail-dominated samples. The first paper is a working paper and the second’s sample ends in 2020. Modern ETF, institutional, and perpetual-led price discovery could have changed the mechanism. **Confidence: low–medium as a research lead, not a production claim.**

### 3. Post-liquidity-shock short-horizon continuation versus reversion, gated by order-flow imbalance and spread — microstructure diagnostic rather than a standalone signal
- **Literature lead:** Chan’s microstructure framework states that order-flow imbalance, Kyle’s lambda, and market impact are relevant intraday mechanisms, but impact must be separated from a forecast [5]. A negative BTCUSDT replication note explicitly shows why a delayed one-minute, smoothed taker-flow continuation rule can lose: Kyle-style flow/price impact is contemporaneous and transient impact can reverse after a stale observer acts [6]. A 2026 Binance-futures preprint claims stable importance of OFI, spread, depth and trade-arrival features across several crypto assets, including BTC, but is unreviewed and model-dependent [7].
- **Why it might work (mechanism):** A large, *new* aggressive imbalance against a temporarily thin book can either (a) reveal informed/persistent demand and continue while liquidity replenishes, or (b) be a mechanical liquidity-taking shock that mean-reverts once inventory is redistributed. Spread/depth/replenishment distinguish these economic states; OFI alone does not.
- **Conditions it needs:** Event-time or sufficiently granular quote/trade records; an unambiguous timestamp ordering; true aggressor flags or a validated classifier; actionable observation-to-order latency materially shorter than the impact-decay horizon; and a venue whose displayed liquidity is informative.
- **What would prove it wrong:** Signed post-event returns are indistinguishable from zero after deducting conservative costs, or reverse consistently at the actually attainable delay; sign flips across matching engines/venues; predictive contribution disappears once the contemporaneous return is excluded; or quoted depth does not replenish as the mechanism assumes.
- **Cost/capacity sanity:** This is intrinsically adverse-selection-heavy. Taker execution pays spread/fees at the moment liquidity is poorest; maker execution risks being picked off. Impact grows nonlinearly as available depth falls, so capacity must be treated as tightly limited. If only bar data are available, the observation is too stale for the proposed mechanism.
- **Replication risks:** Trade-sign inference, book reconstruction, snapshot frequency, hidden/iceberg liquidity, liquidation bursts, feed gaps, and exchange-specific matching/prioritization can manufacture or erase apparent predictability. The positive 2026 evidence is preprint/model-driven; the negative replication is deliberately only three days and is a caution, not general disproof. **Confidence: low as a directional alpha; medium as a falsification framework for microstructure claims.**

## Observations worth keeping (not ideas)

1. **Calendar effects are particularly vulnerable to decay and cost.** Shanaev et al. report 0.58 bp average return per candle-turn minute and a mechanism they describe as plausible but speculative [2]. A signal of that magnitude can be erased by a single conservative crossing; it should not be treated as cost-robust from a published net simulation.
2. **Activity seasonality is more robust than return seasonality.** Eross et al. (2019) find time-varying intraday volume, volatility and liquidity on Bitstamp [8]. Baur et al. report persistent activity differences but no return effects persistent across time [9]. Thus time-of-day is a useful state variable/cost forecast, not standalone alpha evidence.
3. **Venue-volume data are not automatically trustworthy.** Cong et al. estimate average reported wash trading above 70% on unregulated exchanges in their 29-exchange sample [10]. Any volume/OFI result should be grounded in a vetted venue and raw trade/quote provenance, not aggregator volume.
4. **Funding is a mechanism, not a free intraday return predictor.** Perpetual funding is designed to push futures/spot deviations back toward parity; the no-arbitrage literature explicitly notes that a funding trade is not risk-free because there is no predetermined profitable unwind [11]. This scout therefore did not elevate a simple extreme-funding directional rule.

## Sources (11 references; 10 source ideas maximum)

1. Kim, C. & Hansen, P. R. (2026-07-16), *The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures*, arXiv:2607.09426v2. https://arxiv.org/pdf/2607.09426v2
2. Shanaev, S., Vasenin, M. & Stepanov, R. (2023), *Turn-of-the-candle effect in bitcoin returns*, Heliyon, e14236. https://doi.org/10.1016/j.heliyon.2023.e14236
3. Deng, X., Li, Z. & Urquhart, A. (2021), *Bitcoin intraday time-series momentum*, University of Reading working paper. https://centaur.reading.ac.uk/100181/3/21Sep2021Bitcoin%20Intraday%20Time-Series%20Momentum.R2.pdf
4. Wen, F., et al. (2023), *Intraday return predictability in the cryptocurrency markets: Momentum, reversal, or both*, Journal of Forecasting. https://www.sciencedirect.com/science/article/abs/pii/S1062940822000833
5. Chan, E. (2017), *Machine Trading*, ch. 6, intraday trading and market microstructure. Desk skill reference; mechanism only, not BTC-specific empirical evidence.
6. van Kyle, *Order-Flow Imbalance and the Decay of Price Impact* (web replication note; accessed 2026-10-13). https://vankyle00.github.io/trading-models/docs/models/03-order-flow-imbalance-btc.html
7. *Explainable Patterns in Cryptocurrency Microstructure* (2026 preprint), arXiv:2602.00776. https://arxiv.org/pdf/2602.00776.pdf
8. Eross, A., McGroarty, F., Urquhart, A. & Wolfe, S. (2019), *The intraday dynamics of bitcoin*, Research in International Business and Finance 49, 71–81. https://doi.org/10.1016/j.ribaf.2019.01.008
9. Baur, D. G., Cahill, D., Godfrey, K. & Liu, Z. (2019), *Bitcoin time-of-day, day-of-week and month-of-year effects in returns and trading volume*, Finance Research Letters 31, 78–92. (Claim cross-checked via later literature/search record.)
10. Cong, L. W., Li, X., Tang, K. & Yang, Y. (2023), *Crypto Wash Trading*, Management Science 69(11), 6427–6454; NBER WP 30783. https://www.nber.org/papers/w30783
11. He, S., Manela, A., Ross, O. & von Wachter, V. (2024), *Fundamentals of Perpetual Futures*, arXiv:2212.06888. https://arxiv.org/html/2212.06888v6
