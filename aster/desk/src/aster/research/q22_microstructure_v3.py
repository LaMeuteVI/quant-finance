"""Q22 — Tick-data microstructure V3 (D3 GREEN).

Extends Q21 V2 with:
- multi-bar-freq support (1min, 5min, 15min) on the same observables;
- the ETH leg (free Binance Vision, 2022-01..02, streamed-and-discarded);
- the cross-asset signed-flow lead-lag at 5m and 15m.

Re-uses every primitive from `q21_microstructure`. This module only adds the
multi-bar orchestrator and the per-axis verdict.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

from aster.research import q21_microstructure as q21


# -------- Bar sizes --------

DEFAULT_BAR_FREQS = ("1min", "5min", "15min")


# -------- Per-bar-freq run --------


def run_for_bar(
    sym: str,
    bar_freq: str,
    *,
    max_rows: int = 2_000_000,
    root: Path | None = None,
) -> dict:
    """Run the full Q21 observable set for one (symbol, bar_freq)."""
    root = root or Path("/root/quant-finance/aster/desk/data/r2/market/spot/aggtrades")
    df = q21._read_btc_partitions(root / f"symbol={sym}", max_rows=max_rows)
    if df.empty:
        return {"symbol": sym, "bar_freq": bar_freq, "status": "no_data"}
    br = q21.aggregate_bars(df, bar_freq=bar_freq, max_rows=0)
    bar = br.bar
    return {
        "symbol": sym,
        "bar_freq": bar_freq,
        "n_trades": br.n_trades_total,
        "n_bars": br.n_bars,
        "kyle_lambda": q21.kyle_lambda(bar),
        "amihud": q21.amihud(bar),
        "roll_spread": q21.roll_spread(bar),
        "vpin": q21.vpin(bar),
        "predictive_signed_flow": q21.predictive_signed_flow(bar),
        "quintile_return": q21.quintile_return(bar),
    }


def run_cross(
    sym_a: str,
    sym_b: str,
    bar_freq: str,
    *,
    max_rows: int = 2_000_000,
    max_lag: int = 5,
    root: Path | None = None,
) -> dict:
    root = root or Path("/root/quant-finance/aster/desk/data/r2/market/spot/aggtrades")
    df_a = q21._read_btc_partitions(root / f"symbol={sym_a}", max_rows=max_rows)
    df_b = q21._read_btc_partitions(root / f"symbol={sym_b}", max_rows=max_rows)
    if df_a.empty or df_b.empty:
        return {"pair": f"{sym_a}-{sym_b}", "bar_freq": bar_freq, "status": "missing_data"}
    bar_a = q21.aggregate_bars(df_a, bar_freq=bar_freq, max_rows=0).bar
    bar_b = q21.aggregate_bars(df_b, bar_freq=bar_freq, max_rows=0).bar
    lag = q21.cross_asset_flow_lag(bar_a, bar_b, max_lag=max_lag)
    return {
        "pair": f"{sym_a}-{sym_b}",
        "bar_freq": bar_freq,
        "lags": lag["lags"],
        "n_intersection": lag.get("n_intersection"),
    }


# -------- Verdict --------

COST_3X_BPS_SIDE = 10.0  # 3× taker, 10 bps/side per leg, 2 sides ⇒ 6 bps/side/round-trip
COST_3X_BPS_RT = 6.0 * COST_3X_BPS_SIDE  # 60 bps round-trip


def _verdict_for(axis: dict) -> dict:
    """Verdict per axis. A candidate iff:
    1. predictive Spearman exists with the expected sign AND |ρ| > 0.05;
    2. Q4 − Q0 gross > 60 bps (3× taker hurdle);
    Else 'no candidate'."""
    psf = axis.get("predictive_signed_flow") or {}
    quint = axis.get("quintile_return") or {}
    out = {
        "spearman_signed_flow": psf.get("spearman"),
        "spearman_sign_ok": (psf.get("spearman") or 0.0) > 0.05,
        "quintile_q4_minus_q0_bps": (quint.get("quintiles") or {}).get("Q_max_minus_Q_min"),
        "above_3x_cost_hurdle": ((quint.get("quintiles") or {}).get("Q_max_minus_Q_min") or 0.0) > COST_3X_BPS_RT,
    }
    out["candidate"] = out["spearman_sign_ok"] and out["above_3x_cost_hurdle"]
    return out


# -------- Top-level --------


def run(
    *,
    bar_freqs: tuple[str, ...] = DEFAULT_BAR_FREQS,
    symbols: tuple[str, ...] = ("BTCUSDT", "ETHUSDT"),
    max_rows: int = 2_000_000,
) -> dict:
    results: dict = {"protocol": "Q22 V3 (D3 GREEN)", "axes": {}}
    for sym in symbols:
        for bf in bar_freqs:
            axis = run_for_bar(sym, bf, max_rows=max_rows)
            key = f"{sym}_{bf}"
            if axis.get("status") == "no_data":
                results["axes"][key] = axis
                continue
            axis["verdict"] = _verdict_for(axis)
            results["axes"][key] = axis
    # Cross-asset at 5m and 15m only (1m lag is dominated by 1-minute noise in Q21 V2)
    if "BTCUSDT" in symbols and "ETHUSDT" in symbols:
        for bf in ("5min", "15min"):
            xa = run_cross("BTCUSDT", "ETHUSDT", bf, max_rows=max_rows, max_lag=5)
            results["axes"][f"BTC_ETH_cross_{bf}"] = xa
    return results


def _json_safe(o):
    if isinstance(o, dict):
        return {k: _json_safe(v) for k, v in o.items() if not k.startswith("_")}
    if isinstance(o, list):
        return [_json_safe(x) for x in o]
    if isinstance(o, float) and (o != o or o in (float("inf"), float("-inf"))):
        return None
    if isinstance(o, (np.floating,)):
        f = float(o)
        return None if (f != f or f in (float("inf"), float("-inf"))) else f
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def main() -> None:
    res = run()
    safe = _json_safe(res)
    out_path = Path("research/atlas/q22_microstructure.json")
    out_path.write_text(json.dumps(safe, indent=2, default=str), encoding="utf-8")
    n_axes = len(safe.get("axes", {}))
    n_candidates = sum(1 for a in safe.get("axes", {}).values() if (a.get("verdict") or {}).get("candidate"))
    print(f"wrote {out_path}: {n_axes} axes, {n_candidates} candidates")


if __name__ == "__main__":
    main()
