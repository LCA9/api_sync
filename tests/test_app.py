from fastapi.testclient import TestClient
from http import HTTPStatus



def test_read_root_deve_retornar_ok_e_ola_mundo(client):
   #client = TestClient(app) # Arrange (organiza)

    response = client.get('/')  # Act (ação)

    assert response.status_code == 200 # assert
    #assert responde.status_code == HTTPStatus.OK # assert
    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user(client):
    #client = TestClient(app)

    response = client.post( #User
        '/users/',
        json={
            'username': 'testeusermane',
            'password': 'passaword',
            'email': 'teste@test.com', 
        }
    )

    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED

    # Validar UserPublic
    assert response.json() == {
        'username': 'testeusermane',
        'email': 'teste@test.com',
        'id': 1
    }

# esse teste dependendo do de cima, pois o de cima add um usuario no banco e esse test "pega" as informações adicionadas pelo teste de cima e compara.
def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusermane',
                'email': 'teste@test.com',
                'id': 1
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password':'123',
            'username': 'testusername2',
            'email': 'teste@test.com',
            'id': 1
        },
    )

    assert response.json() =={
            'username': 'testusername2',
            'email': 'teste@test.com',
            'id': 1
        }

# criar um test para testar o erro do put


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}