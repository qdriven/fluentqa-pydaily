#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Basic
class metaType(object):
    """
    type(object) -> the object's type
    type(name, bases, dict) -> a new type
    """

    def __init__(cls, what, bases=None, dict=None):  # known special case of type.__init__
        """
        type(object) -> the object's type
        type(name, bases, dict) -> a new type
        # (copied from class doc)
        """
        print(cls)
        print(what)
        print(bases)
        print(dict)


class A:
    def __init__(self):
        self.a = "a"


class B:
    def __init__(self):
        self.b = "b"


AB = metaType('AB', (A, B), {'ab': None})

print(AB())
