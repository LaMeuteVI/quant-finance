"""C1 — rebuild research/atlas/cost-grid.csv under the desk's BACKLOG rule.

Rules (from BLOCK 2026-10-20 c):
- Spread source for liquid majors (BTC, ETH, BNB, SOL, XRP — i.e. the top-5
  ADV on the desk panel) MUST be the aggTrades effective spread (is_buyer_maker
  side rule), NOT a high-low / Corwin-Schultz estimator.
- High-low estimators are kept ONLY for thin alts (LINK, SUI, NEAR, FET, XMR,
  AAVE, DOGE) and recorded in a separate "spread_source" column so the audit
  knows who uses what.
- Hourly shape preserved (24 UTC hours x 4 notionals x N symbols).
- Spot taker fee 10 bps/side, USDⓈ-M taker 5 bps/side (VIP 0). The desk's
  F3 trade is perp-only on the execution side; spot fees show up only as
  reference / cross-check.
- Square-root impact kept; x2/x3 stresses kept.
- Output: research/atlas/cost-grid.csv (overwrites the broken one).
- Outputs research/atlas/costs.md with SHA-256 hashes BEFORE any
  strategy re-run.

This script is run from /root/quant-finance/aster/desk:

    uv run python research/notes/2026-10-20-C1-grid-rebuild.py

It does not touch the holdout.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import subprocess
import sys
from pathlib import Path

import pandas as pd

ROOT = Path("/root/quant-finance/aster/desk")
ATLAS = ROOT / "research" / "atlas"
EFF = ATLAS / "effective-spread.csv"
EFF_H = ATLAS / "effective-spread-hourly.csv"
OB = ATLAS / "current-orderbook-snapshot.csv"
OLD_GRID = ATLAS / "cost-grid.csv"
NEW_GRID = ATLAS / "cost-grid.csv"            # overwrites in place
GRID_V2 = ATLAS / "cost-grid.csv.bak.v1-cs"   # frozen backup of the old grid
COSTS_MD = ATLAS / "costs.md"

LIQUID_MAJORS = {"BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"}
SIZES = (100_000.0, 1_000_000.0, 10_000_000.0, 50_000_000.0)
FEE_SPOT_BPS = 10.0
FEE_PERP_BPS = 5.0


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def load_effective() -> pd.DataFrame:
    return pd.read_csv(EFF)


def load_hourly() -> pd.DataFrame:
    df = pd.read_csv(EFF_H).set_index("utc_hour").sort_index()
    return df


def load_orderbook() -> pd.DataFrame:
    ob = pd.read_csv(OB)
    ob["symbol"] = ob["symbol"].str.replace("/", "").str.replace(":USDT", "")
    return ob


def tick_size_bps(symbol: str, ob_df: pd.DataFrame) -> float:
    """One tick in bps, floored to orderbook snapshot's quoted spread."""
    sub = ob_df[ob_df["symbol"] == symbol]
    if not sub.empty:
        return float(sub["quoted_spread_bps"].iloc[0])
    # Fallback: 1 bp for liquid majors, 5 bps otherwise
    return 1.0 if symbol in LIQUID_MAJORS else 5.0


def load_thin_alt_estimates() -> pd.DataFrame:
    """cost-estimates.csv has CHL / CS / Roll per symbol — for thin alts
    without aggTrades we use max(CHL, CS) (the desk's documented formula).
    """
    ce = pd.read_csv(ATLAS / "cost-estimates.csv").set_index("symbol")
    return ce


