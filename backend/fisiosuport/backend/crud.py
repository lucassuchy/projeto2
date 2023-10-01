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
    db_user = models.User(name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_type(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Types).offset(skip).limit(limit).all()


def create_user_type(db: Session, type: schemas.TypeCreate, user_id: int):
    db_type = models.Types(**type.dict(), owner_id=user_id)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type
