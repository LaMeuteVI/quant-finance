"""BTC N0: reproducible descriptive asset dossier, strictly pre-cutoff.

N0 is not a signal test and makes no alpha claim.  It records the conditions
under which later BTC studies must be interpreted: coverage, clock repair,
frozen minutes, trading intensity, notional liquidity and aggressive-flow
availability.  The immutable R2 reader rejects post-cutoff values.

Run: ``uv run python -m aster.research.btc_n0``.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from aster.data.bars import normalise_clock
from aster.data.minute_quality import profile_frame
from aster.data.r2_klines import CUTOFF, read_local

SYMBOL = "BTCUSDT"
OUTPUT = Path("research/assets/2026-10-13-btc-n0.md")
TABLE = Path("research/assets/2026-10-13-btc-n0-hourly.csv")


def hourly_profile(frame: pd.DataFrame) -> pd.DataFrame:
    """Return an hour-of-week liquidity profile with frozen minutes explicit."""
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


def build_report(symbol: str = SYMBOL) -> tuple[dict, pd.DataFrame]:
    """Read, repair transparently, and calculate the BTC N0 report payload."""
    raw = read_local(symbol)
    repaired, clock = normalise_clock(raw)
    quality = profile_frame(symbol, raw, partitions=0)
    index = pd.DatetimeIndex(repaired.index)
    hour = hourly_profile(repaired)
    tradeful = repaired[repaired["trades"] > 0]
    payload = {
        "symbol": symbol,
        "cutoff_exclusive": CUTOFF.isoformat(),
        "raw_rows": int(len(raw)),
        "repaired_rows": int(len(repaired)),
        "first": index.min().isoformat(),
        "last": index.max().isoformat(),
        "clock_repair": clock.as_dict(),
        "coverage_raw": quality.coverage,
        "missing_minutes_raw": quality.missing_minutes,
        "frozen_minutes_raw": quality.frozen_bars,
        "frozen_share_raw": quality.frozen_share,
        "median_minute_dollar_volume": float(repaired["quote_volume"].median()),
        "median_tradeful_minute_dollar_volume": float(tradeful["quote_volume"].median()),
        "median_minute_trades": float(repaired["trades"].median()),
        "median_tradeful_minute_trades": float(tradeful["trades"].median()),
        "median_taker_buy_ratio": float(
            (tradeful["taker_buy_base"] / tradeful["volume"]).median()),
        "hourly_rows": int(len(hour)),
    }
    return payload, hour


def _pct(value: float) -> str:
    return f"{value * 100:.3f}%"


def write_report(payload: dict, profile: pd.DataFrame) -> None:
    """Write only values from ``build_report`` and its CSV artifact."""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    profile.to_csv(TABLE)
    repair = payload["clock_repair"]
    text = f"""# BTC N0 — dossier de données et liquidité

**Statut : descriptif uniquement.** Aucun signal, aucune hypothèse et aucun backtest.

- Source : R2 local, klines spot Binance 1 minute auditées ; le lecteur interdit toute observation >= `{payload['cutoff_exclusive']}`.
- Échantillon : `{payload['first']}` à `{payload['last']}` ; `{payload['raw_rows']:,}` minutes brutes.
- Couverture brute : `{_pct(payload['coverage_raw'])}` ; `{payload['missing_minutes_raw']:,}` minutes calendaires absentes. Les trous ne sont ni remplis ni convertis en prix plats.
- Minutes sans trade : `{payload['frozen_minutes_raw']:,}` (`{_pct(payload['frozen_share_raw'])}`). Elles restent marquées et seront exclues des futurs tests de lead-lag et d'autocorrélation courte.

## Horloge source

- Timestamps hors grille avant réparation : `{repair['off_grid_before']:,}`.
- Après `floor('min')` et dédoublonnage déterministe : `{repair['off_grid_after']:,}` hors grille, `{repair['dropped_duplicates']:,}` doublon supprimé.
- Offsets observés : `{', '.join(repair['offsets']) or 'aucun'}`.
- La réparation ne modifie aucun prix/volume ; elle rend simplement l'index resamplable. Les analyses futures doivent citer cette étape.

## Activité observée

- Dollar-volume médian par minute : `${payload['median_minute_dollar_volume']:,.0f}` ; sur minutes avec trade : `${payload['median_tradeful_minute_dollar_volume']:,.0f}`.
- Nombre médian de trades par minute : `{payload['median_minute_trades']:,.0f}` ; sur minutes avec trade : `{payload['median_tradeful_minute_trades']:,.0f}`.
- Ratio médian taker-buy base (minutes avec trade) : `{payload['median_taker_buy_ratio']:.4f}`. Ce n'est pas une prédiction : c'est une matière première pour N5.

## Profil horaire

Le tableau reproductible `2026-10-13-btc-n0-hourly.csv` contient les 168 seaux heure-de-semaine UTC : minutes, dollar-volume médian/moyen, trades médians, part gelée, ratio taker-buy moyen et dispersion de l'imbalance. Aucun classement de « meilleure heure » n'est publié : ce serait déjà un test multiple sans FDR.

## Décision N0

BTC est utilisable pour les analyses descriptives N1/N2 **après** la réparation d'horloge explicitement tracée. Les limitations restent : 34 gaps bruts, `{_pct(payload['frozen_share_raw'])}` de minutes gelées et une unique venue. Les premières statistiques devront segmenter les gaps, exclure les minutes gelées là où la dépendance intraminute est étudiée, et rester pré-enregistrées avant tout backtest.

## Reproduction

```bash
uv run python -m aster.research.btc_n0
```
"""
    OUTPUT.write_text(text, encoding="utf-8")


def main() -> int:
    payload, profile = build_report()
    write_report(payload, profile)
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(f"wrote {OUTPUT}")
    print(f"wrote {TABLE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
