from pydantic import BaseModel, PositiveInt, PositiveFloat, Field
from typing import Optional

class ShipSchema(BaseModel):
    id: Optional[PositiveInt]
    name: str = Field(min_length=3, max_length=255)
    max_speed: PositiveFloat
    distance: PositiveFloat
    cost_per_day: PositiveFloat

    def __str__(self) -> str:
        return self.name
