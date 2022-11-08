from fastapi import APIRouter, HTTPException

from pyrometheus.schemas.ships import ShipSchema


router = APIRouter(
    prefix='/ships',
    tags=['ships']
)

ships = []


@router.get('/')
async def index():
    return ships


@router.get('/{ship_id}')
async def get(ship_id: int):
    return get_ship(ship_id)


@router.delete('/{ship_id}')
async def delete(ship_id: int):
    get_ship(ship_id)
    del ships[ship_id]

    return ships


@router.put('/{ship_id}')
async def update(ship_id: int, ship: ShipSchema):
    get_ship(ship_id)
    ships[ship_id] = ship

    return ships


@router.post('/', status_code=201)
async def add(ship: ShipSchema):
    ships.append(ship)

    return ships


def get_ship(ship_id: int) -> ShipSchema:
    try:
        return ships[ship_id]
    except IndexError:
        raise HTTPException(status_code=404, detail='This ship does\'t exist')
