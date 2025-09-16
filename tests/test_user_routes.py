import pytest
from fastapi.testclient import TestClient
from main import app
from app.crud import create_tables, drop_tables

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Setup and teardown test DB"""
    create_tables()
    yield
    drop_tables()

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_create_user(client):
    response = client.post("/users", json={"email": "bob@example.com", "username": "bobby", "user_password" : "test123"})
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data

def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert any(u["email"] == "bob@example.com" for u in users)
