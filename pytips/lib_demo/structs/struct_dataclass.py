#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Dataclasses by default automatically initialise a bunch of dunder methods for us in a class such as:
#
# __init__ The initialisation method for the class
# __repr__ How the class is represented with print() is called
# __str__ How the class is represented as a string (called with __repr__)
# __eq__ Used when equality operators are used (eg, ==)
# __hash__ The hash for the class (called with __eq__)
import typing
from dataclasses import dataclass

from pytips.lib_demo.structs import class_tester


@dataclass
class DataStruct:
    x: float = None
    y: float = None
    kwargs: typing.Dict = None

class_tester(DataStruct)
