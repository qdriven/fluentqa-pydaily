#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Optional, Union

from fastapi import FastAPI
from core import config

from fastapi import Depends
from pydantic import BaseModel

from core.pyapi_settings import PyAPISetting, get_settings
app = FastAPI()
from fastapi import APIRouter

from pyapi.todo.api import task as tasks

api_router = APIRouter()
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(api_router, prefix=config.API_V1)


@app.get('/hello')
def hello_world():
    return {"message": "Hello World!"}


@app.get('/ping')
def pong(settings: PyAPISetting = Depends(get_settings)):
    return settings


@app.get('/resources/{id}')
def restful_demo_get_request(id: int, q: Union[str, None] = None):
    return {"id": id, "name": q}


class ResReqDTO(BaseModel):
    id: Optional[str | None] = None
    name: str


@app.post("/resources")
def restful_demo_post_request(req: ResReqDTO):
    print(req)
    req.id = "test_id"
    req.name = "-".join([req.name, req.id])
    return req


@app.put("/resource/{id}")
def restful_demo_update_request(id: str, req: ResReqDTO):
    print(req)
    req.id = id
    req.name = "-".join([req.name, req.id, "updated"])
    return req


@app.delete("/resource/{id}")
def restful_demo_update_request(id: str, req: ResReqDTO):
    req.id = id
    req.name = "-".join([req.name, req.id])
    req.name.removeprefix("test")
    return req

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(
#         "pyapi.main:pyapi",
#         host="0.0.0.0",
#         reload=True,
#         port=3001,
#     )
