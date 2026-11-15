# Author: Chandler Harris
# Date: 11/15/2026
# File: services.py
# Description: auth/services will handle the registration process
from sqlmodel import Session, select
from fastapi import HTTPException
from users.models import User, Role
from users.services import create_user
from auth.schemas import RegisterRequest


#register a new user
def register_user(session: Session, user_data: RegisterRequest):

    #check if username already exists
    existing_username = session.exec(
        select(User).where(User.username == user_data.username)).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists")

    #check if email already exists
    existing_email = session.exec(
        select(User).where(User.email == user_data.email)).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists")

    #check if the role exists
    existing_role = session.get(Role, user_data.role_id)

    if not existing_role:
        raise HTTPException(
            status_code=400,
            detail="Invalid role ID")

    #create user and hash password
    return create_user(session, user_data)

