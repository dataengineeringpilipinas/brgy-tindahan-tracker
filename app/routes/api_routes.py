"""
API routes for Barangay Tindahan Tracker
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.database import get_db
from app.controllers.store_controller import (
    create_tindahan, get_tindahan, get_tindahan_list, update_tindahan, delete_tindahan
)
from app.models.store import TindahanCreate, TindahanUpdate, TindahanResponse

router = APIRouter(tags=["api"])


# Tindahan routes
@router.post("/tindahan", response_model=TindahanResponse, tags=["tindahan"])
async def create_tindahan_endpoint(
    tindahan: TindahanCreate,
    db: AsyncSession = Depends(get_db)
) -> TindahanResponse:
    """Register a new tindahan."""
    return await create_tindahan(db, tindahan)


@router.get("/tindahan", response_model=List[TindahanResponse], tags=["tindahan"])
async def get_tindahan_endpoint(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    active_only: bool = Query(True),
    db: AsyncSession = Depends(get_db)
) -> List[TindahanResponse]:
    """Get all registered tindahan with pagination."""
    return await get_tindahan_list(db, skip, limit, active_only)


@router.get("/tindahan/{tindahan_id}", response_model=TindahanResponse, tags=["tindahan"])
async def get_tindahan_by_id_endpoint(
    tindahan_id: int,
    db: AsyncSession = Depends(get_db)
) -> TindahanResponse:
    """Get a specific tindahan by ID."""
    tindahan = await get_tindahan(db, tindahan_id)
    if not tindahan:
        raise HTTPException(status_code=404, detail="Tindahan not found")
    return tindahan


@router.put("/tindahan/{tindahan_id}", response_model=TindahanResponse, tags=["tindahan"])
async def update_tindahan_endpoint(
    tindahan_id: int,
    tindahan_update: TindahanUpdate,
    db: AsyncSession = Depends(get_db)
) -> TindahanResponse:
    """Update a tindahan registration."""
    tindahan = await update_tindahan(db, tindahan_id, tindahan_update)
    if not tindahan:
        raise HTTPException(status_code=404, detail="Tindahan not found")
    return tindahan


@router.delete("/tindahan/{tindahan_id}", tags=["tindahan"])
async def delete_tindahan_endpoint(
    tindahan_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Deactivate a tindahan registration (soft delete)."""
    success = await delete_tindahan(db, tindahan_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tindahan not found")
    return {"message": "Tindahan deactivated successfully"}
