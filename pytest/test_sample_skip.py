import pytest


def test_add1():
    assert 6+6 == 12


@pytest.mark.skip
def test_add2():
    assert 6+7 == 10


@pytest.mark.xfail
def test_add3():
    assert 8+6 == 12


@pytest.mark.skip
def test_add4():
    assert 6+6 == 13


def test_add5():
    assert 6+6 == 12
