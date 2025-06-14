from typing import Optional, Annotated

from pydantic import BaseModel, conint, ConfigDict, field_validator, Field

from enum import Enum

class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


class Status(Enum):
    created = 'created'
    paid = 'paid'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'

class OrderItem(BaseModel):
    order_id: int = Field(..., alias="id")
    product: str
    size: Size
    quantity: Annotated[int, Field(ge=1, strict=True)] = 1

    model_config = ConfigDict(extra="forbid")


    @field_validator('quantity')
    def quantity_non_nullable(cls, value):
        assert value is not None, 'quantity may not be None'
        return value