#!/usr/bin/env python
# -*- coding:utf-8 -*-
from spell.ioc import ioc


def test_container():
    ioc["default"] = "test"
    assert ioc["default"] == "test"
