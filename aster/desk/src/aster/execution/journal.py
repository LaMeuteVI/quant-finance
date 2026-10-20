"""Append-only, hash-chained decision journal (JSONL).

Each record carries the hash of the previous one, so any after-the-fact edit
or deletion breaks the chain and `desk journal verify` reports it.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from aster import paths

GENESIS = "0" * 64


def journal_path() -> Path:
    return paths.path("journal", "decisions.jsonl")


def _digest(prev: str, body: dict) -> str:
    return hashlib.sha256((prev + json.dumps(body, sort_keys=True, default=str)).encode()).hexdigest()


def _last_hash(p: Path) -> str:
    if not p.exists() or p.stat().st_size == 0:
        return GENESIS
    with p.open("rb") as fh:
        fh.seek(0, 2)
        size = fh.tell()
        fh.seek(max(0, size - 65536))
        tail = fh.read().decode().strip().splitlines()
    return json.loads(tail[-1])["hash"]


def append(kind: str, payload: dict, p: Path | None = None) -> dict:
    p = p or journal_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    prev = _last_hash(p)
    body = {"ts": datetime.now(timezone.utc).isoformat(), "kind": kind, "payload": payload, "prev": prev}
    rec = {**body, "hash": _digest(prev, body)}
    with p.open("a") as fh:
        fh.write(json.dumps(rec, sort_keys=True, default=str) + "\n")
    return rec


def verify(p: Path | None = None) -> dict:
    p = p or journal_path()
    if not p.exists():
        return {"ok": True, "records": 0}
    prev = GENESIS
    for i, line in enumerate(p.read_text().splitlines(), 1):
        rec = json.loads(line)
        body = {k: rec[k] for k in ("ts", "kind", "payload", "prev")}
        if rec["prev"] != prev or _digest(prev, body) != rec["hash"]:
            return {"ok": False, "records": i - 1, "broken_at_line": i}
        prev = rec["hash"]
    return {"ok": True, "records": i if p.stat().st_size else 0}


def read(p: Path | None = None, since: str | None = None) -> list[dict]:
    p = p or journal_path()
    if not p.exists():
        return []
    recs = [json.loads(line) for line in p.read_text().splitlines() if line.strip()]
    return [r for r in recs if since is None or r["ts"] >= since]
