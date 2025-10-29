import os

from dotenv import load_dotenv

load_dotenv()


class MySQLConfig:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "password")
        self.database = os.getenv("DB_NAME", "database")

    @property
    def get_database_url(self):
        return (
            f"mysql+pymysql://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )


mysql_config = MySQLConfig()
