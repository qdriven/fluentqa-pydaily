#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


def f():
    return 3


def test_function():
    assert f() == 4

def test_odd():
    a=4
    assert a % 2 == 0, "value was odd, should be even"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)

def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()

@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()

def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2