from pydantic import BaseModel


class TypeBase(BaseModel):
    title: str
    description: str | None = None


class TypeCreate(TypeBase):
    pass


class Type(TypeBase):
    id: int
    type_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    types: list[Type] = []

    class Config:
        orm_mode = True
