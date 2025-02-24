from pydantic import BaseModel, EmailStr

class Message (BaseModel):
    message: str

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserDB(UserSchema):
    id: int

class PublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserList(BaseModel):
    users: list[PublicSchema]  # estamos dizendo que o retorne será um alista apenas com id, username e email