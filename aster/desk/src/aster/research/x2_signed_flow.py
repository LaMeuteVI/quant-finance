"""X2 runner — intraday signed-flow as a tradeable rule, per axis.

Preregistered 2026-10-20 (research/notes/2026-10-20-X2-prereg.md).

Q22 measured the signal descriptively and rejected it against a 60 bps
hurdle its own preregistration never wrote down (the prereg says 6 bps
gross). X2 closes that gap: for each (symbol, bar size) axis it builds
the bars from the raw aggTrades, hands the panel to the real
``IntradaySignedFlow`` strategy, and prices the result through
``run_backtest`` with the C1b grid at the venue actually traded (spot,
because the aggTrades store is spot).

Four axes: {BTCUSDT, ETHUSDT} x {15min, 1h}. Per axis the runner reports
the gross quintile spread, the net result, and the arithmetic that
decides it.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

from aster.backtest.cost_model import GridCostModel
from aster.backtest.engine import run_backtest
from aster.research import q21_microstructure as q21
from aster.strategies.intraday_signed_flow import IntradaySignedFlow

ROOT = Path("/root/quant-finance/aster/desk")
AGG_ROOT = ROOT / "data/r2/market/spot/aggtrades"
GRID = ROOT / "research/atlas/cost-grid.csv"

# Bars per 15min bar, for annualising intraday returns.
BARS_PER_DAY = {"15min": 96, "1h": 24, "5min": 288, "1min": 1440}

SYMBOLS = ["BTCUSDT", "ETHUSDT"]
BAR_FREQS = ["15min", "1h"]

# Preregistered: hold 3 bars, enter on the trailing 80th/20th percentile.
HOLD_BARS = 3


def _slug(sym: str) -> str:
    return f"{sym[:-4]}-USDT"


def _round_trip(grid: GridCostModel, sym: str, notional: float) -> float:
    """Mean C1b round trip for one symbol at one notional.

    The grid is hourly; the book trades across all 24 hours, so the mean
    over the day is the honest number to compare against a bar-level
    spread.
    """
    g = grid.grid
    key = sym.replace("-", "").upper()
    sub = g[g["symbol"].astype(str).str.replace("-", "").str.upper() == key]
    if sub.empty:
        raise KeyError(f"no C1b grid rows for {sym}")
    n = sub[np.isclose(sub["notional"], notional)]
    if n.empty:
        n = sub[sub["notional"] == sub["notional"].min()]
    return float(n["round_trip_bps_spot"].mean())


def gross_quintile_spread(bar: pd.DataFrame) -> dict:
    """Q4 - Q0 gross return in bps, on the signed-flow ranking.

    This is the descriptive number Q22 reported; X2 keeps it only to show
    the strategy is trading the same effect the memo described.
    """
    work = bar[["signed_flow_imbalance", "ret_1bar"]].dropna()
    if len(work) < 100:
        return {"q4_minus_q0_bps": None, "n": int(len(work))}
    q = work["signed_flow_imbalance"].rank(pct=True, method="first")
    q4 = work.loc[q >= 0.8, "ret_1bar"]
    q0 = work.loc[q <= 0.2, "ret_1bar"]
    if len(q4) == 0 or len(q0) == 0:
        return {"q4_minus_q0_bps": None, "n": int(len(work))}
    spread_bps = float((q4.mean() - q0.mean()) * 1e4)
    return {
        "q4_minus_q0_bps": spread_bps,
        "n": int(len(work)),
        "q4_mean_bps": float(q4.mean() * 1e4),
        "q0_mean_bps": float(q0.mean() * 1e4),
    }


def spearman(signal: pd.Series, forward: pd.Series) -> float | None:
    w = pd.concat([signal, forward], axis=1).dropna()
    if len(w) < 30:
        return None
    return float(w.iloc[:, 0].corr(w.iloc[:, 1], method="spearman"))


def run_axis(sym: str, bar_freq: str, *, aum: float,
             max_rows: int = 4_000_000, grid: GridCostModel) -> dict:
    """Build one axis end to end and return its report block."""
    df = q21._read_btc_partitions(AGG_ROOT / f"symbol={sym}", max_rows=max_rows)
    if df.empty:
        return {"symbol": sym, "bar_freq": bar_freq, "status": "no_data"}
    br = q21.aggregate_bars(df, bar_freq=bar_freq, max_rows=0)
    bar = br.bar
    if bar.empty:
        return {"symbol": sym, "bar_freq": bar_freq, "status": "no_bars"}

    slug = _slug(sym)
    flow = bar[["signed_flow_imbalance"]].rename(
        columns={"signed_flow_imbalance": slug})
    px = bar[["vwap"]].rename(columns={"vwap": slug})

    strat = IntradaySignedFlow(timeframe=bar_freq, hold_bars=HOLD_BARS)
    w = strat.target_weights(px, signed_flow=flow)

    rt = _round_trip(grid, sym, aum)
    res = run_backtest(px, w, costs=grid, AUM=aum, perp_legs=[], lag=1)

    per_year = BARS_PER_DAY[bar_freq] * 365.0
    net = res.returns.dropna()
    if len(net) < 2:
        return {"symbol": sym, "bar_freq": bar_freq, "status": "too_short",
                "n_bars": int(len(net))}
    ann_ret = float(net.mean() * per_year)
    ann_vol = float(net.std(ddof=1) * math.sqrt(per_year))
    sharpe = ann_ret / ann_vol if ann_vol > 0 else None
    dd = float((1 + net).cumprod().div((1 + net).cumprod().cummax()).sub(1).min())

    trade_cost_ann = float(res.costs.fillna(0).mean() * per_year)
    gross_ann = float(res.gross_returns.dropna().mean() * per_year)

    n_invested = int((w.abs().sum(axis=1) > 0).sum())
    quint = gross_quintile_spread(bar)
    fwd = bar["ret_1bar"].shift(-HOLD_BARS)

    return {
        "symbol": sym,
        "bar_freq": bar_freq,
        "status": "ok",
        "n_bars": int(len(bar)),
        "n_trades_sampled": int(br.n_trades_total),
        "n_bars_invested": n_invested,
        "time_in_market": float(n_invested / max(len(bar), 1)),
        "annualisation_bars": per_year,
        "gross_pnl_ann": gross_ann,
        "cost_drag_ann": trade_cost_ann,
        "funding_pnl_ann": 0.0,
        "net_pnl_ann": ann_ret,
        "vol_ann": ann_vol,
        "sharpe_ann": sharpe,
        "max_drawdown": dd,
        "turnover_ann": float(res.turnover.fillna(0).mean() * per_year),
        "round_trip_bps_c1b": rt,
        "breakeven_gross_bps_per_hold": rt / HOLD_BARS,
        "quintile": quint,
        "spearman_flow_vs_forward_ret": spearman(
            bar["signed_flow_imbalance"], fwd),
    }


def verdict(axis: dict, gates: dict) -> dict:
    """Preregistered falsification: fail on any config/desk.yaml gate."""
    if axis.get("status") != "ok":
        return {"passes": False, "reason": axis.get("status")}
    checks = {
        "min_obs": axis["n_bars"] >= gates["min_obs"],
        "sharpe_ann": (axis["sharpe_ann"] is not None
                       and axis["sharpe_ann"] >= gates["sharpe_ann_min"]),
        "max_drawdown": axis["max_drawdown"] >= gates["max_drawdown_floor"],
        "net_positive": axis["net_pnl_ann"] > 0.0,
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "failed": sorted(k for k, v in checks.items() if not v),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aum", type=float, default=250_000.0)
    ap.add_argument("--max-rows", type=int, default=4_000_000)
    ap.add_argument("--out", default=str(ROOT / "research/atlas/x2_signed_flow.json"))
    args = ap.parse_args()

    import yaml
    gates = yaml.safe_load((ROOT / "config/desk.yaml").read_text())["gates"]
    grid = GridCostModel.from_csv(GRID)

    axes = []
    for sym in SYMBOLS:
        for freq in BAR_FREQS:
            ax = run_axis(sym, freq, aum=args.aum, max_rows=args.max_rows,
                          grid=grid)
            ax["verdict"] = verdict(ax, gates)
            axes.append(ax)
            print(f"{sym} {freq}: "
                  f"status={ax.get('status')} "
                  f"sharpe={ax.get('sharpe_ann')} "
                  f"net={ax.get('net_pnl_ann')} "
                  f"rt={ax.get('round_trip_bps_c1b')} "
                  f"verdict={'PASS' if ax.get('verdict',{}).get('passes') else 'FAIL'}",
                  flush=True)

    report = {
        "item": "X2",
        "prereg": "research/notes/2026-10-20-X2-prereg.md",
        "aum_usd": args.aum,
        "hold_bars": HOLD_BARS,
        "gates": gates,
        "venue": "spot (the aggTrades store is spot; charged at "
                 "round_trip_bps_spot)",
        "axes": axes,
        "any_pass": any(a.get("verdict", {}).get("passes") for a in axes),
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, default=float))
    print(f"\nwrote {out}")
    print(f"any_pass = {report['any_pass']}")


if __name__ == "__main__":
    main()
