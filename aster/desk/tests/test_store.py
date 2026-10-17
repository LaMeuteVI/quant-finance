import pytest

from aster.data import store


def test_generic_store_rejects_sealed_paths(isolated_desk):
    with pytest.raises(ValueError, match="sealed holdout paths"):
        store.read("sealed", "market", "spot", "klines_1m")