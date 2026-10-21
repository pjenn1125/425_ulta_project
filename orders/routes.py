# Author: Chandler Harris
# Date: 10/20/2026
# File: routes.py
# Description: Defines the order API endpoints for retrieving orders and their related items.

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from .schemas import OrderRead
from .services import get_all_orders, get_order_by_id

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get(
    "/",
    response_model=List[OrderRead],
    summary="Get all orders"
)
def read_orders(
    session: Session = Depends(get_session)
):
    return get_all_orders(session)


@router.get(
    "/{order_id}",
    response_model=OrderRead,
    summary="Get an order by ID"
)
def read_order(
    order_id: int,
    session: Session = Depends(get_session)
):
    order = get_order_by_id(session, order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


from order_items.models import OrderItem
from order_items.schemas import OrderItemRead

#end point

from order_items.models import OrderItem
from order_items.schemas import OrderItemRead


@router.get("/{order_id}/items", response_model=list[OrderItemRead], summary="Get items for an order")
def get_order_items(
    order_id: int,
    session: Session = Depends(get_session)
):
    order_items = session.exec(
        select(OrderItem).where(OrderItem.order_id == order_id)
    ).all()

    return order_items

