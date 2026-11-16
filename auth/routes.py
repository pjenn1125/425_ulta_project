# Author: Chandler Harris
# Date: 11/15/2026
# File: routes.py
# Description: creating endpoints

from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from api.dependencies import get_current_user
from auth.schemas import LoginRequest, RegisterRequest, TokenResponse
from auth.services import login_user, register_user
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


@router.post("/login", response_model=TokenResponse)
def login(
    user_data: LoginRequest,
    session: Session = Depends(get_session),
):
    return login_user(session, user_data)


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: UserRead = Depends(get_current_user)):
    return current_user
