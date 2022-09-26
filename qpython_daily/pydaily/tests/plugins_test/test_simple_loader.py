#!/usr/bin/env python
# -*- coding:utf-8 -*-
import inspect
import os.path
import pkgutil

from qpython_daily.plugins.models import SimplePlugin

PLUGIN_BASE_PATH = os.path.dirname(__file__).replace("tests/plugins_test", "")
print(PLUGIN_BASE_PATH)


def test_walk_package():
    imported_package = __import__("plugins.demo.t1_plugin")
    for _, pluginname, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
        if not ispkg:
            plugin_module = __import__(pluginname, fromlist=['blah'])
            clsmembers = inspect.getmembers(plugin_module, inspect.isclass)
            for (_, c) in clsmembers:
                # 仅加入Plugin类的子类，忽略掉Plugin本身
                if issubclass(c, SimplePlugin) and (c is not SimplePlugin):
                    print(f'    找到插件类: {c.__module__}.{c.__name__}')
