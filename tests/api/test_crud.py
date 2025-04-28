import requests

BASE_URL = "https://api.example.com"
LOGIN_ENDPOINT = "/auth/login"
PROTECTED_ENDPOINT = "/user/profile"



def test_crud_operations():
    # Авторизация
    auth_data = {"username": "test", "password": "test"}
    auth_response = requests.post(f"{BASE_URL}{LOGIN_ENDPOINT}", json=auth_data)
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # CREATE - Создание нового ресурса
    new_item = {"name": "Test Item", "description": "Test Description"}
    create_response = requests.post(
        f"{BASE_URL}/items", 
        json=new_item, 
        headers=headers
    )
    assert create_response.status_code == 201
    item_id = create_response.json()["id"]
    
    # READ - Получение созданного ресурса
    get_response = requests.get(
        f"{BASE_URL}/items/{item_id}", 
        headers=headers
    )
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Item"
    
    # UPDATE - Обновление ресурса
    updated_data = {"name": "Updated Name"}
    update_response = requests.patch(
        f"{BASE_URL}/items/{item_id}", 
        json=updated_data, 
        headers=headers
    )
    assert update_response.status_code == 200
    
    # DELETE - Удаление ресурса
    delete_response = requests.delete(
        f"{BASE_URL}/items/{item_id}", 
        headers=headers
    )
    assert delete_response.status_code == 204
    
    # Проверка что ресурс удален
    get_deleted_response = requests.get(
        f"{BASE_URL}/items/{item_id}", 
        headers=headers
    )
    assert get_deleted_response.status_code == 404