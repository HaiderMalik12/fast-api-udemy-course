from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, utils, dependencies, schemas, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Login route


@auth_router.post("/login", response_model=schemas.Token)
def login(auth_dto: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dependencies.get_db)):
    user = db.query(models.User).filter(
        models.User.email == auth_dto.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong credentials")

    verified = utils.verify_password(auth_dto.password, user.password)

    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = oauth2.create_access_token(data={
        "user_id": user.id
    })

    return {"access_token": access_token, "token_type": "bearer"}
