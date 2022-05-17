#!/usr/bin/env python
# -*- coding:utf-8 -*-
import importlib as imp

import module_class_demo as mod

## static load a module from import
demo = mod.DemoClass()
demo.hello_world()


## dynamic import
def dynamic_import(name: str, class_name: str):
    fp, path, desc = imp.import_module(name=name)
