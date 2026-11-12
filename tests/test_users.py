
def test_get_all_users(api_client, base_url):
    response = api_client.get(f"{base_url}/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

def test_get_single_user(api_client, base_url):
    user_id = 1
    response = api_client.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert isinstance(user, dict)
    assert user["id"] == user_id
    assert "name" in user
    assert "email" in user

def test_get_nonexistent_user(api_client, base_url):
    user_id = 9999
    response = api_client.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404