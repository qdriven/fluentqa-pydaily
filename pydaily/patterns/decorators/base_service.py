#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pydaily.patterns.container import service


class BaseService:
    @classmethod
    def instance(cls):
        return cls()


@service.service
class ServiceDemo(BaseService):
    def create_resources(self):
        print("print results")

    def update_resources(self):
        print("update result")

    def delete_resources(self):
        print("delete results")

    def post_resources(self):
        print("delete results")
