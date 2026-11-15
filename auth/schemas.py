# Author: Chandler Harris
# Date: 11/15/2026
# File: schemas.py
# Description:
from users.schemas import UserCreate


#info required to register a new user
class RegisterRequest(UserCreate):
    pass
