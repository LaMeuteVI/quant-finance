"""Strategy registry. Add a strategy: one file, one class, one line here."""

from aster.strategies.base import Strategy
from aster.strategies.tsmom import TSMom
from aster.strategies.btc_daily_tsmom_60 import BTCDailyTSMom60

REGISTRY: dict[str, type[Strategy]] = {
    TSMom.name: TSMom,
    BTCDailyTSMom60.name: BTCDailyTSMom60,
}


def get(name: str) -> type[Strategy]:
    if name not in REGISTRY:
        raise KeyError(f"unknown strategy {name}; known: {sorted(REGISTRY)}")
    return REGISTRY[name]
