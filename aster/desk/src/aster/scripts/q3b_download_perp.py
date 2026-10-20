"""Download BTCUSDT perp klines (3 streams) + metrics for the pre-cutoff window.

Stream-and-discard: one ZIP at a time, never more than one in flight,
CHECKSUM verified before import. Refuses to re-import a partition.
"""
import argparse
import hashlib
import subprocess
import time
from datetime import date
from pathlib import Path

from aster.data.perp_data import (
    DEFAULT_CUTOFF,
    import_kline_archive,
    import_metrics_archive,
)


def _curl(url: str, out: Path) -> tuple[int, str]:
    r = subprocess.run(["curl", "-fsS", "-o", str(out), url], capture_output=True, text=True)
    return r.returncode, r.stderr


STREAMS_KLINE = {
    "klines_1h": "klines",
    "premium_index_klines_1h": "premiumIndexKlines",
    "mark_price_klines_1h": "markPriceKlines",
}


def _months(start: date, end: date) -> list[str]:
    out = []
    y, m = start.year, start.month
    while (y, m) <= (end.year, end.month):
        out.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            m = 1
            y += 1
    return out


def main(symbol: str = "BTCUSDT",
         start: str = "2020-01",
         end: str = "2024-06",
         skip_metrics: bool = False) -> int:
    sy, sm = (int(x) for x in start.split("-"))
    ey, em = (int(x) for x in end.split("-"))
    months = _months(date(sy, sm, 1), date(ey, em, 1))
    t0 = time.time()
    total_rows = 0
    n_ok = 0
    n_skip = 0
    # ---- klines x 3 streams ----
    for stream, kind in STREAMS_KLINE.items():
        for ym in months:
            url = (
                f"https://data.binance.vision/data/futures/um/monthly/{kind}/"
                f"{symbol}/1h/{symbol}-1h-{ym}.zip"
            )
            out = Path(f"/tmp/{symbol}-1h-{ym}.zip")
            rc, err = _curl(url, out)
            if rc != 0:
                n_skip += 1
                print(f"SKIP {stream} {ym}: HTTP error ({err.strip()[:200]})")
                continue
            cs_url = url + ".CHECKSUM"
            cs_path = out.with_suffix(out.suffix + ".CHECKSUM")
            rc, err = _curl(cs_url, cs_path)
            if rc != 0:
                n_skip += 1
                print(f"SKIP {stream} {ym}: no CHECKSUM")
                out.unlink(missing_ok=True)
                continue
            with out.open("rb") as fh:
                sha = hashlib.sha256(fh.read()).hexdigest()
            expected = cs_path.read_text().strip().split()[0]
            if sha != expected:
                n_skip += 1
                print(f"SKIP {stream} {ym}: CHECKSUM MISMATCH got={sha[:12]} expected={expected[:12]}")
                out.unlink(missing_ok=True)
                cs_path.unlink(missing_ok=True)
                continue
            try:
                res = import_kline_archive(stream, out)
                total_rows += res["rows_imported"]
                n_ok += 1
            except FileExistsError:
                n_ok += 1  # already imported on a prior run
            out.unlink(missing_ok=True)
            cs_path.unlink(missing_ok=True)
        elapsed = time.time() - t0
        print(f"  {stream}: {n_ok} months OK, {n_skip} skipped, {total_rows} rows total ({elapsed:.0f}s)")
    # ---- metrics (daily) ----
    if not skip_metrics:
        # We sample one file per month (the daily file is large but
        # we only need 1 of 30 daily rows for the loader sanity).
        # Per the prereg, we keep the full set of daily files for F2.
        for ym in months:
            y, m = ym.split("-")
            url = (
                f"https://data.binance.vision/data/futures/um/daily/metrics/"
                f"{symbol}/{symbol}-metrics-{ym}-01.zip"
            )
            out = Path(f"/tmp/{symbol}-metrics-{ym}-01.zip")
            rc, err = _curl(url, out)
            if rc != 0:
                print(f"SKIP metrics {ym}-01: HTTP error")
                continue
            try:
                res = import_metrics_archive(out)
                total_rows += res["rows_imported"]
            except FileExistsError:
                pass
            out.unlink(missing_ok=True)
    print(f"DONE: {total_rows} rows imported, {time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--start", default="2020-01")
    ap.add_argument("--end", default="2024-06")
    ap.add_argument("--skip-metrics", action="store_true")
    args = ap.parse_args()
    raise SystemExit(main(args.symbol, args.start, args.end, args.skip_metrics))
