from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config import core_config
from app.databases.mysql.core import db
from app.modules.auth import auth_router
from app.modules.user import user_router

app = FastAPI()
db.create_tables()

app = FastAPI(
    title=core_config.project_name,
    version=core_config.project_version,
    openapi_url=f"{core_config.app_prefix}/openapi.json",
)

if core_config.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=core_config.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(auth_router, prefix=core_config.app_prefix)
app.include_router(user_router, prefix=core_config.app_prefix)
