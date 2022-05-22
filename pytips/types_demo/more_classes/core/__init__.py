#!/usr/bin/env python
# -*- coding:utf-8 -*-


__all__ = ["Singleton", "ThreadSingleton", "SingletonArgs", "ThreadSingletonArgs"]

from .singleton import SingletonMeta,ThreadSafeMixin,SingletonArgsMeta,ThreadSafeMixin


class Singleton(SingletonMeta):
    pass


class ThreadSingleton(ThreadSafeMixin, Singleton):
    pass


class SingletonArgs(SingletonArgsMeta):
    pass


class ThreadSingletonArgs(ThreadSafeMixin, SingletonArgs):
    pass
