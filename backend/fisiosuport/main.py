from fastapi import Depends, FastAPI, HTTPException
from .backend import crud, models
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from .backend import schemas, crud, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Users
@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario já cadastrado")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/documento/{documento}", response_model=schemas.User)
def read_user(documento: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_document(db, documento=documento)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User não encontrado")
    return db_user

@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User não encontrado")
    return db_user

@app.patch("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id:int ,user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User não encontrado")
    return crud.update_user(db=db, user=user, user_id=user_id)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not crud.get_user(db, user_id = user_id):
        raise HTTPException(status_code=404, detail="User não encontrado")
    crud.delete_user(db, user_id = user_id)
    # Mudar a mensagem de retorno
    return {"Ok": True}


# Types
@app.get("/type/", response_model=list[schemas.Type])
async def read_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    type = crud.get_type(db, skip=skip, limit=limit)
    return type

@app.get("/type/name/{name}", response_model=schemas.Type)
async def get_type(name: str, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_name(db, name=name)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type não encontrado")
    return db_type

@app.post("/type/", response_model=schemas.Type)
async def create_user_type(type: schemas.TypeCreate, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_name(db, name=type.name)
    if db_type:
        raise HTTPException(status_code=400, detail="Type já cadastrado")
    return crud.create_user_type(db=db, type=type)

@app.get("/type/{id}", response_model=schemas.Type)
async def get_type(id: int, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_id(db, id=id)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type não encontrado")
    return db_type

@app.patch("/type/{id}", response_model=schemas.Type)
async def update_type(id:int ,type: schemas.TypeUpdate, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_id(db, id=id)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type não encontrado")
    return crud.update_type(db=db, type=type, type_id=id)

# specialty
@app.get("/specialty/", response_model=list[schemas.Specialty])
async def read_specialty(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    type = crud.get_specialty(db, skip=skip, limit=limit)
    return type

@app.post("/specialty/", response_model=schemas.Specialty)
async def create_specialty(specialty: schemas.SpecialtyCreate, db: Session = Depends(get_db)):
    db_specialty = crud.get_specialty_by_name(db, name=specialty.name)
    if db_specialty:
        raise HTTPException(status_code=400, detail="specialty já cadastrado")
    return crud.create_specialty(db=db, specialty=specialty)

@app.get("/specialty/{id}", response_model=schemas.Specialty)
async def get_specialty(id: int, db: Session = Depends(get_db)):
    db_specialty = crud.get_specialty_by_id(db, id=id)
    if db_specialty is None:
        raise HTTPException(status_code=404, detail="Specialty não encontrado")
    return db_specialty

@app.get("/specialty/name/{name}", response_model=schemas.Type)
async def get_specialty_name(name: str, db: Session = Depends(get_db)):
    db_specialty = crud.get_specialty_by_name(db, name=name)
    if db_specialty is None:
        raise HTTPException(status_code=404, detail="Specialty não encontrado")
    return db_specialty

@app.patch("/specialty/{id}", response_model=schemas.Specialty)
async def update_specialty(id:int ,specialty: schemas.SpecialtyUpdate, db: Session = Depends(get_db)):
    db_specialty = crud.get_specialty_by_id(db, id=id)
    if db_specialty is None:
        raise HTTPException(status_code=404, detail="Specialty não encontrado")
    return crud.update_specialty(db=db, specialty=specialty, specialty_id=id)

@app.delete("/specialty/{specialty_id}")
def delete_specialty(specialty_id: int, db: Session = Depends(get_db)):
    if not crud.get_specialty_by_id(db, id = specialty_id):
        raise HTTPException(status_code=404, detail="Specialty não encontrado")
    crud.delete_specialty(db, specialty_id = specialty_id)
    # Mudar a mensagem de retorno
    return {"Ok": True}


# treatment
@app.get("/treatment/", response_model=list[schemas.Treatment])
async def read_treatment(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    type = crud.get_treatment(db, skip=skip, limit=limit)
    return type

@app.post("/treatment/", response_model=schemas.Treatment)
async def create_treatment(treatment: schemas.TreatmentCreate, db: Session = Depends(get_db)):
    db_treatment = crud.get_treatment_by_name(db, name=treatment.name)
    if db_treatment:
        raise HTTPException(status_code=400, detail="treatment já cadastrado")
    return crud.create_treatment(db=db, treatment=treatment)

@app.get("/treatment/{id}", response_model=schemas.Treatment)
async def get_treatment(id: int, db: Session = Depends(get_db)):
    db_treatment = crud.get_treatment_by_id(db, id=id)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="treatment não encontrado")
    return db_treatment

@app.get("/treatment/name/{name}", response_model=schemas.Treatment)
async def get_treatment_name(name: str, db: Session = Depends(get_db)):
    db_treatment = crud.get_treatment_by_name(db, name=name)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="treatment não encontrado")
    return db_treatment

@app.patch("/treatment/{id}", response_model=schemas.Treatment)
async def update_treatment(id:int ,treatment: schemas.TreatmentUpdate, db: Session = Depends(get_db)):
    db_treatment = crud.get_treatment_by_id(db, id=id)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="treatment não encontrado")
    return crud.update_treatment(db=db, treatment=treatment, treatment_id=id)

@app.delete("/treatment/{treatment_id}")
def delete_treatment(treatment_id: int, db: Session = Depends(get_db)):
    if not crud.get_treatment_by_id(db, id = treatment_id):
        raise HTTPException(status_code=404, detail="treatment não encontrado")
    crud.delete_treatment(db, treatment_id = treatment_id)
    # Mudar a mensagem de retorno
    return {"Ok": True}

# physiotherapist
@app.get("/physiotherapist/", response_model=list[schemas.Physiotherapist])
async def read_physiotherapist(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    type = crud.get_physiotherapist(db, skip=skip, limit=limit)
    return type

@app.post("/physiotherapist/", response_model=schemas.Physiotherapist)
async def create_physiotherapist(physiotherapist: schemas.PhysiotherapistCreate, db: Session = Depends(get_db)):
    db_physiotherapist = crud.get_physiotherapist_by_name(db, name=physiotherapist.name)
    if db_physiotherapist:
        raise HTTPException(status_code=400, detail="physiotherapist já cadastrado")
    return crud.create_physiotherapist(db=db, physiotherapist=physiotherapist)

@app.get("/physiotherapist/{id}", response_model=schemas.Physiotherapist)
async def get_physiotherapist(id: int, db: Session = Depends(get_db)):
    db_physiotherapist = crud.get_physiotherapist_by_id(db, id=id)
    if db_physiotherapist is None:
        raise HTTPException(status_code=404, detail="physiotherapist não encontrado")
    return db_physiotherapist

@app.get("/physiotherapist/name/{name}", response_model=schemas.Physiotherapist)
async def get_physiotherapist_name(name: str, db: Session = Depends(get_db)):
    db_physiotherapist = crud.get_physiotherapist_by_name(db, name=name)
    if db_physiotherapist is None:
        raise HTTPException(status_code=404, detail="physiotherapist não encontrado")
    return db_physiotherapist

@app.patch("/physiotherapist/{id}", response_model=schemas.Physiotherapist)
async def update_physiotherapist(id:int ,physiotherapist: schemas.PhysiotherapistUpdate, db: Session = Depends(get_db)):
    db_physiotherapist = crud.get_physiotherapist_by_id(db, id=id)
    if db_physiotherapist is None:
        raise HTTPException(status_code=404, detail="physiotherapist não encontrado")
    return crud.update_physiotherapist(db=db, physiotherapist=physiotherapist, physiotherapist_id=id)

@app.delete("/physiotherapist/{physiotherapist_id}")
def delete_physiotherapist(physiotherapist_id: int, db: Session = Depends(get_db)):
    if not crud.get_physiotherapist_by_id(db, id = physiotherapist_id):
        raise HTTPException(status_code=404, detail="physiotherapist não encontrado")
    crud.delete_physiotherapist(db, physiotherapist_id = physiotherapist_id)
    # Mudar a mensagem de retorno
    return {"Ok": True}

# patient
@app.get("/patient/", response_model=list[schemas.Patient])
async def read_patient(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    type = crud.get_patient(db, skip=skip, limit=limit)
    return type

@app.post("/patient/", response_model=schemas.Patient)
async def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_name(db, name=patient.name)
    if db_patient:
        raise HTTPException(status_code=400, detail="Paciente já cadastrado")
    return crud.create_patient(db=db, patient=patient)

@app.get("/patient/{id}", response_model=schemas.Patient)
async def get_patient(id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_id(db, id=id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return db_patient

@app.get("/patient/name/{name}", response_model=schemas.Patient)
async def get_patient_name(name: str, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_name(db, name=name)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="patient não encontrado")
    return db_patient

@app.patch("/patient/{id}", response_model=schemas.Patient)
async def update_patient(id:int ,patient: schemas.PatientUpdate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_id(db, id=id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return crud.update_patient(db=db, patient=patient, patient_id=id)

@app.delete("/patient/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    if not crud.get_patient_by_id(db, id = patient_id):
        raise HTTPException(status_code=404, detail="patient não encontrado")
    crud.delete_patient(db, patient_id = patient_id)
    # Mudar a mensagem de retorno
    return {"Ok": True}