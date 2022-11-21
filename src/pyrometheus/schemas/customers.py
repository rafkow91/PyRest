from pydantic import (
    BaseModel,
    PositiveInt,
    Field,
    validator,
)
from typing import Optional


class CustomerSchema(BaseModel):
    id: Optional[PositiveInt]
    name: str = Field(min_length=3, max_length=255)
    address: str = Field(min_length=3, max_length=255)
    document_number: str = Field(min_length=9, max_length=9)

    @validator('document_number')
    def validate_document_number(cls, value: str) -> str:
        value.upper()
        checksum = 0
        multiplier = [7, 3, 1, '', 7, 3, 1, 7, 3]
        for i, char in enumerate(value):
            if i == 3:
                continue
            if not char.isdecimal():
                char = ord(char) - 55

            checksum += int(char) * multiplier[i]

        if int(value[3]) != checksum % 10:
            raise ValueError('Document number isn\'t correct!')

        return value
