from fastapi import FastAPI

from src.api.health import router as health_router
from src.api.licenses import router as licenses_router


fastapi_app = FastAPI(
    title="Robot API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None
)

fastapi_app.include_router(health_router)
fastapi_app.include_router(licenses_router)