from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.config import mysql_config

Base = declarative_base()


class MysqlDatabase:
    def __init__(self):
        self.engine = create_engine(mysql_config.get_database_url, echo=True)
        self.session_local = sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False
        )

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

    def get_session(self) -> Session:
        return self.session_local()


db = MysqlDatabase()
