"""Calibrate the real effective spread for every desk symbol from aggTrades.

Run: ``uv run python -m aster.data.spread_calibration``

Writes ``research/atlas/effective-spread.csv`` and
``research/atlas/effective-spread-hourly.csv``.  Read-only with respect to the
desk: no policy, risk, execution or ledger file is touched.

The tick sizes are Binance's published ``exchangeInfo`` filters for these
symbols, hard-coded here because they are a property of the venue, not a
parameter of the estimator.  They are what make the result interpretable: an
effective spread expressed in ticks is comparable across assets, one expressed
only in bps is not.
"""

from __future__ import annotations

import os

import numpy as np
import pandas as pd

from aster.data.effective_spread import block_spreads, read_agg_trades, summarise_spread

# Binance spot tickSize per the venue's exchangeInfo.  Verified against the
# price grid of each tape: every observed price sits on a multiple of the tick.
TICK_SIZES: dict[str, float] = {
    "BTCUSDT": 0.01,
    "ETHUSDT": 0.01,
    "BNBUSDT": 0.01,
    "SOLUSDT": 0.01,
    "XRPUSDT": 0.0001,
    "DOGEUSDT": 0.00001,
}

# The aggTrades proxy must not be below a mechanically observable one-tick
# spread.  The primary statistics may be below a tick when aggressor trades
# execute at the same last price; that is a property of the proxy, not evidence
# that a market order crosses less than a tick.  The cost grid applies
# ``max(proxy, one_tick)`` before its sensitivity multiplier.

MONTH = "2024-06"  # the lightest fully pre-cutoff month for all six symbols


def calibrate(symbol: str, *, block: str = "1min") -> tuple[pd.Series, pd.Series, dict]:
    path = f"data/aggtrades/{symbol}-aggTrades-{MONTH}.zip"
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    tape = read_agg_trades(path)
    blocks = block_spreads(tape["price"], tape["ts"], side=tape["aggressor_side"],
                           block=block, symbol=symbol)
    tick_rule_blocks = block_spreads(tape["price"], tape["ts"], block=block,
                                     symbol=f"{symbol} tick-rule control")
    reference = float(tape["price"].median())
    tick = TICK_SIZES[symbol]
    stats = summarise_spread(blocks, reference_price=reference, tick_size=tick)
    control = summarise_spread(tick_rule_blocks, reference_price=reference, tick_size=tick)
    stats["tick_rule_median_bps"] = control["median_bps"]
    stats["side_method"] = "binance_is_buyer_maker"
    stats["tick_rule_ratio"] = (stats["median_bps"] / control["median_bps"]
                                if control["median_bps"] > 0 else np.nan)
    stats["symbol"] = symbol
    stats["reference_price"] = reference
    stats["tick_size"] = tick
    stats["n_trades"] = int(len(tape))
    stats["month"] = MONTH

    # Sanity: every price must sit on the tick grid, else the tick size is
    # wrong and the "ticks" column is meaningless.
    residual = np.abs(tape["price"].to_numpy() / tick - np.round(
        tape["price"].to_numpy() / tick))
    stats["max_tick_residual"] = float(residual.max())
    stats["on_grid_share"] = float((residual < 1e-6).mean())

    hourly = blocks.groupby(blocks.index.hour).median()
    hourly.name = "spread_bps"
    return blocks, hourly, stats


def main() -> int:
    rows, hourly_frames = [], []
    for symbol in TICK_SIZES:
        _, hourly, stats = calibrate(symbol)
        rows.append(stats)
        hourly_frames.append(hourly.rename(symbol))
        print(f"{symbol:9s} median {stats['median_bps']:7.3f} bps = "
              f"{stats['ticks_median']:5.2f} ticks  ({stats['n_trades']:,} trades, "
              f"grille {stats['on_grid_share'] * 100:.2f} %)")

    summary = pd.DataFrame(rows).set_index("symbol")
    summary.to_csv("research/atlas/effective-spread.csv")
    hourly_table = pd.concat(hourly_frames, axis=1).sort_index()
    hourly_table.index.name = "utc_hour"
    hourly_table.to_csv("research/atlas/effective-spread-hourly.csv")

    print("\nHourly spread, bps (real, from the trade tape):")
    print(hourly_table.round(3).to_string())
    print(f"\nEcrit research/atlas/effective-spread.csv")
    print(f"Ecrit research/atlas/effective-spread-hourly.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())