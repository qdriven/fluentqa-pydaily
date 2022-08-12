#!/usr/bin/env python
# -*- coding:utf-8 -*-
from backup.pytips.patterns.ioc_demo.simpleioc.con_service_1 import DiService

# sdk.get(type(DiService)).action1()
from backup.pytips.patterns.ioc_demo.simpleioc.di import sdk

sdk.get(DiService).action_1()
sdk["diservice"].action_2()
