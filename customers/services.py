# Author: Chandler Harris
# Date: 10/18/2026
# File: services.py
# Description: Contains the functions used to retrieve customer records from the database.

from sqlmodel import Session, select

from .models import Customer
from .schemas import CustomerCreate, CustomerUpdate


def get_all_customers(session: Session):
    statement = select(Customer)
    customers = session.exec(statement).all()
    return customers


def get_customer_by_id(session: Session, customer_id: int):
    statement = select(Customer).where(
        Customer.customer_id == customer_id
    )
    customer = session.exec(statement).first()
    return customer


def create_customer(session: Session, customer: CustomerCreate):
    db_customer = Customer(**customer.model_dump())
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)
    return db_customer


def update_customer(
    session: Session,
    customer_id: int,
    customer: CustomerUpdate,
):
    db_customer = get_customer_by_id(session, customer_id)
    if db_customer is None:
        return None

    for field, value in customer.model_dump(exclude_unset=True).items():
        setattr(db_customer, field, value)

    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)
    return db_customer


def delete_customer(session: Session, customer_id: int):
    customer = get_customer_by_id(session, customer_id)
    if customer is None:
        return None

    session.delete(customer)
    session.commit()
    return customer
