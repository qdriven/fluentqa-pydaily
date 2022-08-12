import pytest


def inc(x):
    return x + 1


@pytest.mark.serial
def test_inc_correct():
    assert inc(3) == 4


@pytest.mark.slow
def test_inc_failed():
    assert inc(4) != 6

@pytest.mark.slowest
def test_slowest_case():
    print("slowest cases")
    assert 1