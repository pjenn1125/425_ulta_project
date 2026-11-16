# Author: Chandler Harris
# Date: 11/15/2026
# File: services.py
# Description: auth/services will handle the registration process
from sqlmodel import Session, select
from fastapi import HTTPException, status
from jose import JWTError, jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os

from users.models import User, Role
from users.schemas import UserRead
from users.services import create_user
from users.services import password_hash
from auth.schemas import LoginRequest, RegisterRequest, TokenResponse


def _jwt_settings() -> tuple[str, str, int]:
    load_dotenv()
    secret_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM", "HS256")
    expiration_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")

    if not secret_key:
        raise RuntimeError("SECRET_KEY must be configured in the environment")

    try:
        expiration = int(expiration_minutes)
    except ValueError as exc:
        raise RuntimeError("ACCESS_TOKEN_EXPIRE_MINUTES must be an integer") from exc

    if expiration <= 0:
        raise RuntimeError("ACCESS_TOKEN_EXPIRE_MINUTES must be greater than zero")

    return secret_key, algorithm, expiration


def create_access_token(user: User) -> str:
    if user.user_id is None:
        raise RuntimeError("Cannot issue a token for a user without an ID")

    secret_key, algorithm, expiration_minutes = _jwt_settings()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=expiration_minutes)
    claims = {
        "sub": str(user.user_id),
        "role_id": user.role_id,
        "exp": expires_at,
    }
    return jwt.encode(claims, secret_key, algorithm=algorithm)


def decode_access_token(token: str) -> dict:
    secret_key, algorithm, _ = _jwt_settings()
    claims = jwt.decode(token, secret_key, algorithms=[algorithm])

    if (
        not isinstance(claims.get("sub"), str)
        or not claims["sub"]
        or not isinstance(claims.get("role_id"), int)
        or isinstance(claims.get("role_id"), bool)
        or "exp" not in claims
    ):
        raise JWTError("Token is missing required claims")

    return claims

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


def login_user(session: Session, user_data: LoginRequest) -> TokenResponse:
    user = session.exec(
        select(User).where(User.username == user_data.username)
    ).first()

    if user is None or not password_hash.verify(user_data.password, user.hashed_pw):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user.user_id is None:
        raise RuntimeError("Cannot issue a token for a user without an ID")

    user_read = UserRead(
        user_id=user.user_id,
        username=user.username,
        email=user.email,
        role_id=user.role_id,
    )
    return TokenResponse(
        access_token=create_access_token(user),
        user=user_read,
    )
