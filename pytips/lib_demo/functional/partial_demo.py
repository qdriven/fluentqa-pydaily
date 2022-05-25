#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import partial


def add(a, b, t=None, **kwargs):
    # 打印位置参数
    # for n in args:
    #     print(n)
    print(a, b)
    print("-" * 20)
    if t:
        print("t:", t)
    # 打印关键字参数
    for k, v in kwargs.items():
        print('%s:%s' % (k, v))
    # 暂不做返回，只看下参数效果，理解 partial 用法


# 普通调用
add(1, 2, v1=10, v2=20)

add_partial = partial(add, 1, 10)
add_partial(t=100, v1=100)
