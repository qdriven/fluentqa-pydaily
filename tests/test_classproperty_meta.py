#!/usr/bin/env python
# -*- coding:utf-8 -*-
import dataclasses
from typing import Any
from pytips.types_demo.classproperty_demo import ClassProperty, ClassPropertyMeta
from pytips.types_demo.classproperty_demo import clsproperty


@dataclasses.dataclass
class DemoClass:
    name: str
    data: Any


class TestClass(metaclass=ClassPropertyMeta):
    _ro_attr: str = "read-only"
    _rw_attr: str = "change_me"

    @clsproperty
    def ro_attr(cls) -> str:
        return cls._ro_attr

    @clsproperty
    def rw_attr(cls) -> str:
        return cls._rw_attr

    @rw_attr.setter
    def rw_attr(cls, value) -> None:
        cls._rw_attr = value

    @rw_attr.deleter
    def rw_attr(cls) -> None:
        del cls._rw_attr


def test__classproperty():
    result = ClassProperty.get_class(DemoClass)
    instance_result = ClassProperty.get_class(DemoClass("test", "data"))
    print(result, instance_result)
    assert result == instance_result


class TestTestCase:

    def setup(self):
        pass
    def test_attr(self):
        t: TestClass = TestClass()
        assert t.rw_attr == "change_me"
