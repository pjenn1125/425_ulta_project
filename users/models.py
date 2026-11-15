# Author: Chandler Harris
# Date: 11/15/2026
# File: routes.py
# Description: defines the DB model for roles and users
from sqlmodel import SQLModel, Field
from typing import Optional


class Role(SQLModel, table=True):
    __tablename__ = "roles"

    role_id: Optional[int] = Field(default=None, primary_key=True)
    role_name: str = Field(unique=True, index=True)
    description: Optional[str] = None


class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    hashed_pw: str
    role_id: int = Field(foreign_key="roles.role_id")