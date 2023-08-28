from typing import List
from sqlalchemy.orm import Session

from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas import TrackModel, TrackUpdateModel, Track, TrackCreate, TrackUpdate
from app.dependencies import get_db
from app.crud.tracks_crud import create_track, get_tracks, get_track_by_id, delete_track_by_id, update_track_by_id

tracks_router = APIRouter(
    prefix="/tracks",
    tags=["Tracks"]
)

tracks = []


@tracks_router.get("/", response_model=List[Track])
def get_tracks_route(db: Session = Depends(get_db)):
    return get_tracks(db=db)


@tracks_router.post("/", response_model=Track)
def create_track_route(track_dto: TrackCreate, db: Session = Depends(get_db)):
    return create_track(db=db, track_dto=track_dto)


@tracks_router.get("/{track_id}", response_model=Track)
def get_track_route(track_id: int, db: Session = Depends(get_db)):
    return get_track_by_id(db, track_id)


@tracks_router.delete("/{track_id}")
def delete_track_route(track_id: int, db: Session = Depends(get_db)):
    return delete_track_by_id(db=db, track_id=track_id)


@tracks_router.put("/{track_id}", response_model=Track)
def update_track_route(track_id: int, track_dto: TrackUpdate, db: Session = Depends(get_db)):
    return update_track_by_id(db=db, track_id=track_id, track_dto=track_dto)
