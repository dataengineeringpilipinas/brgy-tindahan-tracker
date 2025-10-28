"""
Inspection model for barangay compliance monitoring
"""

from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class InspectionType(str, Enum):
    """Types of inspections."""
    ROUTINE = "routine"  # Regular scheduled inspection
    COMPLAINT = "complaint"  # Inspection due to complaint
    FOLLOW_UP = "follow_up"  # Follow-up inspection
    RENEWAL = "renewal"  # Inspection for permit renewal
    EMERGENCY = "emergency"  # Emergency inspection


class InspectionStatus(str, Enum):
    """Inspection status."""
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ViolationType(str, Enum):
    """Types of violations."""
    NO_PERMIT = "no_permit"  # Operating without permit
    EXPIRED_PERMIT = "expired_permit"  # Permit has expired
    UNAUTHORIZED_LOCATION = "unauthorized_location"  # Operating in unauthorized area
    UNSANITARY_CONDITIONS = "unsanitary_conditions"  # Poor hygiene/sanitation
    NOISE_VIOLATION = "noise_violation"  # Excessive noise
    BLOCKING_TRAFFIC = "blocking_traffic"  # Blocking pedestrian/vehicle traffic
    OVERPRICING = "overpricing"  # Selling above regulated prices
    UNAUTHORIZED_PRODUCTS = "unauthorized_products"  # Selling prohibited items
    OTHER = "other"


class InspectionBase(SQLModel):
    """Base inspection model."""
    tindahan_id: int = Field(foreign_key="tindahan.id", description="Tindahan being inspected")
    inspection_type: InspectionType = Field(description="Type of inspection")
    inspector_name: str = Field(max_length=100, description="Name of inspector")
    inspection_date: datetime = Field(description="Date of inspection")
    status: InspectionStatus = Field(default=InspectionStatus.SCHEDULED, description="Inspection status")
    notes: Optional[str] = Field(default=None, max_length=1000, description="Inspection notes")


class Inspection(InspectionBase, table=True):
    """Inspection database model."""
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ViolationBase(SQLModel):
    """Base violation model."""
    inspection_id: int = Field(foreign_key="inspection.id", description="Inspection where violation was found")
    violation_type: ViolationType = Field(description="Type of violation")
    description: str = Field(max_length=500, description="Detailed description of violation")
    severity: int = Field(ge=1, le=5, description="Violation severity (1-5 scale)")
    is_resolved: bool = Field(default=False, description="Whether violation has been resolved")
    resolution_notes: Optional[str] = Field(default=None, max_length=500, description="Notes on how violation was resolved")
    resolution_date: Optional[datetime] = Field(default=None, description="Date violation was resolved")


class Violation(ViolationBase, table=True):
    """Violation database model."""
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class InspectionCreate(InspectionBase):
    """Inspection creation model."""
    pass


class ViolationCreate(ViolationBase):
    """Violation creation model."""
    pass


class InspectionResponse(InspectionBase):
    """Inspection response model."""
    id: int
    created_at: datetime
    updated_at: datetime
    violations: List["ViolationResponse"] = []

    class Config:
        from_attributes = True


class ViolationResponse(ViolationBase):
    """Violation response model."""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
