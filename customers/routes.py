# Author: Chandler Harris
# Date: 10/18/2026
# File: routes.py
# Description: Defines the customer API endpoints for retrieving customers and their orders.


from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from .schemas import CustomerRead
from .services import get_all_customers, get_customer_by_id
from orders.models import Order
from orders.schemas import OrderRead

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get(
    "/",
    response_model=List[CustomerRead],
    summary="Get all customers"
)
def read_customers(
    session: Session = Depends(get_session)
):
    return get_all_customers(session)


@router.get(
    "/{customer_id}",
    response_model=CustomerRead,
    summary="Get a customer by ID"
)
def read_customer(
    customer_id: int,
    session: Session = Depends(get_session)
):
    customer = get_customer_by_id(session, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.get(
    "/{customer_id}/orders",
    response_model=List[OrderRead],
    summary="Get orders for a customer"
)
def get_customer_orders(
    customer_id: int,
    session: Session = Depends(get_session)
):
    customer_orders = session.exec(
        select(Order).where(Order.customer_id == customer_id)
    ).all()

    return customer_orders
