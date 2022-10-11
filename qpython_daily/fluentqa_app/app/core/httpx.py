#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import AsyncGenerator

from httpx import AsyncClient


async def init_http_client() -> AsyncGenerator[AsyncClient, None]:
    """Initialize HTTPX Client and close it when finished."""
    client = AsyncClient()
    yield client
    await client.aclose()
