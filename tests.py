"""
Base tests
"""



from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main():
    """
    Response root endpoint
    """
    response = client.get("/")
    assert response.status_code == 200


def test_api_response():
    """
    Response api endpoint
    """
    response = client.get("/api/v1/")
    assert response.status_code == 200
