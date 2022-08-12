#!/usr/bin/env python
# -*- coding:utf-8 -*-
from backup.pytips.patterns.ioc_demo.simpleioc.di import sdk, BaseDiService, ClassFactory


@sdk.register
class DiService(BaseDiService, ClassFactory):

    def action_1(self):
        print("action-1")

    def action_2(self):
        print("action-1")

    def action_3(self):
        print("action-1")
