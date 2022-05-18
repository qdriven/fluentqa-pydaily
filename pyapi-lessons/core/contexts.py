#!/usr/bin/env python
# -*- coding:utf-8 -*-

from injector import Injector

from core.db import Database

injector = Injector()
database = injector.get(Database)

