"""Panel N0: descriptive liquidity/quality dossiers for the secondary universe.

Pre-cutoff only.  No signal, no hypothesis, no backtest.  Produces one report
per symbol (BNB, XRP, SOL, LINK, DOGE, XMR) and one combined comparison table.

Symbols are read from ``R2`` via the same immutable reader used for BTC/ETH.
XMR is kept as the only delisted survivor of the panel (its inclusion is the
guard against survivor bias in cross-sectional results).
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from aster.data.bars import normalise_clock
from aster.data.minute_quality import profile_frame
from aster.data.r2_klines import CUTOFF, read_local

SYMBOLS = ("BNBUSDT", "XRPUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT", "XMRUSDT")
ASSET_DIR = Path("research/assets")
COMPARISON_CSV = Path("research/assets/2026-10-14-panel-n0-comparison.csv")


@dataclass
class AssetPayload:
    symbol: str
    raw_rows: int
    coverage: float
    missing_minutes: int
    frozen_minutes: int
    frozen_share: float
    median_dollar_volume: float
    median_tradeful_dollar_volume: float
    median_trades: float
    median_tradeful_trades: float
    median_taker_buy_ratio: float
    first: str
    last: str

    def to_row(self) -> dict:
        return {
            "symbol": self.symbol,
            "raw_rows": self.raw_rows,
            "coverage": self.coverage,
            "missing_minutes": self.missing_minutes,
            "frozen_minutes": self.frozen_minutes,
            "frozen_share": self.frozen_share,
            "median_dollar_volume": self.median_dollar_volume,
            "median_tradeful_dollar_volume": self.median_tradeful_dollar_volume,
            "median_trades": self.median_trades,
            "median_tradeful_trades": self.median_tradeful_trades,
            "median_taker_buy_ratio": self.median_taker_buy_ratio,
            "first": self.first,
            "last": self.last,
        }


def hourly_profile(frame: pd.DataFrame) -> pd.DataFrame:
    index = pd.DatetimeIndex(frame.index)
    work = pd.DataFrame(index=index)
    work["dollar_volume"] = frame["quote_volume"].astype(float)
    work["trades"] = frame["trades"].astype(float)
    work["frozen"] = (frame["trades"] == 0).astype(float)
    volume = frame["volume"].to_numpy(dtype=float)
    taker_buy_base = frame["taker_buy_base"].to_numpy(dtype=float)
    ratio = np.full(len(frame), np.nan, dtype=float)
    np.divide(taker_buy_base, volume, out=ratio, where=volume > 0)
    work["taker_buy_ratio"] = ratio
    work["imbalance"] = 2.0 * work["taker_buy_ratio"] - 1.0
    grouped = work.groupby([index.dayofweek, index.hour])
    result = grouped.agg(
        minutes=("trades", "size"),
        median_dollar_volume=("dollar_volume", "median"),
        mean_dollar_volume=("dollar_volume", "mean"),
        median_trades=("trades", "median"),
        frozen_share=("frozen", "mean"),
        mean_taker_buy_ratio=("taker_buy_ratio", "mean"),
        imbalance_std=("imbalance", "std"),
    )
    result.index.names = ["weekday_utc", "hour_utc"]
    return result.sort_index()


def build_payload(symbol: str) -> tuple[AssetPayload, pd.DataFrame]:
    raw = read_local(symbol)
    repaired, clock = normalise_clock(raw)
    quality = profile_frame(symbol, raw, partitions=0)
    tradeful = repaired[repaired["trades"] > 0]
    payload = AssetPayload(
        symbol=symbol,
        raw_rows=int(len(raw)),
        coverage=float(quality.coverage),
        missing_minutes=int(quality.missing_minutes),
        frozen_minutes=int(quality.frozen_bars),
        frozen_share=float(quality.frozen_share),
        median_dollar_volume=float(repaired["quote_volume"].median()),
        median_tradeful_dollar_volume=float(tradeful["quote_volume"].median()),
        median_trades=float(repaired["trades"].median()),
        median_tradeful_trades=float(tradeful["trades"].median()),
        median_taker_buy_ratio=float((tradeful["taker_buy_base"] / tradeful["volume"]).median()),
        first=repaired.index.min().isoformat(),
        last=repaired.index.max().isoformat(),
    )
    profile = hourly_profile(repaired)
    return payload, profile


def write_per_asset_report(payload: AssetPayload, profile: pd.DataFrame) -> None:
    """Write the per-asset markdown dossier, only fields the payload contains."""
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    md_path = ASSET_DIR / f"2026-10-14-{payload.symbol.lower()}-n0.md"
    csv_path = ASSET_DIR / f"2026-10-14-{payload.symbol.lower()}-n0-hourly.csv"
    profile.to_csv(csv_path)

    def pct(x: float) -> str:
        return f"{x * 100:.3f}%"

    text = f"""# {payload.symbol} N0 — dossier de données et liquidité

