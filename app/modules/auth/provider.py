from app.databases.mysql.core import db
from app.databases.mysql.repositories import UserRepository

from .service import AuthService


def get_auth_service():
    session = db.get_session()
    try:
        repo = UserRepository(session)
        service = AuthService(repo)
        yield service
    finally:
        session.close()
