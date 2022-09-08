#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

print(os.environ.get("test"))
os.environ.setdefault("test","test_value")
assert os.environ.get("test")=="test_value"
os.environ.clear()
