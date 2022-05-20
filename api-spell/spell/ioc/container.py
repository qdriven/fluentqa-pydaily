#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Union, Type

from box import Box

from spell.clogger import clogger
from spell.ioc import RegisteredKeyError


@dataclass
class Container:
    _cached_by_type: Box[Union[Type], Any] = field(default_factory=Box)
    _cached_by_name: Box[Union[str], Any] = field(default_factory=Box)
    # _alias: Box[Union[str, Type], List[Union[str, Type]]] = field(default_factory=Box)
    _loaded_objects: Box[Union[str], Any] = field(default_factory=Box)

    def __post_init__(self):
        clogger.info("container is initialized")

    def __setitem__(self, key: Union[str, Type], value: Any) -> None:
        self._loaded_objects[key] = value
        if key in self._loaded_objects:
            if isinstance(key, str):
                self._cached_by_name[key] = value
            else:
                self._cached_by_type[key] = value

    def __getitem__(self, key: Union[str, Type]) -> Any:
        if key in self._loaded_objects:
            return self._loaded_objects[key]
        raise RegisteredKeyError(f"Service {key} is not registered", key)
    # TODO: getattr/setattr

# export ioc container
ioc: Container = Container()
__all__ = ["Container", "ioc"]
