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
class SpecialtyBase(BaseModel):
    name: str

class Specialty(SpecialtyBase):
    id: int
    name: str
    class Config:
        orm_mode = True

class SpecialtyCreate(SpecialtyBase):
	name: str	

class SpecialtyUpdate(SpecialtyBase):
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
    
class TreatmentCreate(TreatmentBase):
    id: int
    name: str
    video: str
    

# Physiotherapist
class PhysiotherapistBase(BaseModel):
    user_id: int
    specialty_id: int

class Physiotherapist(PhysiotherapistBase):
    user_id: int
    specialty_id: int
    class Config:
        orm_mode = True

class PhysiotherapistUpdate(PhysiotherapistBase):
    user_id: Optional[int] = None
    specialty_id: Optional[int] = None
    
class PhysiotherapistCreate(PhysiotherapistBase):
    user_id: int
    specialty_id: int
    
# patient
# Preciso revisar a necessidade de relacionamento aqui
class PatientBase(BaseModel):
    id: int
    quantity: int
    duration: int
    user_id: int
    treatment_id: int
    fisioterapeuta_id: int
    
class PatientCreate(PatientBase):
    id: int
    quantity: int
    duration: int
    user_id: int
    treatment_id: int
    fisioterapeuta_id: int

class Patient(PatientBase):
    id: int
    user_id: int
    treatment_id: int
    fisioterapeuta_id: int
    quantity: int
    duration: int
    class Config:
        orm_mode = True

class PatientUpdate(PatientBase):
    treatment_id: Optional[int] = None
    fisioterapeuta_id: Optional[int] = None
    quantity: Optional[int] = None
    duration: Optional[int] = None
    
