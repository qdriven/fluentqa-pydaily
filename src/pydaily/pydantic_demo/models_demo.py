#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from typing import Optional, List

from pydantic import ValidationError, BaseModel


class UserModel(BaseModel):
    id: int
    name = "Simon"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user = UserModel(**external_data)

print(user.id)
print(repr(user))
print(repr(user.signup_ts))
print(user.dict())

# jsonify
try:
    UserModel(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())


## nested object
class Foo(BaseModel):
    count: int
    size: float = None


class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]


m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
print(m)
# > foo=Foo(count=4, size=None) bars=[Bar(apple='x1', banana='y'),
# > Bar(apple='x2', banana='y')]
print(m.dict())
"""
{
    'foo': {'count': 4, 'size': None},
    'bars': [
        {'apple': 'x1', 'banana': 'y'},
        {'apple': 'x2', 'banana': 'y'},
    ],
}
"""
