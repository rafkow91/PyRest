from fastapi import APIRouter
from passlib.context import CryptContext


router = APIRouter(
    prefix='/users',
    tags=['users']
)

pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

@router.get('/get-password')
def get_password():
    return pwd_context.hash('admin')