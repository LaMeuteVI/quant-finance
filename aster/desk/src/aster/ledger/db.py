"""Hypothesis ledger: the desk's long-term memory.

Every idea, every backtest attempt and every lesson lives here. Three
invariants are enforced in code, not left to the agent's good will:
  1. Pre-registration is immutable: statement, falsification test and
     prediction are hashed at creation; there is no API to edit them.
  2. Every backtest run is a trial and is counted. The DSR uses that count.
  3. The sealed holdout is read once per hypothesis, then never again.
Status changes follow an explicit state machine; live stages need a human.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from aster import paths

STATUSES = (
    "idea", "preregistered", "backtest_passed", "holdout_passed", "paper",
    "paper_passed", "live_pilot", "live", "paused", "rejected", "retired",
)
HUMAN_ONLY = {"live_pilot", "live"}
TRANSITIONS = {
    "idea": {"preregistered", "rejected"},
    "preregistered": {"backtest_passed", "rejected"},
    "backtest_passed": {"holdout_passed", "rejected"},
    "holdout_passed": {"paper", "rejected"},
    "paper": {"paper_passed", "rejected", "paused"},
    "paper_passed": {"live_pilot", "rejected", "paused"},
    "live_pilot": {"live", "paused", "retired", "rejected"},
    "live": {"paused", "retired"},
    "paused": {"paper", "retired", "rejected"},
    "rejected": set(),
    "retired": set(),
}
# A stage can only be entered if the latest trial of that sample passed its gate.
EVIDENCE = {"backtest_passed": "dev", "holdout_passed": "holdout", "paper_passed": "paper"}
MAX_REVISIONS = 5  # strategy versions per hypothesis before it must be abandoned

SCHEMA = """
CREATE TABLE IF NOT EXISTS hypotheses (
    id TEXT PRIMARY KEY,
    created_at TEXT NOT NULL,
    title TEXT NOT NULL,
    statement TEXT NOT NULL,
    mechanism TEXT NOT NULL,
    falsification TEXT NOT NULL,
    prediction_json TEXT NOT NULL,
    prereg_hash TEXT NOT NULL,
    family TEXT NOT NULL,
    market TEXT NOT NULL,
    source TEXT NOT NULL,
    regime TEXT,
    status TEXT NOT NULL,
    strategy TEXT,
    holdout_start TEXT,
    holdout_read_at TEXT,
    approved_by TEXT,
    lessons TEXT NOT NULL DEFAULT '',
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS trials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hypothesis_id TEXT NOT NULL REFERENCES hypotheses(id),
    family TEXT NOT NULL,
    created_at TEXT NOT NULL,
    strategy TEXT NOT NULL,
    version TEXT NOT NULL,
    params_json TEXT NOT NULL,
    sample TEXT NOT NULL CHECK (sample IN ('dev', 'holdout', 'paper', 'live')),
    sharpe_pp REAL, sharpe_ann REAL, n_obs INTEGER, skew REAL, kurtosis REAL,
    total_return REAL, max_drawdown REAL, psr REAL, dsr REAL, n_trials_family INTEGER,
    passed INTEGER, artifact TEXT, notes TEXT
);
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    hypothesis_id TEXT,
    kind TEXT NOT NULL,
    detail TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS trials_family ON trials(family);
