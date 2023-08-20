from sqlalchemy import Column, String, Integer, DATE, TIME
from .database import Base


class Track(Base):
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    released_date = Column(DATE)
    duration = Column(TIME)
