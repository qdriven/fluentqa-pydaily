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



router = APIRouter()


@router.post(
    "/todos",
    responses={
        200: {"model": Todo, "description": "Successful response."},
    },
    tags=["todos"],
    summary="Create a Todo",
)
async def create_todo(
        new_todo: NewTodo = Body(None, description="A new &#x60;Todo&#x60; to be created."),
) -> Todo:
    """Creates a new instance of a &#x60;Todo&#x60;."""
    ...


@router.delete(
    "/todos/{todoId}",
    responses={
        204: {"description": "Successful response."},
    },
    tags=["todos"],
    summary="Delete a Todo",
)
async def delete_todo(
        todoId: str = Path(None, description="A unique identifier for a &#x60;Todo&#x60;."),
) -> None:
    """Deletes an existing &#x60;Todo&#x60;."""
    ...


@router.get(
    "/todos/{todoId}",
    responses={
        200: {"model": Todo, "description": "Successful response - returns a single &#x60;Todo&#x60;."},
    },
    tags=["todos"],
    summary="Get a Todo",
)
async def get_todo(
        todoId: str = Path(None, description="A unique identifier for a &#x60;Todo&#x60;."),
) -> Todo:
    """Gets the details of a single instance of a &#x60;Todo&#x60;."""
    ...


@router.get(
    "/todos",
    responses={
        200: {"model": List[Todo],
              "description": "Successful response - returns an array of &#x60;Todo&#x60; entities."},
    },
    tags=["todos"],
    summary="List All todos",
)
async def gettodos(
) -> List[Todo]:
    """Gets a list of all &#x60;Todo&#x60; entities."""
    ...


@router.put(
    "/todos/{todoId}",
    responses={
        200: {"model": Todo, "description": "Successful response."},
    },
    tags=["todos"],
    summary="Update a Todo",
)
async def update_todo(
        todoId: str = Path(None, description="A unique identifier for a &#x60;Todo&#x60;."),
        todo: Todo = Body(None, description="Updated &#x60;Todo&#x60; information."),
) -> Todo:
    """Updates an existing &#x60;Todo&#x60;."""
    ...