CREATE INDEX IF NOT EXISTS hyp_status ON hypotheses(status);
"""


class LedgerError(RuntimeError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def prereg_hash(statement: str, mechanism: str, falsification: str, prediction: dict) -> str:
    blob = json.dumps({"s": statement, "m": mechanism, "f": falsification, "p": prediction},
                      sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode()).hexdigest()


class Ledger:
    def __init__(self, db_path: Path | None = None):
        self.db_path = Path(db_path or paths.ledger_path())
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._conn() as c:
            c.executescript(SCHEMA)

    @contextmanager
    def _conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _event(self, c, hid: str | None, kind: str, detail: dict) -> None:
        c.execute("INSERT INTO events (ts, hypothesis_id, kind, detail) VALUES (?,?,?,?)",
                  (_now(), hid, kind, json.dumps(detail, ensure_ascii=False)))

    # ---- hypotheses -------------------------------------------------------
    def register(self, title: str, statement: str, mechanism: str, falsification: str, prediction: dict,
                 family: str, market: str, source: str, regime: str | None = None,
                 strategy: str | None = None) -> str:
        """Create a pre-registered hypothesis. The prediction must exist BEFORE any backtest."""
        for name, v in {"statement": statement, "mechanism": mechanism, "falsification": falsification}.items():
            if not v or len(v.strip()) < 10:
                raise LedgerError(f"{name} is required and must be specific")
        if not prediction:
            raise LedgerError("prediction is required (e.g. {'sharpe_ann_min': 0.8, 'max_dd_max': -0.25})")
        day = datetime.now(timezone.utc).strftime("%Y%m%d")
        with self._conn() as c:
            n = c.execute("SELECT COUNT(*) FROM hypotheses WHERE id LIKE ?", (f"H-{day}-%",)).fetchone()[0]
            hid = f"H-{day}-{n + 1:03d}"
            h = prereg_hash(statement, mechanism, falsification, prediction)
            c.execute(
                "INSERT INTO hypotheses (id, created_at, title, statement, mechanism, falsification, prediction_json,"
                " prereg_hash, family, market, source, regime, status, strategy, updated_at)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (hid, _now(), title, statement, mechanism, falsification, json.dumps(prediction, sort_keys=True),
                 h, family, market, source, regime, "preregistered", strategy, _now()),
            )
            self._event(c, hid, "registered", {"prereg_hash": h})
        return hid

    def get(self, hid: str) -> dict:
        with self._conn() as c:
            row = c.execute("SELECT * FROM hypotheses WHERE id = ?", (hid,)).fetchone()
        if not row:
            raise LedgerError(f"unknown hypothesis {hid}")
        d = dict(row)
        d["prediction"] = json.loads(d.pop("prediction_json"))
        return d

    def verify_prereg(self, hid: str) -> bool:
        h = self.get(hid)
        return prereg_hash(h["statement"], h["mechanism"], h["falsification"], h["prediction"]) == h["prereg_hash"]

    def search(self, status: str | None = None, market: str | None = None, family: str | None = None,
               text: str | None = None) -> list[dict]:
        q, args = "SELECT id, title, family, market, regime, status, lessons, updated_at FROM hypotheses WHERE 1=1", []
        for col, val in (("status", status), ("market", market), ("family", family)):
            if val:
                q += f" AND {col} = ?"
                args.append(val)
        if text:
            q += " AND (title LIKE ? OR statement LIKE ? OR lessons LIKE ?)"
            args += [f"%{text}%"] * 3
        with self._conn() as c:
            return [dict(r) for r in c.execute(q + " ORDER BY created_at DESC", args)]

    def set_status(self, hid: str, new: str, reason: str, approved_by: str | None = None) -> None:
        if new not in STATUSES:
            raise LedgerError(f"unknown status {new}")
        cur = self.get(hid)["status"]
        if new not in TRANSITIONS[cur]:
            raise LedgerError(f"illegal transition {cur} -> {new}")
        if new in HUMAN_ONLY and not approved_by:
            raise LedgerError(f"{new} requires a human approval (desk promote)")
        evidence = EVIDENCE.get(new)
        if evidence and not self._has_passed_trial(hid, evidence):
            raise LedgerError(f"{new} requires a passed '{evidence}' trial recorded by the pipeline")
        with self._conn() as c:
            c.execute("UPDATE hypotheses SET status = ?, updated_at = ?, approved_by = COALESCE(?, approved_by)"
                      " WHERE id = ?", (new, _now(), approved_by, hid))
            self._event(c, hid, "status", {"from": cur, "to": new, "reason": reason, "approved_by": approved_by})

    def _has_passed_trial(self, hid: str, sample: str) -> bool:
        with self._conn() as c:
            row = c.execute("SELECT passed FROM trials WHERE hypothesis_id = ? AND sample = ? ORDER BY id DESC LIMIT 1",
                            (hid, sample)).fetchone()
        return bool(row and row[0])

    def add_lesson(self, hid: str, lesson: str) -> None:
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        with self._conn() as c:
            c.execute("UPDATE hypotheses SET lessons = lessons || ?, updated_at = ? WHERE id = ?",
                      (f"[{stamp}] {lesson}\n", _now(), hid))
            self._event(c, hid, "lesson", {"text": lesson})

    # ---- sealed holdout ---------------------------------------------------
    def seal_holdout(self, hid: str, holdout_start: str) -> None:
        h = self.get(hid)
        if h["holdout_start"] and h["holdout_start"] != holdout_start:
            raise LedgerError(f"holdout already sealed at {h['holdout_start']}; it cannot move")
        with self._conn() as c:
            c.execute("UPDATE hypotheses SET holdout_start = ? WHERE id = ?", (holdout_start, hid))

    def consume_holdout(self, hid: str) -> None:
        h = self.get(hid)
        if h["status"] != "backtest_passed":
            raise LedgerError("holdout can only be read after the dev backtest passed")
        if h["holdout_read_at"]:
            raise LedgerError(f"holdout already read at {h['holdout_read_at']}: one shot per hypothesis")
        with self._conn() as c:
            c.execute("UPDATE hypotheses SET holdout_read_at = ? WHERE id = ?", (_now(), hid))
            self._event(c, hid, "holdout_read", {})

    # ---- trials -----------------------------------------------------------
    def n_trials(self, family: str, sample: str = "dev") -> int:
        with self._conn() as c:
            return c.execute("SELECT COUNT(*) FROM trials WHERE family = ? AND sample = ?",
                             (family, sample)).fetchone()[0]

    def trial_sharpes(self, family: str, sample: str = "dev") -> list[float]:
        with self._conn() as c:
            rows = c.execute("SELECT sharpe_pp FROM trials WHERE family = ? AND sample = ? AND sharpe_pp IS NOT NULL",
                             (family, sample)).fetchall()
        return [r[0] for r in rows]

    def versions(self, hid: str) -> set[str]:
        with self._conn() as c:
            return {r[0] for r in c.execute("SELECT DISTINCT version FROM trials WHERE hypothesis_id = ?", (hid,))}

    def check_revision_budget(self, hid: str, version: str) -> None:
        v = self.versions(hid)
        if version not in v and len(v) >= MAX_REVISIONS:
            raise LedgerError(f"{hid} already has {len(v)} strategy versions (max {MAX_REVISIONS}). "
                              "Reject it and write the lesson instead of fitting noise.")

    def record_trial(self, hid: str, strategy: str, version: str, params: dict, sample: str, stats: dict,
                     psr: float | None, dsr: float | None, n_trials_family: int, passed: bool | None,
                     artifact: str | None = None, notes: str = "") -> int:
        h = self.get(hid)
        with self._conn() as c:
            cur = c.execute(
                "INSERT INTO trials (hypothesis_id, family, created_at, strategy, version, params_json, sample,"
                " sharpe_pp, sharpe_ann, n_obs, skew, kurtosis, total_return, max_drawdown, psr, dsr,"
                " n_trials_family, passed, artifact, notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (hid, h["family"], _now(), strategy, version, json.dumps(params, sort_keys=True), sample,
                 stats.get("sharpe_pp"), stats.get("sharpe_ann"), stats.get("n_obs"), stats.get("skew"),
                 stats.get("kurtosis"), stats.get("total_return"), stats.get("max_drawdown"), psr, dsr,
                 n_trials_family, None if passed is None else int(passed), artifact, notes),
            )
            return int(cur.lastrowid)

    def trials(self, hid: str) -> list[dict]:
        with self._conn() as c:
            return [dict(r) for r in c.execute("SELECT * FROM trials WHERE hypothesis_id = ? ORDER BY id", (hid,))]

    def events(self, hid: str | None = None, limit: int = 50) -> list[dict]:
        q = "SELECT * FROM events" + (" WHERE hypothesis_id = ?" if hid else "") + " ORDER BY id DESC LIMIT ?"
        with self._conn() as c:
            return [dict(r) for r in c.execute(q, ((hid, limit) if hid else (limit,)))]
