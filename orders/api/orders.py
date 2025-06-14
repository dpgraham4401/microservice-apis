from datetime import datetime, timezone, timedelta

from fastapi import APIRouter, HTTPException

from schema import OrderItem, Size, GetOrderSchema, Status

router = APIRouter(prefix="/orders", tags=["orders"])

orders: list[OrderItem] = [
    OrderItem(quantity=1, product="Tomatoes", size=Size.big, id=1, status=Status.created, created=datetime.now(timezone.utc)),
    OrderItem(quantity=4, product="Brocolli", size=Size.small, id=2, status=Status.cancelled, created=datetime.now(timezone.utc) - timedelta(hours=5)),
    OrderItem(quantity=23, product="Potatoes", size=Size.medium, id=3, status=Status.paid, created=datetime.now(timezone.utc) - timedelta(days=3, hours=2)),
    OrderItem(quantity=98, product="Carrots", size=Size.small, id=4, status=Status.progress, created=datetime.now(timezone.utc) - timedelta(days=1)),
]

@router.get("")
async def get_orders(limit: int | None = None):
    """Get all orders."""
    query_set = [order for order in orders]

    if limit and limit < len(orders):
        query_set = query_set[:limit]

    return query_set


@router.get("/{order_id}", response_model=GetOrderSchema)
async def get_order_by_id(order_id: int):
    """Get order by id."""
    for order in orders:
        if order.order_id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@router.post("")
async def create_order(order: OrderItem):
    """Create new order."""
    order["created"] = datetime.now(timezone.utc)
    order["status"] = "created"
    orders.append(order)
    return order