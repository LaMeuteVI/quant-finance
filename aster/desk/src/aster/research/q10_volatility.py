"""Q10 — per-alt N3 volatility forecast grid.

The descriptive run is deliberately fast: GARCH(1,1) is estimated once on the
fixed pre-2023 training sample, then recursively filtered for each evaluation
origin. The forecast comparison remains pseudo-OOS and strictly pre-cutoff.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from aster.data import r2_klines
from aster.research.n3_vol import (
    CUTOFF, MIN_TRAIN, TRAIN_END, _garch_params, _garch_variance,
    _har_features, _daily_close_returns, dm_hln, realized_daily,
)

SYMBOLS = ["BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT",
           "XMRUSDT", "AAVEUSDT", "FETUSDT", "NEARUSDT", "SUIUSDT"]


def _bh(pvalues: np.ndarray) -> np.ndarray:
    p = np.asarray(pvalues, dtype=float)
    out = np.full(len(p), np.nan)
    idx = np.flatnonzero(np.isfinite(p))
    order = idx[np.argsort(p[idx])]
    running = 1.0
    for rank in range(len(order), 0, -1):
        i = order[rank - 1]
        running = min(running, p[i] * len(order) / rank)
        out[i] = running
    return out


def _fit_har_vector(log_rv: pd.Series, eval_positions: np.ndarray) -> np.ndarray:
    features = _har_features(log_rv)
    target = log_rv.shift(-1)
    out = np.full(len(eval_positions), np.nan)
    for j, origin in enumerate(eval_positions):
        train = pd.concat([features, target.rename("target")], axis=1).iloc[:origin].dropna()
        if len(train) < MIN_TRAIN:
            continue
        beta = np.linalg.lstsq(train[["const", "lag1", "mean5", "mean22"]].to_numpy(),
                                train["target"].to_numpy(), rcond=None)[0]
        row = features.iloc[origin][["const", "lag1", "mean5", "mean22"]].to_numpy(float)
        if np.isfinite(row).all():
            out[j] = float(row @ beta)
    return out


def _fixed_garch_vector(returns: pd.Series, eval_positions: np.ndarray) -> np.ndarray:
    clean = returns.dropna().to_numpy(float)
    # Fixed training boundary: locate by timestamp in the original series.
    train_mask = returns.index <= TRAIN_END
    train = returns.loc[train_mask].dropna().to_numpy(float)
    out = np.full(len(eval_positions), np.nan)
    if len(train) < MIN_TRAIN:
        return out
    sample = train[-min(len(train), 1260):]
    params = _garch_params(sample)
    omega, alpha, beta = params
    last_var = max(float(np.var(sample)), 1e-12)
    last_return = sample[-1]
    # Filter sequentially over all known returns after training; predictions
    # at evaluation origins use only observations available before the target.
    eval_set = set(int(x) for x in eval_positions)
    for pos in range(len(returns)):
        if pos < len(train):
            continue
        forecast_var = omega + alpha * last_return ** 2 + beta * last_var
        if pos in eval_set:
            out[np.flatnonzero(eval_positions == pos)[0]] = np.log(max(forecast_var * 1e8, 1e-12))
        last_return = clean[pos] if pos < len(clean) else last_return
        last_var = forecast_var
    return out


def _dataset(minutes: pd.DataFrame) -> pd.DataFrame:
    data = realized_daily(minutes)
    return data.join(_daily_close_returns(minutes), how="left")


def _mean_or_none(values: np.ndarray) -> float | None:
    values = np.asarray(values, dtype=float)
    return float(np.nanmean(values)) if np.isfinite(values).any() else None


def _safe_float(value: object) -> float | None:
    return float(value) if value is not None and np.isfinite(float(value)) else None


def _inverse_leverage(data: pd.DataFrame) -> dict:
    d = data.loc[data["valid"] & data["rv"].gt(0)].copy()
    r = d["daily_return"].to_numpy(float)
    future = d["rv"].shift(-1).to_numpy(float)
    mask = np.isfinite(r) & np.isfinite(future)
    r, future = r[mask], future[mask]
    scale = np.nanmedian(np.abs(r)) if len(r) else np.nan
    band = (np.abs(r) >= .5 * scale) & (np.abs(r) <= 2 * scale) if np.isfinite(scale) else np.zeros(len(r), bool)
    pos, neg = future[band & (r > 0)], future[band & (r < 0)]
    return {"n": int(len(r)), "matched_positive_n": int(len(pos)),
            "matched_negative_n": int(len(neg)),
            "positive_mean": _safe_float(np.mean(pos)) if len(pos) else None,
            "negative_mean": _safe_float(np.mean(neg)) if len(neg) else None,
            "difference": _safe_float(np.mean(pos) - np.mean(neg)) if len(pos) and len(neg) else None}


def run() -> dict:
    forecasts = []
    inverse, dataset_meta = {}, {}
    for symbol in SYMBOLS:
        minutes = r2_klines.read_local(symbol)
        data = _dataset(minutes)
        inverse[symbol] = _inverse_leverage(data)
        dataset_meta[symbol] = {"minute_rows": int(len(minutes)), "daily_rows": int(len(data)),
                                "valid_days": int(data["valid"].sum())}
        d = data.loc[data["valid"] & data["rv"].gt(0)].copy()
        d["log_rv"] = np.log(d["rv"])
        d["daily_return"] = d["daily_return"]
        positions = np.arange(len(d) - 1)
        dates = d.index
        positions = positions[(dates[positions] > TRAIN_END) & (dates[positions + 1] < CUTOFF)]
        har = _fit_har_vector(d["log_rv"], positions)
        garch = _fixed_garch_vector(d["daily_return"], positions)
        naive = np.array([d["log_rv"].iloc[max(0, i - 29):i + 1].mean() for i in positions])
        for j, i in enumerate(positions):
            forecasts.append({"symbol": symbol, "origin": str(dates[i]), "target": str(dates[i + 1]),
                              "target_log_rv": float(d["log_rv"].iloc[i + 1]),
                              "naive_log_rv": float(naive[j]), "har_log_rv": float(har[j]),
                              "garch_log_rv": float(garch[j]) if np.isfinite(garch[j]) else None})
    f = pd.DataFrame(forecasts)
    rows = []
    for symbol in SYMBOLS:
        g = f[f.symbol == symbol]
        for loss_name, loss_fn in (("squared", lambda x: x*x), ("absolute", np.abs)):
            for first, second in (("har", "naive"), ("garch", "naive"), ("har", "garch")):
                e1 = loss_fn(g.target_log_rv - g[f"{first}_log_rv"])
                e2 = loss_fn(g.target_log_rv - g[f"{second}_log_rv"])
                diff = (e1 - e2).to_numpy(float)
                dm, p = dm_hln(diff)
                y23 = diff[pd.to_datetime(g.target).dt.year.to_numpy() == 2023]
                y24 = diff[pd.to_datetime(g.target).dt.year.to_numpy() == 2024]
                rows.append({"symbol": symbol, "loss": loss_name, "model_1": first,
                             "model_2": second, "observations": int(np.isfinite(diff).sum()),
                             "mean_loss_diff": _mean_or_none(diff), "dm_hln": _safe_float(dm),
                             "p_value": _safe_float(p), "year_2023_mean_diff": _mean_or_none(y23),
                             "year_2024_mean_diff": _mean_or_none(y24)})
    c = pd.DataFrame(rows)
    c["bh_q_value"] = _bh(c.p_value.to_numpy())
    c["bh_q_value"] = c["bh_q_value"].where(pd.notna(c["bh_q_value"]), None)
    c["bh_q05"] = c.bh_q_value.map(lambda x: bool(x < .05) if x is not None else False)
    c["sign_stable"] = ((c.year_2023_mean_diff.notna()) &
                         (c.year_2024_mean_diff.notna()) &
                         (c.year_2023_mean_diff * c.year_2024_mean_diff > 0))
    return {"cutoff_exclusive": CUTOFF.isoformat(), "train_end": TRAIN_END.isoformat(),
            "symbols": SYMBOLS, "models": ["naive_30d", "har_rv_recursive", "garch11_fixed_train"],
            "dataset": dataset_meta, "forecasts": int(len(f)), "inverse_leverage": inverse,
            "comparisons": c.where(pd.notna(c), None).to_dict(orient="records"),
            "summary": {"comparison_cells": int(len(c)), "bh_q05_cells": int(c.bh_q05.sum()),
                        "stable_bh_q05_cells": int((c.bh_q05 & c.sign_stable).sum()),
                        "har_vs_naive_bh_q05": int(((c.model_1 == "har") & (c.model_2 == "naive") & c.bh_q05).sum())}}


def _json_safe(value: object) -> object:
    if isinstance(value, float):
        return value if np.isfinite(value) else None
    if isinstance(value, dict):
        return {key: _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    return value


def main() -> None:
    out = run(); path = Path("research/atlas/q10_volatility.json")
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(json.dumps(_json_safe(out), indent=2, allow_nan=False))
    print(f"wrote {path} ({path.stat().st_size} bytes)")
    print(f"forecasts={out['forecasts']} summary={out['summary']}")

if __name__ == "__main__":
    main()
