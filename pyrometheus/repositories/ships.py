from sqlalchemy.orm import Session
from sqlalchemy import update
from pyrometheus.models import Ship


def create(db: Session, name: str, max_speed: float, distance: float, cost_per_day: float):
    db_ship = Ship(name=name, max_speed=max_speed, distance=distance, cost_per_day=cost_per_day)
    print(db)
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)

    return db_ship


def fetch_one(db: Session, ship_id: int):
    return db.get(Ship, ship_id)
