import pytest
from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

@pytest.fixture
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope='module')
def test_app():
    return client

def test_create_task(test_app):
    response = test_app.post("/tasks/", json={"description": "Test Task", "status": "Pending"})
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Test Task"
    assert data["status"] == "Pending"
    assert "id" in data

def test_read_tasks(test_app):
    response = test_app.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)