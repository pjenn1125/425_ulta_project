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
def read_customers(session: Session = Depends(get_session)):
    return get_all_customers(session)


@router.get(
    "/{customer_id}",
    response_model=CustomerRead,
    summary="Get a customer by ID"
)
def read_customer(customer_id: int, session: Session = Depends(get_session)):
    customer = get_customer_by_id(session, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer

# ---------------------------------------------------------
# CREATE CUSTOMER (Lab 3 - Added by Jennifer P.)
# ---------------------------------------------------------
@router.post(
    "/",
    response_model=CustomerRead,
    status_code=201,
    summary="Create a new customer"
)
def create_customer_route(
    customer: CustomerCreate,
    session: Session = Depends(get_session)
):
    return create_customer(session, customer)


# ---------------------------------------------------------
# UPDATE CUSTOMER (Lab 3 - Added by Jennifer P.)
# ---------------------------------------------------------
@router.put(
    "/{customer_id}",
    response_model=CustomerRead,
    summary="Update an existing customer"
)
def update_customer_route(
    customer_id: int,
    customer: CustomerUpdate,
    session: Session = Depends(get_session)
):
    updated = update_customer(session, customer_id, customer)

    if updated is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return updated


# DELETE CUSTOMER (Lab 3 - Added by Jennifer P.)

@router.delete(
    "/{customer_id}",
    status_code=200,
    summary="Delete a customer"
)
def delete_customer_route(
    customer_id: int,
    session: Session = Depends(get_session)
):
    deleted = delete_customer(session, customer_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {"message": "Customer deleted"}