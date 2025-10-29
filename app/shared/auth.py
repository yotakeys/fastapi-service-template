from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status

from app.config import jwt_config


class JWTManager:
    def __init__(self):
        self.secret = jwt_config.secret_key
        self.algorithm = jwt_config.algorithm
        self.expire_minutes = jwt_config.access_token_expire_minutes

    def create_access_token(self, data: dict) -> str:
        """Create a JWT token with an expiration time."""
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=self.expire_minutes)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret, algorithm=self.algorithm)

    def verify_token(self, token: str) -> dict:
        """Decode and verify JWT token."""
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError as exc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
            ) from exc
        except jwt.InvalidTokenError as exc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            ) from exc


jwt_manager = JWTManager()
