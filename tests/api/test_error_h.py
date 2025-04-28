import requests

import pytest



# Базовые настройки
BASE_URL = "https://api.example.com"
LOGIN_ENDPOINT = "/auth/login"
PROTECTED_ENDPOINT = "/user/profile"

def test_error_handling():
    # Неправильные учетные данные
    invalid_auth = {"username": "wrong", "password": "wrong"}
    response = requests.post(f"{BASE_URL}{LOGIN_ENDPOINT}", json=invalid_auth)
    assert response.status_code == 401
    assert "error" in response.json()
    
    # Попытка доступа без токена
    response = requests.get(f"{BASE_URL}{PROTECTED_ENDPOINT}")
    assert response.status_code == 401
    
    # Несуществующий эндпоинт
    response = requests.get(f"{BASE_URL}/nonexistent")
    assert response.status_code == 404