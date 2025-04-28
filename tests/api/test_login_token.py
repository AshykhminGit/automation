import requests
import pytest

# Базовые настройки
# Импортируем необходимые библиотеки 
#https://reqres.in/
#https://reqres.in/api-docs/#/default/post_login
#https://petstore.swagger.io/
#https://restful-booker.herokuapp.com/apidoc/index.html

BASE_URL = "https://restful-booker.herokuapp.com/"
LOGIN_ENDPOINT = "/auth/"
PROTECTED_ENDPOINT = "/user/profile"



def test_successful_auth_and_token_usage():
    # 1. Авторизация и получение токена
    # auth_data = {
    #     "username": "test_user",
    #     "password": "test_password"
    # }

    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    
    response = requests.post(f"{BASE_URL}{LOGIN_ENDPOINT}", json=auth_data)
    
    # Проверяем успешность авторизации
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    
    # Извлекаем токен из ответа
    token = response.json().get("token")
    assert token is not None, "Токен не получен в ответе"
    
    # 2. Использование токена для доступа к защищенному эндпоинту
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    profile_response = requests.get(
        f"{BASE_URL}{PROTECTED_ENDPOINT}", 
        headers=headers
    )
    
    # Проверяем доступ к защищенным данным
    assert profile_response.status_code == 200, "Не удалось получить доступ с токеном"
    assert "username" in profile_response.json(), "В ответе нет данных пользователя"