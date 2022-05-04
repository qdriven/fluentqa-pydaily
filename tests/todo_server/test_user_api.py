# coding: utf-8

from fastapi.testclient import TestClient


from todo_server.models.user import User  # noqa: F401


def test_get_user_profile(client: TestClient):
    """Test case for get_user_profile

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/user",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

