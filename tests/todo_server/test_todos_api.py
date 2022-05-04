# coding: utf-8

from fastapi.testclient import TestClient


from todo_server.models.new_todo import NewTodo  # noqa: F401
from todo_server.models.todo import Todo  # noqa: F401


def test_create_todo(client: TestClient):
    """Test case for create_todo

    Create a Todo
    """
    new_todo = {"id":"ec3b48dc-938d-11ea-8877-c7ea413b00cb","title":"Example Todo","description":"This is a Todo entity with a description","created":"2020-05-14T09:00:00.000Z","due_date":"2020-05-20T09:00:00.000Z","complete":0}

    headers = {
    }
    response = client.request(
        "POST",
        "/todos",
        headers=headers,
        json=new_todo,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_todo(client: TestClient):
    """Test case for delete_todo

    Delete a Todo
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/todos/{todoId}".format(todoId='todo_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_todo(client: TestClient):
    """Test case for get_todo

    Get a Todo
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/todos/{todoId}".format(todoId='todo_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_gettodos(client: TestClient):
    """Test case for gettodos

    List All todos
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/todos",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_todo(client: TestClient):
    """Test case for update_todo

    Update a Todo
    """
    todo = None

    headers = {
    }
    response = client.request(
        "PUT",
        "/todos/{todoId}".format(todoId='todo_id_example'),
        headers=headers,
        json=todo,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

