"""Q8 — descriptive funding-rate persistence and carry.

This module reads only the local pre-cutoff Q3 funding-rate store.  It does
not read the sealed store, register ledger hypotheses, or run a backtest.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.data.r2_klines import CUTOFF

SYMBOLS = (
    "BTCUSDT", "ETHUSDT", "SOLUSDT", "AAVEUSDT", "DOGEUSDT", "SUIUSDT",
    "XRPUSDT", "BNBUSDT", "LINKUSDT", "NEARUSDT", "XMRUSDT", "FETUSDT",
)
FIXING_HOURS = (0, 8, 16)
LAGS = (1, 3, 7)
BLOCK = 24
N_BOOT = 200


def _read_funding_panel(root: Path, symbols: tuple[str, ...] = SYMBOLS) -> pd.DataFrame:
    """Load one funding-rate column per symbol, enforcing the cutoff."""
    frames: dict[str, pd.Series] = {}
    for symbol in symbols:
        files = sorted((root / f"symbol={symbol}").glob("year=*/month=*/part-0.parquet"))
        pieces: list[pd.Series] = []
        for path in files:
            frame = pd.read_parquet(path)
            index = pd.to_datetime(frame.index, utc=True)
            values = pd.to_numeric(frame["last_funding_rate"], errors="raise")
            piece = pd.Series(values.to_numpy(), index=index, name=symbol)
            pieces.append(piece[piece.index < CUTOFF])
        if pieces:
            series = pd.concat(pieces).sort_index()
            frames[symbol] = series[~series.index.duplicated(keep="last")]
    if not frames:
        raise FileNotFoundError(f"no funding partitions under {root}")
    return pd.DataFrame(frames).sort_index()


def _fixings(panel: pd.DataFrame) -> pd.DataFrame:
    """Keep the three Binance funding fixing hours and align to a grid."""
    idx = panel.index
    mask = (idx.minute == 0) & (idx.second == 0) & idx.hour.isin(FIXING_HOURS)
    out = panel.loc[mask].copy()
    out.index = out.index.floor("8h")
    out = out.groupby(level=0).last().sort_index()
    return out[out.index < CUTOFF]


def _autocorr(values: np.ndarray, lag: int) -> float:
    if len(values) <= lag + 10:
        return float("nan")
    x, y = values[:-lag], values[lag:]
    mask = np.isfinite(x) & np.isfinite(y)
    if mask.sum() < 20 or np.std(x[mask]) == 0 or np.std(y[mask]) == 0:
        return float("nan")
    return float(np.corrcoef(x[mask], y[mask])[0, 1])


def _block_mean_ci(values: np.ndarray, *, seed: int) -> tuple[float, float]:
    """Moving-block bootstrap CI for a mean, with deterministic draws."""
    values = values[np.isfinite(values)]
    n_blocks = len(values) // BLOCK
    if n_blocks < 4:
        return float("nan"), float("nan")
    blocks = values[: n_blocks * BLOCK].reshape(n_blocks, BLOCK)
    rng = np.random.default_rng(seed)
    means = np.empty(N_BOOT)
    for i in range(N_BOOT):
        means[i] = blocks[rng.integers(0, n_blocks, size=n_blocks)].mean()
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def _conditional_spread(values: np.ndarray, *, horizon: int = 1, seed: int) -> dict:
    """High-minus-low spread in funding ``horizon`` fixings ahead."""
    if horizon < 1:
        raise ValueError("horizon must be positive")
    current = values[:-horizon]
    future = values[horizon:]
    mask = np.isfinite(current) & np.isfinite(future)
    current, future = current[mask], future[mask]
    if len(current) < 40:
        return {"n_obs": int(len(current)), "high_next": float("nan"),
                "low_next": float("nan"), "spread": float("nan"),
                "ci_lo": float("nan"), "ci_hi": float("nan")}
    lo, hi = np.quantile(current, [0.2, 0.8])
    high = future[current >= hi]
    low = future[current <= lo]
    spread = float(high.mean() - low.mean())
    # Bootstrap paired blocks of (current, future), preserving the label rule.
    pairs = np.column_stack([current, future])
    n_blocks = len(pairs) // BLOCK
    blocks = pairs[: n_blocks * BLOCK].reshape(n_blocks, BLOCK, 2)
    rng = np.random.default_rng(seed)
    draws = np.empty(N_BOOT)
    for i in range(N_BOOT):
        sample = blocks[rng.integers(0, n_blocks, size=n_blocks)].reshape(-1, 2)
        q_lo, q_hi = np.quantile(sample[:, 0], [0.2, 0.8])
        draws[i] = sample[sample[:, 0] >= q_hi, 1].mean() - sample[sample[:, 0] <= q_lo, 1].mean()
    return {
        "n_obs": int(len(current)),
        "high_next": float(high.mean()),
        "low_next": float(low.mean()),
        "spread": spread,
        "spread_bps": spread * 10_000.0,
        "ci_lo": float(np.quantile(draws, 0.025)),
        "ci_hi": float(np.quantile(draws, 0.975)),
        "bootstrap_p_value": float(min(1.0, 2.0 * min(np.mean(draws <= 0), np.mean(draws >= 0)))),
    }


def _pvalue_mean(values: np.ndarray) -> float:
    values = values[np.isfinite(values)]
    if len(values) < 10 or np.std(values, ddof=1) == 0:
        return float("nan")
    return float(2.0 * stats.t.sf(abs(np.mean(values) / (np.std(values, ddof=1) / np.sqrt(len(values)))), len(values) - 1))


def _bh_qvalues(pvalues: np.ndarray) -> np.ndarray:
    out = np.full(len(pvalues), np.nan)
    finite = np.isfinite(pvalues)
    vals = pvalues[finite]
    if not len(vals):
        return out
    order = np.argsort(vals)
    ranked = vals[order]
    q = ranked * len(ranked) / np.arange(1, len(ranked) + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    restored = np.empty(len(vals))
    restored[order] = np.minimum(q, 1.0)
    out[finite] = restored
    return out


def _cross_sectional_stats(fixings: pd.DataFrame) -> dict:
    """Cross-sectional dispersion and rank persistence across fixing times."""
    dispersion = fixings.std(axis=1, skipna=True)
    rank_corr: list[float] = []
    for lag in (1, 3, 7):
        pairs: list[float] = []
        for i in range(lag, len(fixings)):
            a, b = fixings.iloc[i - lag], fixings.iloc[i]
            valid = a.notna() & b.notna()
            if valid.sum() >= 5:
                pairs.append(float(a[valid].rank().corr(b[valid].rank())))
        rank_corr.append(float(np.nanmean(pairs)) if pairs else float("nan"))
    return {
        "mean_dispersion": float(dispersion.mean()),
        "median_dispersion": float(dispersion.median()),
        "rank_persistence": {f"lag{lag}": value for lag, value in zip((1, 3, 7), rank_corr)},
        "n_fixings": int(len(fixings)),
    }


def analyse(panel: pd.DataFrame) -> dict:
    """Return the complete preregistered Q8 descriptive result."""
    fixings = _fixings(panel)
    by_symbol: dict[str, dict] = {}
    conditional_rows: list[dict] = []
    for symbol in fixings.columns:
        values = fixings[symbol].dropna().to_numpy(dtype=float)
        p_mean = _pvalue_mean(values)
        row = {
            "n_obs": int(len(values)),
            "start": str(fixings[symbol].dropna().index[0]) if len(values) else None,
            "end": str(fixings[symbol].dropna().index[-1]) if len(values) else None,
            "mean_rate": float(np.mean(values)) if len(values) else float("nan"),
            "median_rate": float(np.median(values)) if len(values) else float("nan"),
            "std_rate": float(np.std(values, ddof=1)) if len(values) > 1 else float("nan"),
            "positive_fraction": float(np.mean(values > 0)) if len(values) else float("nan"),
            "annualised_simple": float(np.mean(values) * 3 * 365) if len(values) else float("nan"),
            "p_value_mean": p_mean,
            "autocorr": {f"lag{lag}": _autocorr(values, lag) for lag in LAGS},
        }
        by_symbol[symbol] = row
        for lag in LAGS:
            if len(values) > lag:
                spread = _conditional_spread(values, horizon=lag, seed=int.from_bytes(hashlib.sha256(f"{symbol}|{lag}".encode()).digest()[:4], "little"))
                spread.update({"symbol": symbol, "lag_fixings": lag})
                conditional_rows.append(spread)
    conditional = pd.DataFrame(conditional_rows)
    if not conditional.empty:
        conditional["p_value"] = conditional["bootstrap_p_value"]
        conditional["bh_q_value"] = _bh_qvalues(conditional["p_value"].to_numpy())
        conditional["joint_survivor"] = (
            (conditional["ci_lo"] > 0) | (conditional["ci_hi"] < 0)
        )
    def _json_safe(value):
        if isinstance(value, float) and not np.isfinite(value):
            return None
        return value
    panel_json = json.loads(json.dumps(by_symbol, default=_json_safe, allow_nan=False))
    conditional_json = json.loads(json.dumps(conditional.to_dict(orient="records"), default=_json_safe, allow_nan=False))
    return {
        "cutoff_exclusive": CUTOFF.isoformat(),
        "symbols": list(fixings.columns),
        "fixing_hours_utc": list(FIXING_HOURS),
        "lags_fixings": list(LAGS),
        "block_fixings": BLOCK,
        "bootstrap_draws": N_BOOT,
        "panel": panel_json,
        "cross_sectional": _cross_sectional_stats(fixings),
        "conditional_quintile": conditional_json,
    }


def main() -> None:
    root = Path("data/r2/market/futures/um/funding_rate")
    panel = _read_funding_panel(root)
    result = analyse(panel)
    path = Path("research/atlas/q8_funding_carry.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    print(f"wrote {path} ({path.stat().st_size} bytes)")
    print(f"symbols={len(result['symbols'])} fixings={result['cross_sectional']['n_fixings']} conditional_cells={len(result['conditional_quintile'])}")


if __name__ == "__main__":
    main()
