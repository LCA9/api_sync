from http import HTTPStatus

from fastapi import FastAPI, HTTPException


#from codigos import Message, UserSchema, PublicSchema, UserDB
from .schemas  import Message, UserSchema, PublicSchema, UserDB, UserList
app = FastAPI()

database = []

@app.get('/', status_code = HTTPStatus.OK, response_model=Message )
def read_root():
    return {'message': 'Olá mundo!'}


@app.post('/users/', status_code = HTTPStatus.CREATED, response_model=PublicSchema) #status_code = 201 # esse schema é para mostrar o que será retornado
def create_user(user: UserSchema): # esse schema é para mostrar o que precisa receber

    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump() # tira o objeto user do formato pydantic, e converte para um tipo dicionario. E o ** desempacota 
    )

    database.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UserList)
def read_user():
    return {'users': database}

@app.put('/users/{user_id}',response_model=PublicSchema)
def update_user(user_id: int, user: UserSchema):

    if user_id < 0 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail = "User not found"
        )


    user_with_id = UserDB(
            id=user_id,
            **user.model_dump()
    )

    database[user_id - 1] = user_with_id
    return user_with_id

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):

    if user_id < 0 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail = "User not found"
        )
    
    del database[user_id - 1]
    return {'message': 'User deleted'}