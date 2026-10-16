"""Q13 — dependence structure: denoised/detoned correlation, clustering, tail dependence.

Strictly pre-cutoff descriptive study. No ledger hypothesis and no holdout read.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform

from aster.data.r2_backtest_store import bars_from_minutes
from aster.data.r2_klines import read_local

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
START = pd.Timestamp("2021-01-01", tz="UTC")
SYMBOLS = ("BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT", "AAVEUSDT", "SUIUSDT", "NEARUSDT")
BOOTSTRAP_DRAWS = 1_000
SEED = 0xDADA1331
OUT = Path("research/atlas/q13_dependence.json")


def _daily_returns(symbol: str) -> pd.Series:
    minutes = read_local(symbol)
    bars = bars_from_minutes(minutes, "1d")
    close = pd.Series(bars["close"], index=bars.index, name=symbol)
    close = close.loc[(close.index >= START) & (close.index < CUTOFF)]
    return np.log(close).diff().dropna()


def _build_panel() -> pd.DataFrame:
    series = []
    for symbol in SYMBOLS:
        try:
            series.append(_daily_returns(symbol))
        except Exception as exc:  # noqa: BLE001
            series.append(pd.Series(dtype=float, name=symbol))
    panel = pd.concat(series, axis=1, join="inner").dropna(how="any")
    if panel.empty or panel.shape[1] < 4:
        raise ValueError("insufficient overlap to build the dependence panel")
    return panel


def _marcenko_pastur(eigenvalues: np.ndarray, q: float) -> float:
    n = len(eigenvalues)
    sigma2 = float(np.mean(eigenvalues))
    return sigma2 * (1.0 + 1.0 / np.sqrt(q)) ** 2


def _denoise(corr: np.ndarray, q: float) -> tuple[np.ndarray, dict]:
    eigenvalues, eigenvectors = np.linalg.eigh(corr)
    order = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]
    upper = _marcenko_pastur(eigenvalues, q)
    n = corr.shape[0]
    market = eigenvectors[:, 0] * np.sqrt(eigenvalues[0])
    detoned = corr - np.outer(market, market)
    np.fill_diagonal(detoned, 1.0)
    keep = eigenvalues > upper
    cleaned = eigenvectors[:, keep] * np.maximum(eigenvalues[keep], 0.0) @ eigenvectors[:, keep].T
    cleaned = 0.5 * (cleaned + cleaned.T)
    np.fill_diagonal(cleaned, 1.0)
    return cleaned, {"mp_upper": upper, "eigenvalues": eigenvalues.tolist(), "market_mode_norm": float(np.linalg.norm(market)), "detoned_max_offdiag": float(np.max(np.abs(detoned - np.eye(n))))}


def _angular_distance(corr: np.ndarray) -> np.ndarray:
    return np.sqrt(0.5 * (1.0 - corr)).astype(float)


def _silhouette(distance: np.ndarray, labels: np.ndarray) -> float:
    n = len(labels)
    if n < 3 or len(set(labels)) < 2: return float("nan")
    if hasattr(distance, "shape") and distance.ndim == 1:
        dmat = squareform(distance, checks=False)
    else:
        dmat = np.asarray(distance, dtype=float)
    scores = []
    for i in range(n):
        own = labels[i]
        own_idx = np.where(labels == own)[0]
        own_idx = own_idx[own_idx != i]
        a = dmat[i, own_idx].mean() if own_idx.size else 0.0
        other_means = []
        for other in set(labels):
            if other == own: continue
            other_idx = np.where(labels == other)[0]
            other_means.append(dmat[i, other_idx].mean() if other_idx.size else 1.0)
        b = min(other_means) if other_means else 1.0
        scores.append((b - a) / max(b, a, 1e-12))
    return float(np.mean(scores))


def _clusters(corr: np.ndarray) -> tuple[dict, pd.DataFrame]:
    dist = _angular_distance(corr)
    condensed = squareform(dist, checks=False)
    linkage_matrix = linkage(condensed, method="average")
    rows = []
    for k in (2, 3, 4):
        labels = fcluster(linkage_matrix, t=k, criterion="maxclust")
        rows.append({"k": k, "silhouette": _silhouette(dist, labels), "labels": [int(x) for x in labels.tolist()]})
    table = pd.DataFrame(rows).set_index("k")
    best_k = int(table["silhouette"].idxmax()) if table["silhouette"].notna().any() else 2
    chosen = table.loc[best_k, "labels"]
    chosen_list = chosen if isinstance(chosen, list) else [int(x) for x in chosen]
    return {"best_k": best_k, "by_k": {int(k): {"silhouette": float(v["silhouette"]), "labels": v["labels"]} for k, v in table.iterrows()}, "chosen_labels": chosen_list}, table.reset_index().to_dict(orient="records")


def _lower_tail(returns: pd.DataFrame, q: float = 0.1) -> dict:
    pair_rows = []
    cols = returns.columns
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            thresh_a = returns[a].quantile(q)
            thresh_b = returns[b].quantile(q)
            mask = (returns[a] <= thresh_a) & (returns[b] <= thresh_b)
            pair_rows.append({"pair": f"{a}/{b}", "joint_lower": float(mask.mean()), "n_days": int(len(returns)), "n_crashes": int(mask.sum())})
    return {"quantile": q, "pairs": pair_rows}


def _stability(panel: pd.DataFrame, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    base_labels = linkage(squareform(_angular_distance(panel.corr().values), checks=False), method="average")
    n = len(panel)
    block = 5
    counts = {}
    n_draws = 50
    for _ in range(n_draws):
        starts = rng.integers(0, n, size=int(np.ceil(n / block)))
        idx = ((starts[:, None] + np.arange(block)[None, :]) % n).ravel()[:n]
        sub_corr = panel.iloc[idx].corr().values
        sub_dist = squareform(_angular_distance(sub_corr), checks=False)
        sub_labels = fcluster(linkage(sub_dist, method="average"), t=2, criterion="maxclust")
        key = tuple(sorted(sub_labels.tolist()))
        counts[key] = counts.get(key, 0) + 1
    return {"bootstrap_draws": n_draws, "block": block, "top_allocations": sorted(counts.items(), key=lambda item: -item[1])[:3]}


def run() -> dict:
    panel = _build_panel()
    raw_corr = panel.corr().values
    t, n = panel.shape
    q = n / t
    denoised, eigen = _denoise(raw_corr, q)
    clusters, table_rows = _clusters(denoised)
    stability = _stability(panel, SEED)
    unconditional = _lower_tail(panel)
    rv = panel.rolling(60, min_periods=20).std() * np.sqrt(365)
    rv_median = rv.median(axis=1).dropna()
    threshold = float(rv.stack().median())
    high_vol = panel.loc[rv_median.index[rv_median >= threshold]]
    low_vol = panel.loc[panel.index.difference(high_vol.index).intersection(panel.index)]
    return {
        "protocol": {"cutoff_exclusive": str(CUTOFF), "start": str(START), "symbols": list(SYMBOLS), "bootstrap_draws": BOOTSTRAP_DRAWS, "seed": SEED, "status": "descriptive_only"},
        "panel": {"n_days": int(panel.shape[0]), "n_symbols": int(panel.shape[1]), "start": str(panel.index[0]), "end": str(panel.index[-1])},
        "raw_corr_max_offdiag": float(np.max(np.abs(raw_corr - np.eye(n)))),
        "denoising": {**eigen, "max_offdiag": float(np.max(np.abs(denoised - np.eye(n))))},
        "clustering": clusters,
        "clustering_table": table_rows,
        "stability": stability,
        "lower_tail_unconditional": unconditional,
        "lower_tail_by_vol": {
            "high_vol_n": int(high_vol.shape[0]),
            "low_vol_n": int(low_vol.shape[0]),
            "high_vol_top3": _lower_tail(high_vol)["pairs"][:3] if high_vol.shape[0] > 5 else [],
            "low_vol_top3": _lower_tail(low_vol)["pairs"][:3] if low_vol.shape[0] > 5 else [],
        },
        "candidate": False,
    }


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(run(), indent=2, allow_nan=False, default=float), encoding="utf-8")


if __name__ == "__main__":
    main()
