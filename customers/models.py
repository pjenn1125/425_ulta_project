# Author: Chandler Harris
# Date: 10/18/2026
# File: models.py
# Description: Defines the Customer database table and its fields.

from typing import Optional

from sqlmodel import SQLModel, Field


class Customer(SQLModel, table=True):
    customer_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None

