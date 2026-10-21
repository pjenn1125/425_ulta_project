# Author: Chandler Harris
# Date: 10/20/2026
# File: models.py
# Description: Defines the Inventory database table and its fields.

from typing import Optional

from sqlmodel import SQLModel, Field


class Inventory(SQLModel, table=True):
    inventory_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    product_id: int = Field(foreign_key="product.product_id")
    quantity_in_stock: int
    warehouse_location: str
