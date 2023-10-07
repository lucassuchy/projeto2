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
    type_id: int
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
    type_id: int
    document: int
    birth_date: date
    

class UserUpdate(UserBase):
    name: Optional[str] = None
    document: Optional[int] = None
    type_id: Optional[int] = None
    password: Optional[str] = None
    birth_date: Optional[date] = None

# specialty
class specialtyBase(BaseModel):
    id: int
    name: str

class specialty(specialtyBase):
    id: int
    name: str
    class Config:
        orm_mode = True

class specialtyUpdate(specialtyBase):
    name: Optional[str] = None

# treatment
class TreatmentBase(BaseModel):
    id: int
    name: str
    video: str

class Treatment(TreatmentBase):
    id: int
    name: str
    video: str
    class Config:
        orm_mode = True

class TreatmentUpdate(TreatmentBase):
    name: Optional[str] = None
    video: Optional[str] = None

# Paciente
# Preciso revisar a necessidade de relacionamento aqui
class PacienteBase(BaseModel):
    id: int
    quantity: int
    duration: int
    user_id: int
    treatment_id: int
    fisioterapeuta_id: int

class Paciente(PacienteBase):
    id: int
    user_id: int
    treatment_id: int
    fisioterapeuta_id: int
    quantity: int
    duration: int
    class Config:
        orm_mode = True

class PacienteUpdate(PacienteBase):
    user_id: Optional[int] = Column(Integer)
    treatment_id: Optional[int] = Column(Integer)
    fisioterapeuta_id: Optional[int] = Column(Integer)
    quantity: Optional[int] = None
    duration: Optional[int] = None