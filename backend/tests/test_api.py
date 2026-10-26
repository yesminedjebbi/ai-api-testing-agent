
import pytest
from fastapi.testclient import TestClient
import app.main as main

client = TestClient(main.app)


# Réinitialiser les données avant chaque test
@pytest.fixture(autouse=True)
def reset_database():
    main.users.clear()
    main.next_id = 1
    yield
    main.users.clear()


# Test 1 : créer un utilisateur valide
def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": "Alice",
            "email": "alice@example.com"
        }
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1


# Test 2 : email invalide
def test_invalid_email():
    response = client.post(
        "/users",
        json={
            "name": "Alice",
            "email": "invalid-email"
        }
    )

    assert response.status_code == 422


# Test 3 : email manquant
def test_missing_email():
    response = client.post(
        "/users",
        json={"name": "Alice"}
    )

    assert response.status_code == 422


# Test 4 : utilisateur inexistant
def test_user_not_found():
    response = client.get("/users/999")

    assert response.status_code == 404


# Test 5 : suppression d'un utilisateur
def test_delete_user():
    response = client.post(
        "/users",
        json={
            "name": "Alice",
            "email": "alice@example.com"
        }
    )

    user_id = response.json()["id"]

    delete_response = client.delete(
        f"/users/{user_id}"
    )

    assert delete_response.status_code == 204

    get_response = client.get(
        f"/users/{user_id}"
    )

    assert get_response.status_code == 404
