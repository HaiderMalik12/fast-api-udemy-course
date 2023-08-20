from sqlalchemy.orm import Session
from schemas import TrackCreate
from models import Track


def create_track(db: Session, track_dto: TrackCreate):
    db_track = Track(title=track_dto.title, duration=track_dto.duration,
                     released_date=track_dto.released_date)
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track
