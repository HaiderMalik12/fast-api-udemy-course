from fastapi import APIRouter
from model import TrackModel, TrackUpdateModel

tracks_router = APIRouter()

tracks = []


@tracks_router.get("/tracks")
def get_tracks() -> dict:
    return {
        "tracks": tracks
    }


@tracks_router.post("/tracks")
def create_track(track: TrackModel) -> dict:
    tracks.append(track)
    return {
        "tracks": tracks
    }


@tracks_router.get("/tracks/{track_id}")
def get_track_by_id(track_id: int) -> dict:
    for track in tracks:
        if track.id == track_id:
            return {"track": track}


@tracks_router.delete("/tracks/{track_id}")
def get_track_by_id(track_id: int) -> dict:
    for index in range(len(tracks)):
        track = tracks[index]
        if track.id == track_id:
            tracks.pop(index)
            return {"message": "Track deleted"}


@tracks_router.put("/tracks/{track_id}")
def get_track_by_id(track_id: int, track_dto: TrackUpdateModel) -> dict:
    tracks_len_response = len(tracks)
    print(tracks_len_response)
    for index in range(tracks_len_response):
        track = tracks[index]
        if track.id == track_id:
            track.title = track_dto.title
            return {"track": track}
