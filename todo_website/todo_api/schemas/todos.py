from typing import Optional
from ninja import Schema

from .auth import UserSchema


class TodoSchema(Schema):
    id: int
    text: str
    is_completed: bool = False
    author: UserSchema


class TodoCreateSchema(Schema):
    text: str


class TodoUpdateSchema(Schema):
    text: Optional[str] = None
    is_completed: Optional[bool] = None


class TodoDeleteSchema(Schema):
    is_deleted: bool