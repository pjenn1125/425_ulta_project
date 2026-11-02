# Author: Chandler Harris, Jennifer P.
# Date: 10/18/2026
# File: schemas.py
# Description: Defines the customer data schemas used to validate and return API responses

from typing import Optional
from sqlmodel import SQLModel
from pydantic import Field, field_validator, model_validator


# BASE SCHEMA (shared fields)

class CustomerBase(SQLModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., pattern=r".+@.+\..+")
    phone: Optional[str] = Field(None, min_length=10, max_length=14)

    # Custom validator
    @field_validator("first_name", "last_name")
    def only_letters(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Names must contain only letters")
        return value


# CREATE SCHEMA

class CustomerCreate(CustomerBase):
    pass



# UPDATE SCHEMA

class CustomerUpdate(SQLModel):
    first_name: Optional[str] = Field(None, min_length=2, max_length=50)
    last_name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[str] = Field(None, pattern=r".+@.+\..+")
    phone: Optional[str] = Field(None, min_length=10, max_length=14)

    @field_validator("first_name", "last_name")
    @classmethod
    def only_letters(cls, value):
        if value is not None and not value.replace(" ", "").isalpha():
            raise ValueError("Names must contain only letters")
        return value

    @model_validator(mode="before")
    @classmethod
    def reject_null_required_fields(cls, values):
        if isinstance(values, dict):
            if not values:
                raise ValueError("At least one customer field must be provided")
            for field in ("first_name", "last_name", "email"):
                if field in values and values[field] is None:
                    raise ValueError(f"{field} cannot be null")
        return values


# READ SCHEMA (returned to client)

class CustomerRead(CustomerBase):
    customer_id: int