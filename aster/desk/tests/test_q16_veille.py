import json
from pathlib import Path


JSON_PATH = Path("research/atlas/q16_veille.json")


def test_veille_artefact_is_well_formed():
    assert JSON_PATH.exists(), "Q16 veille artefact must exist"
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    assert "claims" in data
    assert "top3_replication_leads" in data
    assert isinstance(data["claims"], list) and len(data["claims"]) >= 6
    for claim in data["claims"]:
        assert "reference" in claim and "claim" in claim
        assert "ladder_level" in claim
        assert "ranking" in claim
    assert data["candidate"] is False
    assert data["top3_replication_leads"] == []


def test_veille_protocol_lock():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    proto = data["protocol"]
    assert proto["cutoff_exclusive"].startswith("2024-07-01")
    assert proto["no_holdout"] is True
    assert proto["no_data_download"] is True
    assert proto["no_ledger_hypothesis"] is True
    assert proto["no_modify_protected_paths"] is True
