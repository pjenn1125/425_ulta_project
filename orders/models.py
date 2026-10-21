# Author: Chandler Harris
# Date: 10/20/2026
# File: models.py
# Description: Defines the Order database table and its fields.

from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field


class Order(SQLModel, table=True):
    order_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    customer_id: int = Field(foreign_key="customer.customer_id")
    order_date: date
    status: str
