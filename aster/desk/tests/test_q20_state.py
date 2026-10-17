import json
from pathlib import Path


JSON_PATH = Path("research/atlas/q20_state.json")


def test_q20_state_well_formed():
    assert JSON_PATH.exists(), "Q20 state artefact must exist"
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    assert data["protocol"]["cutoff_exclusive"].startswith("2024-07-01")
    assert data["protocol"]["no_holdout"] is True
    assert data["protocol"]["no_live"] is True
    assert data["protocol"]["no_paper"] is True
    assert data["protocol"]["no_order"] is True
    assert data["protocol"]["no_key"] is True
    assert data["protocol"]["status"] == "descriptive_only"
    assert data["ledger"]["open_hypotheses"] == 0
    assert data["candidates"]["ledger_strategies"] == 0
    assert isinstance(data["what_died_and_why"], list) and len(data["what_died_and_why"]) >= 9
    assert "tick microstructure" in data["verdict"].lower() or "red" in data["verdict"].lower()


def test_q20_memo_present():
    memo = Path("research/memos/2026-10-16-Q20-N9.md")
    assert memo.exists(), "Q20 memo must exist"
    text = memo.read_text(encoding="utf-8")
    assert "2026-10-16" in text
    assert "No holdout" in text or "no holdout" in text
    assert "Q20" in text
    assert "Q5" in text and "Q14" in text
