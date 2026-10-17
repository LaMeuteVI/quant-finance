import json
from pathlib import Path


JSON_PATH = Path("research/atlas/q17_atlas.json")
SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT", "AAVEUSDT", "SUIUSDT", "NEARUSDT")


def test_atlas_index_well_formed():
    assert JSON_PATH.exists()
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    assert data["protocol"]["cutoff_exclusive"].startswith("2024-07-01")
    assert data["protocol"]["no_holdout"] is True
    assert set(data["dossiers"].keys()) == set(SYMBOLS)
    for sym in SYMBOLS:
        path = Path(data["dossiers"][sym]["path"])
        assert path.exists(), f"missing dossier for {sym}: {path}"
        text = path.read_text(encoding="utf-8")
        assert "Level reached" in text
        assert sym in text
        assert "2024-07-01" in text
