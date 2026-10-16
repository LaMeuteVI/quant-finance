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
from aster.data import store
from aster.data.quality import check_ohlcv
from aster.ledger.db import Ledger, LedgerError
from aster.strategies import get as get_strategy
from aster.validation.cv import sealed_split
from aster.validation.lookahead import check_truncation_invariance
from aster.validation.stats import (deflated_sharpe, expected_max_sharpe, haircut_sharpe_bonferroni,
                                    min_track_record_length, probabilistic_sharpe)


def _gates(cfg: dict, prediction: dict) -> dict:
    g = dict(cfg.get("gates", {}))
    g.update({k: v for k, v in prediction.items() if k in g})
    return g


def evaluate(prices: pd.DataFrame, weights: pd.DataFrame, costs: CostModel, timeframe: str,
             funding: pd.DataFrame | None, perp_legs=None, start: pd.Timestamp | None = None) -> dict:
    """Base + stress backtests, restricted to bars >= start (holdout) when given.

    ``perp_legs`` follows the engine contract (None, ``"all"`` or iterable).
    P2 wires it from the preregistration so that funding only hits the perp
    columns of a delta-neutral book; the legacy default ``None`` is the safe
    one for spot-only strategies that previously charged funding on every
    weight by accident.
    """
    def cut(s):
        return s if start is None else s[s.index >= start]

    base = run_backtest(prices, weights, costs, lag=1, funding=funding, perp_legs=perp_legs)
    stress = {
        "costs_x2": run_backtest(prices, weights, costs.scaled(2), lag=1, funding=funding, perp_legs=perp_legs),
        "costs_x3": run_backtest(prices, weights, costs.scaled(3), lag=1, funding=funding, perp_legs=perp_legs),
        "lag_2": run_backtest(prices, weights, costs, lag=2, funding=funding, perp_legs=perp_legs),
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
        funding: pd.DataFrame | None = None, notes: str = "") -> dict:
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
    if prices is None:
        symbols = list(universe)
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

    holdout_start = sealed_split(prices.index, cfg.get("holdout_frac", 0.25))
    if hyp["holdout_start"]:
        holdout_start = pd.Timestamp(hyp["holdout_start"])
    else:
        ledger.seal_holdout(hypothesis_id, holdout_start.isoformat())

    if sample == "dev":
        px = prices[prices.index < holdout_start]
        start = None
    elif sample == "holdout":
        ledger.consume_holdout(hypothesis_id)   # raises if not allowed or already read
        px, start = prices, holdout_start
    else:
        raise ValueError("sample must be dev or holdout")

    # ---- look-ahead test (on what the strategy is allowed to see) ----------
    la = check_truncation_invariance(strat.target_weights, px[px.index < holdout_start])
    weights = strat.target_weights(px)

    costs = CostModel(**cfg.get("costs", {}))
    ev = evaluate(px, weights, costs, timeframe, funding, perp_legs, start)
    base = ev["base"]
    returns = ev.pop("_returns")

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
    out_dir = paths.path("backtests", hypothesis_id, f"{stamp}-{sample}-{strat.name}-v{strat.version}")
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "hypothesis_id": hypothesis_id, "sample": sample, "strategy": strat.describe(),
        "prediction": hyp["prediction"], "gates": g, "checks": checks, "passed": passed,
        "holdout_start": holdout_start.isoformat(), "period": [str(returns.index[0]), str(returns.index[-1])]
        if len(returns) else None, "costs": costs.__dict__, "data_quality": quality, **ev, "statistics": stats_out,
        "notes": notes,
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2, default=str))
    returns.to_csv(out_dir / "returns.csv", header=["ret"])
    trial_id = ledger.record_trial(hypothesis_id, strat.name, strat.version, strat.params, sample, base, psr, dsr,
                                   n_family, passed, str(out_dir.relative_to(paths.desk_root())), notes)
    report["trial_id"] = trial_id
    report["artifact"] = str(out_dir)
    return report
