#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cloudpickle

def add_func(a,b):
    print("print add",a+b)
    return a+b

squared = lambda x: x ** 2

pickled_lambda = cloudpickle.dumps(squared)
pickled_func = cloudpickle.dumps(add_func)

new_squared = cloudpickle.loads(pickled_lambda)
new_squared(2)

nwe_pickled_func = cloudpickle.loads(pickled_func)
result = nwe_pickled_func(2,3)
print(result)
