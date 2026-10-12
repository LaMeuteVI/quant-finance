"""Labeling and stationary features (AFML ch. 3 and 5; skill lopez-de-prado-afml)."""

from __future__ import annotations

import numpy as np
import pandas as pd


def triple_barrier(close: pd.Series, events: pd.DatetimeIndex, vol: pd.Series, pt_mult: float = 1.0,
                   sl_mult: float = 1.0, horizon: int = 10, side: pd.Series | None = None) -> pd.DataFrame:
    """Label each event by the first barrier touched: profit-take (+1), stop (-1) or time (sign of return, or 0).

    Returns columns: t1 (label end time, needed by PurgedKFold), ret, label.
    With `side` given (primary model's direction) the labels become meta-labels {0, 1}.
    """
    out = []
    idx = close.index
    for t0 in events:
        if t0 not in idx or pd.isna(vol.get(t0)):
            continue
        i0 = idx.get_loc(t0)
        i1 = min(i0 + horizon, len(idx) - 1)
        if i1 == i0:
            continue
        s = 1.0 if side is None else float(side.get(t0, 0.0))
        if s == 0:
            continue
        path = (close.iloc[i0: i1 + 1] / close.iloc[i0] - 1) * s
        up, dn = pt_mult * vol[t0], -sl_mult * vol[t0]
        hit_up = path[path >= up].index.min() if pt_mult > 0 else pd.NaT
        hit_dn = path[path <= dn].index.min() if sl_mult > 0 else pd.NaT
        t1 = min([t for t in (hit_up, hit_dn, idx[i1]) if pd.notna(t)])
        r = float(path.loc[t1])
        if side is None:
            label = 1 if t1 == hit_up else (-1 if t1 == hit_dn else int(np.sign(r)))
        else:
            label = int(r > 0)
        out.append({"t0": t0, "t1": t1, "ret": r, "label": label})
    return pd.DataFrame(out).set_index("t0") if out else pd.DataFrame(columns=["t1", "ret", "label"])


def cusum_events(close: pd.Series, threshold: float) -> pd.DatetimeIndex:
    """Symmetric CUSUM filter: sample events when cumulative log-moves exceed threshold."""
    r = np.log(close).diff().dropna()
    events, s_pos, s_neg = [], 0.0, 0.0
    for t, x in r.items():
        s_pos, s_neg = max(0.0, s_pos + x), min(0.0, s_neg + x)
        if s_pos > threshold:
            s_pos = 0.0
            events.append(t)
        elif s_neg < -threshold:
            s_neg = 0.0
            events.append(t)
    return pd.DatetimeIndex(events)


def ffd_weights(d: float, threshold: float = 1e-4) -> np.ndarray:
    w, k = [1.0], 1
    while True:
        nxt = -w[-1] * (d - k + 1) / k
        if abs(nxt) < threshold:
            break
        w.append(nxt)
        k += 1
    return np.array(w[::-1])


def frac_diff_ffd(series: pd.Series, d: float, threshold: float = 1e-4) -> pd.Series:
    """Fixed-width fractional differentiation: stationary while keeping memory."""
    w = ffd_weights(d, threshold)
    width = len(w)
    x = series.to_numpy(dtype=float)
    out = np.full(len(x), np.nan)
    for i in range(width - 1, len(x)):
        window = x[i - width + 1: i + 1]
        if not np.isnan(window).any():
            out[i] = float(w @ window)
    return pd.Series(out, index=series.index)
