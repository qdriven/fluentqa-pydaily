#!/usr/bin/env python
# -*- coding:utf-8 -*-
import inspect

call_frame = inspect.stack()

print(call_frame[0])
print(dir(call_frame[0]))