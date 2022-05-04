#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Optional

from src.lessons.server_api import app as app


@app.get("/helloworld")
def hell_world():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def get_item_by_id(item_id:int,q:Optional[str]=None):
    return {"item_id":item_id,"q":q}