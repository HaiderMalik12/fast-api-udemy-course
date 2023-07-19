from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello world!"}


@app.get('/items')
async def get_items():
    return ['item1', 'item2', 'item3']
