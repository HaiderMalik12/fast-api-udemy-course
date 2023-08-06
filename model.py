from pydantic import BaseModel


class TrackModel(BaseModel):
    id: int
    title: str


class TrackUpdateModel(BaseModel):
    title: str
