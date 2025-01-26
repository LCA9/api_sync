import pytest
from codigos.app import app
from fastapi.testclient import TestClient

@pytest.fixture() # serve para não ter que fica o tempo do fazendo isso  client = TestClient(app)
def client():
    return TestClient(app)
