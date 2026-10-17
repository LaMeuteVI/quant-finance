# Backtest standard

A backtest exists to find out whether a strategy is fake. Implements the 10 checks of skill `quant-backtest-hygiene`, adapted to crypto. Items marked [code] are enforced by `desk backtest`; [you] are your responsibility and must appear in the report.

## Timing and leakage
- [code] Weights at bar t use data up to t; execution lag >= 1 bar; stress at lag 2.
- [code] Truncation look-ahead test on every run (`validation/lookahead.py`). Failure = broken strategy.
- [code] The currently forming bar is dropped at fetch time.
- [you] No full-sample statistics (z-scores, PCA, scalers, thresholds) unless fitted on a rolling/expanding window. No `bfill`, centered windows, `shift(-k)`.
- [you] ML models: purged k-fold with embargo (`validation/cv.py::PurgedKFold`), labels from `research/labeling.py` with `t1`. Never plain k-fold or random shuffles on time series.

## Samples
- [code] Most recent `holdout_frac` (25%) sealed per hypothesis at its first run; read once after `backtest_passed`.
- [you] Prefer walk-forward evaluation (`validation/cv.py::walk_forward`) for any fitted parameter; report the per-window results, not just the aggregate.
- [you] Report results by regime: bull (2020-21, 2023-24), bear (2022), crash windows (Mar-2020, May-2021, Nov-2022 FTX), chop. A strategy that works in one regime only is a regime bet; say so.

## Costs (crypto)
- [code] Fees + slippage per side on drift-aware turnover; stress at 2x and 3x.
- [code] Funding on perps, per bar held (fetch with `desk data fetch --funding`).
- [you] Use your actual fee tier. Alts and size: raise slippage (square-root impact: cost ~ spread/2 + k * sigma * sqrt(order / ADV)).
- [you] Borrow costs and availability for spot shorts; perp basis risk.

## Statistics and multiple testing
- [code] PSR, DSR with the family's trial count, MinTRL, Bonferroni haircut Sharpe.
- [code] Dev gate (desk.yaml `gates`, tightened by the prediction): min obs, Sharpe, max DD floor, DSR >= 0.95, Sharpe under 2x costs and lag 2.
- [you] Parameter sweeps: PBO via CSCV < 0.3. Report the full distribution, not the best config.
- [you] Turnover, average holding period, number of independent bets per year. Fewer than ~30 independent bets: statistics are weak; say so.

## Crypto-specific biases
- **Survivorship**: today's top coins are survivors. Test on point-in-time universes when the hypothesis is cross-sectional (rank by trailing volume/market cap at each date, including delisted coins: LUNA, FTT, etc.). Results on the current universe are an upper bound.
- **Exchange risk**: one venue's prints can be wrong or manipulated (wash trading on small venues). Cross-check closes against a second venue for any surprising result.
- **Listing effects**: early bars of a new listing are wild; exclude the first 30 days per asset for cross-sectional work unless the hypothesis is about listings.
- **Stablecoin and quote risk**: USDT is not USD. Note depeg episodes in the stress section.
- **24/7 market**: daily bars close at 00:00 UTC; weekends are trading days; annualize with 365.

## Report
Use `templates/backtest_report.md`. Every number cites its artifact. State what was not tested.
