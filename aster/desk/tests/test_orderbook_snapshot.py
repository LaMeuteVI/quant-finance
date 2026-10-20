"""Tests for public operational order-book snapshots."""
from __future__ import annotations

import pytest

from aster.data.orderbook_snapshot import quote_spread_bps


def test_quote_spread_bps_manual_reference():
    # bid=100, ask=100.02 -> 0.02 / 100.01 * 1e4 = 1.9998 bps.
    assert quote_spread_bps(100.0, 100.02) == pytest.approx(1.99980002)


def test_quote_spread_bps_zero_for_a_locked_book():
    assert quote_spread_bps(100.0, 100.0) == 0.0


@pytest.mark.parametrize("bid,ask", [(0.0, 1.0), (1.0, 0.0), (101.0, 100.0)])
def test_quote_spread_rejects_an_invalid_book(bid, ask):
    with pytest.raises(ValueError, match="invalid"):
        quote_spread_bps(bid, ask)
