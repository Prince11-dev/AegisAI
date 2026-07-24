from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # --------------------------------------------------
    # Application
    # --------------------------------------------------
    APP_NAME: str = Field(default="AegisAI")
    APP_VERSION: str = Field(default="0.1.0")
    APP_DESCRIPTION: str = (
    "Enterprise-grade Open Source AI Platform for building "
    "LLM, RAG, Agentic AI, and Automation applications."
    )
    APP_ENV: str = Field(default="development")
    DEBUG: bool = Field(default=True)

    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    API_V1_PREFIX: str = Field(default="/api/v1")

    # --------------------------------------------------
    # Security
    # --------------------------------------------------
    SECRET_KEY: str
    ALGORITHM: str = Field(default="HS256")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7)

    # --------------------------------------------------
    # Database
    # --------------------------------------------------
    DATABASE_URL: str

    # --------------------------------------------------
    # Redis
    # --------------------------------------------------
    REDIS_URL: str

    # --------------------------------------------------
    # ChromaDB
    # --------------------------------------------------
    CHROMA_HOST: str = Field(default="localhost")
    CHROMA_PORT: int = Field(default=8001)
    CHROMA_COLLECTION: str = Field(default="documents")

    # --------------------------------------------------
    # Ollama
    # --------------------------------------------------
    OLLAMA_BASE_URL: str = Field(default="http://localhost:11434")
    OLLAMA_DEFAULT_MODEL: str = Field(default="llama3.2")

    # --------------------------------------------------
    # OpenAI
    # --------------------------------------------------
    OPENAI_API_KEY: str = Field(default="")

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FORMAT: str = Field(default="json")

    # --------------------------------------------------
    # CORS
    # --------------------------------------------------
    BACKEND_CORS_ORIGINS: str = Field(default="http://localhost:3000")

    # --------------------------------------------------
    # File Storage
    # --------------------------------------------------
    UPLOAD_DIR: str = Field(default="storage/uploads")
    MAX_UPLOAD_SIZE_MB: int = Field(default=50)

    # --------------------------------------------------
    # Embeddings
    # --------------------------------------------------
    EMBEDDING_MODEL: str = Field(default="nomic-embed-text")

    # --------------------------------------------------
    # RAG
    # --------------------------------------------------
    CHUNK_SIZE: int = Field(default=1000)
    CHUNK_OVERLAP: int = Field(default=200)
    TOP_K_RESULTS: int = Field(default=5)


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()


settings = get_settings()