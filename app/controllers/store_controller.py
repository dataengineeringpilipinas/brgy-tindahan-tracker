"""
Store controller for business logic operations
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import List, Optional
from fastapi import HTTPException

from app.models.store import Tindahan, TindahanCreate, TindahanUpdate, TindahanResponse


async def create_tindahan(db: AsyncSession, tindahan: TindahanCreate) -> TindahanResponse:
    """Create a new tindahan registration."""
    db_tindahan = Tindahan(**tindahan.model_dump())
    db.add(db_tindahan)
    await db.commit()
    await db.refresh(db_tindahan)
    return TindahanResponse.model_validate(db_tindahan)


async def get_tindahan(db: AsyncSession, tindahan_id: int) -> Optional[TindahanResponse]:
    """Get a specific tindahan by ID."""
    result = await db.execute(select(Tindahan).where(Tindahan.id == tindahan_id))
    tindahan = result.scalar_one_or_none()
    return TindahanResponse.model_validate(tindahan) if tindahan else None


async def get_tindahan_list(db: AsyncSession, skip: int = 0, limit: int = 100, active_only: bool = True) -> List[TindahanResponse]:
    """Get all tindahan with pagination."""
    query = select(Tindahan)
    if active_only:
        query = query.where(Tindahan.is_active == True)
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    tindahan_list = result.scalars().all()
    return [TindahanResponse.model_validate(tindahan) for tindahan in tindahan_list]


async def update_tindahan(db: AsyncSession, tindahan_id: int, tindahan_update: TindahanUpdate) -> Optional[TindahanResponse]:
    """Update a tindahan registration."""
    result = await db.execute(select(Tindahan).where(Tindahan.id == tindahan_id))
    db_tindahan = result.scalar_one_or_none()
    
    if not db_tindahan:
        return None
    
    update_data = tindahan_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_tindahan, field, value)
    
    await db.commit()
    await db.refresh(db_tindahan)
    return TindahanResponse.model_validate(db_tindahan)


async def delete_tindahan(db: AsyncSession, tindahan_id: int) -> bool:
    """Soft delete a tindahan (set is_active to False)."""
    result = await db.execute(select(Tindahan).where(Tindahan.id == tindahan_id))
    db_tindahan = result.scalar_one_or_none()
    
    if not db_tindahan:
        return False
    
    db_tindahan.is_active = False
    await db.commit()
    return True


async def get_tindahan_by_name(db: AsyncSession, name: str) -> Optional[TindahanResponse]:
    """Get tindahan by business name."""
    result = await db.execute(select(Tindahan).where(Tindahan.business_name == name))
    tindahan = result.scalar_one_or_none()
    return TindahanResponse.model_validate(tindahan) if tindahan else None
