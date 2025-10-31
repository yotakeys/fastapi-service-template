import bcrypt
from fastapi import HTTPException, status

from app.databases.mysql import User
from app.databases.mysql import UserRepository
from app.shared.auth import jwt_manager


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def verify_password(self, plain: str, hashed: str) -> bool:
        return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))

    def authenticate_user(self, email: str, password: str) -> User:
        user = self.repo.get_by_email(email)
        if not user or not self.verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
        return user

    def create_token(self, user: User) -> str:
        data = {"sub": str(user.id), "email": user.email}
        return jwt_manager.create_access_token(data)
