"""
Barangay Tindahan Compliance Tracker - Main FastAPI Application
A compliance monitoring system for barangay officials to track and monitor
local tindahan, street hawkers, and peddlers for regulatory compliance.
A Vibecamp Creation
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db
from app.routes import api_router, web_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    # Startup
    await init_db()
    yield
    # Shutdown


app = FastAPI(
    title="Barangay Tindahan Compliance Tracker",
    description="Monitor and track compliance of local tindahan, street hawkers, and peddlers for barangay regulatory enforcement", 
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(web_router)
app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Barangay Tindahan Compliance Tracker is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
