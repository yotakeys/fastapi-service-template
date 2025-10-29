from fastapi import HTTPException

from app.databases.mysql.entities import User
from app.databases.mysql.repositories import UserRepository
from app.modules.auth import AuthService

from .schema import UserCreate


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        self.auth = AuthService(repo)

    def create_user(self, user_data: UserCreate) -> User:
        if self.repo.get_by_email(user_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed = self.auth.hash_password(user_data.password)
        user = User(name=user_data.name, email=user_data.email, password=hashed)
        return self.repo.create(user)

    def list_users(self) -> list[User]:
        return self.repo.get_all()
