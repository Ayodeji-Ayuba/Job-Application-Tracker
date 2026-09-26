def test_register(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "pytest_register_001@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "pytest_register_001@example.com"
    assert "id" in data
    assert "created_at" in data

        # Then, try to register the same user again
    response = client.post(
        "/auth/register",
        json={
            "email": "pytest_register_001@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 400


def test_login(client):


    # Then, login with the registered user
    response = client.post(
        "/auth/login",
        json={
            "email": "pytest_register_001@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200