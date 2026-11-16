# Author: Chandler Harris
# Date: 10/18/2026
# File: models.py
# Description: Defines the Product database table and its fields.
from typing import Optional
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    __tablename__ = "product"

    product_id: Optional[int] = Field(
        default=None, primary_key=True
    )
    product_name: str = Field(
        sa_column=Column("name", String, nullable=False)
    )
    brand: str
    price: float
    category: str

