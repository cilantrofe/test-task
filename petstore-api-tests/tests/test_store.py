import requests
from src.api_client import APIClient
from typing import Dict, Any


def test_create_order(api_client: APIClient, new_order_data: Dict[str, Any]):
    """Тестирование создания заказа."""
    response = api_client.post("store/order", new_order_data)

    assert response.status_code == requests.codes.ok
    assert response.json()["id"] == new_order_data["id"]


def test_get_order_by_id(api_client: APIClient, new_order_data: Dict[str, Any]):
    """Тестирование получения заказа по ID."""
    api_client.post("store/order", new_order_data)

    order_id = new_order_data["id"]
    response = api_client.get(f"store/order/{order_id}")

    assert response.status_code == requests.codes.ok
    assert response.json()["id"] == order_id


def test_delete_order(api_client: APIClient, new_order_data: Dict[str, Any]):
    """Тестирование удаления заказа."""
    api_client.post("store/order", new_order_data)

    order_id = new_order_data["id"]
    response = api_client.delete(f"store/order/{order_id}")

    assert response.status_code == requests.codes.ok

    response = api_client.get(f"store/order/{order_id}")

    assert response.status_code == requests.codes.not_found
