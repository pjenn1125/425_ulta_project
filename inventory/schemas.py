# Author: Chandler Harris
# Date: 10/20/2026
# File: schemas.py
# Description: Defines the inventory data schemas used to validate and return API responses.

from sqlmodel import SQLModel


class InventoryRead(SQLModel):
    inventory_id: int
    product_id: int
    quantity_in_stock: int
    warehouse_location: str

