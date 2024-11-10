import requests
from src.api_client import APIClient
from typing import Dict, Any


def test_create_pet(api_client: APIClient, pet_data: Dict[str, Any]):
    """Тестирование создания питомца."""
    response = api_client.post("pet", pet_data)

    assert response.status_code == requests.codes.ok
    assert response.json()["name"] == pet_data["name"]


def test_get_pet_by_id(api_client: APIClient, pet_data: Dict[str, Any]):
    """Тестирование получения питомца по ID."""
    api_client.post("pet", pet_data)

    pet_id = pet_data["id"]
    response = api_client.get(f"pet/{pet_id}")

    assert response.status_code == requests.codes.ok
    assert response.json()["id"] == pet_id


def test_update_pet(api_client: APIClient, pet_data: Dict[str, Any]):
    """Тестирование обновления питомца."""
    updated_pet_data = pet_data.copy()
    updated_pet_data["name"] = "MuhtarUpdated"
    updated_pet_data["status"] = "sold"

    api_client.post("pet", pet_data)

    response = api_client.put("pet", updated_pet_data)

    assert response.status_code == requests.codes.ok
    assert response.json()["name"] == updated_pet_data["name"]
    assert response.json()["status"] == "sold"


def test_delete_pet(api_client: APIClient, pet_data: Dict[str, Any]):
    """Тестирование удаления питомца."""
    api_client.post("pet", pet_data)

    pet_id = pet_data["id"]
    response = api_client.delete(f"pet/{pet_id}")

    assert response.status_code == requests.codes.ok

    response = api_client.get(f"pet/{pet_id}")

    assert response.status_code == requests.codes.not_found
