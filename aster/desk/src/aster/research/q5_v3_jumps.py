"""Q5-V3 — jumps + CUSUM/SADF bubbles on BTC/ETH intraday.

Descriptive only. No ledger hypothesis, no F-hypothesis, no DSR charge.

Outputs ``research/atlas/q5_v3_jumps.json`` and the corresponding memo.
The preregistration is in ``research/notes/2026-10-19-Q5-V3-prereg.md``.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

from aster.data import r2_klines
from aster.data.r2_backtest_store import bars_from_minutes

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
SPOT_SYMBOLS = ("BTCUSDT", "ETHUSDT")
JUMP_TIMEFRAMES = ("5m", "15m", "1h", "4h")
CUSUM_TIMEFRAMES = ("1h", "4h", "1d")
SEED = 20261019
LOCAL_VOL_WINDOW = 100
JUMP_ALPHA = 0.05
JUMP_THRESH_FACTOR = 1.0  # multiplier on c_alpha
CUSUM_THRESHOLD_K = 4.0  # S > K * sqrt(n) counts as drift
SADF_CRITICAL_5PCT = -1.4  # ADF 5% critical for daily panel
ROUND_TRIP_BPS = 30.0
FDR_Q = 0.05
OUT = Path("research/atlas/q5_v3_jumps.json")


# ---------- helpers ----------

def _bh_adjust(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, dtype=float)
    n = len(p)
    order = np.argsort(p)
    ranked = p[order]
    adj = ranked * n / (np.arange(n) + 1)
    adj = np.minimum.accumulate(adj[::-1])[::-1]
    adj = np.clip(adj, 0.0, 1.0)
    out = np.empty(n, dtype=float)
    out[order] = adj
    return out


def _log_returns(bars: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    c = np.log(bars["close"].astype(float))
    r = c.diff()
    return c, r


def _lee_mykland_threshold(n: int, alpha: float) -> float:
    """Lee-Mykland (2008) jump threshold (z scale)."""
    return float(-math.log(-math.log(1.0 - alpha)) * math.sqrt(2.0 * math.log(max(n, 2))))


def _detect_jumps(returns: np.ndarray, *, vol_window: int = LOCAL_VOL_WINDOW,
                  alpha: float = JUMP_ALPHA) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return boolean jump mask, |z| stats, threshold.

    Lee-Mykland normalisation: r(t) / sqrt(realised_var_local_window).
    realised_var_local = (1/(K-1)) * sum_{j=t-K+1}^{t-1} (r(j) - mean)^2.
    We use the centered sum-of-squares around 0 over the last K-1 bars.
    """
    r = returns.copy()
    n = len(r)
    z = np.full(n, np.nan)
    is_jump = np.zeros(n, dtype=bool)
    # rolling sum-of-squares of the last `vol_window` returns
    # local_var[t] = sum_{j=t-vol_window}^{t-1} r(j)^2 / vol_window (simple var proxy)
    # Use pandas rolling
    rs = pd.Series(r)
    local_var = (rs ** 2).rolling(vol_window, min_periods=vol_window).mean().shift(1).to_numpy()
    sigma = np.sqrt(np.where(np.isfinite(local_var) & (local_var > 0), local_var, np.nan))
    with np.errstate(invalid="ignore", divide="ignore"):
        z = r / sigma
    threshold = _lee_mykland_threshold(n, alpha)
    is_jump = np.isfinite(z) & (np.abs(z) > threshold)
    return is_jump, z, threshold


