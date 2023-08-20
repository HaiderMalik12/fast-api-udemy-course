from typing import List
from sqlalchemy.orm import Session

from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas import TrackModel, TrackUpdateModel, Track, TrackCreate
from app.dependencies import get_db
from app.crud.tracks_crud import create_track

tracks_router = APIRouter()

tracks = []


@tracks_router.get("/tracks", response_model=List[TrackModel])
def get_tracks():
    return tracks


@tracks_router.post("/tracks", response_model=Track)
def create_track_route(track_dto: TrackCreate, db: Session = Depends(get_db)):
    return create_track(db=db, track_dto=track_dto)


@tracks_router.get("/tracks/{track_id}")
def get_track_by_id(track_id: int) -> TrackModel:
    for track in tracks:
        if track.id == track_id:
            return track

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The track does not exist"
    )


@tracks_router.delete("/tracks/{track_id}")
def get_track_by_id(track_id: int) -> dict:
    for index in range(len(tracks)):
        track = tracks[index]
        if track.id == track_id:
            tracks.pop(index)
            return {"message": "Track deleted"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The track does not exist"
    )


@tracks_router.put("/tracks/{track_id}")
def get_track_by_id(track_id: int, track_dto: TrackUpdateModel) -> TrackModel:
    tracks_len_response = len(tracks)
    print(tracks_len_response)
    for index in range(tracks_len_response):
        track = tracks[index]
        if track.id == track_id:
            track.title = track_dto.title
            return track

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The track does not exist"
    )
