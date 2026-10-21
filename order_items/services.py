# Author: Chandler Harris
# Date: 10/20/2026
# File: services.py
# Description: Contains the functions used to retrieve order item records from the database.

from sqlmodel import Session, select

from .models import OrderItem


def get_all_order_items(session: Session):
    statement = select(OrderItem)
    return session.exec(statement).all()


def get_order_item_by_id(session: Session, order_item_id: int):
    statement = select(OrderItem).where(
        OrderItem.order_item_id == order_item_id
    )
    return session.exec(statement).first()
