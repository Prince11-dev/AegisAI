from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging, logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle events."""

    configure_logging()
    logger.info(
        "Starting AegisAI Backend",
        version=settings.APP_VERSION,
        environment=settings.APP_ENV,
    )

    yield

    logger.info("Shutting down AegisAI Backend")


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    logger.info("Root endpoint accessed")

    return {
        "message": f"Welcome to {settings.APP_NAME}",
    }


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    logger.info("Health check successful")

    return {
        "status": "healthy",
    }