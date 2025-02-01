from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Crypto Market API!"}

def test_get_coins():
    response = client.get("/coins?page_num=1&per_page=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