def _post_jump_stats(returns: np.ndarray, jumps: np.ndarray, *, horizon: int) -> dict:
    """Forward returns after a jump, separated by sign."""
    n = len(returns)
    fwd = np.full(n, np.nan)
    # forward cumulative return from bar t+1 to t+horizon
    for i in range(n - horizon):
        if not jumps[i]:
            continue
        fwd[i] = float(np.sum(returns[i + 1: i + 1 + horizon]))
    mask = jumps
    pos = mask & (returns > 0)
    neg = mask & (returns < 0)
    # means/se
    def _se(arr: np.ndarray) -> tuple[float, float, int]:
        v = arr[np.isfinite(arr)]
        if len(v) < 5:
            return float("nan"), float("nan"), int(len(v))
        return float(np.mean(v)), float(np.std(v, ddof=1) / math.sqrt(len(v))), int(len(v))
    # split by sign of the jump itself
    sgn = np.where(returns > 0, 1.0, np.where(returns < 0, -1.0, 0.0))
    fwd_up = fwd[(sgn > 0) & mask]
    fwd_dn = fwd[(sgn < 0) & mask]
    m_up, se_up, n_up = _se(fwd_up)
    m_dn, se_dn, n_dn = _se(fwd_dn)
    t_up = m_up / se_up if se_up and se_up > 0 else float("nan")
    t_dn = m_dn / se_dn if se_dn and se_dn > 0 else float("nan")
    return {
        "horizon": horizon,
        "n_jumps_up": n_up, "mean_fwd_up": m_up, "se_fwd_up": se_up, "t_fwd_up": t_up,
        "n_jumps_down": n_dn, "mean_fwd_dn": m_dn, "se_fwd_dn": se_dn, "t_fwd_dn": t_dn,
    }


def _cusum_episodes(returns: np.ndarray, *, K: float = CUSUM_THRESHOLD_K) -> dict:
    """CUSUM chart on a return series; detect sustained drift."""
    r = returns[np.isfinite(returns)]
    n = len(r)
    if n < 50:
        return {"n": n, "episodes": [], "max_S": float("nan")}
    mu = float(np.mean(r))
    sigma = float(np.std(r, ddof=1))
    if sigma <= 0:
        return {"n": n, "episodes": [], "max_S": float("nan")}
    z = (r - mu) / sigma
    s_pos = np.zeros(n)
    s_neg = np.zeros(n)
    for i in range(1, n):
        s_pos[i] = max(0.0, s_pos[i - 1] + z[i] - K / 2.0)
        s_neg[i] = min(0.0, s_neg[i - 1] + z[i] + K / 2.0)
    thresh = K * math.sqrt(n)
    episodes = []
    in_pos = False
    start = 0
    for i, v in enumerate(s_pos):
        if not in_pos and v > thresh:
            in_pos = True
            start = i
        elif in_pos and v <= 0:
            in_pos = False
            episodes.append({"kind": "pos", "start": int(start), "end": int(i), "max_S": float(s_pos[start:i + 1].max())})
    if in_pos:
        episodes.append({"kind": "pos", "start": int(start), "end": int(n), "max_S": float(s_pos[start:].max())})
    in_neg = False
    for i, v in enumerate(s_neg):
        if not in_neg and v < -thresh:
            in_neg = True
            start = i
        elif in_neg and v >= 0:
            in_neg = False
            episodes.append({"kind": "neg", "start": int(start), "end": int(i), "max_S": float(s_neg[start:i + 1].min())})
    if in_neg:
        episodes.append({"kind": "neg", "start": int(start), "end": int(n), "max_S": float(s_neg[start:].min())})
    return {"n": n, "episodes": episodes, "max_S": float(np.nanmax(np.abs(s_pos))) if len(s_pos) else float("nan"),
            "threshold_S": float(thresh)}


