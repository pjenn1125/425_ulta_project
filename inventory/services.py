# Author: Chandler Harris
# Date: 10/20/2026
# File: services.py
# Description: Contains the functions used to retrieve inventory records from the database.

from sqlmodel import Session, select

from .models import Inventory


def get_all_inventory(session: Session):
    statement = select(Inventory)
    return session.exec(statement).all()


def get_inventory_by_id(session: Session, inventory_id: int):
    statement = select(Inventory).where(
        Inventory.inventory_id == inventory_id
    )
    return session.exec(statement).first()

