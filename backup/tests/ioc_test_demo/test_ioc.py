#!/usr/bin/env python
# -*- coding:utf-8 -*-
from injector import Injector

from backup.pytips.patterns.ioc_demo.modules import ServiceClass, ServiceDataClassDemo, RepoClass


class TestIoCDemo:

    def setup(self):
        self.container = Injector()
        self.service = self.container.get(ServiceClass)
        self.service_2 = self.container.get(ServiceDataClassDemo)

    def test_injection(self):
        self.service.serve_you()
        self.service_2.serve_you()

    def test_not_in_injection(self):
        repo = self.container.get(RepoClass)
        print(repo)