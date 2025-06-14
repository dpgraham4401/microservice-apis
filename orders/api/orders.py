from fastapi import APIRouter, HTTPException

from schema import OrderItem, Size

router = APIRouter(prefix="/orders", tags=["orders"])

orders: list[OrderItem] = [
    OrderItem(quantity=1, product="foo", size=Size.big, id=1)
]

@router.get("")
async def get_orders():
    return orders


@router.get("/{order_id}")
async def get_order_by_id(order_id: int):
    for order in orders:
        if order.order_id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")
