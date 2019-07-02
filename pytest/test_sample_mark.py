import pytest


@pytest.mark.set1
def test_add1():
    x = 5
    y = 5
    assert x == y, "should pass"


@pytest.mark.set2
def test_add2():
    x = 6
    y = 5
    assert x == y, "should fail"
