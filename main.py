from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello world, I am learning FAST API"}


@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    return {"item_id": item_id}


@app.get("/albums/{album_id}")
def get_album(album_id: int):
    return {"album_id": album_id}


@app.get("/users/me")
def get_user():
    return {"user": "the current user"}


@app.get("/users/{user_id}")
def get_user_by_id(user_id: str):
    return {"user_id": user_id}


@app.get("/users")
def get_users1():
    return ["ALi", "Sam"]


@app.get("/users")
def get_users():
    return ["john", "sandy"]


class ApplicationType(str, Enum):
    LOAN = 'loan'
    BUSINESS_FINANCING = "business_financing"
    CAR_FINANCING = "car_financing"
    HOME_FINANCING = "home_financing"


@app.get('/application/{app_type}')
def get_application(app_type: ApplicationType):
    print(app_type)
    if app_type is ApplicationType.LOAN:
        return {"app_type": app_type}
    if app_type.value == 'business_financing':
        return {"app_type": app_type}
    if app_type.value == 'car_financing':
        return {"app_type": app_type}
    if app_type.value == 'home_financing':
        return {"app_type": app_type}
    return {"app_type": app_type}

# Query Parameters


@app.get("/songs")
def get_songs(skip: int = 1, limit: int = 10, page: int = 1, per_page: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "page": page,
        "per_page": per_page
    }

# Multiple Query Parameters


# @app.get("/playlist/{playlist_id}/songs/{song_id}")
# def get_songs_by_playlist(playlist_id: int, song_id: int):
#     return {
#         "song_id": song_id,
#         "playlist_id": playlist_id
#     }


@app.get("/playlist/{playlist_id}/songs/{song_id}")
def get_songs_by_playlist(playlist_id: int, song_id: int, q: str = ""):
    return {
        "song_id": song_id,
        "playlist_id": playlist_id
    }
