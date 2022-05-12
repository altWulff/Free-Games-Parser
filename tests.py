"""
Base tests
"""


from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main():
    """
    Test response root endpoint
    """
    response = client.get("/")
    assert response.status_code == 200


def test_api_response():
    """
    Test response api endpoint
    """
    response = client.get("/api/v1/")
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) > 0


def test_api_response_data_len():
    """
    Test response data
    assert length greater than one
    """
    response = client.get("/api/v1/")
    response_data = response.json()
    assert len(response_data) > 0


def test_api_response_correct_schema():
    """
    Test response data
    assert correct data in schema
    """
    response = client.get("/api/v1/")
    response_data = response.json()
    for indx, _ in enumerate(response_data):
        response = client.get(f"/api/v1/{indx}")
        assert response.status_code == 200
