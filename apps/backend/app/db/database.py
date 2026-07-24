from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.core.config import settings


def get_engine() -> Engine:
    """
    Create and return the SQLAlchemy engine.
    """

    return create_engine(
        settings.DATABASE_URL,
        echo=settings.DEBUG,
        future=True,
        pool_pre_ping=True,
    )


engine = get_engine()