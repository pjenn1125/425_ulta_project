# Author: Chandler Harris
# Date: 10/20/2026
# File: models.py
# Description: Defines the Inventory database table and its fields.

from typing import Optional

from sqlalchemy import Column, Integer, String
from sqlmodel import SQLModel, Field


class Inventory(SQLModel, table=True):
    __tablename__ = "inventory"

    inventory_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    product_id: int = Field(foreign_key="product.product_id")
    quantity_in_stock: int = Field(
        sa_column=Column("quantity_available", Integer, nullable=False)
    )
    warehouse_location: str = Field(
        sa_column=Column("location", String, nullable=False)
    )
