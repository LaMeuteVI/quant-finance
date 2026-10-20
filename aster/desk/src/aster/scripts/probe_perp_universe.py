"""Probe USD-M perp datasets on data.binance.vision for the pre-cutoff window.

For each (symbol, dataset) cell, returns:
  - exists: bool (HTTP 200 for at least one month in the pre-cutoff window)
  - first_month, last_month: first and last YYYY-MM with 200
  - present_months: number of months with 200 in the pre-cutoff window
  - source: probe source URL template

Honours `ASTER_OFFLINE=1` (skips HTTP and returns the empty result).
"""
from __future__ import annotations

import csv
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

# Pre-cutoff window: the strict exploration cutoff is 2024-07-01.
# We start from 2019-01 because fundingRate on Binance USD-M starts
# in late 2019 for the first perps (BTCUSDT perp launched 2019-09-25).
START_YEAR, START_MONTH = 2019, 1
CUTOFF_YEAR, CUTOFF_MONTH = 2024, 7  # exclusive

# Inventory: align with the spot R2 store. Q2 already documented that
# RENDER/ONDO/PUMP/HYPE have no pre-cutoff free data; here we probe
# only the 12 spot symbols (and known perp symbols that may differ
# from the spot listing).
PROBE_SYMBOLS = (
    "BTCUSDT", "ETHUSDT", "SOLUSDT", "AAVEUSDT", "DOGEUSDT",
    "SUIUSDT", "XRPUSDT", "BNBUSDT", "LINKUSDT", "NEARUSDT",
    "XMRUSDT", "FETUSDT",
)

DATASETS = {
    # Funding rate is a sparse 8-hour series. One CSV per month.
    "fundingRate": "https://data.binance.vision/data/futures/um/monthly/fundingRate/{sym}/{sym}-fundingRate-{ym}.zip",
    # Premium index klines: ZIPs not reliably present on the archive
    # (verified 404 on 2026-10-16). Probed here for completeness.
    "premiumIndexKlines": "https://data.binance.vision/data/futures/um/monthly/premiumIndexKlines/{sym}/1m/{sym}-premiumIndexKlines-1m-{ym}.zip",
    # Mark price klines: same.
    "markPriceKlines": "https://data.binance.vision/data/futures/um/monthly/markPriceKlines/{sym}/1m/{sym}-markPriceKlines-1m-{ym}.zip",
    # Aggregate metrics (OI, long/short ratio).
    "metrics": "https://data.binance.vision/data/futures/um/monthly/metrics/{sym}/{sym}-metrics-{ym}.zip",
    # Perp klines 1m — we record availability but do not import in this iteration
    # to keep the iteration scope small. Listed for the atlas.
    "klines_1m": "https://data.binance.vision/data/futures/um/monthly/klines/{sym}/1m/{sym}-1m-{ym}.zip",
}

HTTP_TIMEOUT = 8.0


def _month_iter(start_year: int, start_month: int, cutoff_year: int, cutoff_month: int):
    y, m = start_year, start_month
    while (y, m) < (cutoff_year, cutoff_month):
        yield y, m
        m += 1
        if m == 13:
            m = 1
            y += 1


def _head(url: str, timeout: float = HTTP_TIMEOUT) -> int:
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310
            return r.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except urllib.error.URLError:
        return 0


def probe_symbol_month(symbol: str, dataset: str, ym: str, url: str) -> int:
    """Return HTTP status for one URL. Cheap (HEAD)."""
    return _head(url.format(sym=symbol, ym=ym))


def main(argv: list[str]) -> int:
    offline = bool(os.environ.get("ASTER_OFFLINE"))
    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=["symbol", "dataset", "exists", "first_month", "last_month",
                    "present_months", "checked_months", "sample_url"],
    )
    writer.writeheader()

    if offline:
        # Offline mode: emit empty coverage rows so downstream code is
        # deterministic.
        for symbol in PROBE_SYMBOLS:
            for dataset in DATASETS:
                writer.writerow({
                    "symbol": symbol, "dataset": dataset,
                    "exists": "no", "first_month": "", "last_month": "",
                    "present_months": 0, "checked_months": 0,
                    "sample_url": DATASETS[dataset].format(sym=symbol, ym="2020-01"),
                })
        return 0

    months = [(y, m, f"{y:04d}-{m:02d}") for y, m in _month_iter(START_YEAR, START_MONTH, CUTOFF_YEAR, CUTOFF_MONTH)]

    # Restrict to a single dataset by default to keep the probe cheap:
    # full coverage of all 5 datasets × 12 symbols × ~66 months is
    # ~4000 HEAD requests. The default probe is `fundingRate`, the
    # primary input for F1/F2. Set PROBE_DATASETS=fundingRate,markPriceKlines
    # (comma-separated) to extend.
    raw = os.environ.get("PROBE_DATASETS", "fundingRate")
    selected = {k for k in (d.strip() for d in raw.split(",")) if k}
    datasets_to_run = {k: v for k, v in DATASETS.items() if k in selected}
    if not datasets_to_run:
        datasets_to_run = {"fundingRate": DATASETS["fundingRate"]}

    for symbol in PROBE_SYMBOLS:
        for dataset, url_tpl in datasets_to_run.items():
            present: list[str] = []
            sample_url = ""
            for y, m, ym in months:
                url = url_tpl.format(sym=symbol, ym=ym)
                status = probe_symbol_month(symbol, dataset, ym, url_tpl)
                if status == 200:
                    present.append(ym)
                    if not sample_url:
                        sample_url = url
            writer.writerow({
                "symbol": symbol, "dataset": dataset,
                "exists": "yes" if present else "no",
                "first_month": present[0] if present else "",
                "last_month": present[-1] if present else "",
                "present_months": len(present),
                "checked_months": len(months),
                "sample_url": sample_url,
            })
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))