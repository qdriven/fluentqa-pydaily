#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(100000)


def fib(n):
    if n == 1: return 1
    if n == 2: return 1
    return fib(n - 2) + fib(n - 1)


def fib_generator(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    result = fib_generator(5)
    print(list(result))

