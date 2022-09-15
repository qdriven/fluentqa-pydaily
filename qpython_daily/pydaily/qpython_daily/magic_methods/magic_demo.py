#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
__eq__(self, other) Defines behavior for the equality operator, ==.
__ne__(self, other) Defines behavior for the inequality operator, !=.
__lt__(self, other) Defines behavior for the less-than operator, <.
__gt__(self, other) Defines behavior for the greater-than operator, >.
__le__(self, other) Defines behavior for the less-than-or-equal-to operator, <=.
__ge__(self, other) Defines behavior for the greater-than-or-equal-to operator, >=
__pos__(self) Implements behavior for unary positive (e.g. +some_object)
__neg__(self) Implements behavior for negation (e.g. -some_object)
__abs__(self) Implements behavior for the built in abs() function.
__invert__(self) Implements behavior for inversion using the ~ operator.
__round__(self, n) Implements behavior for the buil in round() function. n is the number
of decimal places to round to.
__floor__(self) : Implements behavior for math.floor(), i.e., rounding down to the nearest
integer.
__ceil__(self) : Implements behavior for math.ceil(), i.e., rounding up to the nearest
integer.
__trunc__(self) : Implements behavior for math.trunc(), i.e., truncating to an integral.
__add__(self, other) Implements addition.
__sub__(self, other) Implements subtraction.
__mul__(self, other) Implements multiplication.
__floordiv__(self, other) Implements integer division using the // operator.
__div__(self, other) Implements division using the / operator.
__truediv__(self, other) Implements true division. Note that this only works when from
__future__ import division is in effect.
__mod__(self, other) Implements modulo using the % operator.
__divmod__(self, other) Implements behavior for long division using the divmod() built in
function.
__pow__ Implements behavior for exponents using the ** operator.
__lshift__(self, other) Implements left bitwise shift using the << operator.
__rshift__(self, other) Implements right bitwise shift using the >> operator.
__and__(self, other) Implements bitwise and using the & operator.
__or__(self, other) Implements bitwise or using the | operator.
__xor__(self, other) Implements bitwise xor using the ^ operator.
"""
from typing import Iterable


class MagicClass(object):

    # def __new__(cls, *args, **kwargs):
    #     print("this is new ")

    def __init__(self, v=1):
        print("this is __init__")
        self.__values = {"v": v}
        self.temp = v

    def __del__(self):
        print("this is from __del__")

    def __eq__(self, other):
        print("this is ==")
        return True
        # return self ==other

    def __add__(self, other):
        print("this is +")
        print(self.temp + other.temp)

    def __cmp__(self, other):
        return

    def __str__(self):
        return str(self.temp)

    def __repr__(self):
        return "this is {}".format(self.temp)

    # def __dir__(self) -> Iterable[str]:
    #     pass
    #
    def __getitem__(self, item):
        try:
            return self.__values[item]
        except KeyError as e:
            raise KeyError("invalid attribute name {}".format(item))

    def __get__(self, instance, owner):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __copy__(self):
        pass

    def __deepcopy__(self, memodict={}):
        pass

    # # item container
    # def __getitem__(self, item):
    #     pass
    #
    # def __iter__(self):
    #     pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    m = MagicClass()
    m1 = MagicClass(2)
    print(m.v)
    print(m == m1)
    print(m + m1)
    print(repr(m))
    print(str(m))
