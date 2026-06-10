from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_environment_endpoint():
    response = client.get("/environment")

    assert response.status_code == 200
    assert response.json() == {"environment": "development"}
