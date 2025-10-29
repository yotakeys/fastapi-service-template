import os

from dotenv import load_dotenv

load_dotenv()


class JWTConfig:
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET", "your_default_secret_key")
        self.algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        self.access_token_expire_minutes = int(
            os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
        )


jwt_config = JWTConfig()
