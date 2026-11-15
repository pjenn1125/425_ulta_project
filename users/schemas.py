# Author: Chandler Harris
# Date: 11/15/2026
# File: schemas.py
# Description: controls what information is accepted when creating a user and what get sent to the API
from sqlmodel import SQLModel
from typing import Optional

#info needed to create a user
class UserCreate(SQLModel):
    username: str
    email: str
    password: str
    role_id: int


#info returned about a user
class UserRead(SQLModel):
    user_id: int
    username: str
    email: str
    role_id: int


#info used to update a user
class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[int] = None
