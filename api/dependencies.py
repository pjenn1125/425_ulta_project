# OAuth2 bearer authentication and current-user lookup by Jennifer P.
#added RBAC function - chandler h

from typing import Annotated, Callable

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

def role_required(*allowed_roles: int) -> Callable[..., User]:
    def role_checker(
        current_user: Annotated[User, Depends(get_current_user)],
    ) -> User:
        if current_user.role_id not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource",
            )
        return current_user

    return role_checker


AdminDep = Annotated[User, Depends(role_required(1))]
ManagerDep = Annotated[User, Depends(role_required(1, 2))]
EmployeeDep = Annotated[User, Depends(role_required(1, 2, 3))]
