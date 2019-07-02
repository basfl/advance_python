import pytest


def test_add1():
    x = 5
    y = 5
    assert x == y, "should pass"


def test_add2():
    x = 6
    y = 5
    assert x == y, "should fail"
