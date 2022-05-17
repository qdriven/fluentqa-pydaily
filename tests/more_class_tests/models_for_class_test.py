#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pydaily.more_classes.core import ThreadSingleton, SingletonArgs, ThreadSingletonArgs
from pydaily.more_classes.singleton_demo import Singleton


class TSingletonBase():
    def __init__(self, arg1: str = '', arg2: str = '') -> None:
        self._param1: str = arg1
        self._param2: str = arg2

    @property
    def param1(self) -> str:
        return self._param1

    @param1.setter
    def param1(self, value: str):
        self._param1 = value

    @property
    def param2(self) -> str:
        return self._param2

    @param2.setter
    def param2(self, value: str):
        self._param2 = value


class TSingleton(TSingletonBase, metaclass=Singleton):
    pass


class TThreadSingleton(TSingletonBase, metaclass=ThreadSingleton):
    pass


class TSingletonArgs(TSingletonBase, metaclass=SingletonArgs):
    pass


class TSingletonArgsWithoutInit(metaclass=SingletonArgs):
    # no __init__ method in this class
    pass


class TThreadSingletonArgs(TSingletonBase, metaclass=ThreadSingletonArgs):
    pass
