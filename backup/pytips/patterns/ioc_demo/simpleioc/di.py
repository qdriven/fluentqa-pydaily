#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import Dict, Any


class ClassFactory:

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)


class Container:
    cls_dic: Dict[type, Any]
    named_dic: Dict[str, Any]

    def __init__(self, invoker: Any):
        self.cls_dic = {}
        self.named_dic = {}
        self.invoker = invoker

    def register(self, type: Any, **kwargs):
        """
        注册到SDK容器
        Args:
            type: class type
            **kwargs:
                - name:
                - scope: singleton
        Returns:

        """
        print("start to inject to Container")
        if self.cls_dic[type] is None:
            instance = type.create(invoker=self.invoker)
            self.cls_dic[type] = instance
            self.named_dic[type.__name__.lower()] = instance
        return type

    def get(self, type: Any) -> Any:
        return self.cls_dic[type]

    def __getitem__(self, name) -> Any:
        if self.named_dic[name]:
            return self.named_dic[name]
        else:
            raise KeyError(f"{name} service is not registered")


class BaseDiService:
    invoker: str

    def __init__(self, **kwargs):
        self.invoker = kwargs["invoker"]


sdk = Container(invoker="sdk")
