from fastapi.testclient import TestClient
from http import HTTPStatus

from codigos.app import app



def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app) # Arrange (organiza)

    response = client.get('/')  # Act (ação)

    assert response.status_code == 200 # assert
    #assert responde.status_code == HTTPStatus.OK # assert
    assert response.json() == {'message': 'Olá mundo!'}