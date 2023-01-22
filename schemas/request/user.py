import sqlalchemy
from pydantic import BaseModel

from models import RoleType


class UserBase(BaseModel):
    email: str


class UserRegisterIn(UserBase):
    password: str
    login: str
    first_name: str
    last_name: str
    role: str

class UserLoginIn(UserBase):
    password: str