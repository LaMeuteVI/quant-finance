"""`desk` command line: the desk's single entry point for agent and human.

Human-only commands (promote, kill off) refuse to run inside an agent process
or without an interactive terminal.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from aster import paths


def _print(obj) -> None:
    print(json.dumps(obj, indent=2, default=str, ensure_ascii=False))


def _human_gate(what: str, token: str) -> str:
    if os.environ.get("HERMES_HOME") or os.environ.get("HERMES_REAL_HOME") or os.environ.get("ASTER_AGENT"):
        sys.exit(f"refused: '{what}' is a human-only action and cannot run inside an agent session")
    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        sys.exit(f"refused: '{what}' needs an interactive terminal")
    name = input("Your name (recorded in the ledger): ").strip()
    typed = input(f"Type '{token}' to confirm {what}: ").strip()
    if not name or typed != token:
        sys.exit("aborted")
    return name


# ---- init / data -------------------------------------------------------------
def cmd_init(a) -> None:
    from aster.ledger.db import Ledger

    paths.ensure_dirs()
    Ledger()
    _print({"desk": str(paths.desk_root()), "ledger": str(paths.ledger_path())})


def cmd_data_fetch(a) -> None:
    from aster.data import ccxt_source, store

    cfg = paths.load_config("desk")
    ex_id = a.exchange or cfg["exchange"]
    tf = a.timeframe or cfg["timeframe"]
    symbols = a.symbols.split(",") if a.symbols else cfg["universe"]
    ex = ccxt_source.make_exchange(ex_id)
    out = {}
    for s in symbols:
        df = ccxt_source.fetch_ohlcv(ex, s, tf, since=a.since or cfg.get("history_start"))
        store.write(df, "ohlcv", ex_id, s, tf, source=f"ccxt:{ex_id}")
        out[s] = {"rows": len(df), "start": str(df.index[0]) if len(df) else None,
                  "end": str(df.index[-1]) if len(df) else None}
    if a.funding:
        perp_ex = ccxt_source.make_exchange(cfg.get("perp_exchange", ex_id))
        for s in symbols:
            perp = cfg.get("perp_symbols", {}).get(s)
            if not perp:
                continue
            f = ccxt_source.fetch_funding(perp_ex, perp, since=a.since or cfg.get("history_start"))
            if f.empty:
                continue
            f = f.resample(tf).sum()   # funding paid per bar
            store.write(f, "funding", ex_id, s, tf, source=f"ccxt:{cfg.get('perp_exchange', ex_id)}:{perp}")
            out[s]["funding_rows"] = len(f)
    _print(out)


def cmd_data_check(a) -> None:
    from aster.data import store
    from aster.data.quality import check_ohlcv

    cfg = paths.load_config("desk")
    res = {}
    for s in cfg["universe"]:
        try:
            df = store.read("ohlcv", cfg["exchange"], s, cfg["timeframe"])
        except FileNotFoundError as e:
            res[s] = {"errors": [str(e)]}
            continue
        r = check_ohlcv(df, cfg["timeframe"])
        res[s] = {"ok": r.ok, "errors": r.errors, "warnings": r.warnings,
                  "manifest": store.manifest("ohlcv", cfg["exchange"], s, cfg["timeframe"])}
    _print(res)


def cmd_data_import(a) -> None:
    from aster.data.binance_vision import import_root

    _print(import_root(Path(a.root)))


def cmd_data_import_r2(a) -> None:
    from aster.data.r2_klines import SYMBOLS, import_r2

    symbols = tuple(a.symbols.split(",")) if a.symbols else SYMBOLS
    _print(import_r2(symbols))


def cmd_data_check_r2(a) -> None:
    from aster.data.r2_klines import SYMBOLS, audit_local

    symbols = tuple(a.symbols.split(",")) if a.symbols else SYMBOLS
    _print(audit_local(symbols, verify_sha256=a.sha256))


def cmd_data_check_stores(a) -> None:
    """Audit every store the desk reads from: R2 spot 1m, sealed holdout, funding, aggTrades.

    P2 added this command because the legacy `cmd_data_check` only looked at
    the absent ``data/ohlcv`` daily store. A hypothesis preregistration may
    ask for any timeframe (5m/15m/1h/4h/1d) and any perp leg; the check
    must report which (symbol, timeframe) pairs the bar bridge has built,
    which R2 spot 1m partitions exist, which funding rates are imported
    and which sealed holdout partitions are present, so the prereg can be
    declared ready without re-touching the data layer.
    """
    from aster.data import r2_klines, funding_rate, aggtrades

    r2_symbols = tuple(a.symbols.split(",")) if a.symbols else r2_klines.SYMBOLS
    perp_symbols = ("BTCUSDT", "ETHUSDT", "SOLUSDT", "AAVEUSDT", "DOGEUSDT",
                    "SUIUSDT", "XRPUSDT", "BNBUSDT", "LINKUSDT", "NEARUSDT",
                    "XMRUSDT", "FETUSDT")
    agg_symbols = ("BTCUSDT", "ETHUSDT")

    r2_summary: dict = {"requested": list(r2_symbols)}
    try:
        r2_audit = r2_klines.audit_local(r2_symbols, verify_sha256=False)
        r2_summary.update({
            "ok": r2_audit.get("ok"),
            "partitions": r2_audit.get("partitions"),
            "rows": r2_audit.get("rows"),
            "bytes": r2_audit.get("bytes"),
            "symbols_found": r2_audit.get("symbols"),
            "missing": sorted(set(r2_symbols) - set(r2_audit.get("symbols", []))),
        })
    except FileNotFoundError as e:
        r2_summary["ok"] = False
        r2_summary["error"] = str(e)

    try:
        funding_audit = funding_rate.audit_local(perp_symbols, verify_sha256=False)
        funding_summary = {
            "ok": funding_audit.get("ok"),
            "partitions": funding_audit.get("partitions"),
            "rows": funding_audit.get("rows"),
            "symbols_found": funding_audit.get("symbols"),
            "missing": sorted(set(perp_symbols) - set(funding_audit.get("symbols", []))),
        }
    except FileNotFoundError as e:
        funding_summary = {"ok": False, "error": str(e)}

    try:
        agg_audit = aggtrades.audit_local(agg_symbols, verify_sha256=False)
        agg_summary = {
            "ok": agg_audit.get("ok"),
            "partitions": agg_audit.get("partitions"),
            "rows": agg_audit.get("rows"),
            "symbols_found": agg_audit.get("symbols"),
            "missing": sorted(set(agg_symbols) - set(agg_audit.get("symbols", []))),
        }
    except FileNotFoundError as e:
        agg_summary = {"ok": False, "error": str(e)}

    # Sealed holdout is checked separately; reading its content crosses the
    # holdout boundary, so we only report its presence here.
    from aster import paths
    sealed_root = paths.path("data", "sealed")
    sealed_summary = {
        "path": str(sealed_root),
        "exists": sealed_root.is_dir(),
    }
    if sealed_summary["exists"]:
        sealed_files = list(sealed_root.rglob("*.parquet"))
        sealed_summary["partitions"] = len(sealed_files)
        sealed_summary["bytes"] = sum(p.stat().st_size for p in sealed_files)

    # Bar bridge state: which (symbol, timeframe) parquets the bridge wrote.
    from aster.data import store
    cfg = paths.load_config("desk")
    bar_bridge: dict = {}
    ohlcv_root = paths.path("data", "ohlcv", cfg["exchange"])
    if ohlcv_root.is_dir():
        for sym_dir in sorted(ohlcv_root.iterdir()):
            if not sym_dir.is_dir():
                continue
            symbol = sym_dir.name.replace("-", "/")
            for tf_path in sorted(sym_dir.glob("*.parquet")):
                tf = tf_path.stem
                bar_bridge.setdefault(symbol, {})[tf] = {
                    "rows": int(pd.read_parquet(tf_path).shape[0]),
                    "manifest": str(tf_path.with_suffix(".manifest.json")),
                }

    _print({
        "r2_spot_1m": r2_summary,
        "funding_rate": funding_summary,
        "aggtrades": agg_summary,
        "sealed_holdout": sealed_summary,
        "bar_bridge": bar_bridge,
    })


def cmd_data_materialise_bars(a) -> None:
    """Materialise multi-TF spot bars from the sealed pre-cutoff R2 minute store.

    P2 made the bar bridge prereg-driven: the timeframe is no longer read
    from ``config/desk.yaml`` alone.  This CLI command materialises one or
    more timeframes for an explicit symbol list and writes a Parquet +
    manifest pair under ``data/ohlcv/<exchange>/<symbol>/<tf>.parquet``.
    """
    from aster.data import r2_backtest_store
    cfg = paths.load_config("desk")
    r2_symbols = [s.strip() for s in a.symbols.split(",") if s.strip()]
    tfs = [t.strip() for t in a.timeframes.split(",") if t.strip()]
    result = r2_backtest_store.materialise_bars(r2_symbols, tfs, exchange=cfg["exchange"])
    _print(r2_backtest_store.summarise(result))


def cmd_data_import_funding(a) -> None:
    """Import monthly funding rate ZIPs from a local folder.

    Each ZIP is parsed, validated against the strict cutoff, and stored under
    `data/r2/market/futures/um/funding_rate/`. A metadata-only manifest is
    written next to each Parquet. The explorer never reads the post-cutoff store.
    """
    from aster.data.funding_rate import import_archive

    root = Path(a.root)
    files = sorted(root.rglob("*.zip"))
    if not files:
        raise SystemExit(f"no funding ZIPs found under {root}")
    results = [import_archive(p) for p in files]
    _print({"imported": len(results), "files": [str(Path(r["source"])) for r in results]})


def cmd_data_audit_funding(a) -> None:
    """Audit the local funding rate store: manifest, cutoff and (optional) SHA-256."""
    from aster.data.funding_rate import audit_local

    symbols = tuple(a.symbols.split(",")) if a.symbols else (
        "BTCUSDT", "ETHUSDT", "SOLUSDT", "AAVEUSDT", "DOGEUSDT",
        "SUIUSDT", "XRPUSDT", "BNBUSDT", "LINKUSDT", "NEARUSDT",
        "XMRUSDT", "FETUSDT",
    )
    _print(audit_local(symbols, verify_sha256=a.sha256))


def cmd_data_import_aggtrades(a) -> None:
    """Import monthly aggTrades ZIPs from a local folder into Parquet partitions."""
    from aster.data.aggtrades import import_archive

    root = Path(a.root)
    if not root.exists():
        raise SystemExit(f"--root {root} does not exist")
    desk_root = Path(os.environ.get("ASTER_DESK", "."))
    dest_root = desk_root / "data" / "r2" / "market" / "spot" / "aggtrades"
    files = sorted(root.glob("*-aggTrades-*.zip"))
    results = []
    for z in files:
        results.append(import_archive(z, dest_root, archive_url=f"https://data.binance.vision/{z.name}"))
    _print({"imported": len(results), "rows": sum(r["rows"] for r in results),
            "files": [str(r["source"]) for r in results[:5]],
            "total_files": len(results)})


def cmd_data_audit_aggtrades(a) -> None:
    """Audit the local aggTrades store: manifest, cutoff and (optional) SHA-256."""
    from aster.data.aggtrades import audit_local

    symbols = tuple(a.symbols.split(",")) if a.symbols else ("BTCUSDT", "ETHUSDT")
    _print(audit_local(symbols, verify_sha256=a.sha256))


def cmd_data_build_volume_bars(a) -> None:
    """Build information bars (volume / dollar / taker-imbalance) from aggTrades.

    Reads the aggTrades Parquet partitions under ``data/r2/market/spot/aggtrades``,
    builds the requested family, and writes a sibling Parquet under
    ``data/r2/market/spot/aggtrades_bars/<family>/``. Returns a JSON report with
    the bar counts and a manifest of the input partitions that contributed.
    """
    from aster.data import aggtrades, information_bars

    family = a.family
    if family not in ("volume", "dollar", "taker_imbalance"):
        raise SystemExit(f"--family must be one of volume/dollar/taker_imbalance; got {family}")

    desk_root = Path(os.environ.get("ASTER_DESK", "."))
    src_root = desk_root / "data" / "r2" / "market" / "spot" / "aggtrades"
    if not src_root.exists():
        raise SystemExit(f"aggTrades store not built: {src_root} missing")
    out_root = desk_root / "data" / "r2" / "market" / "spot" / "aggtrades_bars" / family
    out_root.mkdir(parents=True, exist_ok=True)

    builders = {
        "volume": information_bars.build_volume_bars,
        "dollar": information_bars.build_dollar_bars,
        "taker_imbalance": information_bars.build_taker_imbalance_bars,
    }

    symbols = tuple(a.symbols.split(",")) if a.symbols else ("BTCUSDT", "ETHUSDT")
    summary: dict = {"family": family, "symbols": {}, "out_root": str(out_root)}
    for sym in symbols:
        sym_dir = src_root / f"symbol={sym}"
        if not sym_dir.exists():
            continue
        partitions = sorted(sym_dir.glob("year=*/month=*/part-0.parquet"))
        all_bars = []
        for part in partitions:
            table = pd.read_parquet(part)
            spec = builders[family](table, sym)
            if len(spec.bars):
                all_bars.append(spec.bars)
        if all_bars:
            bars = pd.concat(all_bars).sort_index()
            out = out_root / f"symbol={sym}.parquet"
            bars.to_parquet(out, engine="pyarrow", compression="snappy")
            manifest = {
                "family": family, "symbol": sym, "rows": int(len(bars)),
                "start": bars.index.min().isoformat(),
                "end": bars.index.max().isoformat(),
                "partitions_used": [p.name for p in partitions],
                "source_store": str(src_root),
            }
            (out.with_suffix(out.suffix + ".manifest.json")).write_text(
                json.dumps(manifest, indent=2, sort_keys=True)
            )
            summary["symbols"][sym] = manifest
    _print(summary)


def cmd_data_quality_r2(a) -> None:
    """Profile pre-cutoff minute quality. Never reads post-cutoff values."""
    from aster.data.minute_quality import profile_symbols

    cfg = paths.load_config("desk")
    defaults = cfg.get("minute_quality", {})
    symbols = tuple(a.symbols.split(",")) if a.symbols else None
    if symbols is None:
        symbols = tuple(defaults.get("symbols", ())) or None
    kwargs = {}
    if a.max_frozen_share is not None:
        kwargs["max_frozen_share"] = a.max_frozen_share
    if a.min_coverage is not None:
        kwargs["min_coverage"] = a.min_coverage
    if a.max_staleness_days is not None:
        kwargs["max_staleness_days"] = a.max_staleness_days
    if symbols is None:
        from aster.data.r2_klines import SYMBOLS
        kwargs["symbols"] = SYMBOLS
    else:
        kwargs["symbols"] = symbols
    _print(profile_symbols(**kwargs))


def cmd_data_bars_r2(a) -> None:
    """Build temporal + information bars from audited pre-cutoff minutes.

    Read-only and pre-cutoff by construction: the reader refuses a frame that
    crosses the exploration cutoff.  The clock repair is reported per symbol,
    never applied silently.
    """
    from aster.data.bars import bars_frame_report, build_bars, normalise_clock
    from aster.data.r2_klines import SYMBOLS, read_local

    symbols = tuple(a.symbols.split(",")) if a.symbols else SYMBOLS
    timeframes = a.timeframes.split(",") if a.timeframes else ["1h"]
    out: dict = {"timeframes": timeframes, "symbols": {}}
    for symbol in symbols:
        frame, repair = normalise_clock(read_local(symbol))
        out["symbols"][symbol] = {
            "clock_repair": repair.as_dict(),
            "bars": [bars_frame_report(symbol, frame, tf, drop_frozen=a.drop_frozen)
                     for tf in timeframes],
        }
    _print(out)


# ---- ledger ------------------------------------------------------------------
def cmd_ledger(a) -> None:
    from aster.ledger.db import Ledger

    L = Ledger()
    if a.action == "new":
        hid = L.register(a.title, a.statement, a.mechanism, a.falsification, json.loads(a.prediction),
                         a.family, a.market, a.source, a.regime, a.strategy)
        _print({"id": hid, "status": "preregistered"})
    elif a.action == "list":
        _print(L.search(a.status, a.market, a.family, a.text))
    elif a.action == "show":
        _print({"hypothesis": L.get(a.id), "prereg_intact": L.verify_prereg(a.id),
                "trials": L.trials(a.id), "events": L.events(a.id, 20)})
    elif a.action == "status":
        L.set_status(a.id, a.to, a.reason)
        _print({"id": a.id, "status": a.to})
    elif a.action == "lesson":
        L.add_lesson(a.id, a.text)
        _print({"id": a.id, "lesson": a.text})
    elif a.action == "trials":
        _print({"family": a.family, "dev_trials": L.n_trials(a.family, "dev")})


# ---- research ----------------------------------------------------------------
def cmd_backtest(a) -> None:
    from aster.backtest import pipeline

    rep = pipeline.run(a.hypothesis, a.strategy, json.loads(a.params or "{}"), a.sample, notes=a.notes or "")
    keep = ("hypothesis_id", "sample", "passed", "checks", "base", "stress", "statistics",
            "cost_drag_ann", "funding_drag_ann", "worst_windows", "trial_id", "artifact", "period")
    _print({k: rep[k] for k in keep if k in rep})


def cmd_pbo(a) -> None:
    from aster.validation.pbo import pbo_cscv

    m = pd.read_csv(a.returns_csv, index_col=0, parse_dates=True)
    _print(pbo_cscv(m, a.splits))


# ---- trading -----------------------------------------------------------------
def _broker(kind: str, cfg: dict):
    from aster.execution.brokers import CcxtBroker, PaperBroker, public_price_feed

    if kind == "paper":
        c = cfg.get("costs", {})
        return PaperBroker(public_price_feed(cfg["exchange"]), cfg.get("paper_initial_cash", 10_000.0),
                           c.get("fee_bps", 10.0), c.get("slippage_bps", 5.0))
    return CcxtBroker(cfg["exchange"], kind)


def cmd_trade_run(a) -> None:
    from aster.data import ccxt_source
    from aster.execution import journal
    from aster.execution.router import check_stage, rebalance
    from aster.ledger.db import Ledger
    from aster.risk.gate import RiskLimits
    from aster.strategies import get as get_strategy

    cfg = paths.load_config("desk")
    limits = RiskLimits.load()
    L = Ledger()
    hyp = L.get(a.hypothesis)
    broker = _broker(a.broker, cfg)
    check_stage(broker.mode, a.hypothesis, L)
    passed = [t for t in L.trials(a.hypothesis) if t["sample"] == "dev" and t["passed"]]
    if not passed:
        sys.exit("no passed dev trial: nothing validated to trade")
    t = passed[-1]
    strat = get_strategy(t["strategy"])(timeframe=cfg["timeframe"], **json.loads(t["params_json"]))
    if strat.version != t["version"]:
        sys.exit(f"strategy code is v{strat.version} but v{t['version']} was validated: re-validate first")

    ex = ccxt_source.make_exchange(cfg["exchange"])
    since = int((pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=cfg.get("live_warmup_days", 400))).timestamp() * 1000)
    closes = pd.DataFrame({s: ccxt_source.fetch_ohlcv(ex, s, cfg["timeframe"], since=since)["close"]
                           for s in cfg["universe"]})
    w = strat.target_weights(closes).iloc[-1]
    target = {s: float(v) for s, v in w.items() if abs(v) > 1e-6}
    fills = rebalance(target, broker, limits, L, a.hypothesis, strat.name, strat.version,
                      cfg.get("min_trade_usd", 10.0), cfg.get("rebalance_band", 0.02))
    acct = broker.account_state(cfg["universe"])
    journal.append("equity_snapshot", {"hypothesis_id": a.hypothesis, "mode": broker.mode,
                                       "equity": acct.equity, "positions": acct.positions})
    _print({"bar": str(closes.index[-1]), "target": target, "fills": [f.__dict__ if f else None for f in fills],
            "equity": acct.equity, "status": hyp["status"]})


def cmd_trade_run_all(a) -> None:
    """Run one bar for every hypothesis allowed to trade in this broker mode (used by cron)."""
    from aster.execution.router import LIVE_STAGES, PAPER_STAGES
    from aster.ledger.db import Ledger

    stages = LIVE_STAGES if a.broker == "live" else PAPER_STAGES
    hids = [h["id"] for h in Ledger().search() if h["status"] in stages]
    if not hids:
        return  # silent: nothing to trade
    for hid in hids:
        a.hypothesis = hid
        try:
            cmd_trade_run(a)
        except (SystemExit, Exception) as exc:  # one failing book must not stop the others
            print(f"ASTER TRADE ERROR {hid}: {exc!r}")


def cmd_paper_review(a) -> None:
    """Compare paper results with the dev backtest. Records a 'paper' trial."""
    from aster.backtest.metrics import summary
    from aster.execution import journal
    from aster.ledger.db import Ledger

    cfg = paths.load_config("desk")
    L = Ledger()
    hyp = L.get(a.hypothesis)
    snaps = [r for r in journal.read() if r["kind"] == "equity_snapshot"
             and r["payload"]["hypothesis_id"] == a.hypothesis and r["payload"]["mode"] in {"paper", "testnet"}]
    if len(snaps) < 3:
        sys.exit("not enough paper snapshots yet")
    eq = pd.Series({pd.Timestamp(r["ts"]).floor("D"): r["payload"]["equity"] for r in snaps}).sort_index()
    r = eq.pct_change().dropna()
    days = (eq.index[-1] - eq.index[0]).days
    dev = [t for t in L.trials(a.hypothesis) if t["sample"] == "dev" and t["passed"]][-1]
    bt = pd.read_csv(paths.path(dev["artifact"], "returns.csv"), index_col=0)["ret"]
    z = (r.mean() - bt.mean()) / (bt.std(ddof=1) / np.sqrt(len(r))) if len(r) > 1 else float("nan")
    decisions = [x for x in journal.read() if x["kind"] == "order_decision"
                 and x["payload"]["order"]["hypothesis_id"] == a.hypothesis]
    rejected = sum(not x["payload"]["approved"] for x in decisions)
    p = cfg.get("paper", {})
    checks = {"min_days": days >= p.get("min_days", 28),
              "consistent_with_backtest": bool(z >= p.get("min_z_vs_backtest", -2.0)),
              "no_kill_trip": not any(x["payload"].get("tripped_kill") for x in decisions)}
    passed = all(checks.values())
    stats = summary(r, "1d")
    if a.record:
        L.record_trial(a.hypothesis, dev["strategy"], dev["version"], json.loads(dev["params_json"]), "paper",
                       stats, None, None, 1, passed, notes=f"days={days} z={z:.2f} rejected_orders={rejected}")
    _print({"hypothesis": a.hypothesis, "status": hyp["status"], "days": days, "z_vs_backtest": z,
            "orders": len(decisions), "rejected_orders": rejected, "checks": checks, "passed": passed,
            "stats": stats, "recorded": a.record})


def cmd_risk_status(a) -> None:
    from aster.risk.gate import RiskLimits, kill_active, loss_metrics

    cfg = paths.load_config("desk")
    limits = RiskLimits.load()
    kill = kill_active()
    out = {"mode": limits.mode, "kill": kill}
    try:
        broker = _broker(a.broker or ("paper" if limits.mode == "paper" else limits.mode), cfg)
        acct = broker.account_state(cfg["universe"])
        daily, dd = loss_metrics(acct)
        out.update({"equity": acct.equity, "daily_loss_pct": daily, "drawdown_pct": dd,
                    "positions": acct.positions, "orders_today": acct.orders_today})
        warn = daily >= 0.75 * limits.max_daily_loss_pct or dd >= 0.75 * limits.max_drawdown_pct
    except Exception as exc:
        out["error"] = repr(exc)
        warn = True
    if a.alert_only:
        if kill or warn:
            print(f"ASTER RISK ALERT {datetime.now(timezone.utc):%Y-%m-%d %H:%M}Z")
            _print(out)
        return
    _print(out)


def cmd_kill(a) -> None:
    from aster.execution import journal
    from aster.risk.gate import kill_active, trip_kill

    if a.state == "on":
        trip_kill(a.reason or "manual")
        journal.append("kill_on", {"reason": a.reason or "manual"})
        _print({"kill": kill_active()})
    else:
        if not kill_active():
            _print({"kill": None})
            return
        who = _human_gate("clearing the kill switch", "CLEAR KILL")
        paths.kill_switch_path().unlink()
        journal.append("kill_off", {"by": who})
        _print({"kill": None, "cleared_by": who})


def cmd_promote(a) -> None:
    from aster.ledger.db import Ledger

    L = Ledger()
    h = L.get(a.hypothesis)
    _print({"id": h["id"], "title": h["title"], "status": h["status"], "to": a.to, "trials": len(L.trials(a.hypothesis))})
    who = _human_gate(f"promotion of {a.hypothesis} to {a.to}", f"PROMOTE {a.hypothesis}")
    L.set_status(a.hypothesis, a.to, a.reason or "human promotion", approved_by=who)
    _print({"id": a.hypothesis, "status": a.to, "approved_by": who})


def cmd_journal_verify(a) -> None:
    from aster.execution import journal

    _print(journal.verify())


# ---- parser ------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="desk", description="Aster quant desk")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init").set_defaults(fn=cmd_init)

    d = sub.add_parser("data").add_subparsers(dest="sub", required=True)
    f = d.add_parser("fetch")
    f.add_argument("--exchange"); f.add_argument("--symbols"); f.add_argument("--timeframe")
    f.add_argument("--since"); f.add_argument("--funding", action="store_true")
    f.set_defaults(fn=cmd_data_fetch)
    d.add_parser("check").set_defaults(fn=cmd_data_check)
    imp = d.add_parser("import")
    imp.add_argument("--root", required=True, help="directory containing Binance Vision monthly kline archives")
    imp.set_defaults(fn=cmd_data_import)
    r2 = d.add_parser("import-r2")
    r2.add_argument("--symbols", help="comma-separated approved symbols; defaults to the fixed R2 inventory universe")
    r2.set_defaults(fn=cmd_data_import_r2)
    r2_audit = d.add_parser("audit-r2", aliases=("check-r2",),
                            help="audit only locally imported pre-cutoff R2 spot partitions")
    r2_audit.add_argument("--symbols", help="comma-separated approved symbols; defaults to the fixed R2 inventory universe")
    r2_audit.add_argument("--sha256", action="store_true", help="recompute every local Parquet SHA-256")
    r2_audit.set_defaults(fn=cmd_data_check_r2)
    r2_stores = d.add_parser("check-stores",
                             help="audit every store the desk reads from (R2 1m, sealed, funding, aggTrades, bar bridge)")
    r2_stores.add_argument("--symbols", help="comma-separated R2 spot symbols; defaults to the full inventory")
    r2_stores.set_defaults(fn=cmd_data_check_stores)
    mat_b = d.add_parser("materialise-bars",
                         help="materialise multi-TF spot bars from the sealed pre-cutoff R2 minute store")
    mat_b.add_argument("--symbols", required=True, help="comma-separated R2 spot symbols (e.g. BTCUSDT,ETHUSDT)")
    mat_b.add_argument("--timeframes", required=True,
                       help="comma-separated timeframes (one or more of 5m,15m,1h,4h,1d)")
    mat_b.set_defaults(fn=cmd_data_materialise_bars)
    r2_q = d.add_parser("quality-r2",
                        help="profile pre-cutoff R2 minute bars: coverage, frozen minutes, price integrity")
    r2_q.add_argument("--symbols", help="comma-separated approved symbols; defaults to the fixed R2 inventory universe")
    r2_q.add_argument("--max-frozen-share", type=float,
                      help="maximum share of zero-trade minutes before a symbol is unusable")
    r2_q.add_argument("--min-coverage", type=float,
                      help="minimum present/expected calendar minutes before a symbol is unusable")
    r2_q.add_argument("--max-staleness-days", type=float,
                      help="maximum lag of a symbol's last bar behind the panel's last bar")
    r2_q.set_defaults(fn=cmd_data_quality_r2)
    r2_b = d.add_parser("bars-r2",
                        help="build temporal and information bars from pre-cutoff R2 minutes")
    r2_b.add_argument("--symbols", help="comma-separated approved symbols; defaults to the fixed R2 inventory universe")
    r2_b.add_argument("--timeframes", default="1h", help="comma-separated timeframes; default 1h")
    r2_b.add_argument("--drop-frozen", action="store_true",
                      help="drop zero-trade minutes (off by default: it hides illiquidity)")
    r2_b.set_defaults(fn=cmd_data_bars_r2)

    imp_f = d.add_parser("import-funding",
                         help="import monthly USD-M funding rate ZIPs from a local folder")
    imp_f.add_argument("--root", required=True)
    imp_f.set_defaults(fn=cmd_data_import_funding)

    aud_f = d.add_parser("audit-funding", aliases=("check-funding",),
                         help="audit local USD-M funding rate partitions")
    aud_f.add_argument("--symbols",
                       help="comma-separated approved symbols; defaults to the 12-symbol pre-cutoff inventory")
    aud_f.add_argument("--sha256", action="store_true")
    aud_f.set_defaults(fn=cmd_data_audit_funding)

    imp_a = d.add_parser("import-aggtrades",
                         help="import monthly spot aggTrades ZIPs from a local folder")
    imp_a.add_argument("--root", required=True)
    imp_a.set_defaults(fn=cmd_data_import_aggtrades)

    aud_a = d.add_parser("audit-aggtrades", aliases=("check-aggtrades",),
                         help="audit local spot aggTrades partitions")
    aud_a.add_argument("--symbols", default="BTCUSDT,ETHUSDT",
                       help="comma-separated approved symbols; defaults to BTCUSDT,ETHUSDT")
    aud_a.add_argument("--sha256", action="store_true")
    aud_a.set_defaults(fn=cmd_data_audit_aggtrades)

    bar_a = d.add_parser("build-volume-bars",
                         help="build information bars (volume/dollar/taker_imbalance) from aggTrades")
    bar_a.add_argument("--family", default="volume",
                       help="bar family: volume | dollar | taker_imbalance")
    bar_a.add_argument("--symbols", default="BTCUSDT,ETHUSDT",
                       help="comma-separated approved symbols; defaults to BTCUSDT,ETHUSDT")
    bar_a.set_defaults(fn=cmd_data_build_volume_bars)

    lg = sub.add_parser("ledger").add_subparsers(dest="action", required=True)
    n = lg.add_parser("new")
    for k in ("title", "statement", "mechanism", "falsification", "prediction", "family", "market", "source"):
        n.add_argument(f"--{k}", required=True)
    n.add_argument("--regime"); n.add_argument("--strategy")
    ls = lg.add_parser("list")
    ls.add_argument("--status"); ls.add_argument("--market"); ls.add_argument("--family"); ls.add_argument("--text")
    lg.add_parser("show").add_argument("id")
    st = lg.add_parser("status")
    st.add_argument("id"); st.add_argument("to"); st.add_argument("--reason", required=True)
    le = lg.add_parser("lesson"); le.add_argument("id"); le.add_argument("text")
    tr = lg.add_parser("trials"); tr.add_argument("family")
    for sp in (n, ls, st, le, tr):
        sp.set_defaults(fn=cmd_ledger)
    lg.choices["show"].set_defaults(fn=cmd_ledger)

    b = sub.add_parser("backtest")
    b.add_argument("--hypothesis", required=True); b.add_argument("--strategy", required=True)
    b.add_argument("--params"); b.add_argument("--sample", default="dev", choices=["dev", "holdout"])
    b.add_argument("--notes")
    b.set_defaults(fn=cmd_backtest)

    pb = sub.add_parser("pbo")
    pb.add_argument("returns_csv"); pb.add_argument("--splits", type=int, default=16)
    pb.set_defaults(fn=cmd_pbo)

    t = sub.add_parser("trade").add_subparsers(dest="sub", required=True)
    tr = t.add_parser("run")
    tr.add_argument("--hypothesis", required=True)
    tr.add_argument("--broker", default="paper", choices=["paper", "testnet", "live"])
    tr.set_defaults(fn=cmd_trade_run)
    ta = t.add_parser("run-all")
    ta.add_argument("--broker", default="paper", choices=["paper", "testnet", "live"])
    ta.set_defaults(fn=cmd_trade_run_all)

    pr = sub.add_parser("paper").add_subparsers(dest="sub", required=True)
    rv = pr.add_parser("review"); rv.add_argument("--hypothesis", required=True)
    rv.add_argument("--record", action="store_true")
    rv.set_defaults(fn=cmd_paper_review)

    r = sub.add_parser("risk").add_subparsers(dest="sub", required=True)
    rs = r.add_parser("status"); rs.add_argument("--alert-only", action="store_true")
    rs.add_argument("--broker", choices=["paper", "testnet", "live"])
    rs.set_defaults(fn=cmd_risk_status)

    k = sub.add_parser("kill")
    k.add_argument("state", choices=["on", "off"]); k.add_argument("--reason")
    k.set_defaults(fn=cmd_kill)

    pm = sub.add_parser("promote")
    pm.add_argument("hypothesis"); pm.add_argument("--to", required=True, choices=["live_pilot", "live"])
    pm.add_argument("--reason")
    pm.set_defaults(fn=cmd_promote)

    j = sub.add_parser("journal").add_subparsers(dest="sub", required=True)
    j.add_parser("verify").set_defaults(fn=cmd_journal_verify)
    return p


def _load_dotenv() -> None:
    """Load desk/config/.env without overriding the shell. ASTER_LIVE_ARMED is never read
    from a file: arming live trading must be an explicit act in the running shell."""
    p = paths.path("config", ".env")
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k != "ASTER_LIVE_ARMED" and v and k not in os.environ:
            os.environ[k] = v


def main(argv: list[str] | None = None) -> None:
    _load_dotenv()
    args = build_parser().parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
