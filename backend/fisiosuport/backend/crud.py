from sqlalchemy.orm import Session, aliased, load_only

from . import models, schemas

## API

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

# Preciso alterar aqui pra receber o id do type e o documento
def login_user(db: Session, user: schemas.UserLogin):
    db_user = db.query(models.User).filter(models.User.document == user.document).first()
    if db_user:
        if db_user.password == user.password:
            return {"ok":True}
        else:
            return {"ok":False}
    else:
        return {"ok":False}

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
    retorno = db.query(models.Types).offset(skip).limit(limit).all()
    print(retorno)
    print(type(retorno))
    return retorno

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


# Treament


def get_treatments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Treatment).offset(skip).limit(limit).all()

def get_treatment_by_id(db: Session, id: int):
    return db.query(models.Treatment).filter(models.Treatment.id == id).first()

def get_treatment_by_name(db: Session, name: str):
    return db.query(models.Treatment).filter(models.Treatment.name == name).first()

def create_treatment(db: Session, treatment: schemas.TreatmentCreate):
    db_treatment = models.Treatment(name=treatment.name)
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    for videos in treatment.video_id:
        db_treatment_video = models.Videos_Treatment(treatment_id = db_treatment.id, video_id = videos)
        db.add(db_treatment_video)
        db.commit()
        db.refresh(db_treatment_video)
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
    '''
    select a.id, a.name,a.document, a.is_active,a.type_id, c.name from users a
            inner join physiotherapist b on a.id = b.user_id
            inner join specialty c on b.specialty_id = c.id 
    '''
    '''
    models.User.id.label('id')
                    , models.User.name
                    , models.User.document
                    , models.User.birth_date
                    , models.Specialty.name.label('specialty')
    '''
    retorno = (db.query(models.User, )
                .join(models.Physiotherapist, models.User.id == models.Physiotherapist.user_id)
                .join(models.Specialty, models.Physiotherapist.specialty_id == models.Specialty.id)
                .with_entities(models.User.id.label('id')
                    , models.User.name
                    , models.User.document
                    , models.User.birth_date
                    , models.Specialty.name.label('specialty'))
                .filter(models.User.type_id == 1)
                .filter(models.User.is_active == True)
                .offset(skip)
                .limit(limit)
                .all())
    return retorno

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
    ''' 
    select c.id as "patient_id"
    , b.name as "patient"
    , b.birth_date
    , a.quantity
    , a.duration
    , a.description
    , c.name as "treatment"
    , d.id as "physiotherapist_id"
    , d.name as "physiotherapist_id"
            from patient a 
            inner join users b on a.user_id = b.id 
            inner join treatment c on a.treatment_id = c.id
            inner join users d on a.physiotherapist_id = d.id;
    '''

    retorno = (db.query(models.User.name.label('patient')
                        , models.Treatment.name.label('treatment')
                        , models.User.id.label('patient_id')
                        , models.Patient.quantity
                        , models.Patient.duration
                        , models.Patient.description
                        , models.Treatment.name.label('treatment')
                     )
                .join(models.Patient, models.Patient.user_id == models.User.id)
                .join(models.Treatment, models.Treatment.id == models.Patient.treatment_id)      
                .filter(models.User.type_id == 2)
                .filter(models.User.is_active == True)
                .limit(limit)
                .offset(skip)
                .all())
    return  retorno

def get_patient_by_id(db: Session, id: int):
    retorno = (db.query(models.User.name.label('patient')
                        , models.User.document
                        , models.Treatment.name.label('treatment')
                        , models.User.id.label('patient_id')
                        , models.User.birth_date
                        , models.Patient.quantity
                        , models.Patient.duration
                        , models.Treatment.name.label('treatment')
                        , models.Treatment.id.label('treatment_id')
                     )
                .join(models.Patient, models.Patient.user_id == models.User.id)
                .join(models.Treatment, models.Treatment.id == models.Patient.treatment_id)      
                .filter(models.User.type_id == 2)
                .filter(models.User.is_active == True)
                .filter(models.User.id == id)
                .first())
    return  retorno

def get_patient_by_user_id(db: Session, user_id: int):
    return db.query(models.Patient).filter(models.Patient.user_id == user_id).first()

def get_patient_by_name(db: Session, name: str):
    return db.query(models.Patient).filter(models.Patient.name == name).first()

def create_patient(db: Session, patient: schemas.PatientCreate):
    fake_hashed_password = patient.password + "notreallyhashed"
    db_user = models.User(name=patient.name
                        , password=fake_hashed_password
                        , type_id = patient.type_id
                        , birth_date = patient.birth_date
                        , document = patient.document)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_patient = models.Patient(quantity=patient.quantity
                                , duration = patient.duration
                                , user_id = db_user.id
                                , treatment_id = patient.treatment_id
                                , physiotherapist_id = patient.physiotherapist_id
                                , description = patient.description)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: str, patient: schemas.PatientUpdate):
    ## Atualiza na user
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    patient_data = patient.dict(exclude_unset=True)
    for key, value in patient_data.items():
        setattr(db_patient, key, value)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    db_user = db.query(models.User).filter(models.User.id == patient.user_id).first()
    user_data = patient.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_patient

def delete_patient(db: Session, patient_id: str):
    patient = db.query(models.patient).filter(models.patient.id == patient_id).first()
    db.delete(patient)
    db.commit()
    return {"ok":True}


### Videos

def get_Video(db: Session, Video_id: int):
    return db.query(models.Videos).filter(models.Videos.id == Video_id).first()

def get_Video_by_name(db: Session, name: str):
    return db.query(models.Videos).filter(models.Videos.name == name).first()

def get_Videos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Videos.id.label('value')
                    , models.Videos.name.label('label')).offset(skip).limit(limit).all()


def get_exercicios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Videos).offset(skip).limit(limit).all()


# Preciso alterar aqui pra receber o id do type e o documento
def create_Video(db: Session, Video: schemas.VideoCreate):
    db_Video = models.Videos(name=Video.name, url = Video.url)
    db.add(db_Video)
    db.commit()
    db.refresh(db_Video)
    return db_Video

def update_Video(db: Session, Video_id: str, Video: schemas.VideoUpdate):
    db_Video = db.query(models.Videos).filter(models.Videos.id == Video_id).first()
    Video_data = Video.dict(exclude_unset=True)
    for key, value in Video_data.items():
        setattr(db_Video, key, value)
    db.add(db_Video)
    db.commit()
    db.refresh(db_Video)
    return db_Video


def delete_Video(db: Session, Video_id: str):
    Video = db.query(models.Videos).filter(models.Videos.id == Video_id).first()
    db.delete(Video)
    db.commit()
    return {"ok":True}