#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pytips.patterns.decorators.container import service


class BaseService:
    @classmethod
    def instance(cls, **kwargs):
        print(type(cls))
        return cls(**kwargs)


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
