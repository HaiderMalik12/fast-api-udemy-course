from fastapi import FastAPI

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
