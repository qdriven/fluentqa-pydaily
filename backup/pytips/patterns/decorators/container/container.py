#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any

from box import Box


class ServiceRegister:

    def __init__(self):
        self._services: Box = Box()

    def all_services(self):
        return self._services

    def register(self, s):
        self._services[s.__name__] = s.instance()
        return s

    def service(self, s):
        print(s)
        self._services[s.__name__.upper()] = s.instance()
        return s

    def get(self, type) -> Any:
        return self._services[type.__name__.upper()]

    def __getattr__(self, item):
        return self._services.get(item.upper())
# <pydaily.patterns.container.container.ServiceRegister object at 0x105291c00>
# <container.contrainer.ServiceRegister object at 0x104f68b20>
