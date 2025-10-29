import os

from dotenv import load_dotenv

load_dotenv()


class CoreConfig:
    def __init__(self):
        self.project_name = os.getenv("PROJECT_NAME", "FastAPI Service Template")
        self.project_version = os.getenv("PROJECT_VERSION", "0.1.0")
        self.app_prefix = os.getenv("API_PREFIX", "/api/v1")
        self.all_cors_origins = (
            os.getenv("ALL_CORS_ORIGINS", "").split(",")
            if os.getenv("ALL_CORS_ORIGINS")
            else ["*"]
        )


core_config = CoreConfig()
