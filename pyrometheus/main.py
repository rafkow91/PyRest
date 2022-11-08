from fastapi import FastAPI
from pyrometheus.routers import (
    attachments,
    bookings,
    customers,
    ships,
)

app = FastAPI()
app.include_router(ships.router)
app.include_router(bookings.router)
app.include_router(customers.router)
app.include_router(attachments.router)


@app.get('/')
async def root():
    return {'message': 'Hello World'}
