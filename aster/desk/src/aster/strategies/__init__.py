"""Strategy registry. Add a strategy: one file, one class, one line here."""

from aster.strategies.base import Strategy
from aster.strategies.tsmom import TSMom
from aster.strategies.btc_daily_tsmom_60 import BTCDailyTSMom60
from aster.strategies.funding_carry_dn import FundingCarryDN
from aster.strategies.xs_funding_carry import XSFundingCarry
from aster.strategies.intraday_signed_flow import IntradaySignedFlow
from aster.strategies.crowding_premium import CrowdingPremium
from aster.strategies.vol_target_trend_ensemble import VolTargetTrendEnsemble
from aster.strategies.capital_allocator import CapitalAllocator

REGISTRY: dict[str, type[Strategy]] = {
    TSMom.name: TSMom,
    BTCDailyTSMom60.name: BTCDailyTSMom60,
    FundingCarryDN.name: FundingCarryDN,
    XSFundingCarry.name: XSFundingCarry,
    IntradaySignedFlow.name: IntradaySignedFlow,
    CrowdingPremium.name: CrowdingPremium,
    VolTargetTrendEnsemble.name: VolTargetTrendEnsemble,
    CapitalAllocator.name: CapitalAllocator,
}


def get(name: str) -> type[Strategy]:
    if name not in REGISTRY:
        raise KeyError(f"unknown strategy {name}; known: {sorted(REGISTRY)}")
    return REGISTRY[name]
