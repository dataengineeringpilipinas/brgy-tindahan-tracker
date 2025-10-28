"""
Compliance report model for barangay monitoring
"""

from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class ReportType(str, Enum):
    """Types of compliance reports."""
    MONTHLY = "monthly"  # Monthly compliance summary
    QUARTERLY = "quarterly"  # Quarterly compliance report
    ANNUAL = "annual"  # Annual compliance report
    ZONE_SPECIFIC = "zone_specific"  # Report for specific barangay zone
    VIOLATION_SUMMARY = "violation_summary"  # Summary of violations
    PERMIT_STATUS = "permit_status"  # Permit status report


class ComplianceMetrics(SQLModel):
    """Compliance metrics for reporting."""
    total_tindahan: int = Field(description="Total number of registered tindahan")
    compliant_tindahan: int = Field(description="Number of compliant tindahan")
    warning_tindahan: int = Field(description="Number of tindahan with warnings")
    violation_tindahan: int = Field(description="Number of tindahan with violations")
    suspended_tindahan: int = Field(description="Number of suspended tindahan")
    expired_permits: int = Field(description="Number of expired permits")
    pending_inspections: int = Field(description="Number of pending inspections")
    total_violations: int = Field(description="Total number of violations")
    resolved_violations: int = Field(description="Number of resolved violations")
    compliance_rate: float = Field(description="Overall compliance rate percentage")


class ComplianceReportBase(SQLModel):
    """Base compliance report model."""
    report_type: ReportType = Field(description="Type of report")
    report_period_start: datetime = Field(description="Start of reporting period")
    report_period_end: datetime = Field(description="End of reporting period")
    barangay_zone: Optional[str] = Field(default=None, max_length=50, description="Specific zone (if applicable)")
    generated_by: str = Field(max_length=100, description="Name of person who generated report")
    summary: str = Field(max_length=1000, description="Report summary")
    recommendations: Optional[str] = Field(default=None, max_length=1000, description="Recommendations for improvement")


class ComplianceReport(ComplianceReportBase, table=True):
    """Compliance report database model."""
    id: Optional[int] = Field(default=None, primary_key=True)
    metrics: Optional[str] = Field(default=None, description="JSON string of compliance metrics")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ComplianceReportCreate(ComplianceReportBase):
    """Compliance report creation model."""
    metrics: Optional[ComplianceMetrics] = Field(default=None)


class ComplianceReportResponse(ComplianceReportBase):
    """Compliance report response model."""
    id: int
    metrics: Optional[ComplianceMetrics]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
