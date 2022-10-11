#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration

from app.config.environment import Settings
from app.core.httpx import init_http_client


class Container(DeclarativeContainer):
    """Base DI container."""

    config = Configuration()
    http_client = providers.Resource(init_http_client)


def create_container(settings: Settings, modules: list[Any]) -> Container:
    """Create a Conteiner."""
    container = Container()
    container.config.from_pydantic(settings, required=True)
    container.wire(modules=modules)

    return container
