from fastapi import FastAPI
from .routers import tracks_router
from .database import engine

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello world, I am learning FAST API"}

app.include_router(tracks_router)
