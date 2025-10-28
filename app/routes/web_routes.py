"""
Web routes for serving HTML templates
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page."""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "Barangay Tindahan Compliance Tracker"
    })


@router.get("/tindahan", response_class=HTMLResponse)
async def tindahan_page(request: Request):
    """Tindahan registration and management page."""
    return templates.TemplateResponse("tindahan.html", {
        "request": request,
        "title": "Manage Tindahan"
    })


@router.get("/inspections", response_class=HTMLResponse)
async def inspections_page(request: Request):
    """Compliance inspections page."""
    return templates.TemplateResponse("inspections.html", {
        "request": request,
        "title": "Compliance Inspections"
    })


@router.get("/violations", response_class=HTMLResponse)
async def violations_page(request: Request):
    """Violations tracking page."""
    return templates.TemplateResponse("violations.html", {
        "request": request,
        "title": "Violation Tracking"
    })


@router.get("/reports", response_class=HTMLResponse)
async def reports_page(request: Request):
    """Compliance reports page."""
    return templates.TemplateResponse("reports.html", {
        "request": request,
        "title": "Compliance Reports"
    })
