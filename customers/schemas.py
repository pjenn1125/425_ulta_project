# Author: Chandler Harris
# Date: 10/18/2026
# File: schemas.py
# Description: Defines the customer data schemas used to validate and return API responses.

from typing import Optional

from sqlmodel import SQLModel


class CustomerRead(SQLModel):
    customer_id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
