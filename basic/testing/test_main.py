from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

"""
1. pip install pytest
2. pytest 실행
"""

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}