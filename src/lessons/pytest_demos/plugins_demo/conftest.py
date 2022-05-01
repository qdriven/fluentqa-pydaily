#!/usr/bin/env python
# -*- coding:utf-8 -*-

def pytest_runtest_setup(item):
    print("setting up ",item)
    print(type(item))
