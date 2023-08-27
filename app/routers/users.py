from fastapi import APIRouter
from .. import schemas

users_router = APIRouter()

# Singup new user


@users_router.post("/users")
def create_user(user_dto: schemas.UserCreate):
    return 'Signup Route'
