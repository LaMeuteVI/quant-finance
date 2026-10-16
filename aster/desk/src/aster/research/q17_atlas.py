"""Q17 — Atlas and asset dossiers (former F).

Strictly pre-cutoff, no holdout, no live, no paper, no order, no key. Just
walks the existing `research/assets/` and `research/memos/` and `research/atlas/`
artefacts and writes one consolidated `research/assets/<SYMBOL>-dossier.md` per
asset, with the level reached (N0..N7) at the top.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

DESK = Path("/root/quant-finance/aster/desk/research")
ASSETS = DESK / "assets"
ATLAS = DESK / "atlas"
MEMOS = DESK / "memos"
SYMBOLS = (
    "BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "SOLUSDT",
    "LINKUSDT", "DOGEUSDT", "AAVEUSDT", "SUIUSDT", "NEARUSDT",
)
CUTOFF = "2024-07-01T00:00:00Z"
TODAY = "2026-10-16"


def _find(symbol: str, substring: str) -> list[str]:
    short = symbol.replace("USDT", "").lower()
    pat = re.compile(rf"({re.escape(symbol.lower())}|{re.escape(short)})" + r".*" + re.escape(substring), re.IGNORECASE)
    return sorted(
        str(p.relative_to(DESK.parent)) for p in ASSETS.iterdir() if pat.search(p.name)
    )


def _klines_1m_present(symbol: str) -> bool:
    short = symbol.replace("USDT", "").lower()
    klines_dir = Path("/root/quant-finance/aster/desk/data/r2/market/spot/klines_1m")
    if not klines_dir.exists():
        return False
    candidates = [symbol, short, short.upper(), symbol.lower(), symbol.replace("/", "")]
    for p in klines_dir.iterdir():
        if p.is_dir() and any(c.lower() in p.name.lower() for c in candidates):
            return True
    return False


def _panel_participation(symbol: str) -> list[str]:
    short = symbol.replace("USDT", "").lower()
    candidates = [symbol.lower(), short]
    out = []
    for p in ATLAS.iterdir():
        name = p.name.lower()
        if any(c in name for c in candidates) and any(t in name for t in ("q11", "q12", "q13", "q14")):
            out.append(str(p.relative_to(DESK.parent)))
    for p in MEMOS.iterdir():
        name = p.name.lower()
        if any(c in name for c in candidates) and any(t in name for t in ("q11", "q12", "q13", "q14")):
            out.append(str(p.relative_to(DESK.parent)))
    return sorted(set(out))


def _atlas_match(symbol: str, slug: str) -> str | None:
    """Find an atlas file whose name mentions both `symbol` and `slug`."""
    short = symbol.replace("USDT", "").lower()
    for p in ATLAS.iterdir():
        if (symbol.lower() in p.name.lower() or short in p.name.lower()) and slug.lower() in p.name.lower():
            return str(p.relative_to(DESK.parent))
    return None


def _memo_match(symbol: str, slug: str) -> str | None:
    short = symbol.replace("USDT", "").lower()
    for p in MEMOS.iterdir():
        if (symbol.lower() in p.name.lower() or short in p.name.lower()) and slug.lower() in p.name.lower():
            return str(p.relative_to(DESK.parent))
    return None


def _level_reached(symbol: str) -> dict[str, str | None]:
    """For each N-level, report the most recent dated artefact path, or None."""
    out = {}
    for level in ("N0", "N1", "N2", "N3", "N4", "N5"):
        matches = _find(symbol, level)
        out[level] = matches[-1] if matches else None
    out["N6"] = None
    out["N7"] = None
    return out


def _panel_links() -> list[str]:
    panels = []
    for p in ASSETS.iterdir():
        if re.search(r"(panel|inter|axe-7|q1[3-6])", p.name, re.IGNORECASE):
            panels.append(str(p.relative_to(DESK.parent)))
    return sorted(panels)[-12:]


def _panel_links_for_symbol(symbol: str) -> list[str]:
    short = symbol.replace("USDT", "").lower()
    out = []
    for path in _panel_links():
        if short in path.lower() or symbol.lower() in path.lower():
            out.append(path)
    return out


def _atlas_links(symbol: str) -> list[str]:
    """For per-symbol names: nothing in the atlas uses the symbol (the atlas is axis-keyed)."""
    return []


def _memo_links(symbol: str) -> list[str]:
    return []


def _qaxes_for_symbol(symbol: str) -> list[tuple[str, str]]:
    """Map a symbol to the Q-axes that analysed it (with a short verdict pointer)."""
    short = symbol.replace("USDT", "").lower()
    # BTC and ETH are the only symbols in the N0..N5 per-asset dossiers.
    if short == "btc":
        return [
            ("Q6", "kline flow, no candidate"),
            ("Q7", "lead-lag, no candidate"),
            ("Q8", "funding carry, descriptive"),
            ("Q9", "N2 multi-TF descriptive"),
            ("Q10", "volatility forecast value, no alpha"),
            ("Q11", "excluded from panel (BTC/ETH blackout)"),
        ]
    if short == "eth":
        return [
            ("Q6", "kline flow, no candidate"),
            ("Q7", "lead-lag, no candidate"),
            ("Q8", "funding carry, descriptive"),
            ("Q9", "N2 multi-TF descriptive"),
            ("Q10", "volatility forecast value, no alpha"),
            ("Q11", "excluded from panel (BTC/ETH blackout)"),
        ]
    if short in ("bnb", "xrp", "sol", "link", "doge", "aave", "sui", "near"):
        return [
            ("Q9", "N2 multi-TF descriptive (descriptive only)"),
            ("Q11", "regime grid — no candidate, run quarantined (preregistration written after execution)"),
            ("Q12", "kline flow alts — 0/128 cells past conservative cost hurdle (artefact provisional)"),
            ("Q13", "MP denoising / detoning / angular clustering — no exploitable pairwise structure"),
            ("Q14", "panel FE + sector pairs — all 5 pairs fast mean-reverting (half-life 0.6–0.7 d), falsification bar met"),
        ]
    return []


def _highest_reached(levels: dict[str, str | None]) -> str:
    for level in ("N5", "N4", "N3", "N2", "N1", "N0"):
        if levels.get(level):
            return level
    return "N0 (no N0 dossier present)"


def _one(symbol: str) -> str:
    levels = _level_reached(symbol)
    highest = _highest_reached(levels)
    qaxes = _qaxes_for_symbol(symbol)
    panel_links = _panel_links_for_symbol(symbol)
    panel_q = _panel_participation(symbol)
    klines_1m = _klines_1m_present(symbol)
    rows = []
    for level, path in levels.items():
        status = "**complete**" if path else "—"
        rows.append(f"| {level} | {status} | {path or '—'} |")
    coverage_lines = [
        f"- klines_1m parquet dir: **{'present' if klines_1m else 'not hydrated'}**",
        f"- Panel participation (Q11/Q12/Q13/Q14 artefacts on disk): **{', '.join(p.split('/')[-1] for p in panel_q) if panel_q else 'none on disk (the atlas is axis-keyed, not symbol-keyed)'}**",
    ]
    qaxes_lines = "\n".join(f"- **{q}** — {v}" for q, v in qaxes) or "- _(no Q-axes include this symbol)_"
    return (
        f"# {symbol} — atlas dossier (Q17, generated {TODAY})\n\n"
        f"- **Level reached:** **{highest}** (N0 → N7 ladder; N6 = primary-feature ML, N7 = synthesis & preregistration of mature hypotheses)\n"
        f"- **Cutoff (exclusive):** `{CUTOFF}`\n"
        f"- **No holdout, no live, no paper, no order, no key, no new download.**\n\n"
        f"## Data coverage\n\n" + "\n".join(coverage_lines) + "\n\n"
        f"## Q-axes covering {symbol}\n\n" + qaxes_lines + "\n\n"
        f"## Level summary (most recent dated artefact per N-level)\n\n"
        f"| level | status | path |\n|---|---|---|\n" + "\n".join(rows) + "\n\n"
        f"## Panel / cross-asset artefacts (filtered)\n\n"
        + ("\n".join(f"- `{p}`" for p in panel_links) if panel_links else "- _(none)_") + "\n\n"
        f"## Conclusion\n\n"
        f"See `research/MAP.md` and `research/BACKLOG.md` for the per-level verdict on {symbol}. "
        f"At the close of the klines-1m pre-cutoff block (Q1–Q16), no primary feature survived the joint filter; the desk has no ledger hypothesis on {symbol}.\n"
    )


def run() -> None:
    for symbol in SYMBOLS:
        path = ASSETS / f"{symbol.lower()}-dossier.md"
        path.write_text(_one(symbol), encoding="utf-8")


def main() -> None:
    run()


if __name__ == "__main__":
    main()
