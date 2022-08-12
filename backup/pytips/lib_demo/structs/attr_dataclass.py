#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typing

import attr

from backup.pytips.lib_demo.structs import class_tester


@attr.s
class DataAttrDataClass:
    x: float = attr.ib(default=None)
    y: float = attr.ib(default=None)
    kwargs: typing.Dict = attr.ib(default=None)


class_tester(DataAttrDataClass)


@attr.s
class ValidatedData:
    x: float = attr.ib(default=None, validator=attr.validators.instance_of(int))
    y: float = attr.ib(default=None)
    kwargs: typing.Dict = attr.ib(default=None)

    @x.validator
    def more_than_the_meaning_of_life(self, attribute, value):
        if not value >= 42:
            raise ValueError("Must be more than the meaning of life!")


test_data_point_1 = ValidatedData(42)

test_data_point_2 = ValidatedData(-35)

import attr


@attr.s
class ConvertedData:
    x: float = attr.ib(default=None, converter=int)
    y: float = attr.ib(default=None)
    kwargs: typing.Dict = attr.ib(default=None)

    @x.validator
    def more_than_the_meaning_of_life(self, attribute, value):
        if not value >= 42:
            raise ValueError("Must be more than the meaning of life!")


test_data_point_1 = ConvertedData(42)

print(test_data_point_1)

test_data_point_2 = ConvertedData("42")

print(test_data_point_2)

ProgrammaticData = attr.make_class("Data",
                            {'x': attr.ib(default=None),
                            'y': attr.ib(default=None),
                            'kwargs': attr.ib(default=None)}
                            )

print(Data())
print(ProgrammaticData())