from pydantic import BaseModel
from typing import  Optional, Union
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



class UserLogin(BaseModel):
    document: int
    password: str
    class Config:
        orm_mode = True

class UserLoginCreate(BaseModel):
    document: int
    password: str
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

class UserInDB(UserBase):
    password: str

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
    name: str

class Treatment(TreatmentBase):
    id: int
    name: str
    class Config:
        orm_mode = True

class TreatmentUpdate(TreatmentBase):
    name: Optional[str] = None
    
class TreatmentCreate(TreatmentBase):
    name: str
    video_id: list 


    
# Physiotherapist
class PhysiotherapistBase(BaseModel):
    user_id: int
    specialty_id: int
    class Config:
        orm_mode = True

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
        orm_mode  = True
    
# patient
# Preciso revisar a necessidade de relacionamento aqui
class PatientBase(BaseModel):
    quantity: int
    duration: int
    user_id: int
    treatment_id: int
    physiotherapist_id: int
    class Config:
        orm_mode = True


class Patient(PatientBase):
    id: int
    user_id: int
    treatment_id: int
    physiotherapist_id: int
    quantity: int
    duration: int
    description: Optional[str] = None
    class Config:
        orm_mode = True

class PatientUpdate(BaseModel):
    name:  Optional[str] = None
    document:  Optional[int] = None
    user_id: Optional[int] = None
    description: Optional[str] = None
    birth_date:  Optional[date] = None
    quantity:  Optional[int] = None
    duration:  Optional[int] = None
    treatment_id:  Optional[int] = None
    physiotherapist_id:  Optional[int] = None
    class Config:
        orm_mode = True

class PatientCreate(PatientBase):
    name: str
    password: str
    type_id: int
    document: int
    user_id: Optional[int] = None
    description: Optional[str] = None
    birth_date: date
    quantity: int
    duration: int
    treatment_id: int
    physiotherapist_id: int
  
class PatientOut(BaseModel):
    patient_id: Union[int, None]
    patient: Union[str, None]
    quantity: Union[int, None]
    duration: Union[int, None]
    description: Union[str, None]
    treatment: Union[str, None]
    class Config:
        orm_mode = True


class PatientOutEdit(BaseModel):
    patient_id: Union[int, None]
    patient: Union[str, None]
    quantity: Union[int, None]
    duration: Union[int, None]
    birth_date: Union[date, None]
    document: Union[int, None]
    description: Union[str, None]
    treatment: Union[str, None]
    treatment_id: Union[int, None]
    class Config:
        orm_mode = True

## Finalizar a alteração dos schemas dos videos 
class VideosBase(BaseModel):
    name: Union[str, None]
    url: Union[str, None]
    class Config:
        orm_mode = True

class Video(VideosBase):
    id: Union[int, None]
    name: Union[str, None]
    url: Union[str, None]

class VideoUpdate(VideosBase):
    name: Optional[str] = None
    url: Optional[str] = None

class VideoCreate(VideosBase):
    name: Optional[str] = None
    url: Optional[str] = None

class VideoOutput(BaseModel):
    value: Union[int, None]
    label: Union[str, None]
    class Config:
        orm_mode = True
