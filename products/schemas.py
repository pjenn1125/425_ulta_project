# Author: Chandler Harris
# Date: 10/18/2026
# File: schemas.py
# Description: Defines the product data schemas used to validate and return API responses.

from pydantic import BaseModel, Field, field_validator
from typing import Optional

#schema for creating a product
class ProductCreate(BaseModel):
    product_name: str = Field(...,min_length=2, max_length=100)
    brand: str = Field(...,min_length=2, max_length=50)
    price: float = Field(...,gt=0, le=10000)
    category: str = Field(...,min_length=2, max_length=50)

    @field_validator('product_name', 'brand','category', mode='after')
    @classmethod
    def clean_text(cls, value):
        return value.strip()

#schema for updating a product
class ProductUpdate(BaseModel):
    product_name:Optional[str] = Field(default=None, min_length=2, max_length=100)
    brand:Optional[str] = Field(default=None, min_length=2, max_length=50)
    price:Optional[float] = Field(default=None, gt=0, le=10000)
    category:Optional[str] = Field(default=None, min_length=2, max_length=50)

    @field_validator('product_name', 'brand','category', mode='after')
    @classmethod
    def clean_text(cls, value):
        return value.strip()

#schema for displaying a product
class ProductRead(BaseModel):
    product_id: int
    product_name: str
    brand: str
    price: float
    category: str



