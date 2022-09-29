from datetime import date
from pydantic import BaseModel
from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix='/customers',
    tags=['customers']
)


class CustomerSchema(BaseModel):
    id: Optional[int]
    name: str
    address: str
    document_number: str



@router.get('/')
async def index():
    return {'message': 'list of customers'}


@router.post('/')
async def add(customer: CustomerSchema):
    return {'message': 'add new customer'}


@router.get('/{customer_id}')
async def get(customer_id: int):
    return {'message': f'details of customer (id: {customer_id}'}


@router.put('/{customer_id}')
async def update(customer_id: int):
    return {'message': f'update customer (id: {customer_id}'}


@router.delete('/{customer_id}')
async def delete(customer_id: int):
    return {'message': f'delete customer (id: {customer_id}'}
