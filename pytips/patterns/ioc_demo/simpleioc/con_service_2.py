#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pytips.patterns.ioc_demo.simpleioc.di import sdk, BaseDiService, ClassFactory


@sdk.register
class ManualService(BaseDiService,ClassFactory):

    def action_1(self):
        print("action-1")

    def action_2(self):
        print("action-1")

    def action_3(self):
        print("action-1")
