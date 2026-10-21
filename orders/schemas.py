# Author: Chandler Harris
# Date: 10/20/2026
# File: schemas.py
# Description:Defines the order data schemas used to validate and return API responses.

from datetime import date

from sqlmodel import SQLModel


class OrderRead(SQLModel):
    order_id: int
    customer_id: int
    order_date: date
    status: str
