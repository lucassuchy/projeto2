from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario já cadastrado")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User não encontrado")
    return db_user

@app.get("/users/{documento}", response_model=schemas.User)
def read_user(documento: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_document(db, documento=documento)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User não encontrado")
    return db_user


@app.post("/users/{user_id}/type/", response_model=schemas.Type)
def create_type_for_user(
    user_id: int, Type: schemas.TypeCreate, db: Session = Depends(get_db)
):
    return crud.create_user_type(db=db, Type=type, user_id=user_id)


@app.get("/types/", response_model=list[schemas.Type])
def read_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    types = crud.get_type(db, skip=skip, limit=limit)
    return types
