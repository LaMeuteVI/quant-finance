"""Q7 — pre-cutoff intraday lead-lag grid.

Descriptive only: raw and BTC/ETH-residualised return correlations for
all directed pairs in the materialised five-asset panel. No ledger writes,
backtests, or holdout access occur here.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.data import store
from aster.data.r2_klines import CUTOFF

SYMBOLS = ("BTC/USDT", "ETH/USDT", "SOL/USDT", "BNB/USDT", "XRP/USDT")
TIMEFRAMES = ("5m", "15m", "1h", "4h")
LAGS = (1, 2, 5, 15)
BLOCK = 24
N_BOOT = 100


def _stable_seed(*parts: object) -> int:
    digest = hashlib.sha256("|".join(map(str, parts)).encode()).digest()
    return int.from_bytes(digest[:4], "little")


def _corr(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) < 20 or np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def _block_bootstrap_ci(x: np.ndarray, y: np.ndarray, *, seed: int) -> tuple[float, float]:
    """Moving-block bootstrap CI for correlation, deterministic by seed."""
    n = min(len(x), len(y))
    n_blocks = n // BLOCK
    if n_blocks < 10:
        return float("nan"), float("nan")
    x = x[: n_blocks * BLOCK].reshape(n_blocks, BLOCK)
    y = y[: n_blocks * BLOCK].reshape(n_blocks, BLOCK)
    rng = np.random.default_rng(seed)
    values = np.empty(N_BOOT, dtype=float)
    for b in range(N_BOOT):
        idx = rng.integers(0, n_blocks, size=n_blocks)
        xb = x[idx].reshape(-1)
        yb = y[idx].reshape(-1)
        values[b] = _corr(xb, yb)
    return float(np.nanquantile(values, 0.025)), float(np.nanquantile(values, 0.975))


def _bh_qvalues(pvalues: np.ndarray) -> np.ndarray:
    """Benjamini-Hochberg q-values, NaN-safe."""
    out = np.full(len(pvalues), np.nan, dtype=float)
    finite = np.isfinite(pvalues)
    vals = pvalues[finite]
    if not len(vals):
        return out
    order = np.argsort(vals)
    ranked = vals[order]
    q = ranked * len(ranked) / np.arange(1, len(ranked) + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    restored = np.empty(len(vals), dtype=float)
    restored[order] = np.minimum(q, 1.0)
    out[finite] = restored
    return out


def _pvalue_corr(r: float, n: int) -> float:
    if not np.isfinite(r) or n < 4 or abs(r) >= 1:
        return 0.0 if abs(r) >= 1 else float("nan")
    t = r * np.sqrt((n - 2) / max(1e-15, 1 - r * r))
    return float(2 * stats.t.sf(abs(t), n - 2))


def _residualise(panel: pd.DataFrame) -> pd.DataFrame:
    """Residualise alt returns on contemporaneous BTC/ETH controls.

    The controls remain as observable leader series. Residualising BTC/ETH
    themselves would create zero columns and a mechanically meaningless grid.
    """
    controls = panel[["BTC/USDT", "ETH/USDT"]].to_numpy()
    design = np.column_stack([np.ones(len(panel)), controls])
    out: dict[str, np.ndarray] = {}
    for col in panel.columns:
        y = panel[col].to_numpy()
        if col in {"BTC/USDT", "ETH/USDT"}:
            out[col] = y
            continue
        beta, *_ = np.linalg.lstsq(design, y, rcond=None)
        out[col] = y - design @ beta
    return pd.DataFrame(out, index=panel.index)


def _panel(symbols: tuple[str, ...], timeframe: str) -> pd.DataFrame:
    closes = {}
    for symbol in symbols:
        frame = store.read("ohlcv", "binance", symbol, timeframe)
        series = frame["close"].copy()
        series.index = pd.to_datetime(series.index, utc=True)
        closes[symbol] = series[series.index < CUTOFF]
    close = pd.DataFrame(closes).sort_index()
    returns = close.pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan)
    return returns.dropna(how="any")


def _cost_hurdle_bps(follower: str) -> float:
    """Optimistic lower bound of 100k-USDT round-trip cost across UTC hours."""
    path = Path("research/atlas/cost-grid.csv")
    if not path.exists():
        return float("nan")
    table = pd.read_csv(path)
    rows = table[(table["symbol"] == follower.replace("/", "")) & (table["notional"] == 100_000.0)]
    return float(rows["round_trip_bps"].min()) if len(rows) else float("nan")


def _half_year_sign_consistent(index: pd.Index, x: np.ndarray, y: np.ndarray) -> bool:
    """Whether non-zero half-year correlations share one sign."""
    dt_index = pd.to_datetime(index, utc=True, errors="coerce")
    if not isinstance(dt_index, pd.DatetimeIndex) or dt_index.isna().all():
        # Unit-test panels may have no calendar index; do not claim stability.
        return False
    dt_values = np.asarray(dt_index)
    labels = np.array([ts.year * 2 + int(ts.month > 6) for ts in dt_values])
    signs: list[float] = []
    for label in np.unique(labels):
        mask = labels == label
        r = _corr(x[mask], y[mask])
        if np.isfinite(r) and abs(r) > 0:
            signs.append(float(np.sign(r)))
    return len(signs) >= 2 and len(set(signs)) == 1


def _grid(panel: pd.DataFrame, *, timeframe: str, residual: bool) -> pd.DataFrame:
    data = _residualise(panel) if residual else panel
    rows: list[dict] = []
    for leader in data.columns:
        for follower in data.columns:
            if leader == follower:
                continue
            for lag in LAGS:
                x0 = data[leader].to_numpy()[:-lag]
                y0 = data[follower].to_numpy()[lag:]
                idx0 = data.index[lag:]
                mask = np.isfinite(x0) & np.isfinite(y0)
                x, y, idx = x0[mask], y0[mask], idx0[mask]
                r = _corr(x, y)
                p = _pvalue_corr(r, len(x))
                lo, hi = _block_bootstrap_ci(
                    x, y, seed=_stable_seed(timeframe, residual, leader, follower, lag)
                )
                rows.append({
                    "timeframe": timeframe,
                    "leader": leader,
                    "follower": follower,
                    "lag_bars": lag,
                    "residual": residual,
                    "n_obs": int(len(x)),
                    "corr": r,
                    "p_value": p,
                    "bootstrap_lo": lo,
                    "bootstrap_hi": hi,
                    "effect_bps": float(10_000 * r * np.std(y)) if len(y) else float("nan"),
                    "half_year_sign_consistent": _half_year_sign_consistent(idx, x, y),
                    "cost_hurdle_bps": _cost_hurdle_bps(follower),
                })
    return pd.DataFrame(rows)


def run() -> dict:
    frames: list[pd.DataFrame] = []
    for timeframe in TIMEFRAMES:
        panel = _panel(SYMBOLS, timeframe)
        raw = _grid(panel, timeframe=timeframe, residual=False)
        residual = _grid(panel, timeframe=timeframe, residual=True)
        frames.extend([raw, residual])
    grid = pd.concat(frames, ignore_index=True)
    grid["bh_q_value"] = _bh_qvalues(grid["p_value"].to_numpy())
    grid["survives_bh_q05"] = grid["bh_q_value"] < 0.05
    grid["bootstrap_excludes_zero"] = (
        (grid["bootstrap_lo"] > 0) | (grid["bootstrap_hi"] < 0)
    )
    grid["joint_survivor"] = grid["survives_bh_q05"] & grid["bootstrap_excludes_zero"]
    return {
        "cutoff_exclusive": CUTOFF.isoformat(),
        "symbols": list(SYMBOLS),
        "timeframes": list(TIMEFRAMES),
        "lags_bars": list(LAGS),
        "block_bars": BLOCK,
        "bootstrap_draws": N_BOOT,
        "n_cells": int(len(grid)),
        "n_joint_survivors": int(grid["joint_survivor"].sum()),
        "n_residual_joint_survivors": int(grid.loc[grid["residual"], "joint_survivor"].sum()),
        "grid": grid.to_dict(orient="records"),
    }


def main() -> None:
    out = run()
    path = Path("research/atlas/q7_intraday_leadlag.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True, allow_nan=False))
    print(f"wrote {path} ({path.stat().st_size} bytes)")
    print(f"cells={out['n_cells']} joint_survivors={out['n_joint_survivors']} residual={out['n_residual_joint_survivors']}")


if __name__ == "__main__":
    main()
