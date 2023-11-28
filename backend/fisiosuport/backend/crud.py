from sqlalchemy.orm import Session, aliased

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_user_by_document(db: Session, document: int):
    return db.query(models.User).filter(models.User.document == document).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Preciso alterar aqui pra receber o id do type e o documento
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, password=fake_hashed_password, type_id = user.type_id, birth_date = user.birth_date, document = user.document)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: str, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {"ok":True}


def get_type(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Types).offset(skip).limit(limit).all()

def get_type_by_id(db: Session, id: int):
    return db.query(models.Types).filter(models.Types.id == id).first()


def get_type_by_name(db: Session, name: str):
    return db.query(models.Types).filter(models.Types.name == name).first()

def create_user_type(db: Session, type: schemas.TypeCreate):
    db_type = models.Types(name=type.name)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

def update_type(db: Session, type_id: str, type: schemas.TypeUpdate):
    db_type = db.query(models.Types).filter(models.Types.id == type_id).first()
    type_data = type.dict(exclude_unset=True)
    for key, value in type_data.items():
        setattr(db_type, key, value)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type


def get_specialty(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Specialty).offset(skip).limit(limit).all()


def get_specialty_by_id(db: Session, id: int):
    return db.query(models.Specialty).filter(models.Specialty.id == id).first()

def get_specialty_by_name(db: Session, name: str):
    return db.query(models.Specialty).filter(models.Specialty.name == name).first()

def create_specialty(db: Session, specialty: schemas.SpecialtyCreate):
    db_specialty = models.Specialty(name=specialty.name)
    db.add(db_specialty)
    db.commit()
    db.refresh(db_specialty)
    return db_specialty

def update_specialty(db: Session, specialty_id: str, specialty: schemas.SpecialtyUpdate):
    db_specialty = db.query(models.Specialty).filter(models.Specialty.id == specialty_id).first()
    specialty_data = specialty.dict(exclude_unset=True)
    for key, value in specialty_data.items():
        setattr(db_specialty, key, value)
    db.add(db_specialty)
    db.commit()
    db.refresh(db_specialty)
    return db_specialty

def delete_specialty(db: Session, specialty_id: str):
    specialty = db.query(models.Specialty).filter(models.Specialty.id == specialty_id).first()
    db.delete(specialty)
    db.commit()
    return {"ok":True}


def get_patient_by_id(db: Session, id: int):
    return db.query(models.Patient).filter(models.Patient.id == id).first()

def get_patient_by_name(db: Session, name: str):
    return db.query(models.Patient).filter(models.patient.name == name).first()


# Adc validações
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.patient(name=patient.name)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: str, patient: schemas.PatientUpdate):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    patient_data = patient.dict(exclude_unset=True)
    for key, value in patient_data.items():
        setattr(db_patient, key, value)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: str):
    patient = db.query(models.Patient).filter(models.patient.id == patient_id).first()
    db.delete(patient)
    db.commit()
    return {"ok":True}


# Treament


def get_treatments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Treatment).offset(skip).limit(limit).all()

def get_treatment_by_id(db: Session, id: int):
    return db.query(models.Treatment).filter(models.Treatment.id == id).first()

def get_treatment_by_name(db: Session, name: str):
    return db.query(models.Treatment).filter(models.Treatment.name == name).first()

def create_treatment(db: Session, treatment: schemas.TreatmentCreate):
    db_treatment = models.Treatment(name=treatment.name, video=treatment.video)
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    return db_treatment

def update_treatment(db: Session, treatment_id: str, treatment: schemas.TreatmentUpdate):
    db_treatment = db.query(models.Treatment).filter(models.Treatment.id == treatment_id).first()
    treatment_data = treatment.dict(exclude_unset=True)
    for key, value in treatment_data.items():
        setattr(db_treatment, key, value)
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    return db_treatment

def delete_treatment(db: Session, treatment_id: str):
    treatment = db.query(models.Treatment).filter(models.Treatment.id == treatment_id).first()
    db.delete(treatment)
    db.commit()
    return {"ok":True}

# physiotherapist
def get_physiotherapist(db: Session, skip: int = 0, limit: int = 100):
    
    # specialty = aliased(models.Specialty.name, name="specialty")
    return (db.query(models.User.id, models.User.name
                    , models.User.document
                    , models.User.birth_date
                    , models.Specialty.name.label('specialty'))
                .join(models.Physiotherapist, models.User.id == models.Physiotherapist.user_id)
                .join(models.Specialty, models.Physiotherapist.specialty_id == models.Specialty.id)
                .filter(models.User.type_id == 1)
                .filter(models.User.is_active == True)
                .offset(skip)
                .limit(limit)
                .all())

def get_physiotherapist_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()

def get_physiotherapist_by_name(db: Session, name: str):
    return db.query(models.Physiotherapist).filter(models.Physiotherapist.name == name).first()

def create_physiotherapist(db: Session, physiotherapist: schemas.PhysiotherapistCreate):
    db_physiotherapist = models.Physiotherapist(user_id=physiotherapist.user_id, specialty_id=physiotherapist.specialty_id)
    db.add(db_physiotherapist)
    db.commit()
    db.refresh(db_physiotherapist)
    return db_physiotherapist

def update_physiotherapist(db: Session, physiotherapist_id: str, physiotherapist: schemas.PhysiotherapistUpdate):
    db_physiotherapist = db.query(models.Physiotherapist).filter(models.Physiotherapist.id == physiotherapist_id).first()
    physiotherapist_data = physiotherapist.dict(exclude_unset=True)
    for key, value in physiotherapist_data.items():
        setattr(db_physiotherapist, key, value)
    db.add(db_physiotherapist)
    db.commit()
    db.refresh(db_physiotherapist)
    return db_physiotherapist

def delete_physiotherapist(db: Session, physiotherapist_id: str):
    physiotherapist = db.query(models.Physiotherapist).filter(models.Physiotherapist.id == physiotherapist_id).first()
    db.delete(physiotherapist)
    db.commit()
    return {"ok":True}

def get_patient(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Physiotherapist).filter(models.User.type_id == 2).offset(skip).limit(limit).all()

def get_patient_by_id(db: Session, id: int):
    return db.query(models.patient).filter(models.patient.id == id).first()

def get_patient_by_name(db: Session, name: str):
    return db.query(models.patient).filter(models.patient.name == name).first()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.patient(name=patient.name)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: str, patient: schemas.PatientUpdate):
    db_patient = db.query(models.patient).filter(models.patient.id == patient_id).first()
    patient_data = patient.dict(exclude_unset=True)
    for key, value in patient_data.items():
        setattr(db_patient, key, value)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: str):
    patient = db.query(models.patient).filter(models.patient.id == patient_id).first()
    db.delete(patient)
    db.commit()
    return {"ok":True}