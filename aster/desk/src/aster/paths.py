"""Filesystem layout of the desk. ASTER_DESK overrides the root (used by tests)."""

from __future__ import annotations

import os
from pathlib import Path

import yaml


def desk_root() -> Path:
    env = os.environ.get("ASTER_DESK")
    if env:
        return Path(env).expanduser().resolve()
    return Path(__file__).resolve().parents[2]


def path(*parts: str) -> Path:
    return desk_root().joinpath(*parts)


DIRS = ("data", "research", "backtests", "journal", "reports", "memory", "state", "config")


def ensure_dirs() -> None:
    for d in DIRS:
        path(d).mkdir(parents=True, exist_ok=True)


def load_config(name: str) -> dict:
    """Load desk/config/<name>.yaml."""
    p = path("config", f"{name}.yaml")
    with p.open() as fh:
        return yaml.safe_load(fh) or {}


def ledger_path() -> Path:
    return path("memory", "ledger.db")


def kill_switch_path() -> Path:
    return path("state", "KILL")
