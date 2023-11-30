from pydantic import BaseModel
from typing import  Optional
from sqlalchemy import  Column, ForeignKey, Integer, BigInteger
from sqlalchemy.orm import relationship
from datetime import date

# Type
class TypeBase(BaseModel):
    name: str

class Type(TypeBase):
    id: int
    name: str

    class Config:
        from_attributes = True

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
        from_attributes = True

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
        from_attributes = True

class SpecialtyCreate(SpecialtyBase):
	name: str	

class SpecialtyUpdate(SpecialtyBase):
    name: Optional[str] = None

# treatment
class TreatmentBase(BaseModel):
    name: str
    video: str

class Treatment(TreatmentBase):
    id: int
    name: str
    video: str
    class Config:
        from_attributes = True

class TreatmentUpdate(TreatmentBase):
    name: Optional[str] = None
    video: Optional[str] = None
    
class TreatmentCreate(TreatmentBase):
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
        from_attributes = True

class PhysiotherapistUpdate(PhysiotherapistBase):
    user_id: Optional[int] = None
    specialty_id: Optional[int] = None
    
class PhysiotherapistCreate(PhysiotherapistBase):
    user_id: int
    specialty_id: int
    

class PhysiotherapistOutput(BaseModel):
    id:int
    name: str
    document: int
    birth_date: date
    specialty: str

    class Config:
        from_attributes = True
    
# patient
# Preciso revisar a necessidade de relacionamento aqui
class PatientBase(BaseModel):
    quantity: int
    duration: int
    user_id: int
    treatment_id: int
    physiotherapist_id: int
    
class PatientCreate(PatientBase):
    name: str
    password: str
    type_id: int
    document: int
    user_id: Optional[int] = None
    birth_date: date
    quantity: int
    duration: int
    treatment_id: int
    physiotherapist_id: int

class Patient(PatientBase):
    id: int
    user_id: int
    treatment_id: int
    physiotherapist_id: int
    quantity: int
    duration: int
    class Config:
        from_attributes = True

class PatientUpdate(PatientBase):
    treatment_id: Optional[int] = None
    physiotherapist_id: Optional[int] = None
    quantity: Optional[int] = None
    duration: Optional[int] = None
    
class PatientOut(BaseModel):
    patient_id: int
    patient: str
    quantity: int
    duration: int
    description: Optional[str] = None
    treatment: str
    physiotherapist_id: int
    physiotherapist: str



