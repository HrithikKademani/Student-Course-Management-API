from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "test@example.com"