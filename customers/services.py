# Author: Chandler Harris
# Date: 10/18/2026
# File: services.py
# Description: Contains the functions used to retrieve customer records from the database.

from sqlmodel import Session, select

from .models import Customer


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
