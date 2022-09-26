#!/usr/bin/env python
# -*- coding:utf-8 -*-
from qpython_daily.plugins.models import SimplePlugin


class T1Plugin(SimplePlugin):

    def __init__(self):
        super().__init__()

    def perform(self, argument):
        print(argument)
