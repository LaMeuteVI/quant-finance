"""Q3c — Download perp market data for ETH and liquid alts (R2 of QUEUE 2026-10-19).

Same logic as `q3b_download_perp.py` but iterates over a list of symbols.
Pre-cutoff only (2024-07-01 exclusive). Stream-and-discard, CHECKSUM-verified.
"""
import argparse
import sys
from pathlib import Path

# Re-use the BTC implementation by importing it as a library and calling main().
from aster.scripts import q3b_download_perp as q3b


SYMBOLS_R2 = [
    # symbol, start month for downloads (YYYY-MM)
    ("ETHUSDT",  "2017-08"),  # ETH/USDT perp launched 2017-08-18
    ("BNBUSDT",  "2017-12"),
    ("SOLUSDT",  "2020-09"),
    ("XRPUSDT",  "2019-06"),
    ("DOGEUSDT", "2019-08"),
    ("LINKUSDT", "2018-12"),
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--end", default="2024-06")
    ap.add_argument("--symbols", nargs="*", default=None,
                    help="Override the R2 symbol list; each entry SYM:START")
    ap.add_argument("--skip-metrics", action="store_true")
    ap.add_argument("--only", choices={"klines_1h", "premium_index_klines_1h",
                                        "mark_price_klines_1h", "metrics"},
                    default=None,
                    help="Import only one stream (faster on a partial run)")
    args = ap.parse_args(argv)
    pairs = SYMBOLS_R2
    if args.symbols:
        pairs = []
        for spec in args.symbols:
            sym, start = spec.split(":")
            pairs.append((sym, start))
    rc = 0
    for sym, start in pairs:
        if args.only and args.only != "klines_1h":
            if args.only in ("premium_index_klines_1h", "mark_price_klines_1h"):
                # those run inside main() anyway; if only-metrics, skip klines
                pass
        print(f"\n=== {sym} from {start} to {args.end} ===", flush=True)
        r = q3b.main(symbol=sym, start=start, end=args.end,
                     skip_metrics=args.skip_metrics)
        rc = max(rc, r)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())