from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_redirect_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "hint" in response.json()

def test_helloworld():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    