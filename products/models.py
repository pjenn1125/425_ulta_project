# Author: Chandler Harris
# Date: 10/18/2026
# File: models.py
# Description: Defines the Product database table and its fields.
from typing import Optional
from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    product_id: Optional[int] = Field(
        default=None, primary_key=True
    )
    product_name: str
    brand: str
    price: float
    category: str


