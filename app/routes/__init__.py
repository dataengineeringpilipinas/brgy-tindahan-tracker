"""
Routes for Barangay Tindahan Tracker
"""

from fastapi import APIRouter
from .web_routes import router as web_router
from .api_routes import router as api_router

__all__ = ["web_router", "api_router"]
