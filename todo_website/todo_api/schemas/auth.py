from typing import Optional
from ninja import Schema


class UserSchema(Schema):
    id: int
    username: Optional[str]
    first_name: Optional[str]
    email: Optional[str]


class UserLoginSchema(Schema):
    username: str
    password: str


class UserRegistrationSchema(Schema):
    first_name: str
    username: str
    email: str
    password1: str
    password2: str