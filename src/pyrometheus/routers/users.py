from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

from pyrometheus.schemas.users import User

router = APIRouter(
    prefix='/users',
    tags=['users']
)

pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

SECRET_KEY = '5f4930bfb1d55eaccd607bbcae4588e1a9dce3556ef4ece2d5cf3b55f095c6f9'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    'rkowalski': {
        'username': 'rkowalski',
        'full_name': 'Rafał Kowalski',
        'email': 'my@mail.com',
        'hashed_password': '$2b$12$agVzk/B7Ng5vxb55Ivbrjeyz4ZQNi64P/LCTbHfb/0J.fgk3LAfoW',
        'active': True
    }
}


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str) -> User:
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(fake_db, username: str, password: str) -> User | None:
    user = get_user(fake_db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post('/token')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}
    