from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.databases.mysql.core import db
from app.databases.mysql.repositories import UserRepository
from app.shared.auth import jwt_manager

from .service import UserService


def get_user_service():
    session = db.get_session()
    try:
        repo = UserRepository(session)
        service = UserService(repo)
        yield service
    finally:
        session.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    service: UserService = Depends(get_user_service),
):
    payload = jwt_manager.verify_token(credentials.credentials)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token"
        )

    user = service.repo.get_by_id(int(payload["sub"]))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user
