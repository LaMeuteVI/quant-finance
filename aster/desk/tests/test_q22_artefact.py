"""Tests for the Q22 microstructure JSON artefact."""
import json
from pathlib import Path


JSON_PATH = Path("research/atlas/q22_microstructure.json")


def test_q22_artefact_well_formed():
    assert JSON_PATH.exists()
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    assert "Q22" in data["protocol"]
    assert "axes" in data
    # Expect 6 single-asset axes (BTC/ETH × 1m/5m/15m) + 2 cross-asset axes.
    assert "BTCUSDT_1min" in data["axes"]
    assert "BTCUSDT_5min" in data["axes"]
    assert "BTCUSDT_15min" in data["axes"]
    assert "ETHUSDT_1min" in data["axes"]
    assert "ETHUSDT_5min" in data["axes"]
    assert "ETHUSDT_15min" in data["axes"]
    assert "BTC_ETH_cross_5min" in data["axes"]
    assert "BTC_ETH_cross_15min" in data["axes"]


def test_q22_per_axis_verdict():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    # All axes must have a verdict with 'candidate' key (cross-asset axes do not, skip).
    for key, axis in data["axes"].items():
        if "verdict" in axis:
            v = axis["verdict"]
            assert "candidate" in v
            assert isinstance(v["candidate"], bool)
            # On 2026-10-16 the run produced 0 candidates.
            assert v["candidate"] is False, f"unexpected candidate at {key}"


def test_q22_memo_present():
    memo = Path("research/memos/2026-10-16-Q22-N11.md")
    assert memo.exists()
    text = memo.read_text(encoding="utf-8")
    assert "2026-10-16" in text
    assert "No holdout" in text or "no holdout" in text
    assert "H-20261022-001" in text
    assert "falsif" in text.lower()


def test_q22_prereg_present():
    prereg = Path("research/notes/2026-10-16-Q22-prereg.md")
    assert prereg.exists()
    text = prereg.read_text(encoding="utf-8")
    assert "2024-07-01" in text
    assert "H-20261022-001" in text
    assert "H-20261022-002" in text
    assert "stream-and-discard" in text
