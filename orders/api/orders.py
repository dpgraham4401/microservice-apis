from fastapi import APIRouter

from schema import OrderItem, Size

router = APIRouter(prefix="/orders", tags=["orders"])

orders: list[OrderItem] = [
    OrderItem(quantity=1, product="foo", size=Size.big, id=1)
]

@router.get("")
async def get_orders():
    return orders


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
