---
name: aster-crypto-alpha-map
description: Map of crypto edge families — mechanism, data, costs, pitfalls, crowding. Use when generating or triaging crypto ideas.
version: 1.0.0
metadata:
  hermes:
    tags: [crypto, alpha, market-structure, funding, momentum]
    category: quant-desk
---

# Crypto alpha map

## When to Use
Generating ideas, triaging memos, or challenging a hypothesis's mechanism. These are PRIORS to test, not validated edges. Every family below is known and partly crowded; expect decay vs published numbers.

## Families
| Family | Mechanism (who pays) | Data | Main pitfalls |
|---|---|---|---|
| Time-series trend (TSMOM) | slow diffusion, herding flows; trend followers paid for crash-risk | daily OHLCV | huge drawdowns in V-reversals; whipsaw in chop; long-only = beta in disguise (compare vs buy-and-hold BTC) |
| Cross-sectional momentum | attention/flow persistence across coins | PIT universe by volume/mcap, incl. delisted | survivorship (dead coins missing), small-cap illiquidity, sharp reversals |
| Short-term reversal | liquidity provision after overreaction | intraday bars, order book | costs eat everything; needs maker execution |
| Funding carry / basis | leveraged longs pay to hold perps | funding history, perp + spot prices | funding regime shifts; liquidation/ADL risk; exchange counterparty risk; carry crashes in selloffs |
| Funding as signal | crowded positioning predicts reversals | funding, open interest | look-ahead on settlement timestamps; noisy at single-coin level |
| Liquidation cascades | forced sellers/buyers at known levels | OI, liquidation feeds, order book | data quality varies by venue; execution in fast markets |
| Volatility risk premium (options) | option buyers overpay for crash/lottery payoff | Deribit IV surface, RV | fat-tail losses; skills `gatheral-volatility-surface`, `passarelli-option-greeks` |
| Pairs / stat-arb | temporary mispricing between related assets | prices, cointegration tests | spurious cointegration; regime breaks; skill `pairs-trading-partial-cointegration` |
| Calendar / session effects | flows tied to time (weekends, funding times, US open) | intraday bars | data mining magnet; demand a mechanism and DSR across all calendar slices tried |
| Listing / unlock events | supply shocks, predictable flows | listings, token unlock schedules | event timestamps (PIT), small samples, survivorship |
| On-chain flows | exchange inflows precede selling | on-chain providers | revisions, indexer lag, heavy look-ahead risk |

## Triage questions
1. Who is on the other side, and why do they keep paying?
2. Is it just BTC beta? Report correlation and alpha vs BTC buy-and-hold.
3. How many independent bets per year? (< 30: weak statistics)
4. Gross edge per trade vs round-trip cost?
5. Was it already tried (`desk ledger list --text`)?

## Pitfalls
- Confusing a bull-market long bias with skill (2020-21, 2023-24).
- Ignoring that crypto correlations go to 1 in crashes.
- Treating published Sharpe ratios as achievable after costs and decay.
