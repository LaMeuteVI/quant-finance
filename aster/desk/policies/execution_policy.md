# Execution policy

## Principle
The trading loop is deterministic code, scheduled without an LLM: `desk trade run --hypothesis H --broker <paper|testnet|live>`. It loads the strategy and parameters of the last PASSED dev trial (the exact validated version), computes the latest target weights, and rebalances through the router. The agent studies the results; it does not sit in the order path.

## Modes
| Mode | Broker | Requirements |
|---|---|---|
| paper | local simulation on public prices | hypothesis in `paper`, `paper_passed`, `live_pilot`, `live` |
| testnet | exchange sandbox (Binance Spot Testnet) | same + testnet keys |
| live | exchange spot sub-account | `risk_limits.mode: live` + `ASTER_LIVE_ARMED=1` in the running shell + hypothesis in `live_pilot`/`live` (human promotion) + live keys |

## Order rules
- Sells before buys (free cash). Rebalance band 2% of equity per asset; minimum trade 10 USD.
- Market orders for daily-bar strategies on majors; limit orders with a price band for alts or size > 0.1% of daily volume.
- Every decision (approved or rejected) and every fill is journaled with the account snapshot; the journal is hash-chained.
- Exchange errors are journaled and re-raised; never retried blindly. Partial fills: the next run reconciles from the actual balance.

## Monitoring execution quality
- Realised slippage = fill price vs reference price, per order; compare with the modelled slippage. If realised > 2x modelled over 20 orders, pause the strategy and re-cost the backtest.
- Paper vs backtest divergence: `desk paper review` (z-score of paper returns vs backtest distribution).

## Scheduling
Daily-bar strategies run once per day shortly after the 00:00 UTC close (cron `aster-paper-trade` at 00:10 UTC). Never run the loop twice for the same bar; never run it from a chat session "to see what happens" in live mode.
