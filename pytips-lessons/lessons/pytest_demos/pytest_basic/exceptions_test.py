#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


def err_raise():
    raise SystemExit(1)


def test_err_raise():
    with pytest.raises(SystemExit):
        err_raise()