def _sadf(log_price: pd.Series, *, min_frac: float = 0.05, max_frac: float = 0.95) -> dict:
    """Phillips-Shimotsu SADF on a log-price series.

    ADF regression on [r0, r1] window:
        delta_y = alpha + beta * y_{t-1} + sum gamma_i delta y_{t-i} + eps

    SADF = sup_{r0 in [min_frac, r1]} ADF_t
    Returns the sup ADF stat and the window [r0_best, r1_best].
    """
    y = log_price.to_numpy()
    n = len(y)
    if n < 200:
        return {"sadf": float("nan"), "r0_best": float("nan"), "r1_best": float("nan"), "n": n}
    dy = np.diff(y)
    # implement SADF: rolling ADF stat with OLS, very lightweight (no constant trend)
    def _adf_stat(window_dy: np.ndarray, window_y: np.ndarray) -> float:
        """ADF stat on a window.

        ``window_y`` has length ``L+1`` and ``window_dy`` has length ``L`` where
        ``window_dy[i] = window_y[i+1] - window_y[i]``. We regress
        ``window_dy[i] = alpha + beta * window_y[i] + eps`` so ``window_y`` is
        the level lagged by one step (``window_y[:-1]``).
        """
        y_lag = window_y[:-1]
        if len(y_lag) != len(window_dy) or len(y_lag) < 5:
            return float("nan")
        x = np.column_stack([np.ones_like(y_lag), y_lag])
        XtX = x.T @ x
        XtY = x.T @ window_dy
        try:
            beta = np.linalg.solve(XtX, XtY)
        except np.linalg.LinAlgError:
            return float("nan")
        resid = window_dy - x @ beta
        dof = max(len(window_dy) - x.shape[1], 1)
        sigma2 = float(resid @ resid / dof)
        try:
            cov = sigma2 * np.linalg.inv(XtX)
        except np.linalg.LinAlgError:
            return float("nan")
        se_beta = math.sqrt(cov[1, 1])
        if se_beta <= 0:
            return float("nan")
        return float(beta[1] / se_beta)

    start_min = int(min_frac * n)
    start_max = int(max_frac * n)
    best_stat = -np.inf
    best_r0, best_r1 = start_min, n
    # subsample for speed: every K-th r0 candidate (K = max(1, n//200))
    K = max(1, (start_max - start_min) // 200)
    for r1 in range(start_min + 50, n):
        for r0 in range(start_min, r1 - 20, K):
            # ADF on (y[r0:r1+1], dy[r0:r1])
            window_y = y[r0: r1 + 1]
            window_dy = dy[r0:r1]
            stat = _adf_stat(window_dy, window_y)
            if math.isfinite(stat) and stat > best_stat:
                best_stat = stat
                best_r0, best_r1 = r0, r1
    return {"sadf": float(best_stat), "r0_best": float(best_r0), "r1_best": float(best_r1), "n": n}


# ---------- entry ----------

def run() -> dict:
    out: dict = {
        "cutoff_exclusive": CUTOFF.isoformat(),
        "spot_symbols": list(SPOT_SYMBOLS),
        "jump_timeframes": list(JUMP_TIMEFRAMES),
        "cusum_timeframes": list(CUSUM_TIMEFRAMES),
        "params": {
            "local_vol_window": LOCAL_VOL_WINDOW,
            "jump_alpha": JUMP_ALPHA,
            "cusum_K": CUSUM_THRESHOLD_K,
            "sadf_critical_5pct": SADF_CRITICAL_5PCT,
            "round_trip_bps": ROUND_TRIP_BPS,
        },
    }
    flat_post_jump: list[dict] = []
    jump_stats: dict = {}
    for sym in SPOT_SYMBOLS:
        sym_block: dict = {}
        try:
            minutes = r2_klines.read_local(sym)
        except FileNotFoundError:
            sym_block["_error"] = "read_local missing"
            jump_stats[sym] = sym_block
            continue
        for tf in JUMP_TIMEFRAMES:
            try:
                bars = bars_from_minutes(minutes, tf)
            except ValueError as exc:
                sym_block[tf] = {"_error": str(exc)}
                continue
            _, r = _log_returns(bars)
            ret = r.to_numpy()
            jumps, z, thr = _detect_jumps(ret)
            n_obs = int(np.isfinite(ret).sum())
            n_jumps = int(jumps.sum())
            frac = float(n_jumps / n_obs) if n_obs else float("nan")
            post = {}
            for h in (1, 2, 5, 10):
                ph = _post_jump_stats(ret, jumps, horizon=h)
                post[h] = ph
                # flat row for BH-FDR: per (symbol, tf, horizon, side)
                flat_post_jump.append({"kind": "fwd_up", "symbol": sym, "timeframe": tf,
                                       "horizon": h, "t": ph["t_fwd_up"], "n": ph["n_jumps_up"]})
                flat_post_jump.append({"kind": "fwd_dn", "symbol": sym, "timeframe": tf,
                                       "horizon": h, "t": ph["t_fwd_dn"], "n": ph["n_jumps_down"]})
            sym_block[tf] = {
                "n_obs": n_obs,
                "n_jumps": n_jumps,
                "frac_jumps": frac,
                "threshold_z": float(thr),
                "post": post,
            }
        jump_stats[sym] = sym_block
        # CUSUM on 1h, 4h, 1d
        cusum_block: dict = {}
        for tf in CUSUM_TIMEFRAMES:
            try:
                bars = bars_from_minutes(minutes, tf)
            except ValueError as exc:
                cusum_block[tf] = {"_error": str(exc)}
                continue
            _, r = _log_returns(bars)
            cs = _cusum_episodes(r.to_numpy())
            cusum_block[tf] = cs
        # SADF on 1d
        try:
            bars = bars_from_minutes(minutes, "1d")
            _, r = _log_returns(bars)
            sadf = _sadf(np.log(bars["close"].astype(float)))
            cusum_block["sadf_1d"] = sadf
        except ValueError as exc:
            cusum_block["sadf_1d"] = {"_error": str(exc)}
        out[sym] = {"jump": sym_block, "cusum": cusum_block}
    out["jump_stats"] = jump_stats

    # ---- verdict ----
    # H1 — jumps & post-jump
    total_obs = 0
    total_jumps = 0
    bh_sig = 0
    flat = flat_post_jump
    ts = np.array([r["t"] for r in flat], dtype=float)
    ns = np.array([r["n"] for r in flat], dtype=float)
    finite = np.isfinite(ts)
    if finite.any():
        from scipy import stats as sst
        df = np.where(finite, np.maximum(ns - 2, 1), 1.0)
        p_two = 2.0 * (1.0 - sst.t.cdf(np.abs(np.where(finite, ts, 0.0)), df))
        adj = _bh_adjust(p_two)
        sig = (adj < FDR_Q) & finite
        bh_sig = int(sig.sum())
        for sym, block in jump_stats.items():
            if "_error" in block:
                continue
            for tf, cell in block.items():
                if "_error" in cell:
                    continue
                total_obs += cell["n_obs"]
                total_jumps += cell["n_jumps"]
    frac_jumps = total_jumps / total_obs if total_obs else 0.0
    h1_pass = frac_jumps >= 0.005 and bh_sig >= 1

    # H2 — CUSUM
    cusum_cells = 0
    cusum_total_episodes = 0
    cusum_pass = False
    for sym in SPOT_SYMBOLS:
        if sym not in out:
            continue
        for tf in CUSUM_TIMEFRAMES:
            cs = out[sym]["cusum"].get(tf, {})
            if "_error" in cs:
                continue
            cusum_cells += 1
            cusum_total_episodes += len(cs.get("episodes", []))
    cusum_pass = cusum_total_episodes >= max(1, cusum_cells // 2)

    # H3 — SADF
    sadf_stats = []
    for sym in SPOT_SYMBOLS:
        if sym not in out:
            continue
        s = out[sym]["cusum"].get("sadf_1d", {})
        if "_error" not in s and math.isfinite(s.get("sadf", float("nan"))):
            sadf_stats.append(s["sadf"])
    sadf_pass = any(s > SADF_CRITICAL_5PCT for s in sadf_stats) if sadf_stats else False

    out["verdict"] = {
        "n_jump_cells": len(flat) // 2,
        "n_post_jump_bh_significant": bh_sig,
        "frac_jumps_overall": frac_jumps,
        "cusum_cells": cusum_cells,
        "cusum_total_episodes": cusum_total_episodes,
        "sadf_stats": sadf_stats,
        "h1_pass": bool(h1_pass),
        "h2_pass": bool(cusum_pass),
        "h3_pass": bool(sadf_pass),
        "verdict": "RETAIN" if (h1_pass or cusum_pass or sadf_pass) else "FALSIFIED_ON_COVERAGE",
    }
    return out


def main() -> None:
    out = run()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True, default=str))
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    v = out["verdict"]
    print(f"verdict={v['verdict']} H1={v['h1_pass']} H2={v['h2_pass']} H3={v['h3_pass']}")


if __name__ == "__main__":
    main()
