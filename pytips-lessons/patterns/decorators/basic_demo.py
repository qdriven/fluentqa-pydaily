#!/usr/bin/env python
# -*- coding:utf-8 -*-

logger_dict = dict()


def log_demo():
    print("log_demo")


logger_dict["log_demo"] = log_demo


def request_logger(f):
    print(f)
    logger_dict[f.__name__] = f
    print(type(f))
    print("start printing logger")
    return f


def req_proxy(f):
    return log_demo


@request_logger
def log_it():
    print("logit")


@req_proxy
def log_proxy_it():
    print("log_proxy_it")


log_it()
print(logger_dict)
logger_dict["log_it"]()
log_proxy_it()
