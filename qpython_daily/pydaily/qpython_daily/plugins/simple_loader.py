#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SimplePluginLoader:

    def __init__(self, plugin_package):
        self.plugin_package = plugin_package
        self.reload_plugins()

    def reload_plugins(self):
        self.plugins = []
        self.seen_paths = []
        print(f"在 {self.plugin_package} 包里查找插件")
        self.walk_package(self.plugin_package)

    def walk_package(self, plugin_package):
        imported_package = __import__(plugin_package, fromlist=['blah'])



