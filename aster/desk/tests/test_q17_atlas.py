from pathlib import Path

from aster.research import q17_atlas

SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT", "AAVEUSDT", "SUIUSDT", "NEARUSDT")


def test_dossiers_written():
    q17_atlas.main()
    for sym in SYMBOLS:
        path = Path(f"research/assets/{sym.lower()}-dossier.md")
        assert path.exists(), f"missing {path}"
        content = path.read_text(encoding="utf-8")
        assert "Level reached" in content
        assert "2024-07-01" in content
        assert "No holdout" in content


def test_protocol_constants():
    assert q17_atlas.CUTOFF.startswith("2024-07-01")
    assert q17_atlas.SYMBOLS[0] == "BTCUSDT"
    assert "AAVEUSDT" in q17_atlas.SYMBOLS
