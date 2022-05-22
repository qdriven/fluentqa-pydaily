#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pytips.patterns.factory_pattern.factory_meta import FactoryMeta


class ClassWithFactoryPattern(metaclass=FactoryMeta):
    def __init__(self, arg: str) -> None:
        print("__init__ in class")
        self.__arg: str = arg

    @property
    def arg(self) -> str:
        return self.__arg

    @classmethod
    def create_cls(cls, arg: str) -> "ClassWithFactoryPattern":
        print("in create class method")
        return ClassWithFactoryPattern(arg)


class NormalClass():
    pass


normal_clz = NormalClass()

try:
    clz_factory = ClassWithFactoryPattern()  ## error
except Exception as e:
    print(e)
    clz_factory = ClassWithFactoryPattern.create_cls(ClassWithFactoryPattern)
    print(clz_factory)
