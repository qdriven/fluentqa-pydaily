#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from types import FrameType
from typing import List, Callable, Any, Type, Optional


class _FactoryMeta(type):
    # hashed methods list
    __classmethods: List[int] = []

    def __init__(cls, name: str, bases: tuple, attr: dict) -> None:
        print("in meta __init__ method")
        super(_FactoryMeta, cls).__init__(name, bases, attr)
        # iterate over the attributes of this class
        for attr_name, attribute in attr.items():
            # add all classmethods to a list
            # only these methods can create instances of the class that uses this meta class
            if isinstance(attribute, classmethod):
                cls_method: Callable[..., Any] = getattr(cls, attr_name)
                # add the hash to the classmethod list
                cls.__classmethods.append(hash(cls_method))

    def __call__(cls, *args, **kwargs) -> Type:
        frame: Optional[FrameType] = sys._getframe().f_back
        if frame is not None:
            name: str = frame.f_code.co_name
        else:
            # this should not happen
            raise _FactoryException(cls)
        func: Callable[..., Any] = getattr(cls, name, None)
        # and the hash must be in the classmethods list
        if hash(func) not in cls.__classmethods:
            # if not, the class was instantiated from outside of the class
            # so raise an exception here
            raise _FactoryException(cls)

        # continue if everything is alright
        return type.__call__(cls, *args, **kwargs)


class _FactoryException(Exception):
    def __init__(self, factory_cls: type) -> None:
        # check if the provided class uses the factory pattern meta class
        if not issubclass(type(factory_cls), _FactoryMeta):
            raise ValueError("The class '%s' must have 'FactoryMeta' as its meta class!" % factory_cls.__name__)

        super(_FactoryException, self).__init__("The class '%s' can't be instantiated directly!" % factory_cls.__name__)


FactoryException = _FactoryException


class FactoryMeta(_FactoryMeta):
    pass


__all__ = ["FactoryMeta", "FactoryException"]
