from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from pyrometheus.database import get_db
from pyrometheus.repositories.ships import (
    create,
    delete_one,
    fetch_one,
    fetch_by_page,
    fetch_all,
    update_by_id,
)
from pyrometheus.schemas.ships import ShipSchema


router = APIRouter(
    prefix='/ships',
    tags=['ships']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

@router.get('/')
async def get_by_page(page: int = None, limit: int = None, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    print(token)
    if page is None or limit is None:
        return fetch_all(db=db)
    return fetch_by_page(db=db, page=page, ships_by_page=limit)


@router.get('/{ship_id}')
async def get(ship_id: int, db: Session = Depends(get_db)):
    return fetch_one(db=db, ship_id=ship_id)


@router.delete('/{ship_id}')
async def delete(ship_id: int, db: Session = Depends(get_db)):
    return delete_one(db=db, ship_id=ship_id)


@router.put('/{ship_id}')
async def update(ship_id: int, ship: ShipSchema, db: Session = Depends(get_db)):
    return update_by_id(
        db=db,
        ship_id=ship_id,
        **ship.dict()
    )


@router.post('/', status_code=201)
async def add(ship: ShipSchema, db: Session = Depends(get_db)):
    create(
        db=db,
        name=ship.name,
        max_speed=ship.max_speed,
        distance=ship.distance,
        cost_per_day=ship.cost_per_day,
    )

    return []
