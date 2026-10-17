"""ETH N2 descriptive return dependence, using the fixed BTC N2 design."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from aster.data import store
from aster.research.btc_n2 import CUTOFF, DEV_END, HORIZONS, SEED, BOOTSTRAPS, analyse

SYMBOL = "ETH/USDT"
OUTPUT_CSV = Path("research/assets/2026-10-14-eth-n2.csv")
OUTPUT_MD = Path("research/assets/2026-10-14-eth-n2.md")


def main() -> int:
    prices = store.read("ohlcv", "binance", SYMBOL, "1d")["close"]
    result = analyse(prices)
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT_CSV, index=False)
    manifest = store.manifest("ohlcv", "binance", SYMBOL, "1d")
    survivors = result[result["fdr_survives_q05"] & result["bootstrap_excludes_zero"]]
    lines = [
        "# ETH N2 — descriptive return dependence",
        "",
        "**Status: descriptive only; no strategy validation or holdout read.**",
        "",
        f"- Dataset manifest SHA-256: `{manifest['sha256']}`.",
        f"- Development boundary: `{DEV_END.isoformat()}`; exploration cutoff: `{CUTOFF.isoformat()}`.",
        f"- Horizons: `{list(HORIZONS)}`; moving-block bootstrap: `{BOOTSTRAPS}`; seed: `{SEED}`.",
        "- BH-FDR is applied across the six primary tests. Overlapping returns make p-values diagnostic, not independent evidence.",
        "",
        "## Results",
        "",
        result.to_string(index=False),
        "",
        f"Joint bootstrap/FDR survivors: `{len(survivors)}`.",
        "",
        "A descriptive relationship is not a tradable edge. Any candidate requires a new ledger preregistration and a counted desk backtest.",
    ]
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT_CSV}")
    print(f"wrote {OUTPUT_MD}")
    print(f"joint_survivors={len(survivors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
