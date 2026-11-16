#added by jennifer p (lab4): Implements OAuth2PasswordBearer token auht, JWT validation
#and current user retrieval for securing protected API endpoints
#added RBAC function - chandler h

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlmodel import Session

from auth.services import decode_access_token
from database import get_session
from users.models import User
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        claims = decode_access_token(token)
        user_id = int(claims["sub"])
    except (JWTError, TypeError, ValueError):
        raise credentials_exception from None

    user = session.get(User, user_id)
    if user is None:
        raise credentials_exception

    return user

#check whether a user has the required role
def require_role(*allowed_roles: int):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role_id not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource")
        return current_user

    return role_checker