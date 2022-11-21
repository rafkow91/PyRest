from fastapi import FastAPI, Request, Response

from sqlalchemy.orm import sessionmaker

from pyrometheus.database import engine
from pyrometheus.routers import (
    attachments,
    bookings,
    customers,
    ships,
)

app = FastAPI()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internal server error', status_code=500)

    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response

app.include_router(attachments.router)
app.include_router(bookings.router)
app.include_router(customers.router)
app.include_router(ships.router)


@app.get('/')
async def root():
    return {'message': 'Hello World'}

