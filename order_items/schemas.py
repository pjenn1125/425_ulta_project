# Author: Chandler Harris
# Date: 10/20/2026
# File: schemas.py
# Description: Defines the order item data schemas used to validate and return API responses.

from sqlmodel import SQLModel


class OrderItemRead(SQLModel):
    order_item_id: int
    order_id: int
    product_id: int
    quantity_ordered: int
    unit_price: float
