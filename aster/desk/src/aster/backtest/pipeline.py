"""The research backtest pipeline. One call = one counted trial in the ledger.

dev sample:     data strictly before the sealed holdout start.
holdout sample: read once per hypothesis, after the dev gate passed.

Steps: stage checks -> data quality -> look-ahead test -> base backtest ->
stress tests -> statistics (PSR, DSR with the family's trial count, MinTRL,
haircut) -> gate vs the pre-registered prediction -> artifacts -> ledger.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from aster import paths
from aster.backtest.engine import CostModel, run_backtest
from aster.backtest.metrics import PERIODS_PER_YEAR, summary, worst_windows
from aster.data.r2_klines import CUTOFF, read_holdout as _read_holdout
from aster.data import store
from aster.data.quality import check_ohlcv
from aster.ledger.db import Ledger, LedgerError
from aster.strategies import get as get_strategy
from aster.validation.cv import sealed_split, walk_forward
from aster.validation.lookahead import check_truncation_invariance
from aster.validation.pbo import pbo_cscv
from aster.validation.stats import (deflated_sharpe, expected_max_sharpe, haircut_sharpe_bonferroni,
                                    min_track_record_length, probabilistic_sharpe)


def _gates(cfg: dict, prediction: dict) -> dict:
    g = dict(cfg.get("gates", {}))
    g.update({k: v for k, v in prediction.items() if k in g})
    return g


def _build_holdout_prices(ledger: Ledger, hypothesis_id: str, symbols: list[str],
                          *, exchange: str, timeframe: str) -> pd.DataFrame:
    """Assemble the post-cutoff close panel for a holdout backtest.

    The sealed store only carries 1-minute klines, so the function reads
    each symbol's sealed Parquet through :func:`read_holdout` (which
    atomically consumes the ledger gate) and resamples to ``timeframe``
    with the same :func:`build_bars` contract the dev path uses. The
    result is a wide close panel (UTC index x symbols), every row
    strictly at or after the exploration cutoff.

    Raises whatever :func:`read_holdout` raises: missing partitions,
    already-consumed gates, schema drift, or a sealed frame that crosses
    the cutoff. The caller is expected to have checked the dev gate.
    """
    if timeframe not in {"1d", "4h", "1h", "15m", "5m"}:
        raise ValueError(f"unsupported holdout timeframe {timeframe!r}")
    from aster.data.bars import build_bars, normalise_clock
    from aster.data.r2_backtest_store import R2_TO_PIPELINE_SYMBOL

    panels: dict[str, pd.Series] = {}
    for r2_symbol in R2_TO_PIPELINE_SYMBOL:
        pipeline_symbol = R2_TO_PIPELINE_SYMBOL[r2_symbol]
        if pipeline_symbol not in symbols:
            continue
        sealed = _read_holdout(r2_symbol, hypothesis_id=hypothesis_id, ledger=ledger)
        if sealed.empty:
            continue
        # The sealed store is 1-minute; the bar bridge resamples with the
        # same rules as the pre-cutoff side. ``label='close'`` is the only
        # research-grade label: a bar at t contains information up to t
        # and is not usable at t.
        repaired, _ = normalise_clock(sealed)
        bars = build_bars(repaired, timeframe, label="close", drop_frozen=False)
        if bars.empty:
            continue
        panels[pipeline_symbol] = bars["close"]
    if not panels:
        raise ValueError(
            f"holdout assembled no symbols: requested {symbols}, sealed store empty"
        )
    wide = pd.DataFrame(panels).sort_index()
    if wide.index.empty or wide.index.min() < CUTOFF:
        raise ValueError(
            f"holdout frame contains a pre-cutoff row ({wide.index.min() if len(wide.index) else 'n/a'})"
        )
    return wide


def _walk_forward_report(returns: pd.Series, timeframe: str) -> dict:
    """Per-fold Sharpe / drawdown / max-Loss table on the base backtest.

    Uses :func:`aster.validation.cv.walk_forward` with defaults that
    match a daily-bar strategy: 1-year train, quarterly test, one
    trading-week embargo, expanding window. The function does NOT
    refit the strategy per fold — it slices the realised returns of
    the base backtest — so the table measures the temporal stability
    of the backtested Sharpe, not the out-of-sample performance of a
    re-fitted strategy (which is the more demanding contract; that
    would require a strategy that exposes ``refit`` and the desk
    will add it as part of the F-family work).

    Returns a dict with ``n_folds``, the per-fold list of records
    (start, end, sharpe_ann, max_drawdown, n_obs) and a stability
    summary (mean / std of fold Sharpes, worst-fold Sharpe).
    """
    n = len(returns)
    train_bars, test_bars, embargo_bars = 252, 63, 5
    if n < train_bars + embargo_bars + test_bars:
        return {"n_folds": 0, "folds": [], "stability": None,
                "reason": f"need >= {train_bars + embargo_bars + test_bars} bars, got {n}"}
    folds = []
    ppy = PERIODS_PER_YEAR[timeframe]
    for _, test_idx in walk_forward(returns.index, train_bars=train_bars,
                                    test_bars=test_bars, embargo_bars=embargo_bars,
                                    expanding=True):
        if len(test_idx) < 2:
            continue
        r = returns.iloc[test_idx].dropna()
        if r.std(ddof=1) == 0 or len(r) < 2:
            continue
        sr_pp = float(r.mean() / r.std(ddof=1))
        sr_ann = float(sr_pp * np.sqrt(ppy))
        eq = (1 + r).cumprod()
        max_dd = float((eq / eq.cummax() - 1).min())
        folds.append({
            "start": str(returns.index[test_idx[0]]),
            "end": str(returns.index[test_idx[-1]]),
            "n_obs": int(len(r)),
            "sharpe_ann": sr_ann,
            "max_drawdown": max_dd,
        })
    if not folds:
        return {"n_folds": 0, "folds": [], "stability": None,
                "reason": "walk_forward produced no usable folds"}
    sharpes = np.array([f["sharpe_ann"] for f in folds])
    return {
        "n_folds": len(folds),
        "folds": folds,
        "stability": {
            "mean_sharpe_ann": float(sharpes.mean()),
            "std_sharpe_ann": float(sharpes.std(ddof=1)) if len(sharpes) > 1 else 0.0,
            "worst_fold_sharpe_ann": float(sharpes.min()),
            "best_fold_sharpe_ann": float(sharpes.max()),
        },
        "config": {"train_bars": train_bars, "test_bars": test_bars,
                   "embargo_bars": embargo_bars, "expanding": True},
    }


def _pbo_report(strat_factory, prices: pd.DataFrame, params_grid: list[dict],
                costs, timeframe: str, funding, perp_legs, AUM) -> dict:
    """PBO across a parameter sweep.

    ``strat_factory`` is a callable that takes a ``params`` dict and
    returns a strategy object (anything :func:`pipeline.run` would
    accept as the ``strategy`` argument). The function runs one
    backtest per configuration, stacks the per-bar returns into a
    wide DataFrame, and feeds it to :func:`pbo_cscv` with
    ``n_splits=16`` (the standard AFML recommendation for stable
    logits).
    """
    rets = {}
    for params in params_grid:
        strat = strat_factory(params)
        w = strat.target_weights(prices)
        result = run_backtest(prices, w, costs, lag=1, funding=funding,
                              perp_legs=perp_legs, AUM=AUM)
        rets[json.dumps(params, sort_keys=True)] = result.returns
    panel = pd.concat(rets, axis=1).dropna()
    if panel.shape[1] < 4:
        return {"pbo": None, "n_configs": panel.shape[1],
                "reason": "PBO needs >= 4 configurations; got fewer"}
    pbo = pbo_cscv(panel, n_splits=16)
    return {"pbo": pbo["pbo"], "n_configs": panel.shape[1],
            "n_splits": 16, "logit_mean": pbo["logit_mean"]}


def evaluate(prices: pd.DataFrame, weights: pd.DataFrame, costs: CostModel, timeframe: str,
             funding: pd.DataFrame | None, perp_legs=None, start: pd.Timestamp | None = None,
             AUM: float | None = None) -> dict:
    """Base + stress backtests, restricted to bars >= start (holdout) when given.

    ``perp_legs`` follows the engine contract (None, ``"all"`` or iterable).
    P2 wires it from the preregistration so that funding only hits the perp
    columns of a delta-neutral book; the legacy default ``None`` is the safe
    one for spot-only strategies that previously charged funding on every
    weight by accident.

    P4 adds the ``AUM`` argument: when provided, the engine looks up the
    per-asset, per-UTC-hour round-trip cost in the grid panel; when
    ``None``, the legacy scalar path is used (every existing test in the
    suite that calls ``evaluate`` without ``AUM`` continues to charge
    the same 10+5 bps as before).
    """
    def cut(s):
        return s if start is None else s[s.index >= start]

    base = run_backtest(prices, weights, costs, lag=1, funding=funding,
                        perp_legs=perp_legs, AUM=AUM)
    stress = {
        "costs_x2": run_backtest(prices, weights, costs.scaled(2), lag=1, funding=funding,
                                 perp_legs=perp_legs, AUM=AUM),
        "costs_x3": run_backtest(prices, weights, costs.scaled(3), lag=1, funding=funding,
                                 perp_legs=perp_legs, AUM=AUM),
        "lag_2": run_backtest(prices, weights, costs, lag=2, funding=funding,
                              perp_legs=perp_legs, AUM=AUM),
    }
    r = cut(base.returns)
    window = {"1d": 30, "4h": 180, "1h": 720, "15m": 720, "5m": 720}.get(timeframe, 30)
    return {
        "base": summary(r, timeframe, cut(base.turnover)),
        "stress": {k: summary(cut(v.returns), timeframe) for k, v in stress.items()},
        "cost_drag_ann": float(cut(base.costs).mean() * PERIODS_PER_YEAR[timeframe]),
        "funding_drag_ann": float(cut(base.funding).mean() * PERIODS_PER_YEAR[timeframe]),
        "worst_windows": worst_windows(r, window),
        "_returns": r,
    }


def run(hypothesis_id: str, strategy: str, params: dict | None = None, sample: str = "dev",
        ledger: Ledger | None = None, prices: pd.DataFrame | None = None,
        funding: pd.DataFrame | None = None, notes: str = "",
        params_grid: list[dict] | None = None) -> dict:
    cfg = paths.load_config("desk")
    ledger = ledger or Ledger()
    params = params or {}
    hyp = ledger.get(hypothesis_id)
    if not ledger.verify_prereg(hypothesis_id):
        raise LedgerError("pre-registration hash mismatch: the hypothesis was tampered with")

    # ---- P2: timeframe + universe + perp_legs come from the prereg first ----
    # The legacy config-level timeframe and universe stay as the fallback so
    # the original daily strategies keep working. A prereg may TIGHTEN the
    # universe (or move to a different horizon) but never silently widen.
    pred = hyp.get("prediction", {}) or {}
    timeframe = pred.get("timeframe") or cfg["timeframe"]
    if timeframe not in {"1d", "4h", "1h", "15m", "5m"}:
        raise ValueError(
            f"pre-registered timeframe {timeframe!r} is not supported by the bar bridge"
        )
    perp_legs = pred.get("perp_legs", None)  # None, "all" or iterable of symbols
    universe = pred.get("universe") or cfg["universe"]

    strat = get_strategy(strategy)(timeframe=timeframe, **params)
    ledger.check_revision_budget(hypothesis_id, strat.version)

    if sample == "dev" and hyp["status"] not in {"preregistered", "backtest_passed"}:
        raise LedgerError(f"dev backtests are for preregistered hypotheses (status: {hyp['status']})")

    # ---- data ---------------------------------------------------------------
    quality = {}
    symbols = list(universe)  # used by both the loader and the holdout reader
    if prices is None:
        for s in symbols:
            rep = check_ohlcv(store.read("ohlcv", cfg["exchange"], s, timeframe), timeframe)
            quality[s] = {"errors": rep.errors, "warnings": rep.warnings}
            if not rep.ok:
                raise ValueError(f"data quality errors for {s}: {rep.errors}")
        prices = store.load_closes(cfg["exchange"], symbols, timeframe)
        if perp_legs:
            # Funding panel for perp symbols. Reindexed to the weight frame
            # columns by the engine; the store loader keeps the union.
            funding = store.load_funding(cfg["exchange"], symbols, timeframe)

    holdout_start = CUTOFF  # P3: sealed cutoff, NOT holdout_frac on the pre-cutoff index
    if hyp["holdout_start"]:
        # Backwards-compatible override: an old ledger row may carry a
        # pre-P3 quantile-based holdout_start. Refuse to honour it: a
        # quantile that lies inside the pre-cutoff window is exactly the
        # leak P3 was written to close.
        configured = pd.Timestamp(hyp["holdout_start"])
        if configured < CUTOFF:
            raise LedgerError(
                f"hypothesis {hypothesis_id} carries a pre-P3 holdout_start "
                f"({configured.isoformat()}) inside the pre-cutoff window; "
                "the holdout must be the sealed store from 2024-07-01"
            )
        holdout_start = configured
    else:
        ledger.seal_holdout(hypothesis_id, holdout_start.isoformat())

    if sample == "dev":
        # The bar bridge already materialises pre-cutoff bars only. A
        # dev run therefore cannot read a single sealed row by construction.
        px = prices[prices.index < holdout_start]
        if not px.empty and px.index.max() >= holdout_start:
            # Defence in depth: the bridge invariant must hold, but if a
            # caller ever sneaks a non-pre-cutoff frame in, fail closed.
            raise ValueError(
                f"dev sample crosses the exploration cutoff "
                f"({px.index.max().isoformat()} >= {holdout_start.isoformat()})"
            )
        start = None
    elif sample == "holdout":
        # The sealed store is read exactly once per (hypothesis, symbol)
        # pair through ``consume_sealed_holdout``. The ledger gate raises
        # if the dev backtest has not passed or the pair has already been
        # consumed. This is the only way a post-cutoff row enters the
        # backtest.
        ledger.consume_holdout(hypothesis_id)   # raises if not allowed or already read
        px = _build_holdout_prices(ledger, hypothesis_id, symbols, exchange=cfg["exchange"],
                                    timeframe=timeframe)
        start = holdout_start
    else:
        raise ValueError("sample must be dev or holdout")

    # ---- look-ahead test (on what the strategy is allowed to see) ----------
    la = check_truncation_invariance(strat.target_weights, px[px.index < holdout_start])
    weights = strat.target_weights(px)

    costs = CostModel(**cfg.get("costs", {}))
    # P4: every dev backtest now reports a net-Sharpe sweep at the four
    # brief §9 sizes (100k / 1M / 10M / 50M USD) and the linearly
    # interpolated AUM at which net Sharpe first crosses 1.0.
    # The default-size evaluation (used for the gate) is run at 1M USD.
    default_aum = float(cfg.get("default_aum_usd", 1_000_000.0))
    aum_sweep = tuple(float(a) for a in cfg.get(
        "aum_sweep_usd", (100_000.0, 1_000_000.0, 10_000_000.0, 50_000_000.0)))
    ev = evaluate(px, weights, costs, timeframe, funding, perp_legs, start, AUM=default_aum)
    base = ev["base"]
    returns = ev.pop("_returns")
    sweep_results: dict = {}
    if sample == "dev":
        for aum in aum_sweep:
            ev_s = evaluate(px, weights, costs, timeframe, funding, perp_legs,
                            start, AUM=aum)
            sweep_results[f"{aum:.0f}"] = {
                "sharpe_ann_net": ev_s["base"].get("sharpe_ann"),
                "sharpe_ann_gross": None,  # gross is reported on the default run below
                "max_drawdown": ev_s["base"].get("max_drawdown"),
            }
        # Capacity = AUM at which net Sharpe first crosses 1.0, linearly
        # interpolated between sweep points. If the curve is already
        # below 1.0 at the smallest AUM the strategy is not viable.
        net_sharpe_by_aum = {aum: sweep_results[f"{aum:.0f}"]["sharpe_ann_net"]
                             for aum in aum_sweep
                             if sweep_results[f"{aum:.0f}"]["sharpe_ann_net"] is not None}
        # Lazy import to avoid a hard dependency on cost_model at module load
        from aster.backtest.cost_model import capacity_max_AUM
        capacity_usd = capacity_max_AUM(net_sharpe_by_aum, threshold=1.0)
    else:
        capacity_usd = None

    # ---- statistics ----------------------------------------------------------
    stats_out: dict = {"lookahead": la}
    psr = dsr = None
    n_family = ledger.n_trials(hyp["family"], sample) + 1
    if "sharpe_pp" in base:
        sr, n, sk, ku = base["sharpe_pp"], base["n_obs"], base["skew"], base["kurtosis"]
        psr = probabilistic_sharpe(sr, n, sk, ku)
        prior = ledger.trial_sharpes(hyp["family"], sample) + [sr]
        sr_var = float(np.var(prior, ddof=1)) if len(prior) > 1 else 0.0
        dsr = deflated_sharpe(sr, n, sk, ku, n_family, sr_var) if sample == "dev" else psr
        stats_out.update({
            "psr": psr, "dsr": dsr, "n_trials_family": n_family, "sr_variance_trials": sr_var,
            "expected_max_sr_pp": expected_max_sharpe(n_family, sr_var),
            "min_trl_bars": min_track_record_length(sr, sk, ku),
            "haircut_sharpe_ann": haircut_sharpe_bonferroni(base["sharpe_ann"], base["years"], n_family),
        })

    # ---- gate vs pre-registered prediction ----------------------------------
    g = _gates(cfg, hyp["prediction"])
    checks = {}
    if "sharpe_pp" not in base:
        checks["has_statistics"] = False
    elif sample == "dev":
        checks = {
            "lookahead_clean": la["passed"],
            "min_obs": base["n_obs"] >= g["min_obs"],
            "sharpe_ann": base["sharpe_ann"] >= g["sharpe_ann_min"],
            "max_drawdown": base["max_drawdown"] >= g["max_drawdown_floor"],
            "dsr": dsr >= g["dsr_min"],
            "stress_costs_x2": ev["stress"]["costs_x2"].get("sharpe_ann", -9) >= g["stress_sharpe_ann_min"],
            "stress_lag_2": ev["stress"]["lag_2"].get("sharpe_ann", -9) >= g["stress_sharpe_ann_min"],
        }
    else:
        hg = cfg.get("holdout_gates", {})
        checks = {
            "lookahead_clean": la["passed"],
            "sharpe_ann": base["sharpe_ann"] >= g["sharpe_ann_min"] * hg.get("sharpe_fraction_of_prediction", 0.5),
            "max_drawdown": base["max_drawdown"] >= g["max_drawdown_floor"],
            "psr": psr >= hg.get("psr_min", 0.8),
        }
    passed = bool(checks) and all(checks.values())

    # ---- artifacts -------------------------------------------------------------
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    # ---- P5: walk-forward + optional PBO across a parameter sweep -----------
    walk_forward_block: dict = {}
    pbo_block: dict = {}
    if sample == "dev" and len(returns) > 0:
        walk_forward_block = _walk_forward_report(returns, timeframe)
    if sample == "dev" and params_grid:
        def _factory(p):
            return get_strategy(strategy)(**p)
        pbo_block = _pbo_report(_factory, px, params_grid, costs, timeframe,
                                 funding, perp_legs, default_aum)

    out_dir = paths.path("backtests", hypothesis_id, f"{stamp}-{sample}-{strat.name}-v{strat.version}")
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "hypothesis_id": hypothesis_id, "sample": sample, "strategy": strat.describe(),
        "prediction": hyp["prediction"], "gates": g, "checks": checks, "passed": passed,
        "holdout_start": holdout_start.isoformat(), "period": [str(returns.index[0]), str(returns.index[-1])]
        if len(returns) else None, "costs": costs.__dict__, "data_quality": quality, **ev, "statistics": stats_out,
        "aum_sweep": sweep_results, "capacity_max_AUM_usd": capacity_usd, "default_aum_usd": default_aum,
        "walk_forward": walk_forward_block, "pbo_cscv": pbo_block,
        "notes": notes,
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2, default=str))
    returns.to_csv(out_dir / "returns.csv", header=["ret"])
    trial_id = ledger.record_trial(hypothesis_id, strat.name, strat.version, strat.params, sample, base, psr, dsr,
                                   n_family, passed, str(out_dir.relative_to(paths.desk_root())), notes)
    report["trial_id"] = trial_id
    report["artifact"] = str(out_dir)
    return report
