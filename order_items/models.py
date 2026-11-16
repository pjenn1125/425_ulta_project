# Author: Chandler Harris
# Date: 10/20/2026
# File: models.py
# Description: Defines the OrderItem database table and its fields.

from typing import Optional

from sqlalchemy import Column, Integer
from sqlmodel import SQLModel, Field


class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"

    order_item_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    order_id: int = Field(foreign_key="orders.order_id")
    product_id: int = Field(foreign_key="product.product_id")
    quantity_ordered: int = Field(
        sa_column=Column("quantity", Integer, nullable=False)
    )
    unit_price: float
