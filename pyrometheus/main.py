from fastapi import FastAPI
from pyrometheus.routers import ships

app = FastAPI()
app.include_router(ships.router)


@app.get('/')
async def root():
    return {'message': 'Hello World'}
