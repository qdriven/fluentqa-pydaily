#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typing

from backup.pytips.lib_demo.structs import class_tester


class DemoStuct:
    def __init__(self, x: float = None, y: float = None, kwargs: typing.Dict = None):
        self.x = x
        self.y = y
        self.kwargs = kwargs


class_tester(DemoStuct)
