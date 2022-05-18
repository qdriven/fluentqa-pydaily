#!/usr/bin/env python
# -*- coding:utf-8 -*-
from box import Box

movie_box = Box({"Robin Hood: Men in Tights":
                     {"imdb stars": 6.7, "length": 104}})

print(movie_box.Robin_Hood_Men_in_Tights.imdb_stars)

another_json = Box({
    "req": "test",
    "resp": {"body": "a123", "code": "12", "msg": "msg"}
})

print(another_json.req)
print(another_json.resp)
movie_box['name'] = "test"
print(movie_box.name)
