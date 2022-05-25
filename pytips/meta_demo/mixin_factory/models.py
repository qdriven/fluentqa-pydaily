#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pydantic import BaseModel


class BaseModelFactory:

    @classmethod
    def create(cls: BaseModel, **kwargs):
        return cls(**kwargs)
