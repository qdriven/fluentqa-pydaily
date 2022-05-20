#!/usr/bin/env python
# -*- coding:utf-8 -*-
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class FuncParameter:
    type: Any
    name: str
    default: Any


def inspect_func_params(func: Callable, ):
    pass
