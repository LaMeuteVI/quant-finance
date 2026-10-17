"""Tests for the Q21 microstructure JSON artefact."""
import json
from pathlib import Path


JSON_PATH = Path("research/atlas/q21_microstructure.json")


def test_q21_artefact_well_formed():
    assert JSON_PATH.exists()
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    assert "Q21" in data["protocol"]
    assert data["bar_freq"] == "1min"
    assert "BTCUSDT" in data["results"]
    btc = data["results"]["BTCUSDT"]
    assert btc["kyle_lambda"]["valid"] is True
    assert btc["predictive_signed_flow"]["valid"] is True
    assert btc["quintile_return"]["valid"] is True


def test_q21_memo_present():
    memo = Path("research/memos/2026-10-16-Q21-N10.md")
    assert memo.exists()
    text = memo.read_text(encoding="utf-8")
    assert "2026-10-16" in text
    assert "No new download" in text or "no new download" in text
    assert "H-20261016-005" in text
    assert "falsif" in text.lower()


def test_q21_prereg_present():
    prereg = Path("research/notes/2026-10-16-Q21-prereg.md")
    assert prereg.exists()
    text = prereg.read_text(encoding="utf-8")
    assert "2024-07-01" in text
    assert "H-20261016-005" in text
    assert "H-20261016-006" in text