**Statut : descriptif uniquement.** Aucun signal, aucune hypothèse et aucun backtest.

- Source : R2 local, klines spot Binance 1 minute ; le lecteur interdit toute observation >= `{CUTOFF.isoformat()}`.
- Échantillon : `{payload.first}` à `{payload.last}` ; `{payload.raw_rows:,}` minutes brutes.
- Couverture brute : `{pct(payload.coverage)}` ; `{payload.missing_minutes:,}` minutes absentes.
- Minutes sans trade : `{payload.frozen_minutes:,}` (`{pct(payload.frozen_share)}`).

## Activité observée

- Dollar-volume médian/minute : `${payload.median_dollar_volume:,.0f}` ; sur minutes avec trade : `${payload.median_tradeful_dollar_volume:,.0f}`.
- Trades médians/minute : `{payload.median_trades:,.0f}` ; tradeful : `{payload.median_tradeful_trades:,.0f}`.
- Ratio médian taker-buy (minutes avec trade) : `{payload.median_taker_buy_ratio:.4f}`. Matière première pour N5, **pas** un signal.

## Profil horaire

Le CSV `{csv_path.name}` contient les 168 seaux heure-de-semaine UTC. Aucun classement d'heures n'est publié : ce serait un test multiple.

## Décision N0

{payload.symbol} est utilisable pour les études descriptives ultérieures après réparation d'horloge tracée. N0 ne constitue pas une preuve d'alpha et ne déclenche aucun backtest. La liquidité médiane/minute sert au dimensionnement en AUM (capacité) des futures hypothèses.

## Reproduction

```bash
uv run python -m aster.research.panel_n0
```
"""
    md_path.write_text(text, encoding="utf-8")


def write_combined_report(payloads: list[AssetPayload]) -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    rows = [p.to_row() for p in payloads]
    df = pd.DataFrame(rows)
    df.to_csv(COMPARISON_CSV, index=False)

    table = "\n".join(
        f"| {p.symbol} | {p.raw_rows:,} | {p.coverage * 100:.3f}% | {p.frozen_share * 100:.3f}% | "
        f"${p.median_tradeful_dollar_volume:,.0f} | {p.median_tradeful_trades:,.0f} | "
        f"{p.median_taker_buy_ratio:.4f} |"
        for p in payloads
    )
    text = f"""# Panel N0 — comparatif liquidité (BNB, XRP, SOL, LINK, DOGE, XMR)

**Statut : descriptif uniquement.** Cutoff `{CUTOFF.isoformat()}` (XMR délisté garde-fou survivant).

| Symbole | Minutes | Couverture | Frozen % | DV médian tradeful ($) | Trades médian | Taker-buy ratio |
|---|---|---|---|---|---|---|
{table}

Les valeurs sont les médianes sur minutes avec trade, sans agrégation horaire : le DV médian tradeful est ce qui dimensionne la capacité (Almgren-Chriss, racine carrée). Aucune hypothèse n'est enregistrée. CSV reproductible : `{COMPARISON_CSV.name}`.
"""
    out = ASSET_DIR / "2026-10-14-panel-n0.md"
    out.write_text(text, encoding="utf-8")


def main() -> int:
    payloads: list[AssetPayload] = []
    for symbol in SYMBOLS:
        payload, profile = build_payload(symbol)
        write_per_asset_report(payload, profile)
        payloads.append(payload)
        print(json.dumps(payload.to_row(), sort_keys=True))
    write_combined_report(payloads)
    print(f"wrote {COMPARISON_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
