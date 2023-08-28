from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, utils, dependencies, schemas

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Login route


@auth_router.post("/login")
def login(auth_dto: schemas.Login, db: Session = Depends(dependencies.get_db)):
    user = db.query(models.User).filter(
        models.User.email == auth_dto.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong credentials")

    verified = utils.verify_password(auth_dto.password, user.password)

    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return {"token": "SADASD"}
