# tests/test_integration_example.py
# ruff: noqa: I001
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.app import app

# Test health endpoint
def test_health_endpoint():
    client = app.test_client()

    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
