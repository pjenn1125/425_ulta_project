# Author: Chandler Harris
# Date: 11/15/2026
# File: services.py
# Description: the handling of the creation of user accounts and password hashing.

from sqlmodel import Session
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher

from users.models import User
from users.schemas import UserCreate


#set up password hashing using bcrypt
password_hash = PasswordHash((BcryptHasher(),))


#create a new user
def create_user(session: Session, user_data: UserCreate):

    #hash the user's password
    hashed_password = password_hash.hash(user_data.password)

    #create the user account
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_pw=hashed_password,
        role_id=user_data.role_id)

    #cave the user to the database
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user
