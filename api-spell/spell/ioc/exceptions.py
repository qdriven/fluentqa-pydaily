#!/usr/bin/env python
# -*- coding:utf-8 -*-

class IoCError(RuntimeError):
    pass


class ResolverError(IoCError):
    pass


class ExecutionError(IoCError):
    pass


class RegisteredKeyError(IoCError):
    pass
