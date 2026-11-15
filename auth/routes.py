# Author: Chandler Harris
# Date: 11/15/2026
# File: routes.py
# Description: creating endpoints

from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from auth.schemas import RegisterRequest
from auth.services import register_user
from users.schemas import UserRead


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"])


# Register a new user
@router.post("/register", response_model=UserRead, status_code=201)
def register(
    user_data: RegisterRequest,
    session: Session = Depends(get_session)):
    return register_user(session, user_data)

