# Author: Chandler Harris
# Date: 10/20/2026
# File: services.py
# Description: Contains the functions used to retrieve order records from the database.

from sqlmodel import Session, select

from .models import Order


def get_all_orders(session: Session):
    statement = select(Order)
    return session.exec(statement).all()


def get_order_by_id(session: Session, order_id: int):
    statement = select(Order).where(
        Order.order_id == order_id
    )
    return session.exec(statement).first()
