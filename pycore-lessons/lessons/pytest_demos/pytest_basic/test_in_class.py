#!/usr/bin/env python
# -*- coding:utf-8 -*-

class TestDemoForTestInClass:
    value = 0 ## class level attributes
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        print(hasattr(x,"format"))
        assert hasattr(x, "format")

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        print("current value is ",self.value)
        assert self.value == 1