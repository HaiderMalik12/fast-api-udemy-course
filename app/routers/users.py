from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, dependencies, models, utils

users_router = APIRouter()

# Singup new user


@users_router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    hashed_password = utils.get_hashed_password(user.password)
    user.password = hashed_password
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
