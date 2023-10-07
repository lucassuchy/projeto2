from pydantic import BaseModel
from typing import  Optional
from sqlalchemy import  Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import date

# Type
class TypeBase(BaseModel):
    name: str

class Type(TypeBase):
    id: int
    name: str

    class Config:
        orm_mode = True

class TypeCreate(TypeBase):
    name: str

class TypeUpdate(TypeBase):
    name: Optional[str] = None

# User
class UserBase(BaseModel):
    name: str
    password: str
    type_id: Optional[int] = Column(Integer, ForeignKey("type.id"), default=None)
    document: int
    birth_date: date

class User(UserBase):
    id: int
    is_active: bool
    document: int
    type_id: Optional[int] = None
    birth_date: Optional[date] = None

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    name: str
    password: str
    type_id: Optional[int] = Column(Integer, ForeignKey("type.id"), default=None)
    document: int
    birth_date: date
    

class UserUpdate(UserBase):
    name: Optional[str] = None
    document: Optional[int] = None
    type_id: Optional[int] = None
    password: Optional[str] = None
    birth_date: Optional[date] = None

# Especialidade
class EspecialidadeBase(BaseModel):
    id: int
    name: str

class Especialidade(EspecialidadeBase):
    id: int
    name: str
    class Config:
        orm_mode = True

class EspecialidadeUpdate(EspecialidadeBase):
    name: Optional[str] = None

# Tratamento
class TratamentoBase(BaseModel):
    id: int
    name: str
    video: str

class Tratamento(TratamentoBase):
    id: int
    name: str
    video: str
    class Config:
        orm_mode = True

class TratamentoUpdate(TratamentoBase):
    name: Optional[str] = None
    video: Optional[str] = None

# Paciente
class PacienteBase(BaseModel):
    id: int
    user_id: Column(Integer, ForeignKey("users.id"), default=None)
    tratamento_id: Column(Integer, ForeignKey("tratamento.id"), default=None)
    fisioterapeuta_id: Column(Integer, ForeignKey("users.id"), default=None)
    quantity: int
    duration: int

class Paciente(PacienteBase):
    id: int
    user_id: Column(Integer, ForeignKey("users.id"), default=None)
    tratamento_id: Column(Integer, ForeignKey("tratamento.id"), default=None)
    fisioterapeuta_id: Column(Integer, ForeignKey("users.id"), default=None)
    quantity: int
    duration: int
    class Config:
        orm_mode = True

class PacienteUpdate(PacienteBase):
    user_id: Optional[int] = Column(Integer, ForeignKey("user.id"), default=None)
    tratamento_id: Optional[int] = Column(Integer, ForeignKey("tratamento.id"), default=None)
    fisioterapeuta_id: Optional[int] = Column(Integer, ForeignKey("fisioterapeuta.id"), default=None)
    quantity: Optional[int] = None
    duration: Optional[int] = None