#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


class MyPlugins:

    def pytest_sessionfinish(self):
        print("it is done")

    def plugins(self):
        return {"my_plugin": self}


class PytestRunner:

    def run(self, *args, **kwargs):
        ret_code = pytest.main(
            *args, plugins=[kwargs["plugins"]]
        )
        print(ret_code)


if __name__ == '__main__':
    runner = PytestRunner()
    plugins = MyPlugins().plugins()
    runner.run(["pytest_basic/test_sample_01.py"]
               , plugins=plugins["my_plugin"])
