#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ContainerError(RuntimeError):
    pass


class ExecutionError(ContainerError):
    pass


class ResolverError(ContainerError):
    pass


class ServiceError(ContainerError, KeyError):
    pass
