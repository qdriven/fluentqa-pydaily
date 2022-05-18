#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

from pydantic import BaseSettings

from pyapi.pyapi_logger import log


class PyAPISetting(BaseSettings):
    env: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


def get_settings() -> BaseSettings:
    log.info("getting settings")
    return PyAPISetting()
