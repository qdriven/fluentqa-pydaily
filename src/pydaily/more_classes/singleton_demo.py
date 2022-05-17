#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)

# <__main__.Singleton object at 0x106db39d0>
# <__main__.Singleton object at 0x106db39d0>