#!/usr/bin/env python
# -*- coding:utf-8 -*-
import inspect
from typing import Dict, Any

call_frame = inspect.stack()

print(call_frame[0])
print(dir(call_frame[0]))


def demo_func(a: str, b: Dict, c: Any):
    print(a, b, c)


result = inspect.getfullargspec(demo_func)

print(result.args)
print(result.annotations)


class ClassForInspect:

    def __init__(self, **kwargs):
        print(kwargs)


class_result = inspect.classify_class_attrs(ClassForInspect)
print(class_result)
