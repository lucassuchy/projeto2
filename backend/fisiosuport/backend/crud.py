from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_user_by_document(db: Session, documento: int):
    return db.query(models.User).filter(models.User.documento == documento).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Preciso alterar aqui pra receber o id do type e o documento
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, hashed_password=fake_hashed_password, type_id = user.type_id, documento = user.documento)
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

def delete_type(db: Session, type_id: str):
    type = db.query(models.Types).filter(models.Types.id == type_id).first()
    db.delete(type)
    db.commit()
    return {"ok":True}

def create_user_type(db: Session, type: schemas.TypeCreate):
    db_type = models.Types(**type.dict())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type
