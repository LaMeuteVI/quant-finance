# Hypothesis: BTC daily 60-day long-only time-series momentum

- **Family**: `btc-daily-tsmom`
- **Market**: crypto-spot
- **Source**: Aster BTC N0 + independent N1-design/literature memos
- **Regime context**: any; explicitly stress-tested in bull, bear and chop periods

## Statement (falsifiable)

On Binance BTC/USDT spot daily close-labelled bars from the sealed pre-2024-07-01 store, allocate long one unit when the trailing 60-calendar-day close return is positive and cash otherwise, with execution no earlier than the next daily bar. Net of the configured 10 bps/side taker fee and 5 bps/side slippage, the development sample will achieve annualised Sharpe >= 1.0, maximum drawdown >= -35%, DSR >= 0.95, and annualised Sharpe >= 0.3 under both two-times costs and two-day execution lag.

## Mechanism

Crypto has fragmented, 24/7 participants and recurring retail/institutional flow. If information diffusion, herding and gradual de-risking dominate at a multi-week horizon, positive 60-day return should be followed by further positive return. A cash-or-long rule does not assume borrow availability or funding economics. The counterparty is an impatient or risk-constrained seller who exits gradually after negative performance, and trend-chasing demand that continues after positive performance. This mechanism is weak and crowded; its only purpose here is a clean baseline that can be rejected quickly.

## Falsification

Reject immediately if the sole development trial fails any pipeline gate, especially DSR < 0.95, annualised Sharpe < 1.0, max drawdown < -35%, or either cost×2 / lag-2 stress Sharpe < 0.3. Also reject rather than tune if the 60-day signal’s daily return is not superior to its *sign-inverted* cash-or-long control in the pre-specified descriptive comparison. No parameter sweep or lookback adjustment follows this result; a later 30-day or 90-day idea is a new, counted hypothesis in the same family.

## Prediction (JSON, written before any test)

```json
{"sharpe_ann_min": 1.0, "max_drawdown_floor": -0.35}
```

## Prior evidence and ledger check

- `desk ledger list --text momentum` returned `[]` on 2026-10-13.
- `desk ledger list --status rejected` returned `[]` on 2026-10-13.
- BTC N0 establishes a pre-cutoff, close-labelled daily derivation with gaps/frozen minutes retained as quality metadata: `research/assets/2026-10-13-btc-n0.md`.
- This is deliberately a single-asset, long-only daily baseline. It makes no cross-sectional or universal crypto-momentum claim and does not inspect the sealed holdout.

## Cost and capacity sanity

The daily rule can change state only after a 60-day sign crossing; expected turnover is low. The generic pipeline has a fixed small-size cost of 30 bps per unit turnover (10 bps fee + 5 bps slippage per side). This deliberately exceeds the current BTC reference spread but does not yet include a size-specific square-root impact model. The dev prediction requires a net result after these costs and after 2× cost stress. Capacity is therefore not claimed; a passing result would still require the separate conservative cost grid before any paper consideration.

## Controls outside the pipeline gate

- **Inverse control:** long when the 60-day return is non-positive, cash otherwise, evaluated descriptively on exactly the same development partition.
- **Placebo:** circularly shift the binary signal by a fixed 17 calendar days before applying it. It preserves turnover/marginal exposure but breaks contemporaneous signal-return alignment. It is diagnostic only, not eligible for selection.
- Neither control changes the registered execution strategy or consumes a second pipeline trial.

## Register

```bash
uv run desk ledger new --title "BTC daily 60d long-only time-series momentum" --statement "..." --mechanism "..." --falsification "..." \
  --prediction '{"sharpe_ann_min": 1.0, "max_drawdown_floor": -0.35}' --family btc-daily-tsmom --market crypto-spot \
  --source aster-btc-n1 --regime any --strategy btc_daily_tsmom_60
```
