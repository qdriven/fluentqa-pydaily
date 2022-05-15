#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pydantic import BaseModel


class FunctionModel(BaseModel):
    name: str
    