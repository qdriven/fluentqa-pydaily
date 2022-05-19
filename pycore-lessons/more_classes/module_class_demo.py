#!/usr/bin/env python
# -*- coding:utf-8 -*-

class DemoClass(object):

    # def __getnewargs__(self):
    #     print(dir(self))
    # def __new__(cls, *args, **kwargs):
    #     print(*args, **kwargs)
    #     print("create class")
    #     cls.__new__(DemoClass, *args, **kwargs)

    def __init__(self):
        print("init class")
        self.field = "default"

    def hello_world(self):
        print("hello world!")

    def __private_method_call(self):
        print("private method class")

    def __call__(self, *args, **kwargs):
        print("callable")
        print(*args, **kwargs)

    def __enter__(self):
        print("enter class")

    #
    # def __getattr__(self, item):
    #     return getattr(self, item)
    #
    # def __setattr__(self, key, value):
    #     setattr(self, key, value)
