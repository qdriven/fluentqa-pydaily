#!/usr/bin/env python
# -*- coding:utf-8 -*-
from injector import inject, Injector
from db_request import DatabaseModule, config_binding, DbRequestHandler
from modules import ServiceClass
injector = Injector([config_binding, DatabaseModule()])
handler = injector.get(DbRequestHandler)
result = tuple(map(str, handler.get()[0]))
print(result)

injector.get(ServiceClass).serve_you()
