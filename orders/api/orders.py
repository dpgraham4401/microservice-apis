from fastapi import APIRouter, HTTPException

from schema import OrderItem, Size

router = APIRouter(prefix="/orders", tags=["orders"])

orders: list[OrderItem] = [
    OrderItem(quantity=1, product="Tomatoes", size=Size.big, id=1),
    OrderItem(quantity=4, product="Brocolli", size=Size.small, id=2),
    OrderItem(quantity=23, product="Potatoes", size=Size.medium, id=3),
    OrderItem(quantity=98, product="Carrots", size=Size.small, id=4),
]

@router.get("")
async def get_orders(limit: int | None = None):
    """Get all orders."""
    query_set = [order for order in orders]

    if limit and limit < len(orders):
        query_set = query_set[:limit]

    return query_set


@router.get("/{order_id}")
async def get_order_by_id(order_id: int):
    """Get order by id."""
    for order in orders:
        if order.order_id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@router.post("")
async def create_order(order: OrderItem):
    """Create new order."""
    orders.append(order)
    return order