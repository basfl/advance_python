import pytest


@pytest.fixture
def supply_data():
    return["NYC", "DC", "SYZ"]


def test_compare(supply_data):
    assert supply_data[0] == "NYC", "should pass"
