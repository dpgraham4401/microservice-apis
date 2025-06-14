from fastapi import APIRouter

from schema import OrderItemSchema, Size

router = APIRouter()

orders: list[OrderItemSchema] = [
    OrderItemSchema(quantity=1, product="foo", size=Size.big)
]

@router.get("/")
async def root():
    return orders


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
