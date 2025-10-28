"""
Tindahan model for barangay compliance monitoring
"""

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class BusinessType(str, Enum):
    """Types of business operations."""
    TINDAHAN = "tindahan"  # Small sari-sari store
    STREET_HAWKER = "street_hawker"  # Mobile street vendor
    PEDDLER = "peddler"  # Door-to-door seller
    FOOD_CART = "food_cart"  # Food cart vendor
    OTHER = "other"


class ComplianceStatus(str, Enum):
    """Compliance status levels."""
    COMPLIANT = "compliant"
    WARNING = "warning"
    VIOLATION = "violation"
    SUSPENDED = "suspended"


class TindahanBase(SQLModel):
    """Base tindahan model for compliance monitoring."""
    business_name: str = Field(max_length=100, description="Business/tindahan name")
    owner_name: str = Field(max_length=100, description="Owner/operator name")
    business_type: BusinessType = Field(description="Type of business operation")
    address: str = Field(max_length=200, description="Business address")
    contact_number: Optional[str] = Field(default=None, max_length=20, description="Contact number")
    barangay_zone: str = Field(max_length=50, description="Barangay zone/section")
    is_active: bool = Field(default=True, description="Whether business is currently operating")


class Tindahan(TindahanBase, table=True):
    """Tindahan database model for compliance tracking."""
    id: Optional[int] = Field(default=None, primary_key=True)
    business_permit_number: Optional[str] = Field(default=None, max_length=50, description="Barangay business permit number")
    permit_issued_date: Optional[datetime] = Field(default=None, description="Date permit was issued")
    permit_expiry_date: Optional[datetime] = Field(default=None, description="Date permit expires")
    compliance_status: ComplianceStatus = Field(default=ComplianceStatus.COMPLIANT, description="Current compliance status")
    last_inspection_date: Optional[datetime] = Field(default=None, description="Date of last inspection")
    next_inspection_due: Optional[datetime] = Field(default=None, description="Next inspection due date")
    registered_at: datetime = Field(default_factory=datetime.utcnow, description="Date registered with barangay")
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TindahanCreate(TindahanBase):
    """Tindahan registration model."""
    business_permit_number: Optional[str] = Field(default=None, max_length=50)
    permit_issued_date: Optional[datetime] = Field(default=None)
    permit_expiry_date: Optional[datetime] = Field(default=None)


class TindahanUpdate(SQLModel):
    """Tindahan update model."""
    business_name: Optional[str] = Field(default=None, max_length=100)
    owner_name: Optional[str] = Field(default=None, max_length=100)
    business_type: Optional[BusinessType] = Field(default=None)
    address: Optional[str] = Field(default=None, max_length=200)
    contact_number: Optional[str] = Field(default=None, max_length=20)
    barangay_zone: Optional[str] = Field(default=None, max_length=50)
    business_permit_number: Optional[str] = Field(default=None, max_length=50)
    permit_issued_date: Optional[datetime] = Field(default=None)
    permit_expiry_date: Optional[datetime] = Field(default=None)
    compliance_status: Optional[ComplianceStatus] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)


class TindahanResponse(TindahanBase):
    """Tindahan response model."""
    id: int
    business_permit_number: Optional[str]
    permit_issued_date: Optional[datetime]
    permit_expiry_date: Optional[datetime]
    compliance_status: ComplianceStatus
    last_inspection_date: Optional[datetime]
    next_inspection_due: Optional[datetime]
    registered_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
