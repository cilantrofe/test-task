import requests
from typing import Dict, Any


class APIClient:
    """Клиент для работы с API Petstore."""

    BASE_URL = "https://petstore.swagger.io/v2"
    PET_ENDPOINT = "pet"
    STORE_ENDPOINT = "store/order"
    USER_ENDPOINT = "user"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def post(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        """POST-запрос."""
        try:
            return self.session.post(f"{self.BASE_URL}/{endpoint}", json=data)
        except requests.RequestException as e:
            print(f"Error in POST request: {e}")
            raise

    def get(self, endpoint: str) -> requests.Response:
        """GET-запрос."""
        try:
            return self.session.get(f"{self.BASE_URL}/{endpoint}")
        except requests.RequestException as e:
            print(f"Error in GET request: {e}")
            raise

    def put(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        """PUT-запрос."""
        try:
            return self.session.put(f"{self.BASE_URL}/{endpoint}", json=data)
        except requests.RequestException as e:
            print(f"Error in PUT request: {e}")
            raise

    def delete(self, endpoint: str) -> requests.Response:
        """DELETE-запрос."""
        try:
            return self.session.delete(f"{self.BASE_URL}/{endpoint}")
        except requests.RequestException as e:
            print(f"Error in DELETE request: {e}")
            raise
