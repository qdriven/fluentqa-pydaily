#!/usr/bin/env python
# -*- coding:utf-8 -*-
import abc
import dataclasses

from pydaily import inject, di

di["a"] = 1
di["b"] = "test"
di["c"] = 2
di["d"] = "test_2"
di["message"] = "Hello, Tom"


class Interface(abc.ABC):
    ...


@inject(alias=Interface)
class ConcreteA(Interface):
    ...


@inject(alias=Interface)
class ConcreteB(Interface):
    ...


@inject(alias=Interface)
class ConcreteC(Interface):
    ...


@inject()
class UseAllInterface:
    def __init__(self, concretes: list[Interface]):
        self.concretes = concretes


@inject
def inject_test(a: int, b: str):
    return {"a": a, "b": b}


@inject()
@dataclasses.dataclass
class A:
    message: str


def test_can_inject_values_to_function() -> None:
    assert inject_test() == {"a": 1, "b": "test"}


def test_can_override_injected_values() -> None:
    assert inject_test(12) == {"a": 12, "b": "test"}
    assert inject_test(b="test_2") == {"a": 1, "b": "test_2"}
    assert inject_test(12, "test_2") == {"a": 12, "b": "test_2"}
    assert inject_test() == {"a": 1, "b": "test"}


def test_can_do_constructor_injection() -> None:
    instance = A()
    assert instance.message == "Hello, Tom"
    instance = A("Hello, Jack")
    assert instance.message == "Hello, Jack"


def test_di() -> None:
    instance = di[UseAllInterface]
    assert len(instance.concretes) == 3
    assert instance.concretes[0] == di[ConcreteA]
    assert instance.concretes[1] == di[ConcreteB]
    assert instance.concretes[2] == di[ConcreteC]
