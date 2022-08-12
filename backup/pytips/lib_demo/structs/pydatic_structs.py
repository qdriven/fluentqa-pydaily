#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pydantic.dataclasses import dataclass
import typing

from backup.pytips.lib_demo.structs import class_tester


@dataclass
class Data:
    x: float = None
    y: float = None
    kwargs: typing.Dict = None

class_tester(Data)

test_data_point = Data(x='123')
print(test_data_point)
Data(x='t')