from sqlalchemy.orm import Session
from app.schemas import TrackCreate
from app.models import Track


def create_track(db: Session, track_dto: TrackCreate):
    db_track = Track(title=track_dto.title, duration=track_dto.duration,
                     released_date=track_dto.released_date)
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track


def get_tracks(db: Session):
    return db.query(Track).all()