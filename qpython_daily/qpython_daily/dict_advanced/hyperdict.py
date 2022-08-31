#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Optional, Dict


class HyperDict:

    def __init__(self, dict_obj: Optional[Dict] = None, **options) -> None:
        if dict_obj is None:
            self.__dict_box = {}
        else:
            self.__dict_box = dict_obj
        self.__key_cache = {}
        self.k = list(self.__dict_box.keys())
        self.v = list(self.__dict_box.values())
        self.i = list(self.__dict_box.items())
        self._options = options

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __repr__(self):
        pass
