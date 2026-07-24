"""
Application-wide constants.

This module contains reusable constants that should not be hardcoded
throughout the codebase.
"""

# Project Metadata
PROJECT_NAME = "AegisAI"
PROJECT_DESCRIPTION = (
    "Enterprise-grade Open Source AI Platform for building "
    "LLM, RAG, Agentic AI, and Automation applications."
)

# API
API_V1_PREFIX = "/api/v1"
API_VERSION = "v1"

# Pagination Defaults
DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Upload Limits
MAX_UPLOAD_SIZE_MB = 100

# Supported File Types
SUPPORTED_DOCUMENT_TYPES = {
    ".pdf",
    ".docx",
    ".txt",
    ".md",
    ".csv",
}

# Health Status
STATUS_HEALTHY = "healthy"
STATUS_UNHEALTHY = "unhealthy"

# Logging
REQUEST_ID_HEADER = "X-Request-ID"

# Time
UTC = "UTC"