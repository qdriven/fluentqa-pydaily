#!/usr/bin/env python
# -*- coding:utf-8 -*-
from decorators.base_service import ServiceDemo
from backup.pytips.patterns.decorators.container import service

result = service.get(ServiceDemo)
result.create_resources()

