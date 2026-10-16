"""Probe RENDER, ONDO, PUMP, HYPE for pre-cutoff data in our free channels.

Outputs CSV to stdout. No record values are emitted, only keys and HTTP statuses.
Honours `ASTER_OFFLINE=1` (returns local-only results without network I/O).
"""
from __future__ import annotations

import csv
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Symbols added by BRIEF.md §2 that are NOT in the existing pre-cutoff R2 store.
# HYPE is a USDⓈ-M perp, not spot; Q3 handles its channel. We probe it here
# only to record the absence uniformly.
PROBE_SYMBOLS = ("RENDERUSDT", "ONDOUSDT", "PUMPUSDT", "HYPEUSDT")

VISION_SPOT = "https://data.binance.vision/data/spot/monthly/klines/{sym}/1m/"
VISION_UM = "https://data.binance.vision/data/futures/um/monthly/klines/{sym}/1m/"


def _local_r2_paths(desk_root: Path, symbol: str) -> list[Path]:
    base = desk_root / "data" / "r2" / "market" / "spot" / "klines_1m" / f"symbol={symbol}"
    return sorted(base.rglob("*.parquet")) if base.is_dir() else []


def _vision_exists(url: str, timeout: float = 10.0) -> tuple[bool, str]:
    """Return (exists, error). `exists=True` if S3 returns a non-empty listing."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:  # noqa: S310
            body = response.read(200_000).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return False, f"http_{exc.code}"
    except urllib.error.URLError as exc:
        return False, f"url_error:{exc.reason}"
    if "<Error>" in body or "NoSuchKey" in body:
        return False, "no_such_key"
    # Listing contains keys like "<SYM>-1m-YYYY-MM.zip" (spot) or "<SYM>-1m-YYYY-MM.zip" (um).
    import re
    return (re.search(r"[A-Z]+USDT-1m-\d{4}-\d{2}\.zip", body) is not None), "listed"


def probe(desk_root: Path, offline: bool) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for symbol in PROBE_SYMBOLS:
        local_paths = _local_r2_paths(desk_root, symbol)
        rows.append({
            "symbol": symbol, "channel": "local-r2-spot",
            "exists": "yes" if local_paths else "no",
            "sample_key": local_paths[0].relative_to(desk_root).as_posix() if local_paths else "",
            "error": "",
        })
        if offline:
            spot_exists, spot_err = (False, "offline")
            um_exists, um_err = (False, "offline")
        else:
            spot_exists, spot_err = _vision_exists(VISION_SPOT.format(sym=symbol))
            um_exists, um_err = _vision_exists(VISION_UM.format(sym=symbol))
        rows.append({
            "symbol": symbol, "channel": "data.binance.vision-spot",
            "exists": "yes" if spot_exists else "no",
            "sample_key": "", "error": spot_err,
        })
        rows.append({
            "symbol": symbol, "channel": "data.binance.vision-um",
            "exists": "yes" if um_exists else "no",
            "sample_key": "", "error": um_err,
        })
    return rows


def main(argv: list[str]) -> int:
    desk_root = Path(os.environ.get("ASTER_DESK") or Path.cwd()).resolve()
    offline = bool(os.environ.get("ASTER_OFFLINE"))
    writer = csv.DictWriter(sys.stdout, fieldnames=["symbol", "channel", "exists", "sample_key", "error"])
    writer.writeheader()
    writer.writerows(probe(desk_root, offline))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))