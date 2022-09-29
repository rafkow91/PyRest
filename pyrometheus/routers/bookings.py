from datetime import date
from pydantic import BaseModel
from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix='/bookings',
    tags=['bookings']
)


class BookingSchema(BaseModel):
    id: Optional[int]
    spaceship_id: int
    customer_id: int
    date_start: date
    date_end: date


@router.get('/')
async def index():
    return {'message': 'list of bookings'}


@router.post('/')
async def add(booking: BookingSchema):
    return {'message': 'add new booking'}


@router.get('/{booking_id}')
async def get(booking_id: int):
    return {'message': f'details of booking (id: {booking_id}'}


@router.put('/{booking_id}')
async def update(booking_id: int):
    return {'message': f'update booking (id: {booking_id}'}


@router.delete('/{booking_id}')
async def delete(booking_id: int):
    return {'message': f'delete booking (id: {booking_id}'}
