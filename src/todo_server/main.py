# coding: utf-8

"""
    Todo

    My Todo list API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from todo_server.apis.todos_api import router as TodosApiRouter
from openapi_server.apis.user_api import router as UserApiRouter

app = FastAPI(
    title="Todo",
    description="My Todo list API",
    version="1.0.0",
)

app.include_router(TodosApiRouter)
app.include_router(UserApiRouter)