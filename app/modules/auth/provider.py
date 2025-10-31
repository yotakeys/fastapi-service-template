from app.databases.mysql import db
from app.databases.mysql import UserRepository

from .service import AuthService


def get_auth_service():
    session = db.get_session()
    try:
        repo = UserRepository(session)
        service = AuthService(repo)
        yield service
    finally:
        session.close()
