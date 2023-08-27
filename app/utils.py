
from passlib.context import CryptContext

# This would be my default hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash_password) -> bool:
    return pwd_context.verify(password, hash_password)
