import requests
from src.api_client import APIClient
from typing import Dict, Any


def test_create_user(api_client: APIClient, new_user_data: Dict[str, Any]):
    """Тестирование создания пользователя."""
    response = api_client.post("user", new_user_data)

    assert response.status_code == requests.codes.ok
    assert response.json()["message"] == str(new_user_data["id"])


def test_get_user_by_username(api_client: APIClient, new_user_data: Dict[str, Any]):
    """Тестирование получения пользователя по имени."""
    api_client.post("user", new_user_data)

    username = new_user_data["username"]
    response = api_client.get(f"user/{username}")

    assert response.status_code == requests.codes.ok
    assert response.json()["username"] == username


def test_update_user(api_client: APIClient, new_user_data: Dict[str, Any]):
    """Тестирование обновления пользователя."""
    api_client.post("user", new_user_data)

    username = new_user_data["username"]
    updated_data = new_user_data.copy()
    updated_data["firstName"] = "UpdatedName"
    response = api_client.put(f"user/{username}", updated_data)

    assert response.status_code == requests.codes.ok

    response = api_client.get(f"user/{username}")

    assert response.json()["firstName"] == "UpdatedName"


def test_delete_user(api_client: APIClient, new_user_data: Dict[str, Any]):
    """Тестирование удаления пользователя."""
    api_client.post("user", new_user_data)

    username = new_user_data["username"]
    response = api_client.delete(f"user/{username}")

    assert response.status_code == requests.codes.ok

    response = api_client.get(f"user/{username}")

    assert response.status_code == requests.codes.not_found
