#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tests.more_class_tests.models_for_class_test import TSingletonArgs


class TestSingleton:

    def setup(self):
        print("start setup!")
        TSingletonArgs._instances.clear()  # noqa
        TSingletonArgsWithoutInit._instances.clear()  # noqa

    def test_with_same_args(self):
        arg1: str = "arg1"
        instance1: TSingletonArgs = TSingletonArgs(arg1)
        instance2: TSingletonArgs = TSingletonArgs(arg1)

        # the instances must be equal
        self.assertEqual(instance1, instance2)
        self.assertEqual(instance1.param1, instance2.param1)
        self.assertEqual(arg1, instance1.param1)