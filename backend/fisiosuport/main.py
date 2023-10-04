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
    return {"Ok": True}


# Types
@app.get("/types/", response_model=list[schemas.Type])
async def read_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    types = crud.get_type(db, skip=skip, limit=limit)
    return types

@app.get("/types/{name}", response_model=schemas.Type)
async def get_type(name: str, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_name(db, name=name)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type não encontrado")
    return db_type

@app.post("/types/", response_model=schemas.Type)
async def create_type(type: schemas.TypeCreate, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_name(db, name=type.name)
    if db_type:
        raise HTTPException(status_code=400, detail="User Type já cadastrado")
    return crud.create_user_type(db=db, type=type)


@app.get("/types/{id}", response_model=schemas.Type)
async def get_type(id: int, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_id(db, id=id)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type não encontrado")
    return db_type