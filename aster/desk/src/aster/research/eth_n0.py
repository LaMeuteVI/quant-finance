"""ETH N0: reproducible descriptive asset dossier, strictly pre-cutoff.

This is a quality/liquidity report only.  It makes no alpha claim and never
reads post-cutoff market data.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from aster.data.bars import normalise_clock
from aster.data.minute_quality import profile_frame
from aster.data.r2_klines import CUTOFF, read_local

SYMBOL = "ETHUSDT"
OUTPUT = Path("research/assets/2026-10-14-eth-n0.md")
TABLE = Path("research/assets/2026-10-14-eth-n0-hourly.csv")


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
        minutes=("trades", "size"), median_dollar_volume=("dollar_volume", "median"),
        mean_dollar_volume=("dollar_volume", "mean"), median_trades=("trades", "median"),
        frozen_share=("frozen", "mean"), mean_taker_buy_ratio=("taker_buy_ratio", "mean"),
        imbalance_std=("imbalance", "std"),
    )
    result.index.names = ["weekday_utc", "hour_utc"]
    return result.sort_index()


def build_report() -> tuple[dict, pd.DataFrame]:
    raw = read_local(SYMBOL)
    repaired, clock = normalise_clock(raw)
    quality = profile_frame(SYMBOL, raw, partitions=0)
    hourly = hourly_profile(repaired)
    tradeful = repaired[repaired["trades"] > 0]
    ratio = tradeful["taker_buy_base"] / tradeful["volume"]
    payload = {
        "symbol": SYMBOL, "cutoff_exclusive": CUTOFF.isoformat(), "raw_rows": int(len(raw)),
        "repaired_rows": int(len(repaired)), "first": repaired.index.min().isoformat(),
        "last": repaired.index.max().isoformat(), "clock_repair": clock.as_dict(),
        "coverage_raw": quality.coverage, "missing_minutes_raw": quality.missing_minutes,
        "frozen_minutes_raw": quality.frozen_bars, "frozen_share_raw": quality.frozen_share,
        "median_minute_dollar_volume": float(repaired["quote_volume"].median()),
        "median_tradeful_minute_dollar_volume": float(tradeful["quote_volume"].median()),
        "median_minute_trades": float(repaired["trades"].median()),
        "median_tradeful_minute_trades": float(tradeful["trades"].median()),
        "median_taker_buy_ratio": float(ratio.median()), "hourly_rows": int(len(hourly)),
    }
    return payload, hourly


def _pct(value: float) -> str:
    return f"{value * 100:.3f}%"


def write_report(payload: dict, profile: pd.DataFrame) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    profile.to_csv(TABLE)
    repair = payload["clock_repair"]
    text = f"""# ETH N0 — dossier de données et liquidité

**Statut : descriptif uniquement.** Aucun signal, aucune hypothèse et aucun backtest.

- Source : R2 local, klines spot Binance 1 minute ; le lecteur interdit toute observation >= `{payload['cutoff_exclusive']}`.
- Échantillon : `{payload['first']}` à `{payload['last']}` ; `{payload['raw_rows']:,}` minutes brutes.
- Couverture brute : `{_pct(payload['coverage_raw'])}` ; `{payload['missing_minutes_raw']:,}` minutes absentes.
- Minutes sans trade : `{payload['frozen_minutes_raw']:,}` (`{_pct(payload['frozen_share_raw'])}`). Elles restent marquées et ne sont pas transformées en prix plats.

## Horloge source

- Timestamps hors grille avant réparation : `{repair['off_grid_before']:,}`.
- Après `floor('min')` et dédoublonnage : `{repair['off_grid_after']:,}` hors grille, `{repair['dropped_duplicates']:,}` doublon supprimé.
- Offsets observés : `{', '.join(repair['offsets']) or 'aucun'}`.

## Activité observée

- Dollar-volume médian/minute : `${payload['median_minute_dollar_volume']:,.0f}` ; tradeful : `${payload['median_tradeful_minute_dollar_volume']:,.0f}`.
- Trades médians/minute : `{payload['median_minute_trades']:,.0f}` ; tradeful : `{payload['median_tradeful_minute_trades']:,.0f}`.
- Ratio médian taker-buy : `{payload['median_taker_buy_ratio']:.4f}`.

Le profil reproductible `2026-10-14-eth-n0-hourly.csv` contient les 168 seaux heure-de-semaine UTC. Aucun classement d'heures n'est publié à ce stade : ce serait un test multiple.

## Décision N0

ETH est utilisable pour les études descriptives suivantes après réparation d'horloge explicitement tracée. N0 ne constitue pas une preuve d'alpha et ne déclenche aucun backtest.

Reproduction : `uv run python -m aster.research.eth_n0`
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
