from datetime import datetime
from pydantic import BaseModel, PositiveInt, validator
from typing import Optional


class BookingSchema(BaseModel):
    id: Optional[PositiveInt]
    spaceship_id: PositiveInt
    customer_id: PositiveInt
    date_start: datetime
    date_end: datetime


    @validator('date_end')
    def validate_date_end(cls, value: datetime, values) -> datetime:
        if value <= values['date_start']:
            raise ValueError('End date must be later than start date!')
        print(values)
        return value