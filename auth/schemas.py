# Author: Chandler Harris
# Date: 11/15/2026
# File: schemas.py
# Description:


from users.schemas import UserRead
from sqlmodel import SQLModel


class RegisterRequest(SQLModel):
    username: str
    email: str
    password: str


#login and JWT response schemas added by Jennifer P.
class LoginRequest(SQLModel):
    username: str
    password: str

class TokenResponse(SQLModel):
    access_token: str
    token_type: str = "bearer"
    user: UserRead