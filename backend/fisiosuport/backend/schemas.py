from pydantic import BaseModel
from typing import  Optional
from sqlalchemy import  Column


class TypeBase(BaseModel):
    id: int
    name: str


class TypeCreate(TypeBase):
    name: str

class TypeUpdate(TypeBase):
    id: Optional[int] = None
    name: Optional[str] = None

class Type(TypeBase):
    id: int
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    name: str
    password: str
    type_id: Optional[int] = Column(default=None, foreign_key="type.id")
    documento: int
    

class UserUpdate(UserBase):
    id: Optional[int] = None
    name: Optional[str] = None
    documento: Optional[int] = None
    type_id: Optional[int] = None
    password: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    documento: int
    type_id: Optional[int] = None

    class Config:
        orm_mode = True


class Especialidade(UserBase):
    id: int
    name: str
    class Config:
        orm_mode = True


class Especialidade(UserBase):
    id: int
    name: str
    class Config:
        orm_mode = True