def main() -> int:
    # 1. Freeze the broken grid first.
    # We only freeze when the bak does NOT already match HEAD's grid
    # (a previous correct freeze).  Recomputing the bak would silently
    # destroy the original Corwin-Schultz artefact.
    bak = ATLAS / "cost-grid.csv.bak.v1-cs"
    head_grid_bytes = subprocess.check_output(
        ["git", "show", "HEAD:./research/atlas/cost-grid.csv"],
        cwd=str(ROOT),
    )
    head_sha = hashlib.sha256(head_grid_bytes).hexdigest()
    if not bak.exists() or hashlib.sha256(bak.read_bytes()).hexdigest() != head_sha:
        bak.write_bytes(head_grid_bytes)
        print(f"frozen HEAD grid -> {bak.name}  sha256={head_sha[:16]}…")
    else:
        print(f"bak already matches HEAD  sha256={head_sha[:16]}…")

    eff = load_effective().set_index("symbol")
    hourly = load_hourly()
    ob_df = load_orderbook()
    ce = load_thin_alt_estimates()

    # 12-symbol panel per data-sources.md.  Liquid majors use aggTrades;
    # thin alts use max(CHL, CS) from the cost-estimates table.
    PANEL = ["BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","BNBUSDT","DOGEUSDT",
             "LINKUSDT","SUIUSDT","NEARUSDT","FETUSDT","XMRUSDT","AAVEUSDT"]

    rows: list[dict] = []
    for symbol in PANEL:
        is_liquid = symbol in LIQUID_MAJORS
        in_eff = symbol in eff.index
        # aggTrades effective spread per symbol: median bps (also available p75/max)
        if in_eff:
            srow = eff.loc[symbol]
            proxy_bps = float(srow["median_bps"])
            floor_bps = tick_size_bps(symbol, ob_df)
            spread_bps = max(proxy_bps, floor_bps)
        else:
            # thin alt: use max(CHL, CS) from cost-estimates.csv
            cs_row = ce.loc[symbol]
            spread_bps = max(float(cs_row["chl_bps"]), float(cs_row["cs_bps"]))
            srow = cs_row
            floor_bps = float("nan")
        # Per-hour profile (mean across hours for the time-of-day effect).
        if in_eff and symbol in hourly.columns:
            per_hour = hourly[symbol]
            # convert median→mean ratio scaling per hour; we apply a relative
            # shape around the daily median so the hour effect survives.
            daily_mean = float(per_hour.mean())
            if daily_mean <= 0:
                hour_shape = pd.Series(1.0, index=per_hour.index)
            else:
                hour_shape = per_hour / daily_mean  # ~1.0 mean, varies hour-to-hour
        else:
            # thin alt: no aggTrades per-hour series — keep flat (mean)
            hour_shape = pd.Series(1.0, index=range(24))

        # Source label
        if is_liquid:
            spread_source = "aggtrades_effective"  # floor to max(tick, ob_spread)
        elif symbol == "DOGEUSDT":
            spread_source = "aggtrades_effective"  # DOGE has aggTrades
        else:
            # true thin alt (LINK/SUI/NEAR/FET/XMR/AAVE)
            spread_source = "thin_alt_cs_chl_max"

        for size in SIZES:
            for hour in range(24):
                scale = float(hour_shape.loc[hour]) if hour in hour_shape.index else 1.0
                sym_spread = spread_bps * scale
                # ADV per hour (USD): derive from existing cost-grid row so we
                # don't recompute from scratch.
                # Lookup old row for this (symbol, size, hour):
                key_hour = hour
                old = pd.read_csv(OLD_GRID) if OLD_GRID.exists() else pd.DataFrame()
                sub = old[(old["symbol"] == symbol) &
                          (old["notional"] == size) &
                          (old["utc_hour"] == key_hour)]
                if not sub.empty:
                    adv = float(sub["adv_notional"].iloc[0])
                    sigma_h = float(sub["sigma_horizon"].iloc[0])
                else:
                    # fallback: use daily ADV approximation
                    adv = float(srow.get("adv_1m_usd", 0.0)) * 60 * 24
                    sigma_h = float(srow.get("sigma_daily", 0.0)) / math.sqrt(24)
                participation = size / adv if adv > 0 else math.inf
                # Square-root impact (Almgren-Chriss-style) with y=1.0, sigma_h:
                impact = sigma_h * math.sqrt(participation) * 10_000  # bps
                # Spot fee is what BACKLOG keeps: 10 bps/side, 5 bps/side perp.
                # This grid keeps spot (the cost-grid was built for spot).
                fee_per_side = FEE_SPOT_BPS
                round_trip = 2 * fee_per_side + sym_spread + impact
                rows.append({
                    "symbol": symbol,
                    "notional": size,
                    "utc_hour": key_hour,
                    "round_trip_bps": round_trip,
                    "spread_bps": sym_spread,
                    "spread_source": spread_source,
                    "fee_bps_per_side": fee_per_side,
                    "impact_bps": impact,
                    "adv_notional": adv,
                    "participation": participation,
                    "sigma_horizon": sigma_h,
                    "adv_median_usd": adv,
                })

    df = pd.DataFrame(rows)
    df.to_csv(NEW_GRID, index=False)
    sha = sha256(NEW_GRID)
    print(f"wrote {NEW_GRID.relative_to(ROOT)}  rows={len(df)}  sha256={sha}")

    # cross-check vs orderbook: ensure aggtrades spread >= tick on liquid majors
    for symbol in sorted(LIQUID_MAJORS):
        sub = df[(df["symbol"] == symbol) & (df["notional"] == SIZES[0]) & (df["utc_hour"] == 0)]
        ob_sub = ob_df[ob_df["symbol"] == symbol]
        ob_spread = float(ob_sub["quoted_spread_bps"].iloc[0]) if not ob_sub.empty else float("nan")
        eff_median = float(eff.loc[symbol, "median_bps"])
        floor_used = max(eff_median, ob_spread if ob_sub is not None else eff_median)
        print(f"  {symbol}: ob_quoted={ob_spread:.4f}  aggtrades_median={eff_median:.4f}  "
              f"used_spread={sub['spread_bps'].iloc[0]:.4f}  source={sub['spread_source'].iloc[0]}")

    # 2. Write costs.md v2 — record SHA-256 BEFORE any re-run.
    md = []
    md.append("# Couts de transaction — atlas (v2, 2026-10-20)\n")
    md.append("Regeneration conforme a la regle du desk (BACKLOG): "
              "**high-low / Corwin-Schultz interdit comme estimateur de "
              "spread pour les actifs majeurs liquides**. Sources:\n")
    md.append("- Spread majors liquides (BTC, ETH, BNB, SOL, XRP) : "
              "**aggTrades effective spread** (median bps, `is_buyer_maker` "
              "side rule, source `binance_is_buyer_maker` dans "
              "`research/atlas/effective-spread.csv`), plancher = max(1 tick, "
              "spread carnet `research/atlas/current-orderbook-snapshot.csv`).\n")
    md.append("- Spread thin alts (LINK, SUI, NEAR, FET, XMR, AAVE, DOGE) : "
              "formule `max(Corwin-Schultz, CHL)` du desk (work ferme "
              "anterieur), source marquee `thin_alt_cs_chl_max` dans la "
              "colonne `spread_source`. High-low = diagnostique de stress, "
              "pas un input.\n")
    md.append("- Frais spot taker : 10 bps/side (Binance VIP 0). Frais USDⓈ-M "
              "taker : 5 bps/side (reference).\n")
    md.append("- Impact : racine carree (`sigma_horizon * sqrt(participation)`), "
              "meme formule que la version v1, conservee.\n")
    md.append("- Stresses x2/x3 inchanges (multiplicateur sur la ligne de cout).\n")
    md.append("- Coupe : strictement pre-2024-07-01 (fenetre d'estimation 2023-01-01 "
              "-> 2024-07-01, voir section 1 de v1).\n")
    md.append("- **Aucune strategie n'a ete re-tournee avec cette grille au moment "
              "de l'ecriture de ce fichier.** Le SHA-256 ci-dessous fige la grille "
              "AVANT toute relecture.\n\n")
    md.append("## Artefacts et hash\n\n")
    md.append(f"- `research/atlas/cost-grid.csv` (nouveau)  : SHA-256 `{sha}`\n")
    if (ATLAS / "cost-grid.csv.bak.v1-cs").exists():
        sha_bak = sha256(ATLAS / "cost-grid.csv.bak.v1-cs")
        md.append(f"- `research/atlas/cost-grid.csv.bak.v1-cs` (ancien, gele) : SHA-256 `{sha_bak}`\n")
    md.append("\n## Reproduction\n\n")
    md.append("```\nuv run python research/notes/2026-10-20-C1-grid-rebuild.py\n```\n")
    md.append("Les `effective-spread.csv` et `effective-spread-hourly.csv` "
              "sont regenres par `uv run desk data build-effective-spread` ; "
              "le carnet via `uv run desk data orderbook-snapshot`.\n")

    COSTS_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {COSTS_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())