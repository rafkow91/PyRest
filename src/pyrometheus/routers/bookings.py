from fastapi import APIRouter

from pyrometheus.schemas.bookings import BookingSchema


router = APIRouter(
    prefix='/bookings',
    tags=['bookings']
)


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
