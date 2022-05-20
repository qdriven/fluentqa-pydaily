#!/usr/bin/env python
# -*- coding:utf-8 -*-
import inspect
from typing import Dict, Any

call_frame = inspect.stack()

print(call_frame[0])
print(dir(call_frame[0]))


def demo_func(a: str, b: Dict, c: Any):
    print(a, b, c)


