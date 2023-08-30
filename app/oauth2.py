from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, dependencies, models
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordBearer

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(data: dict):
    to_encode = data.copy()  # Clone the data

    # find expiry date or time
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # update the expiry date/time on dictonary
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,
                             algorithm=ALGORITHM)  # encode the token xxxx.sdddd.eeerree

    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if not id:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme),  db: Session = Depends(dependencies.get_db)):
    credentials_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                           detail=f"could not validate credentials",
                                           headers={"WWW-Authenticate": "Bearer"})
    token = verify_token(token, credentials_exceptions)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
