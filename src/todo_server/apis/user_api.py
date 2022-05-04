# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.user import User


router = APIRouter()


@router.get(
    "/user",
    responses={
        200: {"model": User, "description": "The user profile information"},
    },
    tags=["user"],
)
async def get_user_profile(
) -> User:
    """Return the current user profile"""
    ...
