# Author: Chandler Harris
# Date: 10/18/2026
# File: schemas.py
# Description: Defines the product data schemas used to validate and return API responses.

from sqlmodel import SQLModel


class ProductRead(SQLModel):
    product_id: int
    product_name: str
    brand: str
    price: float
    category: str
