from pydantic import BaseModel, EmailStr
from datetime import date, time


class TrackBase(BaseModel):
    title: str
    released_date: date | None = None
    duration: time | None = None


class TrackCreate(TrackBase):
    pass


class TrackUpdate(BaseModel):
    title: str | None = None
    released_date: date | None = None
    duration: time | None = None


class Track(TrackBase):
    id: int

    class Config:
        form_attributes = True


class TrackModel(BaseModel):
    id: int
    title: str


class TrackUpdateModel(BaseModel):
    title: str


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        form_attributes = True


class Login(BaseModel):
    email: EmailStr
    password: str
