import requests
import pytest
import json
import time
import logging
import os
from requests.auth import HTTPBasicAuth


def test_successful_auth_and_token_usage():
    auth_data = {
        "username": "admin",
        "password": "password123"
    }

    BASE_URL = "https://restful-booker.herokuapp.com/auth"

    response = requests.post(f"{BASE_URL}", json=auth_data)

    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    print(response.status_code)
    # Извлекаем токен из ответа
    token = response.json().get("token")
    assert token is not None, "Токен не получен в ответе"
    print(token, "Токен получен в ответе")
    # 2. Использование токена для доступа к защищенному эндпоинту
    headers = {
        "Authorization": f"Bearer {token}"
    }
    # Проверяем доступ к защищенным данным
    # response = requests.get(
    #     f"{BASE_URL}", 
    #     headers=headers
    # )
    # assert response.status_code == 200, "Не удалось получить доступ с токеном"
    # assert "username" in response.json(), "В ответе нет данных пользователя"
    # print(response.status_code)
    # # Проверяем, что данные пользователя корректны
    # assert response.json()["username"] == "admin", "Имя пользователя не совпадает"
    # print(response.json())




