#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import wraps


class UpperAttrMetaClass(type):
    def __new__(mcs, name, bases, attrs):
        print("new here")
        mcs.org_attrs = attrs
        new_attrs = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(mcs, name, bases, new_attrs)


class UserDemo(object):
    __metaclass__ = UpperAttrMetaClass
    name = "sunny"


def return_self(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        func(self, *args, **kwargs)
        return self

    return wrapped


class ReturnSelfMeta(type):

    def __new__(mcs, name, bases, attrs):  # noqa
        cls = super(ReturnSelfMeta, mcs).__new__(mcs, name, bases, attrs)

        methods = cls.__methods_return_self__
        for method in methods:
            origin = getattr(cls, method)
            setattr(cls, method, return_self(origin))
        return cls


if __name__ == '__main__':
    print(UserDemo().name)
