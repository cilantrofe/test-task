import pytest
import random
from src.api_client import APIClient
from typing import Dict, Any


@pytest.fixture(scope="session")
def api_client() -> APIClient:
    """Фикстура для создания клиента API, используемого в тестах."""
    return APIClient()


@pytest.fixture
def pet_data():
    """Тестовые данные для создания питомца."""
    return {
        "id": 101,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Muhtar",
        "photoUrls": ["https://example.com/photo1.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available",
    }


@pytest.fixture
def new_order_data() -> Dict[str, Any]:
    """Тестовые данные для создания нового заказа с уникальным ID."""
    return {
        "id": random.randint(100, 1000),
        "petId": 1,
        "quantity": 2,
        "shipDate": "2024-11-10T15:49:56.789Z",
        "status": "placed",
        "complete": True,
    }


@pytest.fixture
def new_user_data() -> Dict[str, Any]:
    """Тестовые данные для создания нового пользователя с уникальным ID."""
    unique_id = random.randint(1000, 10000)
    return {
        "id": unique_id,
        "username": f"testuser{unique_id}",
        "firstName": "Test",
        "lastName": "User",
        "email": f"testuser{unique_id}@yandex.ru",
        "password": "password123",
        "phone": "123-456-7890",
        "userStatus": 1,
    }
