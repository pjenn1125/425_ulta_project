# Author: Chandler Harris
# Date: 10/20/2026
# File: routes.py
# Description: Defines the order item API endpoints for retrieving all order items and a specific item.

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from database import get_session
from .schemas import OrderItemRead
from .services import get_all_order_items, get_order_item_by_id

router = APIRouter(
    prefix="/order-items",
    tags=["Order Items"]
)


@router.get(
    "/",
    response_model=List[OrderItemRead],
    summary="Get all order items"
)
def read_order_items(
    session: Session = Depends(get_session)
):
    return get_all_order_items(session)


@router.get(
    "/{order_item_id}",
    response_model=OrderItemRead,
    summary="Get an order item by ID"
)
def read_order_item(
    order_item_id: int,
    session: Session = Depends(get_session)
):
    order_item = get_order_item_by_id(session, order_item_id)

    if order_item is None:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    return order_item
