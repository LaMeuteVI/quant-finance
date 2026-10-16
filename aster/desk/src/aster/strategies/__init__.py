"""Strategy registry. Add a strategy: one file, one class, one line here."""

from aster.strategies.base import Strategy
from aster.strategies.tsmom import TSMom
from aster.strategies.btc_daily_tsmom_60 import BTCDailyTSMom60
from aster.strategies.funding_carry_dn import FundingCarryDN

REGISTRY: dict[str, type[Strategy]] = {
    TSMom.name: TSMom,
    BTCDailyTSMom60.name: BTCDailyTSMom60,
    FundingCarryDN.name: FundingCarryDN,
}


def get(name: str) -> type[Strategy]:
    if name not in REGISTRY:
        raise KeyError(f"unknown strategy {name}; known: {sorted(REGISTRY)}")
    return REGISTRY[name]
